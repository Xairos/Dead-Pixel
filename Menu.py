import os
import random
import pygame
import math
import glob
from pygame.locals import *

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()

size = (1024,768)
done = False
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("DEAD PIXEL")

black    = (   0,   0,   0)
grey     = ( 130, 130, 130)
white    = ( 255, 255, 255)
green    = (   0, 255,   0)
red      = ( 255,   0,   0)

gravity=2

asdf="bleh"

x_speed=0
y_speed=0

#Set up quadratic sun and moon movement
moon_x=-300
moon_y=0
sun_x=-300
sun_y=0

#Set various game variables
suncycle=True
cycleanim=False
night_alpha=0
offset = 0
mountain_offset = 0
cloud_offset = 0
house_offset = 0
run_switch = True
run_time = 0
start_frame = 0
start_state = False
page = 2
dropdown = False
saveselect = ""
loading_screen = False
closing_screen = False
load_complete = False
loading_fillscreen = 0
loading_closingscreen = 1200
reset_loading_fillscreen = 0
various_grasses = []
for i in range(33):
        various_grasses.append(i*32)

#Set up second surface for alpha 'blitting', MUCH FASTER THAN SET_ALPHA DRAWING
night = pygame.Surface((1024,768))  # the size of your rect
night.set_alpha(0)                # alpha level
night.fill((39,43,48))           # this fills the entire surface

#Function for screen transitions, works in an aperture-like manner
def load_anim(x):
        if loading_screen == True:
                pygame.draw.rect(screen,black,[0,0,1024,384-x/3])
                pygame.draw.rect(screen,black,[0,0,512-x/2,784])
                pygame.draw.rect(screen,black,[0,384+x/3,1024,768])
                pygame.draw.rect(screen,black,[512+x/2,0,1024,768])

def close_anim(x):
        if closing_screen == True:
                pygame.draw.rect(screen,black,[0,0,1024,384-x/3])
                pygame.draw.rect(screen,black,[0,0,512-x/2,784])
                pygame.draw.rect(screen,black,[0,384+x/3,1024,768])
                pygame.draw.rect(screen,black,[512+x/2,0,1024,768])

#Set up mouse positions [x and y coordinates]
pos = pygame.mouse.get_pos()
x_cross=pos[0]
y_cross=pos[1]
#Make the mouse pointer invisible
pygame.mouse.set_visible(0)

#Draw mouse crosshairs
def draw_cross(screen,x,y):
        pygame.draw.line(screen,red,[x-6,y],[x-2,y],2)
        pygame.draw.line(screen,red,[x+6,y],[x+2,y],2)
        pygame.draw.line(screen,red,[x,y-6],[x,y-2],2)
        pygame.draw.line(screen,red,[x,y+6],[x,y+2],2)

#Using a function for loading pictures is much easier
def load_image(x,i):
    #load an image from the data directory with per pixel alpha transparency.
    return pygame.image.load(os.path.join("data\\" + x, i)).convert_alpha()

def name_pass(x):
        fo = open("saves\LEVEL.pass", "w+")
        fo.write(x);
        fo.close()

#Function for loading save files
def svgm_list():
        list = []
        for files in glob.glob(os.path.join("saves", "*.svgm")):
            list.append(files[6:files.find('.')])
        return list

savelist = svgm_list()

#Load game resources
day = load_image("backgrounds","lightbg.png")
sun = load_image("backgrounds","sun.png")
moon = load_image("backgrounds","moon.png")
mountains = load_image("backgrounds","mountains_old.png")
clouds = load_image("backgrounds","clouds.png")

dirt = load_image("tiles","dirt.png")
grass = load_image("tiles","grass1.png")

player = load_image("player","sprite.png")
player_running = load_image("player","run.png")

red_gun = load_image("player","red_gun.png")

start = load_image("menu","start.png")
start2 = load_image("menu","start2.png")
logo = load_image("menu","logo.png")

house = load_image("scenery","house1.png")

myfont = pygame.font.Font("data\\fonts\\WONDER.ttf", 25)

#Start game music
pygame.mixer.music.load(os.path.join("data\\music", "titlescreen.ogg"))
pygame.mixer.music.play(-1)

#set volume to a non-destructive level(remove it later)
pygame.mixer.music.set_volume(0.2)
      
joystick_count=pygame.joystick.get_count()
if joystick_count == 0:
    # No joysticks!
    print ("No joysticks connected. Defaulting to KO-MODE")
else:
    # Use joystick #0 and initialize it
    my_joystick = pygame.joystick.Joystick(0)
    my_joystick.init()

