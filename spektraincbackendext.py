import turtle
from dataext import *

t = turtle.Turtle()

class Graph:

    def axis(t):
        t.color('black')
        t.speed(0)
        t.penup()
        t.backward(350)
        t.right(90)
        t.forward(350)
        t.pendown()
        t.left(90)
        t.forward(635)
        t.backward(635)
        t.left(90)
        t.forward(625)
        t.backward(625)
        t.right(90)
        t.penup()
        t.home()
        t.backward(350)
        t.right(90)
        t.forward(350)
        t.left(90)

    def colourKey(t):
        t.speed()
        t.penup()
        t.home()
        t.forward(300)
        t.left(90)
        t.forward(250)
        t.right(90)
        t.pendown()

    def drawBar(t, value, gap, colour):
        h = 625
        b = value
        m = 15
        v = h * (b / m)
        Movement.ghostforward(t, gap)
        #t.up()
        #t.forward(gap/2)
        #t.down()
        Movement.rectangle(t, v, gap, colour)
        Movement.ghostforward(t, gap)


class Movement:
    def ghostforward(t, distance):
        t.up()
        t.forward(distance)
        t.down()

    def rectangle(t, height, width, colour):
        t.color(colour)

        t.begin_fill()
        t.left(90)
        t.forward(height)
        t.right(90)
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.left(90)
        t.end_fill()

    def Centre(t):
        t.up()
        t.goto(-350, -350)
        t.down()

class Data:

    def axisY(t):
        t.left(90)
        t.speed(0)
        t.color('black')
        style = ('ariel', 12)

        for i in range(0, 15):
            t.write(str(i), font = style, align = 'right')

            h = 625
            t.forward(h / 15)
            t.down()
            t.left(90)
            t.forward(25)
            t.backward(25)
            t.right(90)
            t.up()
        t.backward(620)
        t.right(90)

    def axisX(t, width):
        t.speed(0)
        t.color('black')
        style = ('ariel', 10)

        Movement.Centre(t)
        t.up()
        t.right(90)
        t.forward(20)
        t.left(90)

        total = width * 3

        t.forward(total/2)
        t.write('Brown', font = style, align = 'center')
        t.forward(total)
        t.write('Black', font = style, align = 'center')
        t.forward(total)
        t.write('Blonde', font = style, align = 'center')
        t.forward(total)
        t.write('Ginger', font = style, align = 'center')
        t.forward(total)
        t.write('Male', font = style, align = 'center')
        t.forward(total)
        t.write('Female', font = style, align = 'center')
        t.forward(total)
        t.write('Programmer', font = style, align = 'center')
        t.forward(total)
        t.write('Musician', font = style, align = 'center')
        t.forward(total)
        t.write('Artist', font = style, align = 'center')
        t.down()

    def colourKey(t):
        t.speed(0)
        t.color('green')
        style = ('ariel', 12)
        t.penup()
        t.write('Green = Brown Hair', font = style, align ='right')
        t.right(90)
        t.forward(20)
        t.left(90)
        t.color('purple')
        t.write('Purple = Black Hair', font = style, align = 'right')
        t.right(90)
        t.forward(20)
        t.left(90)
        t.color('darkgoldenrod1')
        t.write('Yellow = Blonde Hair', font = style, align = 'right')
        t.right(90)
        t.forward(20)
        t.left(90)
        t.color('slateblue')
        t.write('Slate Blue = Ginger Hair', font = style, align = 'right')
        t.right(90)
        t.forward(40)
        t.left(90)
        t.color('green')
        t.write('Green = Male', font = style, align = 'right')
        t.right(90)
        t.forward(20)
        t.left(90)
        t.color('purple')
        t.write('Purple = Female', font = style, align = 'right')
        t.right(90)
        t.forward(40)
        t.left(90)
        t.color('darkgoldenrod1')
        t.write('Yellow = Programmer', font = style, align = 'right')
        t.right(90)
        t.forward(20)
        t.left(90)
        t.color('slateblue')
        t.write('Slate Blue = Musician', font = style, align = 'right')
        t.right(90)
        t.forward(20)
        t.left(90)
        t.color('green')
        t.write('Green = Artist', font = style, align = 'right')

def main(t, d):
    t.hideturtle()
    w = 23.5
    turtle.bgcolor('grey')
    Graph.axis(t)
    Data.axisY(t)
    Data.axisX(t, w)
    Graph.colourKey(t)
    Data.colourKey(t)

    Movement.Centre(t)
    Graph.drawBar(t, d.count_data("Hair", "Brown"), w, "Green")
    Graph.drawBar(t, d.count_data("Hair", "Black"), w, "Purple")
    Graph.drawBar(t, d.count_data("Hair", "Blonde"), w, "Darkgoldenrod1")
    Graph.drawBar(t, d.count_data("Hair", "Ginger"), w, "Slateblue")
    Graph.drawBar(t, d.count_data("Sex", "Male"), w, "Green")
    Graph.drawBar(t, d.count_data("Sex", "Female"), w, "Purple")
    Graph.drawBar(t, d.count_data("Role", "Programmer"), w, "Darkgoldenrod1")
    Graph.drawBar(t, d.count_data("Role", "Musician"), w, "Slateblue")
    Graph.drawBar(t, d.count_data("Role", "Artist"), w, "Green")
    turtle.done()



if __name__ == "__main__":
    test = DataTable()
    test.insert_data("Jacob", Name = "Jacob", Age = 22, Hair = "Brown", Role = "Programmer", Sex = "Male")
    test.insert_data("Joao", Name = "Joao", Age = 16, Hair = "Brown", Role = "Artist", Sex = "Male")
    test.insert_data("Maja", Name = "Maja", Age = 17, Hair = "Black", Role = "Artist", Sex = "Female")
    test.insert_data("Filip", Name = "Filip", Age = 17, Hair = "Blonde", Role = "Musician", Sex = "Male")
    test.insert_data("Lucas", Name = "Lucas", Age = 17, Hair = "Blonde", Role = "Musician", Sex = "Male")
    test.insert_data("Macaiah", Name = "Macaiah", Age = 17, Hair = "Ginger", Role = "Musician", Sex = "Male")
    main(t, test)