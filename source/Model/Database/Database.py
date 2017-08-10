from source.Model.Database.IDatabase import IDatabase


class Database(IDatabase):

    def __init(self):
        self.conn = None

    def create_connection(self, database_name='mydb'):
        # Todo Method needs to be implemented
        pass

    def make_tables(self):
        # Todo Method needs to be implemented
        pass

    def insert_person(self, person_ob):
        # Todo Method needs to be implemented
        pass

    def get_person_information(self):
        # Todo Method needs to be implemented
        pass
