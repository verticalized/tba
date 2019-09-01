import random
from time import sleep
from colorama import init
from colorama import Fore, Back, Style

init(autoreset=True)

from objectImportTest import *

from scene_module import *

object_list = []
object_list.append(object001)
for object in object_list:
    print(object.name)

###########################----GLOBAL_VARIABLES-----####################

version = "1.8"

dev_mode = 0
check_for_combat = True
restock_shops = True
restock_ticks = 0

steps_x = 0
steps_y = 0
steps_z = 0

###########################################

prev_x = 0
prev_y = 0
prev_z = 0

npc_fight = False
npc_enemy_fname = "0"
npc_enemy_lname = "0"

in_fight = False

val = 999 #spell selection value
val_npc = 999 #selection value
val_enemy = 999 #selection value
val_dialouge = 999 #selection value
val_shop = 999 #selection value
val_drop = 999 #selection value
val_sell = 999 #selection value



if dev_mode >= 1:
    sleep_time = 0
    sleep_time_fast = 0
    sleep_time_slow = 0
else:
    sleep_time = 0.1
    sleep_time_fast = 0.1
    sleep_time_slow = 0.1

raining = 1
weather = 0
season = 3 # value from 0,3 that determines season

time = 0
days = 19
months = 4
years = 1567

all_npcs = []
all_scene_types = []
all_game_items = []
all_ground_game_items = []
all_game_weapons = []
all_ground_game_weapons = []
all_game_armor = []
all_ground_game_armor = []
all_game_helmets = []
all_ground_game_helmets = []
all_game_shields = []
all_ground_game_shields = []

all_game_spells = []

default_drop_table_items = []
default_drop_table_weapons = []
default_drop_table_armor = []

###########################------COLOUR_VARIABLES-------#############################

colour_reset = (Style.RESET_ALL) # resest colour

colour_scene_name = (Fore.GREEN + Style.DIM) # text colours for scene variables

colour_scene_temp = (Fore.MAGENTA + Style.DIM)

colour_scene_light_day = (Fore.BLUE + Style.BRIGHT)
colour_scene_light_night = (Fore.BLUE + Style.DIM)

colour_item_name = (Fore.BLACK + Style.BRIGHT) # text colour for all item names

colour_gear_name = (Fore.CYAN + Style.DIM) # text colour for all gear names
colour_spell_name = (Fore.CYAN + Style.NORMAL) # text colour

colour_enemy_name = (Fore.RED + Style.DIM) # text colour

colour_misc_name = (Fore.BLACK + Style.BRIGHT) # misc. text colour

colour_attribute = (Fore.BLACK + Style.BRIGHT) # misc. text colour

###########################------CLASSES------#########################

# to do list:

# add quest class and make bandit quest
# more enemies
# more spells
# make more locations, dungeons, undeground areas



class scene_type:
    def __init__(self, xpos, ypos, zpos, name, temp, light, safe, can_fish, can_cook, can_craft, can_steal, passable, treasure, difficulty, biome, has_stairs, indoors, impass_msg, flavour, scene_inventory, scene_weapon_inventory, scene_armor_inventory, scene_helmet_inventory, scene_shield_inventory):
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
        self.has_stairs = has_stairs
        self.indoors = indoors
        self.impass_msg = impass_msg
        self.flavour = flavour
        self.scene_inventory = scene_inventory
        self.scene_weapon_inventory = scene_weapon_inventory
        self.scene_armor_inventory = scene_armor_inventory
        self.scene_helmet_inventory = scene_helmet_inventory
        self.scene_shield_inventory = scene_shield_inventory

        self.npc_list = []

        if self.biome == "seaside":
            self.name = (Fore.CYAN + Style.NORMAL + name + Style.RESET_ALL)
        elif self.biome == "water":
            self.name = (Fore.BLUE + Style.NORMAL + name + Style.RESET_ALL)
        elif self.biome == "forest":
            self.name = (Fore.GREEN + Style.NORMAL + name + Style.RESET_ALL)
        elif self.biome == "town":
            self.name = (Fore.BLACK + Style.BRIGHT + name + Style.RESET_ALL)
        elif self.biome == "sandy":
            self.name = (Fore.YELLOW + Style.NORMAL + name + Style.RESET_ALL)
        elif self.biome == "grassy":
            self.name = (Fore.GREEN + Style.DIM + name + Style.RESET_ALL)
        elif self.biome == "snow":
            self.name = (Fore.WHITE + Style.BRIGHT + name + Style.RESET_ALL)
        elif self.biome == "cave":
            self.name = (Fore.MAGENTA + Style.DIM + name + Style.RESET_ALL)
        elif self.biome == "ground":
            self.name = (Fore.BLACK + Style.BRIGHT + name + Style.RESET_ALL)
        else:
            self.name = (Fore.RED + Style.DIM + name + Style.RESET_ALL)
        all_scene_types.append(self)

hills = scene_type(0,0,0,"the hills","temperate","sunny",True,False,False,False,False,True,False,0,"forest",False,False,"","rolling green hills",[],[],[],[],[])
lakeside = scene_type(0,-1,0,"lakeside","temperate","sunny",True,False,False,False,False,True,False,0,"forest",False,False,"","the shore of the lake",[],[],[],[],[])

#large tree cave
large_tree = scene_type(1,0,0,"a large tree","temperate","shady",True,False,False,False,True,True,False,0,"forest",True,False,"","a very, very large oak tree",[],[],[],[],[])
large_tree_tunnel_a = scene_type(1,0,-1,"a tunnel","temperate","shady",True,False,False,False,False,True,False,0,"forest",True,False,"","there are tree roots supporting the tunnel",[],[],[],[],[])
large_tree_tunnel_b = scene_type(1,0,-2,"a tunnel ","temperate","shady",True,False,False,False,False,True,False,0,"forest",True,False,"","the tunnel goes down quite far",[],[],[],[],[])
large_tree_cave_a = scene_type(1,0,-3,"oak tree cave","temperate","shady",False,False,False,False,False,True,False,1,"forest",True,False,"","a cave below the large oak tree",[],[],[],[],[])
large_tree_cave_b = scene_type(0,0,-3,"oak tree cave","temperate","shady",False,False,False,False,False,True,False,1,"forest",False,False,"","a cave below the large oak tree",[],[],[],[],[])
large_tree_cave_c = scene_type(0,-1,-3,"oak tree cave","temperate","shady",False,False,False,False,False,True,False,1,"forest",False,False,"","a cave below the large oak tree",[],[],[],[],[])
large_tree_cave_d = scene_type(0,-2,-3,"oak tree cave","temperate","shady",False,False,False,False,False,True,False,1,"forest",False,False,"","a cave below the large oak tree",[],[],[],[],[])
large_tree_cave_e = scene_type(0,-3,-3,"oak tree cave","temperate","shady",False,False,False,False,False,True,False,1,"forest",False,False,"","a cave below the large oak tree",[],[],[],[],[])

large_tree_cave_door = scene_type(0,-4,-3,"oak doorway","temperate","shady",True,False,False,False,False,False,False,0,"forest",False,False,"this door is locked, you need a key..","The door is unlocked...",[],[],[],[],[])

large_tree_cave_f = scene_type(0,-5,-3,"oak tree cave","temperate","shady",True,False,False,False,False,True,True,0,"forest",False,False,"","a cave below the large oak tree",[],[],[],[],[])

birds_nest = scene_type(2,0,0,"a bird's nest","cosy","dimly lit",True,False,False,False,True,True,False,0,"forest",False,False,"","you are in a house made of twigs and branches",[],[],[],[],[])

forest_a = scene_type(3,0,0,"the dark forest","cold","shady",False,False,False,False,False,True,False,0,"forest",False,False,"","it's dark here",[],[],[],[],[])
forest_b = scene_type(3,1,0,"the dark forest","cold","shady",False,False,False,False,False,True,False,1,"forest",False,False,"","the smell of pine forest is very strong here",[],[],[],[],[])
forest_c = scene_type(4,0,0,"the dark forest","cold","shady",False,False,False,False,False,True,False,0,"forest",False,False,"","lots of trees...",[],[],[],[],[])
forest_d = scene_type(4,1,0,"the dark forest","cold","shady",False,False,False,False,False,True,False,1,"forest",False,False,"","there's a circle of rocks in a small clearing",[],[],[],[],[])
forest_e = scene_type(3,2,0,"the dark forest","cold","shady",False,False,False,False,False,True,False,0,"forest",False,False,"","small mushrooms litter the ground here",[],[],[],[],[])
forest_f = scene_type(2,1,0,"the dark forest","cold","shady",False,False,False,False,False,True,False,0,"forest",False,False,"","there is smoke to the north",[],[],[],[],[])
forest_g = scene_type(4,2,0,"the dark forest","cold","shady",False,False,False,False,False,True,False,0,"forest",False,False,"","",[],[],[],[],[])
forest_h = scene_type(4,-1,0,"the dark forest","cold","shady",False,False,False,False,False,True,False,0,"forest",False,False,"","the forest isn't so dense here",[],[],[],[],[])
forest_i = scene_type(3,-1,0,"the dark forest","cold","shady",False,False,False,False,False,True,False,0,"forest",False,False,"","",[],[],[],[],[])
forest_j = scene_type(2,-1,0,"the dark forest","cold","shady",False,False,False,False,False,True,False,0,"forest",False,False,"","",[],[],[],[],[])
forest_k = scene_type(1,-1,0,"the dark forest","cold","shady",False,False,False,False,False,True,False,0,"forest",False,False,"","",[],[],[],[],[])
forest_l = scene_type(1,1,0,"the dark forest","cold","shady",False,False,False,False,False,True,False,0,"forest",False,False,"","",[],[],[],[],[])
forest_m = scene_type(1,2,0,"the dark forest","cold","shady",False,False,False,False,False,True,False,0,"forest",False,False,"","",[],[],[],[],[])
forest_n = scene_type(2,3,0,"the dark forest","cold","shady",False,False,False,False,False,True,False,0,"forest",False,False,"","",[],[],[],[],[])

forest_cabin = scene_type(2,2,0,"the forest cabin","temperate","cloudy",True,False,False,False,True,True,False,0,"forest",False,False,"", "a nice log cabin, many strange objects are displayed on shelves and a large desk has piles of books next to it.",[],[],[],[],[])

grassland_a = scene_type(2,5,0,"grassland","cold","shady",False,False,False,False,False,True,False,0,"grassy",False,False,"","wide open space, lots of grass",[],[],[],[],[])
grassland_b = scene_type(1,5,0,"grassland","cold","shady",False,False,False,False,False,True,False,0,"grassy",False,False,"","wide open space, lots of grass",[],[],[],[],[])
grassland_c = scene_type(1,4,0,"grassland","cold","shady",False,False,False,False,False,True,False,0,"grassy",False,False,"","wide open space, lots of grass",[],[],[],[],[])
grassland_d = scene_type(1,3,0,"grassland","cold","shady",False,False,False,False,False,True,False,0,"grassy",False,False,"","wide open space, lots of grass",[],[],[],[],[])
grassland_e = scene_type(3,5,0,"grassland","cold","shady",False,False,False,False,False,True,False,0,"grassy",False,False,"","wide open space, lots of grass",[],[],[],[],[])
grassland_f = scene_type(3,4,0,"grassland","cold","shady",False,False,False,False,False,True,False,0,"grassy",False,False,"","wide open space, lots of grass",[],[],[],[],[])
grassland_g = scene_type(3,3,0,"grassland","cold","shady",False,False,False,False,False,True,False,0,"grassy",False,False,"","wide open space, lots of grass",[],[],[],[],[])

grassland_h = scene_type(6,-1,0,"grassland","cold","shady",False,False,False,False,False,True,False,0,"grassy",False,False,"","wide open space, lots of grass",[],[],[],[],[])
grassland_i = scene_type(7,-1,0,"grassland","cold","shady",False,False,False,False,False,True,False,0,"grassy",False,False,"","wide open space, lots of grass",[],[],[],[],[])

north_beach_a = scene_type(1,6,0,"the north beach","hot","sunny",True,True,False,False,True,True,False,0,"seaside",False,False,"","the ocean stretches off to the north",[],[],[],[],[])
north_beach_b = scene_type(2,6,0,"the north beach","hot","sunny",True,True,False,False,True,True,False,0,"seaside",False,False,"","the ocean stretches off to the north",[],[],[],[],[])
north_beach_c = scene_type(3,6,0,"the north beach","hot","sunny",True,True,False,False,True,True,False,0,"seaside",False,False,"","the ocean stretches off to the north",[],[],[],[],[])
north_beach_d = scene_type(4,5,0,"the north beach","hot","sunny",True,True,False,False,True,True,False,0,"seaside",False,False,"","the ocean stretches off to the north",[],[],[],[],[])
dismurth_docks_searocks = scene_type(6,5,0,"rocky shore","hot","sunny",True,True,False,False,True,True,False,0,"seaside",False,False,"","the ocean stretches off to the north and east, large waves are crashing against the rocks...",[],[],[],[],[])

crossroads = scene_type(5,0,0,"the crossroads","temperate","sunny",False,False,False,False,False,True,False,0,"forest",False,False,"","There is a sign pointing north labelled \' Dismurth \' ",[],[],[],[],[])
east_road = scene_type(6,0,0,"the east road","hot","sunny",False,False,False,False,False,True,False,0,"forest",False,False,"","this narrow road leads from the crossroads to the east",[],[],[],[],[])
north_road = scene_type(5,1,0,"the north road","hot","sunny",False,False,False,False,False,True,False,0,"forest",False,False,"","this road leads from the crossroads to the northern town of Dismurth, it looks well travelled",[],[],[],[],[])
dismurth_gates = scene_type(5,2,0,"the town gates of Dismurth","hot","sunny",True,False,False,False,True,True,False,0,"town",False,False,"","",[],[],[],[],[])
dismurth_square = scene_type(5,3,0,"the town square of Dismurth","hot","sunny",True,False,False,False,True,True,False,0,"town",False,False,"","",[],[],[],[],[])
dismurth_market = scene_type(5,4,0,"Dismurth markets","hot","sunny",True,False,False,False,True,True,False,0,"town",False,False,"","",[],[],[],[],[])
dismurth_tavern = scene_type(4,4,0,"Dismurth tavern","hot","sunny",True,False,False,False,True,True,False,0,"town",False,False,"","",[],[],[],[],[])
dismurth_docks = scene_type(5,5,0,"the docks of Dismurth","hot","sunny",True,True,False,False,True,True,False,0,"town",False,False,"","",[],[],[],[],[])
dismurth_tower_1f = scene_type(6,4,1,"the tower of Dismurth's first floor","hot","sunny",True,False,False,False,True,True,False,0,"town",True,True,"","the tower walls are lined with more bookshelves",[],[],[],[],[])
dismurth_tower_gf = scene_type(6,4,0,"the tower of Dismurth's ground floor","hot","sunny",True,False,False,False,True,True,False,0,"town",True,True,"","the tower walls are lined with bookshelves, there are many large runestones in the middle of the room",[],[],[],[],[])
dismurth_smith = scene_type(6,3,0,"the Blacksmith of Dismurth","hot","sunny",True,False,False,False,True,True,False,0,"town",False,False,"","*a young man is working hard at the furnace*",[],[],[],[],[])
dismurth_barracks = scene_type(4,3,0,"the Barracks of Dismurth","warm","dimly liy",True,False,False,False,True,True,False,0,"town",False,False,"","you are surrounded by bunks and weapon racks, there is a large table in the middle of the room, a fire crackles in the corner",[],[],[],[],[])
dismurth_farm = scene_type(6,2,0,"the Dismurth farmstead","hot","sunny",True,False,False,False,True,True,False,0,"grassy",False,False,"","",[],[],[],[],[])
rocky_shore_a = scene_type(8,3,0,"rocky shore","hot","sunny",True,True,False,False,False,True,False,0,"seaside",False,False,"","turnips bruzzy",[],[],[],[],[])
rocky_shore_b = scene_type(8,2,0,"rocky shore","hot","sunny",True,True,False,False,False,True,False,0,"seaside",False,False,"","turnips bruzzy",[],[],[],[],[])
dismurth_fisherman_house = scene_type(7,3,0,"fisherman's house","hot","sunny",True,False,False,False,True,True,False,0,"seaside",False,False,"","turnips bruzzy",[],[],[],[],[])
turnip_field = scene_type(7,2,0,"a turnip field","hot","sunny",True,False,False,False,True,True,False,0,"forest",False,False,"","turnips bruzzy",[],[],[],[],[])
highlands_a = scene_type(6,1,0,"highlands","humid","sunny",False,False,False,False,False,True,True,1,"grassy",False,False,"","grass and low stone walls form paddocks around you",[],[],[],[],[])
highlands_b = scene_type(7,1,0,"highlands","humid","sunny",False,False,False,False,False,True,True,1,"grassy",False,False,"","",[],[],[],[],[])

fortress_gate = scene_type(7,0,0,"the bandit fortress gates","humid","sunny",False,False,False,False,False,True,False,100,"forest",False,False,"","",[],[],[],[],[])
fortress = scene_type(8,0,0,"the bandit fortress","humid","sunny",False,False,False,False,False,True,True,100,"forest",False,False,""," surrounded by a palisade wall",[],[],[],[],[])
fort_wall_a = scene_type(8,1,0,"fortress wall","temp_string","light_string",False,False,False,False,False,False,False,0,"forest",False,False,"the large, wooden wall blocks your path","",[],[],[],[],[])
fort_wall_b = scene_type(8,-1,0,"fortress wall","temp_string","light_string",False,False,False,False,False,False,False,0,"forest",False,False,"the large, wooden wall blocks your path","",[],[],[],[],[])
fort_wall_c = scene_type(9,0,0,"fortress wall","temp_string","light_string",False,False,False,False,False,False,False,0,"forest",False,False,"the large, wooden wall blocks your path","",[],[],[],[],[])

highlands_c = scene_type(10,10,0,"highlands","humid","sunny",False,False,False,False,False,True,False,0,"forest",False,False,"","",[],[],[],[],[])

plains_a = scene_type(-1,2,0,"plains","humid","sunny",False,False,False,False,False,True,False,0,"forest",False,False,"","sandy plains",[],[],[],[],[])
plains_b = scene_type(-1,1,0,"plains","humid","sunny",False,False,False,False,False,True,False,0,"forest",False,False,"","sandy plains",[],[],[],[],[])
crags = scene_type(15,15,0,"crags","temperate","cloudy",False,False,False,False,False,True,False,0,"forest",False,False,"", "some particularly generic crags, very rocky indeed",[],[],[],[],[])
fields = scene_type(16,16,0,"ordinary fields","temperate","cloudy",False,False,False,False,False,True,False,0,"forest",False,False,"", "some particularly generic fields",[],[],[],[],[])
swamp = scene_type(17,17,0,"swamp","temperate","cloudy",False,False,False,False,False,True,False,0,"forest",False,False,"", "some particularly generic fields",[],[],[],[],[])

south_road_a = scene_type(5,-1,0,"the south road","temperate","cloudy",True,False,False,False,False,True,False,0,"town",False,False,"", "this road leads from the crossroads to the south ",[],[],[],[],[])
dismurth_bridge = scene_type(5,-2,0,"the Dismurth bridge","temperate","cloudy",True,False,False,False,False,True,False,0,"town",False,False,"you may not cross the bridge without rite of passage", "the river looks nice from here",[],[],[],[],[])
south_road_b = scene_type(5,-3,0,"the south road","temperate","cloudy",True,False,False,False,False,True,False,0,"town",False,False,"", "this road continues from the crossroads to the south",[],[],[],[],[])

#south east cave
cave_entrance = scene_type(5,-4,0,"a cave entrance","temperate","cloudy",True,False,False,False,False,True,False,0,"cave",False,False,"", "there is a cave enterance in the ground here, looks like it goes straight down",[],[],[],[],[])
cave_a = scene_type(5,-4,-1,"a cave","temperate","cloudy",True,False,False,False,False,True,False,0,"cave",False,False,"", "this cave goes down further...",[],[],[],[],[])
cave_b = scene_type(5,-4,-2,"a cave","temperate","cloudy",True,False,False,False,False,True,False,0,"cave",False,False,"", "this cave goes down further...",[],[],[],[],[])
cave_c = scene_type(5,-4,-3,"a cave","temperate","cloudy",True,False,False,False,False,True,False,0,"cave",False,False,"", "this cave goes down further...",[],[],[],[],[])
cave_d = scene_type(5,-4,-4,"a cave","temperate","cloudy",True,False,False,False,False,True,False,0,"cave",False,False,"", "this cave goes down further...",[],[],[],[],[])
cave_e = scene_type(5,-4,-5,"a cave","temperate","cloudy",True,False,False,False,False,True,False,0,"cave",False,False,"", "this cave goes down further...",[],[],[],[],[])
cave_f = scene_type(5,-4,-6,"a cave","temperate","cloudy",True,False,False,False,False,True,False,0,"cave",False,False,"", "this cave goes down further...",[],[],[],[],[])
cave_g = scene_type(5,-4,-7,"a cave","temperate","cloudy",True,False,False,False,False,True,False,0,"cave",False,False,"", "this cave goes down further...",[],[],[],[],[])
cave_h = scene_type(5,-4,-8,"a cave","temperate","cloudy",True,False,False,False,False,True,False,0,"cave",False,False,"", "there is a cavern below...",[],[],[],[],[])

cavern_a = scene_type(5,-4,-9,"the center of a cavern","temperate","cloudy",True,False,False,False,False,True,False,0,"cave",False,False,"", "there is light coming from above...",[],[],[],[],[])
cavern_b = scene_type(5,-3,-9,"a cavern","temperate","cloudy",False,False,False,False,False,True,False,1,"cave",False,False,"", "",[],[],[],[],[])
cavern_c = scene_type(5,-5,-9,"a cavern","temperate","cloudy",False,False,False,False,False,True,False,1,"cave",False,False,"", "",[],[],[],[],[])
cavern_d = scene_type(6,-3,-9,"a cavern","temperate","cloudy",False,False,False,False,False,True,False,1,"cave",False,False,"", "",[],[],[],[],[])
cavern_e = scene_type(4,-3,-9,"a cavern","temperate","cloudy",False,False,False,False,False,True,False,1,"cave",False,False,"", "",[],[],[],[],[])
cavern_f = scene_type(4,-4,-9,"a cavern","temperate","cloudy",False,False,False,False,False,True,False,1,"cave",False,False,"", "",[],[],[],[],[])
cavern_g = scene_type(4,-5,-9,"a cavern","temperate","cloudy",False,False,False,False,False,True,False,1,"cave",False,False,"", "",[],[],[],[],[])
cavern_h = scene_type(6,-4,-9,"a cavern","temperate","cloudy",False,False,False,False,False,True,False,1,"cave",False,False,"", "",[],[],[],[],[])
cavern_i = scene_type(6,-5,-9,"a cavern","temperate","cloudy",False,False,False,False,False,True,False,1,"cave",False,False,"", "",[],[],[],[],[])

