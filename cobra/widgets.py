from kivy.uix.widget import Widget
from kivy.properties import StringProperty

class GroceryItem(Widget):
    label_text = StringProperty()

    def __init__(self,**kwargs):
        super(GroceryItem, self).__init__(**kwargs)
        acceptable_keys_list = ["count", "label_text", "name", "brand"]
        for k in kwargs.keys():
            if k in [acceptable_keys_list]:
                self.__setattr__(k, kwargs[k])
        
        # add image to GroceryItem
        # add + and - button to GroceryItem
        # add callbacks to GroceryItem
    
    def increment(self):
        self.count += 1
        self.label_text = str(self.count)

    def decrement(self):
        self.count -= 1
        self.label_text = str(self.count)