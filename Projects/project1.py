###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################

stage.set_background ("winter")

q1 = codesters.Square(100, 100, 200,'blue')
q2 = codesters.Square(-100, 100, 200,'yellow')
q3 = codesters.Square(-100, -100, 200,'red')
q4 = codesters.Square(100, -100, 200,'green')

s1 = codesters.Sprite("kitten.gif", 100, 100)
s2 = codesters.Sprite("flower.gif", -100, -100)
s2.set_size(0.5)
s3 = codesters.Sprite("paint pallet.png", -100, 100)
s3.set_size(0.1)
s4 = codesters.Sprite("cardinal", -100, -100)
s4.set_size(0.1)


message1 = codesters.Text("My name is Emimae Yamada-Morigeau",0,220,"red")
message2 = codesters.Text("This is my message",0,-200,"black")