###north cave
north_cave_entrance = scene_type(2,4,0,"a cave entrance","temperate","cloudy",True,False,False,False,False,True,False,0,"cave",False,False,"", "there is a cave enterance in the ground here, looks like it goes straight down",[],[],[],[],[])
north_cave_a = scene_type(2,4,-1,"a cave","temperate","cloudy",True,False,False,False,False,True,False,0,"cave",False,False,"", "this cave goes down further, there is light coming from above...",[],[],[],[],[])
north_cave_b = scene_type(2,4,-2,"a cave","temperate","cloudy",True,False,False,False,False,True,False,0,"cave",False,False,"", "this cave goes down further, there is light coming from above...",[],[],[],[],[])
north_cave_c = scene_type(2,4,-3,"a cave","temperate","cloudy",True,False,False,False,False,True,False,0,"cave",False,False,"", "this cave goes down further, there is a faint light coming from above...",[],[],[],[],[])
north_cave_d = scene_type(2,4,-4,"a cave","temperate","cloudy",True,False,False,False,False,True,False,0,"cave",False,False,"", "this cave goes down further, there is a faint light coming from above...",[],[],[],[],[])
north_cave_e = scene_type(2,4,-5,"a cave","temperate","cloudy",True,False,False,False,False,True,False,0,"cave",False,False,"", "this cave goes down further, there is a faint light coming from above...",[],[],[],[],[])
north_cave_f = scene_type(2,4,-6,"a cave","temperate","cloudy",True,False,False,False,False,True,False,0,"cave",False,False,"", "this cave goes down further, there is a faint light coming from above...",[],[],[],[],[])
north_cave_g = scene_type(2,4,-7,"a cave","temperate","cloudy",True,False,False,False,False,True,False,0,"cave",False,False,"", "this cave goes down further, there is a faint light coming from above...",[],[],[],[],[])
north_cave_h = scene_type(2,4,-8,"a cave","temperate","cloudy",True,False,False,False,False,True,False,0,"cave",False,False,"", "there is a tunnnel below, there is a very faint light coming from above...",[],[],[],[],[])

tunnel_a = scene_type(2,4,-9,"an underground tunnel","temperate","cloudy",False,False,False,False,False,True,False,2,"cave",False,False,"", "there is a very faint light coming from above...",[],[],[],[],[])
tunnel_b = scene_type(3,4,-9,"an underground tunnel","temperate","cloudy",False,False,False,False,False,True,False,2,"cave",False,False,"", "this is an ancient tunnel, i wonder why it's here",[],[],[],[],[])
tunnel_c = scene_type(4,4,-9,"an underground tunnel","temperate","cloudy",False,False,False,False,False,True,False,2,"cave",False,False,"", "there are carvings on the wall, they depict goblins fighting some kind of demonic creature.",[],[],[],[],[])
tunnel_d = scene_type(5,4,-9,"an underground tunnel","temperate","cloudy",False,False,False,False,False,True,False,2,"cave",False,False,"", "there are carvings of goblins and humans massed in a large army, 2",[],[],[],[],[])

tunnel_e = scene_type(5,3,-9,"an underground tunnel","temperate","cloudy",False,False,False,False,False,True,False,2,"cave",False,False,"", "this is an ancient tunnel, i wonder why it's here",[],[],[],[],[])
tunnel_f = scene_type(5,2,-9,"an underground tunnel","temperate","cloudy",False,False,False,False,False,True,False,2,"cave",False,False,"", "this is an ancient tunnel, carvings depict a three headed dragon fighting a large demon",[],[],[],[],[])
tunnel_g = scene_type(5,1,-9,"an underground tunnel","temperate","cloudy",False,False,False,False,False,True,False,2,"cave",False,False,"", "this is an ancient tunnel, skeletons of ancient warriors line the walls here",[],[],[],[],[])
tunnel_h = scene_type(5,0,-9,"an underground tunnel","temperate","cloudy",False,False,False,False,False,True,False,2,"cave",False,False,"", "this is an ancient tunnel",[],[],[],[],[])
tunnel_i = scene_type(5,-1,-9,"an underground tunnel","temperate","cloudy",False,False,False,False,False,True,False,2,"cave",False,False,"", "this is an ancient tunnel, it smells of decay",[],[],[],[],[])
tunnel_j = scene_type(5,-2,-9,"an underground tunnel","temperate","cloudy",False,False,False,False,False,True,False,2,"cave",False,False,"", "this is an ancient tunnel, the air is still",[],[],[],[],[])
tunnel_k = scene_type(5,-3,-9,"an underground tunnel","temperate","cloudy",False,False,False,False,False,True,False,2,"cave",False,False,"", "this is an ancient tunnel, it's carved from solid rock",[],[],[],[],[])

###--UNIQUE IMPASSABLE TERRAIN--###

cliffs_a = scene_type(-1,0,0,"cliffs","temp_string","light_string",False,False,False,False,False,False,False,0,"cave",False,False,"cliffs block your path","",[],[],[],[],[])
cliffs_b = scene_type(0,1,0,"cliffs","temp_string","light_string",False,False,False,False,False,False,False,0,"cave",False,False,"cliffs block your path","",[],[],[],[],[])
cliffs_c = scene_type(0,2,0,"cliffs","temp_string","light_string",False,False,False,False,False,False,False,0,"cave",False,False,"cliffs block your path","",[],[],[],[],[])
cliffs_d = scene_type(0,3,0,"cliffs","temp_string","light_string",False,False,False,False,False,False,False,0,"cave",False,False,"cliffs block your path","",[],[],[],[],[])
cliffs_e = scene_type(0,4,0,"cliffs","temp_string","light_string",False,False,False,False,False,False,False,0,"cave",False,False,"cliffs block your path","",[],[],[],[],[])
cliffs_f = scene_type(0,5,0,"cliffs","temp_string","light_string",False,False,False,False,False,False,False,0,"cave",False,False,"cliffs block your path","",[],[],[],[],[])
river_a = scene_type(1,-2,0,"river","temp_string","light_string",False,False,False,False,False,False,False,0,"water",False,False,"a river blocks your path","",[],[],[],[],[])
river_b = scene_type(2,-2,0,"river","temp_string","light_string",False,False,False,False,False,False,False,0,"water",False,False,"a river blocks your path","",[],[],[],[],[])
river_c = scene_type(3,-2,0,"river","temp_string","light_string",False,False,False,False,False,False,False,0,"water",False,False,"a river blocks your path","",[],[],[],[],[])
river_d = scene_type(4,-2,0,"river","temp_string","light_string",False,False,False,False,False,False,False,0,"water",False,False,"a river blocks your path","",[],[],[],[],[])
river_e = scene_type(6,-2,0,"river","temp_string","light_string",False,False,False,False,False,False,False,0,"water",False,False,"a river blocks your path","",[],[],[],[],[])
river_f = scene_type(7,-2,0,"river","temp_string","light_string",False,False,False,False,False,False,False,0,"water",False,False,"a river blocks your path","",[],[],[],[],[])
river_g = scene_type(8,-2,0,"river","temp_string","light_string",False,False,False,False,False,False,False,0,"water",False,False,"a river blocks your path","",[],[],[],[],[])
lake_a = scene_type(0,-2,0,"lake","temp_string","light_string",False,False,False,False,False,False,False,0,"water",False,False,"a deep lake blocks your path","",[],[],[],[],[])
lake_b = scene_type(0,-3,0,"lake","temp_string","light_string",False,False,False,False,False,False,False,0,"water",False,False,"a deep lake blocks your path","",[],[],[],[],[])
lake_c = scene_type(-1,-2,0,"lake","temp_string","light_string",False,False,False,False,False,False,False,0,"water",False,False,"a deep lake blocks your path","",[],[],[],[],[])
lake_d = scene_type(-1,-3,0,"lake","temp_string","light_string",False,False,False,False,False,False,False,0,"water",False,False,"a deep lake blocks your path","",[],[],[],[],[])

ocean = scene_type(999,999,999,"the ocean","temp_string","light_string",False,False,False,False,False,False,False,0,"water",False,False,"the ocean blocks your escape","",[],[],[],[],[])

solid_cave_wall = scene_type(998,998,998,"a solid cave wall","temp_string","light_string",False,False,False,False,False,False,False,0,"ground",False,False,"a sheer wall of rock blocks your path","",[],[],[],[],[])
solid_cave_ground = scene_type(997,997,997,"a solid cave floor","temp_string","light_string",False,False,False,False,False,False,False,0,"ground",False,False,"a floor of rock blocks your path","",[],[],[],[],[])
ground = scene_type(996,996,996,"the ground","temp_string","light_string",False,False,False,False,False,False,False,0,"forest",False,False,"the ground blocks your path","",[],[],[],[],[])
sky = scene_type(995,995,995,"the sky","temp_string","light_string",False,False,False,False,False,False,False,0,"seaside",False,False,"you cannot fly","",[],[],[],[],[])
solid_dungeon_wall = scene_type(994,994,994,"a solid dungeon wall","temp_string","light_string",False,False,False,False,False,False,False,0,"ground",False,False,"a wall of stone brick blocks your path","",[],[],[],[],[])
solid_dungeon_ground = scene_type(993,993,993,"a solid dungeon floor","temp_string","light_string",False,False,False,False,False,False,False,0,"ground",False,False,"a floor of stone brick blocks your path","",[],[],[],[],[])

##################################--PLAYER--############################################

class player_stats:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.xp = 1
        self.hp = 1 # current mana points
        self.mp = 1 # current hit points
        self.gp = 1
        self.magic = 1
        self.strength = 1
        self.attack = 1
        self.defence = 1
        self.maxhp = 1 # hit points maximum value
        self.nobonus_maxhp = 1 #  hit points max without gear bonus
        self.maxmp = 1 # mana points maximum value
        self.nobonus_maxmp = 1 #  mana points max without gear bonus
        self.strength_xp = 1
        self.attack_xp = 1
        self.magic_xp = 1
        self.defence_xp = 1
        self.status_effect = 1
        self.magic_bonus = 1
        self.strength_bonus = 1
        self.attack_bonus = 1
        self.defence_bonus = 1
        self.maxhp_bonus = 1
        self.maxmp_bonus = 1

        self.status_effect_list = []

player1 = player_stats("The Hero")

class player_skills:
    def __init__(self, fishing, fishing_xp, thieving, thieving_xp, crafting, crafting_xp, cooking, cooking_xp):
        self.fishing = fishing
        self.fishing_xp = fishing_xp
        self.thieving = thieving
        self.thieving_xp = thieving_xp
        self.crafting = crafting
        self.crafting_xp = crafting_xp
        self.cooking = cooking
        self.cooking_xp = cooking_xp

player1_skills = player_skills(1,0,1,0,1,0,1,0)

############################################--NPCS/DIALOUGE/QUESTS--#########################################

class npc:
    def __init__(self, first_name, last_name, title, npc_desc, greeting, is_animal, race, gender, faction, attire, assault_dialouge):
        self.first_name = first_name
        self.last_name = last_name
        self.npc_desc = npc_desc
        self.title = title
        self.greeting = greeting
        self.is_animal = is_animal
        self.race = race
        self.gender = gender
        self.faction = faction
        self.attire = attire
        self.assault_dialouge = assault_dialouge

        self.dialouge_options_list = []
        self.combat_enemy_list = []
        self.quest_list = []

        self.npc_inventory = []
        self.npc_spell_inventory = []
        self.npc_weapon_inventory = []
        self.npc_armor_inventory = []
        self.npc_helmet_inventory = []
        self.npc_shield_inventory = []
        self.is_dead = False
        all_npcs.append(self)


#########   TWO NPCS CANNOT HAVE THE SAME FIRST NAME !!!!   #############

npc_jenkins = npc("old man","jenkins","Seer","Good for a chat!","hello",False,"human","man","0","cloth clothes","*the old man transforms into a goblin*")
npc_john_doe = npc("John","Dough","Merchant","weapons merchant...","hello",False,"human","man","0","cloth clothes","oof")
npc_jane_doe = npc("Haney","Dunorf","Peasant","runs an item shop...","'ello",False,"human","woman","0","cloth clothes","oof")
npc_wizard_traenus = npc("Neil","Traenus","Head Wizard","a man of magic...","hello",False,"human","man","0","blue wizard robes","oof")
npc_wizard_marbles = npc("Marbles","the dog","canine magic specialist","a dog of magic...","woof!",True,"dog","cute","0","0","WOOF!")
npc_dismurth_smith = npc("George","Smith","Blacksmith","good at making horseshoes...","G'day",False,"dwarf","man","dwavern","cloth clothes","oof")

npc_wizard_jim = npc("Jim","Greenmichs","Wizard","appreciates a fine brew and a mix...","yo",False,"human","man","0","blue wizard robes","oof")
npc_wizard_tilly = npc("Tilly","the dog","wizard","an apprentice wizard puppy...","woof!",True,"dog","man","0","cloth clothes","oof")

npc_merchant_ollie = npc("Ollie","Zedex","Travelling Merchant","an exotic trader...","G'day",False,"human","man","0","fine clothes","oof")
npc_merchant_dech = npc("Dechen","Pavoni","Extractor","creative concoctions are his specialty...","G'day",False,"human","man","0","fine clothes","oof")


# place npcs in the world
dismurth_square.npc_list.append(npc_jenkins)
dismurth_market.npc_list.append(npc_john_doe)
dismurth_market.npc_list.append(npc_jane_doe)
dismurth_tower_1f.npc_list.append(npc_wizard_traenus)
dismurth_tower_gf.npc_list.append(npc_wizard_marbles)
dismurth_smith.npc_list.append(npc_dismurth_smith)

################################

class dialouge_option:
    def __init__(self, text, is_buy_item, is_buy_weapon, is_buy_armor, is_buy_helmet, is_buy_shield, is_buy_spell, is_sell, is_talk, is_assault, is_give, is_quest):
        self.text = text #text displayed for dialouge option
        self.is_buy_item = is_buy_item #interprets dialouge option as player wanting to make a purchase
        self.is_buy_weapon = is_buy_weapon #interprets dialouge option as player wanting to make a purchase
        self.is_buy_armor = is_buy_armor #interprets dialouge option as player wanting to make a purchase
        self.is_buy_helmet = is_buy_helmet #interprets dialouge option as player wanting to make a purchase
        self.is_buy_shield = is_buy_shield #interprets dialouge option as player wanting to make a purchase
        self.is_buy_spell = is_buy_spell #interprets dialouge option as player wanting to make a purchase
        self.is_sell = is_sell #interprets dialouge option as player wanting to sell something
        self.is_talk = is_talk #interprets dialouge option as player wanting to talk
        self.is_assault = is_assault #interprets dialouge option as player wanting to attack the npc
        self.is_give = is_give #interprets dialouge option as a trigger to give the player an item
        self.is_quest = is_quest #interprets dialouge option as player wanting to give the npc an item


dialouge_buy_item = dialouge_option("can I buy something?",True,False,False,False,False,False,False,False,False,False,False)
dialouge_buy_weapon = dialouge_option("can I buy some weapons?",False,True,False,False,False,False,False,False,False,False,False)
dialouge_buy_armor = dialouge_option("can I buy some armor?",False,False,True,False,False,False,False,False,False,False,False)
dialouge_buy_helmet = dialouge_option("may I browse your helmet selection?",False,False,False,True,False,False,False,False,False,False,False)
dialouge_buy_shield = dialouge_option("i would like to buy a shield, please",False,False,False,False,True,False,False,False,False,False,False)
dialouge_buy_spell = dialouge_option("do you have any spells for sale?",False,False,False,False,False,True,False,False,False,False,False)

dialouge_sell = dialouge_option("can I sell something?",False,False,False,False,False,False,True,False,False,False,False)
dialouge_talk = dialouge_option("have you heard any interesting news?",False,False,False,False,False,False,False,True,False,False,False)
dialouge_gf = dialouge_option("get fucked mate!",False,False,False,False,False,False,False,False,True,False,False)
dialouge_give = dialouge_option("give me something!",False,False,False,False,False,False,False,False,False,True,False)
dialouge_quest = dialouge_option("do you have a quest?",False,False,False,False,False,False,False,False,False,False,True)

npc_jenkins.dialouge_options_list.append(dialouge_talk)
npc_jenkins.dialouge_options_list.append(dialouge_gf)
npc_jenkins.dialouge_options_list.append(dialouge_give)
npc_jenkins.dialouge_options_list.append(dialouge_quest)
npc_jenkins.dialouge_options_list.append(dialouge_sell)

npc_john_doe.dialouge_options_list.append(dialouge_talk)
npc_john_doe.dialouge_options_list.append(dialouge_buy_weapon)
npc_john_doe.dialouge_options_list.append(dialouge_buy_armor)
npc_john_doe.dialouge_options_list.append(dialouge_buy_helmet)
npc_john_doe.dialouge_options_list.append(dialouge_buy_shield)

npc_jane_doe.dialouge_options_list.append(dialouge_talk)
npc_jane_doe.dialouge_options_list.append(dialouge_buy_item)

npc_wizard_traenus.dialouge_options_list.append(dialouge_talk)
npc_wizard_traenus.dialouge_options_list.append(dialouge_buy_spell)
npc_wizard_traenus.dialouge_options_list.append(dialouge_buy_item)

npc_wizard_marbles.dialouge_options_list.append(dialouge_talk)
npc_wizard_marbles.dialouge_options_list.append(dialouge_buy_spell)

npc_dismurth_smith.dialouge_options_list.append(dialouge_talk)
npc_dismurth_smith.dialouge_options_list.append(dialouge_buy_weapon)
npc_dismurth_smith.dialouge_options_list.append(dialouge_buy_armor)
npc_dismurth_smith.dialouge_options_list.append(dialouge_buy_helmet)
npc_dismurth_smith.dialouge_options_list.append(dialouge_buy_shield)
#######################################

#######################################

class quest:
    def __init__(self, name, quest_desc, xp, gp, reward_list, quest_collect_items, item_amount, quest_kill_enemies, kill_amount):
        self.name = name
        self.quest_desc = quest_desc
        self.xp = xp
        self.gp = gp
        self.reward_list = reward_list
        self.quest_collect_items = quest_collect_items
        self.item_amount = item_amount
        self.quest_kill_enemies = quest_kill_enemies
        self.kill_amount = kill_amount

quest_1 = quest("The Bandit Menace","eliminate the local bandit population",200,80,[],False,0,True,10)


#########################################--ITEMS/WEAPONS/ARMOR/SPELLS--#############################################

class item:
    def __init__(self, id, name, value, edible, poisonous, hp, item_desc):
        self.id = id
        self.name = name
        self.print_name = (Fore.BLACK + Style.BRIGHT + name + Style.RESET_ALL)
        self.value = value
        self.edible = edible
        self.poisonous = poisonous
        self.hp = hp
        self.item_desc = item_desc

        all_game_items.append(self)

#ITEM IDS SERVE NO PURPOSE,

#unique items:

    #rope is unique item used to travel down and up on the z axis below 0
rope = item(109,"rope",120,False,False,0,"")
    #tent allows player to use "camp" command to heal fully, late game item.
tent = item(108,"tent",200,True,False,8,"")
    #torch changes description text in dark enviroments, need to implement encounter rate change at night and in dark areas
torch = item(110,"torch",80,False,False,0,"")

#########################################

#edible poisonous items
apple = item(100,"apple",5,True,True,1000,"")
rotten_food = item(100,"rotten food",5,True,True,100,"")

#edible healing items
pear = item(101,"pear",20,True,False,10,"")
cabbage = item(101,"cabbage",2,True,False,10,"")
turnip = item(101,"turnip",5,True,False,10,"")
banana = item(101,"banana",5,True,False,10,"")
pineapple = item(101,"pineapple",5,True,False,10,"")

mushroom = item(101,"mushroom",5,True,False,10,"")
magic_mushroom = item(101,"magic mushroom",5,True,False,10,"")

cup_of_tea = item(108,"cup of tea",2,True,False,8,"")
hp_potion = item(111,"hp potion",20,True,False,1000,"")
super_hp_potion = item(111,"super hp potion",20,True,False,10000,"")

#key items:
beak_polish = item(103,"beak polish",10,False,False,0,"")
pendant = item(105,"pendant",80,False,False,0,"")
legion_seal = item(106,"legion seal",7,False,False,0,"")
oak_key = item(106,"oak key",7,False,False,0,"")
jail_key = item(106,"jail key",7,False,False,0,"")
certificate_of_passage = item(106,"certificate of passage",100,False,False,0,"")

#??? items:
fire_orb = item(106,"fire orb",7,False,False,0,"")
water_orb = item(106,"water orb",7,False,False,0,"")
earth_orb = item(106,"earth orb",7,False,False,0,"")
air_orb = item(106,"air orb",7,False,False,0,"")
bones = item(112,"bones",2,False,False,0,"")
cup = item(104,"cup",12,False,False,0,"")
worms = item(102,"worms",500,False,False,0,"")
tea_bag = item(107,"tea bag",1,False,False,0,"")

class ground_item:
    def __init__(self, name):
        self.name = name
        self.print_name = (Fore.BLACK + Style.BRIGHT + self.name + Style.RESET_ALL)
        all_ground_game_items.append(self)

ground_apple = ground_item("apple")
ground_pear = ground_item("pear")
ground_worms = ground_item("worms")
ground_beak_polish = ground_item("beak polish")
ground_cup = ground_item("cup")
ground_pendant = ground_item("pendant")
ground_legion_seal = ground_item("legion seal")
ground_tea_bag = ground_item("tea bag")
ground_cup_of_tea = ground_item("cup of tea")
ground_tent = ground_item("tent")
ground_rope = ground_item("rope")
ground_torch = ground_item("torch")
ground_hp_potion = ground_item("hp potion")
ground_bones = ground_item("bones")
ground_fire_orb = ground_item("fire orb")
ground_water_orb = ground_item("water orb")
ground_earth_orb = ground_item("earth orb")
ground_air_orb = ground_item("air orb")
ground_mushroom = ground_item("mushroom")
ground_magic_mushroom = ground_item("magic_mushroom")


ground_oak_key = ground_item("oak key")
ground_jail_key = ground_item("jail key")
ground_certificate_of_passage = ground_item("certificate of passage")

class weapon:
    def __init__(self, id, name, value, type, level, attribute, magic_bonus, strength_bonus, attack_bonus, defence_bonus, maxhp_bonus):
        self.id = id
        self.name = name
        self.print_name = (Fore.BLACK + Style.BRIGHT + name + Style.RESET_ALL)
        self.value = value
        self.type = type
        self.level = level
        self.attribute = attribute
        self.magic_bonus = magic_bonus
        self.strength_bonus = strength_bonus
        self.attack_bonus = attack_bonus
        self.defence_bonus = defence_bonus
        self.maxhp_bonus = maxhp_bonus

        if self.attribute == "fire":
            self.print_attribute = (Fore.RED + Style.NORMAL + attribute + Style.RESET_ALL)
        if self.attribute == "water":
            self.print_attribute = (Fore.BLUE + Style.NORMAL + attribute + Style.RESET_ALL)
        if self.attribute == "earth":
            self.print_attribute = (Fore.GREEN + Style.NORMAL + attribute + Style.RESET_ALL)
        if self.attribute == "air":
            self.print_attribute = (Fore.BLACK + Style.BRIGHT + attribute + Style.RESET_ALL)
        if self.attribute == "holy":
            self.print_attribute = (Fore.YELLOW + Style.NORMAL + attribute + Style.RESET_ALL)
        if self.attribute == "undead":
            self.print_attribute = (Fore.MAGENTA + Style.DIM + attribute + Style.RESET_ALL)
        if self.attribute == "slime":
            self.print_attribute = (Fore.GREEN + Style.BRIGHT + attribute + Style.RESET_ALL)
        if self.attribute == "ice":
            self.print_attribute = (Fore.CYAN + Style.NORMAL + attribute + Style.RESET_ALL)

        all_game_weapons.append(self)

