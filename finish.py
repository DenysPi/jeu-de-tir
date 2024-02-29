from p5 import *


width = 800
height = 600

def draw_finish(score):
    
    no_stroke()
    global width, height
    rect_mode("CENTER")
    fill(0,0,139)
    rect(width/2, height/2, width ,height)
    fill(255)
    stroke(0)
    stroke_weight(10)
    rect(width/2, height/2, width-100 ,height-100)
    
    
    text("Score: " + str(score), (120, 100))

