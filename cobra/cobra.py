from firebase import firebase
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

import os
import cv2
from widgets import GroceryItem, RawKivyCamera

# load the video driver
os.system('sudo modprobe bcm2835-v4l2')

Window.clearcolor = (1, 1, 1, 1)

url = "https://rasbpi-9b253.firebaseio.com/"  # URL to Firebase database
# unique token used for authentication
token = "tlXOUKslj8JwDSc1ymJ1lbh8n2tkfUIZb5090xlC"
firebase = firebase.FirebaseApplication(url, token)

list_items = ['milk', 'apple', 'chocolate', 'soft drinks',
              'shrimp', 'steak', 'chicken', 'broccoli']
Window.size = (800, 480)


class InventoryScreen(Screen):

    def __init__(self, **kwargs):
        super(InventoryScreen, self).__init__(**kwargs)
        overall_layout = BoxLayout(
            orientation='vertical', size=(800, 480), size_hint=(1, None))
        topbox = BoxLayout(orientation='horizontal',
                           height=100, size_hint=(1, None))
        label = Label(text='Inventory', color=(0, 0, 0, 1), font_size=60)
        camera = Button(text="Scan Receipt", on_press=self.changeScreen)
        topbox.add_widget(label)
        topbox.add_widget(camera)
        overall_layout.add_widget(topbox)
        bottom_layout = BoxLayout(orientation='horizontal')
        inventory = GridLayout(cols=3, spacing=(125, 50), size_hint=(
            None, None), padding=30, size=(800, 380))

        show_empty = True
        for item, count in firebase.get('/').iteritems():
            if int(count) != 0:
                show_empty = False
                inventory.add_widget(GroceryItem(name=item, count=count))

        if show_empty:
            overall_layout.add_widget(
                Label(text="Your fridge is empty.. :(", color=(0, 0, 0, 1), font_size=60))
        else:
            inventory.height = inventory.minimum_height + 750
            scroller = ScrollView(size=(800, 370))
            scroller.add_widget(inventory)
            bottom_layout.add_widget(scroller)
            overall_layout.add_widget(bottom_layout)

        self.add_widget(overall_layout)

    def changeScreen(self, *args):
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
        inventory = Button(text="Change to Inventory",
                           on_press=self.changeScreen)

        topbox.add_widget(label)
        topbox.add_widget(inventory)
        overall_layout.add_widget(topbox)

        bottom = BoxLayout(orientation="horizontal")
        self.capture = cv2.VideoCapture(0)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self.camera = RawKivyCamera(self.capture, 30)
        self.take_photo_button = Button(
            text="Analyze Receipt", on_press=self.camera.analyze_photo)

        bottom.add_widget(self.camera)
        bottom.add_widget(self.take_photo_button)

        self.bind(on_enter=self.start_cam)
        self.bind(on_leave=self.stop_cam)
        overall_layout.add_widget(bottom)

        self.add_widget(overall_layout)

    def changeScreen(self, *args):
        self.manager.current = "Inventory"

    def start_cam(self, *args):
        self.camera.play = True
    
    def stop_cam(self, *args):
        self.camera.play = False

class CobraApp(App):

    def build(self):
        sm = ScreenManager()
        self.i_s = InventoryScreen(name='Inventory')
        self.c_s = CameraScreen(name="Camera")

        sm.add_widget(self.i_s)
        sm.add_widget(self.c_s)

        return sm

    def on_stop(self):
        # without this, app will not exit even if the window is closed
        self.c_s.capture.release()

if __name__ == '__main__':
    CobraApp().run()
