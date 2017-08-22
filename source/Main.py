"""Written By Thomas

This is the main file. The dependency injection is handled from here
and the cmdloop is started.

 """


from InterpreterController import InterpreterController
from View.GraphView import *
from Model.Interpreter import *
from Model.FileHandler.FileHandler import *
from Model.DataValidation.DataValidator import *
from Model.Database.Database import *
import sys


if __name__ == '__main__':
    InterpreterController(GraphView(), Interpreter(DataValidator(), FileHandler(), Database(),
                          InterpreterController.check_set_file_path(sys.argv))).cmdloop()

