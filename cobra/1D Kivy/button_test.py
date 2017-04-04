from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
from kivy.uix.button import Button
from kivy.uix.label import Label

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
    
class ButApp(App):
    
    def build(self):
        # import gridview here
        list_of_groceries = [{"name": "milk", "count": 5}, { "name": "coke", "count": "3"}]
        for grocery in list_of_groceries:
            GroceryItem(grocery)
            # for every item, add to gridview
        
        #return the gridview with the groceryitems
        return None

ButApp().run()