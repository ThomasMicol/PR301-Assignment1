from Model.FileHandler.IFileHandler import IFileHandler
import csv

class FileHandler(IFileHandler):
    @staticmethod
    def load_file(file_path='data.csv'):
        data_arr = []
        try:
            with open(file_path, newline='') as file:
                read = csv.reader(file)
                for row in read:
                    data_arr.append(row)
        except FileNotFoundError:
            print("File ", file_path, " was not found")
        return data_arr


    def save_file(self, data_arr, file_path='data.csv'):
        try:
            with open(file_path,'wb') as data_file:
                write = csv.writer(data_file)
                for person in data_arr:
                    for data in person:
                        write.writerow(data)
        except FileNotFoundError:
            print("File ", file_path, " was not found")

    def shelve_file(self, file_path):
        # TODO This method needs to be implemeted
        pass