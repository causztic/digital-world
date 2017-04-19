from firebase import firebase
from kivy.uix.widget import Widget
from kivy.uix.image  import Image
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.properties import StringProperty
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.camera import Camera
from kivy.clock import Clock
from kivy.graphics.texture import Texture

from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2

import numpy as np

url = "https://rasbpi-9b253.firebaseio.com/" # URL to Firebase database
token = "tlXOUKslj8JwDSc1ymJ1lbh8n2tkfUIZb5090xlC" # unique token used for authentication
firebase = firebase.FirebaseApplication(url, token)

class GroceryItem(RelativeLayout):

    def __init__(self,**kwargs):
        super(GroceryItem, self).__init__(**kwargs)
        self.count = 0
        acceptable_keys_list = ["count", "label_text", "name", "brand"]
        for k in kwargs.keys():
            if k in acceptable_keys_list:
                self.__setattr__(k, kwargs[k])
        # self.source = self.name+".png"
        # self.size = (150,150)
        image = Image(size=(150,150), source=self.name+".png")
        add_button = Button(size=(25,25), pos=(image.center_x+50, image.center_y), text="+")
        plus_sign = Image(size = (50,50),pos = (add_button.center_x-25,add_button.center_y-25),source = 'plus.png')
        add_button.add_widget(plus_sign)
        remove_button = Button(size=(25,25), pos=(image.center_x+50, image.center_y-75), text="-")
        minus_sign = Image(size = (50,50),pos = (remove_button.center_x-25,remove_button.center_y-25),source = 'minus.png')
        remove_button.add_widget(minus_sign)
        counter_backgrnd = Image (size=(50,50),source = 'label.png',pos =(image.center_x-65, image.center_y-87.5))
        self.counter = Label(size=(20,20),pos=(counter_backgrnd.center_x-10, counter_backgrnd.center_y-9),text=str(self.count),font_size = 30, color=(1,1,1,1))
        counter_backgrnd.add_widget(self.counter)
        image.add_widget(add_button)
        image.add_widget(remove_button)
        image.add_widget(counter_backgrnd)
        image.size_hint = (None,None)
        self.add_widget(image)
        add_button.bind(on_press = self.increment)
        remove_button.bind(on_press = self.decrement)

    def increment(self,instance):
        self.count += 1
        self.counter.text = str(self.count)
        firebase.put('/',self.name,self.counter.text)

    def decrement(self,instance):
        self.count -= 1
        self.counter.text = str(self.count)
        firebase.put('/',self.name,self.counter.text)

class KivyCamera(Image):
    def __init__(self, **kwargs):
        super(KivyCamera, self).__init__(**kwargs)
        self.camera = PiCamera()
        self.camera.resolution = (640, 480)
        self.camera.framerate = 32
        self.rawCapture = PiRGBArray(camera, size=(640, 480))
        time.sleep(0.1)
        Clock.schedule_interval(self.update, 1.0 / fps)

    def update(self, dt):
        for frame in self.camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
            # grab the raw NumPy array representing the image, then initialize the timestamp
            # and occupied/unoccupied text
            image = frame.array
        
            # show the frame
            cv2.imshow("Frame", image)
            key = cv2.waitKey(1) & 0xFF
	        # clear the stream in preparation for the next frame
            self.rawCapture.truncate(0)

            if self.texture is None:
                # Create the texture
                self.texture = Texture.create(self.camera.resolution[1], self.camera.resolution[0])
                self.texture.blit_buffer(image, colorfmt='bgr')
                self.canvas.ask_update()