bird_sword = weapon(201,"bird sword",3,"sword",5,"air",5,9,15,12,10)
super_bird_sword = weapon(202,"super bird sword",180,"sword",50,"air",0,500,500,500,0)

iron_sword = weapon(203,"iron sword",5,"sword",5,"earth",0,10,10,10,1)
steel_sword = weapon(204,"steel sword",80,"sword",10,"earth",0,20,20,20,0)
mithril_sword = weapon(204,"mithril sword",80,"sword",15,"earth",0,30,30,30,0)
adamantite_sword = weapon(204,"adamantite sword",80,"sword",20,"earth",0,40,40,40,0)
rune_sword = weapon(204,"rune sword",80,"sword",25,"earth",0,50,50,50,0)

iron_axe = weapon(205,"iron axe",8,"axe",5,"earth",0,10,10,10,0)
steel_axe = weapon(206,"steel axe",80,"axe",10,"earth",0,20,20,20,0)
mithril_axe = weapon(206,"mithril axe",80,"axe",15,"earth",0,20,20,20,0)
adamantite_axe = weapon(206,"adamantite axe",80,"axe",20,"earth",0,20,20,20,0)
rune_axe = weapon(206,"rune axe",80,"axe",25,"earth",0,20,20,20,0)

greatsword = weapon(207,"greatsword",800,"large sword",32,"water",0,40,40,40,0)
ultra_greatsword = weapon(208,"ultra_greatsword",8000,"large sword",54,"water",0,60,60,60,0)
war_spear = weapon(209,"war spear",80,"spear",16,"fire",70,20,20,20,0)
lance = weapon(210,"lance",80,"spear",28,"air",100,30,30,30,0)

bone_scimitar = weapon(211,"bone scimitar",80000,"sword",320,"undead",10,100,200,0,0)
gladius = weapon(212,"gladius",8000,"sword",120,"holy",5,50,50,200,0)
battle_axe = weapon(213,"battle axe",6000,"axe",160,"fire",0,220,120,50,0)
warhammer = weapon(214,"warhammer",5600,"hammer",280,"earth",0,250,60,22,0)

class ground_weapon:
    def __init__(self, name):
        self.name = name
        self.print_name = (Fore.BLACK + Style.BRIGHT + self.name + Style.RESET_ALL)

        all_ground_game_weapons.append(self)

ground_bird_sword = ground_weapon("bird sword")
ground_super_bird_sword = ground_weapon("super bird sword")
ground_iron_sword = ground_weapon("iron sword")
ground_steel_sword = ground_weapon("steel sword")
ground_iron_axe = ground_weapon("iron axe")
ground_steel_axe = ground_weapon("steel axe")
ground_greatsword = ground_weapon("greatsword")
ground_ultra_greatsword = ground_weapon("ultra_greatsword")
ground_war_spear = ground_weapon("war spear")
ground_lance = ground_weapon("lance")
ground_bone_scimitar = ground_weapon("bone scimitar")
ground_gladius = ground_weapon("gladius")
ground_battle_axe = ground_weapon("battle axe")
ground_warhammer = ground_weapon("warhammer")
ground_mithril_sword  = ground_weapon("mithril sword" )
ground_adamantite_sword = ground_weapon("adamantite sword")
ground_rune_sword = ground_weapon("rune sword")
ground_mithril_axe  = ground_weapon("mithril axe")
ground_adamantite_axe = ground_weapon("adamantite axe")
ground_rune_axe = ground_weapon("rune axe")

class armor:
    def __init__(self, id, name, value, type, level, attribute, magic_bonus, strength_bonus, attack_bonus, defence_bonus, maxhp_bonus):
        self.id = id
        self.name = name
        self.print_name = (Fore.BLACK + Style.BRIGHT + self.name + Style.RESET_ALL)
        self.value = value
        self.type = type
        self.level = level
        self.attribute = attribute
        self.magic_bonus = magic_bonus
        self.strength_bonus = strength_bonus
        self.attack_bonus = attack_bonus
        self.defence_bonus = defence_bonus
        self.maxhp_bonus = maxhp_bonus

        if self.attribute == "fire":
            self.print_attribute = (Fore.RED + Style.NORMAL + attribute + Style.RESET_ALL)
        if self.attribute == "water":
            self.print_attribute = (Fore.BLUE + Style.NORMAL + attribute + Style.RESET_ALL)
        if self.attribute == "earth":
            self.print_attribute = (Fore.GREEN + Style.NORMAL + attribute + Style.RESET_ALL)
        if self.attribute == "air":
            self.print_attribute = (Fore.BLACK + Style.BRIGHT + attribute + Style.RESET_ALL)
        if self.attribute == "holy":
            self.print_attribute = (Fore.YELLOW + Style.NORMAL + attribute + Style.RESET_ALL)
        if self.attribute == "undead":
            self.print_attribute = (Fore.MAGENTA + Style.DIM + attribute + Style.RESET_ALL)
        if self.attribute == "slime":
            self.print_attribute = (Fore.GREEN + Style.BRIGHT + attribute + Style.RESET_ALL)
        if self.attribute == "ice":
            self.print_attribute = (Fore.CYAN + Style.NORMAL + attribute + Style.RESET_ALL)

        all_game_armor.append(self)

birdshirt = armor(301,"bird t shirt",100,"light",99,"air",10,24,22,40,1100)
leather_armor = armor(302,"leather armor",10,"light",1,"water",10,4,4,5,10)
hard_leather_armor = armor(303,"hard leather armor",10,"light",10,"water",18,4,4,8,50)
iron_chain_mail = armor(304,"iron chain mail",40,"heavy",12,"earth",0,7,14,17,50)
iron_plate_armor = armor(305,"iron plate armor",100,"heavy",15,"earth",0,11,9,22,500)
steel_chain_mail = armor(306,"steel chain mail",400,"heavy",14,"earth",0,13,18,25,100)
steel_plate_armor = armor(307,"steel plate armor",1000,"heavy",22,"earth",0,16,15,28,1000)
rags = armor(308,"rags",1,"light",1,"fire",0,1,1,1,1)
mage_robes = armor(309,"mage robes",1000,"mage",20,"air",50,0,0,20,1000)
necro_robes = armor(309,"necromancer robes",1000,"mage",44,"air",55,0,0,50,2000)

class ground_armor:
    def __init__(self, name):
        self.name = name
        self.print_name = (Fore.BLACK + Style.BRIGHT + self.name + Style.RESET_ALL)

        all_ground_game_armor.append(self)

ground_birdshirt = ground_armor("bird t shirt")
ground_leather_armor = ground_armor("leather armor")
ground_hard_leather_armor = ground_armor("hard leather armor")
ground_iron_chain_mail = ground_armor("iron chain mail")
ground_iron_plate_armor = ground_armor("iron plate armor")
ground_steel_chain_mail = ground_armor("steel chain mail")
ground_steel_plate_armor = ground_armor("steel plate armor")
ground_rags = ground_armor("rags")
ground_mage_robes = ground_armor("mage robes")
ground_necro_robes = ground_armor("necromancer robes")

class helmet:
    def __init__(self, id, name, value, type, level, attribute, magic_bonus, strength_bonus, attack_bonus, defence_bonus, maxhp_bonus):
        self.id = id
        self.name = name
        self.print_name = (Fore.BLACK + Style.BRIGHT + self.name + Style.RESET_ALL)
        self.value = value
        self.type = type
        self.level = level
        self.attribute = attribute
        self.magic_bonus = magic_bonus
        self.strength_bonus = strength_bonus
        self.attack_bonus = attack_bonus
        self.defence_bonus = defence_bonus
        self.maxhp_bonus = maxhp_bonus

        if self.attribute == "fire":
            self.print_attribute = (Fore.RED + Style.NORMAL + attribute + Style.RESET_ALL)
        if self.attribute == "water":
            self.print_attribute = (Fore.BLUE + Style.NORMAL + attribute + Style.RESET_ALL)
        if self.attribute == "earth":
            self.print_attribute = (Fore.GREEN + Style.NORMAL + attribute + Style.RESET_ALL)
        if self.attribute == "air":
            self.print_attribute = (Fore.BLACK + Style.BRIGHT + attribute + Style.RESET_ALL)
        if self.attribute == "holy":
            self.print_attribute = (Fore.YELLOW + Style.NORMAL + attribute + Style.RESET_ALL)
        if self.attribute == "undead":
            self.print_attribute = (Fore.MAGENTA + Style.DIM + attribute + Style.RESET_ALL)
        if self.attribute == "slime":
            self.print_attribute = (Fore.GREEN + Style.BRIGHT + attribute + Style.RESET_ALL)
        if self.attribute == "ice":
            self.print_attribute = (Fore.CYAN + Style.NORMAL + attribute + Style.RESET_ALL)

        all_game_helmets.append(self)

bird_hat = helmet(301,"bird hat",100,"light",99,"air",10,24,22,40,1100)
iron_helmet = helmet(301,"iron helmet",100,"heavy",9,"air",1,2,2,10,100)
steel_helmet = helmet(301,"steel helmet",100,"heavy",18,"air",1,4,2,20,500)
mage_hood = helmet(301,"mage hood",100,"light",70,"air",100,0,0,40,1000)

class ground_helmet:
    def __init__(self, name):
        self.name = name
        self.print_name = (Fore.BLACK + Style.BRIGHT + self.name + Style.RESET_ALL)

        all_ground_game_helmets.append(self)

ground_bird_hat = ground_helmet("bird hat")
ground_iron_helmet = ground_helmet("iron helmet")
ground_steel_helmet = ground_helmet("steel helmet")
ground_mage_hood  = ground_helmet("mage hood")

class shield:
    def __init__(self, id, name, value, type, level, attribute, magic_bonus, strength_bonus, attack_bonus, defence_bonus, maxhp_bonus):
        self.id = id
        self.name = name
        self.print_name = (Fore.BLACK + Style.BRIGHT + self.name + Style.RESET_ALL)
        self.value = value
        self.type = type
        self.level = level
        self.attribute = attribute
        self.magic_bonus = magic_bonus
        self.strength_bonus = strength_bonus
        self.attack_bonus = attack_bonus
        self.defence_bonus = defence_bonus
        self.maxhp_bonus = maxhp_bonus

        if self.attribute == "fire":
            self.print_attribute = (Fore.RED + Style.NORMAL + attribute + Style.RESET_ALL)
        if self.attribute == "water":
            self.print_attribute = (Fore.BLUE + Style.NORMAL + attribute + Style.RESET_ALL)
        if self.attribute == "earth":
            self.print_attribute = (Fore.GREEN + Style.NORMAL + attribute + Style.RESET_ALL)
        if self.attribute == "air":
            self.print_attribute = (Fore.BLACK + Style.BRIGHT + attribute + Style.RESET_ALL)
        if self.attribute == "holy":
            self.print_attribute = (Fore.YELLOW + Style.NORMAL + attribute + Style.RESET_ALL)
        if self.attribute == "undead":
            self.print_attribute = (Fore.MAGENTA + Style.DIM + attribute + Style.RESET_ALL)
        if self.attribute == "slime":
            self.print_attribute = (Fore.GREEN + Style.BRIGHT + attribute + Style.RESET_ALL)
        if self.attribute == "ice":
            self.print_attribute = (Fore.CYAN + Style.NORMAL + attribute + Style.RESET_ALL)

        all_game_shields.append(self)

bird_shield = shield(301,"bird shield",100,"light",99,"air",10,24,22,40,1100)
iron_square_shield = shield(301,"iron square shield",100,"heavy",9,"air",1,2,2,10,100)
steel_square_shield = shield(301,"steel square shield",100,"heavy",18,"air",1,4,2,20,500)
mage_book = shield(301,"mage book",100,"light",99,"air",100,0,0,40,1000)

class ground_shield:
    def __init__(self, name):
        self.name = name
        self.print_name = (Fore.BLACK + Style.BRIGHT + self.name + Style.RESET_ALL)

        all_ground_game_shields.append(self)

ground_bird_shield = ground_shield("bird shield")
ground_iron_square_shield = ground_shield("iron square shield")
ground_steel_square_shield = ground_shield("steel square shield")
ground_mage_book = ground_shield("mage book")

class spell:
    def __init__(self, name, level, value, utility, damage, attribute, xp, effect, spell_desc):
        self.name = name
        self.level = level
        self.value = value
        self.utility = utility
        self.damage = damage
        self.attribute = attribute
        self.xp = xp
        self.effect = effect
        self.spell_desc = spell_desc

        self.print_name = (Fore.BLACK + Back.WHITE + Style.NORMAL + name + Style.RESET_ALL)

        if self.attribute == "fire":
            self.print_attribute = (Fore.RED + Style.NORMAL + attribute + Style.RESET_ALL)
        if self.attribute == "water":
            self.print_attribute = (Fore.BLUE + Style.NORMAL + attribute + Style.RESET_ALL)
        if self.attribute == "earth":
            self.print_attribute = (Fore.GREEN + Style.NORMAL + attribute + Style.RESET_ALL)
        if self.attribute == "air":
            self.print_attribute = (Fore.BLACK + Style.BRIGHT + attribute + Style.RESET_ALL)
        if self.attribute == "holy":
            self.print_attribute = (Fore.YELLOW + Style.NORMAL + attribute + Style.RESET_ALL)
        if self.attribute == "undead":
            self.print_attribute = (Fore.MAGENTA + Style.DIM + attribute + Style.RESET_ALL)
        if self.attribute == "slime":
            self.print_attribute = (Fore.GREEN + Style.BRIGHT + attribute + Style.RESET_ALL)
        if self.attribute == "ice":
            self.print_attribute = (Fore.CYAN + Style.NORMAL + attribute + Style.RESET_ALL)

        all_game_spells.append(self)
############--COMBAT SPELLS--#############

# status 0 spells DAMAGE - combat spells, also used for turns where enemy does nothing by doing 0 damage.
slime = spell("slime",5,5,True,0,"slime",0,0,"slurms mackenzie")

# arrow spells
fire_arrow = spell("fire arrow",5,5,False,80,"fire",100,0,"fire damage")
ice_arrow = spell("ice arrow",5,5,False,80,"ice",100,0,"ice damage")

# tier 1 damage spells
fireball = spell("fireball",5,5,False,100,"fire",200,0,"heavy fire damage")
hydro_barrage = spell("hydro barrage",5,5,False,100,"water",200,0,"heavy water damage")
holy_surge = spell("holy surge",5,5,False,100,"holy",200,0,"heavy holy damage")
necro_surge = spell("necro surge",5,5,False,100,"undead",200,0,"heavy undead damage")

# tier 2 damage spells
hydroblast = spell("hydroblast",5,5,False,60,"water",100,0,"light water damage")
fireblast = spell("fireblast",5,5,False,60,"fire",100,0,"light fire damage")
windblast = spell("windblast",5,5,False,60,"air",100,0,"light air damage")
earthblast = spell("earthblast",5,5,False,60,"earth",100,0,"light earth damage")
necroblast = spell("necroblast",5,5,False,60,"undead",100,0,"light undead damage")
holyblast = spell("holyblast",5,5,False,60,"holy",100,0,"light holy damage")

###########--HEALING SPELLS--##########

# status -1 spells HEAL AND DAMAGE

life_drain = spell("life drain",5,5,True,100,"undead",50,-1,"a life draining spell which heals the user")

# status 1 spells HEAL

mega_heal = spell("mega heal",5,5,True,250,"holy",50,1,"a mega healing spell")

super_heal = spell("super heal",5,5,True,100,"holy",50,1,"a super healing spell")

prayer = spell("prayer",5,5,True,50,"holy",50,1,"a light healing spell")

##################--STATUS EFFECT SPELLS--##############################

#status 2 spells FREEZE
snare = spell("snare",5,5,True,5,"ice",70,2,"snares the enemy")

#status 3 spells POISON
poison = spell("poison",5,5,True,5,"earth",70,3,"poisons the enemy")

#status 4 spells BURN
burn = spell("burn",5,5,True,5,"fire",70,4,"burns the enemy")

##################--BUFFS/DEBUFFS--##############################

class status_condition:
    def __init__(self, name, is_freeze, is_poison, is_burn, is_str_up, is_atk_up, is_mgk_up, is_def_up):
        self.name = name
        self.is_freeze = is_freeze
        self.is_poison = is_poison
        self.is_burn = is_burn

        self.is_str_up = is_str_up
        self.is_atk_up = is_atk_up
        self.is_mgk_up = is_mgk_up
        self.is_def_up = is_def_up

frozen = status_condition("frozen",True,False,False,False,False,False,False)

player1.status_effect_list.append(frozen)

###################################--ENEMIES--##########################################

class enemy_stats:
    def __init__(self, name, level, xp, hp, maxhp, mp, maxmp, magic, strength, attack, gp, attribute, weakness, spellbook, drop_table_items, drop_table_weapons, drop_table_armor, drop_table_helmets, drop_table_shields, status_effect):
        self.name =  name
        self.level = level
        self.xp = xp
        self.hp = hp
        self.maxhp = maxhp
        self.mp = mp
        self.maxmp = maxmp
        self.gp = gp
        self.magic = magic
        self.strength = strength
        self.attack = attack
        self.gp = gp
        self.attribute = attribute
        self.print_attribute = colour_attribute + attribute + colour_reset
        self.weakness = weakness
        self.spellbook = spellbook
        self.drop_table_items = drop_table_items
        self.drop_table_weapons = drop_table_weapons
        self.drop_table_armor = drop_table_armor
        self.drop_table_helmets = drop_table_helmets
        self.drop_table_shields = drop_table_shields
        self.status_effect = status_effect
        self.status_effect_list = []

        self.print_name = (Fore.RED + Style.DIM + self.name + Style.RESET_ALL)

        self.drop_table_items.extend(default_drop_table_items)
        self.drop_table_weapons.extend(default_drop_table_weapons)
        self.drop_table_armor.extend(default_drop_table_armor)

goblin = enemy_stats("goblin",2,5,100,100,100,100,1,5,2,100,"earth","fire",[],[],[],[],[],[],0)
hobgoblin = enemy_stats("hobgoblin",3,12,500,500,100,100,1,4,5,300,"earth","fire",[],[],[],[],[],[],0)
bandit = enemy_stats("bandit",5,10,200,200,100,100,1,5,2,100,"fire","earth",[],[],[],[],[],[],0)

legion_soldier = enemy_stats("legion soldier",28,500,1000,1000,100,100,10,14,20,1000,"air","earth",[],[],[],[],[],[],0)
legion_spearman = enemy_stats("legion spearman",25,500,1050,1050,100,100,10,16,10,1050,"air","earth",[],[],[],[],[],[],0)
legion_archer = enemy_stats("legion archer",23,500,870,870,100,100,10,11,22,654,"air","earth",[],[],[],[],[],[],0)
legion_battle_mage = enemy_stats("legion battle mage",29,500,1240,1240,100,100,45,5,6,2245,"air","earth",[],[],[],[],[],[],0)

rock_golem = enemy_stats("rock golem",62,800,10230,10230,100,100,0,55,18,20230,"earth","water",[],[],[],[],[],[],0)
mushroom_man = enemy_stats("mushroom man",67,800,10230,10230,100,100,0,50,20,10230,"earth","fire",[],[],[],[],[],[],0)

bird_warrior = enemy_stats("bird warrior",191,100000,240807,240807,100,100,100,300,220,100,"air","water",[],[],[],[],[],[],0)#leg

fire_elemental = enemy_stats("fire elemental",8,200,320,320,100,100,8,5,2,100,"fire","water",[],[],[],[],[],[],0)
water_elemental = enemy_stats("water elemental",8,200,380,380,100,100,8,5,2,100,"water","earth",[],[],[],[],[],[],0)
earth_elemental = enemy_stats("earth elemental",8,100,320,320,100,100,3,5,2,100,"earth","water",[],[],[],[],[],[],0)
air_elemental = enemy_stats("air elemental",8,100,300,300,100,100,3,5,2,100,"air","earth",[],[],[],[],[],[],0)

giant_snail = enemy_stats("giant snail",14,10,930,930,100,100,0,12,2,930,"earth","earth",[],[],[],[],[],[],0)
giant_spider = enemy_stats("giant spider",33,64,2300,2300,100,100,0,50,2,2300,"earth","fire",[],[],[],[],[],[],0)
giant_moth = enemy_stats("giant moth",18,5,1340,1340,100,100,0,10,20,100,"earth","air",[],[],[],[],[],[],0)

big_slug = enemy_stats("big slug",1,500,10300,10300,100,100,0,0,0,0,"slime","salt",[],[],[],[],[],[],0)#legendary

skeleton_mage = enemy_stats("skeleton mage",101,4202,6007,6007,100,100,53,30,22,100,"undead","holy",[],[],[],[],[],[],0)
skeleton_warrior = enemy_stats("skeleton warrior",101,50922,9207,9207,100,100,0,63,42,100,"undead","holy",[],[],[],[],[],[],0)

######################------ENEMY_SPELLBOOKS------########################

hobgoblin.spellbook.append(earthblast)
hobgoblin.spellbook.append(hydroblast)
hobgoblin.spellbook.append(poison)
hobgoblin.spellbook.append(snare)
hobgoblin.spellbook.append(super_heal)

goblin.spellbook.append(prayer)
goblin.spellbook.append(burn)

giant_moth.spellbook.append(poison)
giant_moth.spellbook.append(poison)

giant_spider.spellbook.append(poison)
giant_spider.spellbook.append(poison)

giant_snail.spellbook.append(slime)

bandit.spellbook.append(snare)
bandit.spellbook.append(prayer)

legion_soldier.spellbook.append(prayer)

legion_spearman.spellbook.append(prayer)
legion_spearman.spellbook.append(prayer)
legion_spearman.spellbook.append(super_heal)

legion_archer.spellbook.append(prayer)
legion_archer.spellbook.append(fire_arrow)
legion_archer.spellbook.append(fire_arrow)
legion_archer.spellbook.append(ice_arrow)
legion_archer.spellbook.append(ice_arrow)

legion_battle_mage.spellbook.append(holyblast)
legion_battle_mage.spellbook.append(holyblast)
legion_battle_mage.spellbook.append(prayer)
legion_battle_mage.spellbook.append(holyblast)
legion_battle_mage.spellbook.append(prayer)
legion_battle_mage.spellbook.append(holyblast)
legion_battle_mage.spellbook.append(holy_surge)
legion_battle_mage.spellbook.append(super_heal)
legion_battle_mage.spellbook.append(holy_surge)
legion_battle_mage.spellbook.append(super_heal)
legion_battle_mage.spellbook.append(holy_surge)
legion_battle_mage.spellbook.append(super_heal)
legion_battle_mage.spellbook.append(holy_surge)

