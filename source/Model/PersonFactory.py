from Model.Person import *

class PersonFactory:

    @staticmethod
    def convert_data_to_persons(data_arr):
        person_arr = []
        for person in data_arr:
            aPerson = Person(person[0], person[1], person[3], person[4], person[5], person[6], person[2])
            person_arr.append(aPerson)
        return person_arr