# kivy library imports
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


from kivy.clock import Clock

# python library imports
import os
import cv2
from firebase import firebase
from functools import partial

# custom imports
from widgets import GroceryItem, RawKivyCamera, ButtonWithImage

# load the video driver
os.system('sudo modprobe bcm2835-v4l2')

# instantiate firebase
url = "https://rasbpi-9b253.firebaseio.com/"
token = "tlXOUKslj8JwDSc1ymJ1lbh8n2tkfUIZb5090xlC"
firebase = firebase.FirebaseApplication(url, token)

# set a list of currently available groceries
groceries = {'milk': 0, 'apple': 0, 'chocolate': 0, 'soft drinks': 0,
             'shrimp': 0, 'steak': 0, 'chicken': 0, 'broccoli': 0}

# set default window size to suit the Pi
Window.size = (800, 480)

class InventoryScreen(Screen):
    """
        The Inventory Screen keeps track of the items in the fridge,
        along with buttons to manually update the items.
    """

    def __init__(self, **kwargs):
        super(InventoryScreen, self).__init__(**kwargs)
        self.overall_layout = BoxLayout(
            orientation='vertical', size=(800, 480), size_hint=(1, None))
        self.topbox = BoxLayout(orientation='horizontal',
                                height=100, size_hint=(1, None))
        label = Label(text='Inventory', color=(0, 0, 0, 1), font_size=60, font_name="assets/ailerons.otf")
        camera = ButtonWithImage(logo="assets/camera.png", text="Scan Receipt", on_press=self.changeScreen)
        self.topbox.add_widget(label)
        self.topbox.add_widget(camera)

        self.grocery_widgets = {}
        self.show_empty = True

        # instantiate GroceryItems with default values.
        for key, value in groceries.iteritems():
            self.grocery_widgets[key] = GroceryItem(name=key, count=value)

        self.empty_label = Label(text="", color=(0, 0, 0, 1), font_size=60)

        self.bottom_layout = BoxLayout(orientation='horizontal')
        self.inventory = GridLayout(cols=3, spacing=(125, 50), size_hint=(
            None, None), padding=30, size=(800, 380))

        #self.bind(on_pre_enter=self.update_from_server)
        self.update_from_server()

        scroller = ScrollView(size=(800, 370))
        scroller.add_widget(self.inventory)
        self.bottom_layout.add_widget(scroller)

        self.add_widget(self.overall_layout)

    def update_from_server(self, *args):
        """ Pull the data from the server and call the updating as a separate process """
        self.empty_label.text = "Loading items!"
        self.overall_layout.add_widget(self.empty_label, 1)
        # show loading message while obtaining from firebase.
        # could make it read locally but kivy is clunky
        self.inventory.clear_widgets()
        Clock.schedule_once(self.update_groceries, 3)

    def update_groceries(self, *args):
        """ Update the groceries according to Firebase. """
        # clear items to reset the addition of widgets
        self.overall_layout.clear_widgets()
        self.overall_layout.add_widget(self.topbox)
        # add the grocery item to the "fridge" if it exists on Firebase
        # add the updated value from firebase + default values instantiated
        # (used for testing) and display them.
        print firebase.get('/')
        for item, count in firebase.get('/').iteritems():
            # check if item is enabled in the application
            if groceries.has_key(item):
                total = int(count) + groceries[item]
                if (total) > 0:
                    self.show_empty = False
                    # get the relevant GroceryItem and update the data
                    self.grocery_widgets[item].count = total
                    self.inventory.add_widget(self.grocery_widgets[item])
                    self.canvas.ask_update()
        if self.show_empty:
            self.empty_label.text = "Your Fridge is empty :("
            self.overall_layout.add_widget(self.empty_label)
        else:
            # dynamically set the height of the gridlayout based
            # on the number of stuff in the inventory to prevent clipping
            self.inventory.height = 300 * len(self.inventory.children) / 3
            self.overall_layout.add_widget(self.bottom_layout)

    def changeScreen(self, *args):
        """ Changes the screen to CameraScreen. """
        self.manager.current = "Camera"


class CameraScreen(Screen):
    """ Camera Screen which allows the user to scan a receipt to add it to the inventory. """
    def __init__(self, **kwargs):
        super(CameraScreen, self).__init__(**kwargs)
        resolution = (800, 480)
        overall_layout = GridLayout(cols=2, size=resolution, size_hint=(1, None))
        right = BoxLayout(orientation="vertical")
        inventory = ButtonWithImage(logo="assets/fridge.png", on_press=self.changeScreen, size=(160, 240), full=True)

        self.capture = cv2.VideoCapture(0)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self.camera = RawKivyCamera(self.capture, 30)

        self.take_photo_button = ButtonWithImage(logo="assets/analysis.png", on_press=partial(self.camera.analyze_photo, self), size=(160, 240), full=True)

        overall_layout.add_widget(self.camera)
        right.add_widget(inventory)
        right.add_widget(self.take_photo_button)

        self.bind(on_enter=self.start_cam)
        self.bind(on_leave=self.stop_cam)
        overall_layout.add_widget(right)

        self.add_widget(overall_layout)

    def changeScreen(self, *args):
        """ Change the screen back to the InventoryScreen. """
        self.manager.current = "Inventory"
        self.manager.transition.direction = "right"

    def start_cam(self, *args):
        """ Starts the camera """
        self.camera.play = True

    def stop_cam(self, *args):
        """ Stops the camera """
        self.camera.play = False


class CobraApp(App):
    """ Main App. Instantiates the two screens needed. """
    def build(self):
        sm = ScreenManager()
        self.i_s = InventoryScreen(name='Inventory')
        self.c_s = CameraScreen(name="Camera")

        sm.add_widget(self.i_s)
        sm.add_widget(self.c_s)

        return sm

    def on_stop(self):
        """ Stops the video capture and frees the memory. """
        # without this, app will not exit even if the window is closed
        self.c_s.capture.release()

if __name__ == '__main__':
    CobraApp().run()
