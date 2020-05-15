import random
from time import sleep
from colorama import init
from colorama import Fore, Back, Style
import pygame

pygame.init()
init(autoreset=True)

all_scene_types = []

minimum_difficulty = 1

spr_grass = pygame.image.load("sprites/map/grass1.png")
spr_forest = pygame.image.load("sprites/map/forest1.png")
spr_road = pygame.image.load("sprites/map/road1.png")
spr_town = pygame.image.load("sprites/map/town1.png")
spr_dirt1 = pygame.image.load("sprites/map/dirt1.png")
spr_dirt2 = pygame.image.load("sprites/map/dirt2.png")
spr_waterdefault = pygame.image.load("sprites/map/cow1.png")

spr_waterfall = pygame.image.load("sprites/map/waterfall1.png")


spr_cliffs1 = pygame.image.load("sprites/map/cliffs1.png")

spr_river = pygame.image.load("sprites/map/river/river_m.png")

spr_river_bt = pygame.image.load("sprites/map/river/river_bt.png")
spr_river_lr = pygame.image.load("sprites/map/river/river_lr.png")

spr_river_tl = pygame.image.load("sprites/map/river/river_tl.png")
spr_river_tr = pygame.image.load("sprites/map/river/river_tr.png")
spr_river_tlr = pygame.image.load("sprites/map/river/river_tlr.png")


spr_river_bl = pygame.image.load("sprites/map/river/river_bl.png")
spr_river_br = pygame.image.load("sprites/map/river/river_br.png")
spr_river_blr = pygame.image.load("sprites/map/river/river_blr.png")


spr_river_t = pygame.image.load("sprites/map/river/river_t.png")
spr_river_b = pygame.image.load("sprites/map/river/river_b.png")
spr_river_l = pygame.image.load("sprites/map/river/river_l.png")
spr_river_r = pygame.image.load("sprites/map/river/river_r.png")

 ####

spr_road = pygame.image.load("sprites/map/road/road_m.png")

spr_road_bt = pygame.image.load("sprites/map/road/road_bt.png")
spr_road_lr = pygame.image.load("sprites/map/road/road_lr.png")

spr_road_tl = pygame.image.load("sprites/map/road/road_tl.png")
spr_road_tr = pygame.image.load("sprites/map/road/road_tr.png")
spr_road_tlr = pygame.image.load("sprites/map/road/road_tlr.png")


spr_road_bl = pygame.image.load("sprites/map/road/road_bl.png")
spr_road_br = pygame.image.load("sprites/map/road/road_br.png")
spr_road_blr = pygame.image.load("sprites/map/road/road_blr.png")


spr_road_t = pygame.image.load("sprites/map/road/road_t.png")
spr_road_b = pygame.image.load("sprites/map/road/road_b.png")
spr_road_l = pygame.image.load("sprites/map/road/road_l.png")
spr_road_r = pygame.image.load("sprites/map/road/road_r.png")






class scene_type:
    def __init__(self, xpos, ypos, zpos, name, temp, light, safe, can_fish, can_cook, can_craft, can_steal, passable, treasure, difficulty, biome, tile_type, has_tp, indoors, impass_msg, flavour, scene_inventory, scene_weapon_inventory, scene_armor_inventory, scene_helmet_inventory, scene_shield_inventory):
        self.xpos = xpos
        self.ypos = ypos
        self.zpos = zpos
        self.name = name
        self.temp = temp
        self.light = light
        self.safe = safe
        self.can_fish = can_fish
        self.can_cook = can_cook
        self.can_craft = can_craft
        self.can_steal = can_steal
        self.passable = passable
        self.treasure = treasure
        self.difficulty = difficulty
        self.biome = biome
        self.tile_type = tile_type
        self.has_tp = has_tp
        self.indoors = indoors
        self.impass_msg = impass_msg
        self.flavour = flavour
        self.scene_inventory = scene_inventory
        self.scene_weapon_inventory = scene_weapon_inventory
        self.scene_armor_inventory = scene_armor_inventory
        self.scene_helmet_inventory = scene_helmet_inventory
        self.scene_shield_inventory = scene_shield_inventory
        self.tile_sprite = spr_grass

        self.npc_list = []

        self.difficulty += minimum_difficulty

        all_scene_types.append(self)

        self.tile_r = 0
        self.tile_g = 255
        self.tile_b = 229

    def func_generate_sprite_positions(self):

        if self.biome == "seaside":
            self.name = (Fore.CYAN + Style.NORMAL + self.name + Style.RESET_ALL)

        elif self.biome == "water":
            self.name = (Fore.BLUE + Style.NORMAL + self.name + Style.RESET_ALL)
            self.tile_sprite = spr_river

            if self.tile_type == "river":
                self.tile_sprite = spr_river

            if self.tile_type == "waterfall":
                self.tile_sprite = spr_waterfall

            elif self.tile_type == "river_bt":
                self.tile_sprite = spr_river_bt

            elif self.tile_type == "river_lr":
                self.tile_sprite = spr_river_lr

                ########

            elif self.tile_type == "river_tl":
                self.tile_sprite = spr_river_tl

            elif self.tile_type == "river_tr":
                self.tile_sprite = spr_river_tr

            elif self.tile_type == "river_tlr":
                self.tile_sprite = spr_river_tlr

            elif self.tile_type == "river_bl":
                self.tile_sprite = spr_river_bl

            elif self.tile_type == "river_br":
                self.tile_sprite = spr_river_br

            elif self.tile_type == "river_blr":
                self.tile_sprite = spr_river_blr

                ########

            elif self.tile_type == "river_t":
                self.tile_sprite = spr_river_t

            elif self.tile_type == "river_b":
                self.tile_sprite = spr_river_b

            elif self.tile_type == "river_l":
                self.tile_sprite = spr_river_l

            elif self.tile_type == "river_r":
                self.tile_sprite = spr_river_r

        elif self.biome == "forest":
            self.name = (Fore.GREEN + Style.NORMAL + self.name + Style.RESET_ALL)
            self.tile_sprite = spr_forest

        elif self.biome == "town":
            self.name = (Fore.BLACK + Style.BRIGHT + self.name + Style.RESET_ALL)
            self.tile_sprite = spr_town

        elif self.biome == "sandy":
            self.name = (Fore.YELLOW + Style.NORMAL + self.name + Style.RESET_ALL)

        elif self.biome == "grassy":
            self.name = (Fore.GREEN + Style.DIM + self.name + Style.RESET_ALL)
            self.tile_sprite = spr_grass

        elif self.biome == "snow":
            self.name = (Fore.WHITE + Style.BRIGHT + self.name + Style.RESET_ALL)

        elif self.biome == "cave":
            self.name = (Fore.MAGENTA + Style.DIM + self.name + Style.RESET_ALL)
            self.tile_sprite = spr_dirt1

        elif self.biome == "dirt":
            self.name = (Fore.BLACK + Style.BRIGHT + self.name + Style.RESET_ALL)
            self.tile_sprite = spr_dirt1

        elif self.biome == "cliffs":
            self.name = (Fore.BLACK + Style.BRIGHT + self.name + Style.RESET_ALL)
            self.tile_sprite = spr_cliffs1


        elif self.biome == "dirt2":
            self.name = (Fore.BLACK + Style.BRIGHT + self.name + Style.RESET_ALL)
            self.tile_sprite = spr_dirt2

        elif self.biome == "road":
            self.name = (Fore.BLACK + Style.BRIGHT + self.name + Style.RESET_ALL)
            self.tile_sprite = spr_road

            if self.tile_type == "road":
                self.tile_sprite = spr_road


            elif self.tile_type == "road_bt":
                self.tile_sprite = spr_road_bt

            elif self.tile_type == "road_lr":
                self.tile_sprite = spr_road_lr

                ########

            elif self.tile_type == "road_tl":
                self.tile_sprite = spr_road_tl

            elif self.tile_type == "road_tr":
                self.tile_sprite = spr_road_tr

            elif self.tile_type == "road_tlr":
                self.tile_sprite = spr_road_tlr

            elif self.tile_type == "road_bl":
                self.tile_sprite = spr_road_bl

            elif self.tile_type == "road_br":
                self.tile_sprite = spr_road_br

            elif self.tile_type == "road_blr":
                self.tile_sprite = spr_road_blr

                ########

            elif self.tile_type == "road_t":
                self.tile_sprite = spr_road_t

            elif self.tile_type == "road_b":
                self.tile_sprite = spr_road_b

            elif self.tile_type == "road_l":
                self.tile_sprite = spr_road_l

            elif self.tile_type == "road_r":
                self.tile_sprite = spr_road_r

        else:
            self.name = (Fore.RED + Style.DIM + self.name + Style.RESET_ALL)
            self.tile_r = 255
            self.tile_g = 0
            self.tile_b = 0


# dev scenes
dev = scene_type(0,0,-1000,"dev skill test area","","",True,True,True,True,True,True,True,0,"grassy","",False,False,"","rolling green hills",[],[],[],[],[])
dev1 = scene_type(1,0,-1000,"dev skill test area","","",True,True,True,True,True,True,True,0,"grassy","",False,False,"","rolling green hills",[],[],[],[],[])
dev2 = scene_type(0,1,-1000,"dev skill test area","","",True,True,True,True,True,True,True,0,"grassy","",False,False,"","rolling green hills",[],[],[],[],[])
dev3 = scene_type(1,1,-1000,"dev skill test area","","",True,True,True,True,True,True,True,0,"grassy","",False,False,"","rolling green hills",[],[],[],[],[])
dev4 = scene_type(1,2,-1000,"dev skill test area","","",True,True,True,True,True,False,False,0,"grassy","",False,False,"","rolling green hills",[],[],[],[],[])
dev5 = scene_type(2,1,-1000,"dev skill test area","","",True,True,True,True,True,True,False,0,"forest","",False,False,"","rolling green hills",[],[],[],[],[])
dev6 = scene_type(2,2,-1000,"dev skill test area","","",True,True,True,True,True,True,True,0,"grassy","",False,False,"","rolling green hills",[],[],[],[],[])
dev7 = scene_type(3,1,-1000,"dev skill test area","","",True,True,True,True,True,True,True,0,"grassy","",False,False,"","rolling green hills",[],[],[],[],[])

# starting area
start_hills2 = scene_type(0,0,0,"the hills","","",True,False,False,False,False,True,False,0,"grassy","",False,False,"","rolling green hills",[],[],[],[],[])
start_hills3 = scene_type(1,0,0,"the hills","","",True,False,False,False,False,True,False,0,"grassy","",False,False,"","rolling green hills",[],[],[],[],[])

hills = scene_type(1,5,0,"the hills","","",True,False,False,False,False,True,False,0,"grassy","",False,False,"","rolling green hills",[],[],[],[],[])
hills = scene_type(1,4,0,"the hills","","",True,False,False,False,False,True,False,0,"grassy","",False,False,"","rolling green hills",[],[],[],[],[])
hills = scene_type(1,3,0,"the hills","","",True,False,False,False,False,True,False,0,"grassy","",False,False,"","rolling green hills",[],[],[],[],[])
hills = scene_type(1,2,0,"the hills","","",True,False,False,False,False,True,False,0,"grassy","",False,False,"","rolling green hills",[],[],[],[],[])
hills = scene_type(1,1,0,"the hills","","",True,False,False,False,False,True,False,0,"grassy","",False,False,"","rolling green hills",[],[],[],[],[])

lakeside = scene_type(1,6,0,"lakeside","","",True,False,False,False,False,True,False,0,"forest","",False,False,"","the shore of the lake",[],[],[],[],[])

# large tree cave
large_tree = scene_type(2,5,0,"a large hollow tree","","",True,False,False,False,True,True,False,0,"grassy","",True,True,"","a very, very large oak tree",[],[],[],[],[])

