from io import BytesIO
from time import sleep
from picamera import PiCamera
from PIL import Image
import pytesseract


# Create the in-memory stream
stream = BytesIO()
camera = PiCamera(rotation=270)
camera.start_preview()
sleep(2)
camera.capture(stream, format='jpeg')
# "Rewind" the stream to the beginning so we can read its content
stream.seek(0)
camera.stop_preview()
image = Image.open(stream)
print(pytesseract.image_to_string(image))