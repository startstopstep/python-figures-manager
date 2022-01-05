import turtle


class Drawing:
    def __init__(self):
        s = turtle.Screen()
        s.bgcolor('black')
        t = turtle.Turtle()
        t.speed(0)
        t.color('red')
        t.dot(5)
        t.goto(0, 300)
        t.goto(0, -300)
        t.goto(0, 0)
        t.goto(-300, 0)
        t.goto(300, 0)
        t.speed(4)
        t.goto(0, 0)
        t.dot(10)
        t.color('yellow')
        t.penup()
        self.t, self.s = t, s

    def draw_circle(self, r):
        self.t.goto(0, 0)
        self.t.pendown()
        self.t.circle(r)
        turtle.exitonclick()

    def draw_triangle(self, coords):
        self.t.goto(coords[0])
        self.t.pendown()
        self.t.goto(coords[1])
        self.t.goto(coords[2])
        self.t.goto(coords[0])
        turtle.exitonclick()

    def draw_rectangle(self, coords):
        self.t.goto(coords[0])
        self.t.pendown()
        self.t.goto(coords[1])
        self.t.goto(coords[2])
        self.t.goto(coords[3])
        self.t.goto(coords[0])
        turtle.exitonclick()
