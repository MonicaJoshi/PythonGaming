# template for "Stopwatch: The Game"
import simplegui

# define global variables
time = "0:00.0"
counter = 0
timer = None
is_timer_on = False
total_stops = 0
success_stops = 0
score = "0/0"

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global time
    a = 0
    b = 0
    c = 0
    d = 0

    # get total 10s of seconds
    tens_of_secs = t // 10
    
    # calculate A
    a = tens_of_secs // 60    
    # calculate B
    b = (tens_of_secs % 60) // 10    
    # calculate C
    c = (tens_of_secs % 60) % 10    
    # calculate D
    d = (t % 10) % 10
    
    # combine the values into string, set time and return
    time = str(a) + ":" + str(b) + str(c) + "." + str(d)
    return time
    
# define event handlers for buttons; "Start", 
# "Stop", "Reset"
def reset():
    global time, timer, counter, is_timer_on, score
    global success_stops, total_stops
    counter = 0
    is_timer_on = False
    success_stops = 0
    total_stops = 0
    
    # stop the timer, update display, reset timer
    timer.stop()
    time = format(counter)
    score = str(success_stops) + "/" + str(total_stops)    
    timer = simplegui.create_timer(100, timer_handler)

def start():
    global is_timer_on
    is_timer_on = True

    # start the timer
    timer.start()
    
def stop():
    global total_stops, is_timer_on, score
    global success_stops, total_stops
    
    # stop timer, update stop count
    timer.stop()
    if is_timer_on:
        total_stops = total_stops + 1

    is_timer_on = False
    # incremet stop success count if whole second
    if counter !=0 and counter % 10 == 0:
        success_stops = success_stops + 1
   
    score = str(success_stops) + "/" + str(total_stops)

# define event handler for timer with 0.1 sec interval
def timer_handler():    
    global time, counter, score
    counter = counter + 1    
    
    # update display
    time = format(counter)
    score = str(success_stops) + "/" + str(total_stops)

# define draw handler
def draw(canvas):
    canvas.draw_text(time, [100,112], 48, "Red")
    canvas.draw_text(score, [250,30], 24, "Red")
    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game",
                               300, 200)

# register event handlers
frame.add_button("Start", start)
frame.add_button("Stop", stop)
frame.add_button("Reset", reset)
frame.set_draw_handler(draw)

timer = simplegui.create_timer(100, timer_handler)

# start frame
frame.start()

# Please remember to review the grading rubric

