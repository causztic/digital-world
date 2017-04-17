from kivy.app import App
from kivy.uix.image  import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
#from ocr import OCR
from widgets import GroceryItem

list_items = ['milk','apple','chocolate','soft drinks','shrimp','steak','meat','broccoli']
Window.size = (800,480)
class InventoryScreen(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        overall_layout = GridLayout(rows=2)
        topbox = BoxLayout(orientation='horizontal',size_hint = (None,None))
        label = Label(text='Inventory',color = (0,0,0,1),font_size=60,size_hint=(None,None))
        camera = Image(source = 'camera.png',size_hint=(None,None),height = 100,width = 100)
        topbox.add_widget(label)
        topbox.add_widget(camera)
        overall_layout.add_widget(topbox)
        inventory = GridLayout(cols=3,spacing = (125,175),size_hint=(None,None),padding = 30)
        inventory.bind(minimum_height = inventory.setter('height'))
        for items in list_items:
            inventory.add_widget(GroceryItem(name=items))
        bottom_layout = ScrollView(size_hint=(1, 0),size=(Window.width, Window.height))
        bottom_layout.add_widget(inventory)
        overall_layout.add_widget(bottom_layout)
        self.add_widget(overall_layout)
        

class CobraApp(App):

    def build(self):
        sm=ScreenManager()
        i_s = InventoryScreen(name='Inventory')
        sm.add_widget(i_s)
        return sm

if __name__ == '__main__':
    CobraApp().run()