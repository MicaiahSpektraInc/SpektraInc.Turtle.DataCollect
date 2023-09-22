import turtle

def test():
     print("Yeah that works!")

class DataTable: #Lucas:Creates the class to be used to insert data for new users completing
     
     def __init__(self):
          self.data = {}

     def insert_data(self, name, **kwargs):#Lucas:Creates module to insert data, (**Key Words Arguments)future proofs the code to be able to add more inputs later on
         self.data[name] = kwargs
         self.data[name]["Name"] = name

     def count_data(self, data, value):#Lucas: Creates a module to allow backend to count data and use it to convert into the bar info
         c = 0
         for i in self.data:
             if self.data[i][data] == value:
                 c += 1
         return c
      
if __name__ == "__main__":
    test = DataTable()

    test.insert_data("Jacob", Name = "Jacob", Age = 23, Role = "Programmer", Sex = "Male", HairColour = "Brown")#Lucas:Next few lines creates each person with(test.insert_data())

    test.insert_data("Joao", Name = "Joao", Age = 16, Role = "Musician", Sex = "Male", HairColour = "Brown")

    test.insert_data("Maja", Name = "Maja", Age = 17, Role = "Artist", Sex = "Female", HairColour = "Brown")

    test.insert_data("Micaiah", Name = "Micaiah", Age = 18, Role = "Artist", Sex = "Male", HairColour = "Black")

    test.insert_data("Filip", Name = "Filip", Age = 16, Role = "Musician", Sex = "Male", HairColour = "Brown")

    test.insert_data("Lucas", Name = "Lucas", Age = 16, Role = "Programmer", Sex = "Male", HairColour = "Brown")

    test.insert_data("Joshua", Name = "Joshua", Age = 16, Role = "Musician", Sex = "Male", HairColour = "Black")

    test.insert_data("Abdul", Name = "Abdul", Age = 18, Role = "Artist", Sex = "Male", HairColour = "Black")

    test.insert_data("Oliver", Name = "Oliver", Age = 16, Role = "Programmer", Sex = "Sex", HairColour = "Brown")

    test.insert_data("Nathan", Name = "Nathan ", Age = 16, Role = "Musician", Sex = "Male", HairColour = "Black")

    test.insert_data("Loic", Name = "Loic", Age = 16, Role = "Programmer", Sex = "Male", HairColour = "Black")

    print(test.count_data("Role", "Programmer")) #Lucas:Tests to see if the code works at the end, counting and sending data to the backend