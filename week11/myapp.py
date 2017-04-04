from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):

  def build(self):
      self.mylabel = Label(text="Hello World", color=(1,0,0,1), font_size=24)
      self.mylabel.bind(on_touch_down=self.callback)
      self.state = 0
      return self.mylabel
  
  def callback(self, instance, touch):
      if (self.state == 0):
          print "to blue"
          self.mylabel.color = (0,0,1,1)
          self.state = 1
      elif (self.state == 1):
          print "to red"
          self.mylabel.color = (1,0,0,1)
          self.state = 0

if __name__ == '__main__':
    MyApp().run()