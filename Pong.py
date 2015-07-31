
#Copy the entire code and paste it in www.codeskulptor.org and then click play button to enjoy the game.

# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = True
RIGHT = False
inc = 1
acc = 0

#Initialize Scores
score1 = 0
score2 = 0

#Initialize Paddle Position
paddle1_vel = [0,0]
paddle2_vel = [0,0]
paddle1_pos = [[0,((HEIGHT / 2) - HALF_PAD_HEIGHT)],[PAD_WIDTH,(HEIGHT / 2 - HALF_PAD_HEIGHT)],[PAD_WIDTH,((HEIGHT / 2) + HALF_PAD_HEIGHT)],[0,((HEIGHT / 2) + HALF_PAD_HEIGHT)]]
paddle2_pos = [[WIDTH - PAD_WIDTH - 1, (HEIGHT / 2) - HALF_PAD_HEIGHT],[WIDTH - 1,(HEIGHT / 2) - HALF_PAD_HEIGHT],[WIDTH - 1,(HEIGHT / 2) + HALF_PAD_HEIGHT],[WIDTH - PAD_WIDTH - 1, (HEIGHT / 2) + HALF_PAD_HEIGHT]]


# initialize ball_pos and ball_vel for new bal in middle of table
ball_x = WIDTH / 2
ball_y = HEIGHT / 2
ball_pos = [ball_x,ball_y]
ball_vel = [0, 0]

# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    if direction:
        ball_x = WIDTH / 2
        ball_y = HEIGHT / 2
        ball_pos = [ball_x,ball_y]
    
        xvel = random.randint(-3,-1)
        yvel = random.randint(-3,-1)
        
        ball_vel = [xvel,yvel]
        
    else:
        ball_x = WIDTH / 2
        ball_y = HEIGHT / 2
        ball_pos = [ball_x,ball_y]
    
        xvel = random.randint(1,3)
        yvel = random.randint(-3,-1)
        
        ball_vel = [xvel,yvel]    

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints 
    global ball_x, ball_y, ball_pos, ball_vel
    global inc, acc
    
    paddle1_vel = [0,0]
    paddle2_vel = [0,0]
    paddle1_pos = [[0,((HEIGHT / 2) - HALF_PAD_HEIGHT)],[PAD_WIDTH,(HEIGHT / 2 - HALF_PAD_HEIGHT)],[PAD_WIDTH,((HEIGHT / 2) + HALF_PAD_HEIGHT)],[0,((HEIGHT / 2) + HALF_PAD_HEIGHT)]]
    paddle2_pos = [[WIDTH - PAD_WIDTH - 1, (HEIGHT / 2) - HALF_PAD_HEIGHT],[WIDTH - 1,(HEIGHT / 2) - HALF_PAD_HEIGHT],[WIDTH - 1,(HEIGHT / 2) + HALF_PAD_HEIGHT],[WIDTH - PAD_WIDTH - 1, (HEIGHT / 2) + HALF_PAD_HEIGHT]]
    
    ball_x = WIDTH / 2
    ball_y = HEIGHT / 2
    ball_pos = [ball_x,ball_y]
    
    xvel = random.randint(-3,3)
    yvel = random.randint(-3,-3)
    
    ball_vel = [xvel, yvel]
    
    score1 = 0
    score2 = 0
    
    inc = 1
    acc = 0

    timer.start()


