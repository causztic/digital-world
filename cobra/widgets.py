from kivy.uix.widget import Widget
from kivy.uix.image  import Image
from kivy.uix.button import Button
from kivy.properties import StringProperty

class GroceryItem(Widget):
    label_text = StringProperty()

    def __init__(self,**kwargs):
        super(GroceryItem, self).__init__(**kwargs)
        self.count = 0
        acceptable_keys_list = ["count", "label_text", "name", "brand"]
        for k in kwargs.keys():
            if k in [acceptable_keys_list]:
                self.__setattr__(k, kwargs[k])
    
    def increment(self):
        self.count += 1
        self.label_text = str(self.count)

    def decrement(self):
        self.count -= 1
        self.label_text = str(self.count)

    def build(self):
        image = Image(size=(300,300), source=self.name+".png")
        add_button = Button(size=(50,50), pos=(image.center_x+100, image.center_y-100), text="+", on_press=(self.increment()))
        remove_button = Button(size=(50,50), pos=(image.center_x+100, image.center_y-100), text="+", on_press=(self.decrement()))
        image.add_widget(add_button)
        image.add_widget(remove_button)
        self.add_widget(image)
        return self