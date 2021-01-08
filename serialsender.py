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
    port = '/dev/ttyUSB0'
    baud = 115200
    timeout = None
    ser = None
    connected = False
    parent = None

    def __init__(self, parent):
        super(SerialSender, self).__init__()
        self.parent = parent
        try:
            self.ser = serial.Serial(self.port,self.baud,timeout=self.timeout)
            self.connected = True
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
        for ap, _, _ in all_port_tuples:
            p = os.path.basename(ap)
            print(p)
            if p.startswith("ttyUSB") or p.startswith("ttyACM"):
                all_ports |= {ap}
                #logging.info("\t%s", str(ap))
                msg = "\t" + str(ap)
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
                break
            else:
                print(a)

    def send_command(self, cmd_param):
        if(self.connected):
            bCmd = (cmd_param + '\r').encode('utf-8')
            self.ser.write(bCmd)
            self.parent.appendOnConsole(cmd_param)
            print(bCmd)
            self.wait_complete()
            time.sleep(0.1)
        else:
            self.parent.appendOnConsole("Not connected")
