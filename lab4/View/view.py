import os.path

from kivy.config import Config

Config.set("graphics", "resizable", 0)
Config.set("graphics", "width", 800)
Config.set("graphics", "height", 600)

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

Builder.load_file(os.path.join(os.path.dirname(__file__), "ui.kv"))


class FirstPage(Screen):
    def __init__(self, controller):
        super(FirstPage, self).__init__()
        self.controller = controller

    def new_game(self):
        self.controller.new_game()

    def continue_game(self):
        self.controller.continue_game()


class MainPage(Screen):
    def __init__(self, controller):
        super(MainPage, self).__init__(name='main')
        self.controller = controller

    def update(self):
        self.ids['train_goods'].text = f'{self.controller.update()[-1]} {self.controller.update()[-2]}'
        self.ids['st_A_goods'].text = self.controller.update()[0]
        self.ids['st_B_goods'].text = self.controller.update()[1]
        self.ids['st_C_goods'].text = self.controller.update()[2]
        self.ids['st_D_goods'].text = self.controller.update()[3]
        self.ids['st_E_goods'].text = self.controller.update()[4]
        self.ids['st_F_goods'].text = self.controller.update()[5]

    def next_station(self, station):
        if station != '':
            self.ids['txt'].text = self.controller.next_station(station.lower())
        self.update()

    def load(self, num):
        if num != '':
            self.ids['txt'].text = self.controller.load(num)
        self.update()

    def unload(self, num):
        if num != '':
            self.ids['txt'].text = self.controller.unload(num)
        self.update()


class TestApp(App):
    def __init__(self, controller):
        super(TestApp, self).__init__()
        self.controller = controller

    Window.clearcolor = (.45, .76, .76, 1)

    def build(self):
        self.title = "Thomas"
        sm = ScreenManager()

        sm.add_widget(FirstPage(self.controller))
        sm.add_widget(MainPage(self.controller))

        return sm
