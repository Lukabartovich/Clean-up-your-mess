import sqlite3
from StringSort import StringSort

class DataBase:

    def __init__(self):
        self.database = 'files/database.db'
        self.connection = sqlite3.connect(self.database)
        self.cursor = self.connection.cursor()

    def clean(self, string, string2):
        s = StringSort(string)
        return s.delete(string2)

    def check_for_number(self, number, name):
        string = f'SELECT "{str(number)}" FROM "Boxes" WHERE "name" = "{name}"'
        self.cursor.execute(string)

        result = self.cursor.fetchall()
        # print(f">>>>>>>>> {result}")
        if str(result) == "[(None,)]" or str(result) == "[('',)]":
            return False
        else:
            return True

    def get_names(self):
        self.cursor.execute("""
        SELECT "name" FROM "Boxes"
        """)
        self.result = self.cursor.fetchall()
        self.clean_result = str(self.clean(str(self.result), "'[],()"))
        return self.clean_result.split()

    def get_for_page(self, number, name):
        num = 0
        for i in range(1, int(number) + 1):
            if self.check_for_number(i, name) == True:
                num += 1
        if num == int(number):
            return True
        else:
            return False

    def get_thing_from_number(self, number, name):
        self.cursor.execute(f'SELECT "{number}" from '
                            f'"Boxes" WHERE "name" = "{name}"')

        result = self.clean(str(self.cursor.fetchall()), "[(,')]")

        if result != 'None':
            return result
        else:
            return ''

    def get_name(self, number, data):
        self.cursor.execute(f'SELECT "name" FROM "Boxes" WHERE '
                            f'"{number}" = "{data}"')
        return str(self.clean(str(self.cursor.fetchall()), "[(',)]"))

    def last_number(self, name):
        number = 0
        for i in range(1, 21):
            if self.check_for_number(i, name) == True:
                number += 1
        if number == 20:
            return number
        else:
            return number

    def update_new_data(self, data, name):
        last_number = self.last_number(name)
        string = f'UPDATE "Boxes" set "{last_number}" = "{data}" WHERE "name"= "{name}"'
        self.connection.execute(string)
        self.connection.commit()

    def new_box(self, name):

        list1 = []
        for i in range(0, 21):
            list1.append('')


        self.connection.execute("""
        INSERT INTO "Boxes" VALUES
            (?, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
        """, [name])

        self.connection.commit()

    def find_thing(self, data, number=None):
        list1 = []
        names = self.get_names()

        for name in range(len(names)):
            current_name = names[name]
            for i in range(21):
                self.cursor.execute(f'SELECT "{i}" from "Boxes" WHERE'
                                    f' "name" = "{current_name}"')
                result = self.cursor.fetchall()
                list1.append(str(self.clean(str(result), "[(',)]")))
            list1.remove('0')
            if str(data) in list1:
                if number:
                    return [str(list1.index(data) + 1), current_name]
                else:
                    return current_name
            else:
                list1 = []
                continue

    def update_number(self, number, data, name):
        self.connection.execute(f'UPDATE "Boxes" set "{number}" '
                                f'= "{data}" WHERE '
                                f'"name" = "{name}"')

        self.connection.commit()

    def delete_thing(self, data):
        name = self.find_thing(data, True)[1]
        number = self.find_thing(data, True)[0]
        last = int(self.last_number(name))
        if name != None and number != None:
            for i in range(int(number), last):
                data_data = self.get_thing_from_number(i + 1, name)
                self.update_number(i, data_data, name)
            self.update_number(last, '', name)


# db = DataBase()
# print(db.get_for_page(6, 'box3'))
# print(db.last_number('box1'))
# db.update_new_data('щетка', 'box1')
# db.new_box('box4')
# print(db.find_thing('ldkfgldkjhg'))
# db.delete_thing('')