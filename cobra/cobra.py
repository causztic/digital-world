from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.core.window import Window
from widgets import GroceryItem, CamItem, KivyCamera

import cv2

list_items = ['milk', 'apple', 'chocolate',
              'soft drinks', 'shrimp', 'steak', 'meat', 'broccoli']

Window.size = (800, 480)
Window.clearcolor = (1, 1, 1, 1)

class InventoryScreen(Screen):

    def __init__(self, **kwargs):
        super(InventoryScreen, self).__init__(**kwargs)
        overall_layout = BoxLayout(
            orientation='vertical', size=(800, 480), size_hint=(1, None))
        topbox = BoxLayout(orientation='horizontal',
                           height=100, size_hint=(1, None))
        label = Label(text='Inventory', color=(0, 0, 0, 1), font_size=60)
        camera = Button(text="Change to Camera", on_press=self.changeScreen)
        topbox.add_widget(label)
        topbox.add_widget(camera)
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

    def changeScreen(self,*args):
        self.manager.current = "Camera"


class CameraScreen(Screen):

    def __init__(self, **kwargs):
        super(CameraScreen, self).__init__(**kwargs)
        resolution = (800, 480)
        overall_layout = BoxLayout(
            orientation='vertical', size=resolution, size_hint=(1, None))
        topbox = BoxLayout(orientation='horizontal',
                           height=100, size_hint=(1, None))
        label = Label(text='Camera', color=(0, 0, 0, 1), font_size=60)
        inventory = Button(text="Change to Inventory", on_press=self.changeScreen)

        topbox.add_widget(label)
        topbox.add_widget(inventory)
        overall_layout.add_widget(topbox)

        self.capture = cv2.VideoCapture(0)
        self.capture.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, resolution[0])
        self.capture.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, resolution[1])
        self.my_camera = KivyCamera(capture=self.capture, fps=30)

        overall_layout.add_widget(self.my_camera)
        self.add_widget(overall_layout)

    def changeScreen(self, *args):
        self.manager.current = "Inventory"

class CobraApp(App):

    def build(self):
        sm = ScreenManager()
        self.i_s = InventoryScreen(name='Inventory')
        self.c_s = CameraScreen(name="Camera")

        sm.add_widget(self.i_s)
        sm.add_widget(self.c_s)

        return sm

    def on_stop(self):
        #without this, app will not exit even if the window is closed
        self.c_s.capture.release()

if __name__ == '__main__':
    CobraApp().run()
