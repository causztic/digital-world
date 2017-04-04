from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


Builder.load_string("""
<MenuScreen>:
    BoxLayout:
        orientation: 'horizontal'
        Button:
            text: 'Settings'
            on_press: root.manager.current = 'settings'
        Button:
            text: 'Quit'
            on_press: app.stop()
<SettingsScreen>:
    BoxLayout:
        Label:
            text: 'Settings Screen'
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'
""")


class MenuScreen(Screen):
    pass


class SettingsScreen(Screen):
    pass

class MyApp(App):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(SettingsScreen(name='settings'))
        return sm

if __name__ == '__main__':
    MyApp(name="Settings").run()
