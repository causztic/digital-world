from io import BytesIO
from time import sleep
from PIL import Image
from kivy.uix.camera import Camera
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

import time
import pytesseract


class OCR(BoxLayout):

    def __init__(self, **kwargs):
        super(OCR, self).__init__(**kwargs)
        self.stream = BytesIO()
        self.camera = Camera(resolution=(640, 480), play=False)
        self.activate_button = Button(text="Toggle Camera", on_press=self.toggle_camera())
        self.take_photo_button = Button(text="Analyze Receipt", on_press=self.analyze_photo())
        self.add_widget(self.camera)
        self.add_widget(self.activate_button)

    def toggle_camera(self):
        self.camera.play = not self.camera.play
        if self.camera.play:
            self.add_widget(self.take_photo_button)
        else:
            self.remove_widget(self.take_photo_button)

    def analyze_photo(self):
        f = "%s.png" % time.strftime("%Y%m%d_%H%M%S")
        self.camera.export_to_png(f)
        return pytesseract.image_to_string(Image.open(f))
