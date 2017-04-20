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
from fuzzywuzzy import process

import cv2
import imutils
import time
import pytesseract
import numpy as np

url = "https://rasbpi-9b253.firebaseio.com/" # URL to Firebase database
token = "tlXOUKslj8JwDSc1ymJ1lbh8n2tkfUIZb5090xlC" # unique token used for authentication
firebase = firebase.FirebaseApplication(url, token)

""" Base GroceryItem Widget to show the items in the fridge."""
class GroceryItem(RelativeLayout):

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        # validate to not allow it to go to negative.
        if value >= 0:
            self._count = value
            if self.counter is not None:
                self.counter.text = str(self.count)
            self.remove_button.opacity = 1
        else:
            self.remove_button.opacity = 0

    def __init__(self, **kwargs):
        super(GroceryItem, self).__init__(**kwargs)

        # set None for counter label first for instantiation of count.
        self.counter = None

        acceptable_keys_list = ["count", "label_text", "name", "brand"]
        for k in kwargs.keys():
            if k in acceptable_keys_list:
                self.__setattr__(k, kwargs[k])
        # self.source = self.name+".png"
        # self.size = (150,150)

        image = Image(size=(150,150), source="assets/" + self.name+".png")
        counter_backgrnd = Image (size=(50,50),source = 'assets/label.png',pos =(image.center_x-65, image.center_y-87.5))
        self.counter = Label(size=(20,20),pos=(counter_backgrnd.center_x-10, counter_backgrnd.center_y-9),text=str(self.count),font_size = 30, color=(1,1,1,1))
        
        add_button = Button(size=(25,25), pos=(image.center_x+50, image.center_y), text="+")
        plus_sign = Image(size = (50,50),pos = (add_button.center_x-25,add_button.center_y-25),source = 'assets/plus.png')
        add_button.add_widget(plus_sign)
        self.remove_button = Button(size=(25,25), pos=(image.center_x+50, image.center_y-75), text="-")
        minus_sign = Image(size = (50,50),pos = (remove_button.center_x-25,remove_button.center_y-25),source = 'assets/minus.png')
        self.remove_button.add_widget(minus_sign)
        counter_backgrnd.add_widget(self.counter)
        image.add_widget(add_button)
        image.add_widget(self.remove_button)
        image.add_widget(counter_backgrnd)
        image.size_hint = (None,None)
        self.add_widget(image)
        add_button.bind(on_press = self.increment)
        self.remove_button.bind(on_press = self.decrement)

    def increment(self,instance):
        self.count = self.count + 1
        self.counter.text = str(self.count)
        firebase.put('/',self.name,self.counter.text)

    def decrement(self,instance):
        self.count = self.count - 1
        self.counter.text = str(self.count)
        firebase.put('/',self.name,self.counter.text)


"""
    ShapeDetector from http://www.pyimagesearch.com/2016/02/08/opencv-shape-detection/
"""
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

"""
    Custom Camera class instead of using Kivy Camera because Kivy Camera has a memory leak on Raspberry Pi,
    in addition to exposing the matrix to perform operations on the image frame.
"""

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
                # flip the image correctly to detect shapes and to analyze in the future
                self.frame = cv2.flip(cv2.flip(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), 0), 1)
                self.buffer = self.detect_shapes(frame)
                self.rgb = cv2.cvtColor(self.buffer, cv2.COLOR_BGR2RGB)
                self.texture.blit_buffer(self.rgb.tostring(), colorfmt='rgb', bufferfmt='ubyte')
                self.canvas.ask_update()
                self.buffer = None
    
    """
        Function to draw contours around shapes to detect the receipt object.
        http://www.pyimagesearch.com/2016/02/08/opencv-shape-detection/
        Add a slight error case to M["m00"] to prevent it from division by zero.BufferError
    """
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

    """ 
        Analyzes the photo with OpenCV, PyTesseract and FuzzyWuzzy.
        Converts the image from BGR to grayscale and add a threshold to increase the accuracy.
        Afterwards, matches the scanned lines to the available choices and adds them to the item count.
    """

    def analyze_photo(self, screen, instance):
        if self.frame is not None:
            gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
            (thresh, bw_img) = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
            txt = pytesseract.image_to_string(pil_image.fromarray(bw_img))
            print txt
            choices = { "milk": ["HL", "Milk"], "chocolate": ["Crunchie", "Hershey"], "apple": ["Apple", "Fuji Apple"], "broccoli": ["Broccoli"],  "chicken": ["Chicken"], "soft drinks": ["Coca-Cola"] }
            all_values = [item for sublist in choices.values() for item in sublist]
            for line in txt.split("\n"):
                match = process.extractOne(line, all_values)
                # match[0] is value, match[1] is score
                if match is not None:
                    if match[1] > 50:
                        for k, v in choices.iteritems():
                            if match[0] in v:
                                # add the count to the inventory
                                c = screen.manager.get_screen("Inventory").grocery_widgets[k].count
                                screen.manager.get_screen("Inventory").grocery_widgets[k].count += 1
                                firebase.put('/', k, str(c + 1))
                                print "%s matches %s" % (line, k)
                                break