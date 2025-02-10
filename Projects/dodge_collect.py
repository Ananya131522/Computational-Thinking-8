#Section 1: Setup
import codesters, random
from codesters import StageClass
stage = StageClass ()
stage.disable_floor()
player = codesters.Sprite("singer")
player.set_size(0.2)
stage.set_background("erastour")
#starting object speed
object_speed = -20
#point tracker
points = 0
#Section 2: Objects
def falling_object():
    global object_speed, object_speed, points
    
    if points != 15:
        x = random.randint(-250,250)
        y = 250
        object = codesters.Sprite("butterfly", x, y)
        object.set_size(0.002)
        object.set_y_speed(object_speed)

stage.event_interval(falling_object, 1)
