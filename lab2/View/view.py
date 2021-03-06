import math
import os.path

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

from Model.model import Model
from Controller.controller import Controller

Builder.load_file(os.path.join(os.path.dirname(__file__), "ui.kv"))


class MenuScreen(Screen):
    pass


class BaseScreen(Screen):
    def update(self, navigation=0):
        information=Controller.update(Controller, navigation)
        self.ids['full_name_base_id'].text = information[0]
        self.ids['group_base_id'].text = information[1]
        self.ids['valid_reason_base_id'].text = information[2]
        self.ids['invalid_reason_base_id'].text = information[3]
        self.ids['totall_base_id'].text = information[4]
    def change_number_of_strings(self,number_of_strings):
        Controller.change_number_of_strings(Model,number_of_strings)


class AddScreen(Screen):
    def input_validation(self, full_name, group, valid_reason, invalid_reason):
        if full_name == '' or not full_name.replace(' ', '').isalpha():
            self.ids['full_name'].text = 'Invalid input!'
        elif group == '':
            self.ids['group'].text = 'Invalid input!'
        elif not valid_reason.isdigit() or valid_reason == '':
            self.ids['valid_reason'].text = 'Invalid input!'
        elif not invalid_reason.isdigit() or invalid_reason == '':
            self.ids['invalid_reason'].text = 'Invalid input!'
        else:
            Controller.add(Controller, full_name, group, valid_reason, invalid_reason)


class SearchScreen(Screen):
    def find(self, full_name, group, valid_reason, invalid_reason):
        self.ids['search_label_id'].text = Controller.find(Controller, full_name, group, valid_reason, invalid_reason)


class DeleteScreen(Screen):
    def delete(self, full_name, group, valid_reason, invalid_reason):
        self.ids['delete_label_id'].text = Controller.delete(Controller, full_name, group, valid_reason, invalid_reason)


class UploadScreen(Screen):
    def upload_file(self, file_name):
        if Controller.upload_file(Controller, file_name):
            self.manager.current = 'menu'
        else:
            self.ids['file'].text = 'No such file!'


class TestApp(App):
    Window.clearcolor = (.81, .77, .87, 1)

    def build(self):
        self.title = "Attendance"
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(BaseScreen(name='base'))
        sm.add_widget(AddScreen(name='add'))
        sm.add_widget(SearchScreen(name='search'))
        sm.add_widget(DeleteScreen(name='delete'))
        sm.add_widget(UploadScreen(name='upload'))

        return sm
