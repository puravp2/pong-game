import play #loDING THE PLAYMODULE LIBARY
import pygame#important pyton game
import random # LOADINGTHE RANDOM LIBARY


w = 300 # defining global varible for horizontal of court
h = 400 # defining global varible for vertical of court
wh = w/2#  defiing global varible for horzontal size of court
hh = h/2# defining global varible for vertical size of court
score = 0# global varible for points
speed = 3 # global varible for velocity of ball

@play.when_program_starts # this create a keyfram to start the game function as soon as you press run
def do():# This is the function to make the backroumd.
  play.set_backdrop("brown")# this set the backround to Dark purple/blue

court = play.new_box(# this function is going to make the box for ping pong court.
  color = (65,44,25),# set the curt color lighter blue/purple
  x = 0,# x coordinate of court
  y = 0,# y coordinate of court
  width = w, #use global varible to populate  local varible
  height = h,# use global varible to populate  local varible
)

paddle = play.new_box(#this is going to make the pattle.
  color = "red",#Thsi si going to set the paddle color to red.
  width = 50,# this is the width of the paddle.
  height = 10,# THis is the height of the paddle
  x = 0,# THis is the x corrdinete of the paddle.
  y = -hh + 10# THis is the y corrdinate for the paddle.
  )

ball = play.new_circle(# THis is the function for a ball.
  color ="blue",# This function makes the ball bluw
  radius = 10,# THis function indacates the radduis of the ball
  x = 0,# This deatermns the x corrdinate of the bal.
  y = hh - 30,# THis detramins the y corrdinate of the ball.
  angle = random.randint(210,330)# THis the angle to call will bounce to.
)
# creating and initilizing a varible for the text of the score
# and initilizing it wiht a build in function new text from play module
score_text = play.new_text(# Tis is the finction for the text "SCORE".
 words = "SCORE: " + str(score),# THis function are for the words being used.
  x = 0,#THis si the x cordinate for the score -text
  y = hh + 15,# THis si the y corrndiate for the score.
  font = None,# THis si for the font
  color = "black", # THis is thefont color.
  )

@play.repeat_forever# this line fo code creates a key fram to do the following code as long as the game is playing
def do(): #define the function or subrutine
  global score# calling for the global varible score
  paddle.x = play.mouse.x # DOT notation o recall the X parameter of the paddle and reasign valut to match mouse X coordinates.
  if( play.mouse.x < -wh + paddle.width/2): 3 # THis si the if staemnt for the mouse ont he bottom of the box.
  paddle.x = -wh + paddle.width/2
# THis is the else stament for paddel of x cornidate and y corndiate.
  if(play.mouse.x > wh - paddle.width/2):#THis is the play mouse function and the if staemnt.
    paddle.x = wh - paddle.width/2# THsi si the if stament for the paddel of the x cordiante.
  ball.move(speed)# this is the ball speed and hwo the ball moves int hat directuon and the speed.
    #bounce off the top/bottom of the screen
  # Ensure that the paddle is not off the playfeild.
  #top wall
  if(ball.y + ball.radius > hh):# THis si the if statemnt for the bal radius.
    ball.angle = 360 - ball.angle# THis fucntion is the ball for the bottom walll.
    #bottom wall
  if(ball.y + ball.radius < -hh):# This is the if staemnt for the ball.x and ball.y.
    ball.angle = 360 - ball.angle# THis is the ball angle for the direction of 360.
    score -=1# THIs function indcates the sscore of the agame.
  # bounce off left/right : 180 -angle
  #right wall
  if(ball.x + ball.radius > wh): # THis is fucntion forn ball.x and ball.y for th -raduis.
   ball.angle = 180 - ball.angle# This si the balla angle for the 180 degres.
  #left wall
  if(ball.x - ball.radius < -wh):# THis is also the function for ball.xand y for 180 degress.
    ball.angle = 180 - ball.angle
    #make sure it bounces as if it has hit the bottom , and give it a little change of trajectory00
  if (ball.is_touching(paddle)): # THis fucntion tells the ball to touch the paddle and the socre will work.
    ball.angle = 360 -ball.angle + random.randint(-30,30)# THis is for the ball degree of 360 degress.
    ball.angle %= 360# THIs si the angle angle function.
    score += 1
  # make sure that the ball goes up after hitting paddle
    if(ball.angle < 20):# this is the angle of greather than 20.
      ball.angle = 20# This also the angle for 20 degres.
    elif(ball.angle > 160):# THis si the else stament.
      ball.angle = 160 # This si the function forn 160 degres angle.                 
    score+= 1# If this functin works the dcore will go up nby 1.
    if(score==1):# if stament for score.
      paddle.width -=5#THIs si the wiodth for paddle

  ball.angle %= 360 #ensure angle is vaild
  score_text.words = "SCORE:" + str(score)# THis is the score text 
play.start_program()
  # THIsnfunction amkes sure the prgram starts.l
