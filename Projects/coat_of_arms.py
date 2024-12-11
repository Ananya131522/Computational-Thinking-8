###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################

stage.set_background("tsily.webp")

q1 = codesters.Square(100, 100, 200, 'LightSkyBlue')
q2 = codesters.Square(-100, 100, 200, 'LightPink')
q3 = codesters.Square(-100, -100, 200, 'Orchid')
q4 = codesters.Square(100, -100, 200, 'LemonChiffon')

s1 = codesters.Sprite ("books15", 100, 100)
s1.set_size(0.2)
s2 = codesters.Sprite("headphones15", -100, -100)
s2.set_size(0.2)
s3 = codesters.Sprite("waves15", 100, -100)
s3.set_size(0.3)
s4 = codesters.Sprite("heart15", -100, 100)
s4.set_size(0.2)

message1 = codesters.Text("Ananya Ajaya Iyer",0,215,"MidnightBlue")
message2 = codesters.Text("I had the time of my life fighting dragons with you-TS",0,-215,"MidnightBlue")