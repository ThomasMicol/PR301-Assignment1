from InterpreterController import InterpreterController
from View.GraphView import *
from Model.Interpreter import *
import sys

global DEFAULT_FILE_PATH

if __name__ == '__main__':
    if len(sys.argv) > 1:
        DEFAULT_FILE_PATH = sys.argv[1]
    InterpreterController(GraphView(), Interpreter(DataValidator()))

