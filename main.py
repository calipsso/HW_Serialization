class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def getInfo(self):
        return f"Person: {self.first_name}, {self.last_name}, {self.age}"
    def getHi(self, msg):
        personinf = self.getInfo()
        return f"{personinf} \n {msg} I am {self.first_name}"

class Student(Person):
    def __init__(self, first_name, last_name, age, score):
        super() .__init__(first_name, last_name, age)
        self.score = score
    def isSuccesfull(self):
        if self.score >= 75:
            return True
        else:
            return False


person = Person("Kamil", "Petpaj", 30)
person1 = Person("Mikulja", "Onanov", 89)
student =Student("Kamil", "Peteraj", 30, 89)

print(person.getInfo())
print(student.getInfo())
print(student.getHi("Hi"))
print(f"Is {student.first_name} succesfull student? {student.isSuccesfull()}")



