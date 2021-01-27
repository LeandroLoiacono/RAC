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

    def __init__(self, parent):
        super(SerialSender, self).__init__()
        self.parent = parent
        self.serial_ports()
        #self.connect()

    def connect(self):
        try:
            msg = 'Trying to connect to port ' + self.port + '\r\n'
            self.parent.appendOnConsole(msg, True)
            self.ser = serial.Serial(self.port,self.baud,timeout=self.timeout)
            self.connected = True
            msg = 'Connected!\r\n'
            self.parent.appendOnConsole(msg,True)
            while self.connected:
                a = self.ser.readline()
                if(a != None and a != b'' and a != ''):
                    msg = a.decode("utf-8")
                    self.parent.appendOnConsole(msg, True)
                else:
                    break
            time.sleep(0.1)
        except (OSError, serial.SerialException):
            msg = "Serial port not available, please chose a different one\r\n"
            self.parent.appendOnConsole(msg, True)
            self.serial_ports()
        time.sleep(2)

    def serial_ports(self):
        all_port_tuples = list_ports.comports()
        #logging.info("listing serial ports")
        msg = "listing serial ports\n"
        #print(msg)
        self.parent.appendOnConsole(msg)
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
                self.parent.appendOnConsole(msg)

        if len(all_ports) == 0:
            #logging.error("No valid port detected!. Possibly, device not plugged/detected.")
            msg = "No valid port detected!. Possibly, device not plugged/detected.\n"
            #print(msg)
            self.parent.appendOnConsole(msg)
            #raise NoValidPortError()

        elif len(all_ports) > 2:
            #logging.info("Several port detected, using first one: %s", str(all_ports))
            msg = "Several port detected, using first one: " + ",".join(all_ports) + "\n"
            #print(msg)
            self.parent.appendOnConsole(msg)
        #return all_ports.pop()

    def wait_complete(self):
        while True:
            a = self.ser.readline()
            if("ok" not in a.decode("utf-8")):
                msg = a.decode("utf-8")
                self.parent.appendOnConsole(msg)
            else:
                break
        time.sleep(0.1)
       
    def send_command(self, cmd_param):
        if(self.connected):
            try:
                bCmd = (cmd_param + '\r').encode('utf-8')
                self.ser.write(bCmd)
                ret = self.ser.readline()
                #print('ret: ' + str(ret))
                self.parent.appendOnConsole(ret.decode("utf-8"))
                #print(bCmd)
                threading.Thread(target=self.wait_complete).start()
            except (OSError, serial.SerialException):
                msg = "Serial write failure, check connection\n"
                #print(msg)
                self.parent.appendOnConsole(msg)
            return True
        else:
            self.parent.appendOnConsole("Not connected\r\n")
            return False
    
    def run_file(self, filename):
        with open(filename) as fp: 
            for line in fp: 
                cmd = line.split('(')[0].strip();
                if(cmd != '%' and len(cmd) > 0 and cmd[0] != ';' and cmd[0] != '('):
                    self.send_command(cmd)

    
    #def set_port(self, port):
    #    self.port = port
    #    self.connect()
