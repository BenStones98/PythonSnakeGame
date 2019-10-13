import turtle
import random
import time
import window

############### GLOBAL VARIABLES ##################

currentPos = [] #2 Dimensional array of each square of the snake's x and y positions
headDirection = 0 #The direction the head of the snake is facing, given as an angle from
score = 0 #To keep track of the score
snakeSize = 0 #To keep track of the size of the snake
foodCoordinate = [0,0] # X and Y coordinates for the food's position
foodVisible = 0 #Variable to change whether a food square is visible on screen, not visible = 0, visible = 1

################### TURTLES #######################

foodTurtle = turtle.Turtle()
highScoreDisplay = turtle.Turtle()
scoreDisplay = turtle.Turtle()

#################### MAIN #########################

def initialiseGame(x,y):
    global foodVisible
    global score
    global snakeSize
    global headDirection
    foodVisible = 0 #Resets the variables needed for a new game
    score = 0 
    snakeSize = 0 
    headDirection = 0
    currentPos[:] = [] 
    highScoreDisplay.clear() #Clears the turtle displaying the high score and score - updates the outputs on the screen
    scoreDisplay.clear()
    displayHighScore() 
    window.drawHomeWindow() #Draws the initial "Home" window
    turtle.onscreenclick(playGame) #When the screen is clicked, the game begins
   

def playGame(x,y):
    global foodVisible
    global score
    window.drawGameWindow() #Draws the game window and the information needed for a new game
    food()
    foodVisible = 1
    displayScore()
    while x > -170 and x < 170 and y > -170 and y < 170: #While loop to contain the snake in the game board 
        if foodVisible == 0: #If no food is visible on the screen, a food is drawn and the variable changed to prevent infinite food-drawing loop.
            food()
            foodVisible = 1
        turtle.onkey(up,"Up")#Key bindings to rotate the direction of the snake head
        turtle.onkey(down,"Down")
        turtle.onkey(left,"Left")
        turtle.onkey(right,"Right")
        turtle.listen()
        move() #Snake is constantly moving
        x = turtle.xcor()
        y = turtle.ycor()
        if (x < foodCoordinate[0]*20+5) and (x > foodCoordinate[0]*20-5) and (y < foodCoordinate[1]*20+5) and (y > foodCoordinate[1]*20-5): #Checks for collisions with food
            foodVisible = 0 #The food is hidden, meaning another food is drawn elsewhere
            foodTurtle.clear()
            score = score + 1 #Score incremented by 1 when food has been eaten, changes to the high score and score are displayed on screen
            updateHighScore()
            displayScore()
        if len(currentPos) > 1: #If the snake is bigger than 1 square long, the position of the head is checked against the position of all the individual snake square positions from the 2d array to check for a collision with itself.
            for i in range(1,len(currentPos)): 
                if (x > currentPos[i][0]-5) and (x < currentPos[i][0]+5) and (y > currentPos[i][1]-5) and (y < currentPos[i][1]+5): #If so, the game is over. Window cleared. 
                    foodTurtle.clear()
                    scoreDisplay.clear()
                    gameOver()
    foodTurtle.clear() #If the snake collides with the edge of the game board, the game is over. Window cleared. 
    scoreDisplay.clear()
    gameOver()

def move():
    global score
    global snakeSize
    turtle.setheading(headDirection)
    turtle.color("black")
    turtle.penup()
    turtle.shape("square")
    turtle.stamp() #Snake moves forward -  stamping green squares to represent the location of the body - by an x or y value of 20 to ensure it stays in line with the game board and food. 
    turtle.fd(20) 
    if score <= 5: #Speed of the turtle is based on the length of the snake (difficulty increases)
        turtle.speed(2)
    elif 5 < score <= 15:
        turtle.speed(3)
    elif 15 < score < 25:
        turtle.speed(4)
    else:
        turtle.speed(5)
    '''
    #Line below in docstring is useful for testing - prints the 2d current position array in th4e console
    print(currentPos)
    '''
    x = turtle.xcor()
    y = turtle.ycor()
    if snakeSize > score:
        turtle.clearstamps(1)#Erases any squares in the body of the snake from the array if the body length exceeds the score (keeps the turtle at a length consistent to the score)
        currentPos.insert(0,[round(x),round(y)])
        currentPos.pop(-1)
    else:
        currentPos.insert(0,[round(x),round(y)]) #if the length of the snake drawn isnt greater than the score, a new snake position is added to the array (Also to ensure the length of the snake is consistent with the score)
        snakeSize = snakeSize + 1

def gameOver():
    displayGameOverText() #Game over information displayed on screen
    displayHighScore() 
    updatePreviousScores()
    displayPreviousScores()
    turtle.onscreenclick(initialiseGame)#Waits for a click to start another game...
    turtle.onkey(turtle.bye, "e")#...Or e to be pressed to exit
    
#################### DISPLAYS #######################
    
