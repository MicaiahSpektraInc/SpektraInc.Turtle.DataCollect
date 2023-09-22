import turtle, spektraincbackendext, dataext

def test():
    print("Yeah, this works!")

t = turtle.Turtle()
d = dataext.DataTable()

for i in range(0, 5):
    name = input("Please enter your name - ")
    age = input("Please enter your age - ")
    role = input("Please enter your profession - ")
    sex = input("Please enter your sex - ")
    hair_colour = input("Please enter your hair colour(eg. Black, Brown) - ")

    d.insert_data(name, Name=name, Age=age, Role=role, Sex=sex, HairColour=hair_colour)








#name1, name2, name3, name4, name5, name6, name7, name8, name9, name10, name11, name12, name13, name14
#age1, age2, age3, age4, age5, age6, age7 ,age8, age9, age10, age11, age12, age13, age14
#role1, role2, role3, role4, role5, role6, role7, role8, role9, role10, role11, role12, role13, role14
#sex1, sex2, sex3, sex4, sex5, sex6, sex7, sex8, sex9, sex10, sex11, sex12, sex13, sex14
#colour1, colour2, colour3, colour4, colour5, colour6, colour7, colour8, colour9, colour10, colour11, colour12, colour13, colour14
