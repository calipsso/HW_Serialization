import random
import math

class ElementsStorage:
    def __init__(self):
        self.storage = set()
    def randomChoiceInt(self, a, b): # random vstup
        for _ in range(10):
            self.storage.add(random.randint(a, b))
        print(self.storage)
    def userChoiceInt(self): # uzivatelsky vstup
        usrVstup = input("Zadajte lubovolny pocet cisel oddelenych medzerou: ")
        for num in usrVstup.split():
            self.storage.add(int(num))
        return self.storage

    #def sumElements(self):
        #sumZoznam = 0
        #for num in self.storage:
            #sumZoznam += num
        #return sumZoznam

class FunctionsElements(ElementsStorage):

    def sumElements(self):
        sumZoznam = 0
        for num in self.storage:
            sumZoznam += num
        return sumZoznam

    def lenStorage(self):
        d = len(self.storage)
        return d

    def arithmElements(self, a, b):
        delenec = b//a
        return delenec



elements = FunctionsElements()
#elements = ElementsStorage()


#elements.randomChoiceInt(10, 99) #random
elements.userChoiceInt() # user

#print(elements.storage)
print(elements.sumElements())
print(elements.arithmElements(elements.lenStorage(), elements.sumElements()))
