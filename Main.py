import os
import random
import pygame
import math
from pygame.locals import *

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()

size = (1024,768)
done = False
clock = pygame.time.Clock()
flags = FULLSCREEN
screen = pygame.display.set_mode(size)
pygame.display.set_caption("DEAD PIXEL")

black    = (   0,   0,   0)
grey    =  ( 130, 130, 130)
white    = ( 255, 255, 255)
green    = (   0, 255,   0)
red      = ( 255,   0,   0)
darkbg_color = (65,65,65)

loading_fillscreen = 0

def load_anim(x):
        if loading_screen == True:
                pygame.draw.rect(screen,black,[0,0,1024,384-x/3])
                pygame.draw.rect(screen,black,[0,0,512-x/2,784])
                pygame.draw.rect(screen,black,[0,384+x/3,1024,768])
                pygame.draw.rect(screen,black,[512+x/2,0,1024,768])

closing_screen = False
loading_closingscreen = 1200
switch_screen = False

def close_anim(x):
        if closing_screen == True:
                pygame.draw.rect(screen,black,[0,0,1024,384-x/3])
                pygame.draw.rect(screen,black,[0,0,512-x/2,784])
                pygame.draw.rect(screen,black,[0,384+x/3,1024,768])
                pygame.draw.rect(screen,black,[512+x/2,0,1024,768])
                #pygame.draw.rect(screen,black,[0,0,1024,784,], x)
gravity=2

save="nothing"

switch_running = 0
running = 1
idle_check = 0
idle_switch = 0
idle = 1

x_speed=0
y_speed=0

health = 20
air_value = 10
last_breath = 0

direction = 1

x_coord=493
y_coord=325

stupid_variable = 0

#scroll
x_screen = x_coord
y_screen = y_coord
scroll_x = 0
scroll_y = 0
scroll_change = 0
return_x = 0
return_y = 0

pos = pygame.mouse.get_pos()
x_cross=pos[0]
y_cross=pos[1]

pygame.mouse.set_visible(0)

#all lists for foreground and collision
level_walls_red=[]
level_walls_ground=[]
level_walls_r_edge = []
level_walls_l_edge = []
level_walls_d_edge = []
level_top=[]
level_air=[]
level_side_left = []
level_side_right = []
level_bottom = []
water = []
water_grounds = []
house_floors = []
house_ceilings = []
house_walls = []
ladders = []
trees = []
enemy_crawler = [] #[x coord, y coord, alive(1) or dead(2), direction(right 1)(left 2), walking or not]
enemy_crawler_range = []
enemy_puffpuff = []
enemy_puffpuff_range = []
bridges = []
level_top_bridges = []
bridges_right = []
bridges_left = []
enemy_flying = []
enemy_flying_range = []

fences = []
cactus = []
wells = []

#NEW LISTS FOR FOREGROUND
rocks = []
rock_right_corners = []
rock_left_corners = []
rock_double_corners = []
rock_ground = []

cave = []
cave_right_corners = []
cave_left_corners = []
cave_double_corners = []
cave_ground = []

sands = []
sand_right_corner = []
sand_left_corner = []
sand_double_corners = []
sand_grounds = []

lavas = []

brick_grounds = []
bricks = []
brick_left_corners = []
brick_right_corners = []

icy = []
ice_right_corners = []
ice_left_corners = []
ice_double_corners = []
icy_grounds = []

mg_rock_ground = []
mg_cave_ground = []
mg_sand_grounds = []
mg_lavas = []
mg_brick_grounds = []
mg_icy_ground = []

#all lists for middleground, (put non collidable stuff in here too, e.g. enclosed ground?)
house_insides = []
mg_ground = []

#water speed
water_x = 0
water_y = 0
use_water = False
in_water = False
in_deep_water = False
drowning = False
press_key_f = False

#next level
next_level = []
go_to_level = ""
previous_level = ""
loading_screen = True
door_change = 0
middleground = []
background = []
enemy_levelpng = []
previous_level_music = ""

#talk to the village people
talking = False
number_villagers = []
level_text = []
press_enter = False
villager = []
villager_number = 0
write_text = False
villager_move = 0
villager_speed = 5

#gun stuff
gun_color = "red"
gun_collide_remove = []
crawler_reverse = False
flying_reverse = False
gun_count = 0
gun_remove = False
gun_list_remove = []
gun_collide_list = []
gun_collidex = 0
gun_collidey = 0
gun_list = []
gun_speed = []
gun_x_speed = 0
gun_y_speed = 0
x_distance = 0
y_distance = 0
total_distance = 0

#CHANGE GUN COLOR
gun_color_changer = []

#signs
sign_start = 0
at_sign = False
number_sign = []
sign_text = []
read_sign = False
signs = []
sign_number = 0

#shift run
lshift_press = False
a_press = False
d_press = False
move_left = False
move_right = False
shift_run = False

#checking on stuff
w_press = False

#houses
houses = []

#get rid of jitter:
ground_count = 0

#all stuff for enemies
#get rid of a crawler
knockback = False
knockback_left = False
knockback_right = False
change_knockback = False
no_knockback = 0
knockback_direction = 1
#crawler
enemy_crawler_dieing = []
change_crawler_die_list = False
#puffpuff
enemy_puffpuff_health = []
enemy_puffpuff_dieing = []
change_puffpuff_die_list = []
#flying
enemy_flying_dieing = []
change_flying_die_list = False
enemy_flying_health = []

#ALL THE COLLECTABLES!!!
collectibles = []
collectibles_remove = []
collectible_count = 0
collectibles_avaliable = 0

#SWITCHES
switch = []
switch_count = 0
switch_press_count = 0

#SWITCH TIMES
time_trial = False
time = []
time_bar_percent = 0
time_bar_black_length = 160
time_bar_black_height = 20
time_bar_x = 10
time_bar_y = 10
time_bar_green_length = 0
time_bar_green_length_reset = 150
time_bar_green_height = 10

#FALLING BLOCKS
falling_blocks = []

#STALACTITES
stalactites = []
stalactites_range = []

#QUICKSAND
quicksand = []
in_quicksand = False

#ladders and bridges
bridge_count = 0
on_a_bridge = False
on_bridge = False
at_ladder = False
on_ladder = False

star_list = []
snow_y_change = 3

level_info = []
level_doors = []
level_music = []
level_backdrop = []
backdrops = []
backdrops.append([-100,0])

save_info = []

def save_load(savename):
        fo = open("saves\\" + savename + ".svgm")
        line_count=0
        for i, line in enumerate(fo):
                line_count+=1
                if i == 0:
                        save_info.append(line.rstrip()) #current level
                elif i == 1:
                        save_info.append(line.rstrip()) #previous level
                elif i == 2:
                        save_info.append(line.rstrip()) #gun color
                elif i == 3:
                        save_info.append(int(line.rstrip())) #health
                #elif i == 4:
                #        save_info.append(int(line)) #collectible count
        save_info.append(int(line_count))
        fo.close()

def save_write(savename,content):
        fo = open("saves\\" + savename + ".svgm", "w+")
        fo.write(content);
        fo.close()

for i in range(100):
    x = random.randrange(0,1024)
    y = random.randrange(0,784)
    star_list.append([x,y])

def lvlParser(level):
    file = open("level\\" + level + ".cfg")
    for i, line in enumerate(file):
        if i == 0:
            info = line.split()
            level_info.append([int(info[0]),int(info[1])])
        elif i == 1:
            level_info.append([line])
        elif i == 2:
            middleground.append(line)
        elif i == 3:
            background.append(line)
        elif i == 4:
                enemy_levelpng.append(line)
        elif i == 5:
                level_backdrop.append(line)
        elif i == 6:
                level_music.append(line)
        elif i == 7:
                time.append(line)
                time.append(line)
        elif i == 8:
            info = line.split()
            number_villagers.append([int(info[0]),int(info[1])])
            sign_start = number_villagers[0][0]*number_villagers[0][1] + 9
        elif  i <= 8  + number_villagers[0][0]*number_villagers[0][1]:
            level_text.append(line)
        elif i == sign_start:
            info = line.split()
            number_sign.append([int(info[0]),int(info[1])])
        elif i <= sign_start + number_sign[0][0]*number_sign[0][1]:
            sign_text.append(line)
        else:
            level_doors.append(line)
    for i in range(len(background)):
        background[i] = background[i].rstrip()
    for i in range(len(middleground)):
        middleground[i] = middleground[i].rstrip()
    for i in range(len(level_text)):
        level_text[i] = level_text[i].rstrip()
    for i in range(len(level_doors)):
        level_doors[i] = level_doors[i].rstrip()
    for i in range(len(level_music)):
        level_music[i] = level_music[i].rstrip()
    for i in range(len(sign_text)):
        sign_text[i] = sign_text[i].rstrip()
    for i in range(len(enemy_levelpng)):
        enemy_levelpng[i] = enemy_levelpng[i].rstrip()
    for i in range(len(time)):
            time[i] = time[i].rstrip()
            time[i] = int(time[i])
    for i in range(len(level_backdrop)):
            level_backdrop[i] = level_backdrop[i].rstrip()
        
            
    file.close()
    return level

previous_level  = "forest_1"
current_level = "hub"

fileobject = open("saves\LEVEL.pass")
level_pass = fileobject.readline()
print("\n"+str(level_pass)+"\n")
if not level_pass == "":
        save=level_pass
        print("Save = level_pass")
else:
        current_level = "hub" #THE DEFAULT STARTING LEVEL, CHANGE LATER FOR DEFAULT / NO SAVE CONTENT
        print("current_level = hub")

save_info = []
save_load(save)
print(str(len(save_info)-1))
if save_info[len(save_info)-1] > 0:
        current_level=save_info[0]
        #print(current_level)
        previous_level=save_info[1]
        #print(previous_level)
        gun_color=save_info[2]
        #print(gun_color)
        health=save_info[3]
        #print(health)
        #collectible_count=save_info[4]
lvlParser(current_level)
x_coord = level_info[0][0]
y_coord = level_info[0][1]
weather = level_info[1][0]

def scroll(x,y):
        for i in range(len(level_walls_red)):
                level_walls_red[i][0] -= x
                level_walls_red[i][1] -= y
        for i in range(len(level_walls_ground)):
                level_walls_ground[i][0] -= x
                level_walls_ground[i][1] -= y
        for i in range(len(level_walls_r_edge)):
                level_walls_r_edge[i][0] -= x
                level_walls_r_edge[i][1] -= y
        for i in range(len(level_walls_l_edge)):
                level_walls_l_edge[i][0] -= x
                level_walls_l_edge[i][1] -= y
        for i in range(len(level_walls_d_edge)):
                level_walls_d_edge[i][0] -= x
                level_walls_d_edge[i][1] -= y
        for i in range(len(level_top)):
                level_top[i][0] -= x
                level_top[i][1] -= y
        for i in range(len(level_side_right)):
                level_side_right[i][0] -= x
                level_side_right[i][1] -= y
        for i in range(len(level_side_left)):
                level_side_left[i][0] -= x
                level_side_left[i][1] -= y
        for i in range(len(level_bottom)):
                level_bottom[i][0] -= x
                level_bottom[i][1] -= y
        for i in range(len(gun_list)):
            gun_list[i][0] -= x
            gun_list[i][1] -= y
        for i in range(len(next_level)):
            next_level[i][0] -= x
            next_level[i][1] -= y
        for i in range(len(water)):
            water[i][0] -= x
            water[i][1] -= y
        for i in range(len(water_grounds)):
            water_grounds[i][0] -= x
            water_grounds[i][1] -= y
        for i in range(len(villager)):
            villager[i][0] -= x
            villager[i][1] -= y
        for i in range(len(signs)):
            signs[i][0] -= x
            signs[i][1] -= y
        for i in range(len(houses)):
            houses[i][0] -= x
            houses[i][1] -= y
        for i in range(len(house_walls)):
            house_walls[i][0] -= x
            house_walls[i][1] -= y
        for i in range(len(house_ceilings)):
            house_ceilings[i][0] -= x
            house_ceilings[i][1] -= y
        for i in range(len(house_floors)):
            house_floors[i][0] -= x
            house_floors[i][1] -= y
        for i in range(len(ladders)):
            ladders[i][0] -= x
            ladders[i][1] -= y
        for i in range(len(bridges)):
                bridges[i][0] -= x
                bridges[i][1] -= y
        for i in range(len(level_top_bridges)):
                level_top_bridges[i][0] -= x
                level_top_bridges[i][1] -= y
        for i in range(len(bridges_left)):
                bridges_left[i][0] -= x
                bridges_left[i][1] -= y
        for i in range(len(bridges_right)):
                bridges_right[i][0] -= x
                bridges_right[i][1] -= y
        for i in range(len(switch)):
                switch[i][0] -= x
                switch[i][1] -= y
        for i in range(len(falling_blocks)):
                falling_blocks[i][0] -= x
                falling_blocks[i][1] -= y
                falling_blocks[i][2] -= y
        for i in range(len(quicksand)):
                quicksand[i][0] -= x
                quicksand[i][1] -= y
        for i in range(len(collectibles)):
                collectibles[i][0] -= x
                collectibles[i][1] -= y
        for i in range(len(lavas)):
                lavas[i][0] -= x
                lavas[i][1] -= y
        for i in range(len(rocks)):
                rocks[i][0] -= x
                rocks[i][1] -= y
        for i in range(len(rock_ground)):
                rock_ground[i][0] -= x
                rock_ground[i][1] -= y
        for i in range(len(rock_right_corners)):
                rock_right_corners[i][0] -= x
                rock_right_corners[i][1] -= y
        for i in range(len(rock_left_corners)):
                rock_left_corners[i][0] -= x
                rock_left_corners[i][1] -= y
        for i in range(len(rock_double_corners)):
                rock_double_corners[i][0] -= x
                rock_double_corners[i][1] -= y
        for i in range(len(sands)):
                sands[i][0] -= x
                sands[i][1] -= y
        for i in range(len(sand_grounds)):
                sand_grounds[i][0] -= x
                sand_grounds[i][1] -= y
        for i in range(len(sand_right_corner)):
                sand_right_corner[i][0] -= x
                sand_right_corner[i][1] -= y
        for i in range(len(sand_left_corner)):
                sand_left_corner[i][0] -= x
                sand_left_corner[i][1] -= y
        for i in range(len(sand_double_corners)):
                sand_double_corners[i][0] -= x
                sand_double_corners[i][1] -= y
        for i in range(len(bricks)):
                bricks[i][0] -= x
                bricks[i][1] -= y
        for i in range(len(brick_grounds)):
                brick_grounds[i][0] -= x
                brick_grounds[i][1] -= y
        for i in range(len(brick_right_corners)):
                brick_right_corners[i][0] -= x
                brick_right_corners[i][1] -= y
        for i in range(len(brick_left_corners)):
                brick_left_corners[i][0] -= x
                brick_left_corners[i][1] -= y
        for i in range(len(icy)):
                icy[i][0] -= x
                icy[i][1] -= y
        for i in range(len(icy_grounds)):
                icy_grounds[i][0] -= x
                icy_grounds[i][1] -= y
        for i in range(len(ice_right_corners)):
                ice_right_corners[i][0] -= x
                ice_right_corners[i][1] -= y
        for i in range(len(ice_left_corners)):
                ice_left_corners[i][0] -= x
                ice_left_corners[i][1] -= y
        for i in range(len(ice_double_corners)):
                ice_double_corners[i][0] -= x
                ice_double_corners[i][1] -= y
        for i in range(len(gun_color_changer)):
                gun_color_changer[i][0] -= x
                gun_color_changer[i][1] -= y
        for i in range(len(cave)):
                cave[i][0] -= x
                cave[i][1] -= y
        for i in range(len(cave_ground)):
                cave_ground[i][0] -= x
                cave_ground[i][1] -= y
        for i in range(len(cave_right_corners)):
                cave_right_corners[i][0] -= x
                cave_right_corners[i][1] -= y
        for i in range(len(cave_left_corners)):
                cave_left_corners[i][0] -= x
                cave_left_corners[i][1] -= y
        for i in range(len(cave_double_corners)):
                cave_double_corners[i][0] -= x
                cave_double_corners[i][1] -= y

def scroll_mg(x,y):
    for i in range(len(house_insides)):
        house_insides[i][0] -= x
        house_insides[i][1] -= y
    for i in range(len(mg_ground)):
        mg_ground[i][0] -= x
        mg_ground[i][1] -= y
    for i in range(len(stalactites)):
        stalactites[i][0] -= x
        stalactites[i][1] -= y
        stalactites[i][2] -= y
    for i in range(len(stalactites_range)):
        stalactites_range[i][0] -= x
        stalactites_range[i][1] -= y
    for i in range(len(mg_lavas)):
        mg_lavas[i][0] -= x
        mg_lavas[i][1] -= y
    for i in range(len(mg_rock_ground)):
        mg_rock_ground[i][0] -= x
        mg_rock_ground[i][1] -= y
    for i in range(len(mg_sand_grounds)):
        mg_sand_grounds[i][0] -= x
        mg_sand_grounds[i][1] -= y
    for i in range(len(mg_icy_ground)):
        mg_icy_ground[i][0] -= x
        mg_icy_ground[i][1] -= y
    for i in range(len(mg_brick_grounds)):
        mg_brick_grounds[i][0] -= x
        mg_brick_grounds[i][1] -= y
    for i in range(len(backdrops)):
            backdrops[i][0] -= x/10
    for i in range(len(trees)):
            trees[i][0] -= x
            trees[i][1] -= y
    for i in range(len(fences)):
            fences[i][0] -= x
            fences[i][1] -= y
    for i in range(len(cactus)):
            cactus[i][0] -= x
            cactus[i][1] -= y
    for i in range(len(wells)):
            wells[i][0] -= x
            wells[i][1] -= y
    for i in range(len(mg_cave_ground)):
        mg_cave_ground[i][0] -= x
        mg_cave_ground[i][1] -= y

def scroll_enemies(x,y):
        for i in range(len(enemy_crawler)):
                enemy_crawler[i][0] -= x
                enemy_crawler[i][1] -= y
        for i in range(len(enemy_crawler_range)):
                enemy_crawler_range[i][0] -= x
                enemy_crawler_range[i][1] -= y
        for i in range(len(enemy_puffpuff)):
                enemy_puffpuff[i][0] -= x
                enemy_puffpuff[i][1] -= y
                enemy_puffpuff[i][9] -= y
        for i in range(len(enemy_puffpuff_range)):
                enemy_puffpuff_range[i][0] -= x
                enemy_puffpuff_range[i][1] -= y
        for i in range(len(enemy_flying)):
                enemy_flying[i][0] -= x
                enemy_flying[i][1] -= y
        for i in range(len(enemy_flying_range)):
                enemy_flying_range[i][0] -= x
                enemy_flying_range[i][1] -= y
        

on_ground = False
change_level = False

def txtEngine(screen,text,line,overlay):
        if overlay:
                pygame.draw.rect(screen,black,[0,468,1024,250])
                pygame.draw.rect(screen,white,[0,468,1024,10])
                pygame.draw.rect(screen,white,[0,708,1024,10])
        myfont = pygame.font.Font("data/fonts/Minecraftia.ttf", 20)
        to_write = myfont.render(text, 1, (255,255,255))
        screen.blit(to_write, (75, 450 + line * 50))

def draw_cross(screen,x,y):
        pygame.draw.line(screen,red,[x-6,y],[x-2,y],2)
        pygame.draw.line(screen,red,[x+6,y],[x+2,y],2)
        pygame.draw.line(screen,red,[x,y-6],[x,y-2],2)
        pygame.draw.line(screen,red,[x,y+6],[x,y+2],2)

def load_image(x,i):
    #load an image from the data directory with per pixel alpha transparency.
    return pygame.image.load(os.path.join("data\\" + x, i)).convert_alpha()

def load_music(i):
    #load music
    return pygame.mixer.music.load(os.path.join("data\\music" , i))

def load_SFX(i):
        #load sfx
        return pygame.mixer.Sound(os.path.join("data\\sound", i))

def load_level(i):
    return pygame.image.load(os.path.join("level\\", i)).convert_alpha()

