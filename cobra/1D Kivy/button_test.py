from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
from kivy.uix.button import Button
from kivy.uix.label import Label


class Milk(Widget):
    label_text = StringProperty()

    def __init__(self,**kwargs):
        super(Milk,self).__init__(**kwargs)
        self.count = 0
        self.label_text = str(self.count)

    def increment(self,*args):
        self.count += 1
        self.label_text = str(self.count)

    def decrement(self,*args):
        self.count -= 1
        self.label_text = str(self.count)

class Coke(Widget):
    label_text = StringProperty()

    def __init__(self,**kwargs):
        super(Coke,self).__init__(**kwargs)
        self.count = 0
        self.label_text = str(self.count)

    def increment(self,*args):
        self.count += 1
        self.label_text = str(self.count)

    def decrement(self,*args):
        self.count -= 1
        self.label_text = str(self.count)

class Items(Widget):
    pass

class ButApp(App):
    
    def build(self):
        return Items()

ButApp().run()