from cmd import Cmd


class InterpreterController(Cmd):
    def __init__(self, in_view, in_interpreter):
        Cmd.__init__(self)
        self.prompt = '> '
        self.my_view = in_view
        self.my_interpreter = in_interpreter

    def do_add(self, *args):
        arg_found = False
        options_arr = self.parse_args(args)
        option_dict = {
            '-l': self.my_interpreter.load_file,
            '-m': self.manual_add,
            '-d': self.my_interpreter.load_database
        }
        for key, value in option_dict.items():
            if options_arr[0] == key:
                arg_found = True
                if not self.try_launch(key, value, options_arr):
                    self.my_view.show("command FAILED")
                else:
                    self.my_view.show("SUCCESS")
        if not arg_found:
            self.my_view.show("That option doesnt work with the given command")


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

    def manual_add(self):
        self.my_interpreter.add_manual_data(self.my_view.manual_person_flow())

    def load_file(self):
        pass

    def try_launch(self, key, value, options_arr):
        if (key == '-m'):
            value()
            return True
        else:
            if len(options_arr) == 2:
                value(options_arr[1])
                return True
            else:
                self.my_view.show("Incorrect amount of arguments")
                return False