from View.IGraphView import IGraphView

class GraphView(IGraphView):

    def sales_by_gender_graph(self, data_arr):
        print("child")

    def show(self, show_string):
        print(show_string)

    def read(self, prompt):
        return input(prompt)

    def manual_person_flow(self):
        person_data_arr= []
        person_data_arr.append(self.read("Enter your employee ID: "))
        person_data_arr.append(self.read("Enter your gender: "))
        person_data_arr.append(self.read("Enter your age: "))
        person_data_arr.append(self.read("Enter your sales count: "))
        person_data_arr.append(self.read("Enter your BMI: "))
        person_data_arr.append(self.read("Enter your salary: "))
        person_data_arr.append(self.read("Enter your birthday, e.g. dd-mm-yyyy: "))
        print(person_data_arr)
        return person_data_arr