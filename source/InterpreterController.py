from cmd import Cmd


class InterpreterController(Cmd):
    def __init__(self, in_view, in_interpreter):
        Cmd.__init__(self)
        self.prompt= '> '
        self.my_view = in_view
        self.my_interpreter = in_interpreter


    def do_add(self, *args):
        options_arr = self.parse_args(args)
        option_dict = {
            '-l' : self.my_interpreter.load_file,
            '-m' : self.manual_add,
            '-d' : self.my_interpreter.load_file
        }
        for key, value in option_dict.items():
            if options_arr[0] == key:
                option_dict[key](options_arr[1])

    def do_save(self, *args):
        # TODO implement this method
        pass

    def do_show(self, *args):
        # TODO implement this method
        pass

    def do_quit(self, *args):
        quit()

    do_q = do_quit

    def parse_args(self, arg_str):
        for arg in arg_str:
            arg_arr = arg.split(' ')
        if len(arg_arr) > 2:
            return "Too many arguments were given"
        else:
            return arg_arr

    def manual_add(self, file_path):
        print(file_path)
        print('HELLO')

    def load_file(self):
        pass