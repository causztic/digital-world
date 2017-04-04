from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


class MyLabel(Label):

    def __init__(self, **kwargs):
        Label.__init__(self, font_size=24, halign='left', valign='middle', **kwargs)
        self.bind(size=self.setter('text_size'))
        self.padding = (20, 20)


class Investment(App):

    def build(self):
        layout = GridLayout(cols=2)
        l1 = MyLabel(text="Investment Amount")
        l2 = MyLabel(text="Years")
        l3 = MyLabel(text="Annual Interest Rate")
        l4 = MyLabel(text="Future Value")
        self.years = TextInput(multiline=False)
        self.ia = TextInput(multiline=False)
        self.air = TextInput()
        self.fv = MyLabel(text="")
        layout.add_widget(l1)
        layout.add_widget(self.ia)
        layout.add_widget(l2)
        layout.add_widget(self.years)

        layout.add_widget(l3)
        layout.add_widget(self.air)
        layout.add_widget(l4)
        layout.add_widget(self.fv)
        btn = Button(text="Calculate", on_press=self.calculate, font_size=24)
        layout.add_widget(btn)
        return layout

    def calculate(self, instance):
        try:
            self.fv.text = str(round(float(
                self.ia.text) * (1 + float(self.air.text) / 1200) ** (float(self.years.text) * 12), 2))
        except:
            self.fv.text = "Invalid values"


Investment().run()
