import turtle

filename = "smiley_emoji_mod.xpm"
fh = open(filename, "r")
colorData = fh.readline() # file handle must be open
colorData.strip() 

print(colorData)

rows, cols, numColors = colorData.split()

numColors=int(numColors)

colorDefs = []
for i in range(numColors):
    colorData = fh.readline()
    colorData.strip()
    [sym, c, color] = colorData.split()
    if (sym == '~'):
        sym = " "
    colorDefs.append([sym, color])

print(colorDefs)

turtle.bgcolor("gray40") # dark gray - try gray70 for a lighter gray
turtle.tracer(0,0)       # turns off updates to speed up plotting
t = turtle.Turtle()      # makes it easier to call the plotting functions
t.hideturtle()           # prevents the plotter sprite from appearing in your image

t.penup() # raises the pen; prevents drawing
t.pendown() # lowers the pen; begins drawing
t.goto(0, 0) # goes to the coordinates (x, y) on the canvas ((0,0) is the center)
t.dot(3, "black") # puts a dot of color of size r, and "color" is a named color

def plotIt (x,y,d,colour):
    counter = 0
    t.goto 
    