fire_elemental.spellbook.append(fireblast)
fire_elemental.spellbook.append(fireblast)
fire_elemental.spellbook.append(fireblast)
fire_elemental.spellbook.append(burn)
fire_elemental.spellbook.append(fireblast)
fire_elemental.spellbook.append(fireblast)
fire_elemental.spellbook.append(burn)

water_elemental.spellbook.append(hydroblast)
water_elemental.spellbook.append(hydroblast)
water_elemental.spellbook.append(hydroblast)
water_elemental.spellbook.append(hydroblast)
water_elemental.spellbook.append(hydroblast)
water_elemental.spellbook.append(hydroblast)
water_elemental.spellbook.append(hydroblast)

earth_elemental.spellbook.append(earthblast)
earth_elemental.spellbook.append(earthblast)
earth_elemental.spellbook.append(earthblast)
earth_elemental.spellbook.append(earthblast)
earth_elemental.spellbook.append(earthblast)
earth_elemental.spellbook.append(earthblast)
earth_elemental.spellbook.append(earthblast)
earth_elemental.spellbook.append(earthblast)

air_elemental.spellbook.append(windblast)
air_elemental.spellbook.append(windblast)
air_elemental.spellbook.append(windblast)
air_elemental.spellbook.append(windblast)
air_elemental.spellbook.append(windblast)
air_elemental.spellbook.append(windblast)
air_elemental.spellbook.append(windblast)
air_elemental.spellbook.append(windblast)

skeleton_mage.spellbook.append(fireblast)
skeleton_mage.spellbook.append(burn)
skeleton_mage.spellbook.append(fireball)
skeleton_mage.spellbook.append(life_drain)
skeleton_mage.spellbook.append(fireball)
skeleton_mage.spellbook.append(life_drain)
skeleton_mage.spellbook.append(fireball)
skeleton_mage.spellbook.append(life_drain)

skeleton_warrior.spellbook.append(life_drain)
skeleton_warrior.spellbook.append(life_drain)

big_slug.spellbook.append(slime)
big_slug.spellbook.append(slime)
big_slug.spellbook.append(slime)
big_slug.spellbook.append(slime)
big_slug.spellbook.append(slime)
big_slug.spellbook.append(slime)
big_slug.spellbook.append(slime)
big_slug.spellbook.append(slime)
big_slug.spellbook.append(slime)
big_slug.spellbook.append(slime)
big_slug.spellbook.append(slime)

############################----DROP_TABLES-###########################

## default drop tables

weapons_drop_table = []
large_weapons_drop_table = []
magic_weapons_drop_table = []

armor_drop_table = []
magic_armor_drop_table = []

helmets_drop_table = []

shields_drop_table = []

healing_drop_table = []
super_healing_drop_table = []
items_drop_table = []

## default shop tables

weapons_shop_table = []
armor_shop_table = []
helmets_shop_table = []
shields_shop_table = []

spells_shop_table = []

items_shop_table = []

weapons_shop_table.extend(weapons_drop_table)
weapons_shop_table.extend(large_weapons_drop_table)
weapons_shop_table.extend(magic_weapons_drop_table)

armor_shop_table.extend(armor_drop_table)
armor_shop_table.extend(magic_armor_drop_table)

helmets_shop_table.extend(helmets_drop_table)

shields_shop_table.extend(shields_drop_table)

items_shop_table.extend(items_drop_table)
items_shop_table.extend(healing_drop_table)

#####################################################

weapons_drop_table.append(iron_sword)
weapons_drop_table.append(iron_axe)
weapons_drop_table.append(steel_sword)
weapons_drop_table.append(steel_axe)
weapons_drop_table.append(mithril_sword)
weapons_drop_table.append(mithril_axe)
weapons_drop_table.append(adamantite_sword)
weapons_drop_table.append(adamantite_axe)
weapons_drop_table.append(rune_sword)
weapons_drop_table.append(rune_axe)

large_weapons_drop_table.append(war_spear)
large_weapons_drop_table.append(greatsword)
large_weapons_drop_table.append(lance)
large_weapons_drop_table.append(ultra_greatsword)

magic_weapons_drop_table.append(gladius)
magic_weapons_drop_table.append(gladius)
magic_weapons_drop_table.append(bone_scimitar)

#####################################################

armor_drop_table.append(leather_armor)
armor_drop_table.append(hard_leather_armor)
armor_drop_table.append(iron_chain_mail)
armor_drop_table.append(iron_plate_armor)
armor_drop_table.append(steel_chain_mail)
armor_drop_table.append(steel_plate_armor)

magic_armor_drop_table.append(mage_robes)
magic_armor_drop_table.append(mage_robes)
magic_armor_drop_table.append(necro_robes)

#######################################################

helmets_drop_table.append(iron_helmet)
helmets_drop_table.append(steel_helmet)
helmets_drop_table.append(mage_hood)

#####################################################

shields_drop_table.append(mage_book)
shields_drop_table.append(iron_square_shield)
shields_drop_table.append(steel_square_shield)

#####################################################

healing_drop_table.append(apple)
healing_drop_table.append(pear)
healing_drop_table.append(hp_potion)
healing_drop_table.append(hp_potion)

super_healing_drop_table.append(hp_potion)
super_healing_drop_table.append(hp_potion)
super_healing_drop_table.append(super_hp_potion)

items_drop_table.append(bones)
items_drop_table.append(water_orb)
items_drop_table.append(fire_orb)
items_drop_table.append(torch)
items_drop_table.append(tent)
items_drop_table.append(rope)
items_drop_table.append(jail_key)

#####################################################################

bandit.drop_table_items.extend(items_drop_table)
bandit.drop_table_items.extend(healing_drop_table)
bandit.drop_table_items.extend(items_drop_table)

goblin.drop_table_items.extend(items_drop_table)
goblin.drop_table_items.extend(healing_drop_table)
goblin.drop_table_items.extend(items_drop_table)

hobgoblin.drop_table_items.extend(healing_drop_table)
hobgoblin.drop_table_items.extend(items_drop_table)
hobgoblin.drop_table_items.extend(healing_drop_table)

legion_soldier.drop_table_items.extend(super_healing_drop_table)
legion_soldier.drop_table_items.extend(items_drop_table)

legion_spearman.drop_table_items.extend(super_healing_drop_table)
legion_spearman.drop_table_items.extend(items_drop_table)

#####################################################################
goblin.drop_table_weapons.extend(weapons_drop_table)
goblin.drop_table_helmets.extend(helmets_drop_table)

hobgoblin.drop_table_weapons.extend(weapons_drop_table)
hobgoblin.drop_table_armor.extend(armor_drop_table)
hobgoblin.drop_table_helmets.extend(helmets_drop_table)
hobgoblin.drop_table_shields.extend(shields_drop_table)

bandit.drop_table_weapons.extend(weapons_drop_table)
bandit.drop_table_armor.extend(armor_drop_table)
bandit.drop_table_helmets.extend(helmets_drop_table)
bandit.drop_table_shields.extend(shields_drop_table)

legion_soldier.drop_table_weapons.extend(large_weapons_drop_table)
legion_soldier.drop_table_armor.extend(armor_drop_table)
legion_soldier.drop_table_helmets.extend(helmets_drop_table)
legion_soldier.drop_table_shields.extend(shields_drop_table)

legion_spearman.drop_table_weapons.extend(large_weapons_drop_table)
legion_spearman.drop_table_armor.extend(armor_drop_table)
legion_spearman.drop_table_helmets.extend(helmets_drop_table)
legion_spearman.drop_table_shields.extend(shields_drop_table)

bird_warrior.drop_table_weapons.extend(large_weapons_drop_table)
bird_warrior.drop_table_weapons.extend(large_weapons_drop_table)
bird_warrior.drop_table_helmets.extend(helmets_drop_table)
bird_warrior.drop_table_shields.extend(shields_drop_table)

skeleton_mage.drop_table_weapons.extend(magic_weapons_drop_table)
skeleton_mage.drop_table_armor.extend(magic_armor_drop_table)

skeleton_warrior.drop_table_weapons.extend(large_weapons_drop_table)
skeleton_warrior.drop_table_weapons.extend(magic_weapons_drop_table)
skeleton_warrior.drop_table_armor.extend(armor_drop_table)
skeleton_warrior.drop_table_helmets.extend(helmets_drop_table)
skeleton_warrior.drop_table_shields.extend(shields_drop_table)

#################################------PLACE GROUND_ITEMS IN WORLD------#######################################

forest_c.scene_inventory.append(ground_oak_key)

fortress.scene_inventory.append(ground_certificate_of_passage)

########################################------LISTS------###############################################

players = []
players_skills = []

players.append(player1)
players_skills.append(player1_skills)

location = []
location_north = []
location_east = []
location_south = []
location_west = []
location_down = []
location_up = []

current_enemies = []

##############

inventory = []
inventory2 = []
weapon_inventory = []
armor_inventory = []
helmet_inventory = []
shield_inventory = []
spell_inventory = []

# inventory.append(pear)
# inventory.append(tent)
# inventory.append(rope)
# inventory.append(torch)
# inventory.append(hp_potion)
#
# spell_inventory.append(fireblast)
# spell_inventory.append(snare)
#
# weapon_inventory.append(super_bird_sword)
# weapon_inventory.append(gladius)
#
# armor_inventory.append(iron_chain_mail)
# armor_inventory.append(steel_chain_mail)
#
# helmet_inventory.append(iron_helmet)
# helmet_inventory.append(steel_helmet)
#
# shield_inventory.append(iron_square_shield)
# shield_inventory.append(steel_square_shield)

####################################################################

equiped_armor = []
equiped_weapon = []
equiped_helmet = []
equiped_shield = []
equiped_spells = []


if dev_mode >= 1:
    equiped_helmet.append(bird_hat)
    equiped_shield.append(bird_shield)
    equiped_weapon.append(super_bird_sword)
    equiped_armor.append(birdshirt)

    equiped_spells.append(mega_heal)
    equiped_spells.append(fireblast)
    equiped_spells.append(hydroblast)
    equiped_spells.append(earthblast)
    equiped_spells.append(windblast)

else:
    equiped_weapon.append(iron_sword)
    equiped_armor.append(rags)

    equiped_spells.append(prayer)


##########################---NPC INVENTORIES---###########################

sir_kobious_inventory = []

sir_kobious_inventory.append(legion_seal)

old_man_inventory = []

old_man_inventory.append(pendant)

wizard_inventory = []
bird_store_inventory = []
bird_store_armor = []
blacksmith_inventory = []

###########################################################
npc_dismurth_smith.npc_armor_inventory.append(leather_armor)
npc_dismurth_smith.npc_armor_inventory.append(hard_leather_armor)
npc_dismurth_smith.npc_armor_inventory.append(iron_chain_mail)
npc_dismurth_smith.npc_armor_inventory.append(iron_plate_armor)
npc_dismurth_smith.npc_armor_inventory.append(steel_chain_mail)

npc_john_doe.npc_weapon_inventory.append(steel_sword)
npc_john_doe.npc_weapon_inventory.append(steel_axe)

npc_john_doe.npc_helmet_inventory.append(steel_helmet)

npc_john_doe.npc_shield_inventory.append(iron_square_shield)

########################################################

npc_wizard_traenus.npc_spell_inventory.append(fire_arrow)
npc_wizard_traenus.npc_spell_inventory.append(ice_arrow)
npc_wizard_traenus.npc_spell_inventory.append(hydroblast)
npc_wizard_traenus.npc_spell_inventory.append(fireblast)
npc_wizard_traenus.npc_spell_inventory.append(windblast)
npc_wizard_traenus.npc_spell_inventory.append(earthblast)
npc_wizard_traenus.npc_spell_inventory.append(necroblast)
npc_wizard_traenus.npc_spell_inventory.append(holyblast)
npc_wizard_traenus.npc_spell_inventory.append(snare)
npc_wizard_traenus.npc_spell_inventory.append(poison)
npc_wizard_traenus.npc_spell_inventory.append(burn)

npc_wizard_marbles.npc_spell_inventory.append(mega_heal)
npc_wizard_marbles.npc_spell_inventory.append(super_heal)
npc_wizard_marbles.npc_spell_inventory.append(prayer)

npc_jane_doe.npc_inventory.append(torch)
npc_jane_doe.npc_inventory.append(rope)
npc_jane_doe.npc_inventory.append(tent)
npc_jane_doe.npc_inventory.append(hp_potion)
npc_jane_doe.npc_inventory.append(super_hp_potion)
npc_jane_doe.npc_inventory.append(cup_of_tea)
npc_jane_doe.npc_inventory.append(tea_bag)

#########################################################

npc_jenkins.combat_enemy_list.append(hobgoblin)

##############################--SHOP-INVENTORYFUNCTIONS--##############################

def func_shop_restock():
    chance = 1
    item_chance = 1
    global restock_ticks #int
    global restock_shops #bool
    restock_ticks += 1
    if restock_ticks < 0:
        restock_ticks = 0
        if restock_shops == True:
            print("\n////////////////////////////   shops restocked!   //////////////////////////////\n")
            for npc in all_npcs:
                for item in npc.npc_inventory:
                    # chance = random.randint(0,1)
                    if chance == 1:
                        npc.npc_inventory.remove(item)
                        print(item.name + " removed from " + npc.first_name + npc.last_name)
                for item in items_shop_table:
                    # item_chance = random.randint(0,1)
                    if item_chance == 1:
                        npc.npc_inventory.append(item)
                        print(item.name + " appended to " + npc.first_name + npc.last_name)


#############################----COMBAT_FUNCTIONS----#########################

def func_choose_enemy():

    combat_mod = random.randint(0,100)
    combat_rating = random.randint(0,100)
    if dev_mode != 0:
        print("Combat mod:", combat_mod)
        print("Combat rating:", combat_rating)

    if dev_mode <= 10:
    #rolls for which enemy to fight
        if steps_z == 0: #check if on surface
            for scene_type in location:
                if scene_type.difficulty == 0:
                    if combat_mod < 25:
                        if combat_rating >= 0 and combat_rating < 25:
                            current_enemies.append(goblin)
                        if combat_rating >= 25 and combat_rating < 50:
                            current_enemies.append(goblin)
                            current_enemies.append(hobgoblin)
                        if combat_rating >= 50 and combat_rating < 75:
                            current_enemies.append(bandit)
                        if combat_rating >= 75 and combat_rating <= 100:
                            current_enemies.append(bandit)
                            current_enemies.append(goblin)

                    if combat_mod >= 25 and combat_mod < 50:
                        if combat_rating >= 0 and combat_rating < 25:
                            current_enemies.append(fire_elemental)
                        if combat_rating >= 25 and combat_rating < 50:
                            current_enemies.append(bandit)
                        if combat_rating >= 50 and combat_rating < 75:
                            current_enemies.append(bandit)
                            current_enemies.append(hobgoblin)
                            current_enemies.append(goblin)
                        if combat_rating >= 75 and combat_rating <= 100:
                            current_enemies.append(hobgoblin)
                            current_enemies.append(goblin)

                    if combat_mod >= 50 and combat_mod < 75:
                        if combat_rating >= 0 and combat_rating < 25:
                            current_enemies.append(fire_elemental)
                        if combat_rating >= 25 and combat_rating < 50:
                            current_enemies.append(water_elemental)
                        if combat_rating >= 50 and combat_rating < 75:
                            current_enemies.append(water_elemental)
                            current_enemies.append(fire_elemental)
                        if combat_rating >= 75 and combat_rating <= 100:
                            current_enemies.append(hobgoblin)
                            current_enemies.append(fire_elemental)
                            current_enemies.append(water_elemental)

                    if combat_mod >= 75 and combat_mod < 90:
                        if combat_rating >= 0 and combat_rating < 25:
                            current_enemies.append(goblin)
                            current_enemies.append(goblin)
                        if combat_rating >= 25 and combat_rating < 50:
                            current_enemies.append(goblin)
                            current_enemies.append(hobgoblin)
                            current_enemies.append(hobgoblin)
                        if combat_rating >= 50 and combat_rating < 75:
                            current_enemies.append(bandit)
                            current_enemies.append(bandit)
                            current_enemies.append(bandit)
                        if combat_rating >= 75 and combat_rating <= 100:
                            current_enemies.append(goblin)

                    if combat_mod >= 90 and combat_mod <= 100:
                        if combat_rating >= 0 and combat_rating < 25:
                            current_enemies.append(fire_elemental)
                            current_enemies.append(water_elemental)
                            current_enemies.append(earth_elemental)
                        if combat_rating >= 25 and combat_rating < 50:
                            current_enemies.append(legion_spearman)
                            current_enemies.append(legion_soldier)
                        if combat_rating >= 50 and combat_rating < 75:
                            current_enemies.append(legion_spearman)
                            current_enemies.append(legion_soldier)
                        if combat_rating >= 75 and combat_rating <= 100:
                            current_enemies.append(bird_warrior)

                if scene_type.difficulty >= 1:
                    if combat_mod < 25:
                        if combat_rating >= 0 and combat_rating < 25:
                            current_enemies.append(goblin)
                        if combat_rating >= 25 and combat_rating < 50:
                            current_enemies.append(goblin)
                            current_enemies.append(hobgoblin)
                        if combat_rating >= 50 and combat_rating < 75:
                            current_enemies.append(bandit)
                        if combat_rating >= 75 and combat_rating <= 100:
                            current_enemies.append(bandit)
                            current_enemies.append(goblin)

                    if combat_mod >= 25 and combat_mod < 50:
                        if combat_rating >= 0 and combat_rating < 25:
                            current_enemies.append(fire_elemental)
                        if combat_rating >= 25 and combat_rating < 50:
                            current_enemies.append(bandit)
                        if combat_rating >= 50 and combat_rating < 75:
                            current_enemies.append(bandit)
                            current_enemies.append(hobgoblin)
                            current_enemies.append(goblin)
                        if combat_rating >= 75 and combat_rating <= 100:
                            current_enemies.append(hobgoblin)
                            current_enemies.append(goblin)

                    if combat_mod >= 50 and combat_mod < 75:
                        if combat_rating >= 0 and combat_rating < 25:
                            current_enemies.append(fire_elemental)
                        if combat_rating >= 25 and combat_rating < 50:
                            current_enemies.append(water_elemental)
                        if combat_rating >= 50 and combat_rating < 75:
                            current_enemies.append(water_elemental)
                            current_enemies.append(fire_elemental)
                        if combat_rating >= 75 and combat_rating <= 100:
                            current_enemies.append(hobgoblin)
                            current_enemies.append(fire_elemental)
                            current_enemies.append(water_elemental)

                    if combat_mod >= 75 and combat_mod < 90:
                        if combat_rating >= 0 and combat_rating < 25:
                            current_enemies.append(legion_soldier)
                        if combat_rating >= 25 and combat_rating < 50:
                            current_enemies.append(legion_spearman)
                        if combat_rating >= 50 and combat_rating < 75:
                            current_enemies.append(legion_spearman)
                            current_enemies.append(legion_soldier)
                        if combat_rating >= 75 and combat_rating <= 100:
                            current_enemies.append(mushroom_man)

                    if combat_mod >= 90 and combat_mod <= 100:
                        if combat_rating >= 0 and combat_rating < 25:
                            current_enemies.append(fire_elemental)
                            current_enemies.append(water_elemental)
                            current_enemies.append(earth_elemental)
                        if combat_rating >= 25 and combat_rating < 50:
                            current_enemies.append(legion_spearman)
                            current_enemies.append(legion_soldier)
                        if combat_rating >= 50 and combat_rating < 75:
                            current_enemies.append(legion_spearman)
                            current_enemies.append(legion_soldier)
                        if combat_rating >= 75 and combat_rating <= 100:
                            current_enemies.append(bird_warrior)

        if steps_z <= -1: #check if underground
            for scene_type in location:
                if scene_type.difficulty == 0:
                    if combat_mod < 25:
                        if combat_rating >= 0 and combat_rating < 25:
                            current_enemies.append(earth_elemental)
                        if combat_rating >= 25 and combat_rating < 50:
                            current_enemies.append(giant_snail)
                        if combat_rating >= 50 and combat_rating < 75:
                            current_enemies.append(giant_moth)
                            current_enemies.append(earth_elemental)
                        if combat_rating >= 75 and combat_rating <= 100:
                            current_enemies.append(giant_spider)

                    if combat_mod >= 25 and combat_mod <= 50:
                        if combat_rating >= 0 and combat_rating < 25:
                            current_enemies.append(hobgoblin)
                        if combat_rating >= 25 and combat_rating < 50:
                            current_enemies.append(giant_snail)
                        if combat_rating >= 50 and combat_rating < 75:
                            current_enemies.append(giant_moth)
                            current_enemies.append(giant_snail)
                        if combat_rating >= 75 and combat_rating <= 100:
                            current_enemies.append(giant_spider)
                            current_enemies.append(giant_snail)

                    if combat_mod >= 50 and combat_mod <= 75:
                        if combat_rating >= 0 and combat_rating < 25:
                            current_enemies.append(earth_elemental)
                            current_enemies.append(giant_snail)
                        if combat_rating >= 25 and combat_rating < 50:
                            current_enemies.append(big_slug)
                        if combat_rating >= 50 and combat_rating < 75:
                            current_enemies.append(skeleton_warrior)
                        if combat_rating >= 75 and combat_rating <= 100:
                            current_enemies.append(skeleton_mage)

                    if combat_mod >= 75 and combat_mod <= 100:
                        if combat_rating >= 0 and combat_rating < 25:
                            current_enemies.append(hobgoblin)
                            current_enemies.append(earth_elemental)
                        if combat_rating >= 25 and combat_rating < 50:
                            current_enemies.append(big_slug)
                            current_enemies.append(big_slug)
                        if combat_rating >= 50 and combat_rating < 75:
                            current_enemies.append(skeleton_warrior)
                        if combat_rating >= 75 and combat_rating <= 100:
                            current_enemies.append(skeleton_mage)
                            current_enemies.append(skeleton_warrior)

