from  source.Model.Person import *

class PersonFactory:

    @staticmethod
    def convert_data_to_persons(data_arr):
        person_arr = []
        for person in data_arr:
            a_person = Person(person[0], person[1], person[3], person[4], person[5], person[6], person[2])
            person_arr.append(a_person)
        return person_arr