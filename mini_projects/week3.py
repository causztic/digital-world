import RPi.GPIO as GPIO
from time import sleep

# Use the BCM GPIO numbers as the numbering scheme
GPIO.setmode(GPIO.BCM)

# Use GPIO23 for LED 1, GPIO24 for LED 2 and GPIO18 for switch
led = [23, 24]
switch = 18

# Set the GPIO23 and GPIO24 as output.
GPIO.setup(led, GPIO.OUT)

# Set the GPIO18 as input with a pull-down resistor.
GPIO.setup(switch, GPIO.IN, GPIO.PUD_DOWN)

def blink(gpio_number, duration):
    blink = True
    '''This function takes in two input: gpio_number and duration. The
    gpio_number specifies the GPIO number which the LED (to be blinked) is
    connected to. The duration is the blink interval in seconds.'''
    GPIO.output(gpio_number, blink)
    blink ^= True
    sleep(duration)

while True:
    # Check whether the switch is closed or opened. When the switch is closed,
    # turn off the LED at GPIO24 and blink the LED at GPIO23. When the switch
    # is opened, turn off the LED at GPIO23 and blink the LED at GPIO24. The
    # blink interval should be 1 second.
    if GPIO.input(switch) == GPIO.HIGH:
        GPIO.output(led[1], False)
        blink(led[0], 1)
    else:
        GPIO.output(led[0], False)
        blink(led[1], 1)