def func_enemy_dead(enemy_stats):

            print("\n// " + enemy_stats.name.upper() + " IS DEAD! // \n")
            sleep(sleep_time)
            player1.gp = player1.gp + enemy_stats.gp
            player1.xp = player1.xp + enemy_stats.xp
            print(enemy_stats.gp)
            print("gold obtained \n")
            sleep(sleep_time)
            print(enemy_stats.xp)
            print("xp obtained \n")
            sleep(sleep_time)

            loot_spawn_chance_item = 1
            loot_chance_item = 0
            loot_amount_item = 0
            loot_spawn_chance_weapon = 1
            loot_chance_weapon = 0
            loot_amount_weapon = 0

            loot_spawn_chance_armor = 1
            loot_chance_armor = 0
            loot_amount_armor = 0

            loot_spawn_chance_helmet = 1
            loot_chance_helmet = 0
            loot_amount_helmet = 0

            loot_spawn_chance_shield = 1
            loot_chance_shield = 0
            loot_amount_shield = 0

            loot_quality = 0

            # loot_spawn_chance_item = random.randint(0,1)
            # loot_spawn_chance_weapon = random.randint(0,1)
            # loot_spawn_chance_armor = random.randint(0,1)
            # loot_spawn_chance_helmet = random.randint(0,1)
            # loot_spawn_chance_shield = random.randint(0,1)

            if loot_spawn_chance_item == 1:
                if len(enemy_stats.drop_table_items) != 0:
                    for item in enemy_stats.drop_table_items:
                        loot_chance_item = random.randint(0,1)
                        if loot_chance_item == 1:
                            for ground_item in all_ground_game_items:
                                if ground_item.name == item.name:
                                    scene_type.scene_inventory.append(ground_item)
                                    print(enemy_stats.name + " dropped " + item.print_name + " \n")
                                    sleep(sleep_time_fast)
                            loot_amount_item = random.randint(0,5)
                            if loot_amount_item != 5:
                                break

            if loot_spawn_chance_weapon == 1:
                if len(enemy_stats.drop_table_weapons) != 0:
                    for weapon in enemy_stats.drop_table_weapons:
                        loot_chance_weapon = random.randint(0,1)
                        if loot_chance_weapon == 1:
                            for ground_weapon in all_ground_game_weapons:
                                if ground_weapon.name == weapon.name:
                                    scene_type.scene_weapon_inventory.append(ground_weapon)
                                    print(enemy_stats.name + " dropped " + weapon.print_name + " \n" )
                                    sleep(sleep_time_fast)
                            loot_amount_weapon = random.randint(0,10)
                            if loot_amount_weapon != 10:
                                break

            if loot_spawn_chance_armor == 1:
                if len(enemy_stats.drop_table_armor) != 0:
                    for armor in enemy_stats.drop_table_armor:
                        loot_chance_armor = random.randint(0,1)
                        if loot_chance_armor == 1:
                            for ground_armor in all_ground_game_armor:
                                if ground_armor.name == armor.name:
                                    scene_type.scene_armor_inventory.append(ground_armor)
                                    print(enemy_stats.name + " dropped " + armor.print_name + " \n" )
                                    sleep(sleep_time_fast)
                            loot_amount_armor = random.randint(0,10)
                            if loot_amount_armor != 10:
                                break

            if loot_spawn_chance_helmet == 1:
                if len(enemy_stats.drop_table_helmets) != 0:
                    for helmet in enemy_stats.drop_table_helmets:
                        loot_chance_helmet = random.randint(0,1)
                        if loot_chance_helmet == 1:
                            for ground_helmet in all_ground_game_helmets:
                                if ground_helmet.name == helmet.name:
                                    scene_type.scene_helmet_inventory.append(ground_helmet)
                                    print(enemy_stats.name + " dropped " + helmet.print_name + " \n" )
                                    sleep(sleep_time_fast)
                            loot_amount_helmet = random.randint(0,10)
                            if loot_amount_helmet != 10:
                                break

            if loot_spawn_chance_shield == 1:
                if len(enemy_stats.drop_table_shields) != 0:
                    for shield in enemy_stats.drop_table_shields:
                        loot_chance_shield = random.randint(0,1)
                        if loot_chance_shield == 1:
                            for ground_shield in all_ground_game_shields:
                                if ground_shield.name == shield.name:
                                    scene_type.scene_shield_inventory.append(ground_shield)
                                    print(enemy_stats.name + " dropped " + shield.print_name + " \n" )
                                    sleep(sleep_time_fast)
                            loot_amount_shield = random.randint(0,10)
                            if loot_amount_shield != 10:
                                break

            func_check_level()

def func_get_target():
    if len(current_enemies) > 1:
        print("")
        for enemy_stats in current_enemies:
            print("|| " + str((current_enemies.index(enemy_stats)+1)) + " || " + enemy_stats.name + " || " + enemy_stats.attribute)
        target_input = input("\nWho will you attack? \n")
        if target_input.isdigit():
            val_target_input = int(target_input)
            val_enemy = val_target_input - 1
            for enemy_stats in current_enemies:
                if val_enemy == current_enemies.index(enemy_stats):
                    target = enemy_stats.name
        else:
            for enemy_stats in current_enemies:
                if enemy_stats.name == target_input:
                    target = enemy_stats.name
    else:
        for enemy_stats in current_enemies:
            target = enemy_stats.name

    return target

def func_player_melee():
    target = func_get_target()
    for enemy_stats in current_enemies:
        if enemy_stats.name == target:
            player_weapon_level = 0
            for weapon in equiped_weapon:
                player_weapon_level = weapon.level
            player_damage = (player1.attack + player1.attack_bonus + player_weapon_level) * (player1.strength + player1.strength_bonus + player_weapon_level)
            if player_damage > (enemy_stats.hp):
                player_damage = (enemy_stats.hp)
            enemy_stats.hp = enemy_stats.hp - player_damage
            print("\nyou hit " + enemy_stats.name + " for: " + Fore.RED + Style.BRIGHT + str(player_damage) + Style.RESET_ALL + " melee damage!")
            sleep(sleep_time)
            player1.attack_xp += (player1.attack * (player_damage))
            player1.strength_xp += (player1.strength * (player_damage + player1.strength))

def func_player_spell():

    spell_damage = 0
    for spell in equiped_spells:
        spell_found = False

        if val == equiped_spells.index(spell):
            spell_found = True

        if spell.name == spell_input:
            spell_found = True

        if spell_found == True:
            if spell.effect == 0:
                target = func_get_target()
                for enemy_stats in current_enemies:
                    if enemy_stats.name == target:
                        spell_damage = spell.damage
                        print("\nyou cast " + spell.print_name)
                        sleep(sleep_time)
                        player_damage = (player1.level + spell_damage) * (player1.magic + player1.magic_bonus)
                        if spell.attribute == enemy_stats.weakness or spell.attribute == enemy_stats.attribute:
                            if spell.attribute == enemy_stats.weakness:
                                print("it's super effective")
                                sleep(sleep_time)
                                player_damage = player_damage * 2
                            if spell.attribute == enemy_stats.attribute:
                                print("it's not very effective")
                                sleep(sleep_time)
                                player_damage = player_damage // 2
                        if player_damage > (enemy_stats.hp):
                            player_damage = (enemy_stats.hp)
                        enemy_stats.hp = enemy_stats.hp - player_damage
                        print("\nyou hit " + enemy_stats.name + " for " + Fore.RED + Style.BRIGHT + str(player_damage) + " " + spell.print_attribute + " " + "damage!")
                        sleep(sleep_time)
                        player1.magic_xp += (player1.magic + spell.xp + spell.damage)
            if spell.effect == 1:
                spell_healing = spell.damage
                print("you cast " + spell.print_name)
                sleep(sleep_time)
                player_healing = (player1.level + spell_healing) * (player1.magic + player1.magic_bonus)
                player_stats.hp = player_stats.hp + player_healing
                if player_stats.hp > player_stats.maxhp:
                    player_stats.hp = player_stats.maxhp
                print("\nyou heal for:" + Fore.GREEN + Style.BRIGHT + str(player_healing))
                sleep(sleep_time)
                player1.magic_xp += (player1.magic + spell.xp + spell.damage)
            if spell.effect == 2:
                target = func_get_target()
                for enemy_stats in current_enemies:
                    if enemy_stats.name == target:
                        print("you cast " + spell.print_name)
                        enemy_stats.status_effect = 2
                        print("you freeze the " + enemy_stats.name)
                        sleep(sleep_time)
            if spell.effect == 3:
                target = func_get_target()
                for enemy_stats in current_enemies:
                    if enemy_stats.name == target:
                        print("you cast " + spell.print_name)
                        enemy_stats.status_effect = 3
                        print("you poison the " + enemy_stats.name)
                        sleep(sleep_time)
            if spell.effect == 4:
                target = func_get_target()
                for enemy_stats in current_enemies:
                    if enemy_stats.name == target:
                        print("you cast " + spell.print_name)
                        enemy_stats.status_effect = 4
                        print("you burn the " + enemy_stats.name)
                        sleep(sleep_time)
    func_check_level()

def func_player_spell_non_combat():
    for spell in equiped_spells:
        if spell.name == spell_input:
            if spell.effect == 0:

                print("\nyou are not in combat...")

            if spell.effect == 1:
                spell_healing = spell.damage
                print("you cast " + spell.print_name)
                player_healing = (player1.level + spell_healing) * (player1.magic + player1.magic_bonus)
                player_stats.hp = player_stats.hp + player_healing
                if player_stats.hp > player_stats.maxhp:
                    player_stats.hp = player_stats.maxhp
                print("\nspell healing: ")
                print(spell_healing)
                print("\nyou heal for:")
                print(player_healing)
                player1.magic_xp += (player_healing)

def func_player_status_check_melee():
    for player_stats in players:
        if player_stats.status_effect == 0:
            func_player_melee()

        if player_stats.status_effect == 2:
            print("you are frozen and cannot move \n")
            sleep(sleep_time)
            defrost_chance = random.randint(0,1)
            if defrost_chance == 0:
                player_stats.status_effect = 0
                print("you broke free from the ice\n")
                sleep(sleep_time)

                func_player_melee()

            else:
                player_stats.status_effect = 2
                print("you are still trapped by ice\n")
                sleep(sleep_time)

        if player_stats.status_effect == 3:
            player_poison_damage = (player_stats.maxhp/10) - ((player_stats.strength/10) + (player_stats.maxhp/100))
            player_stats.hp -= player_poison_damage
            print("you took poison damage of:")
            print(player_poison_damage)
            sleep(sleep_time)

            func_player_melee()

        if player_stats.status_effect == 4:
            player_burn_damage = (player_stats.maxhp/10)
            player_stats.hp -= player_burn_damage
            print("you took burn damage of:")
            print(player_burn_damage)
            sleep(sleep_time)

            func_player_melee()

def func_player_status_check_spell():
    for player_stats in players:
        if player_stats.status_effect == 0:
            func_player_spell()

        if player_stats.status_effect == 2:
            print("you are frozen and cannot move \n")
            defrost_chance = random.randint(0,1)
            if defrost_chance == 0:
                player_stats.status_effect = 0
                print("you broke free from the ice\n")

                func_player_spell()
            else:
                player_stats.status_effect = 2
                print("you are still trapped by ice\n")

        if player_stats.status_effect == 3:
            player_poison_damage = (player_stats.maxhp/10) - ((player_stats.strength/10) + (player_stats.maxhp/100))
            player_stats.hp -= player_poison_damage
            print("you took poison damage of:")
            print(player_poison_damage)

            func_player_spell()

        if player_stats.status_effect == 4:
            player_burn_damage = (player_stats.maxhp/10)
            player_stats.hp -= player_burn_damage
            print("you took burn damage of:")
            print(player_burn_damage)

            func_player_spell()

def func_enemy_status_check():
    for enemy_stats in current_enemies:
        if enemy_stats.status_effect == 0:
            func_enemy_attack(enemy_stats)

        if enemy_stats.status_effect == 2:
            print("the " + enemy_stats.name + " is frozen and cannot move \n")
            sleep(sleep_time)
            defrost_chance = random.randint(0,1)
            if defrost_chance == 0:
                enemy_stats.status_effect = 0
                print("the " + enemy_stats.name + " broke free!\n")
                sleep(sleep_time)
            else:
                enemy_stats.status_effect = 1
                print("the " + enemy_stats.name + " is trapped by ice\n")
                sleep(sleep_time)

        if enemy_stats.status_effect == 3:
            enemy_poison_damage = (enemy_stats.maxhp/10)
            enemy_stats.hp -= enemy_poison_damage
            print("enemy took poison damage of:")
            print(enemy_poison_damage)
            sleep(sleep_time)
            func_check_enemy_dead()
            func_enemy_attack()

        if enemy_stats.status_effect == 4:
            enemy_burn_damage = (enemy_stats.maxhp/10)
            enemy_stats.hp -= enemy_burn_damage
            print("enemy took burn damage of:")
            print(enemy_burn_damage)
            sleep(sleep_time)
            func_check_enemy_dead()
            func_enemy_attack()

def func_check_enemy_dead():
    global in_fight
    global npc_fight
    for enemy_stats in current_enemies:
        if enemy_stats.hp <= 0:
            current_enemies.remove(enemy_stats)
            func_enemy_dead(enemy_stats)
    if len(current_enemies) == 0:
        in_fight = False
        for scene_type in location:
            for npc in scene_type.npc_list:
                if npc_enemy_fname == npc.first_name and npc_enemy_lname == npc.last_name:
                    print("\n" + npc.first_name + "" + npc.last_name + " is dead...")
                    scene_type.npc_list.remove(npc)
                    npc_fight = False

def func_enemy_attack(enemy_stats):
    if (not enemy_stats.spellbook):
        func_enemy_melee(enemy_stats)
    else:
        player_magic_level = 0
        player_defence_level = 0
        enemy_spell_damage = 0
        spell_damage = 0

        player_magic_level = player1.magic
        player_defence_level = player1.defence
        for spell in enemy_stats.spellbook:
            spellchance = random.randint(0,1)
            if spell.effect >= 2 and spell.effect == player1.status_effect:
                spellchance = 0
            if spellchance == 1:
                if spell.effect == 0 or spell.effect == -1:
                    print("\n" + enemy_stats.name + " casts:")
                    print(spell.print_name)
                    sleep(sleep_time)
                    spell_damage = spell.damage
                    enemy_spell_damage = (enemy_stats.level + spell_damage) * enemy_stats.magic
                    enemy_spell_damage = enemy_spell_damage // (player1.magic + player1.defence + player1.defence_bonus // 10)
                    player1.hp = player1.hp - (enemy_spell_damage)
                    print("\n" + enemy_stats.name + " hit you for " + Fore.RED + Style.BRIGHT + str(enemy_spell_damage) + Style.RESET_ALL + " " + spell.print_attribute + " " + "damage!")
                    if spell.effect == -1:
                        print("\n" + enemy_stats.name + " heals for: " + Fore.GREEN + Style.BRIGHT + str(enemy_spell_damage))
                    sleep(sleep_time)
                    if player1.hp <= 0:
                        print("\nYOU ARE DEAD! \n")
                        in_fight = False
                        del current_enemies[:]
                        game_start = 0
                    break
                if spell.effect == 1:
                    spell_healing = spell.damage
                    print("\n" + enemy_stats.name + " casts :")
                    print(spell.print_name)
                    sleep(sleep_time)
                    enemy_healing = (enemy_stats.level + spell_healing) * enemy_stats.magic
                    enemy_stats.hp = enemy_stats.hp + enemy_healing
                    if enemy_stats.hp > enemy_stats.maxhp:
                        enemy_stats.hp = enemy_stats.maxhp
                    print("\n" + enemy_stats.name + " heals for:" + Fore.GREEN + Style.BRIGHT + str(enemy_healing))
                    sleep(sleep_time)
                    break
                if spell.effect == 2:
                    print("\n" + enemy_stats.name + " casts :")
                    print(spell.print_name)
                    sleep(sleep_time)
                    for player_stats in players:
                        player_stats.status_effect = 2
                    print("you were frozen by the " + enemy_stats.name)
                    sleep(sleep_time)
                    break
                if spell.effect == 3:
                    print("\n" + enemy_stats.name + " casts :")
                    print(spell.print_name)
                    sleep(sleep_time)
                    for player_stats in players:
                        player_stats.status_effect = 3
                    print("you were poisoned by the " + enemy_stats.name)
                    sleep(sleep_time)
                    break
                if spell.effect == 4:
                    print("\n" + enemy_stats.name + " casts :")
                    print(spell.print_name)
                    sleep(sleep_time)
                    for player_stats in players:
                        player_stats.status_effect = 4
                    print("you were burnt by the " + enemy_stats.name)
                    sleep(sleep_time)
                    break
                break
            else:
                func_enemy_melee(enemy_stats)
                break

def func_enemy_melee(enemy_stats):
    for player_stats in players:
        player_armor_level = 0
        enemy_damage = 0
        for armor in equiped_armor:
            player_armor_level = armor.level
        enemy_damage = (enemy_stats.attack * enemy_stats.strength)
        enemy_damage = (enemy_damage * enemy_damage)//(player_armor_level + player1.defence + player1.defence_bonus)
        player_stats.hp = player_stats.hp - enemy_damage
        print("\n" + enemy_stats.name + " hit you for " + Fore.RED + Style.BRIGHT + str(enemy_damage) + Style.RESET_ALL + " melee damage!" )
        sleep(sleep_time)
        player1.defence_xp += (player1.defence * (enemy_damage))
        if player_stats.hp <= 0:
            print("\nYOU ARE DEAD \n")
            in_fight = False
            del current_enemies[:]
            game_start = 0

#############################--DIALOUGE FUNCTIONS--#######################

def func_get_target_npc():
    for scene_type in location:
        if len(scene_type.npc_list) > 1:
            print("")
            target_npc = "0"
            for npc in scene_type.npc_list:
                print("|| " + str((scene_type.npc_list.index(npc)+1)) + " || " + npc.first_name + " " + npc.last_name + ", " + npc.title + " || " + npc.npc_desc)
            target_input = input("\nWho will you talk too? \n")
            if target_input.isdigit():
                val_target_input = int(target_input)
                val_npc = val_target_input - 1
                for npc in scene_type.npc_list:
                    if val_npc == scene_type.npc_list.index(npc):
                        target_npc = npc.first_name
            else:
                for npc in scene_type.npc_list:
                    if npc.first_name == target_input:
                        target_npc = npc.first_name
        else:
            for npc in scene_type.npc_list:
                target_npc = npc.first_name

        return target_npc

def func_get_target_dialouge():
    if len(npc.dialouge_options_list) > 1:
        print("")
        target_dialouge = "0"
        for dialouge_option in npc.dialouge_options_list:
            print("|| " + str((npc.dialouge_options_list.index(dialouge_option)+1)) + " || " + dialouge_option.text)
        target_input = input("\nWhat will you say? \n")
        if target_input.isdigit():
            val_target_input = int(target_input)
            val_dialouge = val_target_input - 1
            for dialouge_option in npc.dialouge_options_list:
                if val_dialouge == npc.dialouge_options_list.index(dialouge_option):
                    target_dialouge = dialouge_option.text
        else:
                for dialouge_option in npc.dialouge_options_list:
                    if dialouge_option.text == target_input:
                        target_dialouge = dialouge_option.text
    else:
        for dialouge_option in npc.dialouge_options_list:
            target_dialouge = dialouge_option.text

    return target_dialouge

def func_shop(gear,npc_gear_inv):
    target_gear = "0"
    if player1.gp != -1:
        if game_start == 1:
            print("gold: ", player1.gp)
            print("shop inventory:\n")
            for gear in npc_gear_inv:
                if gear in all_game_weapons:
                    print("|| " + str((npc_gear_inv.index(gear)+1)) + " || " + gear.print_name + " || " + gear.print_attribute + " || lvl: " + str(gear.level) + " || " + str(gear.value) + " gp. ")
                if gear in all_game_armor:
                    print("|| " + str((npc_gear_inv.index(gear)+1)) + " || " + gear.print_name + " || " + gear.print_attribute + " || lvl: " + str(gear.level) + " || " + str(gear.value) + " gp. ")
                if gear in all_game_helmets:
                    print("|| " + str((npc_gear_inv.index(gear)+1)) + " || " + gear.print_name + " || " + gear.print_attribute + " || lvl: " + str(gear.level) + " || " + str(gear.value) + " gp. ")
                if gear in all_game_shields:
                    print("|| " + str((npc_gear_inv.index(gear)+1)) + " || " + gear.print_name + " || " + gear.print_attribute + " || lvl: " + str(gear.level) + " || " + str(gear.value) + " gp. ")
                if gear in all_game_items:
                    print("|| " + str((npc_gear_inv.index(gear)+1)) + " || " + gear.print_name + " || " + str(gear.value) + " gp. ")
                if gear in all_game_spells:
                    print("|| " + str((npc_gear_inv.index(gear)+1)) + " || " + gear.print_name + " || " + gear.print_attribute + " || " + str(gear.value) + " gp. ")

            bought_item = input("please, choose an item to buy\n")
            if bought_item.isdigit():
                val_bought_item = int(bought_item)
                val_shop = val_bought_item - 1
                for gear in npc_gear_inv:
                    if val_shop == npc_gear_inv.index(gear):
                        target_gear = gear.name
            else:
                    for gear in npc_gear_inv:
                        if gear.name == bought_item:
                            target_gear = gear.name
            has_item = False
            for gear in npc_gear_inv:
                if target_gear == gear.name:
                    has_item = True
                    if player1.gp >= gear.value:
                        player1.gp -= gear.value
                        if gear in all_game_weapons:
                            weapon_inventory.append(gear)
                        if gear in all_game_armor:
                            armor_inventory.append(gear)
                        if gear in all_game_helmets:
                            helmet_inventory.append(gear)
                        if gear in all_game_shields:
                            shield_inventory.append(gear)
                        if gear in all_game_items:
                            inventory.append(gear)
                        if gear in all_game_spells:
                            spell_inventory.append(gear)
                        print("\nthanks, enjoy your " + gear.name + "\n")
                    else:
                        print("You can't afford that!")

            if has_item == False:
                print("I don't have " + bought_item + " i'm sorry.\n")
        else:
            print("game_start = 0 func_shop aborted")
    else:
        print("gp = -1, func_shop aborted")

def func_sell(gear,player_gear_inv):
    target_gear = "0"
    for gear in player_gear_inv:
        if gear in all_game_weapons:
            print("|| " + str((player_gear_inv.index(gear)+1)) + " || " + gear.print_name + " || " + gear.print_attribute + " || lvl: " + str(gear.level) + " || " + str(gear.value) + " gp. ")
        if gear in all_game_armor:
            print("|| " + str((player_gear_inv.index(gear)+1)) + " || " + gear.print_name + " || " + gear.print_attribute + " || lvl: " + str(gear.level) + " || " + str(gear.value) + " gp. ")
        if gear in all_game_helmets:
            print("|| " + str((player_gear_inv.index(gear)+1)) + " || " + gear.print_name + " || " + gear.print_attribute + " || lvl: " + str(gear.level) + " || " + str(gear.value) + " gp. ")
        if gear in all_game_shields:
            print("|| " + str((player_gear_inv.index(gear)+1)) + " || " + gear.print_name + " || " + gear.print_attribute + " || lvl: " + str(gear.level) + " || " + str(gear.value) + " gp. ")
        if gear in all_game_items:
            print("|| " + str((player_gear_inv.index(gear)+1)) + " || " + gear.print_name + " || " + str(gear.value) + " gp. ")
        if gear in all_game_spells:
            print("|| " + str((player_gear_inv.index(gear)+1)) + " || " + gear.print_name + " || " + gear.print_attribute + " || " + str(gear.value) + " gp. ")

    sold_item = input("\nwhat do you want to sell\n")
    has_item = False
    if sold_item.isdigit():
        val_sold_item = int(sold_item)
        val_sell = val_sold_item - 1
        for gear in player_gear_inv:
            if val_sell == player_gear_inv.index(gear):
                target_gear = gear.name
    else:
        for gear in player_gear_inv:
            if gear.name == sold_item:
                target_gear = gear.name

    for gear in player_gear_inv:
        if target_gear == gear.name:
            has_item = True
            print("you sold " + gear.print_name + " for " + str(gear.value) + " gp.\n")
            player1.gp += gear.value
            player_gear_inv.remove(gear)
            break

