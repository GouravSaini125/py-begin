from turtle import Turtle
import parser
class Plotter(Turtle):
    def __init__(self):
        super().__init__()

    def moveto(self,x,y):
        self.up()
        self.goto(x,y)
        self.pd()

    def set_axis(self,x=300,y=300):
        self.moveto(300,0)
        self.goto(-300,0)
        self.moveto(0,-300)
        self.goto(0,300)
        self.moveto(0,0)

    def rect(self,x,y):
            self.forward(x)
            self.left(90)
            self.forward(y)
            self.left(90)
            self.forward(x)
            self.left(90)
            self.forward(y)
            self.left(90)

    def plotxy(self,*pts):
        for pt in pts:
            self.goto(pt[0],pt[1])
           
    def polygon(self,sides,len,dir=0,fillcolor='white',linecolor='black'):
        self.color(linecolor)
        self.begin_fill()
        self.fillcolor(fillcolor)
        if not dir == 0:
            self.left(180)
        for i in range(sides):
            self.forward(len)
            if  dir ==0:
                self.left(180-((sides-2)*180)/sides)
            else:
                self.right(180-((sides-2)*180)/sides)
        self.end_fill()
        self.color('black')

    def eq_graph(self,variable,eqn,st=1,end=100):
        for i in range(st,end+1):
            eq = eqn.replace(f'{variable}',f'{i}')
           # eq = parser.expr(eq).compile()

            result = eval(eq)

            self.goto(i,result)

o = Plotter()
o.set_axis()
o.eq_graph('x','x**2')
