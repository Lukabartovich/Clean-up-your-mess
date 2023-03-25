from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.core.window import Window

from DataBase_class import DataBase

Window.size = (500, 600)
Builder.load_file('layout.kv')


class Start(Screen):
    def start(self, string):
        print(string)
        self.manager.current = 'home'


class Home(Screen):
    def glass(self):
        self.text = self.ids.input.text
        if self.text != '':
            db = DataBase()
            result = db.find_thing(str(self.text), True)[1]
            print(result)
            if result != None:
                self.manager.current = 'result'
                self.manager.current_screen.ids.name.text = self.text
                self.manager.current_screen.ids.box.text = result
                name = str(db.find_thing(str(self.text), True)[0])
                number = str(db.find_thing(str(self.text), True)[1])
                print(number, name)


class Result(Screen):
    def back(self):
        self.manager.current = 'home'

    def boxes(self, name):
        self.box_name = name
        with open('files/box.txt', 'w+') as file:
            file.truncate(0)
            file.write(self.box_name)
            file.close()
        db = DataBase()
        if db.get_for_page(1, self.box_name) == True:
            self.manager.current = 'page'
            with open('files/page_number.txt', 'w+') as file2:
                file2.truncate(0)
                file2.write(str(1))
                file2.close()

            self.manager.current_screen.ids.b1.text = \
                db.get_thing_from_number(1, self.box_name)
            self.manager.current_screen.ids.b2.text = \
                db.get_thing_from_number(2, self.box_name)
            self.manager.current_screen.ids.b3.text = \
                db.get_thing_from_number(3, self.box_name)
            self.manager.current_screen.ids.b4.text = \
                db.get_thing_from_number(4, self.box_name)
            self.manager.current_screen.ids.b5.text = \
                db.get_thing_from_number(5, self.box_name)


class Page(Screen):
    def back(self):
        self.ids.name_ = 'page'
        with open('files/page_number.txt', 'w+') as file2:
            self.page_number = file2.read()
            file2.truncate(0)
            file2.write(str(1))

        with open('files/box.txt', 'r+') as file:
            self.name_ = file.read()
            file.truncate(0)
        if self.page_number == '2':
            db = DataBase()
            self.ids.b1.text = db.get_thing_from_number(1, self.name_)
            self.ids.b2.text = db.get_thing_from_number(2, self.name_)
            self.ids.b3.text = db.get_thing_from_number(3, self.name_)
            self.ids.b4.text = db.get_thing_from_number(4, self.name_)
            self.ids.b5.text = db.get_thing_from_number(5, self.name_)

        self.manager.current = 'home'
        self.manager.current_screen.ids.input.text = ''

    def left(self):
        with open('files/page_number.txt', 'r+') as file:
            self.page_number = file.read()

        with open('files/box.txt', 'r+') as file2:
            self.name_ = file2.read()
        if self.page_number == '2':
            db = DataBase()
            self.ids.b1.text = db.get_thing_from_number(1, self.name_)
            self.ids.b2.text = db.get_thing_from_number(2, self.name_)
            self.ids.b3.text = db.get_thing_from_number(3, self.name_)
            self.ids.b4.text = db.get_thing_from_number(4, self.name_)
            self.ids.b5.text = db.get_thing_from_number(5, self.name_)
            with open('files/page_number.txt', 'w+') as file2:
                file2.truncate(0)
                file2.write(str(1))
        if self.page_number == '3':
            db = DataBase()
            self.ids.b1.text = db.get_thing_from_number(11, self.name_)
            self.ids.b2.text = db.get_thing_from_number(12, self.name_)
            self.ids.b3.text = db.get_thing_from_number(13, self.name_)
            self.ids.b4.text = db.get_thing_from_number(14, self.name_)
            self.ids.b5.text = db.get_thing_from_number(15, self.name_)
            with open('files/page_number.txt', 'w+') as file2:
                file2.truncate(0)
                file2.write(str(2))
        if self.page_number == '3':
            db = DataBase()
            self.ids.b1.text = db.get_thing_from_number(11, self.name_)
            self.ids.b2.text = db.get_thing_from_number(12, self.name_)
            self.ids.b3.text = db.get_thing_from_number(13, self.name_)
            self.ids.b4.text = db.get_thing_from_number(14, self.name_)
            self.ids.b5.text = db.get_thing_from_number(15, self.name_)
            with open('files/page_number.txt', 'w+') as file2:
                file2.truncate(0)
                file2.write(str(2))
        if self.page_number == '4':
            db = DataBase()
            self.ids.b1.text = db.get_thing_from_number(11, self.name_)
            self.ids.b2.text = db.get_thing_from_number(12, self.name_)
            self.ids.b3.text = db.get_thing_from_number(13, self.name_)
            self.ids.b4.text = db.get_thing_from_number(14, self.name_)
            self.ids.b5.text = db.get_thing_from_number(15, self.name_)
            with open('files/page_number.txt', 'w+') as file2:
                file2.truncate(0)
                file2.write(str(3))

    def right(self):
        with open('files/page_number.txt', 'r+') as file:
            self.page_number = file.read()

        with open('files/box.txt', 'r+') as file2:
            self.name_ = file2.read()

        if self.page_number == '1':
            db = DataBase()
            if db.get_for_page(6, self.name_) == True:
                self.ids.b1.text = db.get_thing_from_number(6, self.name_)
                self.ids.b2.text = db.get_thing_from_number(7, self.name_)
                self.ids.b3.text = db.get_thing_from_number(8, self.name_)
                self.ids.b4.text = db.get_thing_from_number(9, self.name_)
                self.ids.b5.text = db.get_thing_from_number(10, self.name_)
                with open('files/page_number.txt', 'w+') as file2:
                    file2.truncate(0)
                    file2.write(str(2))
        if self.page_number == '2':
            db = DataBase()
            if db.get_for_page(11, self.name_) == True:
                self.ids.b1.text = db.get_thing_from_number(11, self.name_)
                self.ids.b2.text = db.get_thing_from_number(12, self.name_)
                self.ids.b3.text = db.get_thing_from_number(13, self.name_)
                self.ids.b4.text = db.get_thing_from_number(14, self.name_)
                self.ids.b5.text = db.get_thing_from_number(15, self.name_)
                with open('files/page_number.txt', 'w+') as file2:
                    file2.truncate(0)
                    file2.write(str(3))
        if self.page_number == '3':
            db = DataBase()
            if db.get_for_page(16, self.name_) == True:
                self.ids.b1.text = db.get_thing_from_number(16, self.name_)
                self.ids.b2.text = db.get_thing_from_number(17, self.name_)
                self.ids.b3.text = db.get_thing_from_number(18, self.name_)
                self.ids.b4.text = db.get_thing_from_number(19, self.name_)
                self.ids.b5.text = db.get_thing_from_number(20, self.name_)
                with open('files/page_number.txt', 'w+') as file2:
                    file2.truncate(0)
                    file2.write(str(4))


class Object(Screen):
    pass


class WhatNew(Screen):
    pass


class Root(ScreenManager):
    Window.clearcolor = (0.71, 0.93, 0.49, 1)
    Window.set_icon('files/box.png')
    # против (0.71, 0, 0.49, 1)
    # за (0.24, 0.77, 0.95, 1)


class MainApp(App):
    def build(self):
        self.title = 'Clean Up'

        return Root()


MainApp().run()
