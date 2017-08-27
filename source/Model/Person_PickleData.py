import pickle

class Person:
    def __init__(self, emp_id, gender, age, sales, bmi, salary, birthday):
        self.emp_id = emp_id
        self.gender = gender
        self.age = age
        self.sales = sales
        self.bmi = bmi
        self.salary = salary
        self.birthday = birthday

with open('person_data.pkl', 'wb') as output:
    Person1 = Person('A001', 'F', 23, 45, 'Normal', 999, '30-5-1994')
    pickle.dump(Person1, output, pickle.HIGHEST_PROTOCOL)

    Person2 = Person('A002', 'M', 25, 50, 'Overweight', 850, '21 - 3 - 1995')
    pickle.dump(Person2, output, pickle.HIGHEST_PROTOCOL)

    del Person1
    del Person2

with open('Person_data.pkl', 'rb') as input:
    Person1 = pickle.load(input)
    print(Person1.emp_id)  # -> A001
    print(Person1.gender)  # -> F
    print(Person1.age)
    print(Person1.sales)
    print(Person1.bmi)
    print(Person1.salary)
    print(Person1.birthday)

    Person2 = pickle.load(input)
    print(Person2.emp_id)  # -> A002
    print(Person2.gender)  # -> M
    print(Person2.age)
    print(Person2.sales)
    print(Person2.bmi)
    print(Person2.salary)
    print(Person2.birthday)
