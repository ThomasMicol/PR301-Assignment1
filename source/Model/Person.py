class Person:
    def __init__(self, new_emp_id, new_gender, new_sales, new_bmi, new_salary, new_birthday, new_unchecked_age=None):
        self.emp_id = new_emp_id
        self.gender = new_gender
        self.sales = new_sales
        self.bmi = new_bmi
        self.salary = new_salary
        self.birthday = new_birthday
        self.unchecked_age = new_unchecked_age
        self.age = None
        self.confirm_age()


    def confirm_age(self):
        calculated_age = self.calc_my_age()
        if calculated_age == self.unchecked_age:
            self.age = self.unchecked_age
        else:
            self.age = calculated_age

    def calc_my_age(self):
        birthday_arr = self.birthday.split('-')
        day = birthday_arr[0]
        month = birthday_arr[1]
        year = birthday_arr[2]

