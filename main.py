import turtle
import random
def createTurtles(num):
  turtles = []
  for x in range(num):
    newTurtle = turtle.Turtle()
    newTurtle.color('white')
    newTurtle.penup()
    newTurtle.speed(0)
    turtles.append(newTurtle)
  return turtles

def positionTurtles(turtles):
  xCor = 0
  for x in range(len(turtles)):
    turtles[x].goto(xCor, 0)
    xCor -= 10
  

def moveTurtles(turtles):
  # Get current positions for all turtles except for the last one since no one is teleporting in its position
  length = 20
  OLD_POSITIONS = []

  for i in range(len(turtles) - 1):
    OLD_POSITIONS.append(turtles[i].position())
  
  for i in range(len(turtles)):
    if (i == 0):
      # move the first turtle, which allows for the turtles to keep moving to new positions for each function call
      turtles[i].forward(length)
    else:
      # For every turtle, go to the old position of the previous turtle
      x_cor, y_cor = OLD_POSITIONS[i - 1]
      turtles[i].goto(x_cor, y_cor)
    
def turnTurtles(turtles, count):
  angle = 30
  diff = int(angle / len(turtles))
  for turtle in turtles:
    if count <= 5:
      turtle.left(angle)
    else:
      turtle.right(angle)
    angle -= diff
    




def checkWindowBoundaries(turtles, width, height):
  in_bounds = True
  X_COORD = turtles[0].xcor()
  Y_COORD = turtles[0].ycor()
  
  # If they get out of the window or touch the border then it's out of bounds 
  if ((X_COORD >= width or X_COORD <= -width) or (Y_COORD >= height or Y_COORD <= -height)):
    in_bounds = False
  return in_bounds

def main():
  # (400, 300) class tuple
  # Turtle setup  
  WINDOW = turtle.Screen()
  
  WINDOW.bgcolor('black')
  SCREEN_DIM = WINDOW.screensize()
  NUM_TURTLES = 12
  MY_TURTLES = createTurtles(NUM_TURTLES)
  positionTurtles(MY_TURTLES)
  moveTurtles(MY_TURTLES)

  i = 0
  count = 0
  while (checkWindowBoundaries(MY_TURTLES, SCREEN_DIM[0], SCREEN_DIM[1])):
    moveTurtles(MY_TURTLES)
    turnTurtles(MY_TURTLES, count)
    count += 1

    if (count >= 10):
      count = 0
    
  WINDOW.exitonclick()
main()

# pretty good but You'd probably want to make the turning a little more varied with random, and more turtles, and smoother rendering