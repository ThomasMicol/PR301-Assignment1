
#
# class User:
"""  def __init__(self, first_name: str, last_name: str, date_of_birth: datetime, sex: str):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.sex = sex """

class Person:
    def __init__(self, new_emp_id, new_gender, new_sales, new_bmi, new_salary, new_birthday):
        self.emp_id = new_emp_id
        self.gender = new_gender
        self.sales = new_sales
        self.bmi = new_bmi
        self.salary = new_salary
        self.birthday = new_birthday
        self.age = self.calculate_age()


from pyvaru import Validator
from pyvaru.rules import TypeRule, FullStringRule, ChoiceRule, PastDateRule

class PersonValidator(Validator):
    def get_rules(self) -> list:
        person = self.data # type: Person
        return [
            TypeRule(apply_to=person,
                     label='Person',
                     valid_type=Person,
                     error_message='Person must be an instance of person model.',
                     stop_if_invalid=True),
            FullStringRule(person.emp_id, 'Emp_ID'),
            ChoiceRule(person.gender, 'Gender', choices=('M', 'F')),
            FullStringRule(person.sales, 'Sales'),
            FullStringRule(person.bmi, 'BMI'),
            FullStringRule(person.salary, 'Salary'),
            FullStringRule(person.age, 'Age'),
            PastDateRule(person.birthday, 'Date of birth')
        ]

validation = PersonValidator(person).validate()
if validation.is_successful():
    # do whatever you want with your valid model
    else:
    # you can take a proper action and access validation.errors
    # in order to provide a useful message to the application user,
    # write logs or whatever

    person = Person (emp_id=' ',
                    gender='unknown'
                    sales=None,
                    bmi=None
                    salary=None,
                    age=None,
                    birthday=datetime(2020, 1, 1),
                    )


while True:
    try:
        # Note: Python 2.x users should use raw_input, the equivalent of 3.x's input
        age = int(input("Please enter your age: "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        #better try again... Return to the start of the loop
        continue
    else:
        #age was successfully parsed!
        #we're ready to exit the loop.
        break
if age >= 18:
    print("You are eligible!")
else:
    print("You are not eligible.")

def get_non_negative_int(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue

        if value < 0:
            print("Sorry, your response must not be negative.")
            continue
        else:
            break
    return value

age = get_non_negative_int("Please enter your age: ")
kids = get_non_negative_int("Please enter the number of children you have: ")
salary = get_non_negative_int("Please enter your yearly earnings, in dollars: ")

