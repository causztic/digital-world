import RPi.GPIO as GPIO
from time import sleep
from firebase import firebase

url = "https://rasbpi-9b253.firebaseio.com/"
token = "tlXOUKslj8JwDSc1ymJ1lbh8n2tkfUIZb5090xlC"

# Create a firebase object by specifying the URL of the database and its secret token.
# The firebase object has functions put and get, that allows user to put data onto 
# the database and also retrieve data from the database.
firebase = firebase.FirebaseApplication(url, token)

GPIO.setmode(GPIO.BCM)
ledcolor={'yellow':23, 'red':24}

GPIO.setup(ledcolor.values(), GPIO.OUT)

while True:
    redlight = firebase.get('/redlight')
    yellowlight = firebase.get('/yellight')
    
    if redlight == "on":
        GPIO.output(ledcolor["red"], GPIO.HIGH)
    else:
        GPIO.output(ledcolor["red"], GPIO.LOW)
    
    if yellowlight == "on":
        GPIO.output(ledcolor["yellow"], GPIO.HIGH)
    else:
        GPIO.output(ledcolor["yellow"], GPIO.LOW)
    
    sleep (3)


