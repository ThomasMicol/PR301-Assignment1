from Model.FileHandler.IFileHandler import IFileHandler
import csv


class FileHandler(IFileHandler):
    # Written By Thomas
    #
    # This class handles any file system related functions.
    # It adheres to the abstract methods defined in IFileHandler
    #
    #
    @staticmethod
    def load_file(file_path='data.csv'):
        # Written By Thomas
        #
        # This takes a file path then loads that information into
        # an array. the array is then returned.
        #
        # If the file location isnt found the user is told.
        #
        #
        data_arr = []
        try:
            with open(file_path, newline='') as file:
                read = csv.reader(file)
                for row in read:
                    data_arr.append(row)
        except FileNotFoundError:
            print("File ", file_path, " was not found")
            return False
        except OSError as err:
            print("file path cant be int")
            return False
        return data_arr

    @staticmethod
    def save_file(data_arr, file_path='data.csv'):
        # Written By Thomas
        #
        # This method takes a clean data array and writes it to a
        # file location. This is done in a csv format.
        #
        #
        try:
            with open(file_path, 'w', newline='') as data_file:
                write = csv.writer(data_file, quotechar='|', delimiter=",",
                                   quoting=csv.QUOTE_MINIMAL)
                for person in data_arr:
                    try:
                        write.writerow(person)
                    except:
                        return False
                return True
        except FileNotFoundError:
            print("File ", file_path, " was not found")
            return False

    def shelve_file(self, file_path):
        # TODO This method needs to be implemeted
        pass
