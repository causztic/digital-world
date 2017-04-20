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

from kivy.clock import Clock
from kivy.graphics.texture import Texture
from PIL import Image as pil_image


import cv2
import imutils
import time
import pytesseract
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

class RawKivyCamera(Image):
    def __init__(self, capture, fps, play = False, **kwargs):
        super(RawKivyCamera, self).__init__(**kwargs)
        self.capture = capture
        self.play = play
        self.th = None
        Clock.schedule_interval(self.update, 1.0 / fps)

    def update(self, dt):
        if self.play:
            ret, frame = self.capture.read()
            if self.texture is None:
                self.texture = Texture.create((frame.shape[1], frame.shape[0]))
            if ret:
                # convert the resized image to grayscale, blur it slightly,
                # and threshold it
                self.buffer = frame
                self.texture.blit_buffer(cv2.cvtColor(self.buffer, cv2.COLOR_BGR2RGB).tostring(), colorfmt='rgb', bufferfmt='ubyte')
                self.th = self.outline(frame)
                self.canvas.ask_update()
                self.buffer = None

    def analyze_photo(self, instance):
        if self.th is not None:
            txt = pytesseract.image_to_string(pil_image.fromarray(self.th))
            print txt

    def outline(self, frame):
        gray = cv2.cvtColor(frame.flip(0), cv2.COLOR_BGR2GRAY)
        th = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)
        return th