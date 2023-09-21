import turtle

def test():
     print("Yeah that works!")


class Person:

    def __init__(self,  name, age, hair, sex, role):
        self.name = name
        self.age = age
        self.hair = hair
        self.sex = sex
        self.role = role

class DataTable:
     
     def __init__(self):
          self.data = []
          

     def AddPerson(self, name, age, sex, role, hair_colour):
        n = Person(name, age, hair_colour, sex, role)
        self.data.append(n)

     def CountHairColour(self, colour):
        c = 0
        for i in self.data:
            if i.hair == colour:
                c += 1
        return c
     
     def CountSex(self, sex):
        c = 0
        for i in self.data:
            if i.sex == sex:
                c += 1
        return c
     
     def CountRole(self, role):
         c = 0
         for i in self.data:
             if i.role == role:
                 c += 1
         return c
     

if __name__ == "__main__":
    test = DataTable()
    test.AddPerson("Lucas", 16, "Male", "Musician", "Brown")
    test.AddPerson("Maja", 17, "Female", "Programmer", "Brown")
    test.AddPerson("Micaiah", 18, "Male", "Artist", "Black")
    test.AddPerson("Fillip", 16, "Male", "Musician", "Blonde")
    test.AddPerson("Joao", 16, "Male", "Programmer", "Ginger")
    print(test.CountRole("Musician"))