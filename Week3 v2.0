# template for "Stopwatch: The Game"
import simplegui

# define global variables
time = 0
tries = 0
successes = 0
tries2 = 0
successes2 = 0
running = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    a = "0"
    bc = "0"
    d = "0"
    a = (t//600) 
    bc = ((t/10) % 60)
    d = t % 10
    #check for leading zero, if not add one
    if bc < 10:
        z = "0"
        return str(a) + ":" + str(z) + str(bc) + "." + str(d)
    else:
        return str(a) + ":" + str(bc) + "." + str(d)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def button_start():
    global running
    timer.start()
    running = True

def button_stop():
    global tries2, successes2, time, running
    timer.stop()
    if running:
        if time % 10 == 0:
            tries2 += 1
            successes2 += 1
        else:
            tries2 += 1
    running = False

def button_reset():
    global time, tries, successes, tries2, successes2
    time = 0
    tries = 0
    successes = 0
    tries2 = 0
    successes2 = 0
    
def key_handler(key1):
    """this key handler increments player 1 if the letter A is pressed,
       and player 2 if the letter L is pressed - other keys have no effect"""
    global tries, successes, time, running, tries2, successes2
    if key1 == 76:
        if running:
            if time % 10 == 0:
                tries += 1
                successes += 1
            else:
                tries += 1
    if key1 == 65:
        if running:
            if time % 10 == 0:
                tries2 += 1
                successes2 += 1
            else:
                tries2 += 1
    else:
        pass    
    

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global time
    time += 1

# define draw handler
def draw_handler(canvas):
    global time
    canvas.draw_text(str(format(time)), [95,225], 84, 'Black')
    canvas.draw_text((str(successes) + '    /    ' + str(tries)), [300, 50], 24, 'Green')
    canvas.draw_text("Player 2:", [300,25], 24, 'Green')
    canvas.draw_text((str(successes2) + '    /    ' + str(tries2)), [10, 50], 24, 'Green')
    canvas.draw_text("Player 1:", [10,25], 24, 'Green')
   
# create frame
frame = simplegui.create_frame("Stopwatch: The game", 400, 400)
frame.set_canvas_background('White')
frame.set_draw_handler(draw_handler)
frame.set_keydown_handler(key_handler)
frame.add_label("Player 1 key is: A")
frame.add_label("Player 2 key is: L")
                
# register event handlers
button1 = frame.add_button('Start', button_start, 100)
button2 = frame.add_button('Stop', button_stop, 100)
button3 = frame.add_button('Reset', button_reset, 100)
timer = simplegui.create_timer(100, timer_handler)

# start frame
frame.start()


# Please remember to review the grading rubric
