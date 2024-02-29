from p5 import *


game_option = {0: "PLAY", 1: "SETTINGS"}

width = 800
height = 600


menu_w = width/2
menu_h = height/6
menu_x = width/2
menu_y = height/2





def draw_menu():
    """
    Menu with run game and settings
    """
    global menu_w, menu_h, menu_x, menu_y
    
    global setgs_x, setgs_y, setgs_w, setgs_h, menu_p
    font = create_font("C:/winsows/fonts/arial.ttf", 60)
    text_font(font)
    
    
    rectMode(mode="CENTER")
    stroke_weight(5)
    fill(200)
    rect((menu_x, menu_y), menu_w, menu_h)
    fill(200)
    rect((menu_x, menu_y+120), menu_w, menu_h)
    
    fill(0)
    stroke_weight(3)
    text("  arget Prec  sion", (width/2 - 230, height/2 -200))
    
    image(load_image("7047595.png"), width/2 - 255, 60, 100, 100)
    image(load_image("7944357.png"), width/2 +70, 110, 60, 60)
    

    for key, val in game_option.items():
        fill(0)
        if key == 0:
            text(val, (menu_x - 90, menu_y-40 + key * 120))
        else:
            text(val, (menu_x - 160, menu_y-40 + key * 120))
            
            