#all foreground images here
levelimg = load_level(current_level+".png")
bg = load_image("backgrounds",background[0]+".png")
mg = load_level(middleground[0]+".png")
enemy_level = load_level(enemy_levelpng[0]+".png")
backdrop = load_image("backgrounds\\backdrops",level_backdrop[0]+".png")

grass1 = load_image("tiles","grass1.png")
grass2 = load_image("tiles","grass2.png")
grass3 = load_image("tiles","grass3.png")
double_edge = load_image("tiles","grass_double_corner.png")
ground_tile = load_image("tiles","dirt.png")
left_edge = load_image("tiles","grass_corner_left.png")
right_edge = load_image("tiles","grass_corner_right.png")
water_image = load_image("tiles","water.png")
water_ground = load_image("tiles","water_ground.png")
house_floor = load_image("tiles","floor.png")
house_wall = load_image("tiles","walls.png")
house_ceiling = load_image("tiles","ceiling.png")
house_inside = load_image("tiles","wall_back.png")
bridge = load_image("tiles","bridge.png")
bridge_right = load_image("tiles","bridge_ext_right.png")
bridge_left = load_image("tiles","bridge_ext.png")

#GRAYSCALE
gray_grass1 = load_image("tiles","gray_grass1.png")
gray_grass2 = load_image("tiles","gray_grass2.png")
gray_grass3 = load_image("tiles","gray_grass3.png")
gray_double_edge = load_image("tiles","gray_grass_double_corner.png")
gray_ground_tile = load_image("tiles","gray_dirt.png")
gray_left_edge = load_image("tiles","gray_grass_corner_left.png")
gray_right_edge = load_image("tiles","gray_grass_corner_right.png")

player = load_image("player","sprite.png")
player_left = load_image("player","spriteleft.png")
player_running = load_image("player","run.png")
player_running_left = load_image("player","runleft.png")
player_jumping = load_image("player","jump.png")
player_jumping_left = load_image("player","jumpleft.png")
player_idle = load_image("player","idle1_kneecap.png")
player_idle_left = load_image("player","idle1_left_kneecap.png")
player_back = load_image("player","spriteclimb.png")
player_left_back = load_image("player","spriteclimb_left.png")

elder = load_image("npcs\\villagers\\forest","elder_left.png")

#ALL THE COLLECTIBLE ITEMS
collectible = load_image("mech","crystal.png")
collectible1 = load_image("mech","crystal1.png")
collectible2= load_image("mech","crystal2.png")
collectible3 = load_image("mech","crystal3.png")
collectible4 = load_image("mech","crystal4.png")
collectible5 = load_image("mech","crystal5.png")
collectible6 = load_image("mech","crystal6.png")
collectible7 = load_image("mech","crystal7.png")
collectible8 = load_image("mech","crystal8.png")
collectible9 = load_image("mech","crystal9.png")


#GUNS
blue_gun = load_image("player","blue_gun.png")
red_gun = load_image("player","red_gun.png")
green_gun = load_image("player","blue_gun.png")

blue_gun_left = load_image("player","blue_gun_left.png")
red_gun_left = load_image("player","red_gun_left.png")
green_gun_left = load_image("player","blue_gun_left.png")

blue_gun_dark = load_image("player","blue_gun_dark.png")
red_gun_dark = load_image("player","red_gun_dark.png")
green_gun_dark = load_image("player","blue_gun_dark.png")

blue_gun_dark_left = load_image("player","blue_gun_left_dark.png")
red_gun_dark_left = load_image("player","red_gun_left_dark.png")
green_gun_dark_left = load_image("player","blue_gun_left_dark.png")

blue_gun_charge1 = load_image("player","blue_gun_charge1.png")
red_gun_charge1 = load_image("player","red_gun_charge1.png")
green_gun_charge1 = load_image("player","blue_gun_charge1.png")

blue_gun_charge2 = load_image("player","blue_gun_charge2.png")
red_gun_charge2 = load_image("player","red_gun_charge2.png")
green_gun_charge2 = load_image("player","blue_gun_charge2.png")

blue_gun_charge1_left = load_image("player","blue_gun_left_charge1.png")
red_gun_charge1_left = load_image("player","red_gun_left_charge1.png")
green_gun_charge1_left = load_image("player","blue_gun_left_charge1.png")

blue_gun_charge2_left = load_image("player","blue_gun_left_charge2.png")
red_gun_charge2_left = load_image("player","red_gun_left_charge2.png")
green_gun_charge2_left = load_image("player","blue_gun_left_charge2.png")

left_heart = load_image("gui","left_heart.png")
right_heart = load_image("gui","right_heart.png")
bubble = load_image("gui","air.png")

door = load_image("mech","door.png")
door2 = load_image("mech","door1.png")
sign = load_image("mech","sign.png")
ladder = load_image("mech","ladders.png")

gray_sign = load_image("mech","gray_sign.png")

tree = load_image("scenery","tree.png")
house = load_image("scenery","house1.png")
house2 = load_image("scenery","house2.png")

gray_house = load_image("scenery","gray_house1.png")
gray_house2 = load_image("scenery","gray_house2.png")

#switches
switch_blue = load_image("mech","bluebutton_press.png")
switch_blue_press = load_image("mech","bluebutton_depress.png")
switch_green = load_image("mech","greenbutton_press.png")
switch_green_press = load_image("mech","greenbutton_depress.png")

#STALACTITES
stalactite_cave = load_image("tiles","rockstal.png")
stalactite_ice = load_image("tiles","icystal.png")

#QUICKSAND
quicksand1 = load_image("tiles","quicksand1.png")
quicksand2 = load_image("tiles","quicksand2.png")
quicksand3 = load_image("tiles","quicksand3.png")
quicksand4 = load_image("tiles","quicksand4.png")

#ICE SPRITES
ice = load_image("tiles","icy_snow.png")
ice2 = load_image("tiles","icy_snow2.png")
ice_dirt = load_image("tiles","ice_dirt.png")
ice_double_corner = load_image("tiles","icy_snow_doublecorner.png")
ice_left_corner = load_image("tiles","icy_snow_leftcorner.png")
ice_right_corner = load_image("tiles","icy_snow_rightcorner.png")

#LAVA
lava1 = load_image("tiles","lava1.png")
lava2 = load_image("tiles","lava2.png")
lava3 = load_image("tiles","lava3.png")
lava4 = load_image("tiles","lava4.png")
lava5 = load_image("tiles","lava5.png")

#ROCKY SPRITES
rock = load_image("tiles","rocky 1.png")
rock2 = load_image("tiles","rocky 2.png")
rock3 = load_image("tiles","rocky 3.png")
#TEMP ROCK GROUND
rock_grounds = load_image("tiles","rocky ground.png")
rock_corner_left = load_image("tiles","rocky corner.png")
rock_corner_right = load_image("tiles","rocky corner right.png")
rocky_double_corner = load_image("tiles","rocky double corner.png")

#cave
caves = load_image("tiles","cave 1.png")
cave2 = load_image("tiles","cave 2.png")
cave3 = load_image("tiles","cave 3.png")
#TEMP ROCK GROUND
cave_grounds = load_image("tiles","cave ground.png")
cave_corner_left = load_image("tiles","cave corner.png")
cave_corner_right = load_image("tiles","cave corner right.png")
cave_double_corner = load_image("tiles","cave double corner.png")

#SAND SPRITES
sand1 = load_image("tiles","sand1.png")
sand2 = load_image("tiles","sand2.png")
sand3 = load_image("tiles","sand3.png")
sand_ground = load_image("tiles","sand_ground1.png")
sand_ground2 = load_image("tiles","sand_ground2.png")
sand_corner_left = load_image("tiles","sand_corner.png")
sand_corner_right = load_image("tiles","sand_corner_right.png")
sand_double_corner = load_image("tiles","sand_double_corner.png")

#BRICK SPRITES
brick_under = load_image("tiles","brick_under1.png")
brick_under2 = load_image("tiles","brick_under2.png")
brick = load_image("tiles","brick1.png")
brick_left_corner = load_image("tiles","brick1_leftcorner.png")
brick_right_corner = load_image("tiles","brick1_rightcorner.png")

#enemies
crawler = load_image("enemies\\forestturtle","turtlebig.png")
crawler_run = load_image("enemies\\forestturtle","turtlewalkbig.png")
crawler_left = load_image("enemies\\forestturtle","turtleleftbig.png")
crawler_left_run = load_image("enemies\\forestturtle","turtlewalkleftbig.png")
crawler_die1 = load_image("enemies\\forestturtle","turtledie1big.png")
crawler_die_left1 = load_image("enemies\\forestturtle","turtledie1leftbig.png")
crawler_die2 = load_image("enemies\\forestturtle","turtledie2big.png")
crawler_die_left2 = load_image("enemies\\forestturtle","turtledie2leftbig.png")
crawler_die3 = load_image("enemies\\forestturtle","turtledie3big.png")
crawler_die_left3 = load_image("enemies\\forestturtle","turtledie3leftbig.png")
crawler_die4 = load_image("enemies\\forestturtle","turtledie4big.png")
crawler_die_left4 = load_image("enemies\\forestturtle","turtledie4leftbig.png")

#puffpuffs
puffpuff_1 = load_image("enemies\\puffpuff","puffpuffwalk1right.png")
puffpuff_left_1 = load_image("enemies\\puffpuff","puffpuffwalk1.png")
puffpuff_2 = load_image("enemies\\puffpuff","puffpuffwalk2right.png")
puffpuff_left_2 = load_image("enemies\\puffpuff","puffpuffwalk2.png")
puffpuff_3 = load_image("enemies\\puffpuff","puffpuffwalk3right.png")
puffpuff_left_3 = load_image("enemies\\puffpuff","puffpuffwalk3.png")
puffpuff_jump = load_image("enemies\\puffpuff","puffpuffjumpright.png")
puffpuff_jump_left = load_image("enemies\\puffpuff","puffpuffjump.png")
puffpuff_die = load_image("enemies\\puffpuff","puffpuffdieright.png")
puffpuff_die_left = load_image("enemies\\puffpuff","puffpuffdie.png")

#FLYING ENEMY
flying = load_image("enemies\\bee","move1_right.png")
flying_left = load_image("enemies\\bee","move1.png")
flying_run = load_image("enemies\\bee","move2_right.png")
flying_left_run = load_image("enemies\\bee","move2.png")
flying_die_right = load_image("enemies\\bee","dead_right.png")
flying_die = load_image("enemies\\bee","dead.png")

#TREES AND FENCES
tree1 = load_image("scenery", "tree2.png")
tree2 = load_image("scenery", "tree3.png")
tree3 = load_image("scenery", "tree4.png")
redwood = load_image("scenery", "redwood.png")

green_fence = load_image("scenery", "fence_green.png")
red_fence = load_image("scenery", "fence_red.png")
white_fence = load_image("scenery", "fence_white.png")

cactus1 = load_image("scenery","cactus.png")
cactus2 = load_image("scenery","cactus2.png")
cactus3 = load_image("scenery","cactus3.png")
cactus4 = load_image("scenery","cactus4.png")

gray_tree1 = load_image("scenery", "gray_tree2.png")
gray_tree2 = load_image("scenery", "gray_tree3.png")
gray_tree3 = load_image("scenery", "gray_tree4.png")
gray_redwood = load_image("scenery", "gray_redwood.png")

green_fence = load_image("scenery", "fence_green.png")
red_fence = load_image("scenery", "fence_red.png")
white_fence = load_image("scenery", "fence_white.png")
gray_fence = load_image("scenery", "gray_fence_green.png")

cactus1 = load_image("scenery","cactus.png")
cactus2 = load_image("scenery","cactus2.png")
cactus3 = load_image("scenery","cactus3.png")
cactus4 = load_image("scenery","cactus4.png")

well = load_image("scenery","well.png")
gray_well = load_image("scenery","gray_well.png")

#sound effects
gunshot = load_SFX("gunshoot.wav")
jumpsound = load_SFX("Jump.wav")
pain = load_SFX("Hurt.wav") 
powerup = load_SFX("Powerup.wav")

#set volume to a non-destructive level(remove it later)
pygame.mixer.music.set_volume(0.2)

#all that may be in both

mgwidth = bg.get_width()
mgheight = bg.get_height()

lvlwidth = levelimg.get_width()
lvlheight = levelimg.get_height()

def getenemyRGB():
        for x in range(enemy_level.get_width()):
                for y in range(enemy_level.get_height()):
                        color = enemy_level.get_at((x,y))
                        #all enemy colours
                        if color == (0, 50, 0, 255):
                                #x coord, y coord, alive(1) or dead(2), direction(left 1)(right 2), walking or not, run change, kill enemy counter, death animation sprite, what type of crawler eg forest wno desert]
                                z = random.randrange(1,3)
                                enemy_crawler.append([x*32,y*32 - 32, 1, z, 1, 0, 0, 0, 1])
                        elif color == (0, 60, 0, 255):
                                z = random.randrange(1,3)
                                enemy_crawler.append([x*32,y*32 - 32, 1, z, 1, 0, 0, 0, 2])
                        elif color == (0, 55, 0, 255):
                                enemy_crawler_range.append([x*32,y*32 - 32])
                        elif color == (0,53,0,255):
                                enemy_crawler_range.append([x*32+30, y*32 - 32])
                        elif color == ( 0, 100, 0, 255):
                                #x coord, y coord, alive(1) or dead(2), direction(left 1)(right 2), walking or not,
                                #run change, which run to go to next,
                                #kill enemy counter, jumping, jumping stop point, jumping speed,
                                #what type of puffpuff eg forest snow desert]
                                z = random.randrange(1,3)
                                enemy_puffpuff.append([x*32,y*32 - 32, 1, z, 1, 0, 0, 0, 0, y*32 - 32, 0, 1])
                                enemy_puffpuff_health.append(2)
                        elif color == (0, 105, 0, 255):
                                enemy_puffpuff_range.append([x*32,y*32 - 300])
                        elif color == (0,103,0,255):
                                enemy_puffpuff_range.append([x*32+30, y*32 - 300])
                        elif color == (0, 150, 0, 255):
                                #x coord, y coord, alive(1) or dead(2), direction(left/up 1)(right/down 2), vertical/horizontal
                                #wing up/down, fly change, kill enemy counter, death animation sprite,
                                #what type of crawler eg forest wno desert]
                                z = random.randrange(1,3)
                                enemy_flying.append([x*32,y*32, 1, z, 1, 0, 0, 0, 1, 1, 2])
                                enemy_flying_health.append(3)
                        elif color == (0, 151, 0, 255):
                                #x coord, y coord, alive(1) or dead(2), direction(left/up 1)(right/down 2), vertical/horizontal
                                #wing up/down, fly change, kill enemy counter, death animation sprite,
                                #what type of crawler eg forest wno desert]
                                z = random.randrange(1,3)
                                enemy_flying.append([x*32,y*32, 1, z, 1, 0, 0, 0, 1, 2, 1])
                                enemy_flying_health.append(3)
                        elif color == (0,155,0,255):
                                enemy_flying_range.append([x*32,y*32 - 32])

                        

def getmgRGB():
    for x in range(mg.get_width()):
        for y in range(mg.get_height()):
                color = mg.get_at((x,y))
                if color == (0, 150, 0, 255):
                        house_insides.append([x*32,y*32])
                elif color == (255, 0 ,255, 255):
                        mg_ground.append([x*32,y*32,1])
                elif color == (255,25,255,255):
                        mg_ground.append([x*32,y*32, 2])
                #STALACTITES
                elif color == (55,255,255,255):
                                #x, y, yreset, isitmoving, the speed
                        stalactites.append([x*32,y*32,y*32, 0, 0, 0, 0, 0])
                elif color == (55,254,255,255):
                        stalactites.append([x*32,y*32,y*32, 0, 0, 0, 0, 1])
                elif color == (56,255,255,255):
                        stalactites_range.append([x*32,y*32])
                elif color == (150,150,0,255):
                        mg_rock_ground.append([x*32,y*32])
                elif color == (255,200,0,255):
                        z = random.randrange(1,3)
                        mg_sand_grounds.append([x*32,y*32, z])
                elif color == (150,50,50,255):
                        g = random.randrange(1,6)
                        z = random.randrange(1,10)
                        mg_lavas.append([x*32,y*32, g, z])
                elif color == (0, 50,100,255):
                        z = random.randrange(1,3)
                        mg_brick_grounds.append([x*32,y*32, z])
                elif color == (100,255,255,255):
                        mg_icy_ground.append([x*32,y*32])
                elif color == (255,121,255,255):
                        fences.append([x*32,y*32,1])
                elif color == (255,122,255,255):
                        fences.append([x*32,y*32,2])
                elif color == (255,123,255,255):
                        fences.append([x*32,y*32,3])
                elif color == (255,124,255,255):
                        fences.append([x*32,y*32,4])
                elif color == (0,75,0,255):
                        z = random.randrange(1,5)
                        trees.append([x*32,y*32,z,1])
                elif color == (25,75,0):
                        z = random.randrange(1,5)
                        trees.append([x*32,y*32,z,2])
                elif color == (255,100,0,255):
                        z = random.randrange(1,5)
                        cactus.append([x*32,y*32,z])
                elif color == (0,100,0,255):
                        wells.append([x*32,y*32,1])
                elif color == (25,100,0,255):
                        wells.append([x*32,y*32,2])
                elif color == (0,150,150,255):
                        mg_cave_ground.append([x*32,y*32])
                        
                