#############################----SCENE_FUNCTIONS----#########################
def func_tp(x,y,z):
    global steps_x
    global steps_y
    global steps_z

    steps_x = x
    steps_y = y
    steps_z = z

    if dev_mode >= 1:
        print("you teleported to: ",x,y,z)

def func_drop(gear,player_gear_inv):
    target_gear = "0"
    for gear in player_gear_inv:
        if gear in all_game_weapons:
            print("|| " + str((player_gear_inv.index(gear)+1)) + " || " + gear.print_name + " || " + gear.print_attribute + " || lvl: " + str(gear.level) + " || " + str(gear.value) + " gp. ")
        if gear in all_game_armor:
            print("|| " + str((player_gear_inv.index(gear)+1)) + " || " + gear.print_name + " || " + gear.print_attribute + " || lvl: " + str(gear.level) + " || " + str(gear.value) + " gp. ")
        if gear in all_game_helmets:
            print("|| " + str((player_gear_inv.index(gear)+1)) + " || " + gear.print_name + " || " + gear.print_attribute + " || lvl: " + str(gear.level) + " || " + str(gear.value) + " gp. ")
        if gear in all_game_shields:
            print("|| " + str((player_gear_inv.index(gear)+1)) + " || " + gear.print_name + " || " + gear.print_attribute + " || lvl: " + str(gear.level) + " || " + str(gear.value) + " gp. ")
        if gear in all_game_items:
            print("|| " + str((player_gear_inv.index(gear)+1)) + " || " + gear.print_name + " || " + str(gear.value) + " gp. ")
        if gear in all_game_spells:
            print("|| " + str((player_gear_inv.index(gear)+1)) + " || " + gear.print_name + " || " + gear.print_attribute + " || " + str(gear.value) + " gp. ")

    dropped_item = input("\nwhat do you want to drop\n")
    has_item = False
    if dropped_item.isdigit():
        val_dropped_item = int(dropped_item)
        val_drop = val_dropped_item - 1
        for gear in player_gear_inv:
            if val_drop == player_gear_inv.index(gear):
                target_gear = gear.name
    else:
        for gear in player_gear_inv:
            if gear.name == dropped_item:
                target_gear = gear.name

    for gear in player_gear_inv:
        if target_gear == gear.name:
            has_item = True
            print("you drop " + gear.print_name + "\n")
            player_gear_inv.remove(gear)
            break
    if has_item == True:
        for ground_item in all_ground_game_items:
            if ground_item.name == target_gear:
                scene_type.scene_inventory.append(ground_item)
                break

def func_search_treasure():
            scene_difficulty = 0
            for scene_type in location:
                scene_difficulty = scene_type.difficulty

            loot_spawn_chance_item = 0
            loot_chance_item = 0
            loot_amount_item = 0
            loot_spawn_chance_weapon = 0
            loot_chance_weapon = 0
            loot_amount_weapon = 0

            loot_spawn_chance_armor = 0
            loot_chance_armor = 0
            loot_amount_armor = 0

            loot_spawn_chance_helmet = 0
            loot_chance_helmet = 0
            loot_amount_helmet = 0

            loot_spawn_chance_shield = 0
            loot_chance_shield = 0
            loot_amount_shield = 0

            loot_spawn_chance_gp = 0
            loot_amount_gp = 0

            loot_quality = 0

            loot_spawn_chance_item = random.randint(0,1)
            loot_spawn_chance_weapon = random.randint(0,1)
            loot_spawn_chance_armor = random.randint(0,1)
            loot_spawn_chance_helmet = random.randint(0,1)
            loot_spawn_chance_shield = random.randint(0,1)
            loot_spawn_chance_gp = random.randint(0,1)

            noloot = True

            if loot_spawn_chance_item != 1 and loot_spawn_chance_armor != 1 and loot_spawn_chance_helmet != 1 and loot_spawn_chance_shield != 1 and loot_spawn_chance_weapon != 1:
                noloot = True
            else:
                noloot = False

            if loot_spawn_chance_gp == 1 or noloot == True:
                loot_amount_gp = random.randint(1,100) * random.randint(1,10)
                player1.gp = player1.gp + loot_amount_gp
                print(loot_amount_gp)
                print("gold obtained \n")

            if loot_spawn_chance_item == 1:
                if len(items_drop_table) != 0:
                    for item in items_drop_table:
                        loot_chance_item = random.randint(0,1)
                        if loot_chance_item == 1:
                            for ground_item in all_ground_game_items:
                                if ground_item.name == item.name:
                                    scene_type.scene_inventory.append(ground_item)
                                    print("you found " + item.print_name + " \n")
                            loot_amount_item = random.randint(0,1)
                            if loot_amount_item == 1:
                                break

            if loot_spawn_chance_weapon == 1:
                if len(weapons_drop_table) != 0:
                    for weapon in weapons_drop_table:
                        loot_chance_weapon = random.randint(0,1)
                        if loot_chance_weapon == 1:
                            for ground_weapon in all_ground_game_weapons:
                                if ground_weapon.name == weapon.name:
                                    scene_type.scene_weapon_inventory.append(ground_weapon)
                                    print("you found " + weapon.print_name + " \n" )
                            loot_amount_weapon = random.randint(0,1)
                            if loot_amount_weapon == 1:
                                break


            if loot_spawn_chance_armor == 1:
                if len(armor_drop_table) != 0:
                    for armor in armor_drop_table:
                        loot_chance_armor = random.randint(0,1)
                        if loot_chance_armor == 1:
                            for ground_armor in all_ground_game_armor:
                                if ground_armor.name == armor.name:
                                    scene_type.scene_armor_inventory.append(ground_armor)
                                    print("you found " + armor.print_name + " \n" )
                            loot_amount_armor = random.randint(0,1)
                            if loot_amount_armor == 1:
                                break


            if loot_spawn_chance_helmet == 1:
                if len(helmets_drop_table) != 0:
                    for helmet in helmets_drop_table:
                        loot_chance_helmet = random.randint(0,1)
                        if loot_chance_helmet == 1:
                            for ground_helmet in all_ground_game_helmets:
                                if ground_helmet.name == helmet.name:
                                    scene_type.scene_helmet_inventory.append(ground_helmet)
                                    print("you found " + helmet.print_name + " \n" )
                            loot_amount_helmet = random.randint(0,1)
                            if loot_amount_helmet == 1:
                                break


            if loot_spawn_chance_shield == 1:
                if len(shields_drop_table) != 0:
                    for shield in shields_drop_table:
                        loot_chance_shield = random.randint(0,1)
                        if loot_chance_shield == 1:
                            for ground_shield in all_ground_game_shields:
                                if ground_shield.name == shield.name:
                                    scene_type.scene_shield_inventory.append(ground_shield)
                                    print("you found " + shield.print_name + " \n" )
                            loot_amount_shield = random.randint(0,1)
                            if loot_amount_shield == 1:
                                break
            if noloot == True:
                print("\nthere was no equipment here, but at least I found some gold...")
            func_check_level()

def func_rain():
    global raining
    raining += random.randint(-1,1)
    if raining < 0:
        raining = 0
    if raining >= 10:
        raining = 1

def func_check_weather():
    for scene_type in location:
        if season == 0:
            scene_type.temp = (Fore.YELLOW + "hot" + Style.RESET_ALL)
        if season == 1:
            scene_type.temp = (Fore.CYAN + Style.DIM + "chilly" + Style.RESET_ALL)
        if season == 2:
            scene_type.temp = (Fore.CYAN + "very cold" + Style.RESET_ALL)
        if season == 3:
            scene_type.temp = (Fore.GREEN + "temperate" + Style.RESET_ALL)

def func_check_season():
    if months >= 4:
        season = 0
    if months >= 1 and months <= 3:
        season = 0
    if months >= 4 and months <= 6:
        season = 1
    if months >= 7 and months <= 9:
        season = 2
    if months >= 9 and months <= 12:
        season = 3

def func_check_light():
    has_torch = False
    for scene_type in location:
        if steps_z <= -1:
            for item in inventory:
                if item.name == "torch":
                    has_torch = True
                    scene_type.light = (Fore.YELLOW + Style.DIM + " and very dark, but slightly illuminated by your torch" + Style.RESET_ALL)
                else:
                    scene_type.light = (Fore.BLACK + Style.BRIGHT + " and very dark" + Style.RESET_ALL)

        else:
            is_night = False
            if time >= 12:
                is_night = True
            if is_night == True:
                for item in inventory:
                    if item.name == "torch":
                        has_torch = True
                if has_torch == True:
                    if raining == 1 and steps_z >= 0:
                        scene_type.light = (Fore.BLACK + Style.BRIGHT + ", very dark and lightly raining, your torch illuminates the area" + Style.RESET_ALL)
                    if raining >= 2 and steps_z >= 0:
                        scene_type.light = (Fore.BLACK + Style.BRIGHT + ", very dark and raining heavily, your torch illuminates the area" + Style.RESET_ALL)
                    if raining == 0 and steps_z >= 0:
                        scene_type.light = (Fore.YELLOW + Style.DIM + " and very dark, but slightly illuminated by your torch" + Style.RESET_ALL)
                else:
                    if raining == 1 and steps_z >= 0:
                        scene_type.light = (Fore.BLUE + Style.DIM + ", very dark and lightly raining" + Style.RESET_ALL)
                    if raining >= 2 and steps_z >= 0:
                        scene_type.light = (Fore.BLUE + Style.DIM + ", very dark and raining heavily" + Style.RESET_ALL)
                    if raining == 0 and steps_z >= 0:
                        scene_type.light = (Fore.BLACK + Style.BRIGHT + " and very dark" + Style.RESET_ALL)
            if is_night == False and season == 3:
                if raining == 1 and steps_z >= 0:
                    scene_type.light = (Fore.CYAN + Style.DIM + " and lightly raining" + Style.RESET_ALL)
                if raining >= 2 and steps_z >= 0:
                    scene_type.light = (Fore.BLUE + Style.NORMAL + " and raining heavily" + Style.RESET_ALL)
                if raining == 0 and steps_z >= 0:
                    scene_type.light = (Fore.CYAN + Style.DIM + " and very overcast" + Style.RESET_ALL)
            if is_night == False and season != 3:
                if raining == 1 and steps_z >= 0:
                    scene_type.light = (Fore.CYAN + Style.NORMAL + " and lightly raining" + Style.RESET_ALL)
                if raining >= 2 and steps_z >= 0:
                    scene_type.light = (Fore.BLUE + Style.NORMAL + " and raining heavily" + Style.RESET_ALL)
                if raining == 0 and steps_z >= 0:
                    scene_type.light = (Fore.YELLOW + Style.BRIGHT + " and very sunny" + Style.RESET_ALL)

###########################---PLAYER STATS/SKILLS----############################
def func_equip(gear,player_gear_inv,current_gear):
    target_gear = "0"
    for gear in player_gear_inv:
        if gear in all_game_weapons:
            print("|| " + str((player_gear_inv.index(gear)+1)) + " || " + gear.print_name + " || " + gear.print_attribute + " || " + gear.type + " || lvl: " + str(gear.level) + " || " + str(gear.value) + " gp. ")
        if gear in all_game_armor:
            print("|| " + str((player_gear_inv.index(gear)+1)) + " || " + gear.print_name + " || " + gear.print_attribute + " || " + gear.type + " || lvl: " + str(gear.level) + " || " + str(gear.value) + " gp. ")
        if gear in all_game_helmets:
            print("|| " + str((player_gear_inv.index(gear)+1)) + " || " + gear.print_name + " || " + gear.print_attribute + " || " + gear.type + " || lvl: " + str(gear.level) + " || " + str(gear.value) + " gp. ")
        if gear in all_game_shields:
            print("|| " + str((player_gear_inv.index(gear)+1)) + " || " + gear.print_name + " || " + gear.print_attribute + " || " + gear.type + " || lvl: " + str(gear.level) + " || " + str(gear.value) + " gp. ")

        if gear in all_game_spells:
            print("|| " + str((player_gear_inv.index(gear)+1)) + " || " + gear.print_name + " || " + gear.print_attribute + " || lvl: " + str(gear.level) + " || " + str(gear.value) + " gp. ")

    dropped_item = input("\nwhat do you want to equip\n")
    has_gear = False
    if dropped_item.isdigit():
        val_dropped_item = int(dropped_item)
        val_drop = val_dropped_item - 1
        for gear in player_gear_inv:
            if val_drop == player_gear_inv.index(gear):
                target_gear = gear.name
    else:
        for gear in player_gear_inv:
            if gear.name == dropped_item:
                target_gear = gear.name

    for gear in player_gear_inv:
        if target_gear == gear.name:
            has_gear = True #player has the selected gear in their inv

            has_level = False
            has_space = False

            if player1.level < gear.level:
                print("\nYou are not high enough level to equip this!\n")
                has_level = False
            else:
                has_level = True

            if gear in equiped_spells:
                has_space = False
            else:
                has_space = True

            if has_level == True and has_space == True:
                if gear in all_game_weapons:
                    weapon_inventory.remove(gear)
                if gear in all_game_armor:
                    armor_inventory.remove(gear)
                if gear in all_game_helmets:
                    helmet_inventory.remove(gear)
                if gear in all_game_shields:
                    shield_inventory.remove(gear)
                if gear in all_game_spells:
                    spell_inventory.remove(gear)

                del equiped_weapon[:]

                if gear in all_game_weapons:
                    equiped_weapon.append(gear)
                if gear in all_game_armor:
                    equiped_armor.append(gear)
                if gear in all_game_helmets:
                    equiped_helmets.append(gear)
                if gear in all_game_shields:
                    equiped_shields.append(gear)

                if gear in all_game_spells:
                    equiped_spells.append(gear)

                print(gear.name + " equipped!")
                sleep(sleep_time_fast)
                if current_gear != "0":
                    if gear in all_game_weapons:
                        for weapon in all_game_weapons:
                            if weapon.name == current_gear:
                                weapon_inventory.append(weapon)
                    if gear in all_game_armor:
                        for armor in all_game_armor:
                            if armor.name == current_gear:
                                armor_inventory.append(armor)
                    if gear in all_game_helmets:
                        for helmet in all_game_helmets:
                            if helmet.name == current_gear:
                                helmet_inventory.append(helmet)
                    if gear in all_game_shields:
                        for shield in all_game_shields:
                            if shield.name == current_gear:
                                shield_inventory.append(shield)

            if has_level == True and has_space == False:
                print("\nYou already have this spell in your spellbook!\n")
            if has_level == False and has_space == False:
                print("\nYou are not high enough level to equip this!\n")
            if has_level == False and has_space == True:
                print("\nYou are not high enough level to equip this!\n")

def func_inv(gear,player_gear_inv):
    target_gear = "0"
    for gear in player_gear_inv:
        if gear in all_game_weapons:
            print("|| " + str((player_gear_inv.index(gear)+1)) + " || " + gear.print_name + " || " + gear.print_attribute + " || " + gear.type + " || lvl: " + str(gear.level) + " || " + str(gear.value) + " gp. ")
        if gear in all_game_armor:
            print("|| " + str((player_gear_inv.index(gear)+1)) + " || " + gear.print_name + " || " + gear.print_attribute + " || " + gear.type + " || lvl: " + str(gear.level) + " || " + str(gear.value) + " gp. ")
        if gear in all_game_helmets:
            print("|| " + str((player_gear_inv.index(gear)+1)) + " || " + gear.print_name + " || " + gear.print_attribute + " || " + gear.type + " || lvl: " + str(gear.level) + " || " + str(gear.value) + " gp. ")
        if gear in all_game_shields:
            print("|| " + str((player_gear_inv.index(gear)+1)) + " || " + gear.print_name + " || " + gear.print_attribute + " || " + gear.type + " || lvl: " + str(gear.level) + " || " + str(gear.value) + " gp. ")

        if gear in all_game_spells:
            print("|| " + str((player_gear_inv.index(gear)+1)) + " || " + gear.print_name + " || " + gear.print_attribute + " || " + str(gear.value) + " gp. ")

        if gear in all_game_items:
            print("|| " + str((player_gear_inv.index(gear)+1)) + " || " + gear.print_name + " || " + str(gear.value) + " gp. ")

def func_check_stat_bonus():
    for player_stats in players:

        weapon_magic_bonus = 0
        weapon_strength_bonus = 0
        weapon_attack_bonus = 0
        weapon_defence_bonus = 0
        weapon_maxhp_bonus = 0

        armor_magic_bonus = 0
        armor_strength_bonus = 0
        armor_attack_bonus = 0
        armor_defence_bonus = 0
        armor_maxhp_bonus = 0

        helmet_magic_bonus = 0
        helmet_strength_bonus = 0
        helmet_attack_bonus = 0
        helmet_defence_bonus = 0
        helmet_maxhp_bonus = 0

        shield_magic_bonus = 0
        shield_strength_bonus = 0
        shield_attack_bonus = 0
        shield_defence_bonus = 0
        shield_maxhp_bonus = 0

        for weapon in equiped_weapon:
            weapon_magic_bonus = weapon.magic_bonus
            weapon_strength_bonus = weapon.strength_bonus
            weapon_attack_bonus = weapon.attack_bonus
            weapon_defence_bonus = weapon.defence_bonus
            weapon_maxhp_bonus = weapon.maxhp_bonus

        for armor in equiped_armor:
            armor_magic_bonus = armor.magic_bonus
            armor_strength_bonus = armor.strength_bonus
            armor_attack_bonus = armor.attack_bonus
            armor_defence_bonus = armor.defence_bonus
            armor_maxhp_bonus = armor.maxhp_bonus

        for helmet in equiped_helmet:
            helmet_magic_bonus = helmet.magic_bonus
            helmet_strength_bonus = helmet.strength_bonus
            helmet_attack_bonus = helmet.attack_bonus
            helmet_defence_bonus = helmet.defence_bonus
            helmet_maxhp_bonus = helmet.maxhp_bonus

        for shield in equiped_shield:
            shield_magic_bonus = shield.magic_bonus
            shield_strength_bonus = shield.strength_bonus
            shield_attack_bonus = shield.attack_bonus
            shield_defence_bonus = shield.defence_bonus
            shield_maxhp_bonus = shield.maxhp_bonus

        total_magic_bonus = weapon_magic_bonus + armor_magic_bonus + helmet_magic_bonus + shield_magic_bonus
        total_strength_bonus = weapon_strength_bonus + armor_strength_bonus + helmet_strength_bonus + shield_strength_bonus
        total_attack_bonus = weapon_attack_bonus + armor_attack_bonus + helmet_attack_bonus + shield_attack_bonus
        total_defence_bonus = weapon_defence_bonus + armor_defence_bonus + helmet_defence_bonus + shield_defence_bonus
        total_maxhp_bonus = weapon_maxhp_bonus + armor_maxhp_bonus + helmet_maxhp_bonus + shield_maxhp_bonus

        player_stats.magic_bonus = total_magic_bonus
        player_stats.strength_bonus = total_strength_bonus
        player_stats.attack_bonus = total_attack_bonus
        player_stats.defence_bonus = total_defence_bonus
        player_stats.maxhp_bonus = total_maxhp_bonus

def func_check_level():
    sleep(sleep_time_fast)
    for player_stats in players:
        if player_stats.magic_xp >= (player_stats.magic ** 4):
            player_stats.magic += 1
            print("your magic level is now: ", player_stats.magic)
            func_check_level()

        if player_stats.strength_xp >= (player_stats.strength ** 4):
            player_stats.strength += 1
            print("your strength level is now: ", player_stats.strength)
            func_check_level()

        if player_stats.attack_xp >= (player_stats.attack ** 4):
            player_stats.attack += 1
            print("your attack level is now: ", player_stats.attack)
            func_check_level()

        if player_stats.defence_xp >= (player_stats.defence ** 4):
            player_stats.defence += 1
            print("your defence level is now: ", player_stats.defence)
            func_check_level()

        if player_stats.xp >= (player_stats.level ** 2):
            player_stats.level += 1
            print("you are now level: ", player_stats.level)
            func_check_level()

        player_stats.nobonus_maxhp = (player_stats.level * 100) + (player_stats.defence * 25) + (player_stats.strength * 10) + (player_stats.attack * 10) + (player_stats.magic * 10)

        player_stats.nobonus_maxmp = (player_stats.level * 72) + (player_stats.magic * 125)

        player_stats.maxhp = (player_stats.nobonus_maxhp + player_stats.maxhp_bonus)

        player_stats.maxmp = (player_stats.nobonus_maxmp + player_stats.maxmp_bonus)

#######################---PLAYER LOCATION---#######################

def player_keys_check():
    if len(inventory) == 0: #locks all doors if inventory is empty, tile which are passable by default would be unlocked if the player never picks up an item
        large_tree_cave_door.passable = False
        dismurth_bridge.passable = False
    else:
        for item in inventory:
            if item.name == "oak key":
                large_tree_cave_door.passable = True
                break
            else:
                for item.name in large_tree_cave_door.scene_inventory:
                    if item.name == "oak key":
                        large_tree_cave_door.passable = True
                else:
                    large_tree_cave_door.passable = False

        for item in inventory:
            if item.name == "certificate of passage":
                dismurth_bridge.passable = True
                break
            else:
                for item.name in dismurth_bridge.scene_inventory:
                    if item.name == "certificate of passage":
                        dismurth_bridge.passable = True
                else:
                    dismurth_bridge.passable = False

def player_position_check():
    location_found = False
    for scene_type in all_scene_types:
        if steps_y == scene_type.ypos and steps_x == scene_type.xpos and steps_z == scene_type.zpos:
            location_found = True
            del location[:]
            location.append(scene_type)
            break
    if location_found == False:
        if steps_z == 0:
            del location[:]
            location.append(ocean)
        if steps_z <= -1:
            del location[:]
            location.append(solid_cave_wall)

def player_north_check():
    location_found = False
    for scene_type in all_scene_types:
        if steps_y+1 == scene_type.ypos and steps_x == scene_type.xpos and steps_z == scene_type.zpos:
            location_found = True
            del location_north[:]
            location_north.append(scene_type)
            break
    if location_found == False:
        if steps_z == 0:
            del location_north[:]
            location_north.append(ocean)
        if steps_z <= -1 and steps_z >= -3:
            del location_north[:]
            location_north.append(solid_cave_wall)
        if steps_z <= -4 and steps_z >= -6:
            del location_north[:]
            location_north.append(solid_dungeon_wall)
        if steps_z <= -7 and steps_z >= -9:
            del location_north[:]
            location_north.append(solid_dungeon_wall)
        if steps_z <= -10 and steps_z >= -12:
            del location_north[:]
            location_north.append(solid_dungeon_wall)
        if steps_z >= 1:
            del location_north[:]
            location_north.append(sky)