def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # update ball
    ball_pos[0] += (ball_vel[0])
    ball_pos[1] += (ball_vel[1])
            
    # draw ball
    canvas.draw_circle(ball_pos,BALL_RADIUS,2,"Red","White")
    
    # update paddle's vertical position, keep paddle on the screen
    
    # For keeping Paddle 1 within the rainge
    if paddle1_pos[0][1] > 0 and paddle1_pos[0][1] < 320 : 
        paddle1_pos[0][1] += paddle1_vel[1]
        #print paddle1_pos[0][1]
    elif paddle1_pos[0][1] <= 0 or paddle1_pos[0][1] >= 320:
        paddle1_vel[1] = 0
        if paddle1_pos[0][1] <= 0:
            paddle1_pos[0][1] = 1
        elif paddle1_pos[0][1] >= 320:
            paddle1_pos[0][1] = 319
        
    if paddle1_pos[1][1] > 0 and paddle1_pos[1][1] < 320:
        paddle1_pos[1][1] += paddle1_vel[1]
        #print paddle1_pos[1][1]
    elif paddle1_pos[1][1] <= 0 or paddle1_pos[1][1] >= 320:
        paddle1_vel[1] = 0
        if paddle1_pos[1][1] <= 0:
            paddle1_pos[1][1] = 1
        elif paddle1_pos[1][1] >= 320:
            paddle1_pos[1][1] = 319
        
    if paddle1_pos[2][1] > 0 and paddle1_pos[2][1] < 399:
        paddle1_pos[2][1] += paddle1_vel[1]
        #print paddle1_pos[2][1]
    elif paddle1_pos[2][1] <= 0 or paddle1_pos[2][1] >= 399:
        paddle1_vel[1] = 0
        if paddle1_pos[2][1] <= 0:
            paddle1_pos[2][1] = 1
        elif paddle1_pos[2][1] >= 399:
            paddle1_pos[2][1] = 398
    
    if paddle1_pos[3][1] > 0 and paddle1_pos[3][1] < 399:
        paddle1_pos[3][1] += paddle1_vel[1]
        #print paddle1_pos[3][1]
    elif paddle1_pos[3][1] <= 0 or paddle1_pos[3][1] >= 399:
        paddle1_vel[1] = 0
        if paddle1_pos[3][1] <= 0:
            paddle1_pos[3][1] = 1
        elif paddle1_pos[3][1] >= 399:
            paddle1_pos[3][1] = 398
            
     ########################
     # For keeping Paddle 2 within the rainge
    
    if paddle2_pos[0][1] > 0 and paddle2_pos[0][1] < 320 : 
        paddle2_pos[0][1] += paddle2_vel[1]
        #print paddle2_pos[0][1]
    elif paddle2_pos[0][1] <= 0 or paddle2_pos[0][1] >= 320:
        paddle2_vel[1] = 0
        if paddle2_pos[0][1] <= 0:
            paddle2_pos[0][1] = 1
        elif paddle2_pos[0][1] >= 320:
            paddle2_pos[0][1] = 319
        
    if paddle2_pos[1][1] > 0 and paddle2_pos[1][1] < 320:
        paddle2_pos[1][1] += paddle2_vel[1]
        #print paddle2_pos[1][1]
    elif paddle2_pos[1][1] <= 0 or paddle2_pos[1][1] >= 320:
        paddle2_vel[1] = 0
        if paddle2_pos[1][1] <= 0:
            paddle2_pos[1][1] = 1
        elif paddle2_pos[1][1] >= 320:
            paddle2_pos[1][1] = 319
        
    if paddle2_pos[2][1] > 0 and paddle2_pos[2][1] < 399:
        paddle2_pos[2][1] += paddle2_vel[1]
        #print paddle2_pos[2][1]
    elif paddle2_pos[2][1] <= 0 or paddle2_pos[2][1] >= 399:
        paddle2_vel[1] = 0
        if paddle2_pos[2][1] <= 0:
            paddle2_pos[2][1] = 1
        elif paddle2_pos[2][1] >= 399:
            paddle2_pos[2][1] = 398
    
    if paddle2_pos[3][1] > 0 and paddle2_pos[3][1] < 399:
        paddle2_pos[3][1] += paddle2_vel[1]
        #print paddle1_pos[3][1]
    elif paddle2_pos[3][1] <= 0 or paddle2_pos[3][1] >= 399:
        paddle2_vel[1] = 0
        if paddle2_pos[3][1] <= 0:
            paddle2_pos[3][1] = 1
        elif paddle2_pos[3][1] >= 399:
            paddle2_pos[3][1] = 398
    
    # draw paddles
    canvas.draw_polygon(paddle1_pos,2,"white",'white')
    canvas.draw_polygon(paddle2_pos,2,"white",'white')
    
    # determine whether paddle and ball collide
    #print ball_pos[0] + BALL_RADIUS
    #print paddle1_pos[1][1]
    #print paddle1_pos[2][1]
    
    if (ball_pos[0] <= BALL_RADIUS) and (ball_pos[1] <= paddle1_pos[2][1]) and (ball_pos[1] >= paddle1_pos[1][1]) :
        ball_vel[0] = - ball_vel[0]
    elif ball_pos[0] <= BALL_RADIUS:
        score2 += 1
        spawn_ball(RIGHT)   
        
       
    if (ball_pos[0] >= WIDTH - 1 - BALL_RADIUS) and (ball_pos[1] >= paddle2_pos[0][1]) and (ball_pos[1] <= paddle2_pos[3][1]):
        ball_vel[0] = - ball_vel[0]
    elif ball_pos[0] >= WIDTH - 1 - BALL_RADIUS:
        score1 += 1
        spawn_ball(LEFT)
    
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
        
    if ball_pos[1] >= HEIGHT - 1 - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    
    # draw scores
    canvas.draw_text(str(score1),[(WIDTH / 2) - 50, HEIGHT / 8], 50, "White")
    canvas.draw_text(str(score2),[(WIDTH / 2) + 25, HEIGHT / 8], 50, "White")

def keydown(key):
    #print key
    global paddle1_vel, paddle2_vel
    if key == 40:
        paddle2_vel[1] += inc
    elif key == 38:
        paddle2_vel[1] -= inc
        
    if key == 87:
        paddle1_vel[1] -= inc
    elif key == 83:
        paddle1_vel[1] += inc
    
    
def keyup(key):
    global paddle1_vel, paddle2_vel

def tick():
    global ball_vel
    ball_vel[0] = ball_vel[0] * 1.001
    ball_vel[1] = ball_vel[1] * 1.001
    
def Restart():
    new_game()
    pass    

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
timer = simplegui.create_timer(50,tick)
Restart = frame.add_button( "Restart ", Restart)

# start frame
frame.start()
timer.start()
new_game()