def drawmg():
        for i in range(len(house_insides)):
                if -32 <= house_insides[i][0] <= 1056 and -32 <= house_insides[i][1] <= 800:
                        cur_x = house_insides[i][0]
                        cur_y = house_insides[i][1]
                        screen.blit(house_inside, (cur_x, cur_y))
        for i in range(len(mg_ground)):
            if mg_ground[i][2] == 1:
                if -32 <= mg_ground[i][0] <= 1056 and -32 <= mg_ground[i][1] <= 800:
                        cur_x = mg_ground[i][0]
                        cur_y = mg_ground[i][1]
                        screen.blit(ground_tile, (cur_x, cur_y))
            else:
                 if -32 <= mg_ground[i][0] <= 1056 and -32 <= mg_ground[i][1] <= 800:
                        cur_x = mg_ground[i][0]
                        cur_y = mg_ground[i][1]
                        screen.blit(gray_ground_tile, (cur_x, cur_y))
        for i in range(len(mg_rock_ground)):
                if -32 <= mg_rock_ground[i][0] <= 1056 and -32 <=mg_rock_ground[i][1] <= 800:
                        cur_x = mg_rock_ground[i][0]
                        cur_y = mg_rock_ground[i][1]
                        screen.blit(rock_grounds, (cur_x,cur_y))
        for i in range(len(mg_sand_grounds)):
                if -32 <= mg_sand_grounds[i][0] <= 1056 and -32 <=mg_sand_grounds[i][1] <= 800:
                        cur_x = mg_sand_grounds[i][0]
                        cur_y = mg_sand_grounds[i][1]
                        if mg_sand_grounds[i][2] == 2:
                                screen.blit(sand_ground2, (cur_x,cur_y))
                        else:
                                screen.blit(sand_ground, (cur_x,cur_y))
        for i in range(len(mg_lavas)):
                if -32 <= mg_lavas[i][0] <= 1056 and -32 <=mg_lavas[i][1] <= 800:
                        cur_x = mg_lavas[i][0]
                        cur_y = mg_lavas[i][1]
                        if mg_lavas[i][2] == 1:
                                screen.blit(lava1, (cur_x,cur_y))
                        elif mg_lavas[i][2] == 2:
                                screen.blit(lava2, (cur_x,cur_y))
                        elif mg_lavas[i][2] == 3:
                                screen.blit(lava3, (cur_x,cur_y))
                        elif mg_lavas[i][2] == 4:
                                screen.blit(lava4, (cur_x,cur_y))
                        elif mg_lavas[i][2] == 5:
                                screen.blit(lava5, (cur_x, cur_y))
        for i in range(len(mg_brick_grounds)):
                if -32 <= mg_brick_grounds[i][0] <= 1056 and -32 <=mg_brick_grounds[i][1] <= 800:
                        cur_x = mg_brick_grounds[i][0]
                        cur_y = mg_brick_grounds[i][1]
                        screen.blit(brick_under2, (cur_x,cur_y))
        for i in range(len(mg_icy_ground)):
                if -32 <= mg_icy_ground[i][0] <= 1056 and -32 <=mg_icy_ground[i][1] <= 800:
                        cur_x = mg_icy_ground[i][0]
                        cur_y = mg_icy_ground[i][1]
                        screen.blit(ice_dirt, (cur_x,cur_y))
        for i in range(len(trees)):
            if trees[i][3] == 1:
                if -32 <= trees[i][0] <= 1056 and -32 <= trees[i][1] <= 800:
                        cur_x = trees[i][0]
                        cur_y = trees[i][1]
                        if trees[i][2] == 1:
                                screen.blit(tree1, (cur_x - 38,cur_y - 96))
                        if trees[i][2] == 2:
                                screen.blit(tree2, (cur_x - 28,cur_y - 64))
                        if trees[i][2] == 3:
                                screen.blit(tree3, (cur_x - 21,cur_y - 56))
                        if trees[i][2] == 4:
                                screen.blit(redwood, (cur_x - 8,cur_y - 96))
            else:
                if -32 <= trees[i][0] <= 1056 and -32 <= trees[i][1] <= 800:
                        cur_x = trees[i][0]
                        cur_y = trees[i][1]
                        if trees[i][2] == 1:
                                screen.blit(gray_tree1, (cur_x - 38,cur_y - 96))
                        if trees[i][2] == 2:
                                screen.blit(gray_tree2, (cur_x - 28,cur_y - 64))
                        if trees[i][2] == 3:
                                screen.blit(gray_tree3, (cur_x - 21,cur_y - 56))
                        if trees[i][2] == 4:
                                screen.blit(gray_redwood, (cur_x - 8,cur_y - 96))
        for i in range(len(cactus)):
                if -32 <= cactus[i][0] <= 1056 and -32 <= cactus[i][1] <= 800:
                        cur_x = cactus[i][0]
                        cur_y = cactus[i][1]
                        if cactus[i][2] == 1:
                                screen.blit(cactus1, (cur_x ,cur_y - 32))
                        if cactus[i][2] == 2:
                                screen.blit(cactus2, (cur_x ,cur_y - 32))
                        if cactus[i][2] == 3:
                                screen.blit(cactus3, (cur_x ,cur_y - 32))
                        if cactus[i][2] == 4:
                                screen.blit(cactus4, (cur_x ,cur_y - 32))
        for i in range(len(wells)):
            if wells[i][2] == 1:
                if -32 <= wells[i][0] <= 1056 and -32 <= wells[i][1] <= 800:
                        cur_x = wells[i][0]
                        cur_y = wells[i][1]
                        screen.blit(well, (cur_x,cur_y - 32))
            else:
                if -32 <= wells[i][0] <= 1056 and -32 <= wells[i][1] <= 800:
                        cur_x = wells[i][0]
                        cur_y = wells[i][1]
                        screen.blit(gray_well, (cur_x,cur_y - 32))
        for i in range(len(mg_cave_ground)):
                if -32 <= mg_cave_ground[i][0] <= 1056 and -32 <=mg_cave_ground[i][1] <= 800:
                        cur_x = mg_cave_ground[i][0]
                        cur_y = mg_cave_ground[i][1]
                        screen.blit(cave_grounds, (cur_x,cur_y))

def getRGB():
        for x in range(levelimg.get_width()):
                for y in range(levelimg.get_height()):
                        color = levelimg.get_at((x, y))
                        if color == (255, 0, 0, 255):
                                grass = random.randrange(1,4)
                                level_walls_red.append([x*32,y*32,grass,1])
                                level_top.append([x*32,y*32])
                                #right
                                level_side_right.append([x*32+32, y*32+12])
                                #left
                                level_side_left.append([x*32, y*32+12])
                                #bottom
                                level_bottom.append([x*32 + 10, y*32 + 30])
                        if color == (255, 25, 0, 255):
                                grass = random.randrange(1,4)
                                level_walls_red.append([x*32,y*32,grass,2])
                                level_top.append([x*32,y*32])
                                #right
                                level_side_right.append([x*32+32, y*32+12])
                                #left
                                level_side_left.append([x*32, y*32+12])
                                #bottom
                                level_bottom.append([x*32 + 10, y*32 + 30])
                        elif color ==(255,0,255,255):
                                level_walls_ground.append([x*32,y*32,1])
                                level_top.append([x*32,y*32])
                                #right
                                level_side_right.append([x*32+32, y*32+12])
                                #left
                                level_side_left.append([x*32, y*32+12])
                                #bottom
                                level_bottom.append([x*32 + 10, y*32 + 30])
                        elif color ==(255,25,255,255):
                                level_walls_ground.append([x*32,y*32,2])
                                level_top.append([x*32,y*32])
                                #right
                                level_side_right.append([x*32+32, y*32+12])
                                #left
                                level_side_left.append([x*32, y*32+12])
                                #bottom
                                level_bottom.append([x*32 + 10, y*32 + 30])
                        elif color ==(255,0,150,255):
                                level_walls_l_edge.append([x*32,y*32,1])
                                level_top.append([x*32,y*32])
                                #right
                                level_side_right.append([x*32+32, y*32+12])
                                #left
                                level_side_left.append([x*32, y*32+12])
                                #bottom
                                level_bottom.append([x*32 + 10, y*32 + 30])
                        elif color ==(255,25,150,255):
                                level_walls_l_edge.append([x*32,y*32,2])
                                level_top.append([x*32,y*32])
                                #right
                                level_side_right.append([x*32+32, y*32+12])
                                #left
                                level_side_left.append([x*32, y*32+12])
                                #bottom
                                level_bottom.append([x*32 + 10, y*32 + 30])
                        elif color ==(255,0,200,255):
                                level_walls_r_edge.append([x*32,y*32,1])
                                level_top.append([x*32,y*32])
                                #right
                                level_side_right.append([x*32+32, y*32+12])
                                #left
                                level_side_left.append([x*32, y*32+12])
                                #bottom
                                level_bottom.append([x*32 + 10, y*32 + 30])
                        elif color ==(255,25,200,255):
                                level_walls_r_edge.append([x*32,y*32,2])
                                level_top.append([x*32,y*32])
                                #right
                                level_side_right.append([x*32+32, y*32+12])
                                #left
                                level_side_left.append([x*32, y*32+12])
                                #bottom
                                level_bottom.append([x*32 + 10, y*32 + 30])
                        elif color ==(255,0,50,255):
                                level_walls_d_edge.append([x*32,y*32,1])
                                level_top.append([x*32,y*32])
                                #right
                                level_side_right.append([x*32+32, y*32+12])
                                #left
                                level_side_left.append([x*32, y*32+12])
                                #bottom
                                level_bottom.append([x*32 + 10, y*32 + 30])
                        elif color ==(255,25,50,255):
                                level_walls_d_edge.append([x*32,y*32,2])
                                level_top.append([x*32,y*32])
                                #right
                                level_side_right.append([x*32+32, y*32+12])
                                #left
                                level_side_left.append([x*32, y*32+12])
                                #bottom
                                level_bottom.append([x*32 + 10, y*32 + 30])
                        elif color == (255,255,255,255):
                                next_level.append([x*32,y*32, 1])
                        elif color == (0,0,255,255):
                                water.append([x*32,y*32])
                        elif color == (0,0,150,255):
                                water_grounds.append([x*32,y*32])
                        elif color == (150,150,150,255):
                            villager_direction = random.randrange(0,2)
                            villager.append([x*32,y*32-17,villager_direction, 1, 1, 1, 0, 0, 0])
                        elif color == (151,151,151,255):
                                villager_direction = random.randrange(0,2)
                                villager.append([x*32,y*32-17,villager_direction, 1, 1, 1, 0, 0, 1])
                        elif color == (125,125,125,255):
                            signs.append([x*32,y*32,1])
                        elif color == (150,125,125,255):
                            signs.append([x*32,y*32,2])
                        elif color == (175,175,175,255):
                            houses.append([x*32 - 224 + 32,y*32 - 160 + 32, 1,1])
                        elif color == (176,176,176,255):
                                houses.append([x*32-224+32, y*32 - 160 + 32, 2,1])
                        elif color == (200,175,175,255):
                            houses.append([x*32 - 224 + 32,y*32 - 160 + 32, 1,2])
                        elif color == (201,176,176,255):
                                houses.append([x*32-224+32, y*32 - 160 + 32, 2,2])
                        elif color == (0,255,0,255):
                            house_floors.append([x*32,y*32])
                            level_top.append([x*32,y*32])
                            #right
                            level_side_right.append([x*32+32, y*32+12])
                            #left
                            level_side_left.append([x*32, y*32+12])
                            #bottom
                            level_bottom.append([x*32 + 10, y*32 + 30])
                        elif color == (0,225,0,255):
                            house_ceilings.append([x*32,y*32])
                            level_top.append([x*32,y*32])
                            #right
                            level_side_right.append([x*32+32, y*32+12])
                            #left
                            level_side_left.append([x*32, y*32+12])
                            #bottom
                            level_bottom.append([x*32 + 10, y*32 + 30])
                        elif color == (0,200,0,255):
                            house_walls.append([x*32,y*32])
                            level_top.append([x*32,y*32])
                            #right
                            level_side_right.append([x*32+32, y*32+12])
                            #left
                            level_side_left.append([x*32, y*32+12])
                            #bottom
                            level_bottom.append([x*32 + 10, y*32 + 30])
                        elif color == (255, 255, 50, 255):
                                ladders.append([x*32,y*32])
                        elif color == (255, 255, 75, 255):
                                bridges.append([x*32,y*32])
                                level_top_bridges.append([x*32, y*32])
                        elif color == (255, 255, 76, 255):
                                bridges_right.append([x*32,y*32])
                                level_top_bridges.append([x*32,y*32])
                        elif color == (255, 255, 74, 255):
                                bridges_left.append([x*32-8, y*32])
                                level_top_bridges.append([x*32, y*32])
                        #SWITCHES
                                #GUN HITS
                        elif color == (255, 255, 100, 255):
                                #ON CEILING
                                switch.append([x*32, y*32, 1, 1])
                        #PLAYER COLLIDE
                        elif color == (255,254,100,255):
                                switch.append([x*32, y*32, 1, 2])
                        #FALLING BLOCKS
                        elif color == (50,50,200,255):
                                                      #x,y,resety,steppedon,makeitfall,gravity,offscreen, reset
                                falling_blocks.append([x*32,y*32,y*32,0,0,0,0,0])
                        #QUICKSAND
                        elif color == (255,100,0,255):
                                quicksand.append([x*32,y*32 + 1,0,0])
                                #COLLECTIBLE
                        elif color == (100,255,100,255):
                                collectibles.append([x*32,y*32, 0, 0])
                        #ICE SECTION
                        elif color == (100,255,255,255):
                                icy_grounds.append([x*32,y*32])
                                level_top.append([x*32,y*32])
                                #right
                                level_side_right.append([x*32+32, y*32+12])
                                #left
                                level_side_left.append([x*32, y*32+12])
                                #bottom
                                level_bottom.append([x*32 + 10, y*32 + 30])
                        elif color == (150,255,255,255):
                                z = random.randrange(1,3)
                                icy.append([x*32,y*32, z])
                                level_top.append([x*32,y*32])
                                #right
                                level_side_right.append([x*32+32, y*32+12])
                                #left
                                level_side_left.append([x*32, y*32+12])
                                #bottom
                                level_bottom.append([x*32 + 10, y*32 + 30])
                        elif color == (125,255,255,255):
                                ice_left_corners.append([x*32,y*32])
                                level_top.append([x*32,y*32])
                                #right
                                level_side_right.append([x*32+32, y*32+12])
                                #left
                                level_side_left.append([x*32, y*32+12])
                                #bottom
                                level_bottom.append([x*32 + 10, y*32 + 30])
                        elif color == (175,255,255,255):
                                ice_right_corners.append([x*32,y*32])
                                level_top.append([x*32,y*32])
                                #right
                                level_side_right.append([x*32+32, y*32+12])
                                #left
                                level_side_left.append([x*32, y*32+12])
                                #bottom
                                level_bottom.append([x*32 + 10, y*32 + 30])
                        elif color == (200,255,255,255):
                                ice_double_corners.append([x*32,y*32])
                                level_top.append([x*32,y*32])
                                #right
                                level_side_right.append([x*32+32, y*32+12])
                                #left
                                level_side_left.append([x*32, y*32+12])
                                #bottom
                                level_bottom.append([x*32 + 10, y*32 + 30])
                        #LAVA SECTION
                        elif color == (150,50,50,255):
                                g = random.randrange(1,6)
                                z = random.randrange(1,10)
                                mg_lavas.append([x*32,y*32, g, z])
                                
                                level_top.append([x*32,y*32])
                                #right
                                level_side_right.append([x*32+32, y*32+12])
                                #left
                                level_side_left.append([x*32, y*32+12])
                                #bottom
                                level_bottom.append([x*32 + 10, y*32 + 30])
                        #BRICK SECTION
                        elif color == (0, 50,100,255):
                                z = random.randrange(1,3)
                                brick_grounds.append([x*32,y*32, z])
                                level_top.append([x*32,y*32])
                                #right
                                level_side_right.append([x*32+32, y*32+12])
                                #left
                                level_side_left.append([x*32, y*32+12])
                                #bottom
                                level_bottom.append([x*32 + 10, y*32 + 30])
                        elif color == (0,75,100,255):
                                bricks.append([x*32,y*32])
                                level_top.append([x*32,y*32])
                                #right
                                level_side_right.append([x*32+32, y*32+12])
                                #left
                                level_side_left.append([x*32, y*32+12])
                                #bottom
                                level_bottom.append([x*32 + 10, y*32 + 30])
                        elif color == (0,100,100,255):
                                brick_left_corners.append([x*32,y*32])
                                level_top.append([x*32,y*32])
                                #right
                                level_side_right.append([x*32+32, y*32+12])
                                #left
                                level_side_left.append([x*32, y*32+12])
                                #bottom
                                level_bottom.append([x*32 + 10, y*32 + 30])
                        elif color == (0,125,100,255):
                                brick_right_corners.append([x*32,y*32])
                                level_top.append([x*32,y*32])
                                #right
                                level_side_right.append([x*32+32, y*32+12])
                                #left
                                level_side_left.append([x*32, y*32+12])
                                #bottom
                                level_bottom.append([x*32 + 10, y*32 + 30])
                        #ROCK SECTION
                        elif color == (150,150,0,255):
                                rock_ground.append([x*32,y*32])
                                level_top.append([x*32,y*32])
                                #right
                                level_side_right.append([x*32+32, y*32+12])
                                #left
                                level_side_left.append([x*32, y*32+12])
                                #bottom
                                level_bottom.append([x*32 + 10, y*32 + 30])
                        elif color == (175,150,0,255):
                                z = random.randrange(1,4)
                                rocks.append([x*32,y*32, z])
                                level_top.append([x*32,y*32])
                                #right
                                level_side_right.append([x*32+32, y*32+12])
                                #left
                                level_side_left.append([x*32, y*32+12])
                                #bottom
                                level_bottom.append([x*32 + 10, y*32 + 30])
                        elif color == (200,150,0,255):
                                rock_right_corners.append([x*32,y*32])
                                level_top.append([x*32,y*32])
                                #right
                                level_side_right.append([x*32+32, y*32+12])
                                #left
                                level_side_left.append([x*32, y*32+12])
                                #bottom
                                level_bottom.append([x*32 + 10, y*32 + 30])
                        elif color == (225,150,0,255):
                                rock_left_corners.append([x*32,y*32])
                                level_top.append([x*32,y*32])
                                #right
                                level_side_right.append([x*32+32, y*32+12])
                                #left
                                level_side_left.append([x*32, y*32+12])
                                #bottom
                                level_bottom.append([x*32 + 10, y*32 + 30])
                        elif color == (250,150,0,255):
                                rock_double_corners.append([x*32,y*32])
                                level_top.append([x*32,y*32])
                                #right
                                level_side_right.append([x*32+32, y*32+12])
                                #left
                                level_side_left.append([x*32, y*32+12])
                                #bottom
                                level_bottom.append([x*32 + 10, y*32 + 30])
                        #SAND SECTION
                        elif color == (255,200,0,255):
                                z = random.randrange(1,3)
                                sand_grounds.append([x*32,y*32, z])
                                level_top.append([x*32,y*32])
                                #right
                                level_side_right.append([x*32+32, y*32+12])
                                #left
                                level_side_left.append([x*32, y*32+12])
                                #bottom
                                level_bottom.append([x*32 + 10, y*32 + 30])
                        elif color == (255,175,0,255):
                                z = random.randrange(1,4)
                                sands.append([x*32,y*32,z])
                                level_top.append([x*32,y*32])
                                #right
                                level_side_right.append([x*32+32, y*32+12])
                                #left
                                level_side_left.append([x*32, y*32+12])
                                #bottom
                                level_bottom.append([x*32 + 10, y*32 + 30])
                        elif color == (255,125,0,255):
                                sand_right_corner.append([x*32,y*32])
                                level_top.append([x*32,y*32])
                                #right
                                level_side_right.append([x*32+32, y*32+12])
                                #left
                                level_side_left.append([x*32, y*32+12])
                                #bottom
                                level_bottom.append([x*32 + 10, y*32 + 30])
                        elif color == (255,110,0,255):
                                sand_left_corner.append([x*32,y*32])
                                level_top.append([x*32,y*32])
                                #right
                                level_side_right.append([x*32+32, y*32+12])
                                #left
                                level_side_left.append([x*32, y*32+12])
                                #bottom
                                level_bottom.append([x*32 + 10, y*32 + 30])
                        elif color == (255,75,0,255):
                                sand_double_corners.append([x*32,y*32])
                                level_top.append([x*32,y*32])
                                #right
                                level_side_right.append([x*32+32, y*32+12])
                                #left
                                level_side_left.append([x*32, y*32+12])
                                #bottom
                                level_bottom.append([x*32 + 10, y*32 + 30])
                        elif color == (100,100,100,255):
                                level_side_right.append([x*32+32, y*32+12])
                                level_side_left.append([x*32, y*32+12])
                        elif color == (25,25,25,255):
                                gun_color_changer.append([x*32,y*32,0,0,0])
                        elif color == (26,26,26,255):
                                gun_color_changer.append([x*32,y*32,1,0,0])
                        elif color == (26,26,26,255):
                                gun_color_changer.append([x*32,y*32,2,0,0])
                        elif color == (27,27,27,255):
                                gun_color_changer.append([x*32,y*32,3,0,0])
                                #CAVES
                        elif color == (0,150,150,255):
                                cave_ground.append([x*32,y*32])
                                level_top.append([x*32,y*32])
                                #right
                                level_side_right.append([x*32+32, y*32+12])
                                #left
                                level_side_left.append([x*32, y*32+12])
                                #bottom
                                level_bottom.append([x*32 + 10, y*32 + 30])
                        elif color == (0,150,175,255):
                                z = random.randrange(1,4)
                                cave.append([x*32,y*32, z])
                                level_top.append([x*32,y*32])
                                #right
                                level_side_right.append([x*32+32, y*32+12])
                                #left
                                level_side_left.append([x*32, y*32+12])
                                #bottom
                                level_bottom.append([x*32 + 10, y*32 + 30])
                        elif color == (0,150,100,255):
                                cave_right_corners.append([x*32,y*32])
                                level_top.append([x*32,y*32])
                                #right
                                level_side_right.append([x*32+32, y*32+12])
                                #left
                                level_side_left.append([x*32, y*32+12])
                                #bottom
                                level_bottom.append([x*32 + 10, y*32 + 30])
                        elif color == (0,150,225,255):
                                cave_left_corners.append([x*32,y*32])
                                level_top.append([x*32,y*32])
                                #right
                                level_side_right.append([x*32+32, y*32+12])
                                #left
                                level_side_left.append([x*32, y*32+12])
                                #bottom
                                level_bottom.append([x*32 + 10, y*32 + 30])
                        elif color == (0,150,250,255):
                                cave_double_corners.append([x*32,y*32])
                                level_top.append([x*32,y*32])
                                #right
                                level_side_right.append([x*32+32, y*32+12])
                                #left
                                level_side_left.append([x*32, y*32+12])
                                #bottom
                                level_bottom.append([x*32 + 10, y*32 + 30])
                                
                                
                                
                                