def player_south_check():
    location_found = False
    for scene_type in all_scene_types:
        if steps_y-1 == scene_type.ypos and steps_x == scene_type.xpos and steps_z == scene_type.zpos:
            location_found = True
            del location_south[:]
            location_south.append(scene_type)
            break
    if location_found == False:
        if steps_z == 0:
            del location_south[:]
            location_south.append(ocean)
        if steps_z <= -1 and steps_z >= -3:
            del location_south[:]
            location_south.append(solid_cave_wall)
        if steps_z <= -4 and steps_z >= -6:
            del location_south[:]
            location_south.append(solid_dungeon_wall)
        if steps_z <= -7 and steps_z >= -9:
            del location_south[:]
            location_south.append(solid_dungeon_wall)
        if steps_z <= -10 and steps_z >= -12:
            del location_south[:]
            location_south.append(solid_dungeon_wall)
        if steps_z >= 1:
            del location_south[:]
            location_south.append(sky)

def player_east_check():
    location_found = False
    for scene_type in all_scene_types:
        if steps_y == scene_type.ypos and steps_x+1 == scene_type.xpos and steps_z == scene_type.zpos:
            location_found = True
            del location_east[:]
            location_east.append(scene_type)
            break
    if location_found == False:
        if steps_z == 0:
            del location_east[:]
            location_east.append(ocean)
        if steps_z <= -1 and steps_z >= -3:
            del location_east[:]
            location_east.append(solid_cave_wall)
        if steps_z <= -4 and steps_z >= -6:
            del location_east[:]
            location_east.append(solid_dungeon_wall)
        if steps_z <= -7 and steps_z >= -9:
            del location_east[:]
            location_east.append(solid_dungeon_wall)
        if steps_z <= -10 and steps_z >= -12:
            del location_east[:]
            location_east.append(solid_dungeon_wall)
        if steps_z >= 1:
            del location_east[:]
            location_east.append(sky)

def player_west_check():
    location_found = False
    for scene_type in all_scene_types:
        if steps_y == scene_type.ypos and steps_x-1 == scene_type.xpos and steps_z == scene_type.zpos:
            location_found = True
            del location_west[:]
            location_west.append(scene_type)
            break
    if location_found == False:
        if steps_z == 0:
            del location_west[:]
            location_west.append(ocean)
        if steps_z <= -1 and steps_z >= -3:
            del location_west[:]
            location_west.append(solid_cave_wall)
        if steps_z <= -4 and steps_z >= -6:
            del location_west[:]
            location_west.append(solid_dungeon_wall)
        if steps_z <= -7 and steps_z >= -9:
            del location_west[:]
            location_west.append(solid_dungeon_wall)
        if steps_z <= -10 and steps_z >= -12:
            del location_west[:]
            location_west.append(solid_dungeon_wall)
        if steps_z >= 1:
            del location_west[:]
            location_west.append(sky)

def player_down_check():
    location_found = False
    for scene_type in all_scene_types:
        if steps_y == scene_type.ypos and steps_x == scene_type.xpos and steps_z-1 == scene_type.zpos:
            location_found = True
            del location_down[:]
            location_down.append(scene_type)
            break
    if location_found == False:
        if steps_z == 0:
            del location_down[:]
            location_down.append(ground)
        if steps_z <= -1 and steps_z >= -3:
            del location_down[:]
            location_down.append(solid_cave_ground)
        if steps_z <= -4 and steps_z >= -6:
            del location_down[:]
            location_down.append(solid_dungeon_ground)
        if steps_z <= -7 and steps_z >= -9:
            del location_down[:]
            location_down.append(solid_dungeon_ground)
        if steps_z <= -10 and steps_z >= -12:
            del location_down[:]
            location_down.append(solid_dungeon_ground)
        if steps_z >= 1:
            del location_down[:]
            location_up.append(sky)

def player_up_check():
    location_found = False
    for scene_type in all_scene_types:
        if steps_y == scene_type.ypos and steps_x == scene_type.xpos and steps_z+1 == scene_type.zpos:
            location_found = True
            del location_up[:]
            location_up.append(scene_type)
            break
    if location_found == False:
        if steps_z <= -1 and steps_z >= -3:
            del location_up[:]
            location_up.append(solid_cave_ground)
        if steps_z <= -4 and steps_z >= -6:
            del location_up[:]
            location_up.append(solid_dungeon_ground)
        if steps_z <= -7 and steps_z >= -9:
            del location_up[:]
            location_up.append(solid_dungeon_ground)
        if steps_z <= -10 and steps_z >= -12:
            del location_up[:]
            location_up.append(solid_dungeon_ground)


        if steps_z == 0:
            del location_up[:]
            location_up.append(sky)
        if steps_z >= 1:
            del location_up[:]
            location_up.append(sky)

def location_desc():
    player_position_check()
    player_north_check()
    player_south_check()
    player_east_check()
    player_west_check()
    player_down_check()
    player_up_check()
    func_check_season()
    func_check_weather()
    func_check_light()
    if dev_mode >= 1:
        print("\n///   DEV MODE " + str(dev_mode) +"!  ///\n")

        if dev_mode >= 2:
            # for player_stats in players:
            #     print("status effect: ", player_stats.status_effect)
            print("\ninv:")
            for item in inventory:
                print(item.print_name)
            for spell in spell_inventory:
                print(spell.print_name)
            for armor in armor_inventory:
                print(armor.print_name)
            for weapon in weapon_inventory:
                print(weapon.print_name)
            for helmet in helmet_inventory:
                print(helmet.print_name)
            for shield in shield_inventory:
                print(shield.print_name)
            print("")

            print("restock_ticks " + str(restock_ticks))

            if dev_mode >= 3:
                for scene_type in location:
                    print("scene temp desc. string: ", scene_type.temp)
                    print("scene light desc. string: ", scene_type.light)
                    print("scene_biome: ", scene_type.biome)
                    print("scene_encounter_difficulty: ", scene_type.difficulty)
                    print("can_fish: ", scene_type.can_fish)
                    print("scene_treasure: ", scene_type.treasure)
                print("in_fight: ", in_fight)
                print("x: ", steps_x)
                print("y: ", steps_y)
                print("z: ", steps_z)
                print("last x: ", prev_x)
                print("last y: ", prev_y)
                print("last z: ", prev_z)
                print("time", time)
                print("season", season)
                print("rain status", raining)
                print("date: ", days, months, years)

                if dev_mode >= 4:
                    for scene_type in all_scene_types:
                        print(scene_type.name, scene_type.xpos, scene_type.ypos, scene_type.zpos)

    for scene_type in location:
        scene_npc_count = 0
        scene_animal_count = 0

        print("you are in " + scene_type.name + "\n")
        sleep(sleep_time_fast)
        print("it is " + scene_type.temp + "" + scene_type.light + ".\n")
        sleep(sleep_time_fast)
        print("\"" + scene_type.flavour + "\" \n")
        sleep(sleep_time_fast)

        if scene_type.indoors == True:
            if scene_type.can_fish == True:
                print("looks like I can somehow fish in here ...")
            if scene_type.can_craft == True:
                print("there is a worksbench in here ...")
            if scene_type.can_cook == True:
                print("there is a cooking range here, it is nice and hot...")
            if scene_type.can_steal == True:
                print("I could steal from here...")
            if len(scene_type.npc_list) >= 1:
                if len(scene_type.npc_list) == 1:
                    print("\nthere is someone in here. \n")
            if len(scene_type.npc_list) > 1:
                print("\nthere are " + str(len(scene_type.npc_list)) + " people in here. \n")
        else:
            if scene_type.can_fish == True:
                print("looks like I can fish off here ...")
            if scene_type.can_craft == True:
                print("there is a workbench out here ...")
            if scene_type.can_cook == True:
                print("there is a fire here, it is nice and hot...")
            if scene_type.can_steal == True:
                print("I could steal from here...")

        if len(scene_type.npc_list) >= 1:
            for npc in scene_type.npc_list:
                if npc.is_animal == True:
                    scene_animal_count += 1
                if npc.is_animal == False:
                    scene_npc_count += 1

        if scene_npc_count == 1:
            print("\nthere is someone here. \n")
            sleep(sleep_time_fast)
        if scene_npc_count > 1:
            print("\nthere are " + str(scene_npc_count) + " people here. \n")
            sleep(sleep_time_fast)
        if scene_animal_count == 1:
            print("\nthere is a creature here. \n")
            sleep(sleep_time_fast)
        if scene_animal_count > 1:
            print("\nthere are " + str(scene_animal_count) + " creatures here. \n")
            sleep(sleep_time_fast)

        scene_npc_count = 0
        scene_animal_count = 0

        if scene_type.treasure == True:
            print("\nthere is treasure here. \n")
            sleep(sleep_time_fast)
        if  len(scene_type.scene_inventory) != 0 or len(scene_type.scene_weapon_inventory) != 0 or len(scene_type.scene_armor_inventory) != 0 or len(scene_type.scene_helmet_inventory) != 0 or len(scene_type.scene_shield_inventory) != 0:
            print("on the ground is:")
            sleep(sleep_time_fast)
        else:
            print("there is nothing on the ground.")
            sleep(sleep_time_fast)

        for ground_item in scene_type.scene_inventory:
            print(ground_item.print_name)
            sleep(sleep_time_fast)
        for ground_weapon in scene_type.scene_weapon_inventory:
            print(ground_weapon.print_name)
            sleep(sleep_time_fast)
        for ground_armor in scene_type.scene_armor_inventory:
            print(ground_armor.print_name)
            sleep(sleep_time_fast)
        for ground_helmet in scene_type.scene_helmet_inventory:
            print(ground_helmet.print_name)
            sleep(sleep_time_fast)
        for ground_shield in scene_type.scene_shield_inventory:
            print(ground_shield.print_name)
            sleep(sleep_time_fast)


        if scene_type.safe == False:
            print("\nit is dangerous here... \n")

    func_rain()

    for scene_type in location_north:
        print("\nto your north is " + scene_type.name + "")
        sleep(sleep_time_fast)
    for scene_type in location_south:
        print("to your south is " + scene_type.name + "")
        sleep(sleep_time_fast)
    for scene_type in location_east:
        print("to your east is " + scene_type.name + "")
        sleep(sleep_time_fast)
    for scene_type in location_west:
        print("to your west is " + scene_type.name + "")
        sleep(sleep_time_fast)
    for scene_type in location_down:
        print("below you is " + scene_type.name + "")
        sleep(sleep_time_fast)
    for scene_type in location_up:
        print("above you is " + scene_type.name + "")
        sleep(sleep_time_fast)

def func_HUD():
    status_list = []
    for status_condition in player1.status_effect_list:
        status_list.append(status_condition.name)

    print("\nHP:" + Fore.RED + str(player1.hp) + Style.RESET_ALL + "/" + Fore.RED + str(player1.maxhp) + Style.RESET_ALL)
    print("MP:" + Fore.BLUE + Style.BRIGHT + str(player1.mp) + Style.RESET_ALL + "/" + Fore.BLUE + Style.BRIGHT  + str(player1.maxmp) + Style.RESET_ALL)
    if len(player1.status_effect_list) != 0:
        print("Status: " + str(status_list) + " \n")
    else:
        print("Status: ['N0NE'] ")

##########--pre game stat calcutions--#########

game_start = 1

for player_stats in players:
    player_stats.level = 1
    player_stats.xp = 10
    player_stats.strength = 1
    player_stats.attack = 1
    player_stats.magic = 1
    player_stats.strength_xp = 10
    player_stats.attack_xp = 10
    player_stats.magic_xp = 10

func_check_stat_bonus()
func_check_level()
player_keys_check()

player1.hp = player1.maxhp # has to be last as max hp is calculated from all other stats
player1.mp = player1.maxmp

########## GAME START #########
print(Fore.RED + "Welcome to Bill & Phoebe's Adventure! \n")

print("version: " + version + " \n")

# name = input("Please enter your name: \n")
# for player_stats in players:
#     player_stats.name = name

while game_start == 1:

    func_shop_restock()

    player_keys_check()
    func_check_stat_bonus()
    func_check_level()
    player_position_check()

    if in_fight == False:
        location_desc()
        func_HUD()

    for scene_type in location:

        if check_for_combat == True:
            if scene_type.safe == False:
                if in_fight == False:
                    if time >= 12:
                        combat_chance = random.randint(0,100)
                    if time < 12:
                        combat_chance = random.randint(0,200)
                    if combat_chance > 50:
                        in_fight = False
                    if combat_chance <= 50:
                        in_fight = True
            if in_fight == True: #init combat
                if npc_fight == False:
                    func_choose_enemy()
                npc_fight = False
                for enemy_stats in current_enemies:
                    enemy_stats.hp = (0 + enemy_stats.maxhp)
                    enemy_stats.gp = random.randint(0,10) * enemy_stats.maxhp
                player_turns = 10
                print("//////////// YOU ARE NOW IN COMBAT //////////// \n")
                while in_fight == True:
                    func_check_level()

                    for enemy_stats in current_enemies:
                        print("\nEnemy stats:")
                        print("Name: " + enemy_stats.name)
                        print("Level: ", enemy_stats.level)
                        print("hp:", enemy_stats.hp, "/", enemy_stats.maxhp)

                    for player1 in players:
                        print("\nMy stats")
                        print("hp:", player1.hp, "/", player1.maxhp)

                    print("turns left: " + str(player_turns))

                    combat_input = input("combat input: \n")

                    if combat_input == "run" or combat_input == "r":
                        in_fight = False
                        print("you ran away! \n")
                        del current_enemies[:]
                        location_desc()
                    elif combat_input == "hit" or combat_input == "h":
                        player_turns -= 1
                        func_enemy_status_check()
                        func_player_status_check_melee()
                        func_check_enemy_dead()
                    elif combat_input == "spell" or combat_input == "s":
                        print("\nYour equipped spells: \n")
                        for spell in equiped_spells:
                            print(str((equiped_spells.index(spell) + 1)) + " || " + spell.print_name + " || " + spell.print_attribute)
                        print("")
                        spell_input = input("which spell will you cast? \n")
                        has_spell = 0
                        if spell_input.isdigit():
                            input_val = int(spell_input)
                            val = (input_val - 1)
                            if dev_mode >= 1:
                                print("spell input was an int")
                                print(val)
                            if len(equiped_spells) >= val:
                                has_spell = 1
                                func_enemy_status_check()
                                func_player_status_check_spell()
                                func_check_enemy_dead()

                        else:
                            if dev_mode >= 1:
                                print("spell input was a string ")
                                print(spell_input)
                            for spell in equiped_spells:
                                if spell.name == spell_input:
                                    has_spell = 1
                                    player_turns -= 1
                                    func_enemy_status_check()
                                    func_player_status_check_spell()
                                    func_check_enemy_dead()
                                    break

                        if has_spell == 0:
                            print("Invalid spell!")

                        func_check_enemy_dead()

                    elif combat_input == "quit":
                        in_fight = False
                        del current_enemies[:]
                        game_start = 0

                    else:
                        print("invalid combat command \n")

    func_check_stat_bonus()
    func_check_level()

    print("")
    input_message = ("________________|| input: ||________________\n \n")
    player_input = input(input_message)

    if player_input == "" or player_input == " " or player_input == "  ":
        pass
    else:
        print("")

    if player_input == "search" or input == "j":
        for scene_type in location:
            if scene_type.treasure == True:
                func_search_treasure()
                scene_type.treasure = False
            else:
                print("there is nothing here...\n")

    elif player_input == "help":
        print("commands: \n north (w) \n south (s) \n east (d) \n west (a) \n down (f) \n up (r) \n search (j) \n equip (e) \n stats (q) \n drop (l) \n pickup \n consume (k) \n inv (i) \n spellbook (b) \n cast (c) \n wait (*blank*) \n camp (u) \n quit \n")

    elif player_input == "north" or player_input == "w":
        has_moved = True
        for scene_type in location_north:
            if scene_type.passable == True:
                steps_y += 1
                prev_y = steps_y
                prev_y -= 1
            else:
                print(scene_type.impass_msg + ", you have not moved.")

    elif player_input == "south" or player_input == "s":
        has_moved = True
        for scene_type in location_south:
            if scene_type.passable == True:
                steps_y -= 1
                prev_y = steps_y
                prev_y += 1
            else:
                print(scene_type.impass_msg + ", you have not moved")

    elif player_input == "east" or player_input == "d":
        for scene_type in location_east:
            if scene_type.passable == True:
                steps_x += 1
                prev_x = steps_x
                prev_x -= 1
            else:
                print(scene_type.impass_msg + ", you have not moved")

    elif player_input == "west" or player_input == "a":
        has_moved = True
        for scene_type in location_west:
            if scene_type.passable == True:
                steps_x -= 1
                prev_x = steps_x
                prev_x += 1
            else:
                print(scene_type.impass_msg + ", you have not moved")

    elif player_input == "down" or player_input == "f":
        has_rope = False
        has_stairs = False
        can_climb = False
        for item in inventory:
            if item.name == "rope":
                has_rope = True
                can_climb = True
        for scene_type in location:
            if scene_type.has_stairs == True:
                can_climb = True
                has_stairs = True
        if can_climb == True:
            for scene_type in location_down:
                if scene_type.passable == True:
                    steps_z -= 1
                    prev_z = steps_z
                    prev_z += 1
                else:
                    print(scene_type.impass_msg + ", you have not moved")
        if has_rope == False:
            print("you need a rope to climb down.")

    elif player_input == "up" or player_input == "r":
        has_rope = False
        has_stairs = False
        can_climb = False
        for item in inventory:
            if item.name == "rope":
                has_rope = True
                can_climb = True
        for scene_type in location:
            if scene_type.has_stairs == True:
                can_climb = True
                has_stairs = True
        if can_climb == True:
            for scene_type in location_up:
                if scene_type.passable == True:
                    steps_z += 1
                    prev_z = steps_z
                    prev_z -= 1
                else:
                    print(scene_type.impass_msg + ", you have not moved.")
        if has_rope == False and has_stairs == False:
            print("you need a rope to climb up.")

