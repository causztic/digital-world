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


class ShapeDetector(object):
	def __init__(self):
		pass

	def detect(self, c):
		# initialize the shape name and approximate the contour
		shape = "unidentified"
		peri = cv2.arcLength(c, True)
		approx = cv2.approxPolyDP(c, 0.04 * peri, True)

		# if the shape is a triangle, it will have 3 vertices
		if len(approx) == 3:
			shape = "triangle"

		# if the shape has 4 vertices, it is either a square or
		# a rectangle
		elif len(approx) == 4:
			# compute the bounding box of the contour and use the
			# bounding box to compute the aspect ratio
			(x, y, w, h) = cv2.boundingRect(approx)
			ar = w / float(h)

			# a square will have an aspect ratio that is approximately
			# equal to one, otherwise, the shape is a rectangle
			shape = "square" if ar >= 0.95 and ar <= 1.05 else "rectangle"

		# if the shape is a pentagon, it will have 5 vertices
		elif len(approx) == 5:
			shape = "pentagon"

		# otherwise, we assume the shape is a circle
		else:
			shape = "circle"

		# return the name of the shape
		return shape

class RawKivyCamera(Image):
    def __init__(self, capture, fps, play = False, **kwargs):
        super(RawKivyCamera, self).__init__(**kwargs)
        self.capture = capture
        self.play = play
        self.rgb = None
        Clock.schedule_interval(self.update, 1.0 / fps)

    def update(self, dt):
        if self.play:
            ret, frame = self.capture.read()
            if self.texture is None:
                self.texture = Texture.create((frame.shape[1], frame.shape[0]))
            if ret:
                # convert the resized image to grayscale, blur it slightly,
                # and threshold it
                self.frame = cv2.flip(cv2.flip(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), 0), 1)
                self.buffer = self.detect_shapes(frame)
                self.rgb = cv2.cvtColor(self.buffer, cv2.COLOR_BGR2RGB)
                self.texture.blit_buffer(self.rgb.tostring(), colorfmt='rgb', bufferfmt='ubyte')
                self.canvas.ask_update()
                self.buffer = None
    
    def detect_shapes(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if imutils.is_cv2() else cnts[1]
        sd = ShapeDetector()

        for c in cnts:
            # compute the center of the contour, then detect the name of the
            # shape using only the contour
            M = cv2.moments(c)
            cX = int((M["m10"] / (M["m00"] + 1e-7)))
            cY = int((M["m01"] / (M["m00"] + 1e-7)))
            shape = sd.detect(c)

            # multiply the contour (x, y)-coordinates by the resize ratio,
            # then draw the contours and the name of the shape on the image
            c = c.astype("float")
            c = c.astype("int")
            cv2.drawContours(frame, [c], -1, (0, 255, 0), 2)

            # cv2.putText(frame, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,
            #     0.5, (255, 255, 255), 2)
        
        return frame

    
    def analyze_photo(self, instance):
        if self.frame is not None:
            (thresh, bw_img) = cv2.threshold(self.frame, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
            txt = pytesseract.image_to_string(pil_image.fromarray(bw_img))
            print txt