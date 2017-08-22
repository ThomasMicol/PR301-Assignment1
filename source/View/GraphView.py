# from Source.IGraphView import IGraphView
from plotly import *


class GraphView(IGraphView):

    def sales_by_gender_graph(self, data_arr):
        graph_data = {
            'data': [{'labels': ['Residential', 'Non-Residential', 'Utility'],
                      'values': [19, 26, 55],
                      'type': 'pie'}],
            'layout': {
                'title': 'Forcasted 2014 U.S. PV Installations by Market Segment'}
        }

        self.show_graph(graph_data)

    def show(self, show_string):
        print(show_string)

    def read(self, prompt):
        return input(prompt)

    def manual_person_flow(self):
        person_data_arr = []
        person_data = []
        person_data.append(self.read("Enter your employee ID: "))
        person_data.append(self.read("Enter your gender: "))
        person_data.append(self.read("Enter your age: "))
        person_data.append(self.read("Enter your sales count: "))
        person_data.append(self.read("Enter your BMI: "))
        person_data.append(self.read("Enter your salary: "))
        person_data.append(self.read("Enter your birthday, e.g. dd-mm-yyyy: "))
        person_data_arr.append(person_data)
        return person_data_arr

    @staticmethod
    def show_graph(graph_data):
        plotly.offline.plot(graph_data)
