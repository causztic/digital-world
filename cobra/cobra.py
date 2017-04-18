from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from widgets import GroceryItem
from ocr import OCR

list_items = ['milk', 'apple', 'chocolate','soft drinks', 'shrimp', 'steak', 'meat', 'broccoli']

Window.size = (800, 480)


class InventoryScreen(Screen):

    def __init__(self, **kwargs):
        super(InventoryScreen, self).__init__(**kwargs)
        overall_layout = BoxLayout(
            orientation='vertical', size=(800, 480), size_hint=(1, None))
        topbox = BoxLayout(orientation='horizontal',
                           height=100, size_hint=(1, None))
        label = Label(text='Inventory', color=(0, 0, 0, 1), font_size=60)
        # camera = Image(source='camera.png')
        topbox.add_widget(label)
        #topbox.add_widget(camera)
        topbox.add_widget(OCR)
        overall_layout.add_widget(topbox)
        bottom_layout = BoxLayout(orientation='horizontal')
        inventory = GridLayout(cols=3, spacing=(125, 50), size_hint=(
            None, None), padding=30, size=(800, 380))

        for items in list_items:
            inventory.add_widget(GroceryItem(name=items))
        inventory.height = inventory.minimum_height + 750
        scroller = ScrollView(size=(800, 370))
        scroller.add_widget(inventory)
        bottom_layout.add_widget(scroller)
        overall_layout.add_widget(bottom_layout)
        self.add_widget(overall_layout)


class CobraApp(App):

    def build(self):
        sm = ScreenManager()
        i_s = InventoryScreen(name='Inventory')
        sm.add_widget(i_s)
        return sm

if __name__ == '__main__':
    CobraApp().run()
