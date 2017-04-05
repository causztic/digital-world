from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

from ocr import OCR
from widgets import GroceryItem

class CobraApp(App):

    def build(self):
        layout = GridLayout(cols=3)
        layout.add_widget(Label(text="Your fridge is currently empty!"))
        return layout

if __name__ == '__main__':
    CobraApp().run()