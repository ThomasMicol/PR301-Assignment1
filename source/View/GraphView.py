# from Source.IGraphView import IGraphView
from plotly import *
import plotly.graph_objs as ob


class GraphView(IGraphView):
    """Written By Thomas

    This Class models the graph view and inherits the abstract classes from
    the IGraph View

    Its purpose is to handle the visual aspect of the system. It generates the
    graphs from the data stored in the system.

    """
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
        """Written By Thomas

        This takes an array of pre cleaned person data arrays then formats then
        extracts the needed information into the age and salary data arrays.

        Salary is also multiplied by 1000 to get the actual value of a persons salary

        figure is used to generate a usable graph object. This is passed the graph
        data and the graph format dictionaries.

        the usable graph object is then output by passing it to the show_graph method

        """
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
        """Written By Thomas

        This makes a pie graph of every employees BMI
        The counters are initialized at the start then the array is iterated
        through, matching the BMI of each employee with the correct input then adding
        one to the respective counter.
        """
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
        """Written By Thomas

        Outputs a given string."""
        print(show_string)

    def read(self, prompt):
        """Written By Thomas

        Reads and input while also giving the user a prompt
        which is passed into the method."""
        return input(prompt)

    def manual_person_flow(self):
        """Written By Thomas

        This is a flow for getting manual data from the user.
        It makes a person array then asks a set of questions to find out
        all the information of an employee from the user.
        """
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
        """Written By Thomas

        This takes a graph object from the graph generator methods and displays
        it in the users web browser.

        """
        offline.plot(graph_data)
