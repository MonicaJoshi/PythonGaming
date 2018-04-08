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
LEFT = False
RIGHT = True

# set initial values
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [1, 1]
paddle1_vel = 8
paddle2_vel = 8
paddle1_pos = HEIGHT / 2
paddle2_pos = HEIGHT / 2
score1 = 0
score2 = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    #ball_vel = [24, 18]
    #horiz_vel = random.randrange(120, 240)
    #vert_vel = random.randrange(60, 180)
    horiz_vel = random.randrange(1, 4)
    vert_vel = random.randrange(1, 4)
    #ball_vel[0] = - ball_vel[0]
    #ball_vel = [horiz_vel, vert_vel]
    
    if direction == "RIGHT":  
        # direction right and up
        ball_vel[1] = vert_vel
        ball_vel[0] = horiz_vel
        # ball position update ?
        #ball_pos[0] += ball_vel[0] * BALL_RADIUS        
        #ball_pos[1] += ball_vel[1] * BALL_RADIUS
    else:
        # direction left and down
        ball_vel[1] = vert_vel
        ball_vel[0] = -horiz_vel
        # ball position update ?       
        #ball_pos[0] += ball_vel[0] * BALL_RADIUS        
        #ball_pos[1] += ball_vel[1] * BALL_RADIUS
    

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    spawn_ball("RIGHT")
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos
    global ball_pos, ball_vel 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1,
                       "Black", "White")
    
    # collide and reflect off of left & right hand side of canvas
    if (ball_pos[0] - BALL_RADIUS <= PAD_WIDTH) and \
         (ball_pos[1] >= paddle1_pos - HALF_PAD_HEIGHT \
          and ball_pos[1] <= paddle1_pos + HALF_PAD_HEIGHT):
        #print "collision left!!!"
        #print score1, score2
        ball_vel[0] = - (ball_vel[0] * 1.1)
    elif (ball_pos[0] + BALL_RADIUS == WIDTH - PAD_WIDTH) and \
         (ball_pos[1] >= paddle2_pos - HALF_PAD_HEIGHT \
          and ball_pos[1] <= paddle2_pos + HALF_PAD_HEIGHT):
        #print "collision right!!!"
        #print score1, score2
        ball_vel[0] = - (ball_vel[0] * 1.1)
    else:
        
        #spawn_ball("RIGHT")
        if ball_pos[0] <= (BALL_RADIUS + PAD_WIDTH):
            # ball touching left gutter
            #print "touched left gutter, move right & up now"
            #ball_vel[0] = - ball_vel[0]
            score2 = score2 + 1
            #print score1, score2
            spawn_ball("RIGHT")
        elif ball_pos[0] >= ((WIDTH - PAD_WIDTH) - BALL_RADIUS):
            # ball touching right gutter
            #print "touched right gutter, move left & down now"
            #ball_vel[0] = - ball_vel[0]
            score1 = score1 + 1
            #print score1, score2
            spawn_ball("LEFT")
      

    # refelect from top and bottom frame boundries    
    if (ball_pos[1] <= BALL_RADIUS or
        ball_pos[1] >= HEIGHT - BALL_RADIUS):
        ball_vel[1] = - ball_vel[1]
    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_stats = [(0, paddle1_pos - HALF_PAD_HEIGHT),
                    (PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT),
                    (PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT),
                    (0, paddle1_pos + HALF_PAD_HEIGHT)]
    paddle2_stats = [(WIDTH - PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT),
                     (WIDTH, paddle2_pos - HALF_PAD_HEIGHT),
                     (WIDTH, paddle2_pos + HALF_PAD_HEIGHT),
                     (WIDTH - PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT)]
    # draw paddles
    canvas.draw_polygon(paddle1_stats, 5,
                            'White', 'White')
    canvas.draw_polygon(paddle2_stats, 5,
                        'White', 'White')
    
    # determine whether paddle and ball collide    
    
    
    # draw scores
    canvas.draw_text(str(score1), [(WIDTH / 2 - WIDTH / 4) , 50], 30, 'White')
    canvas.draw_text(str(score2), [(WIDTH / 2 + WIDTH / 4), 50], 30, 'White')
    
def keydown(key):
    global paddle1_vel, paddle2_vel, paddle1_pos, paddle2_pos
    
    if key == simplegui.KEY_MAP["down"]:
        if paddle2_pos < (HEIGHT - HALF_PAD_HEIGHT - paddle2_vel):
            paddle2_pos += paddle2_vel
        #paddle1_pos += paddle1_pos
        #print "keydown after" + str(paddle2_pos)
    elif key == simplegui.KEY_MAP["s"]:
        #print "keydown" + str(paddle1_pos)
        if paddle1_pos < (HEIGHT - HALF_PAD_HEIGHT - paddle1_vel):
            paddle1_pos += paddle1_vel
        #paddle1_pos += paddle1_pos
        #print "keydown after" + str(paddle1_pos)
    
    

def keyup(key):
    global paddle1_vel, paddle2_vel, paddle1_pos, paddle2_pos
    
    #print "keyup" + str(paddle1_pos)
    if key == simplegui.KEY_MAP["up"]:
        #print "keyup" + str(paddle2_pos)
        if paddle2_pos > (HALF_PAD_HEIGHT):
            paddle2_pos -= paddle2_vel
        #print "keyup after" + str(paddle2_pos)
    elif key == simplegui.KEY_MAP["w"]:
        #paddle1_pos -= paddle1_pos
        #print "keydown" + str(paddle1_pos)
        if paddle1_pos > (HALF_PAD_HEIGHT):
            paddle1_pos -= paddle1_vel
        #print "keyup after" + str(paddle1_pos)

def restart():
    new_game()

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", restart, 70)


# start frame
new_game()
frame.start()
