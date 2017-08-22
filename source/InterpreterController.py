from cmd import Cmd

class InterpreterController(Cmd):
    def __init__(self, in_view, in_interpreter):
        Cmd.__init__(self)
        self.prompt = '> '
        self.my_view = in_view
        self.my_interpreter = in_interpreter


    @staticmethod
    def check_set_file_path(running_args):
        if len(running_args) > 2 :
            print("too many arguments supplied")
            return running_args[0]
        try:
            open(running_args[1], 'r')
            return running_args[1]
        except OSError as erro:
            print(erro)
            print("Defaulting to working directory.")
            return running_args[0]
        except IndexError as erro:
            print("No default path provided.")
            print("Defaulting to working directory.")
            return running_args[0]

    def do_add(self, *args):
        options_arr = self.parse_args(args)
        option_dict = {
            '-l': self.my_interpreter.load_file,
            '-m': self.manual_add,
            '-d': self.my_interpreter.load_database
        }
        self.find_in_dict(options_arr, option_dict)



    def do_save(self, *args):
        options_arr = self.parse_args(args)
        option_dict = {
            '-f': self.my_interpreter.save_file,
            '-d': self.my_interpreter.save_database,
            '-s': self.my_interpreter.serialize_data_arr
        }
        self.find_in_dict(options_arr, option_dict)

    def do_show(self, *args):
        options_arr = self.parse_args(args)
        option_dict = {
            '-a': self.my_view.sales_by_gender_graph,
            '-b': self.my_view.employees_by_gender_graph,
            '-c': self.my_view.age_verse_salary_graph,
            '-d': self.my_view.bmi_pie_graph
        }
        for key, value in option_dict.items():
            if options_arr[0] == key:
                value(self.my_interpreter.get_data())

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

    def find_in_dict(self, options_arr, options_dict):
        arg_found = False
        for key, value in options_dict.items():
            if options_arr[0] == key:
                arg_found = True
                if not self.try_launch(key, value, options_arr):
                    return
                else:
                    return
        if not arg_found:
            return

    def try_launch(self, key, value, options_arr):
        if (key == '-m'):
            value()
            return True
        else:
            if len(options_arr) == 2:
                value(options_arr[1])
                return True
            else:
                return False

