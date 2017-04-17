from kivy.app import App
from kivy.uix.label import Label


class MyApp(App):

    def build(self):
        self.mylabel = Label(text="Slide me", font_size=24)
        self.mylabel.bind(on_touch_move=self.detect)
        return self.mylabel

    def detect(self, instance, touch):
        if touch.dx < 0:
            instance.text = "Slide Left"
        elif touch.dx > 0:
            instance.text = "Slide Right"
        elif touch.dy > 0:
            instance.text = "Slide Top"
        elif touch.dy < 0:
            instance.text = "Slide Down"

if __name__ == '__main__':
    MyApp().run()
