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

  isRelative = BooleanProperty(False)
  step = NumericProperty(1)
  console = StringProperty("")
  consoleBufferSize = 100
  consoleSize = 0

  sender = None

  def build(self):
    self.root = Rac()
    self.sender = SerialSender(self)

  def appendOnConsole(self, message):
      if (self.consoleSize < self.consoleBufferSize):
          self.console += message + '\n'
          self.consoleSize += 1
      else:
          self.console = message + '\n'
          self.consoleSize = 0

  def move_relative(self, x, y, z):
    if(self.isRelative == False):
      self.sender.send_command('G91')
      self.isRelative = True

    cmd = 'G1 X' + str(x*self.step) + ' Y' + str(y*self.step) + ' Z' + str(z*self.step)
    self.sender.send_command(cmd)

  def home(self, x, y, z):
    if(self.isRelative == True):
      self.sender.send_command('G90')
      self.isRelative = False
    if( x==1 and y ==1 and z==1):
      cmd = 'G28'
    else:
      cmd = 'G1'
      if(x == 1):
        cmd += ' X0'
      if(y == 1):
        cmd += ' Y200'
      if(z == 1):
        cmd += ' Z120'
    self.sender.send_command(cmd)

  def toggleMotors(self, toggleMottors):
    if(toggleMottors.state == 'down'):
        self.sender.send_command('M17')
    else:
        self.sender.send_command('M18')

RacApp().run()