large_tree_cave_a = scene_type(2,5,-3,"oak tree cave","","",False,False,False,False,False,True,False,15,"forest","",True,False,"","a cave below the large oak tree",[],[],[],[],[])
large_tree_cave_b = scene_type(1,5,-3,"oak tree cave","","",False,False,False,False,False,True,False,15,"forest","",False,False,"","a cave below the large oak tree",[],[],[],[],[])
large_tree_cave_c = scene_type(1,6,-3,"oak tree cave","","",False,False,False,False,False,True,False,15,"forest","",False,False,"","a cave below the large oak tree",[],[],[],[],[])
large_tree_cave_d = scene_type(1,7,-3,"oak tree cave","","",False,False,False,False,False,True,False,15,"forest","",False,False,"","a cave below the large oak tree",[],[],[],[],[])
large_tree_cave_e = scene_type(1,8,-3,"oak tree cave","","",False,False,False,False,False,True,False,15,"forest","",False,False,"","a cave below the large oak tree",[],[],[],[],[])
large_tree_cave_f = scene_type(1,4,-3,"oak tree cave","","",False,False,False,False,False,True,False,15,"forest","",False,False,"","a cave below the large oak tree",[],[],[],[],[])
large_tree_cave_g = scene_type(1,4,-3,"oak tree cave","","",False,False,False,False,False,True,False,15,"forest","",False,False,"","a cave below the large oak tree",[],[],[],[],[])
large_tree_cave_h = scene_type(2,6,-3,"oak tree cave","","",False,False,False,False,False,True,False,15,"forest","",False,False,"","a cave below the large oak tree",[],[],[],[],[])
large_tree_cave_i = scene_type(2,7,-3,"oak tree cave","","",False,False,False,False,False,True,False,15,"forest","",False,False,"","a cave below the large oak tree",[],[],[],[],[])
large_tree_cave_j = scene_type(3,4,-3,"oak tree cave","","",False,False,False,False,False,True,False,15,"forest","",False,False,"","a cave below the large oak tree",[],[],[],[],[])
large_tree_cave_k = scene_type(3,5,-3,"oak tree cave","","",False,False,False,False,False,True,False,15,"forest","",False,False,"","a cave below the large oak tree",[],[],[],[],[])
large_tree_cave_l = scene_type(3,6,-3,"oak tree cave","","",False,False,False,False,False,True,False,15,"forest","",False,False,"","a cave below the large oak tree",[],[],[],[],[])
large_tree_cave_m = scene_type(3,7,-3,"oak tree cave","","",False,False,False,False,False,True,False,15,"forest","",False,False,"","a cave below the large oak tree",[],[],[],[],[])
large_tree_cave_n = scene_type(4,4,-3,"oak tree cave","","",False,False,False,False,False,True,False,15,"forest","",False,False,"","a cave below the large oak tree",[],[],[],[],[])
large_tree_cave_o = scene_type(4,5,-3,"oak tree cave","","",False,False,False,False,False,True,False,15,"forest","",False,False,"","a cave below the large oak tree",[],[],[],[],[])
large_tree_cave_p = scene_type(4,6,-3,"oak tree cave","","",False,False,False,False,False,True,False,15,"forest","",False,False,"","a cave below the large oak tree",[],[],[],[],[])


large_tree_cave_door = scene_type(1,9,-3,"oak doorway","","",True,False,False,False,False,False,False,0,"dirt","",False,False,"this door is locked, you need a key..","The door is unlocked...",[],[],[],[],[])

large_tree_cave_room = scene_type(1,10,-3,"oak tree cave room","","",True,False,False,False,False,True,True,0,"forest","",False,False,"","a cave below the large oak tree",[],[],[],[],[])

birds_nest = scene_type(3,5,0,"a bird's nest","cosy","dimly lit",True,False,False,False,True,True,False,0,"grassy","",False,True,"","you are in a house made of twigs and branches",[],[],[],[],[])
 # Forest

forest_1 = scene_type(4,5,0,"the dark forest","","",False,False,False,False,False,True,False,10,"forest","",False,False,"","it's dark here",[],[],[],[],[])
forest_2 = scene_type(4,4,0,"the dark forest","","",False,False,False,False,False,True,False,10,"forest","",False,False,"","the smell of pine forest is very strong here",[],[],[],[],[])
forest_3 = scene_type(5,5,0,"the dark forest","","",False,False,False,False,False,True,False,10,"forest","",False,False,"","lots of trees...",[],[],[],[],[])
forest_4 = scene_type(5,4,0,"the dark forest","","",False,False,False,False,False,True,False,10,"forest","",False,False,"","there's a circle of rocks in a small clearing",[],[],[],[],[])
forest_5 = scene_type(4,3,0,"the dark forest","","",False,False,False,False,False,True,False,10,"forest","",False,False,"","small mushrooms litter the ground here",[],[],[],[],[])
forest_6 = scene_type(3,4,0,"the dark forest","","",False,False,False,False,False,True,False,10,"forest","",False,False,"","there is smoke to the north",[],[],[],[],[])
forest_7 = scene_type(5,3,0,"the dark forest","","",False,False,False,False,False,True,False,10,"grassy","",False,False,"","the outskirts of dismurth",[],[],[],[],[])
forest_8 = scene_type(2,3,0,"the dark forest","","",False,False,False,False,False,True,False,10,"forest","",False,False,"","the forest isn't so dense here",[],[],[],[],[])
forest_9 = scene_type(4,6,0,"the dark forest","","",False,False,False,False,False,True,False,10,"forest","",False,False,"","",[],[],[],[],[])
forest_10 = scene_type(5,6,0,"the dark forest","","",False,False,False,False,False,True,False,10,"forest","",False,False,"","",[],[],[],[],[])
forest_11 = scene_type(2,6,0,"the dark forest","","",False,False,False,False,False,True,False,10,"forest","",False,False,"","",[],[],[],[],[])
forest_12 = scene_type(3,6,0,"the dark forest","","",False,False,False,False,False,True,False,10,"forest","",False,False,"","",[],[],[],[],[])
forest_13 = scene_type(2,4,0,"the dark forest","","",False,False,False,False,False,True,False,10,"forest","",False,False,"","",[],[],[],[],[])
forest_14 = scene_type(3,2,0,"the dark forest","","",False,False,False,False,False,True,False,10,"forest","",False,False,"","",[],[],[],[],[])

forest_cabin = scene_type(3,3,0,"the forest cabin","","cloudy",True,False,False,False,True,True,False,0,"grassy","",False,True,"", "a nice log cabin, many strange objects are displayed on shelves and a large desk has piles of books next to it.",[],[],[],[],[])

grassland_1 = scene_type(2,0,0,"grassland","","",False,False,False,False,False,True,False,5,"grassy","",False,False,"","wide open space, lots of grass",[],[],[],[],[])
grassland_2 = scene_type(3,0,0,"grassland","","",False,False,False,False,False,True,False,5,"grassy","",False,False,"","wide open space, lots of grass",[],[],[],[],[])
grassland_3 = scene_type(4,0,0,"grassland","","",False,False,False,False,False,True,False,5,"grassy","",False,False,"","wide open space, lots of grass",[],[],[],[],[])
grassland_4 = scene_type(2,1,0,"grassland","","",False,False,False,False,False,True,False,5,"grassy","",False,False,"","wide open space, lots of grass",[],[],[],[],[])
grassland_5 = scene_type(4,1,0,"grassland","","",False,False,False,False,False,True,False,5,"grassy","",False,False,"","wide open space, lots of grass",[],[],[],[],[])
grassland_6 = scene_type(2,2,0,"grassland","","",False,False,False,False,False,True,False,5,"grassy","",False,False,"","wide open space, lots of grass",[],[],[],[],[])
grassland_7 = scene_type(4,2,0,"grassland","","",False,False,False,False,False,True,False,5,"grassy","",False,False,"","wide open space, lots of grass",[],[],[],[],[])

grassland_8 = scene_type(7,6,0,"grassland","","",False,False,False,False,False,True,False,5,"grassy","",False,False,"","wide open space, lots of grass",[],[],[],[],[])
grassland_9 = scene_type(8,6,0,"grassland","","",False,False,False,False,False,True,False,5,"grassy","",False,False,"","wide open space, lots of grass",[],[],[],[],[])

mountain_road_1 = scene_type(8,0,0,"stony road","","",True,True,False,False,True,True,False,0,"road_bt","",False,False,"","the mountains to the north are mined for valuable minerals",[],[],[],[],[])
mountain_road_2 = scene_type(9,0,0,"stony road","","",True,True,False,False,True,True,False,0,"road_bt","",False,False,"","the mountains to the north are mined for valuable minerals",[],[],[],[],[])
dismurth_quarry_c = scene_type(8,1,0,"the dismurth quarry office","","",True,True,False,False,True,True,False,0,"grassy","",False,True,"","dwarves are sorting minerals and shipping them out in carts",[],[],[],[],[])
dismurth_quarry_d = scene_type(9,1,0,"the dismurth quarry","","",True,True,False,False,True,True,False,0,"grassy","",False,False,"","the mountains to the north are mined for valuable minerals",[],[],[],[],[])

mountain_road_3 = scene_type(10,0,0,"stony road","","",True,True,False,False,True,True,False,0,"road","road_bt",False,False,"","the mountains to the north are mined for valuable minerals",[],[],[],[],[])
mountain_road_4 = scene_type(11,0,0,"stony road","","",True,True,False,False,True,True,False,0,"road","road_bt",False,False,"","the mountains to the north are mined for valuable minerals",[],[],[],[],[])
mountain_road_5 = scene_type(12,0,0,"stony road","","",True,True,False,False,True,True,False,0,"road","road_bt",False,False,"","the mountains to the north are mined for valuable minerals",[],[],[],[],[])
mountain_road_6 = scene_type(13,0,0,"stony road","","",True,True,False,False,True,True,False,0,"road","road_bt",False,False,"","the mountains to the north are mined for valuable minerals",[],[],[],[],[])
mountain_road_7 = scene_type(14,0,0,"stony road","","",True,True,False,False,True,True,False,0,"road","road_tr",False,False,"","the mountains to the north are mined for valuable minerals",[],[],[],[],[])
mountain_road_8 = scene_type(14,1,0,"stony road","","",True,True,False,False,True,True,False,0,"road","road_lr",False,False,"","the mountains to the north are mined for valuable minerals",[],[],[],[],[])
mountain_road_9 = scene_type(14,2,0,"stony road","","",True,True,False,False,True,True,False,0,"road","road_lr",False,False,"","the mountains to the north are mined for valuable minerals",[],[],[],[],[])
mountain_road_10 = scene_type(14,3,0,"stony road","","",True,True,False,False,True,True,False,0,"road","road_bl",False,False,"","the mountains to the north are mined for valuable minerals",[],[],[],[],[])
mountain_road_11 = scene_type(15,3,0,"stony road","","",True,True,False,False,True,True,False,0,"road","road_bt",False,False,"","the mountains to the north are mined for valuable minerals",[],[],[],[],[])
mountain_road_12 = scene_type(16,3,0,"stony road","","",True,True,False,False,True,True,False,0,"road","road_bt",False,False,"","the mountains to the north are mined for valuable minerals",[],[],[],[],[])
mountain_road_13 = scene_type(17,3,0,"stony road","","",True,True,False,False,True,True,False,0,"road","road_bt",False,False,"","the mountains to the north are mined for valuable minerals",[],[],[],[],[])
mountain_road_14 = scene_type(18,3,0,"stony road","","",True,True,False,False,True,True,False,0,"road","road_bt",False,False,"","the mountains to the north are mined for valuable minerals",[],[],[],[],[])

