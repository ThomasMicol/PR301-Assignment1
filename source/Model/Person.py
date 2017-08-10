class Person:
    def __init__(self, new_emp_id, new_gender, new_sales, new_bmi, new_salary, new_birthday):
        self.emp_id = new_emp_id
        self.gender = new_gender
        self.sales = new_sales
        self.bmi = new_bmi
        self.salary = new_salary
        self.birthday = new_birthday
        self.age = self.calculate_age()

    def calculate_age(self):
        # TODO Implement this method
        pass
