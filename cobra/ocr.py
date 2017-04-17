from io import BytesIO
from time import sleep
from PIL import Image
from kivy.uix.camera import Camera

import time
import pytesseract


class OCR(object):

    def __init__(self, rotation):
        self.stream = BytesIO()
        self.play = False
        self.camera = Camera(resolution=(640, 480), play=self.play)

    def toggle_camera(self):
        self.play = not self.play

    def analyze_photo(self):
        f = "%s.png" % time.strftime("%Y%m%d_%H%M%S")
        self.camera.export_to_png(f)
        return pytesseract.image_to_string(Image.open(f))