# xpos, ypos, zpos, name, , ,
# is_safe, can_fish, can_cook, can_craft, can_steal, passable, treasure, difficulty, biome_String,
# has_stairs, indoors, impass_msg, flavour_text,
# scene_inventory, scene_weapon_inventory, scene_armor_inventory, scene_helmet_inventory, scene_shield_inventory

# Dismurth

dismurth_monument_a = scene_type(7,0,0,"dwarf monument","","",True,True,False,False,True,True,False,0,"town","",False,False,"","This large monuments mark the entrance to the dismurth tunnel, it is a statue of a dwarf holding a book...",[],[],[],[],[])
dismurth_monument_b = scene_type(5,0,0,"elf monument","","",True,True,False,False,True,True,False,0,"town","",False,False,"","This large monuments mark the entrance to the dismurth tunnel, it is a statue of an elf holding a sword...",[],[],[],[],[])

crossroads = scene_type(6,5,0,"the crossroads","","",True,False,False,False,False,True,False,0,"road","road_l",False,False,"","There is a sign pointing north labelled \' Dismurth \' ",[],[],[],[],[])
east_road = scene_type(7,5,0,"the east road","","",True,False,False,False,False,True,False,0,"road","road_bt",False,False,"","this narrow road leads from the crossroads to the east",[],[],[],[],[])
north_road = scene_type(6,4,0,"the north road","","",True,False,False,False,False,True,False,0,"road","road_lr",False,False,"","this road leads from the crossroads to the northern town of Dismurth, it looks well travelled",[],[],[],[],[])
dismurth_gates = scene_type(6,3,0,"the town gates of Dismurth","","",True,False,False,False,True,True,False,0,"town","",False,False,"","",[],[],[],[],[])
dismurth_square = scene_type(6,2,0,"the town square of Dismurth","","",True,False,False,False,True,True,False,0,"town","",False,False,"","",[],[],[],[],[])
dismurth_market = scene_type(6,1,0,"Dismurth markets","","",True,False,False,False,True,True,False,0,"town","",False,False,"","",[],[],[],[],[])
dismurth_tavern = scene_type(5,1,0,"Dismurth tavern","","",True,False,False,False,True,True,False,0,"town","",False,True,"","",[],[],[],[],[])
dismurth_tunnel_entrance = scene_type(6,0,0,"the entrance to the Dismurth Tunnel","","",True,True,False,False,True,True,False,0,"road","",False,False,"","",[],[],[],[],[])
dismurth_tower_1f = scene_type(7,1,1,"the tower of Dismurth's first floor","","",True,False,False,False,True,True,False,0,"town","",True,True,"","the tower walls are lined with more bookshelves",[],[],[],[],[])
dismurth_tower_gf = scene_type(7,1,0,"the tower of Dismurth's ground floor","","",True,False,False,False,True,True,False,0,"town","",True,True,"","the tower walls are lined with bookshelves, there are many large runestones in the middle of the room",[],[],[],[],[])
dismurth_smith = scene_type(7,2,0,"the Blacksmith of Dismurth","","",True,False,False,False,True,True,False,0,"town","",False,True,"","*a young man is working hard at the furnace*",[],[],[],[],[])
dismurth_barracks = scene_type(5,2,0,"the Barracks of Dismurth","warm","dimly liy",True,False,False,False,True,True,False,0,"town","",False,True,"","you are surrounded by bunks and weapon racks, there is a large table in the middle of the room, a fire crackles in the corner",[],[],[],[],[])
dismurth_farm = scene_type(7,3,0,"the Dismurth farmstead","","",True,False,False,False,True,True,False,0,"grassy","",False,True,"","",[],[],[],[],[])

south_road_a = scene_type(6,6,0,"the south road","","cloudy",True,False,False,False,False,True,False,0,"road","road_lr",False,False,"", "this road leads from the crossroads to the south ",[],[],[],[],[])
dismurth_bridge = scene_type(6,7,0,"the Dismurth bridge","","cloudy",True,False,False,False,False,True,False,0,"road","",False,False,"you may not cross the bridge without rite of passage", "the river looks nice from here",[],[],[],[],[])
south_road_b = scene_type(6,8,0,"the south road","","cloudy",True,False,False,False,False,True,False,0,"road","road_br",False,False,"", "this road continues from the crossroads to the south",[],[],[],[],[])


rocky_hills_1 = scene_type(9,2,0,"rocky hills","","",True,True,False,False,False,True,False,0,"grassy","",False,False,"","very rocky hills",[],[],[],[],[])
rocky_hills_2 = scene_type(9,3,0,"rocky hills","","",True,True,False,False,False,True,False,0,"grassy","",False,False,"","very rocky hills",[],[],[],[],[])

rocky_hills_3 = scene_type(10,1,0,"rocky hills","","",True,True,False,False,False,True,False,0,"grassy","",False,False,"","very rocky hills bruzzy",[],[],[],[],[])
rocky_hills_4 = scene_type(10,2,0,"rocky hills","","",True,True,False,False,False,True,False,0,"forest","",False,False,"","very rocky hills",[],[],[],[],[])
rocky_hills_5 = scene_type(10,3,0,"rocky hills","","",True,True,False,False,False,True,False,0,"grassy","",False,False,"","very rocky hills",[],[],[],[],[])
rocky_forest_1 = scene_type(10,4,0,"rocky forest","","",True,True,False,False,False,True,False,0,"grassy","",False,False,"","very rocky forest",[],[],[],[],[])
rocky_forest_2 = scene_type(10,6,0,"rocky forest","","",True,True,False,False,False,True,False,0,"forest","",False,False,"","very rocky forest",[],[],[],[],[])

rocky_hills_6 = scene_type(11,1,0,"rocky hills","","",True,True,False,False,False,True,False,0,"grassy","",False,False,"","very rocky hills",[],[],[],[],[])
rocky_hills_7 = scene_type(11,2,0,"rocky hills","","",True,True,False,False,False,True,False,0,"grassy","",False,False,"","very rocky hills",[],[],[],[],[])
rocky_hills_8 = scene_type(11,3,0,"rocky hills","","",True,True,False,False,False,True,False,0,"forest","",False,False,"","very rocky hills",[],[],[],[],[])
rocky_forest_3 = scene_type(11,4,0,"rocky forest","","",False,True,False,False,False,True,False,17,"forest","",False,False,"","very rocky forest",[],[],[],[],[])
rocky_forest_4 = scene_type(11,5,0,"rocky forest","","",False,True,False,False,False,True,False,17,"forest","",False,False,"","very rocky forest",[],[],[],[],[])
rocky_forest_5 = scene_type(11,6,0,"rocky forest","","",False,True,False,False,False,True,False,22,"forest","",False,False,"","very rocky forest",[],[],[],[],[])

dense_forest_1 = scene_type(12,1,0,"dense forest","","",False,True,False,False,False,True,False,20,"grassy","",False,False,"","rocky arid lands",[],[],[],[],[])
dense_forest_2 = scene_type(12,2,0,"dense forest","","",False,True,False,False,False,True,False,20,"grassy","",False,False,"","rocky arid lands",[],[],[],[],[])
dense_forest_3 = scene_type(12,3,0,"dense forest","","",False,True,False,False,False,True,False,20,"grassy","",False,False,"","rocky arid lands",[],[],[],[],[])
rocky_forest_6 = scene_type(12,4,0,"rocky forest","","",False,True,False,False,False,True,False,17,"forest","",False,False,"","very rocky forest",[],[],[],[],[])
rocky_forest_7 = scene_type(12,5,0,"rocky forest","","",False,True,False,False,False,False,False,17,"grassy","",False,False,"","very rocky forest",[],[],[],[],[])
rocky_forest_8 = scene_type(12,6,0,"rocky forest","","",False,True,False,False,False,True,False,22,"forest","",False,False,"","very rocky forest",[],[],[],[],[])

dense_forest_4 = scene_type(13,1,0,"dense forest","","",False,True,False,False,False,True,False,20,"forest","",False,False,"","rocky arid lands",[],[],[],[],[])
dense_forest_5 = scene_type(13,2,0,"dense forest","","",False,True,False,False,False,True,False,20,"forest","",False,False,"","rocky arid lands",[],[],[],[],[])
dense_forest_6 = scene_type(13,3,0,"dense forest","","",False,True,False,False,False,True,False,20,"forest","",False,False,"","rocky arid lands",[],[],[],[],[])
rocky_forest_9 = scene_type(13,4,0,"rocky forest","","",False,True,False,False,False,True,False,17,"forest","",False,False,"","very rocky forest",[],[],[],[],[])
rocky_forest_10 = scene_type(13,5,0,"rocky forest","","",False,True,False,False,False,True,False,22,"forest","",False,False,"","very rocky forest",[],[],[],[],[])
rocky_forest_11 = scene_type(13,6,0,"rocky forest","","",False,True,False,False,False,True,False,22,"forest","",False,False,"","very rocky forest",[],[],[],[],[])

rocky_forest_9 = scene_type(14,4,0,"rocky forest","","",False,True,False,False,False,True,False,17,"forest","",False,False,"","very rocky forest",[],[],[],[],[])
rocky_forest_10 = scene_type(14,5,0,"rocky forest","","",False,True,False,False,False,True,False,17,"grassy","",False,False,"","very rocky forest",[],[],[],[],[])
rocky_forest_11 = scene_type(14,6,0,"rocky forest","","",False,True,False,False,False,True,False,22,"forest","",False,False,"","very rocky forest",[],[],[],[],[])

rocky_forest_12 = scene_type(15,4,0,"rocky forest","","",False,True,False,False,False,True,False,17,"forest","",False,False,"","very rocky forest",[],[],[],[],[])
rocky_forest_13 = scene_type(15,5,0,"rocky forest","","",False,True,False,False,False,True,False,17,"grassy","",False,False,"","very rocky forest",[],[],[],[],[])
rocky_forest_14 = scene_type(15,6,0,"rocky forest","","",False,True,False,False,False,True,False,22,"grassy","",False,False,"","very rocky forest",[],[],[],[],[])

rocky_forest_15 = scene_type(16,4,0,"rocky forest","","",False,True,False,False,False,True,False,17,"forest","",False,False,"","very rocky forest",[],[],[],[],[])
rocky_forest_16 = scene_type(16,5,0,"rocky forest","","",False,True,False,False,False,True,False,17,"forest","",False,False,"","very rocky forest",[],[],[],[],[])
rocky_forest_17 = scene_type(16,6,0,"rocky forest","","",False,True,False,False,False,True,False,22,"forest","",False,False,"","very rocky forest",[],[],[],[],[])




dismurth_fisherman_house = scene_type(8,2,0,"fisherman's house","","",True,False,False,False,True,True,False,0,"town","",False,True,"","the fisherman lives here",[],[],[],[],[])
turnip_field = scene_type(8,3,0,"a turnip field","","",True,False,False,False,True,True,False,0,"grassy","",False,False,"","turnips bruzzy",[],[],[],[],[])

highlands_a = scene_type(7,4,0,"highlands","","",False,False,False,False,False,True,True,1,"grassy","",False,False,"","grass and low stone walls form paddocks around you",[],[],[],[],[])
highlands_b = scene_type(8,4,0,"highlands","","",False,False,False,False,False,True,True,1,"grassy","",False,False,"","",[],[],[],[],[])

