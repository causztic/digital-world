from kivy.app import App
from kivy.uix.image  import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
#from ocr import OCR
from widgets import GroceryItem

list_items = ['milk','apple','chocolate','soft drinks','shrimp','steak','meat','broccoli']

class InventoryScreen(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        overall_layout = BoxLayout(orientation = 'vertical')
        topbox = BoxLayout(orientation='horizontal')
        label = Label(text='Inventory',color = (0,0,0,1),font_size=60)
        camera = Image(source = 'camera.png')
        topbox.add_widget(label)
        topbox.add_widget(camera)
        overall_layout.add_widget(topbox)
        bottom_layout = GridLayout(cols=3,spacing = 200,size_hint=(1,None))
        bottom_layout.bind(minimum_height = bottom_layout.setter('height'))
        for items in list_items:
            bottom_layout.add_widget(GroceryItem(name=items))
        root = ScrollView()
        root.add_widget(bottom_layout)
        overall_layout.add_widget(root)
        self.add_widget(overall_layout)
        

class CobraApp(App):

    def build(self):
        sm=ScreenManager()
        i_s = InventoryScreen(name='Inventory')
        sm.add_widget(i_s)
        return sm

if __name__ == '__main__':
    CobraApp().run()