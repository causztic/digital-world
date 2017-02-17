from firebase import firebase

url = "https://digital-world-554eb.firebaseio.com" # URL to Firebase database
token = "677hPadAZ685TPibchhfuouSBvn7cXXtAAid1512" # unique token used for authentication

# Create a firebase object by specifying the URL of the database and its secret token.
# The firebase object has functions put and get, that allows user to put data onto 
# the database and also retrieve data from the database.
firebase = firebase.FirebaseApplication(url, token)

print "Reading from my database."
print firebase.get('/age') # get the value from the node age
firebase.put('/', 'pie', 3.14)
