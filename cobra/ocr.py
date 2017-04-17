from io import BytesIO
from time import sleep
from picamera import PiCamera
from PIL import Image
import pytesseract


class OCR(object):

    def __init__(self, rotation):
        self.camera = PiCamera()
        self.camera.rotation = rotation
        self.stream = BytesIO()

    def take_photo(self):
        self.camera.start_preview()
        sleep(2)
        self.camera.capture(stream, format='jpeg')
        # "Rewind" the stream to the beginning so we can read its content
        stream.seek(0)
        self.camera.stop_preview()
        image = Image.open(stream)
        return pytesseract.image_to_string(image)
