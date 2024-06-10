#!/usr/bin/python3
 
class PartyAnimal:
    x = 0
    name = ""
    def __init__(self, nam):
        self.name = nam
        print("constructed: ",self.name)

    def party(self):
        self.x = self.x + 1
        print(self.name,"party count",self.x)

class football(PartyAnimal):
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name,"points",self.points)

s = PartyAnimal("sally")
s.party()

j = football("jim")
j.party()
j.touchdown()
j.party()
j.touchdown()
j.party()
j.touchdown()
j.party()
j.touchdown()

