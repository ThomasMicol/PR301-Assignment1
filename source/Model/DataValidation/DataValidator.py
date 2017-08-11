from Model.DataValidation.IDataValidator import IDataValidator
import re
import doctest

#person = ["A001", "M", 20, 333, "Normal", 666, "20-2-1997"]

class DataValidator(IDataValidator):
    def validate_data(self, dirty_data_arr):
        # TODO This is where the input from the user is washed and made sure to work with the program.

        for person in dirty_data_arr:
            print(person)

            if len(person) == 7:
                cleaned_data = []
                print("data is correct length")

                if self.validate_empid(str(person[0])):
                    print("Valid empid: " + str(person[0]))
                    cleaned_data.append(str(person[0]))

                if self.validate_gender(str(person[1])):
                    print("Valid gender: " + str(person[1]))
                    cleaned_data.append(str(person[1]))

                if self.validate_age(str(person[2])):
                    print("Valid age: " + str(person[2]))
                    cleaned_data.append(str(person[2]))

                if self.validate_sales(str(person[3])):
                    print("Valid Sales: " + str(person[3]))
                    cleaned_data.append(str(person[3]))

                if self.validate_bmi(str(person[4])):
                    print("Valid BMI: " + str(person[4]))
                    cleaned_data.append(str(person[4]))

                if self.validate_salary(str(person[5])):
                    print("Valid salary: " + str(person[5]))
                    cleaned_data.append(str(person[5]))

                if self.validate_birthday(str(person[6])):
                    print("Valid birthday: " + str(person[6]))
                    cleaned_data.append(str(person[6]))
            else:
                return "Not enough feilds" + str(len(person))

            if len(cleaned_data) == 7:
                return cleaned_data

    @staticmethod
    def validate_empid(empid):
        """
        Checks EMPID = [A-Z][0-9]{3}) e.g. B003

        >>> validate_empid("C002")
        True
        """
        if re.compile("([A-Z][0-9]{3})").match(empid):
            return True
        else:
            return False

    @staticmethod
    def validate_gender(gender):
        """
        Checks gender = M or F e.g. M or F

        >>> validate_gender("F")
        True
        """
        if re.compile("([M|F])").match(gender):
            return True
        else:
            return False

    @staticmethod
    def validate_age(age):
        """
        Checks age = [0-9]{2} e.g. 0 to 99

        >>> validate_age(str(64))
        True
        """
        if re.compile("([0-9]{2})").match(age):
            return True
        else:
            return False

    @staticmethod
    def validate_sales(sales):
        """
        Checks Sales = [0-9]{3} e.g. 330

        >>> validate_sales(str(999))
        True
        """
        if re.compile("([0-9]{3})").match(sales):
            return True
        else:
            return False

    @staticmethod
    def validate_bmi(bmi):
        """
        Checks BMI = normal|overweight|obesity|underweight case insensitive

        >>> validate_bmi("Overweight")
        True
        """
        if re.compile("normal|overweight|obesity|underweight", re.I).match(bmi):
            return True
        else:
            return False

    @staticmethod
    def validate_salary(salary):
        """
        Checks Salary = [0-9]{2,3} e.g. 33 or 330

        >>> validate_salary(str(24))
        True
        """
        if re.compile("([0-9]{2,3})").match(salary):
            return True
        else:
            return False

    @staticmethod
    def validate_birthday(birthday):
        """
        Checks birthday = [0-9]{1,2}-[0-9]{1,2}-[0-9]{4} e.g. 2-5-1967

        >>> validate_birthday("2-6-2014")
        True
        """
        if re.compile("([0-9]{1,2}-[0-9]{1,2}-[0-9]{4})").match(birthday):
            return True
        else:
            return False


# doctest.testmod(verbose=True)