fortress_gate = scene_type(8,5,0,"bandit lands","","",False,False,False,False,False,True,False,100,"grassy","",False,False,"","",[],[],[],[],[])
fortress = scene_type(9,5,0,"the bandit fortress","","",False,False,False,False,False,True,True,100,"grassy","",False,True,"","the bandit fortress",[],[],[],[],[])
fort_wall_a = scene_type(9,4,0,"bandit lands","","",False,False,False,False,False,True,False,0,"grassy","",False,False,"the large, wooden wall blocks your path","",[],[],[],[],[])
fort_wall_b = scene_type(10,5,0,"bandit lands","","",False,False,False,False,False,True,False,0,"grassy","",False,False,"the large, wooden wall blocks your path","",[],[],[],[],[])
fort_wall_c = scene_type(9,6,0,"bandit lands","","",False,False,False,False,False,True,False,0,"grassy","",False,False,"the large, wooden wall blocks your path","",[],[],[],[],[])

highlands_c = scene_type(10,10,0,"highlands","","",False,False,False,False,False,True,False,0,"forest","",False,False,"","",[],[],[],[],[])

plains_1 = scene_type(4,9,0,"plains","","",False,False,False,False,False,True,False,30,"grassy","",False,False,"","sandy plains",[],[],[],[],[])
plains_2 = scene_type(5,9,0,"plains","","",False,False,False,False,False,True,False,30,"grassy","",False,False,"","sandy plains",[],[],[],[],[])
plains_3 = scene_type(4,9,0,"plains","","",False,False,False,False,False,True,False,30,"grassy","",False,False,"","sandy plains",[],[],[],[],[])
plains_4 = scene_type(4,10,0,"plains","","",False,False,False,False,False,True,False,30,"grassy","",False,False,"","sandy plains",[],[],[],[],[])
plains_5 = scene_type(5,10,0,"plains","","",False,False,False,False,False,True,False,30,"grassy","",False,False,"","sandy plains",[],[],[],[],[])
plains_6 = scene_type(2,8,0,"plains","","",False,False,False,False,False,True,False,30,"grassy","",False,False,"","sandy plains",[],[],[],[],[])
plains_7 = scene_type(5,11,0,"plains","","",False,False,False,False,False,True,False,30,"grassy","",False,False,"","sandy plains",[],[],[],[],[])
plains_8 = scene_type(7,8,0,"plains","","",False,False,False,False,False,True,False,30,"grassy","",False,False,"","sandy plains",[],[],[],[],[])
plains_9 = scene_type(7,9,0,"plains","","",False,False,False,False,False,True,False,30,"grassy","",False,False,"","sandy plains",[],[],[],[],[])
plains_10 = scene_type(7,10,0,"plains","","",False,False,False,False,False,True,False,30,"grassy","",False,False,"","sandy plains",[],[],[],[],[])
plains_11 = scene_type(7,11,0,"plains","","",False,False,False,False,False,True,False,30,"grassy","",False,False,"","sandy plains",[],[],[],[],[])

plains_12 = scene_type(8,8,0,"plains","","",False,False,False,False,False,True,False,30,"grassy","",False,False,"","sandy plains",[],[],[],[],[])
plains_13 = scene_type(8,9,0,"plains","","",False,False,False,False,False,True,False,30,"grassy","",False,False,"","sandy plains",[],[],[],[],[])
plains_14 = scene_type(8,10,0,"plains","","",False,False,False,False,False,True,False,30,"grassy","",False,False,"","sandy plains",[],[],[],[],[])
plains_15 = scene_type(8,11,0,"plains","","",False,False,False,False,False,True,False,30,"grassy","",False,False,"","sandy plains",[],[],[],[],[])
plains_16 = scene_type(6,10,0,"plains","","",False,False,False,False,False,True,False,30,"grassy","",False,False,"","sandy plains",[],[],[],[],[])
plains_17 = scene_type(6,11,0,"plains","","",False,False,False,False,False,True,False,30,"grassy","",False,False,"","sandy plains",[],[],[],[],[])

woods_1 = scene_type(9,8,0,"woods","","",False,False,False,False,False,True,False,40,"forest","",False,False,"","some nice woods",[],[],[],[],[])
woods_2 = scene_type(9,9,0,"woods","","",False,False,False,False,False,True,False,40,"forest","",False,False,"","interesting woods",[],[],[],[],[])
woods_3 = scene_type(9,10,0,"woods","","",False,False,False,False,False,True,False,40,"forest","",False,False,"","strange woods",[],[],[],[],[])
woods_4 = scene_type(9,11,0,"woods","","",False,False,False,False,False,True,False,40,"forest","",False,False,"","there is an old broken cart here",[],[],[],[],[])

woods_5 = scene_type(10,8,0,"woods","","",False,False,False,False,False,True,False,40,"forest","",False,False,"","some nice woods",[],[],[],[],[])
woods_6 = scene_type(10,9,0,"woods","","",False,False,False,False,False,True,False,40,"forest","",False,False,"","interesting woods",[],[],[],[],[])
woods_7 = scene_type(10,10,0,"woods","","",False,False,False,False,False,True,False,40,"forest","",False,False,"","strange woods",[],[],[],[],[])
woods_8 = scene_type(10,11,0,"woods","","",False,False,False,False,False,True,False,40,"forest","",False,False,"","a massive boulder looms above the trees, some pieces have fallen off",[],[],[],[],[])

woods_9 = scene_type(11,8,0,"woods","","",False,False,False,False,False,True,False,40,"forest","",False,False,"","some nice woods",[],[],[],[],[])
woods_10 = scene_type(11,9,0,"woods","","",False,False,False,False,False,True,False,40,"forest","",False,False,"","interesting woods",[],[],[],[],[])
woods_11 = scene_type(11,10,0,"woods","","",False,False,False,False,False,True,False,40,"forest","",False,False,"","strange woods",[],[],[],[],[])
woods_12 = scene_type(11,11,0,"woods","","",False,False,False,False,False,True,False,40,"forest","",False,False,"","thick foliage",[],[],[],[],[])
woods_13 = scene_type(11,12,0,"woods","","",False,False,False,False,False,True,False,40,"forest","",False,False,"","thick foliage",[],[],[],[],[])

woods_14 = scene_type(12,8,0,"woods","","",False,False,False,False,False,True,False,40,"forest","",False,False,"","some nice woods",[],[],[],[],[])
woods_15 = scene_type(12,9,0,"woods","","",False,False,False,False,False,True,False,40,"forest","",False,False,"","interesting woods",[],[],[],[],[])
woods_16 = scene_type(12,10,0,"woods","","",False,False,False,False,False,True,False,40,"forest","",False,False,"","strange woods",[],[],[],[],[])
woods_17 = scene_type(12,11,0,"woods","","",False,False,False,False,False,True,False,40,"forest","",False,False,"","thick foliage",[],[],[],[],[])
woods_18 = scene_type(12,12,0,"woods","","",False,False,False,False,False,True,False,40,"forest","",False,False,"","thick foliage",[],[],[],[],[])

woods_19 = scene_type(13,8,0,"deep woods","","",False,False,False,False,False,True,False,70,"forest","",False,False,"","some nice woods",[],[],[],[],[])
woods_20 = scene_type(13,9,0,"deep woods","","",False,False,False,False,False,True,False,70,"forest","",False,False,"","interesting woods",[],[],[],[],[])
woods_21 = scene_type(13,10,0,"deep woods","","",False,False,False,False,False,True,False,70,"forest","",False,False,"","strange woods",[],[],[],[],[])
woods_22 = scene_type(13,11,0,"deep woods","","",False,False,False,False,False,True,False,70,"forest","",False,False,"","thick foliage",[],[],[],[],[])
woods_23 = scene_type(13,12,0,"deep woods","","",False,False,False,False,False,True,False,70,"forest","",False,False,"","thick foliage",[],[],[],[],[])

woods_20 = scene_type(14,9,0,"deep woods","","",False,False,False,False,False,True,False,70,"forest","",False,False,"","interesting woods",[],[],[],[],[])
woods_21 = scene_type(14,10,0,"deep woods","","",False,False,False,False,False,True,False,70,"forest","",False,False,"","strange woods",[],[],[],[],[])
woods_22 = scene_type(14,11,0,"deep woods","","",False,False,False,False,False,True,False,70,"forest","",False,False,"","thick foliage",[],[],[],[],[])
woods_23 = scene_type(14,12,0,"woods","","",False,False,False,False,False,True,False,40,"forest","",False,False,"","thick foliage",[],[],[],[],[])

woods_20 = scene_type(15,9,0,"deep woods","","",False,False,False,False,False,True,False,40,"forest","",False,False,"","interesting woods",[],[],[],[],[])
woods_21 = scene_type(15,10,0,"deep woods","","",False,False,False,False,False,True,False,40,"forest","",False,False,"","strange woods",[],[],[],[],[])
woods_22 = scene_type(15,11,0,"deep woods","","",False,False,False,False,False,True,False,40,"forest","",False,False,"","thick foliage",[],[],[],[],[])
woods_23 = scene_type(15,12,0,"woods","","",False,False,False,False,False,True,False,40,"forest","",False,False,"","thick foliage",[],[],[],[],[])

woods_20 = scene_type(16,9,0,"woods","","",False,False,False,False,False,True,False,40,"forest","",False,False,"","interesting woods",[],[],[],[],[])
woods_21 = scene_type(16,10,0,"woods","","",False,False,False,False,False,True,False,40,"forest","",False,False,"","strange woods",[],[],[],[],[])
woods_22 = scene_type(16,11,0,"woods","","",False,False,False,False,False,True,False,40,"forest","",False,False,"","thick foliage",[],[],[],[],[])

riverbank_1 = scene_type(1,11,0,"river bank","","",False,False,False,False,False,True,False,30,"grassy","",False,False,"","a nice grassy river bank",[],[],[],[],[])
riverbank_2 = scene_type(1,12,0,"river bank","","",False,False,False,False,False,True,False,30,"grassy","",False,False,"","a nice grassy river bank",[],[],[],[],[])
riverbank_3 = scene_type(1,13,0,"river bank","","",False,False,False,False,False,True,False,30,"grassy","",False,False,"","a nice grassy river bank",[],[],[],[],[])
riverbank_4 = scene_type(1,14,0,"river bank","","",False,False,False,False,False,True,False,30,"grassy","",False,False,"","a nice grassy river bank",[],[],[],[],[])
riverbank_5 = scene_type(1,15,0,"river bank","","",False,False,False,False,False,True,False,30,"grassy","",False,False,"","a nice grassy river bank",[],[],[],[],[])
riverbank_6 = scene_type(1,16,0,"river bank","","",False,False,False,False,False,True,False,30,"grassy","",False,False,"","a nice grassy river bank",[],[],[],[],[])
riverbank_7 = scene_type(1,17,0,"river bank","","",False,False,False,False,False,True,False,30,"grassy","",False,False,"","a nice grassy river bank",[],[],[],[],[])
riverbank_8 = scene_type(1,18,0,"river bank","","",False,False,False,False,False,True,False,30,"grassy","",False,False,"","a nice grassy river bank",[],[],[],[],[])

roadside_1 = scene_type(2,12,0,"roadside","","",False,False,False,False,False,True,False,30,"grassy","",False,False,"","a nice grassy river bank",[],[],[],[],[])
roadside_2 = scene_type(2,13,0,"roadside","","",False,False,False,False,False,True,False,30,"grassy","",False,False,"","a nice grassy river bank",[],[],[],[],[])
roadside_3 = scene_type(2,14,0,"roadside","","",False,False,False,False,False,True,False,30,"grassy","",False,False,"","a nice grassy river bank",[],[],[],[],[])
roadside_4 = scene_type(2,15,0,"roadside","","",False,False,False,False,False,True,False,30,"grassy","",False,False,"","a nice grassy river bank",[],[],[],[],[])
roadside_5 = scene_type(2,16,0,"roadside","","",False,False,False,False,False,True,False,30,"forest","",False,False,"","a nice grassy river bank",[],[],[],[],[])
roadside_6 = scene_type(2,17,0,"roadside","","",False,False,False,False,False,True,False,30,"forest","",False,False,"","a nice grassy river bank",[],[],[],[],[])
roadside_7 = scene_type(2,18,0,"roadside","","",False,False,False,False,False,True,False,30,"grassy","",False,False,"","a nice grassy river bank",[],[],[],[],[])

