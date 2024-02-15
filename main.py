class Student: #Trieda
    def __init__(self, name, age): #konstruktor
        self.name = name #atribut / objekt
        self.age = age

    def show_info(self): #Metoda
        return f"{self.name}, {self.age}"
    def show_msg(self, msg_text): #Metoda
        return f"{self.name}, {msg_text}"

student = Student("kamil", 20) # instancia = zabezpecuje pristup ku triede Student
student1 = Student("Peter", 45)

print(student.show_info()) #Vypis
print(student.show_msg("Vitaj"))
print(student1.show_info())
print(student1.show_msg("Vitaj"))