#Main game loop begins
while done == False:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_a:
                                if not loading_screen:
                                        page -= 1
                                        loading_screen = True
                        if event.key == pygame.K_d:
                                if not loading_screen:
                                        page += 1
                                        loading_screen = True
                        if event.key == pygame.K_RETURN and page == 2:
                                #import benSCS_savestest.py
                                closing_screen = True
                                name_pass(saveselect)
                if event.type == pygame.JOYBUTTONDOWN:
                        if my_joystick.get_button(0):
                                #change this, 0 is A button
                                page += 1
                if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                                print(str(x_cross) + "," + str(y_cross))
                                if page == 1:
                                        if pygame.Rect(675,300,75,70).collidepoint(x_cross,y_cross):
                                                dropdown = not dropdown
                                        for i in range(len(savelist)):
                                                if pygame.Rect(300,370+i*70,375,70*(i+1)).collidepoint(x_cross,y_cross):
                                                               saveselect = savelist[i]
        if joystick_count != 0:
                
                # This gets the position of the axis on the game controller
                # It returns a number between -1.0 and +1.0
                horiz_axis_pos= my_joystick.get_axis(0)
                #NOT USING:vert_axis_pos= my_joystick.get_axis(1)   
                # Move x according to the axis. We multiply by 10 to speed up the movement.
                if horiz_axis_pos < -0.1:
                        page -= 1
                if 0.1 > horiz_axis_pos > -0.1:
                        page = 2
                if horiz_axis_pos > 0.1:
                        page += 1

        #Update mouse positions
        pos = pygame.mouse.get_pos()
        x_cross=pos[0]
        y_cross=pos[1]
        
        #Moon and sun calculations
        if suncycle:
                sun_y = (1/50*(sun_x - 512))**2 + 50
                sun_x+=5
                if sun_x > 1080:
                        suncycle = False
                        moon_x = -300
        else:
                moon_y = (1/50*(moon_x - 512))**2 + 50
                moon_x+=5
                if moon_x > 1080:
                        suncycle = True
                        sun_x = -300

        if sun_x > 900:
                if night_alpha > 250:
                        night_alpha = 255
                else:
                        night_alpha += 5
        if moon_x > 900:
                if night_alpha < 5:
                        night_alpha = 0
                else:
                        night_alpha -= 5
        
        #Set night surface transparency                
        night.set_alpha(night_alpha) 
        #Draw images and surfaces to screen
        screen.blit(day, (0,0))
        screen.blit(night, (0,0))
        screen.blit(sun, (sun_x,sun_y))
        screen.blit(moon, (moon_x,moon_y))

        #Mountain scrolling, based on an increasing offset
        for i in range(2):
                screen.blit(mountains, (i*3072-mountain_offset,0))
        mountain_offset += 1
        if mountain_offset >= 3072:
                mountain_offset = 0

        #Blit running frames based on time since last frame
        if run_switch == True:
                screen.blit(player_running, (20,558))
                run_time += 1
                if run_time > 8:
                        run_time = 0
                        run_switch = False
        else:
                screen.blit(player, (20,558))
                run_time += 1
                if run_time > 8:
                        run_time = 0
                        run_switch = True

        screen.blit(red_gun, (25,579))

        #Draw dirt, self explanatory
        for i in range(32):
                screen.blit(dirt, (i*32,736))
                screen.blit(dirt, (i*32,704))
                screen.blit(dirt, (i*32,672))
                screen.blit(dirt, (i*32,640))

        for i in range(34):
                screen.blit(grass, (i*32-offset,608))
        offset += 7
        if offset >= 32:
                offset = 0

        if loading_screen:
            loading_fillscreen += 50
            if loading_fillscreen >= 1200:
                loading_fillscreen = reset_loading_fillscreen
                loading_screen = False

        if closing_screen:
                loading_closingscreen -= 30
                #print(loading_closingscreen)
                #print(load_complete)
                if loading_closingscreen <= -50:
                        load_complete = True
                        pygame.mixer.music.fadeout(1000)
        #check for loading completion
        if load_complete:
                exec(compile(open("Main.py").read(), "Main.py", 'exec'))
                        

        #PAGE 1 BLOCK
        if page == 1:
                screen.blit(logo, (302,40))
                pygame.draw.rect(screen,white,[300,300,450,70],0)
                pygame.draw.rect(screen,black,[300,300,375,70],5)
                pygame.draw.rect(screen,black,[300,300,450,70],5)
                to_write = myfont.render(saveselect, 1, (0,0,0))
                screen.blit(to_write, (310, 320))
                if dropdown:
                        pygame.draw.polygon(screen,black,[(685,355),(710,315),(735,355)],5)
                        pygame.draw.rect(screen,white,[300,370,375,70*len(savelist)])
                        pygame.draw.rect(screen,black,[300,300,375,70],5)
                        pygame.draw.rect(screen,black,[300,300,375,70*(1+len(savelist))],5)
                        for i in range(len(savelist)):
                                to_write = myfont.render(savelist[i], 1, (0,0,0))
                                screen.blit(to_write, (310, 390 + i * 70))
                                pygame.draw.line(screen,black,[300,370 + i * 70],[675,370 + i * 70],5)
                else:
                        pygame.draw.polygon(screen,black,[(685,315),(710,355),(735,315)],5)
                
        #PAGE 2 BLOCK
        if page == 2:
                screen.blit(logo, (302,40))
                if start_frame <= 50:
                        start_frame += 1
                else:
                        start_frame = 0
                        start_state = not start_state
        
                if start_state:
                        screen.blit(start, (352,420))
                else:
                        screen.blit(start2,(352,420))
                        
        load_anim(loading_fillscreen)
        draw_cross(screen,x_cross,y_cross)
        close_anim(loading_closingscreen)
        #Update screen via display.flip()
        pygame.display.flip()
        #Cap framerate at 60 FPS
        clock.tick(60)
pygame.quit()
