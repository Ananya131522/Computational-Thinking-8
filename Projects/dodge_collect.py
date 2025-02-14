#Section 1: Setup
import codesters, random
from codesters import StageClass
stage = StageClass ()
stage.disable_floor()
player = codesters.Sprite("singer (1) (1)", 0,-150)
player.set_size(0.2)
stage.set_background("erastour")
#starting object speed
object_speed = -2
#point tracker
points = 0
#Section 2: Objects
def falling_object():
    global object_speed, object_speed, points
    
    if points <= 30:
        x = random.randint(-250,250)
        y = random.randint(-250,250)
        object = codesters.Sprite("butterfly (1)", 0, 600)
        object.set_size(0.2)
        object.go_to(x,y)
        object.set_y_speed(object_speed)

stage.event_interval(falling_object, 5)
# #Section 3: Collision
def collision(player,object):
    global points
    if object.get_image_name() == "butterfly (1)":
        stage.remove_sprite(object)
        points += 1
        if points >= 30:
            player.say(f"Good job! Now go get on stage!", 0.5, "White")
        else:
            player.say(f"{points}points", 0.5, "White")
player.event_collision(collision)
#Section 4: Controls
#Right Key
def go_right():
    player.move_right(10)
player.event_key("right",go_right)
def go_left():
    player.move_left(10)
player.event_key("left", go_left)