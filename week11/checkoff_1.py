from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):

  def build(self):
      self.mylabel = Label(text="Programming is fun", font_size=24)
      self.mylabel.bind(on_touch_down=self.alternate)
      self.state = 0
      return self.mylabel
  
  def alternate(self, instance, touch):
      if (self.state == 0):
          print "It is fun to program"
          self.mylabel.text = "It is fun to program"
          self.state = 1
      elif (self.state == 1):
          print "to red"
          self.mylabel.text = "Programming is fun"
          self.state = 0

if __name__ == '__main__':
    MyApp().run()