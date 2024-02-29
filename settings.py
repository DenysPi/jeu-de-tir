from p5 import *



setgs_x = 200
setgs_y = 100
setgs_w = 300
setgs_h = 75

write = "OFF"

last_click_time = 0
last_click_speed = 0
click = 100
speed_match = 1


def draw_settings():
    global setgs_x, setgs_y, setgs_w, setgs_h, menu_p
    font1 = create_font("C:/winsows/fonts/arial.ttf", 25)
    text_font(font1)
    draw_mouve()
    speed()
    
        
        
    
    
    




        
        
        
        
def draw_mouve():
    global write, last_click_time
    rect_mode("CENTER")
    fill(200)
    no_stroke()
    rect(setgs_x, setgs_y, setgs_w, setgs_h)
    
    fill(110)
    rect(200,130 ,300,30)
    
    fill(200)
    triangle(setgs_x +30, 120 , setgs_x+30, 140, setgs_x+60, 130)
    triangle(setgs_x -30, 120 , setgs_x-30, 140, setgs_x-60, 130)
    
    fill(0)
    stroke(0)
    stroke_weight(3)
    text("MOUVE",setgs_x -50, setgs_y-25)
    
    fill(200)
    stroke(0)
    stroke_weight(3)
    text(write,setgs_x -22, 115)
    
    
    
    if mouse_is_pressed:
        if millis() - last_click_time > click:
            if setgs_x + 30 <= mouse_x <= setgs_x + 60 and 120 <= mouse_y <= 140 :
                write = "OFF" if write == "ON" else "ON"
            elif setgs_x - 60 <= mouse_x <= setgs_x - 30 and 120 <= mouse_y <= 140 :
                write = "ON" if write == "OFF" else "OFF"
        last_click_time = millis()
        
        
def speed():
    global speed_match
    fill(255)
    no_stroke()
    rect(setgs_x + 400, setgs_y, setgs_w, setgs_h)
    
    fill(180)
    rect(600,130 ,300,30)
    
            
        
    if write == "ON" :
        if mouse_is_pressed:
            if setgs_x + 430 <= mouse_x <= setgs_x + 460 and 120 <= mouse_y <= 140:
                speed_match += 1
            
        fill(200)
        no_stroke()
        rect(setgs_x + 400, setgs_y, setgs_w, setgs_h)
    
        fill(110)
        rect(600,130 ,300,30)
        
        fill(200)
        triangle(setgs_x +430, 120 , setgs_x+430, 140, setgs_x+460, 130)
        triangle(setgs_x +370, 120 , setgs_x+370, 140, setgs_x+340, 130)
        
        fill(0)
        stroke(0)
        stroke_weight(3)
        text("SPEED",setgs_x +350, setgs_y-25)

def draw_mouve():
    global write, last_click_time
    rect_mode("CENTER")
    fill(200)
    no_stroke()
    rect(setgs_x, setgs_y, setgs_w, setgs_h)
    
    fill(110)
    rect(200,130 ,300,30)
    
    fill(200)
    triangle(setgs_x +30, 120 , setgs_x+30, 140, setgs_x+60, 130)
    triangle(setgs_x -30, 120 , setgs_x-30, 140, setgs_x-60, 130)
    
    fill(0)
    stroke(0)
    stroke_weight(3)
    text("MOUVE",setgs_x -50, setgs_y-25)
    
    fill(200)
    stroke(0)
    stroke_weight(3)
    text(write,setgs_x -22, 115)
    
    
    
    if mouse_is_pressed:
        if millis() - last_click_time > click:
            if setgs_x + 30 <= mouse_x <= setgs_x + 60 and 120 <= mouse_y <= 140 :
                write = "OFF" if write == "ON" else "ON"
            elif setgs_x - 60 <= mouse_x <= setgs_x - 30 and 120 <= mouse_y <= 140 :
                write = "ON" if write == "OFF" else "OFF"
        last_click_time = millis()
        
        
def speed():
    global speed_match, last_click_speed
    fill(255)
    no_stroke()
    rect(setgs_x + 400, setgs_y, setgs_w, setgs_h)
    
    fill(180)
    rect(600,130 ,300,30)
        
        
    if write == "ON":
        if mouse_is_pressed:
            if millis() - last_click_speed> click:
                if setgs_x + 430 <= mouse_x <= setgs_x + 460 and 120 <= mouse_y <= 140 :
                    speed_match += 1
            last_click_speed = millis()
        fill(200)
        no_stroke()
        rect(setgs_x + 400, setgs_y, setgs_w, setgs_h)
    
        fill(110)
        rect(600,130 ,300,30)
        
        fill(200)
        triangle(setgs_x +430, 120 , setgs_x+430, 140, setgs_x+460, 130)
        triangle(setgs_x +370, 120 , setgs_x+370, 140, setgs_x+340, 130)
        
        fill(0)
        stroke(0)
        stroke_weight(3)
        text("SPEED",setgs_x +350, setgs_y-25)
    
        
    
        fill(200)
        text(str(speed_match),setgs_x +385, 115)
        
        
        

        
        
    