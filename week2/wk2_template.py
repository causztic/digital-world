# Import eBot and time module
from eBot import eBot
from time import sleep
from week2_hw import celsius_to_fahrenheit

def forward(speed, duration):
    ebot.wheels(speed, speed)
    sleep(duration)
    ebot.halt()
    
def print_temperature():
    c = ebot.temperature()
    f = celsius_to_fahrenheit(c)
    print "The temperature in Celsius is %.3f and Fahrenheit is %.3f" % (c, f)

ebot = eBot.eBot() # create an eBot object
ebot.connect() # connect to the eBot via Bluetooth

############### Start writing your code here ################ 
speed = float(raw_input("Enter forward throttle speed: "))
duration = float(raw_input("Enter duration: "))
forward(speed, duration)
print_temperature()

########################## end ############################## 

ebot.disconnect() # disconnect the Bluetooth communication
