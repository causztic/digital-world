from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.togglebutton import ToggleButton


class LedController(App):

    def tgl_led(self, instance):
        if instance.state == "down":
            instance.text = "on"
        else:
            instance.text = "off"

    def build(self):
        layout = GridLayout(cols=2)
        self.yellow_tgl = ToggleButton(text="off", on_press=self.tgl_led)
        self.red_tgl = ToggleButton(text="off", on_press=self.tgl_led)

        layout.add_widget(Label(text="Yellow LED"))
        layout.add_widget(self.yellow_tgl)
        layout.add_widget(Label(text="Red LED"))
        layout.add_widget(self.red_tgl)

        return layout

if __name__ == "__main__":
    LedController(name="LED").run()
