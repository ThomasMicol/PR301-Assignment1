# Written By Thomas
#
# This is the main file. The dependency injection is handled from here
# and the cmdloop is started.
#
#


from interpreter_controller import InterpreterController
from View.graph_view import *
from Model.interpreter import *
from Model.FileHandler.file_handler import *
from Model.DataValidation.data_validator import *
from Model.Database.database import *
import sys


if __name__ == '__main__':
    InterpreterController(GraphView(), Interpreter(
                            DataValidator(),
                            FileHandler(),
                            Database(),
                            InterpreterController.check_set_file_path(sys.argv)
                            )
                          ).cmdloop()