roadside_8 = scene_type(3,15,0,"roadside","","",False,False,False,False,False,True,False,30,"grassy","",False,False,"","a nice grassy river bank",[],[],[],[],[])
roadside_9 = scene_type(3,16,0,"roadside","","",False,False,False,False,False,True,False,30,"grassy","",False,False,"","a nice grassy river bank",[],[],[],[],[])
roadside_10 = scene_type(3,17,0,"roadside","","",False,False,False,False,False,True,False,30,"grassy","",False,False,"","a nice grassy river bank",[],[],[],[],[])
roadside_11 = scene_type(3,18,0,"roadside","","",False,False,False,False,False,True,False,30,"grassy","",False,False,"","a nice grassy river bank",[],[],[],[],[])

south_roadside_1 = scene_type(4,18,0,"roadside","","",False,False,False,False,False,True,False,30,"grassy","",False,False,"","a nice grassy river bank",[],[],[],[],[])
south_roadside_2 = scene_type(5,18,0,"roadside","","",False,False,False,False,False,True,False,30,"grassy","",False,False,"","a nice grassy river bank",[],[],[],[],[])
south_roadside_3 = scene_type(6,18,0,"roadside","","",False,False,False,False,False,True,False,30,"grassy","",False,False,"","a nice grassy river bank",[],[],[],[],[])
south_roadside_4 = scene_type(7,18,0,"roadside","","",False,False,False,False,False,True,False,30,"grassy","",False,False,"","a nice grassy river bank",[],[],[],[],[])
south_roadside_5 = scene_type(8,18,0,"roadside","","",False,False,False,False,False,True,False,30,"grassy","",False,False,"","a nice grassy river bank",[],[],[],[],[])
south_roadside_6 = scene_type(9,18,0,"roadside","","",False,False,False,False,False,True,False,30,"grassy","",False,False,"","a nice grassy river bank",[],[],[],[],[])



crags = scene_type(15,15,0,"crags","","cloudy",False,False,False,False,False,True,False,50,"forest","",False,False,"", "some particularly generic crags, very rocky indeed",[],[],[],[],[])
fields = scene_type(16,16,0,"ordinary fields","","cloudy",False,False,False,False,False,True,False,50,"forest","",False,False,"", "some particularly generic fields",[],[],[],[],[])
swamp = scene_type(17,17,0,"swamp","","cloudy",False,False,False,False,False,True,False,50,"forest","",False,False,"", "some particularly generic fields",[],[],[],[],[])


# xpos, ypos, zpos, name, , ,
# is_safe, can_fish, can_cook, can_craft, can_steal, passable, treasure, difficulty, biome_String,
# has_stairs, indoors, impass_msg, flavour_text,
# scene_inventory, scene_weapon_inventory, scene_armor_inventory, scene_helmet_inventory, scene_shield_inventory

# Sorlund
sorlund_grass_1 = scene_type(4,12,0,"patchy grass","","",False,False,False,False,False,True,False,30,"grassy","",False,False,"","a nice grassy river bank",[],[],[],[],[])
sorlund_grass_2 = scene_type(4,13,0,"patchy grass","","",False,False,False,False,False,True,False,30,"grassy","",False,False,"","a nice grassy river bank",[],[],[],[],[])
sorlund_grass_3 = scene_type(8,12,0,"patchy grass","","",False,False,False,False,False,True,False,30,"grassy","",False,False,"","a nice grassy river bank",[],[],[],[],[])
sorlund_grass_4 = scene_type(9,12,0,"patchy grass","","",False,False,False,False,False,True,False,30,"grassy","",False,False,"","a nice grassy river bank",[],[],[],[],[])
sorlund_grass_4 = scene_type(10,12,0,"patchy grass","","",False,False,False,False,False,True,False,30,"grassy","",False,False,"","a nice grassy river bank",[],[],[],[],[])

sorrlund_lake_grass_1 = scene_type(5,16,0,"grassy lake side","","",False,False,False,False,False,True,False,30,"grassy","",False,False,"","a nice grassy river bank",[],[],[],[],[])
sorrlund_lake_grass_2 = scene_type(6,16,0,"grassy lake side","","",False,False,False,False,False,True,False,30,"grassy","",False,False,"","a nice grassy river bank",[],[],[],[],[])
sorrlund_lake_grass_3 = scene_type(7,16,0,"grassy lake side","","",False,False,False,False,False,True,False,30,"grassy","",False,False,"","a nice grassy river bank",[],[],[],[],[])
sorrlund_lake_grass_4 = scene_type(8,16,0,"grassy lake side","","",False,False,False,False,False,True,False,30,"grassy","",False,False,"","a nice grassy river bank",[],[],[],[],[])
sorrlund_lake_grass_5 = scene_type(9,16,0,"grassy lake side","","",False,False,False,False,False,True,False,30,"grassy","",False,False,"","a nice grassy river bank",[],[],[],[],[])
sorrlund_lake_grass_6 = scene_type(10,16,0,"grassy lake side","","",False,False,False,False,False,True,False,30,"grassy","",False,False,"","a nice grassy river bank",[],[],[],[],[])

sorrlund_lake_grass_7 = scene_type(10,13,0,"grassy lake side","","",False,False,False,False,False,True,False,30,"grassy","",False,False,"","a nice grassy river bank",[],[],[],[],[])
sorrlund_lake_grass_8 = scene_type(10,14,0,"grassy lake side","","",False,False,False,False,False,True,False,30,"grassy","",False,False,"","a nice grassy river bank",[],[],[],[],[])
sorrlund_lake_grass_9 = scene_type(10,15,0,"grassy lake side","","",False,False,False,False,False,True,False,30,"grassy","",False,False,"","a nice grassy river bank",[],[],[],[],[])



sorrlund_lake_1 = scene_type(5,12,0,"the Sorrlund Lake","","cloudy",True,False,False,False,False,False,False,0,"water","river_tl",False,False,"The river is too deep to pass", "a wide river, i can't see the other side...",[],[],[],[],[])
sorrlund_lake_2 = scene_type(6,12,0,"the Sorrlund Lake","","cloudy",True,False,False,False,False,False,False,0,"water","river_t",False,False,"The river is too deep to pass", "a wide river, i can't see the other side...",[],[],[],[],[])
sorrlund_lake_3 = scene_type(7,12,0,"the Sorrlund Lake","","cloudy",True,False,False,False,False,False,False,0,"water","river_tr",False,False,"The river is too deep to pass", "a wide river, i can't see the other side...",[],[],[],[],[])

sorrlund_lake_4 = scene_type(5,13,0,"the Sorrlund Lake","","cloudy",True,False,False,False,False,False,False,0,"water","river_l",False,False,"The river is too deep to pass", "a wide river, i can't see the other side...",[],[],[],[],[])
sorrlund_lake_5 = scene_type(6,13,0,"the Sorrlund Lake","","cloudy",True,False,False,False,False,False,False,0,"water","river",False,False,"The river is too deep to pass", "a wide river, i can't see the other side...",[],[],[],[],[])
sorrlund_lake_6 = scene_type(7,13,0,"the Sorrlund Lake","","cloudy",True,False,False,False,False,False,False,0,"water","river",False,False,"The river is too deep to pass", "a wide river, i can't see the other side...",[],[],[],[],[])
sorrlund_lake_7 = scene_type(8,13,0,"the Sorrlund Lake","","cloudy",True,False,False,False,False,False,False,0,"water","river_t",False,False,"The river is too deep to pass", "a wide river, i can't see the other side...",[],[],[],[],[])
sorrlund_lake_8 = scene_type(9,13,0,"the Sorrlund Lake","","cloudy",True,False,False,False,False,False,False,0,"water","river_tr",False,False,"The river is too deep to pass", "a wide river, i can't see the other side...",[],[],[],[],[])

sorrlund_lake_9 = scene_type(5,14,0,"the Sorrlund Lake","","cloudy",True,False,False,False,False,False,False,0,"water","river_l",False,False,"The river is too deep to pass", "a wide river, i can't see the other side...",[],[],[],[],[])
sorrlund_lake_10 = scene_type(6,14,0,"the Sorrlund Lake","","cloudy",True,False,False,False,False,False,False,0,"water","river",False,False,"The river is too deep to pass", "a wide river, i can't see the other side...",[],[],[],[],[])
sorrlund_lake_11 = scene_type(7,14,0,"the Sorrlund Lake","","cloudy",True,False,False,False,False,False,False,0,"water","river",False,False,"The river is too deep to pass", "a wide river, i can't see the other side...",[],[],[],[],[])
sorrlund_lake_12 = scene_type(8,14,0,"the Sorrlund Lake","","cloudy",True,False,False,False,False,False,False,0,"water","river",False,False,"The river is too deep to pass", "a wide river, i can't see the other side...",[],[],[],[],[])
sorrlund_lake_13 = scene_type(9,14,0,"the Sorrlund Lake","","cloudy",True,False,False,False,False,False,False,0,"water","river_r",False,False,"The river is too deep to pass", "a wide river, i can't see the other side...",[],[],[],[],[])

sorrlund_lake_13 = scene_type(5,15,0,"the Sorrlund Lake","","cloudy",True,False,False,False,False,False,False,0,"water","river_bl",False,False,"The river is too deep to pass", "a wide river, i can't see the other side...",[],[],[],[],[])
sorrlund_lake_13 = scene_type(6,15,0,"the Sorrlund Lake","","cloudy",True,False,False,False,False,False,False,0,"water","river_b",False,False,"The river is too deep to pass", "a wide river, i can't see the other side...",[],[],[],[],[])
sorrlund_lake_13 = scene_type(7,15,0,"the Sorrlund Lake","","cloudy",True,False,False,False,False,False,False,0,"water","river_b",False,False,"The river is too deep to pass", "a wide river, i can't see the other side...",[],[],[],[],[])
sorrlund_lake_13 = scene_type(8,15,0,"the Sorrlund Lake","","cloudy",True,False,False,False,False,False,False,0,"water","river_b",False,False,"The river is too deep to pass", "a wide river, i can't see the other side...",[],[],[],[],[])
sorrlund_lake_13 = scene_type(9,15,0,"the Sorrlund Lake","","cloudy",True,False,False,False,False,False,False,0,"water","river_br",False,False,"The river is too deep to pass", "a wide river, i can't see the other side...",[],[],[],[],[])



sorrlund_lake_1 = scene_type(5,12,0,"the Sorrlund Lake","","cloudy",True,False,False,False,False,False,False,0,"water","river_tl",False,False,"The river is too deep to pass", "a wide river, i can't see the other side...",[],[],[],[],[])
sorrlund_lake_1 = scene_type(5,12,0,"the Sorrlund Lake","","cloudy",True,False,False,False,False,False,False,0,"water","river_tl",False,False,"The river is too deep to pass", "a wide river, i can't see the other side...",[],[],[],[],[])
sorrlund_lake_1 = scene_type(5,12,0,"the Sorrlund Lake","","cloudy",True,False,False,False,False,False,False,0,"water","river_tl",False,False,"The river is too deep to pass", "a wide river, i can't see the other side...",[],[],[],[],[])



