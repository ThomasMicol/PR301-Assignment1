import pickle
# from Ass1.source import load_data.csv
# files need to be opened as binary files


class Person(object):

    def __init__(self, emp_id, gender, age, sales, bmi, salary, birthday):
        self.emp_id = emp_id
        self.gender = gender
        self.age = age
        self.sales = sales
        self.bmi = bmi
        self.salary = salary
        self.birthday = birthday

    def __str__(self):
        string = u'[<Person> emp_id:%s ' \
                 u'gender:%s ' \
                 u'age:%s ' \
                 u'sales:%s ' \
                 u'bmi:%s ' \
                 u'salary:%s ' \
                 u'birthday:%s]' \
                 % (self.emp_id, self.gender, self.age,
                    self.sales, self.bmi, self.salary, self.birthday)
        return string

# output one item
with open('personData.pickle', 'wb') as f:
    w1 = Person('E1001', 'F', 30, 65, 'Normal', 999, '30-5-1994')
    pickle.dump(w1, f)

# input one item
with open('personData.pickle', 'rb') as f:
    w1_restore = pickle.load(f)
print ('Person: % s' % w1_restore)

# output multi items
with open('personData.pickle', 'wb') as f:
    w1 = Person('E1002', 'F', 28, 55, 'OverWeight', 990, '1981-01-17')
    w2 = Person('E1001', 'F', 25, 60, 'UnderWeight', 899, '1980-07-11')
    pickle.dump([w1, w2], f)

# input multi items
with open('personData.pickle', 'rb') as f:
    w_list = pickle.load(f)

for w in w_list:
    print ('Person-list:%s' % w)