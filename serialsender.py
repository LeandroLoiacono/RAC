#import glob
import serial
import time
import sys
import os
import threading

from serial.tools import list_ports

colorPickZ = -63
waterPickZ = -35
waterCleanZ = 0

blackX = -220
blackY = 70
waterX = -220
waterY = 150

class SerialSender():
    port = ''
    baud = 115200
    timeout = 1
    ser = None
    connected = False
    parent = None
    ports_available = ""
    waiting_operation = False
    buffer = []
    bufferSize = 15
    readingThread = None

    def __init__(self, parent, **kwargs):
        super(SerialSender, self).__init__(**kwargs)
        self.parent = parent
        self.serial_ports()

    def connect(self):
        try:
            msg = 'Trying to connect to port ' + self.port + '\r\n'
            self.parent.appendToConsole(msg, True)
            self.ser = serial.Serial(self.port,self.baud,timeout=self.timeout)
            self.connected = True
            msg = 'Connected!\r\n'
            self.parent.appendToConsole(msg,True)
            self.readingThread = threading.Thread(target=self.read_serial_stream)
            if(not self.readingThread.isAlive()):
                self.readingThread.setDaemon(True)
                self.readingThread.start()
        except (OSError, serial.SerialException):
            msg = "Serial port not available, please chose a different one\r\n"
            self.parent.appendToConsole(msg, True)
            self.serial_ports()
        time.sleep(2)

    def serial_ports(self):
        all_port_tuples = list_ports.comports()
        #logging.info("listing serial ports")
        msg = "listing serial ports\n"
        #print(msg)
        self.parent.appendToConsole(msg)
        all_ports = set()
        i = 0
        for ap, _, _ in all_port_tuples:
            p = os.path.basename(ap)
            if p.startswith("ttyUSB") or p.startswith("ttyACM") or p.startswith("cu."):
                all_ports |= {ap}
                msg = str(ap)
                if(self.ports_available != ""):
                    self.ports_available += ","
                self.parent.ports_available = msg
                if(i == 0):
                    self.port = msg
                i = i + 1
                msg = "\t" + msg + "\n"
                self.parent.appendToConsole(msg)

        if len(all_ports) == 0:
            #logging.error("No valid port detected!. Possibly, device not plugged/detected.")
            msg = "No valid port detected!. Possibly, device not plugged/detected.\n"
            #print(msg)
            self.parent.appendToConsole(msg)
            #raise NoValidPortError()

        elif len(all_ports) > 2:
            #logging.info("Several port detected, using first one: %s", str(all_ports))
            msg = "Several port detected, using first one: " + ",".join(all_ports) + "\n"
            #print(msg)
            self.parent.appendToConsole(msg)
        #return all_ports.pop()

    def read_serial_stream(self):
        while True:
            can_execute =  not self.waiting_operation
            a = self.ser.readline()
            if(a != None and a != b'' and a != ''):
                msg = a.decode("utf-8")
                if("ok" not in msg):
                    self.parent.appendToConsole(msg)
                else:
                    #print("ok received")
                    can_execute = True
            elif(not self.parent.wait_for_ok):
                can_execute = True
            time.sleep(0.1)
            if(can_execute):
                if(len(self.buffer) > 0):
                    cmd = self.buffer.pop(0)
                    self.send_command(cmd, True)
                else:
                    self.waiting_operation = False
       
    def send_command(self, cmd_param, is_buffer = False):
        if(not self.connected):
            self.parent.appendToConsole("Not connected\r\n")
            return False
        if(is_buffer or not self.waiting_operation):
            try:
                bCmd = (cmd_param + '\r').encode('utf-8')
                self.waiting_operation = True
                self.ser.write(bCmd)
            except (OSError, serial.SerialException):
                msg = "Serial write failure, check connection\n"
                #print(msg)
                self.parent.appendToConsole(msg)
            return True
        else:
            if(len(self.buffer) < self.bufferSize):
                self.buffer.append(cmd_param)
            else:
                #print("overbuffer")
                self.parent.appendToConsole("Commands Buffer full, exceeding commands will be ignored\n")
           
    
    def run_file(self, filename):
        with open(filename) as fp: 
            for line in fp: 
                cmd = line.split('(')[0].strip();
                if(cmd != '%' and len(cmd) > 0 and cmd[0] != ';' and cmd[0] != '('):
                    self.send_command(cmd)
