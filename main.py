class Student: #Trieda
    def __init__(self, name, age): #konstruktor
        self.name = name #atribut / objekt
        self.age = age

    def __str__(self):
        return f"name = {self.name}, age = {self.age}"

student = Student("kamil", 20) # instancia = zabezpecuje pristup ku triede Student
student1 = Student("peter", 45)

print(student)
print(student1)