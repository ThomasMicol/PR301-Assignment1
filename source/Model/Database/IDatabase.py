class IDatabase(object):

    def create_connection(self, database_name='mydb'):
        raise NotImplementedError("An abstract method has not been implemented")

    def insert_person(self, person_ob):
        raise NotImplementedError("An abstract method has not been implemented")

    def get_person_information(self):
        raise NotImplementedError("An abstract method has not been implemented")
