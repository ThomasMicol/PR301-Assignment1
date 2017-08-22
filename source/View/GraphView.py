from View.IGraphView import IGraphView
from plotly import *
import plotly.graph_objs as ob


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

    def employees_by_gender_graph(self, data_arr):
        # TODO
        pass

    def age_verse_salary_graph(self, data_arr):
        age_data = []
        salary_data = []
        for person in data_arr:
            age_data.append(person[2])
            salary = int(person[5]) * 1000
            salary_data.append(salary)
        graph_data = [ob.Scatter(
            x=age_data,
            y=salary_data,
            marker=dict(
                color="rgb(16, 32, 77)"
            ),
            name="Age Verse Salary"
        )]
        graph_format = ob.Layout(
            title="Salary Verse Age Scatter Graph",
            xaxis=dict(
                title="Age"
            ),
            yaxis=dict(
                title="Salary"
            )
        )
        graph = ob.Figure(data=graph_data, layout=graph_format)
        self.show_graph(graph)

    def bmi_pie_graph(self, data_arr):
        normal_count = 0
        obesity_count = 0
        underweight_count = 0
        overweight_count = 0
        for person in data_arr:
            if person[4] == "Normal":
                normal_count += 1
            if person[4] == "Overweight":
                overweight_count += 1
            if person[4] == "Obesity":
                obesity_count += 1
            if person[4] == "Underweight":
                underweight_count +=1


        graph_data = {
            'data': [{'labels': ['Normal', 'Overweight', 'Obesity', 'Underweight'],
                      'values': [normal_count, overweight_count, obesity_count, underweight_count],
                      'type': 'pie'}],
            'layout': {
                'title': 'Staff by BMI'}
        }
        self.show_graph(graph_data)


    @staticmethod
    def show(show_string):
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
        offline.plot(graph_data)