high_road_1 = scene_type(5,8,0,"the high road","","cloudy",True,False,False,False,False,True,False,0,"road","road_bt",False,False,"", "this road continues from the crossroads to the south west",[],[],[],[],[])
high_road_2 = scene_type(4,8,0,"the high road","","cloudy",True,False,False,False,False,True,False,0,"road","road_bt",False,False,"", "this road continues from the crossroads to the south west",[],[],[],[],[])
high_road_3 = scene_type(3,8,0,"the high road","","cloudy",True,False,False,False,False,True,False,0,"road","road_tl",False,False,"", "this road continues from the crossroads to the south west",[],[],[],[],[])
high_road_4 = scene_type(3,9,0,"the high road","","cloudy",True,False,False,False,False,True,False,0,"road","road_lr",False,False,"", "this road continues from the crossroads to the south west",[],[],[],[],[])
high_road_5 = scene_type(3,10,0,"the high road","","cloudy",True,False,False,False,False,True,False,0,"road","road_r",False,False,"", "this road continues from the crossroads to the south west",[],[],[],[],[])
high_road_6 = scene_type(3,11,0,"the high road","","cloudy",True,False,False,False,False,True,False,0,"road","road_lr",False,False,"", "this road continues from the crossroads to the south west",[],[],[],[],[])
high_road_7 = scene_type(3,12,0,"the high road","","cloudy",True,False,False,False,False,True,False,0,"road","road_lr",False,False,"", "this road continues from the crossroads to the south west",[],[],[],[],[])
high_road_8 = scene_type(3,13,0,"the high road","","cloudy",True,False,False,False,False,True,False,0,"road","road_lr",False,False,"", "this road continues from the crossroads to the south west",[],[],[],[],[])
high_road_9 = scene_type(3,14,0,"the high road","","cloudy",True,False,False,False,False,True,False,0,"road","road_bl",False,False,"", "this road continues from the crossroads to the south west",[],[],[],[],[])
high_road_10 = scene_type(4,14,0,"the high road","","cloudy",True,False,False,False,False,True,False,0,"road","road_tr",False,False,"", "this road continues from the crossroads to the south west",[],[],[],[],[])
high_road_11 = scene_type(4,15,0,"the high road","","cloudy",True,False,False,False,False,True,False,0,"road","road_lr",False,False,"", "this road continues from the crossroads to the south west",[],[],[],[],[])
high_road_12 = scene_type(4,16,0,"the high road","","cloudy",True,False,False,False,False,True,False,0,"road","road_lr",False,False,"", "this road continues from the crossroads to the south west",[],[],[],[],[])


sorlund_church = scene_type(2,9,0,"the Sorlund church","","cloudy",True,False,False,False,False,True,False,0,"town","",False,True,"", "an ancient monument to the gods of harvest",[],[],[],[],[])
sorlund_graveyard = scene_type(1,9,0,"the Sorlund graveyard","","cloudy",True,False,False,False,False,True,False,0,"town","",False,False,"", "the people of Sorlund bury their dead here...",[],[],[],[],[])
sorlund_road_a = scene_type(2,10,0,"the west road of Sorlund","","cloudy",True,False,False,False,False,True,False,0,"road","road_bt",False,False,"", "this road leads to the graveyard",[],[],[],[],[])
sorlund_road_b = scene_type(1,10,0,"the west road of Sorlund","","cloudy",True,False,False,False,False,True,False,0,"road","road_bt",False,False,"", "this road leads to the church",[],[],[],[],[])

sorlund_tavern = scene_type(2,11,0,"the Sorlund tavern","","cloudy",True,False,False,False,False,True,False,0,"town","",False,True,"", "A tavern",[],[],[],[],[])
sorlund_training_ground = scene_type(4,11,0,"the Sorlund combat academy","","cloudy",True,False,False,False,False,True,False,0,"town","",False,True,"", "the melee training ground for the Sorlund millita",[],[],[],[],[])

sorr_river_a = scene_type(0,9,0,"the river Sorr","","cloudy",True,False,False,False,False,False,False,0,"water","river_r",False,False,"The river is too deep to pass", "a wide river, i can't see the other side...",[],[],[],[],[])
sorr_river_b = scene_type(0,10,0,"the river Sorr","","cloudy",True,False,False,False,False,False,False,0,"water","river_r",False,False,"The river is too deep to pass", "a wide river, i can't see the other side...",[],[],[],[],[])
sorr_river_c = scene_type(0,11,0,"the river Sorr","","cloudy",True,False,False,False,False,False,False,0,"water","river_r",False,False,"The river is too deep to pass", "a wide river, i can't see the other side...",[],[],[],[],[])
sorr_river_d = scene_type(0,12,0,"the river Sorr","","cloudy",True,False,False,False,False,False,False,0,"water","river_r",False,False,"The river is too deep to pass", "a wide river, i can't see the other side...",[],[],[],[],[])
sorr_river_e = scene_type(0,13,0,"the river Sorr","","cloudy",True,False,False,False,False,False,False,0,"water","river_r",False,False,"The river is too deep to pass", "a wide river, i can't see the other side...",[],[],[],[],[])
sorr_river_f = scene_type(0,14,0,"the river Sorr","","cloudy",True,False,False,False,False,False,False,0,"water","river_r",False,False,"The river is too deep to pass", "a wide river, i can't see the other side...",[],[],[],[],[])
sorr_river_g = scene_type(0,15,0,"the river Sorr","","cloudy",True,False,False,False,False,False,False,0,"water","river_r",False,False,"The river is too deep to pass", "a wide river, i can't see the other side...",[],[],[],[],[])
sorr_river_bt = scene_type(0,16,0,"the river Sorr","","cloudy",True,False,False,False,False,False,False,0,"water","river_r",False,False,"The river is too deep to pass", "a wide river, i can't see the other side...",[],[],[],[],[])
sorr_river_i = scene_type(0,17,0,"the river Sorr","","cloudy",True,False,False,False,False,False,False,0,"water","river_r",False,False,"The river is too deep to pass", "a wide river, i can't see the other side...",[],[],[],[],[])
sorr_river_j = scene_type(0,18,0,"the river Sorr","","cloudy",True,False,False,False,False,False,False,0,"water","river_r",False,False,"The river is too deep to pass", "a wide river, i can't see the other side...",[],[],[],[],[])
sorr_river_k = scene_type(0,19,0,"the river Sorr","","cloudy",True,False,False,False,False,False,False,0,"water","river",False,False,"The river is too deep to pass", "a wide river, i can't see the other side...",[],[],[],[],[])

bottom_shore_1 = scene_type(1,19,0,"the bottom shore","","cloudy",True,False,False,False,False,False,False,0,"water","river_t",False,False,"The water is too deep", "a vast sea lies to the south...",[],[],[],[],[])
bottom_shore_2 = scene_type(2,19,0,"the bottom shore","","cloudy",True,False,False,False,False,False,False,0,"water","river_t",False,False,"The water is too deep", "a vast sea lies to the south...",[],[],[],[],[])
bottom_shore_3 = scene_type(3,19,0,"the bottom shore","","cloudy",True,False,False,False,False,False,False,0,"water","river_t",False,False,"The water is too deep", "a vast sea lies to the south...",[],[],[],[],[])
bottom_shore_4 = scene_type(4,19,0,"the bottom shore","","cloudy",True,False,False,False,False,False,False,0,"water","river_t",False,False,"The water is too deep", "a vast sea lies to the south...",[],[],[],[],[])
bottom_shore_5 = scene_type(5,19,0,"the bottom shore","","cloudy",True,False,False,False,False,False,False,0,"water","river_t",False,False,"The water is too deep", "a vast sea lies to the south...",[],[],[],[],[])
bottom_shore_6 = scene_type(6,19,0,"the bottom shore","","cloudy",True,False,False,False,False,False,False,0,"water","river_t",False,False,"The water is too deep", "a vast sea lies to the south...",[],[],[],[],[])
bottom_shore_7 = scene_type(7,19,0,"the bottom shore","","cloudy",True,False,False,False,False,False,False,0,"water","river_t",False,False,"The water is too deep", "a vast sea lies to the south...",[],[],[],[],[])
bottom_shore_8 = scene_type(8,19,0,"the bottom shore","","cloudy",True,False,False,False,False,False,False,0,"water","river_t",False,False,"The water is too deep", "a vast sea lies to the south...",[],[],[],[],[])
bottom_shore_9 = scene_type(9,19,0,"the bottom shore","","cloudy",True,False,False,False,False,False,False,0,"water","river_tr",False,False,"The water is too deep", "a vast sea lies to the south...",[],[],[],[],[])

bottom_shore_10 = scene_type(10,20,0,"the bottom shore","","cloudy",True,False,False,False,False,False,False,0,"water","river_t",False,False,"The water is too deep", "a vast sea lies to the south...",[],[],[],[],[])
bottom_shore_11 = scene_type(11,20,0,"the bottom shore","","cloudy",True,False,False,False,False,False,False,0,"water","river_t",False,False,"The water is too deep", "a vast sea lies to the south...",[],[],[],[],[])
bottom_shore_12 = scene_type(12,20,0,"the bottom shore","","cloudy",True,False,False,False,False,False,False,0,"water","river_t",False,False,"The water is too deep", "a vast sea lies to the south...",[],[],[],[],[])
bottom_shore_13 = scene_type(13,20,0,"the bottom shore","","cloudy",True,False,False,False,False,False,False,0,"water","river_t",False,False,"The water is too deep", "a vast sea lies to the south...",[],[],[],[],[])
bottom_shore_14 = scene_type(14,20,0,"the bottom shore","","cloudy",True,False,False,False,False,False,False,0,"water","river_t",False,False,"The water is too deep", "a vast sea lies to the south...",[],[],[],[],[])
bottom_shore_15 = scene_type(15,20,0,"the bottom shore","","cloudy",True,False,False,False,False,False,False,0,"water","river_t",False,False,"The water is too deep", "a vast sea lies to the south...",[],[],[],[],[])
bottom_shore_16 = scene_type(16,20,0,"the bottom shore","","cloudy",True,False,False,False,False,False,False,0,"water","river_t",False,False,"The water is too deep", "a vast sea lies to the south...",[],[],[],[],[])
bottom_shore_16 = scene_type(17,20,0,"the bottom shore","","cloudy",True,False,False,False,False,False,False,0,"water","river_t",False,False,"The water is too deep", "a vast sea lies to the south...",[],[],[],[],[])

south_plains_1 = scene_type(10,19,0,"the southern plains","","cloudy",True,False,False,False,False,True,False,0,"grassy","",False,False,"you cant get past", "a vast sea lies to the south...",[],[],[],[],[])
south_plains_2 = scene_type(11,19,0,"the southern plains","","cloudy",True,False,False,False,False,True,False,0,"grassy","",False,False,"you cant get past", "a vast sea lies to the south...",[],[],[],[],[])
south_plains_3 = scene_type(12,19,0,"the southern plains","","cloudy",True,False,False,False,False,True,False,0,"grassy","",False,False,"you cant get past", "a vast sea lies to the south...",[],[],[],[],[])
south_plains_4 = scene_type(13,19,0,"the southern plains","","cloudy",True,False,False,False,False,True,False,0,"grassy","",False,False,"you cant get past", "a vast sea lies to the south...",[],[],[],[],[])
south_plains_5 = scene_type(14,19,0,"the southern plains","","cloudy",True,False,False,False,False,True,False,0,"grassy","",False,False,"you cant get past", "a vast sea lies to the south...",[],[],[],[],[])
south_plains_6 = scene_type(15,19,0,"the southern plains","","cloudy",True,False,False,False,False,True,False,0,"grassy","",False,False,"you cant get past", "a vast sea lies to the south...",[],[],[],[],[])
south_plains_7 = scene_type(16,19,0,"the southern plains","","cloudy",True,False,False,False,False,True,False,0,"grassy","",False,False,"you cant get past", "a vast sea lies to the south...",[],[],[],[],[])
south_plains_8 = scene_type(17,19,0,"the southern plains","","cloudy",True,False,False,False,False,True,False,0,"grassy","",False,False,"you cant get past", "a vast sea lies to the south...",[],[],[],[],[])

