import serial
from time import sleep

class DispenseUnit_Arduino():

    def __init__(self, parent,COMPORT,*args, **kwargs):
        self.parent = parent
        self.ser = serial.Serial(COMPORT, 2000000,timeout=0.01)

    def wait_for_idle(self):
        while 1:
            self.ser.write(b'R;')
            r=self.ser.readline()
            if r==b'ready\r\n':
                break
            sleep(0.01)

    def dispense(self,volume):
        self.wait_for_idle()
        command="U"+str(volume)+";"
        self.ser.write(bytes(command,'utf-8'))

    def init(self):
        self.wait_for_idle()
        self.ser.write(b'I;')
