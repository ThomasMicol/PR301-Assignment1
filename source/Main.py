from source.View.GraphView import *
from source.InterpreterController import *
from source.Model.Interpreter import *


if __name__ == '__main__':
    InterpreterController(GraphView(), Interpreter(DataValidator()))

