class Person:
    def __init__(self, firstName, lastName, age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age

    def getInfo(self):
        return f"{self.firstName}, {self.lastName}, {self.age}"
    def getHi(self, msg):
        return f"{msg}, I am {self.lastName}"

class Employee (Person):
    def __init__(self, firstName, lastName, age, jobTitle, salary, seniority):
        super().__init__(firstName, lastName, age)
        self.jobTitle = jobTitle
        self.salary = salary
        self.seniority = seniority

    def getInfo(self):
        return f"{self.firstName}, {self.lastName}, {self.age}, {self.jobTitle}, {self.salary}, {self.seniority}"
    def getSickLeavePerc(self, num):
        if self.seniority > num:
            return True
        else:
            return False

person = Person("kamil", "Peteraj", 36)
emlpoyee = Employee("Erik", "Kalinak", 19, "PR", 1956, 7)

print(emlpoyee.getHi("Hi"))
print(emlpoyee.getInfo())
print(emlpoyee.getSickLeavePerc(2))













