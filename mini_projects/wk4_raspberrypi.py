import RPi.GPIO as GPIO
from time import sleep
from firebase import firebase

url = "https://ebot-ac352.firebaseio.com/" # URL to Firebase database
token = "QwU8aMuyxCQk3lNH3Lh66chvmeMjnv7kRuixeTQB" # unique token used for authentication

# Create a firebase object by specifying the URL of the database and its secret token.
# The firebase object has functions put and get, that allows user to put data onto 
# the database and also retrieve data from the database.
firebase = firebase.FirebaseApplication(url, token)

# Use the BCM GPIO numbers as the numbering scheme
GPIO.setmode(GPIO.BCM)

# Use GPIO12, 16, 20 and 21 for the buttons.
buttons = {'ok': 12, 'left': 16, 'up': 20, 'right': 21}

# Set GPIO numbers in the list: [12, 16, 20, 21] as input with pull-down resistor.
GPIO.setup(buttons.values(), GPIO.IN, GPIO.PUD_DOWN)

# Keep a list of the expected movements that the eBot should perform sequentially.
movement_list = []

done = False

while not done:
    # Check each button to determine whether any of them has been pressed. If
    # the OK button is pressed, the program exits the while loop and writes the
    # movement_list to the Firebase database. If any of the directional buttons
    # are pressed, the commands should be stored in the movement_list.
    if buttons['left'] == GPIO.High:
        movement_list.append('left')
        print 'left'
    if buttons['up'] == GPIO.High:
        movement_list.append('up')
        print 'up'
    if buttons['right'] == GPIO.High:
        movement_list.append('right')
        print 'right'
    if buttons['ok'] == GPIO.High:
        print 'Execute'
        firebase.put('/','movement',movement_list)
        movement_list = []
    sleep(0.1)
    # Write your code here
    pass


# Write to database once the OK button is pressed