def draw_walls():
        for i in range(len(level_walls_red)):
            if level_walls_red[i][3] == 1:
                if -32 <= level_walls_red[i][0] <= 1056 and -32 <= level_walls_red[i][1] <= 800:
                        cur_y = level_walls_red[i][1]
                        cur_x = level_walls_red[i][0]
                
                        if level_walls_red[i][2] == 1:
                                screen.blit(grass1, (cur_x, cur_y))
                        if level_walls_red[i][2] == 2:
                                screen.blit(grass2, (cur_x, cur_y))
                        if level_walls_red[i][2] == 3:
                                 screen.blit(grass3, (cur_x, cur_y))
            else:
                if -32 <= level_walls_red[i][0] <= 1056 and -32 <= level_walls_red[i][1] <= 800:
                        cur_y = level_walls_red[i][1]
                        cur_x = level_walls_red[i][0]
                
                        if level_walls_red[i][2] == 1:
                                screen.blit(gray_grass1, (cur_x, cur_y))
                        if level_walls_red[i][2] == 2:
                                screen.blit(gray_grass2, (cur_x, cur_y))
                        if level_walls_red[i][2] == 3:
                                 screen.blit(gray_grass3, (cur_x, cur_y))
        for i in range(len(level_walls_ground)):
           if level_walls_ground[i][2] == 1:
                if -32 <= level_walls_ground[i][0] <= 1056 and -32 <= level_walls_ground[i][1] <= 800:
                        cur_y = level_walls_ground[i][1]
                        cur_x = level_walls_ground[i][0]
                        screen.blit(ground_tile, (cur_x, cur_y))
           else:
                if -32 <= level_walls_ground[i][0] <= 1056 and -32 <= level_walls_ground[i][1] <= 800:
                        cur_y = level_walls_ground[i][1]
                        cur_x = level_walls_ground[i][0]
                        screen.blit(gray_ground_tile, (cur_x, cur_y))
        for i in range(len(level_walls_l_edge)):
           if level_walls_l_edge[i][2] == 1:
                if -32 <= level_walls_l_edge[i][0] <= 1056 and -32 <= level_walls_l_edge[i][1] <= 800:
                        cur_y = level_walls_l_edge[i][1]
                        cur_x = level_walls_l_edge[i][0]
                        screen.blit(left_edge, (cur_x, cur_y))
           else:
                if -32 <= level_walls_l_edge[i][0] <= 1056 and -32 <= level_walls_l_edge[i][1] <= 800:
                        cur_y = level_walls_l_edge[i][1]
                        cur_x = level_walls_l_edge[i][0]
                        screen.blit(gray_left_edge, (cur_x, cur_y))
        for i in range(len(level_walls_r_edge)):
            if level_walls_r_edge[i][2] == 1:
                if -32 <= level_walls_r_edge[i][0] <= 1056 and -32 <= level_walls_r_edge[i][1] <= 800:
                        cur_y = level_walls_r_edge[i][1]
                        cur_x = level_walls_r_edge[i][0]
                        screen.blit(right_edge, (cur_x, cur_y))
        for i in range(len(level_walls_d_edge)):
            if level_walls_d_edge[i][2] == 1:
                if -32 <= level_walls_d_edge[i][0] <= 1056 and -32 <= level_walls_d_edge[i][1] <= 800:
                        cur_y = level_walls_d_edge[i][1]
                        cur_x = level_walls_d_edge[i][0]
                        screen.blit(double_edge, (cur_x, cur_y))
            else:
                if -32 <= level_walls_d_edge[i][0] <= 1056 and -32 <= level_walls_d_edge[i][1] <= 800:
                        cur_y = level_walls_d_edge[i][1]
                        cur_x = level_walls_d_edge[i][0]
                        screen.blit(gray_double_edge, (cur_x, cur_y))
        for i in range(len(houses)):
          if houses[i][3] == 1:
            if -224 <= houses[i][0] <= 1056 and -160 <= houses[i][1] <= 800:
                cur_x = houses[i][0]
                cur_y = houses[i][1]
                if houses[i][2] == 1:
                        screen.blit(house, (cur_x,cur_y))
                else:
                        screen.blit(house2, (cur_x,cur_y))
          else:
            if -224 <= houses[i][0] <= 1056 and -160 <= houses[i][1] <= 800:
                cur_x = houses[i][0]
                cur_y = houses[i][1]
                if houses[i][2] == 1:
                        screen.blit(gray_house, (cur_x,cur_y))
                else:
                        screen.blit(gray_house2, (cur_x,cur_y))
        for i in range(len(fences)):
                if -32 <= fences[i][0] <= 1056 and -32 <=fences[i][1] <= 800:
                        cur_x = fences[i][0]
                        cur_y = fences[i][1]
                        if fences[i][2] == 1:
                                screen.blit(green_fence, (cur_x,cur_y))
                        elif fences[i][2] == 2:
                                screen.blit(red_fence, (cur_x,cur_y))
                        elif fences[i][2] == 3:
                                screen.blit(white_fence, (cur_x,cur_y))
                        else:
                                screen.blit(gray_fence, (cur_x,cur_y))
        for i in range(len(house_walls)):
             if -32 <= house_walls[i][0] <= 1056 and -32 <= house_walls[i][1] <= 800:
                cur_x = house_walls[i][0]
                cur_y = house_walls[i][1]
                screen.blit(house_wall, (cur_x,cur_y))
        for i in range(len(house_floors)):
             if -32 <= house_floors[i][0] <= 1056 and -32 <= house_floors[i][1] <= 800:
                cur_x = house_floors[i][0]
                cur_y = house_floors[i][1]
                screen.blit(house_floor, (cur_x,cur_y))
        for i in range(len(house_ceilings)):
             if -32 <= house_ceilings[i][0] <= 1056 and -32 <= house_ceilings[i][1] <= 800:
                cur_x = house_ceilings[i][0]
                cur_y = house_ceilings[i][1]
                screen.blit(house_ceiling, (cur_x,cur_y))
        for i in range(len(house_walls)):
             if -32 <= house_walls[i][0] <= 1056 and -32 <= house_walls[i][1] <= 800:
                cur_x = house_walls[i][0]
                cur_y = house_walls[i][1]
                screen.blit(house_wall, (cur_x,cur_y))
        for i in range(len(collectibles)):
             if -32 <= collectibles[i][0] <= 1056 and -32 <= collectibles[i][1] <= 800:
                cur_x = collectibles[i][0]
                cur_y = collectibles[i][1]
                if collectibles[i][2] == 0:
                        screen.blit(collectible, (cur_x,cur_y))
                if collectibles[i][2] == 1:
                        screen.blit(collectible1, (cur_x,cur_y))
                if collectibles[i][2] == 2:
                        screen.blit(collectible2, (cur_x,cur_y))
                if collectibles[i][2] == 3:
                        screen.blit(collectible3, (cur_x,cur_y))
                if collectibles[i][2] == 4:
                        screen.blit(collectible4, (cur_x,cur_y))
                if collectibles[i][2] == 5:
                        screen.blit(collectible5, (cur_x,cur_y))
                if collectibles[i][2] == 6:
                        screen.blit(collectible6, (cur_x,cur_y))
                if collectibles[i][2] == 7:
                        screen.blit(collectible7, (cur_x,cur_y))
                if collectibles[i][2] == 8:
                        screen.blit(collectible8, (cur_x,cur_y))
                if collectibles[i][2] == 9:
                        screen.blit(collectible9, (cur_x,cur_y))
        #ICE DRAW
        for i in range(len(icy)):
                if -32 <= icy[i][0] <= 1056 and -32 <= icy[i][1] <= 800:
                        cur_x = icy[i][0]
                        cur_y = icy[i][1]
                        if icy[i][2] == 1:
                                screen.blit(ice, (cur_x,cur_y))
                        else:
                                screen.blit(ice2, (cur_x,cur_y))
        for i in range(len(icy_grounds)):
                if -32 <= icy_grounds[i][0] <= 1056 and -32 <= icy_grounds[i][1] <= 800:
                        cur_x = icy_grounds[i][0]
                        cur_y = icy_grounds[i][1]
                        screen.blit(ice_dirt, (cur_x,cur_y))
        for i in range(len(ice_right_corners)):
                if -32 <= ice_right_corners[i][0] <= 1056 and -32 <= ice_right_corners[i][1] <= 800:
                        cur_x = ice_right_corners[i][0]
                        cur_y = ice_right_corners[i][1]
                        screen.blit(ice_right_corner, (cur_x,cur_y))
        for i in range(len(ice_left_corners)):
                if -32 <= ice_left_corners[i][0] <= 1056 and -32 <= ice_left_corners[i][1] <= 800:
                        cur_x = ice_left_corners[i][0]
                        cur_y = ice_left_corners[i][1]
                        screen.blit(ice_left_corner, (cur_x,cur_y))
        for i in range(len(ice_double_corners)):
                if -32 <= ice_double_corners[i][0] <= 1056 and -32 <= ice_double_corners[i][1] <= 800:
                        cur_x = ice_double_corners[i][0]
                        cur_y = ice_double_corners[i][1]
                        screen.blit(ice_double_corner, (cur_x,cur_y))
        #LAVA DRAW
        for i in range(len(lavas)):
                if -32 <= lavas[i][0] <= 1056 and -32 <=lavas[i][1] <= 800:
                        cur_x = lavas[i][0]
                        cur_y = lavas[i][1]
                        if lavas[i][2] == 1:
                                screen.blit(lava1, (cur_x,cur_y))
                        elif lavas[i][2] == 2:
                                screen.blit(lava2, (cur_x,cur_y))
                        elif lavas[i][2] == 3:
                                screen.blit(lava3, (cur_x,cur_y))
                        elif lavas[i][2] == 4:
                                screen.blit(lava4, (cur_x,cur_y))
                        elif lavas[i][2] == 5:
                                screen.blit(lava5, (cur_x, cur_y))
        #BRICK DRAW
        for i in range(len(bricks)):
                 if -32 <= bricks[i][0] <= 1056 and -32 <=bricks[i][1] <= 800:
                        cur_x = bricks[i][0]
                        cur_y = bricks[i][1]
                        screen.blit(brick, (cur_x,cur_y))
        for i in range(len(brick_grounds)):
                if -32 <= brick_grounds[i][0] <= 1056 and -32 <=brick_grounds[i][1] <= 800:
                        cur_x = brick_grounds[i][0]
                        cur_y = brick_grounds[i][1]
                        if brick_grounds[i][2] == 1:
                                screen.blit(brick_under, (cur_x,cur_y))
                        else:
                                screen.blit(brick_under2, (cur_x,cur_y))
        for i in range(len(brick_left_corners)):
                 if -32 <= brick_left_corners[i][0] <= 1056 and -32 <=brick_left_corners[i][1] <= 800:
                        cur_x = brick_left_corners[i][0]
                        cur_y = brick_left_corners[i][1]
                        screen.blit(brick_left_corner, (cur_x,cur_y))
        for i in range(len(brick_right_corners)):
                 if -32 <= brick_right_corners[i][0] <= 1056 and -32 <=brick_right_corners[i][1] <= 800:
                        cur_x = brick_right_corners[i][0]
                        cur_y = brick_right_corners[i][1]
                        screen.blit(brick_right_corner, (cur_x,cur_y))
        #ROCK DRAW
        for i in range(len(rocks)):
                 if -32 <= rocks[i][0] <= 1056 and -32 <=rocks[i][1] <= 800:
                        cur_x = rocks[i][0]
                        cur_y = rocks[i][1]
                        if rocks[i][2] == 1:
                                screen.blit(rock, (cur_x,cur_y))
                        elif rocks[i][2] == 2:
                                screen.blit(rock2, (cur_x,cur_y))
                        else:
                                screen.blit(rock3, (cur_x,cur_y))
        for i in range(len(rock_ground)):
                 if -32 <= rock_ground[i][0] <= 1056 and -32 <=rock_ground[i][1] <= 800:
                        cur_x = rock_ground[i][0]
                        cur_y = rock_ground[i][1]
                        screen.blit(rock_grounds, (cur_x,cur_y))
        for i in range(len(rock_right_corners)):
                 if -32 <= rock_right_corners[i][0] <= 1056 and -32 <=rock_right_corners[i][1] <= 800:
                        cur_x = rock_right_corners[i][0]
                        cur_y = rock_right_corners[i][1]
                        screen.blit(rock_corner_right, (cur_x,cur_y))
        for i in range(len(rock_left_corners)):
                 if -32 <= rock_left_corners[i][0] <= 1056 and -32 <=rock_left_corners[i][1] <= 800:
                        cur_x = rock_left_corners[i][0]
                        cur_y = rock_left_corners[i][1]
                        screen.blit(rock_corner_left, (cur_x,cur_y))
        for i in range(len(rock_double_corners)):
                 if -32 <= rock_double_corners[i][0] <= 1056 and -32 <=rock_double_corners[i][1] <= 800:
                        cur_x = rock_double_corners[i][0]
                        cur_y = rock_double_corners[i][1]
                        screen.blit(rock_double_corner, (cur_x,cur_y))
        #SAND SECTION
        for i in range(len(sands)):
             if -32 <= sands[i][0] <= 1056 and -32 <=sands[i][1] <= 800:
                        cur_x = sands[i][0]
                        cur_y = sands[i][1]
                        if sands[i][2] == 1:
                                screen.blit(sand1, (cur_x,cur_y))
                        elif sands[i][2] == 2:
                                screen.blit(sand2, (cur_x,cur_y))
                        else:
                                screen.blit(sand3, (cur_x,cur_y))
        for i in range(len(sand_grounds)):
             if -32 <= sand_grounds[i][0] <= 1056 and -32 <=sand_grounds[i][1] <= 800:
                        cur_x = sand_grounds[i][0]
                        cur_y = sand_grounds[i][1]
                        if sand_grounds[i][2] == 1:
                                screen.blit(sand_ground, (cur_x,cur_y))
                        else:
                                screen.blit(sand_ground2, (cur_x,cur_y))
        for i in range(len(sand_right_corner)):
                if -32 <= sand_right_corner[i][0] <= 1056 and -32 <=sand_right_corner[i][1] <= 800:
                        cur_x = sand_right_corner[i][0]
                        cur_y = sand_right_corner[i][1]
                        screen.blit(sand_corner_right, (cur_x, cur_y))
        for i in range(len(sand_left_corner)):
                if -32 <= sand_left_corner[i][0] <= 1056 and -32 <=sand_left_corner[i][1] <= 800:
                        cur_x = sand_left_corner[i][0]
                        cur_y = sand_left_corner[i][1]
                        screen.blit(sand_corner_left, (cur_x, cur_y))
        for i in range(len(sand_double_corners)):
                if -32 <= sand_double_corners[i][0] <= 1056 and -32 <=sand_double_corners[i][1] <= 800:
                        cur_x = sand_double_corners[i][0]
                        cur_y = sand_double_corners[i][1]
                        screen.blit(sand__double_corner, (cur_x, cur_y))
        #Cave DRAW
        for i in range(len(cave)):
                 if -32 <= cave[i][0] <= 1056 and -32 <= cave[i][1] <= 800:
                        cur_x = cave[i][0]
                        cur_y = cave[i][1]
                        if cave[i][2] == 1:
                                screen.blit(caves, (cur_x,cur_y))
                        elif cave[i][2] == 2:
                                screen.blit(cave2, (cur_x,cur_y))
                        else:
                                screen.blit(cave3, (cur_x,cur_y))
        for i in range(len(cave_ground)):
                 if -32 <= cave_ground[i][0] <= 1056 and -32 <=cave_ground[i][1] <= 800:
                        cur_x = cave_ground[i][0]
                        cur_y = cave_ground[i][1]
                        screen.blit(cave_grounds, (cur_x,cur_y))
        for i in range(len(cave_right_corners)):
                 if -32 <= cave_right_corners[i][0] <= 1056 and -32 <=cave_right_corners[i][1] <= 800:
                        cur_x = cave_right_corners[i][0]
                        cur_y = cave_right_corners[i][1]
                        screen.blit(cave_corner_right, (cur_x,cur_y))
        for i in range(len(cave_left_corners)):
                 if -32 <= cave_left_corners[i][0] <= 1056 and -32 <=cave_left_corners[i][1] <= 800:
                        cur_x = cave_left_corners[i][0]
                        cur_y = cave_left_corners[i][1]
                        screen.blit(cave_corner_left, (cur_x,cur_y))
        for i in range(len(cave_double_corners)):
                 if -32 <= cave_double_corners[i][0] <= 1056 and -32 <=cave_double_corners[i][1] <= 800:
                        cur_x = cave_double_corners[i][0]
                        cur_y = cave_double_corners[i][1]
                        screen.blit(cave_double_corner, (cur_x,cur_y))

        
                

def draw_switch():
        for i in range(len(switch)):
                if switch[i][3] == 1:
                        if switch[i][2] == 1:
                                screen.blit(switch_green, (switch[i][0], switch[i][1]))
                        if switch[i][2] == 2:
                                screen.blit(switch_green_press, (switch[i][0], switch[i][1]))
                elif switch[i][3] == 2:
                        if switch[i][2] == 1:
                                screen.blit(switch_blue, (switch[i][0], switch[i][1]))
                        if switch[i][2] == 2:
                                screen.blit(switch_blue_press, (switch[i][0], switch[i][1]))
                       

def draw_crawlers():
        for i in range(len(enemy_crawler)):
                if -32 <= enemy_crawler[i][0] <= 1056 and -32 <= enemy_crawler[i][1] <= 800:
                        cur_y = enemy_crawler[i][1]
                        cur_x = enemy_crawler[i][0]
                        if enemy_crawler[i][8] == 1:
                                if enemy_crawler[i][2] == 1:
                                        if enemy_crawler[i][3] == 2:
                                                if enemy_crawler[i][4] == 1:
                                                        screen.blit(crawler, (cur_x, cur_y))
                                                else:
                                                        screen.blit(crawler_run, (cur_x, cur_y))
                                        else:
                                                if enemy_crawler[i][4] == 1:
                                                        screen.blit(crawler_left, (cur_x, cur_y))
                                                else:
                                                        screen.blit(crawler_left_run, (cur_x, cur_y))
                                else:
                                        if enemy_crawler[i][3] == 2:
                                                if enemy_crawler[i][7] == 1:
                                                        screen.blit(crawler_die1, (cur_x, cur_y -6))
                                                        #print("right die 1")
                                                if enemy_crawler[i][7] == 2:
                                                        screen.blit(crawler_die2, (cur_x, cur_y -12))
                                                        #print("right die 2")
                                                if enemy_crawler[i][7] == 3:
                                                        screen.blit(crawler_die3, (cur_x, cur_y -6))
                                                        #print("right die 3")
                                                if enemy_crawler[i][7] >= 4:
                                                        screen.blit(crawler_die4, (cur_x, cur_y))
                                                        #print("right die 4")
                        
                                        else:
                                                if enemy_crawler[i][7] == 1:
                                                        screen.blit(crawler_die_left1, (cur_x, cur_y-6))
                                                        #print("left die 1")
                                                if enemy_crawler[i][7] == 2:
                                                        screen.blit(crawler_die_left2, (cur_x, cur_y-12))
                                                        #print("left die 2")
                                                if enemy_crawler[i][7] == 3:
                                                        screen.blit(crawler_die_left3, (cur_x, cur_y-6))
                                                        #print("left die 3")
                                                if enemy_crawler[i][7] >= 4:
                                                        screen.blit(crawler_die_left4, (cur_x, cur_y))
                                                        #print("left die 4")

