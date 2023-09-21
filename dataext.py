import turtle

def test():
     print("Yeah that works!")

class DataTable:
     
     def __init__(self):
          self.data = {}

     def insert_data(self, name, **kwargs):
         self.data[name] = kwargs
         self.data[name]["Name"] = name

     def count_data(self, data, value):
         c = 0
         for i in self.data:
             if self.data[i][data] == value:
                 c += 1
         return c
      
if __name__ == "__main__":
    test = DataTable()
    test.insert_data("Joao", Name = "Joao", Age = 16, County = "London", Sex = "Male")
    test.insert_data("Maja", Name = "Maja", Age = 17, County = "London", Sex = "Female")
    print(test.count_data("County", "London"))