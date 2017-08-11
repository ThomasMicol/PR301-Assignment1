from Model.DataValidation.DataValidator import DataValidator

class Interpreter:
    def __init__(self, in_validator, in_file_handler):
        data_arr = None
        self.my_validator = in_validator
        self.file_handler = in_file_handler


    def serialize_data_arr():
        # TODO Implement this method
        pass

    def save_file(self, args):
        # TODO Implement this method
        pass

    def load_file(self, option_arr):
        print("hello i am in the load")


    def add_manual_data(self, new_person_data):
        data = self.my_validator.validate_data(new_person_data)
        print(data)
        return True

    def set_data_arr(self, dirty_data_arr):
        # TODO Implement this method
        pass
