class IFileHandler(object):

    def load_file(self, file_path):
        raise NotImplementedError("An abstract method has not been implemented")

    def save_file(self, data_arr, file_path):
        raise NotImplementedError("An abstract method has not been implemented")

    def shelve_file(self, data_arr, file_path):
        raise NotImplementedError("An abstract method has not been implemented")