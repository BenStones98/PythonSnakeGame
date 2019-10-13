import turtle
def drawHomeWindow():
    turtle.setup(width=510, height=510) #Opens up a 510x510 pixel window.
    turtle.ht()
    turtle.clear()
    turtle.penup()
    turtle.color("red")
    turtle.goto(0,200) #Draws welcome text on screen
    turtle.write("Welcome! Click to begin...", align="center", font=(None, 25, "normal"))
    turtle.title("Ben Stones - Snake Game")
    
def drawGameWindow(): 
    turtle.clear()
    turtle.penup()
    turtle.speed(0)
    turtle.width(10)
    turtle.color("red")
    turtle.goto(-180,180)
    turtle.pendown()
    turtle.goto(180,180) #Draws the red 180 pixel sqr game board
    turtle.goto(180,-180)
    turtle.goto(-180,-180)
    turtle.goto(-180,180)
    turtle.penup()
    turtle.goto(0,0)
