#import glob
import serial
import time
import sys
import os
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
    timeout = None
    ser = None
    connected = False
    parent = None
    ports_available = ""

    def __init__(self, parent):
        super(SerialSender, self).__init__()
        self.parent = parent
        self.serial_ports()
        #self.connect()

    def connect(self):
        try:
            msg = "Trying to connect to port " + self.port
            print(msg)
            self.parent.appendOnConsole(msg)
            self.ser = serial.Serial(self.port,self.baud,timeout=self.timeout)
            self.connected = True
            msg = "Connected!"
            print(msg)
            self.parent.appendOnConsole(msg)
        except (OSError, serial.SerialException):
            msg = "Serial port not available, please chose a different one"
            print(msg)
            self.parent.appendOnConsole(msg)
            self.serial_ports()
        time.sleep(2)

    def serial_ports(self):
        all_port_tuples = list_ports.comports()
        #logging.info("listing serial ports")
        msg = "listing serial ports"
        print(msg)
        self.parent.appendOnConsole(msg)
        all_ports = set()
        i = 0
        for ap, _, _ in all_port_tuples:
            p = os.path.basename(ap)
            print(p)
            if p.startswith("ttyUSB") or p.startswith("ttyACM"):
                all_ports |= {ap}
                #logging.info("\t%s", str(ap))
                msg = str(ap)
                if(self.ports_available != ""):
                    self.ports_available += ","
                self.parent.ports_available = msg
                if(i == 0):
                    self.port = msg
                i = i + 1
                msg = "\t" + msg
                print(msg)
                self.parent.appendOnConsole(msg)

        if len(all_ports) == 0:
            #logging.error("No valid port detected!. Possibly, device not plugged/detected.")
            msg = "No valid port detected!. Possibly, device not plugged/detected."
            print(msg)
            self.parent.appendOnConsole(msg)
            #raise NoValidPortError()

        elif len(all_ports) > 2:
            #logging.info("Several port detected, using first one: %s", str(all_ports))
            msg = "Several port detected, using first one: " + ",".join(all_ports)
            print(msg)
            self.parent.appendOnConsole(msg)
        #return all_ports.pop()



    def wait_complete(self):
        waitstatus = 1
        while True:
            a = self.ser.readline()
            if "ok" in a.decode("utf-8"):
                waitstatus = 0
                return None
            else:
                return a

    def send_command(self, cmd_param):
        if(self.connected):
            bCmd = (cmd_param + '\r').encode('utf-8')
            self.ser.write(bCmd)
            #print(bCmd)
            ret = self.wait_complete()
            time.sleep(0.1)
            return ret
        else:
            return "Not connected"
    
    #def set_port(self, port):
    #    self.port = port
    #    self.connect()
