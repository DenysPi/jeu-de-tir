from p5 import *
import random
from math import sqrt
import time

from menu import draw_menu

from settings import draw_settings


from finish import draw_finish

###############
width = 800
height = 600
################
settings = False
menu_p = True
game = False
finish = False
################
mouve = False
chance = None

################
menu_w = width/2
menu_h = height/6
menu_x = width/2
menu_y = height/2

speed_x= 0
speed_y = 0 

start_mouve =True

timer = True
def setup():
    global img, img2, img3, font, start_chrono
    size(width, height)
    font = create_font("C:/winsows/fonts/arial.ttf", 60)
    text_font(font)
    
    
    
def draw():
    """foncton principan that run all fonctins"""
    global score, game_over, count_chrono, start_chrono, timer, game, target, finish, write, speed_match, speed_x, speed_y, start_mouve
    
    from settings import write
    from settings import speed_match
    
    
    background(0, 0, 139)
    
    if menu_p:
        draw_menu()
    elif settings:
        draw_settings()
        start_mouve = True
    
    elif game:
        
        add_mouve_and_speed()
             
        
            
        if mouve:
            target.mouvement()
            
        if timer:
            start_chrono = time.time()
            timer = False
        count_chrono = time.time()
        target.object_shoot()
        
        
        add_mouve_and_speed()
            
        

        fill(0, 0, 205)
        stroke(0)
        stroke_weight(1)

        rect((0, 0), width * 2, 140)

        fill(0)

        text_font(font, 60)
        text("Score: " + str(score), (8, 10))
        text_font(font, 50)
        
        text("Timer: " + str(30 - int((count_chrono - start_chrono))), (500, 10))

        if count_chrono - start_chrono > 30:
            draw_finish(score)
            finish = True
    if not menu_p:
        back()        
            
            
        

        

def mouse_pressed():
    """fonction click start game or settings"""
    global score, menu_p, target, mouve, settings, game, timer, chance
    if menu_p:
        if menu_x - menu_w/2 <= mouse_x <= menu_x + menu_w/2 and menu_y - menu_h/2 <= mouse_y <= menu_y + menu_h/2:
            menu_p = False
            game = True
            timer = True
            score = 5
            
            target = Object() 
        if menu_x - menu_w/2 <= mouse_x <= menu_x + menu_w/2 and menu_y + 70<= mouse_y <= menu_y + 120 + menu_h:
            menu_p = False
            settings = True
            game = False
    if settings:
        pass        
    
    if game:
        
        if target and not finish:
            chance = random.randint(1, 3) == 2
            d = distance(mouse_x, mouse_y, target.x, target.y)
            if d < target.size / 4:
                score += 10
            elif d < target.size:
                score += 5
            elif mouse_y > 70:
                score -= 5
            
            target.new()
            
            
            
        


    
def distance(x1, y1, x2, y2):
    """fonction calcule the distance between 2 points"""  
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

def back():
    """button back to menu"""
    global settings, menu_p, game, finish, timer
    image(load_image("1584808-200.png"), 750 , 0, 50, 50)
    if mouse_is_pressed and 750 <+ mouse_x <= 800 and 0 <+ mouse_y <= 50:
        settings = False
        menu_p = True
        game = False
        finish = False
        timer = False
        
def add_mouve_and_speed():
    global mouve, speed_y, speed_x, start_mouve
    if write == "ON":
        mouve = True
        if start_mouve:
            speed_y = speed_match
            speed_x = speed_match
            start_mouve = False
    
class Object:
    """create a target"""
    def __init__(self):
        self.new()

    def new(self):
        self.x = random.randint(30, width-30)
        self.y = random.randint(100, height-30)
        self.size = random.randint(30, 70)

    def object_shoot(self):
        fill(236,202,0)
        stroke(204,204,0)
        ellipse((self.x, self.y), self.size, self.size)
        fill(255, 0, 0)
        stroke(139,0,0)
        ellipse((self.x, self.y), self.size/2, self.size/2)

    def mouvement(self):
        global mouve, speed_x, speed_y
        
        if mouve:
            if self.x<10 or self.x>width-10:
                speed_x = -speed_x
            if self.y<100 or self.y >height-10:
                speed_y = -speed_y
            self.x = self.x + speed_x
            self.y = self.y + speed_y



if __name__ == "__main__":
    run()
