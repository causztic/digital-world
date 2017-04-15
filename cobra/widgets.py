from kivy.uix.widget import Widget
from kivy.uix.image  import Image
from kivy.uix.button import Button
from kivy.properties import StringProperty
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class GroceryItem(Widget):

    def __init__(self,**kwargs):
        super(GroceryItem, self).__init__(**kwargs)
        self.count = 0
        acceptable_keys_list = ["count", "label_text", "name", "brand"]
        for k in kwargs.keys():
            if k in acceptable_keys_list:
                self.__setattr__(k, kwargs[k])
        image = Image(size=(200,200), source=self.name+".png")
        add_button = Button(size=(25,25), pos=(image.center_x+100, image.center_y), text="+")
        plus_sign = Image(size = (50,50),pos = (add_button.center_x-25,add_button.center_y-25),source = 'plus.png')
        add_button.add_widget(plus_sign)
        remove_button = Button(size=(25,25), pos=(image.center_x+100, image.center_y-75), text="-")
        minus_sign = Image(size = (50,50),pos = (remove_button.center_x-25,remove_button.center_y-25),source = 'minus.png')
        remove_button.add_widget(minus_sign)
        counter_backgrnd = Image (size=(50,50),source = 'label.png',pos =(image.center_x-100, image.center_y-75))
        self.counter = Label(size=(20,20),pos=(counter_backgrnd.center_x-9, counter_backgrnd.center_y-6.25),text='0',font_size = 30, color=(1,1,1,1))
        counter_backgrnd.add_widget(self.counter)
        image.add_widget(add_button)
        image.add_widget(remove_button)
        image.add_widget(counter_backgrnd)
        self.add_widget(image)
        image.size_hint = (None,None)
        add_button.bind(on_press = self.increment)
        remove_button.bind(on_press = self.decrement)

    def increment(self,instance):
        self.count += 1
        self.counter.text = str(self.count)

    def decrement(self,instance):
        self.count -= 1
        self.counter.text = str(self.count)