south_plains_9 = scene_type(10,18,0,"the southern plains","","cloudy",True,False,False,False,False,True,False,0,"grassy","",False,False,"you cant get past", "windy plains...",[],[],[],[],[])
south_plains_9 = scene_type(11,18,0,"the southern plains","","cloudy",True,False,False,False,False,True,False,0,"grassy","",False,False,"you cant get past", "windy plains...",[],[],[],[],[])
south_plains_9 = scene_type(12,18,0,"the southern plains","","cloudy",True,False,False,False,False,True,False,0,"grassy","",False,False,"you cant get past", "windy plains...",[],[],[],[],[])
south_plains_9 = scene_type(13,18,0,"the southern plains","","cloudy",True,False,False,False,False,True,False,0,"grassy","",False,False,"you cant get past", "windy plains...",[],[],[],[],[])
south_plains_9 = scene_type(14,18,0,"the southern plains","","cloudy",True,False,False,False,False,False,False,0,"grassy","",False,False,"you cant get past", "windy plains...",[],[],[],[],[])
south_plains_9 = scene_type(15,18,0,"the southern plains","","cloudy",True,False,False,False,False,True,False,0,"grassy","",False,False,"you cant get past", "windy plains...",[],[],[],[],[])
south_plains_9 = scene_type(16,18,0,"the southern plains","","cloudy",True,False,False,False,False,True,False,0,"grassy","",False,False,"you cant get past", "windy plains...",[],[],[],[],[])
south_plains_9 = scene_type(17,18,0,"the southern plains","","cloudy",True,False,False,False,False,True,False,0,"grassy","",False,False,"you cant get past", "windy plains...",[],[],[],[],[])

south_road_1 = scene_type(4,17,0,"the south road","","cloudy",True,False,False,False,False,True,False,0,"road","road_bl",False,False,"", "this road continues from the crossroads to the south west",[],[],[],[],[])
south_road_2 = scene_type(5,17,0,"the south road","","cloudy",True,False,False,False,False,True,False,0,"road","road_bt",False,False,"", "this road continues from the crossroads to the south west",[],[],[],[],[])
south_road_3 = scene_type(6,17,0,"the south road","","cloudy",True,False,False,False,False,True,False,0,"road","road_bt",False,False,"", "this road continues from the crossroads to the south west",[],[],[],[],[])
south_road_4 = scene_type(7,17,0,"the south road","","cloudy",True,False,False,False,False,True,False,0,"road","road_bt",False,False,"", "this road continues from the crossroads to the south west",[],[],[],[],[])
south_road_5 = scene_type(8,17,0,"the south road","","cloudy",True,False,False,False,False,True,False,0,"road","road_bt",False,False,"", "this road continues from the crossroads to the south west",[],[],[],[],[])
south_road_6 = scene_type(9,17,0,"the south road","","cloudy",True,False,False,False,False,True,False,0,"road","road_bt",False,False,"", "this road continues from the crossroads to the south west",[],[],[],[],[])
south_road_7 = scene_type(10,17,0,"the south road","","cloudy",True,False,False,False,False,True,False,0,"road","road_bt",False,False,"", "this road continues from the crossroads to the south west",[],[],[],[],[])
south_road_8 = scene_type(11,17,0,"the south road","","cloudy",True,False,False,False,False,True,False,0,"road","road_bt",False,False,"", "this road continues from the crossroads to the south west",[],[],[],[],[])
south_road_9 = scene_type(12,17,0,"the south road","","cloudy",True,False,False,False,False,True,False,0,"road","road_bt",False,False,"", "this road continues from the crossroads to the south west",[],[],[],[],[])
south_road_10 = scene_type(13,17,0,"the south road","","cloudy",True,False,False,False,False,True,False,0,"road","road_bt",False,False,"", "this road continues from the crossroads to the south west",[],[],[],[],[])
south_road_11 = scene_type(14,17,0,"the south road","","cloudy",True,False,False,False,False,True,False,0,"road","road_bt",False,False,"", "this road continues from the crossroads to the south west",[],[],[],[],[])
south_road_12 = scene_type(15,17,0,"the south road","","cloudy",True,False,False,False,False,True,False,0,"road","road_bt",False,False,"", "this road continues from the crossroads to the south west",[],[],[],[],[])
south_road_13 = scene_type(16,17,0,"the south road","","cloudy",True,False,False,False,False,True,False,0,"road","road_bt",False,False,"", "this road continues from the crossroads to the south west",[],[],[],[],[])



# south east cave
cave_entrance = scene_type(6,9,0,"a cave entrance","","cloudy",True,False,False,False,False,True,False,0,"grassy","",True,False,"", "there is a cave enterance in the ground here, looks like it goes straight down",[],[],[],[],[])

cavern_a = scene_type(6,9,-9,"the center of a cavern","","cloudy",True,False,False,False,False,True,False,0,"cave","",False,False,"", "there is light coming from above...",[],[],[],[],[])
cavern_b = scene_type(6,8,-9,"a cavern","","cloudy",False,False,False,False,False,True,False,100,"cave","",False,False,"", "",[],[],[],[],[])
cavern_c = scene_type(6,10,-9,"a cavern","","cloudy",False,False,False,False,False,True,False,100,"cave","",False,False,"", "",[],[],[],[],[])
cavern_d = scene_type(5,8,-9,"a cavern","","cloudy",False,False,False,False,False,True,False,100,"cave","",False,False,"", "",[],[],[],[],[])
cavern_e = scene_type(5,9,-9,"a cavern","","cloudy",False,False,False,False,False,True,False,100,"cave","",False,False,"", "",[],[],[],[],[])
cavern_f = scene_type(5,10,-9,"a cavern","","cloudy",False,False,False,False,False,True,False,100,"cave","",False,False,"", "",[],[],[],[],[])
cavern_g = scene_type(7,8,-9,"a cavern","","cloudy",False,False,False,False,False,True,False,100,"cave","",False,False,"", "",[],[],[],[],[])
cavern_h = scene_type(7,9,-9,"a cavern","","cloudy",False,False,False,False,False,True,False,100,"cave","",False,False,"", "",[],[],[],[],[])
cavern_i = scene_type(7,10,-9,"a cavern","","cloudy",False,False,False,False,False,True,False,100,"cave","",False,False,"", "",[],[],[],[],[])

### north cave
north_cave_entrance = scene_type(3,1,0,"a cave entrance","","cloudy",True,False,False,False,False,True,False,0,"grassy","",True,False,"", "there is a cave enterance in the ground here, looks like it goes straight down",[],[],[],[],[])

# underground tunnel
tunnel_a = scene_type(3,1,-9,"an underground tunnel","","cloudy",False,False,False,False,False,True,False,62,"cave","",False,False,"", "there is a very faint light coming from above...",[],[],[],[],[])
tunnel_b = scene_type(4,1,-9,"an underground tunnel","","cloudy",False,False,False,False,False,True,False,62,"cave","",False,False,"", "this is an ancient tunnel, i wonder why it's here",[],[],[],[],[])
tunnel_c = scene_type(5,1,-9,"an underground tunnel","","cloudy",False,False,False,False,False,True,False,62,"cave","",False,False,"", "there are carvings on the wall, they depict goblins fighting some kind of demonic creature.",[],[],[],[],[])
tunnel_d = scene_type(6,1,-9,"an underground tunnel","","cloudy",False,False,False,False,False,True,False,62,"cave","",False,False,"", "there are carvings of goblins and humans massed in a large army, 2",[],[],[],[],[])

tunnel_e = scene_type(6,2,-9,"an underground tunnel","","cloudy",False,False,False,False,False,True,False,62,"cave","",False,False,"", "this is an ancient tunnel, i wonder why it's here",[],[],[],[],[])
tunnel_f = scene_type(6,3,-9,"an underground tunnel","","cloudy",False,False,False,False,False,True,False,62,"cave","",False,False,"", "this is an ancient tunnel, carvings depict a three headed dragon fighting a large demon",[],[],[],[],[])
tunnel_g = scene_type(6,4,-9,"an underground tunnel","","cloudy",False,False,False,False,False,True,False,62,"cave","",False,False,"", "this is an ancient tunnel, skeletons of ancient warriors line the walls here",[],[],[],[],[])
tunnel_h = scene_type(6,5,-9,"an underground tunnel","","cloudy",False,False,False,False,False,True,False,62,"cave","",False,False,"", "this is an ancient tunnel",[],[],[],[],[])
tunnel_i = scene_type(6,6,-9,"an underground tunnel","","cloudy",False,False,False,False,False,True,False,62,"cave","",False,False,"", "this is an ancient tunnel, it smells of decay",[],[],[],[],[])
tunnel_j = scene_type(6,7,-9,"an underground tunnel","","cloudy",False,False,False,False,False,True,False,62,"cave","",False,False,"", "this is an ancient tunnel, the air is still",[],[],[],[],[])
tunnel_k = scene_type(6,8,-9,"an underground tunnel","","cloudy",False,False,False,False,False,True,False,62,"cave","",False,False,"", "this is an ancient tunnel, it's carved from solid rock",[],[],[],[],[])

tunnel_l = scene_type(3,5,-9,"an underground tunnel","","cloudy",False,False,False,False,False,True,False,62,"cave","",False,False,"", "this is an ancient tunnel, it's carved from solid rock",[],[],[],[],[])
tunnel_m = scene_type(4,5,-9,"an underground tunnel","","cloudy",False,False,False,False,False,True,False,62,"cave","",False,False,"", "this is an ancient tunnel, it's carved from solid rock",[],[],[],[],[])
tunnel_n = scene_type(5,5,-9,"an underground tunnel","","cloudy",False,False,False,False,False,True,False,62,"cave","",False,False,"", "this is an ancient tunnel, it's carved from solid rock",[],[],[],[],[])

cavern_j = scene_type(2,5,-9,"a misty cavern","","cloudy",False,False,False,False,False,True,False,61,"cave","",False,False,"", "",[],[],[],[],[])
cavern_k = scene_type(2,4,-9,"a misty cavern","","cloudy",False,False,False,False,False,True,True,61,"cave","",False,False,"", "",[],[],[],[],[])
cavern_l = scene_type(1,5,-9,"a misty cavern","","cloudy",False,False,False,False,False,True,True,61,"cave","",False,False,"", "",[],[],[],[],[])
cavern_m = scene_type(2,6,-9,"a misty cavern","","cloudy",False,False,False,False,False,True,True,61,"cave","",False,False,"", "",[],[],[],[],[])


###--  UNIQUE IMPASSABLE TERRAIN  --###
cliffs_10000 = scene_type(-1,-1,0,"waterfall","","",False,False,False,False,False,False,False,0,"water","waterfall",False,False,"a waterfall blocks your path","",[],[],[],[],[])

cliffs_0 = scene_type(0,-1,0,"cliffs","","",False,False,False,False,False,False,False,0,"cliffs","",False,False,"cliffs block your path","",[],[],[],[],[])
cliffs_1 = scene_type(1,-1,0,"cliffs","","",False,False,False,False,False,False,False,0,"cliffs","",False,False,"cliffs block your path","",[],[],[],[],[])
cliffs_2 = scene_type(2,-1,0,"cliffs","","",False,False,False,False,False,False,False,0,"cliffs","",False,False,"cliffs block your path","",[],[],[],[],[])
cliffs_3 = scene_type(3,-1,0,"cliffs","","",False,False,False,False,False,False,False,0,"cliffs","",False,False,"cliffs block your path","",[],[],[],[],[])
cliffs_4 = scene_type(4,-1,0,"cliffs","","",False,False,False,False,False,False,False,0,"cliffs","",False,False,"cliffs block your path","",[],[],[],[],[])
cliffs_5 = scene_type(5,-1,0,"cliffs","","",False,False,False,False,False,False,False,0,"cliffs","",False,False,"cliffs block your path","",[],[],[],[],[])
cliffs_6 = scene_type(6,-1,0,"cliffs","","",False,False,False,False,False,False,False,0,"cliffs","",False,False,"cliffs block your path","",[],[],[],[],[])
cliffs_7 = scene_type(7,-1,0,"cliffs","","",False,False,False,False,False,False,False,0,"cliffs","",False,False,"cliffs block your path","",[],[],[],[],[])