def draw_flying():
        for i in range(len(enemy_flying)):
                if -32 <= enemy_flying[i][0] <= 1056 and -32 <= enemy_flying[i][1] <= 800:
                        cur_y = enemy_flying[i][1]
                        cur_x = enemy_flying[i][0]
                        if enemy_flying[i][8] == 1:
                                if enemy_flying[i][2] == 1:
                                   if enemy_flying[i][10] == 2:
                                        if enemy_flying[i][3] == 2:
                                                if enemy_flying[i][4] == 1:
                                                        screen.blit(flying, (cur_x, cur_y))
                                                else:
                                                        screen.blit(flying_run, (cur_x, cur_y))
                                                           
                                        else:
                                                if enemy_flying[i][4] == 1:
                                                        screen.blit(flying_left, (cur_x, cur_y))
                                                else:
                                                        screen.blit(flying_left_run, (cur_x, cur_y))
                                   else:
                                           if x_coord >= enemy_flying[i][0]:
                                                   if enemy_flying[i][4] == 1:
                                                        screen.blit(flying, (cur_x, cur_y))
                                                   else:
                                                        screen.blit(flying_run, (cur_x, cur_y))
                                           else:
                                                   if enemy_flying[i][4] == 1:
                                                        screen.blit(flying_left, (cur_x, cur_y))
                                                   else:
                                                        screen.blit(flying_left_run, (cur_x, cur_y))
                                else:
                                        if enemy_flying[i][3] == 2:
                                                screen.blit(flying_die_right, (cur_x,cur_y))
                        
                                        else:
                                                screen.blit(flying_die, (cur_x,cur_y))
                                                
def crawler_collide(x,y):
        player_rect = pygame.Rect(x_coord,y_coord,38,50)
        crawler_rect = pygame.Rect(x,y + 38,64,26)
        if player_rect.colliderect(crawler_rect) == True:
                return True
        else:
                return False

def crawler_switch_directions(x,y,a,b):
        crawler_rect = pygame.Rect(x,y,64,32)
        range_rect = pygame.Rect(a,b,2,64)
        if crawler_rect.colliderect(range_rect) == True:
                return True
        else:
                return False

def flying_collide(x,y):
        player_rect = pygame.Rect(x_coord,y_coord,38,50)
        crawler_rect = pygame.Rect(x,y,32,32)
        if player_rect.colliderect(crawler_rect) == True:
                return True
        else:
                return False

def flying_switch_directions(x,y,a,b):
        crawler_rect = pygame.Rect(x,y,32,32)
        range_rect = pygame.Rect(a,b,2,64)
        if crawler_rect.colliderect(range_rect) == True:
                return True
        else:
                return False

def draw_puffpuff():
        #x coord, y coord, alive(1) or dead(2), direction(left 1)(right 2), walking or not,
                                #run change, which run to go to next,
                                #kill enemy counter, jumping, jumping stop point, jumping speed,
                                #what type of puffpuff eg forest snow desert]
        for i in range(len(enemy_puffpuff)):
                if -32 <= enemy_puffpuff[i][0] <= 1056 and -32 <= enemy_puffpuff[i][1] <= 800:
                        cur_y = enemy_puffpuff[i][1]
                        cur_x = enemy_puffpuff[i][0]
                        if enemy_puffpuff[i][2] == 1:
                                if enemy_puffpuff[i][3] == 2:
                                        if enemy_puffpuff[i][8] == 2:
                                                screen.blit(puffpuff_jump, (cur_x, cur_y))
                                        else:
                                                if enemy_puffpuff[i][4] == 1:
                                                        screen.blit(puffpuff_1, (cur_x, cur_y))
                                                if enemy_puffpuff[i][4] == 2:
                                                        screen.blit(puffpuff_2, (cur_x, cur_y))
                                                if enemy_puffpuff[i][4] == 3:
                                                        screen.blit(puffpuff_3, (cur_x, cur_y))
                                elif enemy_puffpuff[i][3] == 1:
                                        if enemy_puffpuff[i][8] == 2:
                                                screen.blit(puffpuff_jump_left, (cur_x, cur_y))
                                        else:
                                                if enemy_puffpuff[i][4] == 1:
                                                        screen.blit(puffpuff_left_1, (cur_x, cur_y))
                                                if enemy_puffpuff[i][4] == 2:
                                                        screen.blit(puffpuff_left_2, (cur_x, cur_y))
                                                if enemy_puffpuff[i][4] == 3:
                                                        screen.blit(puffpuff_left_3, (cur_x, cur_y))
                        else:
                               if enemy_puffpuff[i][3] == 1:
                                       screen.blit(puffpuff_die, (cur_x, cur_y))
                               else:
                                       screen.blit(puffpuff_die_left, (cur_x, cur_y))

def puffpuff_collide(x,y):
        player_rect = pygame.Rect(x_coord,y_coord,38,50)
        puffpuff_rect = pygame.Rect(x,y + 32,64,32)
        if player_rect.colliderect(puffpuff_rect) == True:
                return True
        else:
                return False

def puffpuff_switch_directions(x,y,a,b):
        puffpuff_rect = pygame.Rect(x,y + 32,64,32)
        range_rect = pygame.Rect(a,b,2,350)
        if puffpuff_rect.colliderect(range_rect) == True:
                return True
        else:
                return False

def collide_collectible(x,y):
        player_rect = pygame.Rect(x_coord,y_coord,38,50)
        collectible_rect = pygame.Rect(x,y ,32,32)
        if player_rect.colliderect(collectible_rect) == True:
                return True
        else:
                return False

def draw_bridge_ladder():
        for i in range(len(ladders)):
                if -32 <= ladders[i][0] <= 1056 and -32 <= ladders[i][1] <= 800:
                        cur_x = ladders[i][0]
                        cur_y = ladders[i][1]
                        screen.blit(ladder, (cur_x, cur_y))
        for i in range(len(bridges)):
                if -32 <= bridges[i][0] <= 1056 and -32 <= bridges[i][1] <= 800:
                        cur_x = bridges[i][0]
                        cur_y = bridges[i][1]
                        screen.blit(bridge, (cur_x, cur_y))
        for i in range(len(bridges_right)):
                if -32 <= bridges_right[i][0] <= 1056 and -32 <= bridges_right[i][1] <= 800:
                        cur_x = bridges_right[i][0]
                        cur_y = bridges_right[i][1]
                        screen.blit(bridge_right, (cur_x, cur_y))
        for i in range(len(bridges_left)):
                if -32 <= bridges_left[i][0] <= 1056 and -32 <= bridges_left[i][1] <= 800:
                        cur_x = bridges_left[i][0]
                        cur_y = bridges_left[i][1]
                        screen.blit(bridge_left, (cur_x, cur_y))

def draw_falling_blocks():
        for i in range(len(falling_blocks)):
                if -32 <= falling_blocks[i][0] <= 1056 and -32 <= falling_blocks[i][1] <= 800 and falling_blocks[i][6] == 0:
                        cur_x = falling_blocks[i][0]
                        cur_y = falling_blocks[i][1]
                        screen.blit(bridge, (cur_x, cur_y))
        for i in range(len(stalactites)):
                if -32 <= stalactites[i][0] <= 1056 and -32 <= stalactites[i][1] <= 800:
                        cur_x = stalactites[i][0]
                        cur_y = stalactites[i][1]
                        if stalactites[i][7] == 0:
                                screen.blit(stalactite_cave, (cur_x, cur_y))
                        elif stalactites[i][7] == 1:
                                screen.blit(stalactite_ice, (cur_x, cur_y))

def stalactite_collide(x,y):
        player_rect = pygame.Rect(x_coord,y_coord,38,50)
        stalactite_rect = pygame.Rect(x,y ,32,64)
        if player_rect.colliderect(stalactite_rect) == True:
                return True
        else:
                return False

def stalactite_range_collide(x,y,a,b):
        range_rect = pygame.Rect(a,b,32,32)
        stalactite_rect = pygame.Rect(x,y ,32,64)
        if range_rect.colliderect(stalactite_rect) == True:
                return True
        else:
                return False

def draw_doors():
    for i in range(len(next_level)):
        if -32 <= next_level[i][0] <= 1056 and -32 <= next_level[i][1] <= 800:
            cur_x = next_level[i][0]
            cur_y = next_level[i][1]
            if next_level[i][2] == 1:
                screen.blit(door, (cur_x,cur_y))
            else:
                 screen.blit(door2, (cur_x,cur_y))
        
def draw_water():
    for i in range(len(water)):
        if -32 <= water[i][0] <= 1056 and -32 <= water[i][1] <= 800:
            cur_x = water[i][0]
            cur_y = water[i][1]
            screen.blit(water_image, (cur_x,cur_y))
    for i in range(len(water_grounds)):
        if -32 <= water_grounds[i][0] <= 1056 and -32 <= water_grounds[i][1] <= 800:
            cur_x = water_grounds[i][0]
            cur_y = water_grounds[i][1]
            screen.blit(water_ground, (cur_x,cur_y))
            
def water_collide(x,y):
        player_rect = pygame.Rect(x_coord,y_coord,38,50)
        water_rect = pygame.Rect(x+2,y+2,28,30)
        if player_rect.colliderect(water_rect) == True:
                return True
        else:
                return False
            
def water_ground_collide(x,y):
    player_rect = pygame.Rect(x_coord,y_coord,38,50)
    water_ground_rect = pygame.Rect(x,y,32,32)
    if player_rect.colliderect(water_ground_rect) == True:
        return True
                
    else:
        return False
            
def draw_collision():
        for i in range(len(level_top)):
                pygame.draw.rect(screen,red, (level_top[i][0]+11,level_top[i][1],10,2))
        for i in range(len(level_side_left)):
                pygame.draw.rect(screen, red, (level_side_left[i][0],level_side_left[i][1],2,8))
        for i in range(len(level_side_right)):
                pygame.draw.rect(screen, red, (level_side_right[i][0],level_side_right[i][1],2,8))
        for i in range(len(level_bottom)):
                pygame.draw.rect(screen, red, (level_bottom[i][0],level_bottom[i][1],16,2))

def top_check(x,y): 
        player_rect = pygame.Rect(x_coord,y_coord,38,50)
        top_rect = pygame.Rect(x+10,y,12,2)
        if player_rect.colliderect(top_rect) == True:
                return True
                
        else:
                return False

def side_check(x,y):
        player_rect = pygame.Rect(x_coord,y_coord,38,50)
        side_rect = pygame.Rect(x,y,2,8)
        if player_rect.colliderect(side_rect) == True:
               return True
                
        else:
             return False
        
def bottom_check(x,y):
        player_rect = pygame.Rect(x_coord,y_coord,38,50)
        bottom_rect = pygame.Rect(x,y,12,2)
        if player_rect.colliderect(bottom_rect) == True:
                return True
                
        else:
                return False

#doors!
def door_check(x,y):
    player_rect = pygame.Rect(x_coord,y_coord,38,50)
    door_rect = pygame.Rect(x,y,32,64)
    if player_rect.colliderect(door_rect) == True:
        return True
                
    else:
        return False

def ladder_check(x,y):
    player_rect = pygame.Rect(x_coord,y_coord,38,50)
    ladder_rect = pygame.Rect(x+12,y,8,32)
    if player_rect.colliderect(ladder_rect) == True:
        return True
                
    else:
        return False

def draw_quicksand():
        for i in range(len(quicksand)):
                if -32 <= quicksand[i][0] <= 1056 and -32 <= quicksand[i][1] <= 800:
                        cur_x = quicksand[i][0]
                        cur_y = quicksand[i][1]
                        if quicksand[i][3] == 1:
                                screen.blit(quicksand1, (cur_x,cur_y))
                        elif quicksand[i][3] == 2:
                                screen.blit(quicksand2, (cur_x,cur_y))
                        elif quicksand[i][3] == 3:
                                screen.blit(quicksand3, (cur_x,cur_y))
                        elif quicksand[i][3] == 4:
                                screen.blit(quicksand4, (cur_x,cur_y))

def draw_player(x,y):
        if direction == 2:
                if on_ground == True or on_ladder == True:
                        if knockback == True:
                                screen.blit(player_jumping,(x,y))
                        if knockback == False:
                                if x_speed > 0 and running == 2:
                                    if w_press == False and on_ladder == False:
                                        screen.blit(player_running,(x,y))
                                    else:
                                        screen.blit(player_back, (x,y))
                                elif x_speed == 0 and idle == 2:
                                        screen.blit(player_idle,(x,y))
                                        
                                else:
                                    if w_press == False and on_ladder == False:
                                        screen.blit(player,(x,y))
                                    else:
                                        screen.blit(player_back, (x,y))
                else:
                        screen.blit(player_jumping,(x,y))

                if w_press == False:
                   if gun_color == "red":
                        if idle == 1:
                                if  x_cross >= 550 and 100 <= y_cross <= 658:
                                        if gun_count == 0:
                                                screen.blit(red_gun, (x+5,y+21))
                                        elif gun_count >= 30:
                                                screen.blit(red_gun_charge1, (x+5,y+21))
                                        elif gun_count >= 1:
                                                screen.blit(red_gun_charge2, (x+5,y+21))
                                else:
                                        if gun_count >= 30:
                                                screen.blit(red_gun_charge1, (x+5,y+21))
                                        elif gun_count >= 1:
                                                screen.blit(red_gun_charge2, (x+5,y+21))
                                        else:
                                                screen.blit(red_gun_dark, (x+5,y+21))
                        elif idle == 2:
                                if  x_cross >= 550 and 100 <= y_cross <= 658:
                                        if gun_count == 0:
                                                screen.blit(red_gun, (x+5,y+23))
                                        elif gun_count >= 30:
                                                screen.blit(red_gun_charge1, (x+5,y+23))
                                        elif gun_count >= 1:
                                                screen.blit(red_gun_charge2, (x+5,y+23))
                                else:
                                        if gun_count >= 30:
                                                screen.blit(red_gun_charge1, (x+5,y+23))
                                        elif gun_count >= 1:
                                                screen.blit(red_gun_charge2, (x+5,y+23))
                                        
                                        else:
                                                screen.blit(red_gun_dark, (x+5,y+23))
                   elif gun_color == "blue":
                        if idle == 1:
                                if  x_cross >= 550 and 100 <= y_cross <= 658:
                                        if gun_count == 0:
                                                screen.blit(blue_gun, (x+6,y+21))
                                        elif gun_count >= 30:
                                                screen.blit(blue_gun_charge1, (x+6,y+21))
                                        elif gun_count >= 1:
                                                screen.blit(blue_gun_charge2, (x+6,y+21))
                                else:
                                        if gun_count >= 30:
                                                screen.blit(blue_gun_charge1, (x+6,y+21))
                                        elif gun_count >= 1:
                                                screen.blit(blue_gun_charge2, (x+6,y+21))
                                        else:
                                                screen.blit(blue_gun_dark, (x+6,y+21))
                        elif idle == 2:
                                if  x_cross >= 550 and 100 <= y_cross <= 658:
                                        if gun_count == 0:
                                                screen.blit(blue_gun, (x+6,y+23))
                                        elif gun_count >= 30:
                                                screen.blit(blue_gun_charge1, (x+6,y+23))
                                        elif gun_count >= 1:
                                                screen.blit(blue_gun_charge2, (x+6,y+23))
                                else:
                                        if gun_count >= 30:
                                                screen.blit(blue_gun_charge1, (x+6,y+23))
                                        elif gun_count >= 1:
                                                screen.blit(blue_gun_charge2, (x+6,y+23))
                                        
                                        else:
                                                screen.blit(blue_gun_dark, (x+6,y+23))
                   elif gun_color == "green":
                        if idle == 1:
                                if  x_cross >= 550 and 100 <= y_cross <= 658:
                                        if gun_count == 0:
                                                screen.blit(green_gun, (x+11,y+21))
                                        elif gun_count >= 30:
                                                screen.blit(green_gun_charge1, (x+11,y+21))
                                        elif gun_count >= 1:
                                                screen.blit(green_gun_charge2, (x+11,y+21))
                                else:
                                        if gun_count >= 30:
                                                screen.blit(green_gun_charge1, (x+11,y+21))
                                        elif gun_count >= 1:
                                                screen.blit(green_gun_charge2, (x+11,y+21))
                                        else:
                                                screen.blit(green_gun_dark, (x+11,y+21))
                        elif idle == 2:
                                if  x_cross >= 550 and 100 <= y_cross <= 658:
                                        if gun_count == 0:
                                                screen.blit(green_gun, (x+11,y+23))
                                        elif gun_count >= 30:
                                                screen.blit(green_gun_charge1, (x+11,y+23))
                                        elif gun_count >= 1:
                                                screen.blit(green_gun_charge2, (x+11,y+23))
                                else:
                                        if gun_count >= 30:
                                                screen.blit(green_gun_charge1, (x+11,y+23))
                                        elif gun_count >= 1:
                                                screen.blit(green_gun_charge2, (x+11,y+23))
                                        
                                        else:
                                                screen.blit(green_gun_dark, (x+11,y+23))
        else:
                if on_ground == True or on_ladder == True:
                        if knockback == True:
                                screen.blit(player_jumping_left,(x,y))
                        if knockback == False:
                                if x_speed < 0 and running == 2:
                                    if w_press == False and on_ladder == False:
                                        screen.blit(player_running_left,(x,y))
                                    else:
                                        screen.blit(player_left_back, (x,y))
                                elif x_speed == 0 and idle == 2:
                                        screen.blit(player_idle_left,(x,y))
                                else:
                                    if w_press == False and on_ladder == False:
                                        screen.blit(player_left,(x,y))
                                    else:
                                        screen.blit(player_left_back, (x,y))
                else:
                        screen.blit(player_jumping_left,(x,y))
                if w_press == False:        
                   if gun_color == "red":
                        if idle == 1:
                                if  x_cross <= 470 and 100 <= y_cross <= 658:
                                        if gun_count == 0:
                                                screen.blit(red_gun_left, (x-5,y+21))
                                        elif gun_count >= 30:
                                                screen.blit(red_gun_charge1_left, (x-5,y+21))
                                        elif gun_count >= 1:
                                                screen.blit(red_gun_charge2_left, (x-5,y+21))
                                else:
                                        if gun_count >= 30:
                                                screen.blit(red_gun_charge1_left, (x-5,y+21))
                                        elif gun_count >= 1:
                                                screen.blit(red_gun_charge2_left, (x-5,y+21))
                                        else:
                                                screen.blit(red_gun_dark_left, (x-5,y+21))
                        elif idle == 2:
                                if  x_cross <= 470 and 100 <= y_cross <= 658:
                                        if gun_count == 0:
                                                screen.blit(red_gun_left, (x-5,y+23))
                                        elif gun_count >= 30:
                                                screen.blit(red_gun_charge1_left, (x-5,y+23))
                                        elif gun_count >= 1:
                                                screen.blit(red_gun_charge2_left, (x-5,y+23))
                                else:
                                        if gun_count >= 30:
                                                screen.blit(red_gun_charge1_left, (x-5,y+23))
                                        elif gun_count >= 1:
                                                screen.blit(red_gun_charge2_left, (x-5,y+23))
                                        
                                        else:
                                                screen.blit(red_gun_dark_left, (x-5,y+23))
                   elif gun_color == "blue":
                        if idle == 1:
                                if  x_cross <= 470 and 100 <= y_cross <= 658:
                                        if gun_count == 0:
                                                screen.blit(blue_gun_left, (x-6,y+21))
                                        elif gun_count >= 30:
                                                screen.blit(blue_gun_charge1_left, (x-6,y+21))
                                        elif gun_count >= 1:
                                                screen.blit(blue_gun_charge2_left, (x-6,y+21))
                                else:
                                        if gun_count >= 30:
                                                screen.blit(blue_gun_charge1_left, (x-6,y+21))
                                        elif gun_count >= 1:
                                                screen.blit(blue_gun_charge2_left, (x-6,y+21))
                                        else:
                                                screen.blit(blue_gun_dark_left, (x-6,y+21))
                        elif idle == 2:
                                if  x_cross <= 470 and 100 <= y_cross <= 658:
                                        if gun_count == 0:
                                                screen.blit(blue_gun_left, (x-6,y+23))
                                        elif gun_count >= 30:
                                                screen.blit(blue_gun_charge1_left, (x-6,y+23))
                                        elif gun_count >= 1:
                                                screen.blit(blue_gun_charge2_left, (x-6,y+23))
                                else:
                                        if gun_count >= 30:
                                                screen.blit(blue_gun_charge1_left, (x-6,y+23))
                                        elif gun_count >= 1:
                                                screen.blit(blue_gun_charge2_left, (x-6,y+23))
                                        
                                        else:
                                                screen.blit(blue_gun_dark_left, (x-6,y+23))
                   elif gun_color == "green":
                        if idle == 1:
                                if  x_cross <= 470 and 100 <= y_cross <= 658:
                                        if gun_count == 0:
                                                screen.blit(green_gun_left, (x-11,y+21))
                                        elif gun_count >= 30:
                                                screen.blit(green_gun_charge1_left, (x-11,y+21))
                                        elif gun_count >= 1:
                                                screen.blit(green_gun_charge2_left, (x-11,y+21))
                                else:
                                        if gun_count >= 30:
                                                screen.blit(green_gun_charge1_left, (x-11,y+21))
                                        elif gun_count >= 1:
                                                screen.blit(green_gun_charge2_left, (x-11,y+21))
                                        else:
                                                screen.blit(green_gun_dark_left, (-+11,y+21))
                        elif idle == 2:
                                if  x_cross <= 470 and 100 <= y_cross <= 658:
                                        if gun_count == 0:
                                                screen.blit(green_gun_left, (x-11,y+23))
                                        elif gun_count >= 30:
                                                screen.blit(green_gun_charge1_left, (x-11,y+23))
                                        elif gun_count >= 1:
                                                screen.blit(green_gun_charge2_left, (x-11,y+23))
                                else:
                                        if gun_count >= 30:
                                                screen.blit(green_gun_charge1_left, (x-11,y+23))
                                        elif gun_count >= 1:
                                                screen.blit(green_gun_charge2_left, (x-11,y+23))
                                        
                                        else:
                                                screen.blit(green_gun_dark_left, (x-11,y+23))
                        


