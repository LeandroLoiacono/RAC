from kivy.config import Config
Config.set('graphics', 'window_state', 'maximized')
from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from serialsender import SerialSender
from kivy.properties import BooleanProperty, NumericProperty,  StringProperty


class Rac(StackLayout):
  pass

class RacXY(GridLayout):
  pass

class RacZ(GridLayout):
  pass


class RacApp(App):

  START_X = 0
  START_Y = 200
  START_Z = 120
  START_E = 0
  isRelative = BooleanProperty(False)
  step = NumericProperty(10)
  console = StringProperty("")
  consoleBufferSize = 100
  consoleSize = 0
  x = NumericProperty(0)
  y = NumericProperty(200)
  z = NumericProperty(120)
  e = NumericProperty(0)
  f = NumericProperty(1)
  customCmd = StringProperty("")
  motorsToggleState = StringProperty("normal")
  port = StringProperty("")
  ports_available = StringProperty("")


  sender = None

  def build(self):
    self.root = Rac()
    self.sender = SerialSender(self)
    self.port = self.sender.port

  def appendOnConsole(self, message):
      if (self.consoleSize < self.consoleBufferSize):
          self.console += str(message) + '\n'
          self.consoleSize += 1
      else:
          self.console = str(message) + '\n'
          self.consoleSize = 0

  def move_relative(self, x = 0.0, y = 0.0, z = 0.0, e = 0.0):
    if(self.isRelative == False):
      self.sender.send_command('G91')
      self.isRelative = True

    self.x = x
    self.y = y
    self.z = z
    self.e = e
    cmd = 'G1 X' + str(x*self.step) + ' Y' + str(y*self.step) + ' Z' + str(z*self.step) + ' E' + str(e*self.step)
    self.send_command(cmd)

  def home(self, x = 0, y = 0, z = 0, E = 0):
    if(self.isRelative == True):
      self.send_command('G90')
      self.isRelative = False
    if( x==1 and y ==1 and z==1):
      cmd = 'G28'
    else:
      cmd = 'G1'
      if(x == 1):
        cmd += ' X' + str(self.START_X)
      if(y == 1):
        cmd += ' Y' + str(self.START_Y)
      if(z == 1):
        cmd += ' Z' + str(self.START_Z)
      if(z == 1):
        cmd += ' E' + str(self.START_E)
    ret = self.send_command(cmd)
    self.updateGUI(ret)

  def toggleMotors(self, toggleMotors):
    if(toggleMotors.state == 'down'):
        self.sender.send_command('M17')
    else:
        self.sender.send_command('M18')
  
  def toggleGripper(self, toggleGripper):
    if(toggleGripper.state == 'down'):
        self.sender.send_command('M3')
    else:
        self.sender.send_command('M5')
  
  def setStep(self, step):
    self.step = float(step)
  
  def setPort(self, step):
    self.sender.port = step
    self.sender.connect()

  def send_command(self, cmd):
    msg = self.sender.send_command(cmd)
    if(msg != None):
      self.appendOnConsole(msg)

  def send_gcode(self, gcode):
    cmd = gcode.text
    ret = self.send_command(cmd)
    if(ret != 'Not connected'):
      gcode.text = ''
      self.updateGUI(ret)
      
  
  def updateGUI(self, cmd):
    print(cmd)
    if(cmd == 'M17' or cmd == 'G28' or cmd == 'm17' or cmd == 'g28'):
      self.motorsToggleState = 'down'
    if(cmd == 'M18' or cmd == 'm18'):
      self.motorsToggleState = 'normal'

RacApp().run()
