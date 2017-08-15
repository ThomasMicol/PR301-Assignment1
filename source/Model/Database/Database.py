from source.Model.Database.IDatabase import IDatabase
import sqlite3

class Database(IDatabase):

    def __init(self):
        self.conn = None
        self.cursor = None

    def create_connection(self, database_name):
        try:
            self.conn = sqlite3.connect(database_name)
        except ConnectionError:
            print(ConnectionError)
        self.cursor = self.conn.cursor()
        self.make_tables()



    def make_tables(self):
        make_table = """CREATE TABLE IF NOT EXISTS employees ( EMPID INTERGER PRIMARY KEY, Gender CHAR, sales INTERGER
        , bmi VARCHAR(15), salary INTERGER, birthday DATE);"""
        self.cursor.execute(make_table);
        self.conn.commit()


    def insert_person(self, data_arr):
        for person in data_arr:
            insert_string = """INSERT INTO employees (EMPID ,Gender , sales, bmi, salary, birthday)
             VALUES (NULL, "{gender}", "{sales}", "{bmi}", "{salary}", "{birthday}");"""
            insert_command = insert_string.format(gender=person[1], sales=person[3], bmi=person[4],
                                                  salary=person[5], birthday=person[6])
            self.cursor.execute(insert_command)
            self.conn.commit()

    def get_person_information(self, database_name='mydb'):
        self.create_connection(database_name);


    def save_data(self, data_arr, database_name='mydb'):
        self.create_connection(database_name)
        self.insert_person(data_arr)