def get_gun_movement():
    x_distance = x_coord - x_cross + 17
    y_distance = y_coord - y_cross + 25
    total_distance = math.sqrt(x_distance ** 2 + y_distance ** 2)
    gun_x_speed = x_distance / total_distance * 19
    gun_y_speed = y_distance / total_distance * 19
    gun_speed.append([gun_x_speed,gun_y_speed])

def gun_movement():
    for i in range(len(gun_list)):
        gun_list[i][0] -= gun_speed[i][0]
        gun_list[i][1] -= gun_speed[i][1]

def draw_bullets():
    for i in range(len(gun_list)):
            if gun_color == "red":
                pygame.draw.rect(screen,red,[gun_list[i][0],gun_list[i][1], 5,5])
            elif gun_color == "blue":
                pygame.draw.rect(screen,black,[gun_list[i][0],gun_list[i][1], 5,5])
            elif gun_color == "green":
                pygame.draw.rect(screen,green,[gun_list[i][0],gun_list[i][1], 5,5])

def draw_health(health):
    if 1 <= health <= 20:
        last = 0
        for i in range(health//2):
            screen.blit(left_heart, (700 + i * 30,35))
            screen.blit(right_heart,(712 + i * 30,35))
            last = i
        if health%2==1:
            if health == 1:
                screen.blit(left_heart, (700 + (last) * 30, 35))
            else:
                screen.blit(left_heart, (700 + (last+1) * 30, 35))

def door_screen(x):
    if loading_screen == True:
        pygame.draw.rect(screen,black,[0,0,1024,784,], x)

def draw_air(air):
    if 1 <= air <= 10:
        for i in range(air):
            screen.blit(bubble, (700 + i * 30, 60))

def draw_villagers():
    for i in range(len(villager)):
      if villager[i][8] == 0:
        if villager[i][5] == 2:
            if villager[i][2] == 1:           
                screen.blit(player_running_left, (villager[i][0],villager[i][1]))
            else:
                screen.blit(player_running, (villager[i][0],villager[i][1]))
        else:
            if villager[i][2] == 1:           
                screen.blit(player_left, (villager[i][0],villager[i][1]))
            else:
                screen.blit(player, (villager[i][0],villager[i][1]))
      else:
                screen.blit(elder, (villager[i][0], villager[i][1]))

def talk_to_villagers(x,y):
    player_rect = pygame.Rect(x_coord,y_coord,38,50)
    villager_rect = pygame.Rect(x-10,y,48,50)
    if player_rect.colliderect(villager_rect) == True:
        return True
                
    else:
        return False

def draw_signs():
    for i in range(len(signs)):
        if signs[i][2] == 1:
                screen.blit(sign, (signs[i][0],signs[i][1]))
        else:
                screen.blit(gray_sign, (signs[i][0],signs[i][1]))

def read_the_sign(x,y):
    player_rect = pygame.Rect(x_coord,y_coord,38,50)
    sign_rect = pygame.Rect(x,y,32,32)
    if player_rect.colliderect(sign_rect) == True:
        return True
                
    else:
        return False

def draw_time_bar(x,y,j,k,l,m):
        pygame.draw.rect(screen,black,[x-5,y-5,l,m])
        pygame.draw.rect(screen,green,[x,y,j,k])

def collide_switch(x,y):
    player_rect = pygame.Rect(x_coord,y_coord,38,50)
    switch_rect = pygame.Rect(x,y + 5,32,27)
    if player_rect.colliderect(switch_rect) == True:
        return True
                
    else:
        return False

def draw_gun_color_changer():
        for i in range(len(gun_color_changer)):
                if gun_color_changer[i][2] == 0:
                        screen.blit(red_gun, (gun_color_changer[i][0],gun_color_changer[i][1] + gun_color_changer[i][4]))
                elif gun_color_changer[i][2] == 1:
                        screen.blit(blue_gun, (gun_color_changer[i][0],gun_color_changer[i][1] + gun_color_changer[i][4]))
                else:
                        screen.blit(green_gun, (gun_color_changer[i][0],gun_color_changer[i][1] + gun_color_changer[i][4]))

getRGB()
getmgRGB()
getenemyRGB()
draw_walls()
load_music(level_music[0] + ".ogg")
pygame.mixer.music.play(-1)
for i in range(len(switch)):
        switch_count += 1

#HERE
for i in range(len(level_doors)):
                            if previous_level == level_doors[i]:
                                x_screen = next_level[i][0] - 3
                                y_screen = next_level[i][1] + 13
                                x_speed = x_screen - x_coord
                                y_speed = y_screen - y_coord
                                scroll(x_speed,y_speed)
                                scroll_mg(x_speed,y_speed)
                                scroll_enemies(x_speed, y_speed)
                                x_speed = 0
                                y_speed = 0

joystick_count=pygame.joystick.get_count()
if joystick_count == 0:
    # No joysticks!
    print ("Error, I didn't find any joysticks.")
else:
    # Use joystick #0 and initialize it
    my_joystick = pygame.joystick.Joystick(0)
    my_joystick.init()

while done == False:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_f:
                                health -= 1
                                press_key_f = True
                        if event.key == pygame.K_a:
                                direction = 1
                                switch_running = 0
                                a_press = True
                                d_press = False
                                move_left = True
                                move_right = False
                        if event.key == pygame.K_d:
                                direction = 2
                                switch_running = 0
                                move_left = False
                                move_right =True
                                a_press = False
                                d_press = True
                        if event.key == pygame.K_w:
                            if change_level == True:
                                closing_screen = True
                                talking = False
                                at_sign = False
                                w_press = True
                                        
                            if talking == True:
                                write_text = True
                                w_press = True

                            if at_sign == True:
                                read_sign = True
                                w_press = True

                            if at_ladder == True:
                                y_speed = -5
                                on_ladder = True
                                w_press = True

                        if event.key == pygame.K_SPACE:
                                if on_ground == True or on_ladder == True:
                                        y_speed=-20
                                        on_ladder = False
                                elif in_quicksand == True:
                                        y_speed = -5
                        if event.key == pygame.K_ESCAPE:
                                done = True
                        if event.key == pygame.K_LSHIFT:
                                lshift_press = True
                                shift_run = True

                        if event.key == pygame.K_s:
                            if on_ladder == True:
                                y_speed = 5

                        if event.key == pygame.K_l:
                                save_info = []
                                save_load(save)
                                current_level=save_info[0]
                                print(current_level)
                                previous_level=save_info[1]
                                print(previous_level)
                                gun_color=save_info[2]
                                print(gun_color)
                                health=save_info[3]
                                print(health)
                                #collectible_count=save_info[4]

                if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                                if gun_count == 0:
                                        if gun_color == "red":
                                                if x_cross >= 550 and 100 <= y_cross <= 658 and direction == 2:
                                                        gunshot.play()
                                                        gun_count = 60
                                                        gun_count += 1
                                                        gun_list.append([x_coord+44,y_coord+21, 0])
                                                        get_gun_movement()
                                                if x_cross <= 470 and 100 <= y_cross <= 658 and direction == 1:
                                                        gunshot.play()
                                                        gun_count = 60
                                                        gun_count += 1
                                                        gun_list.append([x_coord-5,y_coord+21, 0])
                                                        get_gun_movement()
                                        if gun_color == "blue":
                                                if x_cross >= 550 and 100 <= y_cross <= 658 and direction == 2:
                                                        gunshot.play()
                                                        gun_count = 40
                                                        gun_count += 1
                                                        gun_list.append([x_coord+44,y_coord+21, 0])
                                                        get_gun_movement()
                                                if x_cross <= 470 and 100 <= y_cross <= 658 and direction == 1:
                                                        gunshot.play()
                                                        gun_count = 40
                                                        gun_count += 1
                                                        gun_list.append([x_coord-5,y_coord+21, 0])
                                                        get_gun_movement()
                                        if gun_color == "green":
                                                if x_cross >= 550 and 100 <= y_cross <= 658 and direction == 2:
                                                        gunshot.play()
                                                        gun_count = 20
                                                        gun_count += 1
                                                        gun_list.append([x_coord+44,y_coord+21, 0])
                                                        get_gun_movement()
                                                if x_cross <= 470 and 100 <= y_cross <= 658 and direction == 1:
                                                        gunshot.play()
                                                        gun_count = 20
                                                        gun_count += 1
                                                        gun_list.append([x_coord-5,y_coord+21, 0])
                                                        get_gun_movement()
                
                if event.type == pygame.JOYBUTTONDOWN:
                        print("BUTTONS")
                        if my_joystick.get_button(0):
                                if(on_ground == True):
                                        y_speed=-20
                
                                
                if event.type == pygame.KEYUP:
                        if event.key == pygame.K_a and x_speed < 0:
                                a_press = False
                                move_left = False
                        if event.key == pygame.K_d and x_speed > 0:
                                d_press = False
                                move_right = False
                        if event.key == pygame.K_f:
                            press_key_f = False
                        if event.key == pygame.K_LSHIFT:
                            lshift_press = False
                            shift_run = False
                        if event.key == pygame.K_w:
                            if at_ladder == True:
                                y_speed = 0
                        if event.key == pygame.K_s:
                            if at_ladder == True:
                                y_speed = 0

        if joystick_count != 0:
                
                # This gets the position of the axis on the game controller
                # It returns a number between -1.0 and +1.0
                horiz_axis_pos= my_joystick.get_axis(0)
                #NOT USING:vert_axis_pos= my_joystick.get_axis(1)   
                # Move x according to the axis. We multiply by 10 to speed up the movement.
                if horiz_axis_pos < -0.1:
                        direction = 1
                        x_speed=-10
                if 0.1 > horiz_axis_pos > -0.1:
                        switch_running = 0
                        x_speed=0
                if horiz_axis_pos > 0.1:
                        direction = 2
                        x_speed=10

        use_water = False
        in_deep_water = False

        #make the speed stuff
        if move_right == True and closing_screen == False and loading_screen == False:
            x_speed = 5
        elif move_left == True and closing_screen == False and loading_screen == False:
            x_speed = -5
        else:
            x_speed = 0

        if shift_run == True:
            x_speed = x_speed * 2

        if a_press == True:
                move_left = True
                move_right = False
        elif d_press == True:
                move_left = False
                move_right = True
        else:
                move_left = False
                move_right = False

        if lshift_press == True:
                shift_run = True
        else:
                shift_run = False
                        


        for i in range(len(water_grounds)):
            if water_grounds[i][0] + 10 + 50 >= x_coord >= water_grounds[i][0] +10 - 50:
                if water_grounds[i][1] + 50 >= y_coord >= water_grounds[i][1] - 50:
                    if water_collide(water_grounds[i][0],water_grounds[i][1]):
                        water_x = x_speed / 4
                        water_y = y_speed / 2.5
                        use_water = True
                        in_water = True
                        in_deep_water = True
                        
        for i in range(len(water)):
            if water[i][0] + 10 + 50 >= x_coord >= water[i][0] +10 - 50:
                if water[i][1] + 50 >= y_coord >= water[i][1] - 50:
                    if water_collide(water[i][0],water[i][1]):
                        water_x = x_speed / 4
                        water_y = y_speed / 2.5
                        use_water = True
                        in_water = True

        for i in range(len(quicksand)):
                if quicksand[i][0] + 10 + 50 >= x_coord >= quicksand[i][0] +10 - 50:
                        if quicksand[i][1] + 50 >= y_coord >= quicksand[i][1] - 50:
                                if water_collide(quicksand[i][0],quicksand[i][1]):
                                      water_x = x_speed / 4
                                      water_y = y_speed
                                      use_water = True

        if use_water == True:
            scroll(water_x,water_y)
            scroll_mg(water_x,water_y)
            scroll_enemies(water_x, water_y)
        else:
            scroll(x_speed, y_speed)
            scroll_mg(x_speed, y_speed)
            scroll_enemies(x_speed, y_speed)

        #tracks screen via player (where with no scrolling)
        x_screen += x_speed
        y_screen += y_speed

        pos = pygame.mouse.get_pos()
        x_cross=pos[0]
        y_cross=pos[1]

        player_rect = pygame.Rect(x_coord,y_coord,38,50)
        found = False

        if on_ground == True :
                if x_speed > 0 or x_speed < 0:
                #left collision
                        for i in range(len(level_side_right)):
                                if level_side_right[i][0] + 10 + 50 >= x_coord >= level_side_right[i][0] +10 - 50:
                                        if level_side_right[i][1] + 50 >= y_coord >= level_side_right[i][1] - 50:
                                                if side_check(level_side_right[i][0],level_side_right[i][1]):
                                                        scroll_x = level_side_right[i][0] +2
                                                        return_x = scroll_x - x_coord
                                                        scroll(return_x,return_y)
                                                        scroll_mg(return_x,return_y)
                                                        scroll_enemies(return_x, return_y)
                                                        x_screen += return_x
                                                        return_x = 0
                        #right collsiion
                        for i in range(len(level_side_left)):
                                if level_side_left[i][0] + 10 + 50 >= x_coord >= level_side_left[i][0] +10 - 50:
                                        if level_side_left[i][1] + 50 >= y_coord >= level_side_left[i][1] - 50:
                                                if side_check(level_side_left[i][0],level_side_left[i][1]):
                                                        scroll_x = level_side_left[i][0] -38
                                                        return_x = scroll_x - x_coord
                                                        scroll(return_x,return_y)
                                                        scroll_mg(return_x,return_y)
                                                        scroll_enemies(return_x, return_y)
                                                        x_screen += return_x
                                                        return_x = 0
        
        #top
        for i in range(len(level_top)):
                if level_top[i][0] + 10 + 50 >= x_coord >= level_top[i][0] +10 - 50:
                        if level_top[i][1] + 50 >= y_coord >= level_top[i][1] - 50:
                                if top_check(level_top[i][0],level_top[i][1]):
                                        on_ground = True
                                        scroll_y = level_top[i][1] - 49
                                        y_speed = scroll_y - y_coord
                                        scroll(return_x,y_speed)
                                        scroll_mg(return_x,y_speed)
                                        scroll_enemies(return_x, y_speed)
                                        y_screen += y_speed
                                        y_speed = 0
                                        found = True

        on_a_bridge = False
        if y_speed >= 0:
                if time_trial == True or switch_count == 0:
                  if bridge_count >= 4 or on_bridge == True:
                    for i in range(len(level_top_bridges)):
                        if level_top_bridges[i][0] + 10 + 50 >= x_coord >= level_top_bridges[i][0] +10 - 50:
                                if on_bridge == True:
                                        z = 3
                                else:
                                        z = 50
                                if level_top_bridges[i][1] + z >= y_coord + 50 >= level_top_bridges[i][1] - z:
                                        if top_check(level_top_bridges[i][0],level_top_bridges[i][1]):
                                                on_ground = True
                                                on_a_bridge = True
                                                on_bridge = True
                                                bridge_count= 0
                                                scroll_y = level_top_bridges[i][1] - 49
                                                y_speed = scroll_y - y_coord
                                                scroll(return_x,y_speed)
                                                scroll_mg(return_x,y_speed)
                                                scroll_enemies(return_x, y_speed)
                                                y_screen += y_speed
                                                y_speed = 0
                                                found = True

        if on_a_bridge == False:
                on_bridge = False
                bridge_count += 1

#x,y,resety,stepped on,makeitfall,gravity,offscreen, reset
                                #falling_blocks.append([x*32,y*32,y*32,0,0,0,0,0]
        for i in range(len(falling_blocks)):
                if falling_blocks[i][6] == 0 and falling_blocks[i][4] <= 29:
                   if falling_blocks[i][0] + 10 + 50 >= x_coord >= falling_blocks[i][0] +10 - 50:
                        if falling_blocks[i][1] + 50 >= y_coord >= falling_blocks[i][1] - 50:
                                if top_check(falling_blocks[i][0],falling_blocks[i][1]):
                                        on_ground = True
                                        scroll_y = falling_blocks[i][1] - 49
                                        y_speed = scroll_y - y_coord
                                        scroll(return_x,y_speed)
                                        scroll_mg(return_x,y_speed)
                                        scroll_enemies(return_x, y_speed)
                                        y_screen += y_speed
                                        y_speed = 0
                                        found = True
                                        falling_blocks[i][3] = 1
                                if bottom_check(falling_blocks[i][0]+10,falling_blocks[i][1]+15):
                                        scroll_y = falling_blocks[i][1] +17
                                        y_speed = scroll_y - y_coord
                                        scroll(return_x,y_speed)
                                        scroll_mg(return_x,y_speed)
                                        scroll_enemies(return_x, y_speed)
                                        y_screen += y_speed
                                        y_speed = 0
                if falling_blocks[i][3] == 1:
                        if falling_blocks[i][4] <= 29:
                                falling_blocks[i][4] += 1
                        else:
                                if falling_blocks[i][6] == 0:
                                        falling_blocks[i][5] += 2
                                        falling_blocks[i][1] += falling_blocks[i][5]
                        if falling_blocks[i][1] >= 768 and falling_blocks[i][6] == 0:
                                falling_blocks[i][6] = 1
                        if falling_blocks[i][6] == 1:
                                falling_blocks[i][7] += 1
                                if falling_blocks[i][7] >= 120:
                                        falling_blocks[i][1] = falling_blocks[i][2]
                                        falling_blocks[i][3] = 0
                                        falling_blocks[i][4] = 0
                                        falling_blocks[i][5] = 0
                                        falling_blocks[i][6] = 0
                                        falling_blocks[i][7] = 0
                                
        in_quicksand = False
        for i in range(len(quicksand)):
                if quicksand[i][0] + 10 + 50 >= x_coord >= quicksand[i][0] +10 - 50:
                        if quicksand[i][1] + 50 >= y_coord >= quicksand[i][1] - 50:
                                if water_collide(quicksand[i][0],quicksand[i][1]):
                                        on_ground = True
                                        y_speed = 1
                                        found = True
                                        in_quicksand = True
                quicksand[i][2] += 1
                if quicksand[i][2] >= 5:
                        quicksand[i][3] += 1
                        quicksand[i][2] = 0
                        if quicksand[i][3] >= 5:
                                quicksand[i][3] = 1
                        
        #bottom
        for i in range(len(level_bottom)):
            if level_bottom[i][0] + 10 + 50 >= x_coord >= level_bottom[i][0] +10 - 50:
                        if level_bottom[i][1] + 50 >= y_coord >= level_bottom[i][1] - 50:
                            if bottom_check(level_bottom[i][0],level_bottom[i][1]):
                                scroll_y = level_bottom[i][1] +2
                                y_speed = scroll_y - y_coord
                                scroll(return_x,y_speed)
                                scroll_mg(return_x,y_speed)
                                scroll_enemies(return_x, y_speed)
                                y_screen += y_speed
                                y_speed = 0

        if not found:
                on_ground = False
                ground_count = 0

        if found == True:
                ground_count += 1

        if ground_count == 1:
                        for i in range(len(level_side_right)):
                                if level_side_right[i][0] + 10 + 50 >= x_coord >= level_side_right[i][0] +10 - 50:
                                        if level_side_right[i][1] + 50 >= y_coord >= level_side_right[i][1] - 50:
                                                if side_check(level_side_right[i][0],level_side_right[i][1]):
                                                        scroll_x = level_side_right[i][0] +2
                                                        return_x = scroll_x - x_coord
                                                        scroll(return_x,return_y)
                                                        scroll_mg(return_x,return_y)
                                                        scroll_enemies(return_x, return_y)
                                                        x_screen += return_x
                                                        return_x = 0
                        #right collsiion
                        for i in range(len(level_side_left)):
                                if level_side_left[i][0] + 10 + 50 >= x_coord >= level_side_left[i][0] +10 - 50:
                                        if level_side_left[i][1] + 50 >= y_coord >= level_side_left[i][1] - 50:
                                                if side_check(level_side_left[i][0],level_side_left[i][1]):
                                                        scroll_x = level_side_left[i][0] -38
                                                        return_x = scroll_x - x_coord
                                                        scroll(return_x,return_y)
                                                        scroll_mg(return_x,return_y)
                                                        scroll_enemies(return_x, return_y)
                                                        x_screen += return_x
                                                        return_x = 0
                        
        if on_ground == False and on_ladder == False:
                if in_water:
                    y_speed += gravity / 3
                    in_water = False
                else:
                    y_speed += gravity

        if on_ground == False:

        #left collision
            for i in range(len(level_side_right)):
                    if level_side_right[i][0] + 10 + 50 >= x_coord >= level_side_right[i][0] +10 - 50:
                            if level_side_right[i][1] + 50 >= y_coord >= level_side_right[i][1] - 50:
                                    if side_check(level_side_right[i][0],level_side_right[i][1]):
                                            scroll_x = level_side_right[i][0] +2
                                            return_x = scroll_x - x_coord
                                            scroll(return_x,return_y)
                                            scroll_mg(return_x,return_y)
                                            scroll_enemies(return_x, return_y)
                                            x_screen += return_x
                                            return_x = 0
        #right collision
            for i in range(len(level_side_left)):
                    if level_side_left[i][0] + 10 + 50 >= x_coord >= level_side_left[i][0] +10 - 50:
                            if level_side_left[i][1] + 50 >= y_coord >= level_side_left[i][1] - 50:
                                    if side_check(level_side_left[i][0],level_side_left[i][1]):
                                            scroll_x = level_side_left[i][0] -38
                                            return_x = scroll_x - x_coord
                                            scroll(return_x,return_y)
                                            scroll_mg(return_x,return_y)
                                            scroll_enemies(return_x, return_y)
                                            x_screen += return_x
                                            return_x = 0

        change_level = False
        got_to_level = ""
        #doors!
        for i in range(len(next_level)):
            if door_check(next_level[i][0], next_level[i][1]):
                change_level = True
                go_to_level = str(level_doors[i])
        
        #door animation
        door_change += 1
        if door_change >= 10:
                for i in range(len(next_level)):
                        if next_level[i][2] == 2:
                                next_level[i][2] = 1
                        else:
                                next_level[i][2] = 2
                        door_change = 0

        #COLLECTIBLE ITEMS
        collectibles_remove = []
        for i in range(len(collectibles)):
                if collectibles[i][0] + 10 + 50 >= x_coord >=collectibles[i][0] +10 - 50:
                             if collectibles[i][1] + 50 >= y_coord >= collectibles[i][1] - 50:
                                     if collide_collectible(collectibles[i][0],collectibles[i][1]):
                                             collectibles_remove.append(i)
        for i in range(len(collectibles_remove)):
                j = collectibles_remove[i]
                collectibles.remove(collectibles[j])
                collectible_count += 1
                health = 20

        for i in range(len(gun_color_changer)):
                if gun_color_changer[i][0] + 10 + 50 >= x_coord >= gun_color_changer[i][0] +10 - 50:
                        if gun_color_changer[i][1] + 50 >= y_coord >= gun_color_changer[i][1] - 50:
                                if gun_color_changer[i][2] == 0:
                                        gun_color = "red"
                                elif gun_color_changer[i][2] == 1:
                                        gun_color = "blue"
                                elif gun_color_changer[i][2] == 3:
                                        gun_color = "none"
                                else:
                                        gun_color = "green"
                gun_color_changer[i][3] += 1
                if gun_color_changer[i][3] >= 10:
                        gun_color_changer[i][3] = 0
                        if gun_color_changer[i][4] == 0:
                                gun_color_changer[i][4] == 7
                        else:
                                gun_color_changer[i][4] == 0
                
        #gun

        gun_collide_list = []
        gun_list_remove = []
        gun_collide_remove = []
        for i in range(len(gun_list)):
                to_make_gun_collide = []
                gun_collidex = gun_speed[i][0] / 10
                gun_collidey = gun_speed[i][1] / 10
                for j in range(9):
                        to_make_gun_collide.append(gun_list[i][0] + gun_collidex*(j+1) - 2*gun_speed[i][0])
                        to_make_gun_collide.append(gun_list[i][1] + gun_collidey*(j+1) - 2*gun_speed[i][1])
                gun_collide_list.append(to_make_gun_collide)
        

        gun_movement()

               #SWITCHES
        change_switch_list = []
        gun_collide_remove = []
        if time_trial == False:
           for i in range(len(switch)):
             if switch[i][3] == 1:
                z = i
                change_switch = False
                for j in range(len(gun_list)):
                     for k in range(9):
                             if gun_collide_list[j][k*2] >= switch[i][0] >= gun_collide_list[j][k*2] - 32 and gun_collide_list[j][k*2+1] >= switch[i][1] >= gun_collide_list[j][k*2+1] - 32:
                                         change_switch = True
                                         l = j
                if change_switch == True:
                        change_switch_list.append(z)
                        gun_list.remove(gun_list[l])
                        gun_speed.remove(gun_speed[l])
                        gun_collide_remove.append(l)
             elif switch[i][3] == 2 and switch[i][2] == 1:
                     z = i
                     change_switch = False
                     if switch[i][0] + 10 + 50 >= x_coord >= switch[i][0] +10 - 50:
                             if switch[i][1] + 50 >= y_coord >= switch[i][1] - 50:
                                     if collide_switch(switch[i][0],switch[i][1]):
                                             change_switch = True
                     if change_switch == True:
                             change_switch_list.append(z)                                     
           for i in range(len(gun_collide_remove)):
                 z = gun_collide_remove[i]
                 z -= i
                 gun_collide_list.remove(gun_collide_list[z])
           for i in range(len(change_switch_list)):
                j = change_switch_list[i]
                if switch[j][2] == 1:
                        switch[j][2] = 2
                        switch_press_count += 1
                else:
                        switch[j][2] = 1
                        switch_press_count -= 1
                        
        if switch_count == 0:
                time_trial = False
        elif switch_press_count == switch_count / 2:
                time_trial = True
        else:
                time_trial = False

        if time_trial == True:
                time[0] -= 1
                for i in range(len(switch)):
                        switch[i][2] = 2

        if time[0] < 1:
                time_trial = False
                switch_press_count = 0
                for i in range(len(switch)):
                        switch[i][2] = 1
                time[0] = time[1]

        #draw the time bar countdown
        if time_trial == True:
                time_bar_percent = time[0]/time[1]
                time_bar_green_length = time_bar_green_length_reset * time_bar_percent  

        #enemy stuff
        enemy_crawler_dieing = []
        #x coord, y coord, alive(1) or dead(2), direction(left 1)(right 2), walking or not, run change, kill enemy counter, death animation sprite]
        for i in range(len(enemy_crawler)):
                              #if they are alive
                if enemy_crawler[i][2] == 1:
                        if enemy_crawler[i][3] == 2:
                              #make them move
                              enemy_crawler[i][0] += 3
                        else:
                              enemy_crawler[i][0] -= 3
                              #change the running anim
                        enemy_crawler[i][5] += 1
                        if enemy_crawler[i][5] >= 10:
                                if enemy_crawler[i][4] == 2:
                                        enemy_crawler[i][4] = 1
                                else:
                                        enemy_crawler[i][4] = 2
                                enemy_crawler[i][5] = 0

                        #GUN WITH CRAWLER: REVERSE DIRECTION
                        for j in range(len(gun_collide_list)):
                                if gun_list[j][2] == 0:
                                        z = j
                                        for k in range(9):
                                                if gun_collide_list[j][k*2] >= enemy_crawler[i][0] >= gun_collide_list[j][k*2] - 74 and gun_collide_list[j][k*2+1] + 5 >= enemy_crawler[i][1] + 32 >= gun_collide_list[j][k*2+1] - 42:
                                                        crawler_reverse = True
                                                        gun_list[j][2] = 1
                                if crawler_reverse == True:
                                        if gun_speed[z][1] >= 3 or gun_speed[z][1] <= -3:
                                                gun_speed[z][1] = -gun_speed[z][1]
                                        else:
                                                gun_speed[z][0] = -gun_speed[z][0]
                                        crawler_reverse = False
                                                
                                        
                        
                        #collision with a range block
                        for j in range(len(enemy_crawler_range)):
                                if enemy_crawler_range[j][0] + 20 + 50 >= enemy_crawler[i][0] >= enemy_crawler_range[j][0] - 70:
                                        if enemy_crawler_range[j][1] + 70 >= enemy_crawler[i][1] >= enemy_crawler_range[j][1] - 70:
                                                if crawler_switch_directions(enemy_crawler[i][0],enemy_crawler[i][1],enemy_crawler_range[j][0],enemy_crawler_range[j][1]):
                                                        if enemy_crawler[i][3] == 2:
                                                                enemy_crawler[i][3] = 1
                                                        else:
                                                                enemy_crawler[i][3] = 2
                        #collision with player
                        if enemy_crawler[i][0] + 20 + 50 >= x_coord >= enemy_crawler[i][0] - 30:
                                if enemy_crawler[i][1] + 50 >= y_coord >= enemy_crawler[i][1] - 50:
                                        if crawler_collide(enemy_crawler[i][0],enemy_crawler[i][1]):
                                                if change_knockback == False and no_knockback < 20:
                                                        if on_ground == True:
                                                                health -= 1
                                                                if direction == 1:
                                                                        enemy_crawler[i][3] = 1
                                                                        change_knockback = True
                                                                        knockback_left = False
                                                                        knockback_right = True
                                                                        no_knockback = 0
                                                                        shift_run = True
                                                                elif direction == 2:
                                                                        enemy_crawler[i][3] = 2
                                                                        change_knockback = True
                                                                        no_knockback = 0
                                                                        knockback_right = False
                                                                        knockback_left = True
                                                                        shift_run = True
                                                               
                                                        elif y_speed >= 0:
                                                                y_speed = -20
                                                                enemy_crawler[i][2] = 2
                                                                enemy_crawler[i][7] = 1
                                                                
                elif enemy_crawler[i][2] == 2:
                        enemy_crawler[i][6] += 1
                        enemy_crawler_dieing.append(i)

        for i in range(len(gun_list)):
                if gun_list[i][2] >= 1:
                        gun_list[i][2] += 1
                        if gun_list[i][2] >= 20 - gun_speed[i][1] and gun_list[i][2] >= 20 - gun_speed[i][0]:
                                gun_list[i][2] = 0


                            
                        
        for i in range(len(enemy_crawler_dieing)):
                z = enemy_crawler_dieing[i]
                if change_crawler_die_list == True:
                        z -= 1
                        change_crawler_die_list = False
                if enemy_crawler[z][7] >= 8:
                        enemy_crawler[z][6] = 13
                if enemy_crawler[z][6] >= 10:
                        #print(enemy_crawler[z][7])
                        enemy_crawler[z][7] += 2
                        enemy_crawler[z][6] = 0
                        if enemy_crawler[z][7] >= 8:
                                enemy_crawler[z][1] = enemy_crawler[z][1] + enemy_crawler[z][7] - 6
                                #print(enemy_crawler[z][1])
                                if enemy_crawler[z][1] >= 768 or enemy_crawler[i][0] <= -64 or enemy_crawler[i][0] >= 1025:
                                        enemy_crawler.remove(enemy_crawler[z])
                                        #print(enemy_crawler)
                                        change_crawler_die_list = True

                #x, y, yreset, isitmoving, the speed,, hits range, to reset the stalactite
        #stalactites.append([x*32,y*32,y*32, 0, 0, 0, 0])
        for i in range(len(stalactites)):
                if stalactites[i][3] == 0 and stalactites[i][5] == 0:
                        if stalactites[i][0] + 30 >= x_coord >= stalactites[i][0] - 30:
                                if stalactites[i][1] <= y_coord <= stalactites[i][1] + 300:
                                        stalactites[i][3] = 1
                elif stalactites[i][3] == 1 and stalactites[i][5] == 0:
                        if stalactites[i][0] + 20 + 50 >= x_coord >= stalactites[i][0] - 30:
                                if stalactites[i][1] + 50 >= y_coord >= stalactites[i][1] - 50:
                                        if stalactite_collide(stalactites[i][0],stalactites[i][1]):
                                                if change_knockback == False and no_knockback < 20:
                                                        health -= 1
                                                        if direction == 1:
                                                                change_knockback = True
                                                                no_knockback = 0
                                                                knockback_right = True
                                                                knockback_left = False
                                                                shift_run = True
                                                        elif direction == 2:
                                                                change_knockback = True
                                                                no_knockback = 0
                                                                knockback_right = False
                                                                knockback_left = True
                                                                shift_run = True
                        stalactites[i][4] += 1
                        stalactites[i][1] += stalactites[i][4]
                        for j in range(len(stalactites_range)):
                                if stalactites[i][1]+ 64 >= stalactites_range[j][1] >= stalactites[i][1] - 64:
                                        if stalactite_range_collide(stalactites[i][0],stalactites[i][1],stalactites_range[j][0],stalactites[j][1]):
                                                stalactites[i][5] = 1
                                                stalactites[i][4] = 0
                                                stalactites[i][3] = 0
                elif stalactites[i][5] == 1:
                        stalactites[i][6] += 1
                        if stalactites[i][6] >= 120:
                                stalactites[i][6] = 0
                                stalactites[i][5] = 0
                                stalactites[i][1] = stalactites[i][2]

                
                                        
        #puffpuffs
        enemy_puffpuff_dieing = []
        gun_collide_remove = []
        #x coord, y coord, alive(1) or dead(2), direction(left 1)(right 2), walking or not,
                                #run change, which run to go to next,
                                #kill enemy counter, jumping, jumping stop point, jumping speed,
                                #what type of puffpuff eg forest snow desert]for i in range(len(enemy_puffpuff)):
        #if they are alive
        for i in range(len(enemy_puffpuff)):
                if enemy_puffpuff[i][2] == 1:
                        if enemy_puffpuff[i][3] == 2:
                              #make them move
                              enemy_puffpuff[i][0] += 5
                        else:
                              enemy_puffpuff[i][0] -= 5
                              #change the running anim
                        enemy_puffpuff[i][5] += 1
                        if enemy_puffpuff[i][5] >= 10:
                                if enemy_puffpuff[i][4] == 2:
                                        if enemy_puffpuff[i][6] == 3:
                                                enemy_puffpuff[i][4] = 1
                                        else:
                                                enemy_puffpuff[i][4] == 3
                                elif enemy_puffpuff[i][4] == 1:
                                        enemy_puffpuff[i][4] = 2
                                        enemy_puffpuff[i][6] = 1
                                elif enemy_puffpuff[i][4] == 3:
                                        enemy_puffpuff[i][4] = 2
                                        enemy_puffpuff[i][6] = 3
                                enemy_puffpuff[i][5] = 0

                        gun_collide_remove = []

                        #GUN WITH PUFFPUFF: DIE
                        for j in range(len(gun_collide_list)):
                                z = j
                                if gun_remove == True:
                                        z -= 1
                                        gun_remove = False
                                for k in range(9):
                                        if gun_collide_list[j][k*2] >= enemy_puffpuff[i][0] >= gun_collide_list[j][k*2] - 74 and gun_collide_list[j][k*2+1] + 5 >= enemy_puffpuff[i][1] + 32 >= gun_collide_list[j][k*2+1] - 42:
                                                gun_remove = True
                                if gun_remove == True:
                                        enemy_puffpuff_health[i] -= 1
                                        if enemy_puffpuff_health[i] <= 0:
                                                enemy_puffpuff[i][2] = 2
                                        gun_list.remove(gun_list[z])
                                        gun_speed.remove(gun_speed[z])
                                        gun_collide_remove.append(j)
                        for j in range(len(gun_collide_remove)):
                                z = gun_collide_remove[j]
                                z -= j
                                gun_collide_list.remove(gun_collide_list[z])
                        #collision with a range block
                        for j in range(len(enemy_puffpuff_range)):
                                if enemy_puffpuff_range[j][0] + 20 + 50 >= enemy_puffpuff[i][0] >= enemy_puffpuff_range[j][0] - 70:
                                        if enemy_puffpuff_range[j][1] + 400 >= enemy_puffpuff[i][1] >= enemy_puffpuff_range[j][1] - 200:
                                                if puffpuff_switch_directions(enemy_puffpuff[i][0],enemy_puffpuff[i][1],enemy_puffpuff_range[j][0],enemy_puffpuff_range[j][1]):
                                                        if enemy_puffpuff[i][3] == 2:
                                                                enemy_puffpuff[i][3] = 1
                                                        else:
                                                                enemy_puffpuff[i][3] = 2
                                                                
                        if enemy_puffpuff[i][8] == 0:
                                if enemy_puffpuff[i][0] + 250 >= x_coord >= enemy_puffpuff[i][0] - 250:
                                        if enemy_puffpuff[i][1] + 100 >= y_coord >= enemy_puffpuff[i][1] - 100:
                                        #x coord, y coord, alive(1) or dead(2), direction(left 1)(right 2), walking or not,
                                #run change, which run to go to next,
                                #kill enemy counter, jumping, jumping stop point, jumping speed,
                                #what type of puffpuff eg forest snow desert]
                                                z = random.randrange(1,4)
                                                if z == 1:
                                                        enemy_puffpuff[i][10] = -10
                                                if z == 2:
                                                        enemy_puffpuff[i][10] = -13
                                                if z == 3:
                                                        enemy_puffpuff[i][10] = -7
                                                enemy_puffpuff[i][8] = 2
                                                if enemy_puffpuff[i][0] > x_coord:
                                                        enemy_puffpuff[i][3] = 1
                                                elif enemy_puffpuff[i][0] < x_coord:
                                                        enemy_puffpuff[i][3] = 2


                        if enemy_puffpuff[i][8] == 2:
                                enemy_puffpuff[i][1] += enemy_puffpuff[i][10]
                                enemy_puffpuff[i][10] += 0.5
                                if enemy_puffpuff[i][1] >= enemy_puffpuff[i][9]:
                                        enemy_puffpuff[i][1] = enemy_puffpuff[i][9]
                                        enemy_puffpuff[i][10] = 0
                                        enemy_puffpuff[i][8] = 0
                                        
                        #collision with player
                        if enemy_puffpuff[i][0] + 20 + 50 >= x_coord >= enemy_puffpuff[i][0] - 30:
                                if enemy_puffpuff[i][1] + 50 >= y_coord >= enemy_puffpuff[i][1] - 50:
                                        if puffpuff_collide(enemy_puffpuff[i][0],enemy_puffpuff[i][1]):
                                                if change_knockback == False and no_knockback < 20:
                                                        if on_ground == True or y_speed <= 0:
                                                                health -= 1
                                                                if direction == 1:
                                                                        change_knockback = True
                                                                        no_knockback = 0
                                                                        knockback_right = True
                                                                        knockback_left = False
                                                                        shift_run = True
                                                                elif direction == 2:
                                                                        change_knockback = True
                                                                        no_knockback = 0
                                                                        knockback_right = False
                                                                        knockback_left = True
                                                                        shift_run = True
                                                                
                elif enemy_puffpuff[i][2] == 2:
                        enemy_puffpuff[i][7] += 2
                        enemy_puffpuff_dieing.append(i)
                        
        for i in range(len(enemy_puffpuff_dieing)):
                z = enemy_puffpuff_dieing[i]
                if change_puffpuff_die_list == True:
                        z -= 1
                        change_puffpuff_die_list = False
                enemy_puffpuff[z][1] += enemy_puffpuff[z][7]
                if enemy_puffpuff[z][1] >= 768 or enemy_puffpuff[i][0] <= -64 or enemy_puffpuff[i][0] >= 1025:
                        enemy_puffpuff.remove(enemy_puffpuff[z])
                        enemy_puffpuff_health.remove(enemy_puffpuff_health[z])
                        #print(enemy_crawler)
                        change_puffpuff_die_list = True

        #FLYING ENEMIES!!!!
        #x coord, y coord, alive(1) or dead(2), direction(left/down 1)(right/up 2), 
                                #wing up/down, fly change, kill enemy counter, death animation sprite,
                                #what type of crawler eg forest wno desert, vertical/horizontal, drawing stuff]
                               # z = random.randrange(1,3)
                               # enemy_flying.append([x*32,y*32 - 32, 1, z, 1, 0, 0, 0, 1, 1''' this is horizontal''', 1])

        enemy_flying_dieing = []
        for i in range(len(enemy_flying)):
                              #if they are alive
                if enemy_flying[i][2] == 1:
                        if enemy_flying[i][3] == 2:
                                if enemy_flying[i][9] == 1:
                              #make them move
                                      enemy_flying[i][0] += 3
                                else:
                                        enemy_flying[i][1] += 3
                        else:
                              if enemy_flying[i][9] == 1:
                              #make them move
                                      enemy_flying[i][0] -= 3
                              else:
                                        enemy_flying[i][1] -= 3
                              #change the running anim
                        enemy_flying[i][5] += 1
                        if enemy_flying[i][5] >= 10:
                                if enemy_flying[i][4] == 2:
                                        enemy_flying[i][4] = 1
                                else:
                                        enemy_flying[i][4] = 2
                                enemy_flying[i][5] = 0

                        gun_collide_remove = []

                        #GUN WITH flying: REVERSE DIRECTION
                        for j in range(len(gun_collide_list)):
                                z = j
                                if gun_remove == True:
                                        z -= 1
                                        gun_remove = False
                                for k in range(9):
                                        if gun_collide_list[j][k*2] >= enemy_flying[i][0] >= gun_collide_list[j][k*2] - 32 and gun_collide_list[j][k*2+1] + 5 >= enemy_flying[i][1] >= gun_collide_list[j][k*2+1] - 42:
                                                gun_remove = True
                                if gun_remove == True:
                                        enemy_flying_health[i] -= 1
                                        if enemy_flying_health[i] <= 0:
                                                enemy_flying[i][2] = 2
                                        gun_list.remove(gun_list[z])
                                        gun_speed.remove(gun_speed[z])
                                        gun_collide_remove.append(j)
                        for j in range(len(gun_collide_remove)):
                                z = gun_collide_remove[j]
                                z -= j
                                gun_collide_list.remove(gun_collide_list[z])
                                                
                                        
                        
                        #collision with a range block
                        for j in range(len(enemy_flying_range)):
                                if enemy_flying_range[j][0] + 20 + 50 >= enemy_flying[i][0] >= enemy_flying_range[j][0] - 70:
                                        if enemy_flying_range[j][1] + 70 >= enemy_flying[i][1] >= enemy_flying_range[j][1] - 70:
                                                if flying_switch_directions(enemy_flying[i][0],enemy_flying[i][1],enemy_flying_range[j][0],enemy_flying_range[j][1]):
                                                        if enemy_flying[i][3] == 2:
                                                                enemy_flying[i][3] = 1
                                                        else:
                                                                enemy_flying[i][3] = 2
                        #collision with player
                        if enemy_flying[i][0] + 20 + 50 >= x_coord >= enemy_flying[i][0] - 30:
                                if enemy_flying[i][1] + 50 >= y_coord >= enemy_flying[i][1] - 50:
                                        if flying_collide(enemy_flying[i][0],enemy_flying[i][1]):
                                                if change_knockback == False and no_knockback < 20:
                                                                health -= 1
                                                                if direction == 1:
                                                                        enemy_flying[i][3] = 1
                                                                        change_knockback = True
                                                                        knockback_left = False
                                                                        knockback_right = True
                                                                        no_knockback = 0
                                                                        shift_run = True
                                                                elif direction == 2:
                                                                        enemy_flying[i][3] = 2
                                                                        change_knockback = True
                                                                        no_knockback = 0
                                                                        knockback_right = False
                                                                        knockback_left = True
                                                                        shift_run = True
                                                                
                elif enemy_flying[i][2] == 2:
                        enemy_flying[i][7] += 2
                        enemy_flying_dieing.append(i)

        for i in range(len(gun_list)):
                if gun_list[i][2] >= 1:
                        gun_list[i][2] += 1
                        if gun_list[i][2] >= 20 - gun_speed[i][1] and gun_list[i][2] >= 20 - gun_speed[i][0]:
                                gun_list[i][2] = 0

                            
                        
        for i in range(len(enemy_flying_dieing)):
                z = enemy_flying_dieing[i]
                if change_flying_die_list == True:
                        z -= 1
                        change_flying_die_list = False
                enemy_flying[z][1] += enemy_flying[z][7]
                if enemy_flying[z][1] >= 768 or enemy_flying[i][0] <= -64 or enemy_flying[i][0] >= 1025:
                        enemy_flying.remove(enemy_flying[z])
                        enemy_flying_health.remove(enemy_flying_health[z])
                        #print(enemy_crawler)
                        change_flying_die_list = True

        if change_knockback == True:
                knockback = True
                no_knockback += 1
                if no_knockback >= 20:
                        knockback = False
                        change_knockback = False
                        no_knockback = 0
                if no_knockback >= 10:
                        knockback = False
                if no_knockback <= 9 and change_knockback == True:
                        if knockback_right == True:
                                d_press = False
                                a_press = False
                                move_right = True
                                move_left = False
                                shift_run = True
                        elif knockback_left == True:
                                d_press = False
                                a_press = False
                                move_left = True
                                move_right = False
                                shift_run = True

        gun_collide_remove = []
   
#see if gun works when it is destroyed down here.
        for i in range(len(gun_list)):
            if gun_list[i][0] >= 1024 or gun_list[i][0] <= 0 or gun_list[i][1] <= 0 or gun_list[i][1] >= 768:
                    gun_list_remove.append(i)
        for i in range(len(gun_list_remove)):
                z = gun_list_remove[i]
                gun_list.remove(gun_list[z])
                gun_speed.remove(gun_speed[z])
                gun_collide_list.remove(gun_collide_list[z])
        for i in range(len(gun_collide_list)):
                z = i
                if gun_remove == True:
                        z -= 1
                        gun_remove = False
                for j in range(9):
                        for k in range(len(level_top)):
                                if gun_collide_list[i][j*2] >= level_top[k][0] >= gun_collide_list[i][j*2] - 32 and gun_collide_list[i][j*2+1] >= level_top[k][1] >= gun_collide_list[i][j*2+1] - 32:
                                        gun_remove = True
                if gun_remove == True:
                        gun_list.remove(gun_list[z])
                        gun_speed.remove(gun_speed[z])
                        '''gun_collide_remove.append(i)
        for j in range(len(gun_collide_remove)):
                z = gun_collide_remove[j]
                z -= j
                gun_collide_list.remove(gun_collide_list[z])'''


        if gun_count > 0:
                gun_count -= 1
                
        talking = False
        #talk to the villagers
        for i in range(len(villager)):
            if villager[i][0] + 20 + 50 >= x_coord >= villager[i][0] - 30:
                if villager[i][1] + 50 >= y_coord >= villager[i][1] - 50:
                    if talk_to_villagers(villager[i][0],villager[i][1]):
                        talking = True
                        villager_number = i
                        if write_text == True:
                            villager[i][3] = 2
                            
            if villager[i][3] == 2:
                if villager[i][0] > x_coord:
                    villager[i][2] = 1
                else:
                    villager[i][2] = 2

        if talking == False:
            write_text = False

        if not x_speed == 0:
            write_text = False


        if write_text == False:
            for i in range(len(villager)):
              if villager[i][8] == 0:
                if -38 <= villager[i][0] <= 1062 and -50 <= villager[i][1] <= 800:
                    if villager[i][5] == 1:
                        villager[i][4] += 1
                        if villager[i][4] >= 50:
                            villager_move = random.randrange(0, 5)
                            if villager_move == 1:
                                villager[i][5] = 2
                            villager[i][4] = 0
                    else:
                        if villager[i][6] == 0:
                            villager[i][2] = random.randrange(0,2)
                        if villager[i][7] >= 21:
                            villager[i][2] = 0
                        if villager[i][7] <= -21:
                            villager[i][2] = 1
                        if villager[i][2] == 1:
                            villager[i][0] -= villager_speed
                            villager[i][6] += 1
                            villager[i][3] = 1
                            villager[i][7] += 1
                        else:
                            villager[i][0] += villager_speed
                            villager[i][6] += 1
                            villager[i][3] = 1
                            villager[i][7] -= 1
                        if villager[i][6] >= 7:
                            villager[i][5] = 1
                            villager[i][4] = 0
                            villager[i][6] = 0      

        #sign stuff
        at_sign = False
            
        for i in range(len(signs)):
            if signs[i][0] + 50 >= x_coord >= signs[i][0] - 30:
                if signs[i][1] + 50 >= y_coord >= signs[i][1] - 50:
                    if read_the_sign(signs[i][0],signs[i][1]):
                        at_sign = True
                        sign_number = i

        if at_sign == False:
            read_sign = False

        if not x_speed == 0:
            read_sign = False

        #ladders
        at_ladder = False
        if time_trial == True or switch_count == 0:
         for i in range(len(ladders)):
            if ladders[i][0] + 50 >= x_coord >= ladders[i][0] - 30:
                if ladders[i][1] + 50 >= y_coord >= ladders[i][1] - 50:
                    if ladder_check(ladders[i][0], ladders[i][1]):
                        at_ladder = True

        if at_ladder == False:
            on_ladder = False

        if on_ladder == False and read_sign == False and write_text == False and closing_screen == False:
            w_press = False

        #for safety
        if y_screen <=-50 or y_screen >= 2100 and closing_screen == False:
                closing_screen = True
                health -= 1
                
        if x_speed > 0 or x_speed < 0:
            if on_ground == True:
                        switch_running += 1
        
        if in_water:
            if switch_running >= 18:
                if running == 1:
                        running = 2
                else:
                        running = 1
                switch_running = 0
        elif shift_run == True:
            if switch_running >= 6:
                if running == 1:
                        running = 2
                else:
                        running = 1
                switch_running = 0
        else:
            if switch_running >= 10:
                if running == 1:
                        running = 2
                else:
                        running = 1
                switch_running = 0
            
                
        
        if x_speed == 0:
            switch_running = 0
    
        if on_ground == False:
            switch_running = 0

        #idle
        if x_speed == 0 and on_ground == True:
                idle_check += 1

        if idle_check >= 30:
                idle_switch += 1

        if idle_switch >= 30:
                if idle == 2:
                        idle = 1
                else:
                        idle =2
                idle_switch = 0

        if on_ground == False:
                idle = 1
                idle_check = 0
                idle_switch = 0

        if x_speed > 0:
                idle = 1
                idle_check = 0
                idle_switch = 0

        if x_speed < 0:
                idle = 1
                idle_check = 0
                idle_switch = 0
                
        if w_press == True:
                idle = 1
                idle_check = 0
                idle_switch = 0

        drowning = False

        if in_deep_water:
            last_breath += 1
            drowning = True
        elif last_breath != 0:
            last_breath = 0
            air_value = 10
        else:
            air_value = 10

        if last_breath > 30:
            if air_value >= 1:
                air_value -= 1
            else:
                health -= 1
            last_breath = 0

            #CHANGE LAVA SPRITES
        for i in range(len(lavas)):
                lavas[i][3] += 1
                if lavas[i][3] >= 20:
                        lavas[i][3] = 0
                        lavas[i][2] += 1
                        if lavas[i][2] >= 6:
                                lavas[i][2] = 1
        for i in range(len(mg_lavas)):
                mg_lavas[i][3] += 1
                if mg_lavas[i][3] >=20:
                        mg_lavas[i][3] = 1
                        mg_lavas[i][2] += 1
                        if mg_lavas[i][2] >= 6:
                                mg_lavas[i][2] = 1

        for i in range(len(collectibles)):
                collectibles[i][3] += 1
                if collectibles[i][2] == 0:
                        if collectibles[i][3] >= 120:
                                collectibles[i][2] += 1
                                collectibles[i][3] = 0
                else:
                        if collectibles[i][3] >= 3:
                                collectibles[i][2] += 1
                                if collectibles[i][2] >= 10:
                                        collectibles[i][2] = 0
                                collectibles[i][3] = 0

        #door screen change
        if loading_screen == True:
                stupid_variable += 1
                pygame.mixer.music.set_volume(0.2)
                if stupid_variable >= 20:
                        loading_fillscreen += 50
                        if loading_fillscreen >= 1200:
                                loading_fillscreen = 0
                                loading_screen = False
                                stupid_variable = 0

        #close screen
        if closing_screen == True:
                loading_closingscreen -= 50
                x_speed = 0
                y_speed = 0
                if loading_closingscreen <= -50:
                        previous_level_music = level_music[0]
                        loading_closingscreen = 1200
                        closing_screen = False
                        loading_screen = True
                        if change_level == True:
                                previous_level = current_level
                                current_level = go_to_level
                                print(current_level)

                        level_info = []
                        background = []
                        middleground = []
                        enemy_levelpng = []
                        level_text = []
                        sign_text = []
                        number_sign = []
                        number_villagers = []
                        level_doors = []
                        level_music = []
                        level_backdrop = []
                        time = []
                        lvlParser(current_level)

                        if previous_level_music == level_music[0]:
                                print("equal")

                        else:
                                pygame.mixer.music.fadeout(2000)
                        
                                load_music(level_music[0] + ".ogg")
                                pygame.mixer.music.set_volume(0)
                                pygame.mixer.music.play(-1,0)

                        weather = level_info[1][0]
                        x_coord = level_info[0][0]
                        y_coord = level_info[0][1]
                                    
                        levelimg = load_level(current_level+".png")
                        mg = load_level(middleground[0]+".png")
                        bg = load_image("backgrounds",background[0]+".png")
                        enemy_level = load_level(enemy_levelpng[0]+".png")
                        backdrop = load_image("backgrounds\\backdrops",level_backdrop[0]+".png")
                        y_screen = y_coord
                        x_screen = x_coord
                        gun_count = 0
                        gun_list = []
                        gun_speed = []
                        houses = []
                        signs = []
                        villager = []
                        next_level = []
                        level_walls_red=[]
                        level_walls_ground=[]
                        level_walls_r_edge = []
                        level_walls_l_edge = []
                        level_walls_d_edge = []
                        level_top=[]
                        level_air=[]
                        level_side_left = []
                        level_side_right = []
                        level_bottom = []
                        water = []
                        water_grounds = []
                        house_floors = []
                        house_ceilings = []
                        house_walls = []
                        ladders = []
                        trees = []
                        bridges = []
                        level_top_bridges = []
                        bridges_left = []
                        bridges_right = []
                        switch = []
                        falling_blocks = []

                        fences = []
                        cactus = []

                        wells = []

                        backdrops = []
                        backdrops.append([-100,0])

                        #NEW LISTS FOR FOREGROUND
                        rocks = []
                        rock_right_corners = []
                        rock_left_corners = []
                        rock_double_corners = []
                        rock_ground = []

                        cave = []
                        cave_right_corners = []
                        cave_left_corners = []
                        cave_double_corners = []
                        cave_ground = []

                        icy = []
                        ice_right_corners = []
                        ice_left_corners = []
                        ice_double_corners = []
                        icy_grounds = []

                        sands = []
                        sand_right_corner = []
                        sand_left_corner = []
                        sand_double_corners = []
                        sand_grounds = []
                        lavas = []

                        brick_grounds = []
                        bricks = []
                        brick_left_corners = []
                        brick_right_corners = []

                        mg_rock_ground = []
                        mg_sand_grounds = []
                        mg_lavas = []
                        mg_brick_grounds = []
                        mg_icy_ground = []
                        mg_cave_ground = []

                        #COLLECTIBLE
                        collectibles = []

                        time_trail = False

                        switch_count = 0
                        switch_press_count = 0

                        enemy_crawler = []
                        enemy_crawler_range = []

                        enemy_flying = []
                        enemy_flying_range = []
                        enemy_flying_health = []

                        enemy_puffpuff = []
                        enemy_puffpuff_range = []
                        enemy_puffpuff_health = []

                        gun_color_changer = []

                        quicksand = []

                        stalactites = []
                        stalactites_range = []

#all lists for background, (put non collidable stuff in here too, e.g. enclosed ground?)
                        house_insides = []
                        mg_ground = []
                                
                        getRGB()
                        getmgRGB()
                        getenemyRGB()

                        for i in range(len(switch)):
                                switch_count += 1

                #try to start on the doors that u came from
                        for i in range(len(level_doors)):
                            if previous_level == level_doors[i]:
                                x_screen = next_level[i][0] - 3
                                y_screen = next_level[i][1] + 13
                                x_speed = x_screen - x_coord
                                y_speed = y_screen - y_coord
                                scroll(x_speed,y_speed)
                                scroll_mg(x_speed,y_speed)
                                scroll_enemies(x_speed, y_speed)
                                x_speed = 0
                                y_speed = 0
                                #Write some save files!
                                print("\n\n"+str(current_level)+"\n"+str(previous_level)+"\n"+str(gun_color)+"\n"+str(health))
                                save_write(save,str(current_level)+"\n"+str(previous_level)+"\n"+str(gun_color)+"\n"+str(health))
                                
            
        screen.blit(bg, (0,0))

        screen.blit(backdrop, (backdrops[0][0], backdrops[0][1]))

        drawmg()

        if time_trial == True or switch_count == 0:
                draw_bridge_ladder()
        
        draw_walls()

        draw_switch()
        
        draw_falling_blocks()

        draw_doors()

        draw_signs()

        draw_villagers()

        draw_crawlers()

        draw_puffpuff()

        draw_flying()

        draw_gun_color_changer()

        draw_player(x_coord, y_coord)

        draw_water()

        draw_quicksand()

        draw_bullets()

        draw_cross(screen,x_cross,y_cross)

        draw_health(health)
        if time_trial == True:
                draw_time_bar(time_bar_x,time_bar_y,time_bar_green_length,time_bar_green_height,time_bar_black_length,time_bar_black_height)

        load_anim(loading_fillscreen)

        close_anim(loading_closingscreen)

        if in_deep_water:
            draw_air(air_value)

        if write_text == True:
            for i in range(number_villagers[0][1]):
                if i == 0:
                    txtEngine(screen, level_text[villager_number * number_villagers[0][1] + i], 1, True)
                else:
                    txtEngine(screen, level_text[villager_number * number_villagers[0][1] + i], i + 1, False)

        if read_sign == True:
            for i in range(number_sign[0][1]):
                if i == 0:
                    txtEngine(screen, sign_text[sign_number * number_sign[0][1] + i], 1, True)
                else:
                    txtEngine(screen, sign_text[sign_number * number_sign[0][1] + i], i + 1, False)
                
        pygame.display.flip()

        clock.tick(60)
pygame.quit()
