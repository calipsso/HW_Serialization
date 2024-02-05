import json

class Capitals():
    def __init__(self):
        self.country_dict = {"Slovakia":"Bratislava", "Czechia":"Praha", "Brazilia":"RIO"}
    def finding_data(self, country):
        vypis = self.country_dict.get(country)
        return vypis
    def deleting_data(self, country):
        vypis = self.country_dict.pop(country)
        return vypis
    def obsah(self):
        return self.country_dict
    def editing_data(self, country):
        mesto = input("vloz mesto: ")
        vypis = self.country_dict.update({country:mesto})
        return vypis
    def adding_data(self,country):
        mesto = input("vloz mesto ako chces:")
        self.country_dict[country]  = mesto
        return self.country_dict

    def to_json(self, a):
        return json.dumps(a)

    def to_json_file(self, a):





capitals = Capitals()

finding_data = capitals.finding_data(input("hladaj:"))
print(finding_data)
del_capital = capitals.deleting_data(input("zadaj country pre vymaz:"))
print(del_capital)
print("------")
edit_data = capitals.editing_data(input("zadaj country pre edit:"))
print(capitals.obsah())
add_data  = capitals.adding_data(input(": zadaj Country pre pridanie: "))
print(add_data)
print("------")
print(capitals.to_json(capitals.country_dict))










