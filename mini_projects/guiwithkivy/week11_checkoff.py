from firebase import firebase
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton

url = "https://rasbpi-9b253.firebaseio.com/" # URL to Firebase database
token = "tlXOUKslj8JwDSc1ymJ1lbh8n2tkfUIZb5090xlC" # unique token used for authentication

# Create a firebase object by specifying the URL of the database and its secret token.
# The firebase object has functions put and get, that allows user to put data onto 
# the database and also retrieve data from the database.
firebase = firebase.FirebaseApplication(url, token)

class MyApp(App):

    def build(self):
        self.layout = GridLayout(cols=2)
        redlight = firebase.get('/redlight')
        yellowlight = firebase.get('/yellight')
        self.yellight = Label(text='Yellow Light',color = (1,1,0,1)if yellowlight == "on" else (1,1,1,1))
        self.yelbutton = ToggleButton(text=yellowlight or 'off', state="down" if yellowlight == "on" else "normal")
        self.redlight = Label(text='Red Light',color = (1,0,0,1)if redlight == "on" else (1,1,1,1))
        self.redbutton = ToggleButton(text = redlight or 'off',state="down" if redlight == "on" else "normal")
        self.layout.add_widget(self.yellight)
        self.layout.add_widget(self.yelbutton)
        self.layout.add_widget(self.redlight)
        self.layout.add_widget(self.redbutton)
        self.yelbutton.bind(on_press = self.yellow_button)
        self.redbutton.bind(on_press = self.red_button)
        return self.layout

    def yellow_button(self,instance):
        if instance.state == 'down' :
            instance.text = 'on'
            firebase.put('/','yellight',instance.text)
            self.yellight.color = (1,1,0,1)
        else:
            instance.text = 'off'
            firebase.put('/','yellight',instance.text)
            self.yellight.color = (1,1,1,1)
    
    def red_button(self,instance):
        if instance.state == 'down' :
            instance.text = 'on'
            firebase.put('/','redlight',instance.text)
            self.redlight.color = (1,0,0,1)
        else:
            instance.text = 'off'
            firebase.put('/','redlight',instance.text)
            self.redlight.color = (1,1,1,1)


MyApp().run()
