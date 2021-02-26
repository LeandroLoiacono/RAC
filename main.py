from kivy.config import Config
Config.set('graphics', 'window_state', 'maximized')
from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from serialsender import SerialSender
from kivy.properties import BooleanProperty, NumericProperty,  StringProperty
from kivy.core.window import Window
#from kivy.uix.widget import Widget

#from kivy.garden.joystick import Joystick


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
  step = NumericProperty(10)
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
  ready = False
  gcodeFile = ''
  wait_for_ok = False
  firmware = "Community"
  maxSpeed = 100

  isRelative = BooleanProperty(False)

  def __init__(self, **kwargs):
    super(RacApp, self).__init__(**kwargs)
    self._keyboard = Window.request_keyboard(self._keyboard_closed, self.root, 'text')
    if self._keyboard.widget:
        # If it exists, this widget is a VKeyboard object which you can use
        # to change the keyboard layout.
        pass
    self._keyboard.bind(on_key_down=self._on_keyboard_down)
  
  def _keyboard_closed(self):
    pass
    #print('RAC keyboard have been closed!')
    #self._keyboard.unbind(on_key_down=self._on_keyboard_down)
    #self._keyboard = None

  def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
    #print('The key', keycode, 'have been pressed')
    #print(' - text is %r' % text)
    #print(' - modifiers are %r' % modifiers)
    
    if keycode[1] == 'up':
      self.move_relative(0,1)
    elif keycode[1] == 'down':
      self.move_relative(0,-1)
    elif keycode[1] == 'left':
      self.move_relative(-1,0)
    elif keycode[1] == 'right':
      self.move_relative(1,0)
    if keycode[1] == 'w':
      self.move_relative(0,0,1)
    elif keycode[1] == 'a':
      self.move_relative(0,0,0,-1)
    elif keycode[1] == 's':
      self.move_relative(0,0,-1)
    elif keycode[1] == 'd':
      self.move_relative(0,0,0,1)
    
    # Keycode is composed of an integer + a string
    # If we hit escape, release the keyboard
    if keycode[1] == 'escape':
        keyboard.release()

    # Return True to accept the key. Otherwise, it will be used by
    # the system.
    return True

  def build(self):
    self.root = Rac()
    self.sender = SerialSender(self)
    self.port = self.sender.port

    
  def appendToConsole(self, message, direct = False):
    if (self.consoleSize < self.consoleBufferSize):
      if direct:
        self.root.ids.Console_txt.text += message
      else: 
        self.root.ids.Console_txt.insert_text(message)
      self.consoleSize += 1
    else:
      self.root.ids.Console_txt.insert_text(message)
      self.consoleSize = 0
      self.root.ids.Console_txt.text = ''
  
  def move_relative(self, x = 0.0, y = 0.0, z = 0.0, e = 0.0):
    if(self.isRelative == False):
      self.send_command('G91')
      self.isRelative = True
    self.x = x
    self.y = y
    self.z = z
    self.e = e
    cmd = 'G1 X' + str(x*self.step) + ' Y' + str(y*self.step) + ' Z' + str(z*self.step) + ' E' + str(e*self.step) + ' F' + str(self.f)
    self.send_command(cmd)
    
  def home(self, x = 0, y = 0, z = 0, e = 0):
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
      if(e == 1):
          cmd += ' E' + str(self.START_E)
      ret = self.send_command(cmd)
      if(ret != False):
        self.updateGUI(cmd)
    
  def setFeedRate(self, feedRate):
    if(feedRate != self.f):
      self.f = feedRate
      self.send_command('G1 F' + str(self.f))

  def toggleMotors(self, toggleMotors):
    if(toggleMotors.state == 'down'):
      self.send_command('M17')
    else:
      self.send_command('M18')
  
  def toggleGripper(self, toggleGripper):
    if(toggleGripper.state == 'down'):
      self.send_command('M3')
    else:
      self.send_command('M5')

  def toggleWaitOK(self, toggleWaitOK):
    if(toggleWaitOK.state == 'down'):
      self.wait_for_ok = True
    else:
      self.wait_for_ok = False

  def setStep(self, step):
    self.step = float(step)
  
  def setFirmware(self, firmware):
    self.firmware = firmware
    if(self.firmware == "Community"):
      self.maxSpeed = 100
      self.wait_for_ok = True
    else:
      self.maxSpeed = 3000
      self.wait_for_ok = False
  
  def setPort(self, step):
    self.sender.port = step
    self.sender.connect()
  
  def checkPorts(self):
    self.sender.serial_ports()

  def send_command(self, cmd):
    self.appendToConsole(cmd + '\r\n')
    ret = self.sender.send_command(cmd)
    return ret

  def send_gcode(self, gcode):
    if(gcode != ''):
      cmd = gcode.text
      ret = self.send_command(cmd)
      if(ret != False):
        gcode.text = ''
        self.updateGUI(ret)
       
  def updateGUI(self, cmd):
    if(cmd == 'M17' or cmd == 'G28' or cmd == 'm17' or cmd == 'g28'):
      self.motorsToggleState = 'down'
    if(cmd == 'M18' or cmd == 'm18'):
      self.motorsToggleState = 'normal'

  def on_request_close(self):
    self.sender.close()
  
  def runFile(self):
    if(self.gcodeFile != ''):
      self.send_gcode('M17')
      self.send_command('G90')
      self.isRelative = False
      self.sender.run_file(self.gcodeFile)

RacApp().run()
