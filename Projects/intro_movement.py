#section 1: Setup
import codesters
from codesters import StageClass
stage = StageClass()

stage.set_background("moon")
s1 = codesters.Sprite("person1",0,-200)
s1.set_size(0.5)



#section 2: define controls
def move_up(sprite):
    sprite.move_up(5)

def move_down(sprite):
    sprite.move_down(5)

def move_left(sprite):
    sprite.move_left(5)

def move_right(sprite):
    sprite.move_right(5)


#section 3: define hide and show
def hide(sprite):
    sprite.hide()
def show(sprite):
    sprite.show()
def turn_left(sprite):
    heading = sprite.heading
    sprite.set_heading(heading + 1)
def turn_right(sprite):
    heading = sprite.heading
    sprite.set_heading(heading - 1)
def forward(sprite):
    sprite.forward(5)
def draw(sprite):
    sprite.pen_down()
def stop_drawing(sprite):
    sprite.pen_up()
def erase(sprite):
    sprite.pen_clear()
def red_pen(sprite):
    sprite.set_color("red")
def green_pen(sprite):
    sprite.set_color("green")
#section 4: bind controls to specific keys
s1.event_key("up",move_up)
s1.event_key("down", move_down)
s1.event_key("left",move_left)
s1.event_key("right", move_right)
s1.event_key("h", hide)
s1.event_key("g", show)
s1.event_key("e", turn_left)
s1.event_key("q", turn_right)
s1.event_key("r", forward)
s1.event_key("y", draw)
s1.event_key("u", stop_drawing)
s1.event_key("i", erase)
s1.event_key("o",red_pen)
s1.event_key("p",green_pen)
#section 5:reminder message
print("Happy Hunger Games, and may the odds be EVER in your favor! Go into ports to play")