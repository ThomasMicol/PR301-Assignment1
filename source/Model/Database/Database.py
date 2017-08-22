from Model.Database.IDatabase import IDatabase
import sqlite3

class Database(IDatabase):

    def __init(self):
        self.conn = None
        self.deleteme= None
        self.cursor = None

    def create_connection(self, database_name):
        try:
            self.conn = sqlite3.connect(database_name)
        except ConnectionError:
            print(ConnectionError)
        self.cursor = self.conn.cursor()
        self.make_tables()

    def make_tables(self):
        make_table = """CREATE TABLE IF NOT EXISTS employees ( EMPID VARCHAR(6), Gender CHAR, age INTERGER, sales INTERGER
        , bmi VARCHAR(15), salary INTERGER, birthday DATE);"""
        self.cursor.execute(make_table);
        self.conn.commit()

    def insert_person(self, data_arr):
        for person in data_arr:
            insert_string = """INSERT INTO employees (EMPID ,Gender, age, sales, bmi, salary, birthday)
             VALUES ("{empID}", "{gender}", "{age}", "{sales}", "{bmi}", "{salary}", "{birthday}");"""
            insert_command = insert_string.format(empID=person[0], gender=person[1], age=person[2], sales=person[3], bmi=person[4],
                                                  salary=person[5], birthday=person[6])
            self.cursor.execute(insert_command)
            self.conn.commit()

    def select_person_data(self):
        data_arr = []
        self.cursor.execute("Select * from employees")
        result = self.cursor.fetchall()
        for r in result:
            data_arr.append(r)
        return data_arr

    def format_incoming_db_info(self, raw_arr):
        person_data_arr = []
        try:
            for a_tuple in raw_arr:
                data_arr = []
                try:
                    for data in a_tuple:
                        data_arr.append(data)
                    person_data_arr.append(data_arr)
                except TypeError as oops:
                    print(oops)
            return person_data_arr
        except TypeError as oops:
            print(oops)

    def get_person_information(self, database_name='mydb'):
        self.create_connection(database_name)
        return self.format_incoming_db_info(self.select_person_data())

    def save_data(self, data_arr, database_name='mydb'):
        self.create_connection(database_name)
        try:
            self.insert_person(data_arr)
            return "Success"
        except RuntimeError:
            print("Error inserting the data into the database")
            return "Error"