cliffs_8 = scene_type(8,-1,0,"cliffs","","",False,False,False,False,False,False,False,0,"cliffs","",False,False,"cliffs block your path","",[],[],[],[],[])
cliffs_9 = scene_type(9,-1,0,"cliffs","","",False,False,False,False,False,False,False,0,"cliffs","",False,False,"cliffs block your path","",[],[],[],[],[])
cliffs_10 = scene_type(10,-1,0,"cliffs","","",False,False,False,False,False,False,False,0,"cliffs","",False,False,"cliffs block your path","",[],[],[],[],[])
cliffs_11 = scene_type(11,-1,0,"cliffs","","",False,False,False,False,False,False,False,0,"cliffs","",False,False,"cliffs block your path","",[],[],[],[],[])
cliffs_12 = scene_type(12,-1,0,"cliffs","","",False,False,False,False,False,False,False,0,"cliffs","",False,False,"cliffs block your path","",[],[],[],[],[])
cliffs_13 = scene_type(13,-1,0,"cliffs","","",False,False,False,False,False,False,False,0,"cliffs","",False,False,"cliffs block your path","",[],[],[],[],[])
cliffs_14 = scene_type(14,-1,0,"cliffs","","",False,False,False,False,False,False,False,0,"cliffs","",False,False,"cliffs block your path","",[],[],[],[],[])

north_river_sorr_a = scene_type(-1,0,0,"river sorr","","",False,False,False,False,False,False,False,0,"water","river_r",False,False,"water block your path","",[],[],[],[],[])
north_river_sorr_b = scene_type(0,1,0,"river sorr","","",False,False,False,False,False,False,False,0,"water","river_tr",False,False,"water block your path","",[],[],[],[],[])
north_river_sorr_c = scene_type(0,2,0,"river sorr","","",False,False,False,False,False,False,False,0,"water","river_r",False,False,"water block your path","",[],[],[],[],[])
north_river_sorr_d = scene_type(0,3,0,"river sorr","","",False,False,False,False,False,False,False,0,"water","river_r",False,False,"water block your path","",[],[],[],[],[])
north_river_sorr_e = scene_type(0,4,0,"river sorr","","",False,False,False,False,False,False,False,0,"water","river_r",False,False,"water block your path","",[],[],[],[],[])
north_river_sorr_f = scene_type(0,5,0,"river sorr","","",False,False,False,False,False,False,False,0,"water","river_r",False,False,"water block your path","",[],[],[],[],[])

north_river_sorr_f = scene_type(0,5,0,"river sorr","","",False,False,False,False,False,False,False,0,"water","river_r",False,False,"water block your path","",[],[],[],[],[])
north_river_sorr_f = scene_type(0,5,0,"river sorr","","",False,False,False,False,False,False,False,0,"water","river_r",False,False,"water block your path","",[],[],[],[],[])


north_shore_1 = scene_type(1,-2,0,"north shore","","",False,False,False,False,False,False,False,0,"water","river_b",False,False,"water blocks your path","",[],[],[],[],[])
north_shore_3 = scene_type(2,-2,0,"north shore","","",False,False,False,False,False,False,False,0,"water","river_b",False,False,"water blocks your path","",[],[],[],[],[])
north_shore_4 = scene_type(3,-2,0,"north shore","","",False,False,False,False,False,False,False,0,"water","river_b",False,False,"water blocks your path","",[],[],[],[],[])
north_shore_5 = scene_type(4,-2,0,"north shore","","",False,False,False,False,False,False,False,0,"water","river_b",False,False,"water lake blocks your path","",[],[],[],[],[])
north_shore_6 = scene_type(5,-2,0,"north shore","","",False,False,False,False,False,False,False,0,"water","river_b",False,False,"water lake blocks your path","",[],[],[],[],[])
north_shore_7 = scene_type(6,-2,0,"north shore","","",False,False,False,False,False,False,False,0,"water","river_b",False,False,"water lake blocks your path","",[],[],[],[],[])

north_shore_8 = scene_type(0,-2,0,"north shore","","",False,False,False,False,False,False,False,0,"water","river_b",False,False,"water lake blocks your path","",[],[],[],[],[])
north_shore_9 = scene_type(-1,-2,0,"north shore","","",False,False,False,False,False,False,False,0,"water","river",False,False,"water lake blocks your path","",[],[],[],[],[])

north_shore_10 = scene_type(7,-2,0,"north shore","","",False,False,False,False,False,False,False,0,"water","river_b",False,False,"water lake blocks your path","",[],[],[],[],[])
north_shore_11 = scene_type(8,-2,0,"north shore","","",False,False,False,False,False,False,False,0,"water","river_b",False,False,"water lake blocks your path","",[],[],[],[],[])
north_shore_12 = scene_type(9,-2,0,"north shore","","",False,False,False,False,False,False,False,0,"water","river_b",False,False,"water lake blocks your path","",[],[],[],[],[])
north_shore_13 = scene_type(10,-2,0,"north shore","","",False,False,False,False,False,False,False,0,"water","river_b",False,False,"water lake blocks your path","",[],[],[],[],[])
north_shore_14 = scene_type(11,-2,0,"north shore","","",False,False,False,False,False,False,False,0,"water","river_b",False,False,"water lake blocks your path","",[],[],[],[],[])
north_shore_15 = scene_type(12,-2,0,"north shore","","",False,False,False,False,False,False,False,0,"water","river_b",False,False,"water lake blocks your path","",[],[],[],[],[])
north_shore_16 = scene_type(13,-2,0,"north shore","","",False,False,False,False,False,False,False,0,"water","river_b",False,False,"water lake blocks your path","",[],[],[],[],[])
north_shore_17 = scene_type(14,-2,0,"north shore","","",False,False,False,False,False,False,False,0,"water","river_b",False,False,"water lake blocks your path","",[],[],[],[],[])
north_shore_18 = scene_type(15,-2,0,"north shore","","",False,False,False,False,False,False,False,0,"water","river_b",False,False,"water lake blocks your path","",[],[],[],[],[])



lake_a = scene_type(0,7,0,"lake","","",False,False,False,False,False,False,False,0,"water","river",False,False,"a deep lake blocks your path","",[],[],[],[],[])
lake_b = scene_type(1,7,0,"lake","","",False,False,False,False,False,False,False,0,"water","river_t",False,False,"a deep lake blocks your path","",[],[],[],[],[])
lake_c = scene_type(0,8,0,"lake","","",False,False,False,False,False,False,False,0,"water","river",False,False,"a deep lake blocks your path","",[],[],[],[],[])
lake_d = scene_type(1,8,0,"lake","","",False,False,False,False,False,False,False,0,"water","river_br",False,False,"a deep lake blocks your path","",[],[],[],[],[])
lake_e = scene_type(0,6,0,"lake","","",False,False,False,False,False,False,False,0,"water","river_r",False,False,"a deep lake blocks your path","",[],[],[],[],[])

river_a = scene_type(2,7,0,"river","","",False,False,False,False,False,False,False,0,"water","river_bt",False,False,"a river blocks your path","",[],[],[],[],[])
river_b = scene_type(3,7,0,"river","","",False,False,False,False,False,False,False,0,"water","river_bt",False,False,"a river blocks your path","",[],[],[],[],[])
river_c = scene_type(4,7,0,"river","","",False,False,False,False,False,False,False,0,"water","river_bt",False,False,"a river blocks your path","",[],[],[],[],[])
river_d = scene_type(5,7,0,"river","","",False,False,False,False,False,False,False,0,"water","river_bt",False,False,"a river blocks your path","",[],[],[],[],[])
river_e = scene_type(7,7,0,"river","","",False,False,False,False,False,False,False,0,"water","river_bt",False,False,"a river blocks your path","",[],[],[],[],[])
river_f = scene_type(8,7,0,"river","","",False,False,False,False,False,False,False,0,"water","river_bt",False,False,"a river blocks your path","",[],[],[],[],[])
river_g = scene_type(9,7,0,"river","","",False,False,False,False,False,False,False,0,"water","river_bt",False,False,"a river blocks your path","",[],[],[],[],[])
river_bt = scene_type(10,7,0,"river","","",False,False,False,False,False,False,False,0,"water","river_bt",False,False,"a river blocks your path","",[],[],[],[],[])
river_i = scene_type(11,7,0,"river","","",False,False,False,False,False,False,False,0,"water","river_bt",False,False,"a river blocks your path","",[],[],[],[],[])
river_j = scene_type(12,7,0,"river","","",False,False,False,False,False,False,False,0,"water","river_bt",False,False,"a river blocks your path","",[],[],[],[],[])
river_k = scene_type(13,7,0,"river","","",False,False,False,False,False,False,False,0,"water","river_bt",False,False,"a river blocks your path","",[],[],[],[],[])
river_l = scene_type(14,7,0,"river","","",False,False,False,False,False,False,False,0,"water","river_tr",False,False,"a river blocks your path","",[],[],[],[],[])
river_m = scene_type(14,8,0,"river","","",False,False,False,False,False,False,False,0,"water","river_bl",False,False,"a river blocks your path","",[],[],[],[],[])
river_n = scene_type(15,8,0,"river","","",False,False,False,False,False,False,False,0,"water","river_bt",False,False,"a river blocks your path","",[],[],[],[],[])
river_o = scene_type(16,8,0,"river","","",False,False,False,False,False,False,False,0,"water","river_bt",False,False,"a river blocks your path","",[],[],[],[],[])
river_p = scene_type(17,8,0,"river","","",False,False,False,False,False,False,False,0,"water","river_bt",False,False,"a river blocks your path","",[],[],[],[],[])
river_p = scene_type(18,8,0,"river","","",False,False,False,False,False,False,False,0,"water","river_bt",False,False,"a river blocks your path","",[],[],[],[],[])

###--  IMPASSABLE TERRAIN  --###


ocean = scene_type(999,999,999,"the ocean","","",False,False,False,False,False,False,False,0,"seaside","",False,False,"the ocean blocks your escape","",[],[],[],[],[])

solid_cave_wall = scene_type(998,998,998,"a solid cave wall","","",False,False,False,False,False,False,False,0,"dirt","",False,False,"a sheer wall of rock blocks your path","",[],[],[],[],[])
solid_cave_ground = scene_type(997,997,997,"a solid cave floor","","",False,False,False,False,False,False,False,0,"dirt","",False,False,"a floor of rock blocks your path","",[],[],[],[],[])
ground = scene_type(996,996,996,"the ground","","",False,False,False,False,False,False,False,0,"dirt","",False,False,"the ground blocks your path","",[],[],[],[],[])
sky = scene_type(995,995,995,"the sky","","",False,False,False,False,False,False,False,0,"seaside","",False,False,"you cannot fly","",[],[],[],[],[])
solid_dungeon_wall = scene_type(994,994,994,"a solid dungeon wall","","",False,False,False,False,False,False,False,0,"dirt","",False,False,"a wall of stone brick blocks your path","",[],[],[],[],[])
solid_dungeon_ground = scene_type(993,993,993,"a solid dungeon floor","","",False,False,False,False,False,False,False,0,"dirt","",False,False,"a floor of stone brick blocks your path","",[],[],[],[],[])
