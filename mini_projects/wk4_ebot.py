from eBot import eBot
from time import sleep
from firebase import firebase

url = "https://ebot-ac352.firebaseio.com/" # URL to Firebase database
token = "QwU8aMuyxCQk3lNH3Lh66chvmeMjnv7kRuixeTQB" # unique token used for authentication

# Create a firebase object by specifying the URL of the database and its secret token.
# The firebase object has functions put and get, that allows user to put data onto 
# the database and also retrieve data from the database.
firebase = firebase.FirebaseApplication(url, token)

ebot = eBot.eBot() # create an eBot object
ebot.connect() # connect to the eBot via Bluetooth

# Use a variable to determine whether there is any valid movement commands in
# the Firebase database.
no_commands = True

movement_dict = {'up':[1,1],'left':[1,0],'right':[0,1],'ok':[0,0]}
while no_commands:
    # Check the value of movement_list in the database at an interval of 0.5
    # seconds. Continue checking as long as the movement_list is not in the
    # database (ie. it is None). If movement_list is a valid list, the program
    # exits the while loop and controls the eBot to perform the movements
    # specified in the movement_list in sequential order. Each movement in the
    # list lasts exactly 1 second.
    
    # Get movement list from Firebase
    #movement_list = None
    movement_list = firebase.get('/movement')
    if movement_list == None:
        ebot.wheels(0,0)
    else:
        for i in movement_list:
            #to_do = movement_list[i]
            #print to_do
            #to_do = str(to_do)
            print i
            to_do_matrix = movement_dict[i]
            ebot.wheels(to_do_matrix[0],to_do_matrix[1])
            sleep(1)
        firebase.put('/','movement',None)
        print "Ez Game"
    #sleep(0.5)
    
# Write the code to control the eBot here


ebot.disconnect() # disconnect the Bluetooth communication