####################################################

    elif player_input == "equip" or player_input == "e":
        if len(equiped_weapon) != 0:
            for weapon in equiped_weapon:
                current_weapon = weapon.name
        else:
            current_weapon = "0"

        if len(equiped_armor) != 0:
            for armor in equiped_armor:
                current_armor = armor.name
        else:
            current_armor = "0"

        if len(equiped_helmet) != 0:
            for helmet in equiped_helmet:
                current_helmet = helmet.name
        else:
            current_helmet = "0"

        if len(equiped_shield) != 0:
            for shield in equiped_shield:
                current_shield = shield.name
        else:
            current_shield = "0"

        current_spell = "0"

        print("your gear:\n")

        print("|| 1 || Weapon")
        print("|| 2 || Armor")
        print("|| 3 || Helmet")
        print("|| 4 || Shield")
        print("|| 5 || Spell")
        equip_gear = input("\nwhat will you equip?\n")

        if equip_gear == "1":
            if len(weapon_inventory) != 0:
                func_equip(weapon,weapon_inventory,current_weapon)
            else:
                print("you have no weapons...")
        elif equip_gear == "2":
            if len(armor_inventory) != 0:
                func_equip(armor,armor_inventory,current_armor)
            else:
                print("you have no armor...")
        elif equip_gear == "3":
            if len(helmet_inventory) != 0:
                func_equip(helmet,helmet_inventory,current_helmet)
            else:
                print("you have no helmets...")
        elif equip_gear == "4":
            if len(shield_inventory) != 0:
                func_equip(shield,shield_inventory,current_shield)
            else:
                print("you have no shields...")
        elif equip_gear == "5":
            if len(spell_inventory) != 0:
                func_equip(spell,spell_inventory,current_spell)
            else:
                print("you have no spell scrolls...")
        else:
            print("\ninvalid choice!\n")

        func_check_stat_bonus()

    elif player_input == "stats" or player_input == "q":
        for player1 in players:
            print("|| Stats: \n")
            print("|| name: " + player1.name)
            print("|| level: " + str(player1.level))
            print("|| xp: " + str(player1.xp))
            print("|| gold: " + str(player1.gp))
            print("|| hp: " + str(player1.hp) + " / " + str(player1.nobonus_maxhp) + " || + " + str(player1.maxhp_bonus))
            print("|| mp: " + str(player1.mp) + " / " + str(player1.nobonus_maxmp) + " || + " + str(player1.maxmp_bonus))

            print("|| magic: " + str(player1.magic) + " || + " + str(player1.magic_bonus) + " || xp: " + str(player1.magic_xp))
            print("|| strength: " + str(player1.strength) + " || + " + str(player1.strength_bonus) + " || xp: " + str(player1.strength_xp))
            print("|| attack: " + str(player1.attack) + " || + " + str(player1.attack_bonus) + " || xp: " + str(player1.attack_xp))
            print("|| defence: " + str(player1.defence) + " || + " + str(player1.defence_bonus) + " || xp: " + str(player1.defence_xp))

    elif player_input == "skills" or player_input == "Q":
        for player1_skills in players_skills:
            print("|| Skills: \n")
            print("|| fishing: " + str(player1_skills.fishing) + " || xp: " + str(player1_skills.fishing_xp))
            print("|| theiving: " + str(player1_skills.thieving) + " || xp: " + str(player1_skills.thieving_xp))
            print("|| crafting: " + str(player1_skills.crafting) + " || xp: " + str(player1_skills.crafting_xp))
            print("|| cooking: " + str(player1_skills.cooking) + " || xp: " + str(player1_skills.cooking_xp))

    elif player_input == "gear" or player_input == "g":
        for player1 in players:

            print("gear: \n")

            if len(equiped_helmet) != 0:
                for helmet in equiped_helmet:
                    print("|| Helmet: \n")
                    print("|| level: ", helmet.level)
                    print("|| name: " + helmet.print_name + " || attribute: " + helmet.print_attribute + " || type: " + helmet.type)
                    print("|| magic: " + str(helmet.magic_bonus) + " || strength: " + str(helmet.strength_bonus) + " || attack: " + str(helmet.attack_bonus))
                    print("|| hp bonus: " + str(helmet.maxhp_bonus) + " || defence: " + str(helmet.defence_bonus))


                print("")
            else:
                print("you have no helmet... \n")

            if len(equiped_armor) != 0:
                for armor in equiped_armor:
                    print("|| Armor: \n")
                    print("|| level: ", armor.level)
                    print("|| name: " + armor.print_name + " || attribute: " + armor.print_attribute + " || type: " + armor.type)
                    print("|| magic: " + str(armor.magic_bonus) + " || strength: " + str(armor.strength_bonus) + " || attack: " + str(armor.attack_bonus))
                    print("|| hp bonus: " + str(armor.maxhp_bonus) + " || defence: " + str(armor.defence_bonus))

                print("")
            else:
                print("you have no armor... \n")

            if len(equiped_shield) != 0:
                for shield in equiped_shield:
                    print("|| Shield: \n")
                    print("|| level: ", shield.level)
                    print("|| name: " + shield.print_name + " || attribute: " + shield.print_attribute + " || type: " + shield.type)
                    print("|| magic: " + str(shield.magic_bonus) + " || strength: " + str(shield.strength_bonus) + " || attack: " + str(shield.attack_bonus))
                    print("|| hp bonus: " + str(shield.maxhp_bonus) + " || defence: " + str(shield.defence_bonus))

                print("")
            else:
                print("you have no shield... \n")

            if len(equiped_weapon) != 0:
                for weapon in equiped_weapon:
                    print("|| Weapon: \n")
                    print("|| level: ", weapon.level)
                    print("|| name: " + weapon.print_name + " || attribute: " + weapon.print_attribute + " || type: " + weapon.type)
                    print("|| magic: " + str(weapon.magic_bonus) + " || strength: " + str(weapon.strength_bonus) + " || attack: " + str(weapon.attack_bonus))
                    print("|| hp bonus: " + str(weapon.maxhp_bonus) + " || defence: " + str(weapon.defence_bonus))
                print("")
            else:
                print("you have no weapon... \n")

    elif player_input == "drop" or player_input == "l":
        print("")
        print("|| 1 || Items")
        print("|| 2 || Weapons")
        print("|| 3 || Armor")
        print("|| 4 || Helmets")
        print("|| 5 || Shields")
        print("|| 6 || Spells")

        drop_gear = input("\nwhich bag to drop from?\n")
        if drop_gear == "1":
            if len(inventory) != 0:
                func_drop(item,inventory)
            else:
                print("you have no weapons...")
        elif drop_gear == "2":
            if len(weapon_inventory) != 0:
                func_drop(weapon,weapon_inventory)
            else:
                print("you have no weapons...")
        elif drop_gear == "3":
            if len(armor_inventory) != 0:
                func_drop(armor,armor_inventory)
            else:
                print("you have no armor...")
        elif drop_gear == "4":
            if len(helmet_inventory) != 0:
                func_drop(helmet,helmet_inventory)
            else:
                print("you have no helmets...")
        elif drop_gear == "5":
            if len(shield_inventory) != 0:
                func_drop(shield,shield_inventory)
            else:
                print("you have no shields...")
        elif drop_gear == "6":
            if len(spell_inventory) != 0:
                func_edrop(spell,spell_inventory)
            else:
                print("you have no spell scrolls...")
        else:
            print("\ninvalid choice!\n")

    elif player_input == "pickup" or player_input == "p":
        pickedup_item = input("Which item do you want to pickup? \n")
        has_item = False
        if has_item == False:
            for scene_type in location:
                for ground_item in scene_type.scene_inventory:
                    if ground_item.name == pickedup_item:
                        has_item = True
                        print("you pickup " + ground_item.print_name + "\n")
                        sleep(sleep_time_fast)
                        scene_type.scene_inventory.remove(ground_item)
                        for item in all_game_items:
                            if item.name == pickedup_item:
                                inventory.append(item)
                                break
                        break

                for ground_weapon in scene_type.scene_weapon_inventory:
                    if ground_weapon.name == pickedup_item:
                        has_item = True
                        print("you pickup " + ground_weapon.print_name + "\n")
                        sleep(sleep_time_fast)
                        scene_type.scene_weapon_inventory.remove(ground_weapon)
                        for weapon in all_game_weapons:
                            if weapon.name == pickedup_item:
                                weapon_inventory.append(weapon)
                                break
                        break

                for ground_armor in scene_type.scene_armor_inventory:
                    if ground_armor.name == pickedup_item:
                        has_item = True
                        print("you pickup " + ground_armor.print_name + "\n")
                        sleep(sleep_time_fast)
                        scene_type.scene_armor_inventory.remove(ground_armor)
                        for armor in all_game_armor:
                            if armor.name == pickedup_item:
                                armor_inventory.append(armor)
                                break
                        break

                for ground_helmet in scene_type.scene_helmet_inventory:
                    if ground_helmet.name == pickedup_item:
                        has_item = True
                        print("you pickup " + ground_helmet.print_name + "\n")
                        sleep(sleep_time_fast)
                        scene_type.scene_helmet_inventory.remove(ground_helmet)
                        for helmet in all_game_helmets:
                            if helmet.name == pickedup_item:
                                helmet_inventory.append(helmet)
                                break
                        break

                for ground_shield in scene_type.scene_shield_inventory:
                    if ground_shield.name == pickedup_item:
                        has_item = True
                        print("you pickup " + ground_shield.print_name + "\n")
                        sleep(sleep_time_fast)
                        scene_type.scene_shield_inventory.remove(ground_shield)
                        for shield in all_game_shields:
                            if shield.name == pickedup_item:
                                shield_inventory.append(shield)
                                break
                        break

                if has_item == False:
                    print("that is not on the ground.\n")
                    sleep(sleep_time_fast)
                    break

    elif player_input == "pickupall" or player_input == "P":
        while len(scene_type.scene_inventory) != 0 or len(scene_type.scene_weapon_inventory) != 0 or len(scene_type.scene_armor_inventory) != 0 or len(scene_type.scene_helmet_inventory) != 0 or len(scene_type.scene_shield_inventory) != 0:
            has_item = False
            while has_item == False:
                for scene_type in location:
                    for ground_item in scene_type.scene_inventory:
                        pickedup_item = "0"
                        pickedup_item = ground_item.name
                        has_item = True
                        print("you pickup " + ground_item.print_name + "\n")
                        sleep(sleep_time_fast)
                        scene_type.scene_inventory.remove(ground_item)
                        for item in all_game_items:
                            if item.name == pickedup_item:
                                inventory.append(item)
                                break
                        break

                    for ground_weapon in scene_type.scene_weapon_inventory:
                        pickedup_item = "0"
                        pickedup_item = ground_weapon.name
                        has_item = True
                        print("you pickup " + ground_weapon.print_name + "\n")
                        sleep(sleep_time_fast)
                        scene_type.scene_weapon_inventory.remove(ground_weapon)
                        for weapon in all_game_weapons:
                            if weapon.name == pickedup_item:
                                weapon_inventory.append(weapon)
                                break
                        break

                    for ground_armor in scene_type.scene_armor_inventory:
                        pickedup_item = "0"
                        pickedup_item = ground_armor.name
                        has_item = True
                        print("you pickup " + ground_armor.print_name + "\n")
                        sleep(sleep_time_fast)
                        scene_type.scene_armor_inventory.remove(ground_armor)
                        for armor in all_game_armor:
                            if armor.name == pickedup_item:
                                armor_inventory.append(armor)
                                break
                        break

                    for ground_helmet in scene_type.scene_helmet_inventory:
                        pickedup_item = "0"
                        pickedup_item = ground_helmet.name
                        has_item = True
                        print("you pickup " + ground_helmet.print_name + "\n")
                        sleep(sleep_time_fast)
                        scene_type.scene_helmet_inventory.remove(ground_helmet)
                        for helmet in all_game_helmets:
                            if helmet.name == pickedup_item:
                                helmet_inventory.append(helmet)
                                break
                        break

                    for ground_shield in scene_type.scene_shield_inventory:
                        pickedup_item = "0"
                        pickedup_item = ground_shield.name
                        has_item = True
                        print("you pickup " + ground_shield.print_name + "\n")
                        sleep(sleep_time_fast)
                        scene_type.scene_shield_inventory.remove(ground_shield)
                        for shield in all_game_shields:
                            if shield.name == pickedup_item:
                                shield_inventory.append(shield)
                                break
                        break

                    if has_item == False:
                        print("\npicked up all items.\n")
                        sleep(sleep_time_fast)
                        break

    elif player_input == "consume" or player_input == "k":
        eaten_item = input("Which item do you want to consume? \n")
        has_item = False
        for item in inventory:
            if eaten_item == item.name:
                has_item = True
                if item.edible == True:
                    if item.poisonous == False:
                        print("you consume " + item.print_name)
                        sleep(sleep_time_fast)
                        player1.hp = player1.hp + item.hp
                        if player1.hp > player1.maxhp:
                            player1.hp = player1.maxhp
                    else:
                        print("you consume " + item.print_name)
                        sleep(sleep_time_fast)
                        player1.hp = player1.hp - item.hp
                        print("you feel sick...")
                        sleep(sleep_time_fast)
                        if player1.hp <= 0:
                            print("\nYOU ARE DEAD \n")
                            game_start = 0
                    inventory.remove(item)
                    break
                else:
                    print("you can't consume " + item.print_name)
                    sleep(sleep_time_fast)
                    break

        if has_item == False:
            print("you don't have " + eaten_item)
            sleep(sleep_time_fast)

##################################################

    elif player_input == "inv" or player_input == "i":

            print("\nInventory: \n")

            if len(inventory) != 0:
                for item in inventory:

                    print("|| " + item.print_name)

            if len(spell_inventory) != 0:
                for spell in spell_inventory:

                    print("|| " + spell.print_name + " || " + spell.print_attribute + " || lvl: " + str(spell.level))

            if len(helmet_inventory) != 0:
                for helmet in helmet_inventory:

                    print("|| " + helmet.print_name + " || attribute: " + helmet.print_attribute + " || type: " + helmet.type + " || lvl: " + str(helmet.level))

            if len(armor_inventory) != 0:
                for armor in armor_inventory:

                    print("|| " + armor.print_name + " || attribute: " + armor.print_attribute + " || type: " + armor.type + " || lvl: " + str(armor.level))

            if len(shield_inventory) != 0:
                for shield in shield_inventory:

                    print("|| " + shield.print_name + " || attribute: " + shield.print_attribute + " || type: " + shield.type + " || lvl: " + str(shield.level))

            if len(weapon_inventory) != 0:
                for weapon in weapon_inventory:

                    print("|| " + weapon.print_name + " || attribute: " + weapon.print_attribute + " || type: " + weapon.type + " || lvl: " + str(weapon.level))

            print("")

    elif player_input == "wait"  or player_input == "":
        for scene_type in location:
            print("you wait in " + scene_type.name + " ...\n")

    elif player_input == "camp"  or player_input == "u":
        can_camp = False
        for item in inventory:
            if item.name == "tent":
                can_camp = True
                print("You camp untill the next morning, your hp has been restored.")
                time += 24
                for player_stats in players:
                    player_stats.hp = player_stats.maxhp
            else:
                can_camp = False

    elif player_input == "cast"  or player_input == "c":
        print("\nYour equipped healing spells: \n")
        for spell in equiped_spells:
            if spell.effect == 1:
                print(spell.print_name)
        print("")
        spell_input = input("which spell will you cast? \n")
        has_spell = 0
        for spell in equiped_spells:
            if spell.name == spell_input:
                has_spell = 1
                if spell.effect == 1:
                    func_player_spell_non_combat()
                    break
                else:
                    print("you have no use for that spell right now")
        if has_spell == 0:
            print("Invalid spell!")

    elif player_input == "spellbook"  or player_input == "b":
        print("\nequiped spells:")
        for spell in equiped_spells:
            print("|| " + spell.print_name + " || " + spell.print_attribute + " || " + spell.spell_desc)
        print("")
        print("spell scrolls:")
        for spell in spell_inventory:
            print("|| " + spell.print_name + " || " + spell.print_attribute + " || " + spell.spell_desc)
        print("")

#################----DIALOGUE----################

    elif player_input == "talk"  or player_input == "t":
        for scene_type in location:
            if len(scene_type.npc_list) >= 1:
                target_npc = func_get_target_npc()
                for npc in scene_type.npc_list:
                    if npc.first_name == target_npc:

                        if npc.is_animal == True:
                            print("in front of you is a " + npc.gender + " " + npc.race + "\n")

                        else:
                            print("in front of you is a " + npc.race + " " + npc.gender + " in " + npc.attire + "\n")

                            if npc.faction != "0":
                                print(npc.greeting + ", I am " + npc.first_name + " " + npc.last_name + ", the " + npc.title + " of the " + npc.faction + "\n")
                            else:
                                print(npc.greeting + ", I am " + npc.first_name + " " + npc.last_name + ", the " + npc.title + "\n")

                        print(npc.npc_desc)

                        target_dialouge = func_get_target_dialouge()
                        for dialouge_option in npc.dialouge_options_list:
                            if dialouge_option.text == target_dialouge:

                                if dialouge_option.is_buy_weapon == True:
                                    func_shop(weapon,npc.npc_weapon_inventory)
                                if dialouge_option.is_buy_armor == True:
                                    func_shop(armor,npc.npc_armor_inventory)
                                if dialouge_option.is_buy_helmet == True:
                                    func_shop(helmet,npc.npc_helmet_inventory)
                                if dialouge_option.is_buy_shield == True:
                                    func_shop(armor,npc.npc_shield_inventory)

                                if dialouge_option.is_buy_item == True:
                                    func_shop(item,npc.npc_inventory)
                                if dialouge_option.is_buy_spell == True:
                                    func_shop(spell,npc.npc_spell_inventory)

                                if dialouge_option.is_talk == True:
                                    print("you have a conversation")

                                if dialouge_option.is_sell == True:
                                    print("")
                                    print("|| 1 || Items")
                                    print("|| 2 || Weapons")
                                    print("|| 3 || Armor")
                                    print("|| 4 || Helmets")
                                    print("|| 5 || Shields")
                                    print("|| 6 || Spells")
                                    sell_gear = input("\nwhich bag to sell from?\n")
                                    if sell_gear == "1":
                                        func_sell(item,inventory)
                                    if sell_gear == "2":
                                        func_sell(weapon,weapon_inventory)
                                    if sell_gear == "3":
                                        func_sell(armor,armor_inventory)
                                    if sell_gear == "4":
                                        func_sell(helmet,helmet_inventory)
                                    if sell_gear == "5":
                                        func_sell(shield,shield_inventory)
                                    if sell_gear == "6":
                                        func_sell(spell,spell_inventory)

                                if dialouge_option.is_assault == True:
                                    print(npc.assault_dialouge)
                                    current_enemies.extend(npc.combat_enemy_list)
                                    npc_enemy_fname = npc.first_name
                                    npc_enemy_lname = npc.last_name
                                    in_fight = True
                                    npc_fight = True

                                if dialouge_option.is_give == True:
                                    print("execute func_give_item")

                                if dialouge_option.is_quest == True:
                                    print("execute func_quest")

            else:
                print("there is nobody to talk to\n")

            if len(scene_type.npc_list) == 9999: #this condition will never be met, it just hides a bunch of code i want to keep
                for scene_type in location:
                    if scene_type == birds_nest:

                        if (not equiped_weapon):
                            print("\nHello you look as though you could do with some supplies skwark!")
                            print("Here you go!\n")
                            inventory.append(worms)
                            equiped_weapon.append(bird_sword)
                            print("The bird hands you some worms and a sword\n")
                            response = input("bird expects a response...\n")
                            if response == "skwark!":
                                print("\n I like you skwark!\n")
                            else:
                                inventory.remove(worms)
                                print("*the bird snatches your worms and scowls*\n")
                        else:
                            print("hello welcome to the bird armory skwark!\n")
                            response2 = input("would you like to purchase any armor skwark!?\n")
                            if response2 == "yes":
                                print("bird shop armory:\n")
                                print("gold: ", player1.gp)
                                for armor in bird_store_armor:
                                    print(armor.name + " ----- ", armor.value, " gp. ")
                                bought_item = input("\nplease choose some armor to buy skwark!\n")
                                has_item = False
                                for armor in bird_store_armor:
                                    if bought_item == armor.name:
                                        has_item = True
                                        if player1.gp >= armor.value:
                                            player1.gp -= armor.value
                                            armor_inventory.append(armor)
                                            print("\nthanks, enjoy your " + armor.name + " skwark!\n")
                                        else:
                                            print("You can't afford that skwark!")
                                    if has_item == False:
                                        print("\nI don't have " + bought_item + " skwark!\n")

                            else:
                                print("okay seeya! skwark!\n")

                for scene_type in location:
                    if scene_type == large_tree:

                            for item in inventory:
                                if item.name == "worms":
                                    has_worms = True

                            if has_worms == True:
                                print ("could I please have your worms, I will give you 100 gold!")


                            else:
                                print("hello welcome to the bird shop for birds skwark!\n")
                                response = input("would you like to purchase any items?\n")
                                if response == "yes":
                                    print("bird shop inventory:\n")
                                    print("gold: ", player1.gp)
                                    for item in bird_store_inventory:
                                        print(item.name + " ----- ", item.value, " gp. ")
                                    bought_item = input("please choose an item to buy skwark!\n")
                                    has_item = False
                                    for item in bird_store_inventory:
                                        if bought_item == item.name:
                                            has_item = True
                                            if player1.gp >= item.value:
                                                player1.gp -= item.value
                                                inventory.append(item)
                                                print("\nthanks, enjoy your " + item.name + " skwark!\n")
                                            else:
                                                print("You can't afford that skwark!")
                                    if has_item == False:
                                        print("I don't have " + bought_item + " skwark!\n")

                                    else:

                                        print("pardon!? skwark!\n")
                                else:

                                    print("okay seeya! skwark!\n")

                for scene_type in location:
                    if scene_type == hills:
                            print("\nhello I am an old man, I have travelled very far")
                            response = input("I found this pendant *cough*, would you like it?\n")
                            if response == "yes":
                                if pendant in old_man_inventory:
                                    inventory.append(pendant)
                                    old_man_inventory.remove(pendant)
                                    print("here you are. \n")
                                else:
                                    print("it's gone! erhm... *cough* damn theives!\n")
                            else:
                                print("erm... herm.. what?\n")

                for scene_type in location:
                    if scene_type == forest_cabin:
                            print("\nwhat are you doing in my cabin?")
                            response = input("do you wish to learn the magic I have created?\n")
                            if response == "yes":
                                for player_stats in players:
                                    if player_stats.magic >= 10:
                                        equiped_spells.append(hydro_barrage)
                                        equiped_spells.append(fireball)
                                        print("you feel more powerful.. \n")
                                    else:
                                        print("you are too weak to learn this. Come back when you're stronger!\n")
                            if response == "no":
                                print("\nThen what are you doing in my cabin?")

                            if response != "yes" and response != "no":
                                print("what?")

                for scene_type in location:
                    if scene_type == dismurth_gates:
                            print("\nwe are the town guard")
                            response = input("Before you can pass, you must answer this question, What is the meaning of life?\n")
                            if response == "fat doinks":
                                print("\nYou may enter, for you understand true path of righteousness \n")
                            else:
                                print("\njust kidding haha \n")

                for scene_type in location:
                    if scene_type == dismurth_square:
                            print("\nhello")
                            response = input("my name is Sir Kobious, I am from the glorious legion, do you support the legion!?\n")
                            if response == "yes":
                                if legion_seal in sir_kobious_inventory:
                                    inventory.append(legion_seal)
                                    sir_kobious_inventory.remove(legion_seal)
                                    print("\nGLORY TO THE LEGION! \n")
                                else:
                                    print("\nGLORY TO THE LEGION! \n")
                            else:
                                print("Blasphemy I say!\n")

                for scene_type in location:
                    if scene_type == dismurth_smith:
                            print("\n*the blacksmith is working hard*")
                            response = input("I am the blacksmith, would you like to purchase anything?\n")
                            if response == "yes":
                                print("gold: ", player1.gp)
                                print("blacksmith inventory:\n")
                                for armor in blacksmith_inventory:
                                    print(armor.name + " ----- ", armor.value, " gp. ")
                                bought_item = input("please, choose an item to buy\n")
                                has_item = False
                                for armor in blacksmith_inventory:
                                    if bought_item == armor.name:
                                        has_item = True
                                        if player1.gp >= armor.value:
                                            player1.gp -= armor.value
                                            armor_inventory.append(armor)
                                            print("\nthanks, enjoy your " + armor.name + "\n")
                                        else:
                                            print("You can't afford that!")

                                if has_item == False:
                                    print("I don't have " + bought_item + " i'm sorry.\n")
                            else:
                                print("Goodbye.\n")

                for scene_type in location:
                    if scene_type == dismurth_barracks:
                            print("\n *There are two soliders aruging, one wearing an eagle helmet, \nanother wearing a red and yellow insignia of a mallet and a small curved cutting tool.*")
                            print("WHAT DID YOU SAY!?")
                            print("*one soldier grabs the other*")
                            print("*a third solider appears*")
                            print("Gentlemen, you cannot fight here, this is the war room!")

                for scene_type in location:
                    if scene_type == dismurth_farm:
                            print("\n*the farmer and his wife look visibly upset*")
                            response = input("Those damn bandits keep raiding our stores, you look like you can handle a fight, would you help us?\n")
                            if response == "yes":
                                print("\nthank you, their fortress is south of here, you might find them there, be careful! \n")

                            else:
                                print("Goodbye.\n")

                for scene_type in location:
                    if scene_type == dismurth_tower:
                            print("\nthe wizard appears to be in deep thought...")
                            response = input("I am the town mage, would you like to learn any spells?\n")
                            if response == "yes":
                                print("gold: ", player1.gp)
                                print("wizard's spellbook:\n")
                                for spell in wizard_inventory:
                                    print(spell.print_name + " || " + spell.print_attribute + " || " + str(spell.damage) + " gp. ")
                                bought_item = input("please, choose a spell to learn\n")
                                has_item = False
                                for spell in wizard_inventory:
                                    if bought_item == spell.name:
                                        has_item = True
                                        if player1.gp >= spell.damage:
                                            player1.gp -= spell.damage
                                            spell_inventory.append(spell)
                                            print("\nthanks, enjoy your " + spell.print_name + "\n")
                                        else:
                                            print("You can't afford that!")

                                if has_item == False:
                                    print("I don't have " + bought_item + " i'm sorry.\n")
                            else:
                                print("Goodbye.\n")

                for scene_type in location:
                    if scene_type == south_road_a:
                            print("*there is a guard blocking the bridge*")
                            print("\n You may not cross the bridge without a certificate of passage")

#################################################

    elif player_input == "quit":
        game_start = 0

########################################


    elif player_input == "dev":
        dev_mode += 1
        if dev_mode >= 6:
            dev_mode = 0

    elif player_input == "/xp":
        if dev_mode >= 1:
            val_dev_xp = 0
            dev_xp_input = input("\nhow much xp?\n")
            if dev_xp_input.isdigit():
                val_dev_xp = int(dev_xp_input)
            player1.xp += val_dev_xp

    elif player_input == "/tp":
        if dev_mode >= 1:
            val_dev_tpx = 0
            val_dev_tpy = 0
            val_dev_tpz = 0

            dev_tpx_input = input("\nx cord:\n")
            if dev_tpx_input.isdigit():
                val_dev_tpx = int(dev_tpx_input)


            dev_tpy_input = input("\ny cord:\n")
            if dev_tpy_input.isdigit():
                val_dev_tpy = int(dev_tpy_input)

            dev_tpz_input = input("\nz cord:\n")
            if dev_tpz_input.isdigit():
                val_dev_tpz = int(dev_tpz_input)

            func_tp(val_dev_tpx,val_dev_tpy,val_dev_tpz)


    else:
        print("invalid command\n")
        sleep(sleep_time_fast)

    if dev_mode >= 1:
        sleep_time = 0
        sleep_time_fast = 0
        sleep_time_slow = 0


    time += 1
    if time >= 24:
        time = 0
        print("\nthe sun has risen...\n")
        sleep(sleep_time_fast)
        days += 1
        if days >= 30:
            days = 1
            months += 1
            if months >= 13:
                months = 1
                years += 1
                print("\nHappy new year " + player1.name + "! \nThe year is now:")
                print(years)
                sleep(sleep_time_fast)

    if time == 12:
        print("\nthe sun has gone down...\n")
        sleep(sleep_time_fast)