def displayHighScore():
    highScoreDisplay.clear() #Any existing high score display is cleared
    with open('highscore.txt', 'r') as f: #Contents of the "highscore.txt" file is saved assigned to "highscore"
        highscore = f.read()
    highScoreDisplay.ht() 
    highScoreDisplay.penup()
    highScoreDisplay.color("red") 
    highScoreDisplay.speed(0) 
    highScoreDisplay.goto(-180,-220)
    highScoreDisplay.write("High Score: " + str(highscore), align="center",font=(20)) #Highscore is then drawn on the bottom left corner of the screen

def displayScore():
    global score #Global score variable is displayed in the bottom right hand corner of the screen
    scoreDisplay.clear()
    scoreDisplay.ht() 
    scoreDisplay.penup()
    scoreDisplay.color("red") 
    scoreDisplay.speed(0) 
    scoreDisplay.goto(180,-220)
    scoreDisplay.write("Score: " + str(score), align="center",font=(20)) 

    
def food():
    foodCoordinate[0] = random.randint(-8,8) #Random x and y coordinates on the game board are generated for the food
    foodCoordinate[1] = random.randint(-8,8)
    foodTurtle.ht()
    foodTurtle.penup()
    foodTurtle.shape("square")
    foodTurtle.color("red")
    foodTurtle.goto(foodCoordinate[0]*20,foodCoordinate[1]*20) #Red square is stamped at those coordinates, multiplied by 20 to keep the food in line with the snake
    foodTurtle.stamp()
                            

def displayGameOverText():
    turtle.speed(0)
    turtle.penup()
    turtle.color("red")
    count = 0
    while True:
        count = count + 1 #"GAME OVER" flashes 3 times (whilst count counts from 0 to 2) at intervals of 0.3 seconds.
        turtle.goto(0,110)
        turtle.write("Game Over!", align="center",font=(None, 40))
        time.sleep(0.3)
        turtle.clear()
        time.sleep(0.3)
        if count > 2:
            break
    turtle.goto(0,110) #Then when the flashing has finished, "GAME OVER" and the option to play again is displayed permanently. 
    turtle.write("Game Over!", align="center",font=(None, 40))
    turtle.goto(0, 80)
    turtle.write("Click to play again", align="center", font=(None,20))
    turtle.goto(0, -155)
    turtle.write("Press 'e' to exit", align="center", font=(None,18))
    

def updateHighScore():
    global score
    with open('highscore.txt', 'r') as f: #The high score saved in the text file is extracted...
        currentHighScore = int(f.read())
    if score > currentHighScore: #It's then checked against the most recent high score...
        text_file = open("highscore.txt","w")
        text_file.write(str(score)) #If the most recent high score is greater than the one saved, the saved score is replaced by the new high score.
        text_file.close()
    
def displayPreviousScores():
    with open('recentscores.txt','r') as f: #Each line in the "recentscores" file, representing a recent score, is opened and assigned to the relevant variable
        score1=f.readline()
        score2=f.readline()
        score3=f.readline()
        score4=f.readline()
        score5=f.readline()

    turtle.goto(0,35) #The turtle then displays the recent scores. 
    turtle.write("Previous Scores:", align="center",font=(None, 10))
    turtle.goto(0,0)
    turtle.write("1. " + score1, align="center",font=(None, 10))
    turtle.goto(0,-25)
    turtle.write("2. " + score2, align="center",font=(None, 10))
    turtle.goto(0,-50)
    turtle.write("3. " + score3, align="center",font=(None, 10))
    turtle.goto(0,-75)
    turtle.write("4. " + score4, align="center",font=(None, 10))
    turtle.goto(0,-100)
    turtle.write("5. " + score5, align="center",font=(None, 10))

def updatePreviousScores():
    global score
    with open('recentscores.txt','r') as f:
    #Recent score file is opened and each recent score is assigned to a temporary score variable
        Tscore1=f.readline()
        Tscore2=f.readline()
        Tscore3=f.readline()
        Tscore4=f.readline()
    #The 5th most recent is discarded and each temporary score is "pushed down". The most recent score is saved as score 1.
    score5 = str(Tscore4)
    score4 = str(Tscore3)
    score3 = str(Tscore2)
    score2 = str(Tscore1)
    score1 = str(score)

    with open('recentscores.txt','r+') as f:
    #The file is then reopened, cleared and rewritten line by line
        f.truncate()
        f.write(score1 + "\n") #The 1st score requires a new line to be inserted after it. Can't work out why. 
        f.write(score2)
        f.write(score3)
        f.write(score4)
        f.write(score5)
        
################### MOVEMENT #####################
        
'''
For all below - 'if' statement is used to prevent the head direction turning 180 degrees and the snake doubling bakc on itself.
The head direction is given as an angle anticlockwise from the horizontal (turtle facing the right hand side of the screen)
'''
def up():
    global headDirection
    if headDirection !=270:
        headDirection = 90 


def down():
    global headDirection
    if headDirection!= 90:
        headDirection = 270
    
def left():
    global headDirection
    if headDirection != 0:
        headDirection = 180

def right():
    global headDirection
    if headDirection != 180:
        headDirection = 0
        
###################################################
        
initialiseGame(0,0)











