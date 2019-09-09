import random
from time import sleep
from colorama import init
from colorama import Fore, Back, Style

init(autoreset=True)

all_scene_types = []

minimum_difficulty = 100

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
            self.tile_r = 0
            self.tile_g = 255
            self.tile_b = 229
        elif self.biome == "water":
            self.name = (Fore.BLUE + Style.NORMAL + name + Style.RESET_ALL)
            self.tile_r = 0
            self.tile_g = 0
            self.tile_b = 255
        elif self.biome == "forest":
            self.name = (Fore.GREEN + Style.NORMAL + name + Style.RESET_ALL)
            self.tile_r = 50
            self.tile_g = 120
            self.tile_b = 40
        elif self.biome == "town":
            self.name = (Fore.BLACK + Style.BRIGHT + name + Style.RESET_ALL)
            self.tile_r = 139
            self.tile_g = 139
            self.tile_b = 143
        elif self.biome == "sandy":
            self.name = (Fore.YELLOW + Style.NORMAL + name + Style.RESET_ALL)
            self.tile_r = 237
            self.tile_g = 206
            self.tile_b = 0
        elif self.biome == "grassy":
            self.name = (Fore.GREEN + Style.DIM + name + Style.RESET_ALL)
            self.tile_r = 90
            self.tile_g = 217
            self.tile_b = 72
        elif self.biome == "snow":
            self.name = (Fore.WHITE + Style.BRIGHT + name + Style.RESET_ALL)
            self.tile_r = 247
            self.tile_g = 247
            self.tile_b = 247
        elif self.biome == "cave":
            self.name = (Fore.MAGENTA + Style.DIM + name + Style.RESET_ALL)
            self.tile_r = 136
            self.tile_g = 10
            self.tile_b = 145
        elif self.biome == "dirt":
            self.name = (Fore.BLACK + Style.BRIGHT + name + Style.RESET_ALL)
            self.tile_r = 145
            self.tile_g = 102
            self.tile_b = 16
        elif self.biome == "road":
            self.name = (Fore.BLACK + Style.BRIGHT + name + Style.RESET_ALL)
            self.tile_r = 89
            self.tile_g = 87
            self.tile_b = 63
        else:
            self.name = (Fore.RED + Style.DIM + name + Style.RESET_ALL)
            self.tile_r = 255
            self.tile_g = 0
            self.tile_b = 0

        all_scene_types.append(self)

        self.difficulty += minimum_difficulty
# dev scenes
dev = scene_type(16,16,0,"dev skill test area","temperate","sunny",True,True,True,True,True,True,True,0,"forest",False,False,"","rolling green hills",[],[],[],[],[])

# starting area

hills = scene_type(1,5,0,"the hills","temperate","sunny",True,False,False,False,False,True,False,0,"forest",False,False,"","rolling green hills",[],[],[],[],[])
lakeside = scene_type(1,6,0,"lakeside","temperate","sunny",True,False,False,False,False,True,False,0,"forest",False,False,"","the shore of the lake",[],[],[],[],[])

# large tree cave
large_tree = scene_type(2,5,0,"a large hollow tree","temperate","shady",True,False,False,False,True,True,False,0,"forest",True,False,"","a very, very large oak tree",[],[],[],[],[])
large_tree_tunnel_a = scene_type(2,5,-1,"a tunnel","temperate","shady",True,False,False,False,False,True,False,0,"forest",True,False,"","there are tree roots supporting the tunnel",[],[],[],[],[])
large_tree_tunnel_b = scene_type(2,5,-2,"a tunnel ","temperate","shady",True,False,False,False,False,True,False,0,"forest",True,False,"","the tunnel goes down quite far",[],[],[],[],[])
large_tree_cave_a = scene_type(2,5,-3,"oak tree cave","temperate","shady",False,False,False,False,False,True,False,1,"forest",True,False,"","a cave below the large oak tree",[],[],[],[],[])
large_tree_cave_b = scene_type(1,5,-3,"oak tree cave","temperate","shady",False,False,False,False,False,True,False,1,"forest",False,False,"","a cave below the large oak tree",[],[],[],[],[])
large_tree_cave_c = scene_type(1,6,-3,"oak tree cave","temperate","shady",False,False,False,False,False,True,False,1,"forest",False,False,"","a cave below the large oak tree",[],[],[],[],[])
large_tree_cave_d = scene_type(1,7,-3,"oak tree cave","temperate","shady",False,False,False,False,False,True,False,1,"forest",False,False,"","a cave below the large oak tree",[],[],[],[],[])
large_tree_cave_e = scene_type(1,8,-3,"oak tree cave","temperate","shady",False,False,False,False,False,True,False,1,"forest",False,False,"","a cave below the large oak tree",[],[],[],[],[])
large_tree_cave_f = scene_type(1,4,-3,"oak tree cave","temperate","shady",False,False,False,False,False,True,False,1,"forest",False,False,"","a cave below the large oak tree",[],[],[],[],[])
large_tree_cave_g = scene_type(1,4,-3,"oak tree cave","temperate","shady",False,False,False,False,False,True,False,1,"forest",False,False,"","a cave below the large oak tree",[],[],[],[],[])
large_tree_cave_h = scene_type(2,6,-3,"oak tree cave","temperate","shady",False,False,False,False,False,True,False,1,"forest",False,False,"","a cave below the large oak tree",[],[],[],[],[])
large_tree_cave_i = scene_type(2,7,-3,"oak tree cave","temperate","shady",False,False,False,False,False,True,False,1,"forest",False,False,"","a cave below the large oak tree",[],[],[],[],[])
large_tree_cave_j = scene_type(3,4,-3,"oak tree cave","temperate","shady",False,False,False,False,False,True,False,1,"forest",False,False,"","a cave below the large oak tree",[],[],[],[],[])
large_tree_cave_k = scene_type(3,5,-3,"oak tree cave","temperate","shady",False,False,False,False,False,True,False,1,"forest",False,False,"","a cave below the large oak tree",[],[],[],[],[])
large_tree_cave_l = scene_type(3,6,-3,"oak tree cave","temperate","shady",False,False,False,False,False,True,False,1,"forest",False,False,"","a cave below the large oak tree",[],[],[],[],[])
large_tree_cave_m = scene_type(3,7,-3,"oak tree cave","temperate","shady",False,False,False,False,False,True,False,1,"forest",False,False,"","a cave below the large oak tree",[],[],[],[],[])
large_tree_cave_n = scene_type(4,4,-3,"oak tree cave","temperate","shady",False,False,False,False,False,True,False,1,"forest",False,False,"","a cave below the large oak tree",[],[],[],[],[])
large_tree_cave_o = scene_type(4,5,-3,"oak tree cave","temperate","shady",False,False,False,False,False,True,False,1,"forest",False,False,"","a cave below the large oak tree",[],[],[],[],[])
large_tree_cave_p = scene_type(4,6,-3,"oak tree cave","temperate","shady",False,False,False,False,False,True,False,1,"forest",False,False,"","a cave below the large oak tree",[],[],[],[],[])


large_tree_cave_door = scene_type(1,9,-3,"oak doorway","temperate","shady",True,False,False,False,False,False,False,0,"dirt",False,False,"this door is locked, you need a key..","The door is unlocked...",[],[],[],[],[])

large_tree_cave_room = scene_type(1,10,-3,"oak tree cave room","temperate","shady",True,False,False,False,False,True,True,0,"forest",False,False,"","a cave below the large oak tree",[],[],[],[],[])

birds_nest = scene_type(3,5,0,"a bird's nest","cosy","dimly lit",True,False,False,False,True,True,False,0,"forest",False,False,"","you are in a house made of twigs and branches",[],[],[],[],[])
 # Forest

forest_a = scene_type(4,5,0,"the dark forest","cold","shady",False,False,False,False,False,True,False,0,"forest",False,False,"","it's dark here",[],[],[],[],[])
forest_b = scene_type(4,4,0,"the dark forest","cold","shady",False,False,False,False,False,True,False,1,"forest",False,False,"","the smell of pine forest is very strong here",[],[],[],[],[])
forest_c = scene_type(5,5,0,"the dark forest","cold","shady",False,False,False,False,False,True,False,0,"forest",False,False,"","lots of trees...",[],[],[],[],[])
forest_d = scene_type(5,4,0,"the dark forest","cold","shady",False,False,False,False,False,True,False,1,"forest",False,False,"","there's a circle of rocks in a small clearing",[],[],[],[],[])
forest_e = scene_type(4,3,0,"the dark forest","cold","shady",False,False,False,False,False,True,False,0,"forest",False,False,"","small mushrooms litter the ground here",[],[],[],[],[])
forest_f = scene_type(3,4,0,"the dark forest","cold","shady",False,False,False,False,False,True,False,0,"forest",False,False,"","there is smoke to the north",[],[],[],[],[])
forest_g = scene_type(5,3,0,"the dark forest","cold","shady",False,False,False,False,False,True,False,0,"forest",False,False,"","",[],[],[],[],[])
forest_h = scene_type(2,3,0,"the dark forest","cold","shady",False,False,False,False,False,True,False,0,"forest",False,False,"","the forest isn't so dense here",[],[],[],[],[])
forest_i = scene_type(4,6,0,"the dark forest","cold","shady",False,False,False,False,False,True,False,0,"forest",False,False,"","",[],[],[],[],[])
forest_j = scene_type(5,6,0,"the dark forest","cold","shady",False,False,False,False,False,True,False,0,"forest",False,False,"","",[],[],[],[],[])
forest_k = scene_type(2,6,0,"the dark forest","cold","shady",False,False,False,False,False,True,False,0,"forest",False,False,"","",[],[],[],[],[])
forest_l = scene_type(3,6,0,"the dark forest","cold","shady",False,False,False,False,False,True,False,0,"forest",False,False,"","",[],[],[],[],[])
forest_m = scene_type(2,4,0,"the dark forest","cold","shady",False,False,False,False,False,True,False,0,"forest",False,False,"","",[],[],[],[],[])
forest_n = scene_type(3,2,0,"the dark forest","cold","shady",False,False,False,False,False,True,False,0,"forest",False,False,"","",[],[],[],[],[])

forest_cabin = scene_type(3,3,0,"the forest cabin","temperate","cloudy",True,False,False,False,True,True,False,0,"dirt",False,False,"", "a nice log cabin, many strange objects are displayed on shelves and a large desk has piles of books next to it.",[],[],[],[],[])

grassland_a = scene_type(2,0,0,"grassland","cold","shady",False,False,False,False,False,True,False,0,"grassy",False,False,"","wide open space, lots of grass",[],[],[],[],[])
grassland_b = scene_type(3,0,0,"grassland","cold","shady",False,False,False,False,False,True,False,0,"grassy",False,False,"","wide open space, lots of grass",[],[],[],[],[])
grassland_c = scene_type(4,0,0,"grassland","cold","shady",False,False,False,False,False,True,False,0,"grassy",False,False,"","wide open space, lots of grass",[],[],[],[],[])
grassland_d = scene_type(2,1,0,"grassland","cold","shady",False,False,False,False,False,True,False,0,"grassy",False,False,"","wide open space, lots of grass",[],[],[],[],[])
grassland_e = scene_type(4,1,0,"grassland","cold","shady",False,False,False,False,False,True,False,0,"grassy",False,False,"","wide open space, lots of grass",[],[],[],[],[])
grassland_f = scene_type(2,2,0,"grassland","cold","shady",False,False,False,False,False,True,False,0,"grassy",False,False,"","wide open space, lots of grass",[],[],[],[],[])
grassland_g = scene_type(4,2,0,"grassland","cold","shady",False,False,False,False,False,True,False,0,"grassy",False,False,"","wide open space, lots of grass",[],[],[],[],[])

grassland_h = scene_type(7,6,0,"grassland","cold","shady",False,False,False,False,False,True,False,0,"grassy",False,False,"","wide open space, lots of grass",[],[],[],[],[])
grassland_i = scene_type(8,6,0,"grassland","cold","shady",False,False,False,False,False,True,False,0,"grassy",False,False,"","wide open space, lots of grass",[],[],[],[],[])

north_beach_a = scene_type(8,0,0,"the northern beach","hot","sunny",True,True,False,False,True,True,False,0,"sandy",False,False,"","the ocean stretches off to the north",[],[],[],[],[])
north_beach_b = scene_type(9,0,0,"the northern beach","hot","sunny",True,True,False,False,True,True,False,0,"sandy",False,False,"","the ocean stretches off to the north",[],[],[],[],[])
north_beach_c = scene_type(8,1,0,"the northern beach","hot","sunny",True,True,False,False,True,True,False,0,"sandy",False,False,"","the ocean stretches off to the north",[],[],[],[],[])
north_beach_d = scene_type(9,1,0,"the northern sand dunes","hot","sunny",True,True,False,False,True,True,False,0,"sandy",False,False,"","the ocean stretches off to the north",[],[],[],[],[])

# xpos, ypos, zpos, name, temp_string, light_string,
# is_safe, can_fish, can_cook, can_craft, can_steal, passable, treasure, difficulty, biome_String,
# has_stairs, indoors, impass_msg, flavour_text,
# scene_inventory, scene_weapon_inventory, scene_armor_inventory, scene_helmet_inventory, scene_shield_inventory

# Dismurth

dismurth_docks_searocks_a = scene_type(7,0,0,"rocky shore","hot","sunny",True,True,False,False,True,True,False,0,"seaside",False,False,"","the ocean stretches off to the north and east, large waves are crashing against the rocks...",[],[],[],[],[])
dismurth_docks_searocks_b = scene_type(5,0,0,"rocky shore","hot","sunny",True,True,False,False,True,True,False,0,"seaside",False,False,"","the ocean stretches off to the north and east, large waves are crashing against the rocks...",[],[],[],[],[])

crossroads = scene_type(6,5,0,"the crossroads","temperate","sunny",False,False,False,False,False,True,False,0,"road",False,False,"","There is a sign pointing north labelled \' Dismurth \' ",[],[],[],[],[])
east_road = scene_type(7,5,0,"the east road","hot","sunny",False,False,False,False,False,True,False,0,"road",False,False,"","this narrow road leads from the crossroads to the east",[],[],[],[],[])
north_road = scene_type(6,4,0,"the north road","hot","sunny",False,False,False,False,False,True,False,0,"road",False,False,"","this road leads from the crossroads to the northern town of Dismurth, it looks well travelled",[],[],[],[],[])
dismurth_gates = scene_type(6,3,0,"the town gates of Dismurth","hot","sunny",True,False,False,False,True,True,False,0,"town",False,False,"","",[],[],[],[],[])
dismurth_square = scene_type(6,2,0,"the town square of Dismurth","hot","sunny",True,False,False,False,True,True,False,0,"town",False,False,"","",[],[],[],[],[])
dismurth_market = scene_type(6,1,0,"Dismurth markets","hot","sunny",True,False,False,False,True,True,False,0,"town",False,False,"","",[],[],[],[],[])
dismurth_tavern = scene_type(5,1,0,"Dismurth tavern","hot","sunny",True,False,False,False,True,True,False,0,"town",False,False,"","",[],[],[],[],[])
dismurth_docks = scene_type(6,0,0,"the docks of Dismurth","hot","sunny",True,True,False,False,True,True,False,0,"town",False,False,"","",[],[],[],[],[])
dismurth_tower_1f = scene_type(7,1,1,"the tower of Dismurth's first floor","hot","sunny",True,False,False,False,True,True,False,0,"town",True,True,"","the tower walls are lined with more bookshelves",[],[],[],[],[])
dismurth_tower_gf = scene_type(7,1,0,"the tower of Dismurth's ground floor","hot","sunny",True,False,False,False,True,True,False,0,"town",True,True,"","the tower walls are lined with bookshelves, there are many large runestones in the middle of the room",[],[],[],[],[])
dismurth_smith = scene_type(7,2,0,"the Blacksmith of Dismurth","hot","sunny",True,False,False,False,True,True,False,0,"town",False,False,"","*a young man is working hard at the furnace*",[],[],[],[],[])
dismurth_barracks = scene_type(5,2,0,"the Barracks of Dismurth","warm","dimly liy",True,False,False,False,True,True,False,0,"town",False,False,"","you are surrounded by bunks and weapon racks, there is a large table in the middle of the room, a fire crackles in the corner",[],[],[],[],[])
dismurth_farm = scene_type(7,3,0,"the Dismurth farmstead","hot","sunny",True,False,False,False,True,True,False,0,"dirt",False,False,"","",[],[],[],[],[])
rocky_shore_a = scene_type(9,2,0,"rocky shore","hot","sunny",True,True,False,False,False,True,False,0,"seaside",False,False,"","turnips bruzzy",[],[],[],[],[])
rocky_shore_b = scene_type(9,3,0,"rocky shore","hot","sunny",True,True,False,False,False,True,False,0,"seaside",False,False,"","turnips bruzzy",[],[],[],[],[])
dismurth_fisherman_house = scene_type(8,2,0,"fisherman's house","hot","sunny",True,False,False,False,True,True,False,0,"town",False,False,"","turnips bruzzy",[],[],[],[],[])
turnip_field = scene_type(8,3,0,"a turnip field","hot","sunny",True,False,False,False,True,True,False,0,"dirt",False,False,"","turnips bruzzy",[],[],[],[],[])
highlands_a = scene_type(7,4,0,"highlands","humid","sunny",False,False,False,False,False,True,True,1,"grassy",False,False,"","grass and low stone walls form paddocks around you",[],[],[],[],[])
highlands_b = scene_type(8,4,0,"highlands","humid","sunny",False,False,False,False,False,True,True,1,"grassy",False,False,"","",[],[],[],[],[])

fortress_gate = scene_type(8,5,0,"the bandit fortress gates","humid","sunny",False,False,False,False,False,True,False,100,"forest",False,False,"","",[],[],[],[],[])
fortress = scene_type(9,5,0,"the bandit fortress","humid","sunny",False,False,False,False,False,True,True,100,"forest",False,False,""," surrounded by a palisade wall",[],[],[],[],[])
fort_wall_a = scene_type(9,4,0,"fortress wall","temp_string","light_string",False,False,False,False,False,False,False,0,"forest",False,False,"the large, wooden wall blocks your path","",[],[],[],[],[])
fort_wall_b = scene_type(10,5,0,"fortress wall","temp_string","light_string",False,False,False,False,False,False,False,0,"forest",False,False,"the large, wooden wall blocks your path","",[],[],[],[],[])
fort_wall_c = scene_type(9,6,0,"fortress wall","temp_string","light_string",False,False,False,False,False,False,False,0,"forest",False,False,"the large, wooden wall blocks your path","",[],[],[],[],[])

highlands_c = scene_type(10,10,0,"highlands","humid","sunny",False,False,False,False,False,True,False,0,"forest",False,False,"","",[],[],[],[],[])

plains_a = scene_type(4,9,0,"plains","humid","sunny",False,False,False,False,False,True,False,0,"grassy",False,False,"","sandy plains",[],[],[],[],[])
plains_b = scene_type(5,9,0,"plains","humid","sunny",False,False,False,False,False,True,False,0,"grassy",False,False,"","sandy plains",[],[],[],[],[])
plains_c = scene_type(4,9,0,"plains","humid","sunny",False,False,False,False,False,True,False,0,"grassy",False,False,"","sandy plains",[],[],[],[],[])
plains_d = scene_type(4,10,0,"plains","humid","sunny",False,False,False,False,False,True,False,0,"grassy",False,False,"","sandy plains",[],[],[],[],[])
plains_e = scene_type(5,10,0,"plains","humid","sunny",False,False,False,False,False,True,False,0,"grassy",False,False,"","sandy plains",[],[],[],[],[])
plains_f = scene_type(2,8,0,"plains","humid","sunny",False,False,False,False,False,True,False,0,"grassy",False,False,"","sandy plains",[],[],[],[],[])
plains_g = scene_type(5,11,0,"plains","humid","sunny",False,False,False,False,False,True,False,0,"grassy",False,False,"","sandy plains",[],[],[],[],[])
plains_h = scene_type(7,8,0,"plains","humid","sunny",False,False,False,False,False,True,False,0,"grassy",False,False,"","sandy plains",[],[],[],[],[])
plains_i = scene_type(7,9,0,"plains","humid","sunny",False,False,False,False,False,True,False,0,"grassy",False,False,"","sandy plains",[],[],[],[],[])
plains_j = scene_type(7,10,0,"plains","humid","sunny",False,False,False,False,False,True,False,0,"grassy",False,False,"","sandy plains",[],[],[],[],[])
plains_k = scene_type(7,11,0,"plains","humid","sunny",False,False,False,False,False,True,False,0,"grassy",False,False,"","sandy plains",[],[],[],[],[])

plains_l = scene_type(8,8,0,"plains","humid","sunny",False,False,False,False,False,True,False,0,"grassy",False,False,"","sandy plains",[],[],[],[],[])
plains_m = scene_type(8,9,0,"plains","humid","sunny",False,False,False,False,False,True,False,0,"grassy",False,False,"","sandy plains",[],[],[],[],[])
plains_n = scene_type(8,10,0,"plains","humid","sunny",False,False,False,False,False,True,False,0,"grassy",False,False,"","sandy plains",[],[],[],[],[])
plains_o = scene_type(8,11,0,"plains","humid","sunny",False,False,False,False,False,True,False,0,"grassy",False,False,"","sandy plains",[],[],[],[],[])

woods_a = scene_type(9,8,0,"woods","humid","sunny",False,False,False,False,False,True,False,0,"forest",False,False,"","some nice woods",[],[],[],[],[])
woods_b = scene_type(9,9,0,"woods","humid","sunny",False,False,False,False,False,True,False,0,"forest",False,False,"","interesting woods",[],[],[],[],[])
woods_c = scene_type(9,10,0,"woods","humid","sunny",False,False,False,False,False,True,False,0,"forest",False,False,"","strange woods",[],[],[],[],[])
woods_d = scene_type(9,11,0,"woods","humid","sunny",False,False,False,False,False,True,False,0,"forest",False,False,"","a massive boulder looms above the trees, some pieces have fallen off",[],[],[],[],[])

woods_d = scene_type(10,8,0,"woods","humid","sunny",False,False,False,False,False,True,False,0,"forest",False,False,"","some nice woods",[],[],[],[],[])
woods_e = scene_type(10,9,0,"woods","humid","sunny",False,False,False,False,False,True,False,0,"forest",False,False,"","interesting woods",[],[],[],[],[])
woods_f = scene_type(10,10,0,"woods","humid","sunny",False,False,False,False,False,True,False,0,"forest",False,False,"","strange woods",[],[],[],[],[])
woods_g = scene_type(10,11,0,"woods","humid","sunny",False,False,False,False,False,True,False,0,"forest",False,False,"","a massive boulder looms above the trees, some pieces have fallen off",[],[],[],[],[])


crags = scene_type(15,15,0,"crags","temperate","cloudy",False,False,False,False,False,True,False,0,"forest",False,False,"", "some particularly generic crags, very rocky indeed",[],[],[],[],[])
fields = scene_type(16,16,0,"ordinary fields","temperate","cloudy",False,False,False,False,False,True,False,0,"forest",False,False,"", "some particularly generic fields",[],[],[],[],[])
swamp = scene_type(17,17,0,"swamp","temperate","cloudy",False,False,False,False,False,True,False,0,"forest",False,False,"", "some particularly generic fields",[],[],[],[],[])

south_road_a = scene_type(6,6,0,"the south road","temperate","cloudy",True,False,False,False,False,True,False,0,"road",False,False,"", "this road leads from the crossroads to the south ",[],[],[],[],[])
dismurth_bridge = scene_type(6,7,0,"the Dismurth bridge","temperate","cloudy",True,False,False,False,False,True,False,0,"road",False,False,"you may not cross the bridge without rite of passage", "the river looks nice from here",[],[],[],[],[])
south_road_b = scene_type(6,8,0,"the south road","temperate","cloudy",True,False,False,False,False,True,False,0,"road",False,False,"", "this road continues from the crossroads to the south",[],[],[],[],[])

# xpos, ypos, zpos, name, temp_string, light_string,
# is_safe, can_fish, can_cook, can_craft, can_steal, passable, treasure, difficulty, biome_String,
# has_stairs, indoors, impass_msg, flavour_text,
# scene_inventory, scene_weapon_inventory, scene_armor_inventory, scene_helmet_inventory, scene_shield_inventory

# Sorlund

high_road_a = scene_type(5,8,0,"the high road","temperate","cloudy",True,False,False,False,False,True,False,0,"road",False,False,"", "this road continues from the crossroads to the south west",[],[],[],[],[])
high_road_b = scene_type(4,8,0,"the high road","temperate","cloudy",True,False,False,False,False,True,False,0,"road",False,False,"", "this road continues from the crossroads to the south west",[],[],[],[],[])
high_road_c = scene_type(3,8,0,"the high road","temperate","cloudy",True,False,False,False,False,True,False,0,"road",False,False,"", "this road continues from the crossroads to the south west",[],[],[],[],[])
high_road_d = scene_type(3,9,0,"the high road","temperate","cloudy",True,False,False,False,False,True,False,0,"road",False,False,"", "this road continues from the crossroads to the south west",[],[],[],[],[])
high_road_e = scene_type(3,10,0,"the high road","temperate","cloudy",True,False,False,False,False,True,False,0,"road",False,False,"", "this road continues from the crossroads to the south west",[],[],[],[],[])
high_road_f = scene_type(3,11,0,"the high road","temperate","cloudy",True,False,False,False,False,True,False,0,"road",False,False,"", "this road continues from the crossroads to the south west",[],[],[],[],[])
high_road_g = scene_type(3,12,0,"the high road","temperate","cloudy",True,False,False,False,False,True,False,0,"road",False,False,"", "this road continues from the crossroads to the south west",[],[],[],[],[])
high_road_h = scene_type(3,13,0,"the high road","temperate","cloudy",True,False,False,False,False,True,False,0,"road",False,False,"", "this road continues from the crossroads to the south west",[],[],[],[],[])

sorlund_church = scene_type(2,9,0,"the Sorlund church","temperate","cloudy",True,False,False,False,False,True,False,0,"town",False,False,"", "an ancient monument to the gods of harvest",[],[],[],[],[])
sorlund_graveyard = scene_type(1,9,0,"the Sorlund graveyard","temperate","cloudy",True,False,False,False,False,True,False,0,"town",False,False,"", "the people of Sorlund bury their dead here...",[],[],[],[],[])
sorlund_tavern = scene_type(2,11,0,"the Sorlund tavern","temperate","cloudy",True,False,False,False,False,True,False,0,"town",False,False,"", "A tavern",[],[],[],[],[])
sorlund_training_ground = scene_type(4,11,0,"the training ground","temperate","cloudy",True,False,False,False,False,True,False,0,"town",False,False,"", "the melee training ground for the Sorlund millita",[],[],[],[],[])


# south east cave
cave_entrance = scene_type(6,9,0,"a cave entrance","temperate","cloudy",True,False,False,False,False,True,False,0,"cave",False,False,"", "there is a cave enterance in the ground here, looks like it goes straight down",[],[],[],[],[])
cave_a = scene_type(6,9,-1,"a cave","temperate","cloudy",True,False,False,False,False,True,False,0,"cave",False,False,"", "this cave goes down further...",[],[],[],[],[])
cave_b = scene_type(6,9,-2,"a cave","temperate","cloudy",True,False,False,False,False,True,False,0,"cave",False,False,"", "this cave goes down further...",[],[],[],[],[])
cave_c = scene_type(6,9,-3,"a cave","temperate","cloudy",True,False,False,False,False,True,False,0,"cave",False,False,"", "this cave goes down further...",[],[],[],[],[])
cave_d = scene_type(6,9,-4,"a cave","temperate","cloudy",True,False,False,False,False,True,False,0,"cave",False,False,"", "this cave goes down further...",[],[],[],[],[])
cave_e = scene_type(6,9,-5,"a cave","temperate","cloudy",True,False,False,False,False,True,False,0,"cave",False,False,"", "this cave goes down further...",[],[],[],[],[])
cave_f = scene_type(6,9,-6,"a cave","temperate","cloudy",True,False,False,False,False,True,False,0,"cave",False,False,"", "this cave goes down further...",[],[],[],[],[])
cave_g = scene_type(6,9,-7,"a cave","temperate","cloudy",True,False,False,False,False,True,False,0,"cave",False,False,"", "this cave goes down further...",[],[],[],[],[])
cave_h = scene_type(6,9,-8,"a cave","temperate","cloudy",True,False,False,False,False,True,False,0,"cave",False,False,"", "there is a cavern below...",[],[],[],[],[])

cavern_a = scene_type(6,9,-9,"the center of a cavern","temperate","cloudy",True,False,False,False,False,True,False,0,"cave",False,False,"", "there is light coming from above...",[],[],[],[],[])
cavern_b = scene_type(6,8,-9,"a cavern","temperate","cloudy",False,False,False,False,False,True,False,1,"cave",False,False,"", "",[],[],[],[],[])
cavern_c = scene_type(6,10,-9,"a cavern","temperate","cloudy",False,False,False,False,False,True,False,1,"cave",False,False,"", "",[],[],[],[],[])
cavern_d = scene_type(5,8,-9,"a cavern","temperate","cloudy",False,False,False,False,False,True,False,1,"cave",False,False,"", "",[],[],[],[],[])
cavern_e = scene_type(5,9,-9,"a cavern","temperate","cloudy",False,False,False,False,False,True,False,1,"cave",False,False,"", "",[],[],[],[],[])
cavern_f = scene_type(5,10,-9,"a cavern","temperate","cloudy",False,False,False,False,False,True,False,1,"cave",False,False,"", "",[],[],[],[],[])
cavern_g = scene_type(7,8,-9,"a cavern","temperate","cloudy",False,False,False,False,False,True,False,1,"cave",False,False,"", "",[],[],[],[],[])
cavern_h = scene_type(7,9,-9,"a cavern","temperate","cloudy",False,False,False,False,False,True,False,1,"cave",False,False,"", "",[],[],[],[],[])
cavern_i = scene_type(7,10,-9,"a cavern","temperate","cloudy",False,False,False,False,False,True,False,1,"cave",False,False,"", "",[],[],[],[],[])

### north cave
north_cave_entrance = scene_type(3,1,0,"a cave entrance","temperate","cloudy",True,False,False,False,False,True,False,0,"cave",False,False,"", "there is a cave enterance in the ground here, looks like it goes straight down",[],[],[],[],[])
north_cave_a = scene_type(3,1,-1,"a cave","temperate","cloudy",True,False,False,False,False,True,False,0,"cave",False,False,"", "this cave goes down further, there is light coming from above...",[],[],[],[],[])
north_cave_b = scene_type(3,1,-2,"a cave","temperate","cloudy",True,False,False,False,False,True,False,0,"cave",False,False,"", "this cave goes down further, there is light coming from above...",[],[],[],[],[])
north_cave_c = scene_type(3,1,-3,"a cave","temperate","cloudy",True,False,False,False,False,True,False,0,"cave",False,False,"", "this cave goes down further, there is a faint light coming from above...",[],[],[],[],[])
north_cave_d = scene_type(3,1,-4,"a cave","temperate","cloudy",True,False,False,False,False,True,False,0,"cave",False,False,"", "this cave goes down further, there is a faint light coming from above...",[],[],[],[],[])
north_cave_e = scene_type(3,1,-5,"a cave","temperate","cloudy",True,False,False,False,False,True,False,0,"cave",False,False,"", "this cave goes down further, there is a faint light coming from above...",[],[],[],[],[])
north_cave_f = scene_type(3,1,-6,"a cave","temperate","cloudy",True,False,False,False,False,True,False,0,"cave",False,False,"", "this cave goes down further, there is a faint light coming from above...",[],[],[],[],[])
north_cave_g = scene_type(3,1,-7,"a cave","temperate","cloudy",True,False,False,False,False,True,False,0,"cave",False,False,"", "this cave goes down further, there is a faint light coming from above...",[],[],[],[],[])
north_cave_h = scene_type(3,1,-8,"a cave","temperate","cloudy",True,False,False,False,False,True,False,0,"cave",False,False,"", "there is a tunnnel below, there is a very faint light coming from above...",[],[],[],[],[])

# underground tunnel
tunnel_a = scene_type(3,1,-9,"an underground tunnel","temperate","cloudy",False,False,False,False,False,True,False,2,"cave",False,False,"", "there is a very faint light coming from above...",[],[],[],[],[])
tunnel_b = scene_type(4,1,-9,"an underground tunnel","temperate","cloudy",False,False,False,False,False,True,False,2,"cave",False,False,"", "this is an ancient tunnel, i wonder why it's here",[],[],[],[],[])
tunnel_c = scene_type(5,1,-9,"an underground tunnel","temperate","cloudy",False,False,False,False,False,True,False,2,"cave",False,False,"", "there are carvings on the wall, they depict goblins fighting some kind of demonic creature.",[],[],[],[],[])
tunnel_d = scene_type(6,1,-9,"an underground tunnel","temperate","cloudy",False,False,False,False,False,True,False,2,"cave",False,False,"", "there are carvings of goblins and humans massed in a large army, 2",[],[],[],[],[])

tunnel_e = scene_type(6,2,-9,"an underground tunnel","temperate","cloudy",False,False,False,False,False,True,False,2,"cave",False,False,"", "this is an ancient tunnel, i wonder why it's here",[],[],[],[],[])
tunnel_f = scene_type(6,3,-9,"an underground tunnel","temperate","cloudy",False,False,False,False,False,True,False,2,"cave",False,False,"", "this is an ancient tunnel, carvings depict a three headed dragon fighting a large demon",[],[],[],[],[])
tunnel_g = scene_type(6,4,-9,"an underground tunnel","temperate","cloudy",False,False,False,False,False,True,False,2,"cave",False,False,"", "this is an ancient tunnel, skeletons of ancient warriors line the walls here",[],[],[],[],[])
tunnel_h = scene_type(6,5,-9,"an underground tunnel","temperate","cloudy",False,False,False,False,False,True,False,2,"cave",False,False,"", "this is an ancient tunnel",[],[],[],[],[])
tunnel_i = scene_type(6,6,-9,"an underground tunnel","temperate","cloudy",False,False,False,False,False,True,False,2,"cave",False,False,"", "this is an ancient tunnel, it smells of decay",[],[],[],[],[])
tunnel_j = scene_type(6,7,-9,"an underground tunnel","temperate","cloudy",False,False,False,False,False,True,False,2,"cave",False,False,"", "this is an ancient tunnel, the air is still",[],[],[],[],[])
tunnel_k = scene_type(6,8,-9,"an underground tunnel","temperate","cloudy",False,False,False,False,False,True,False,2,"cave",False,False,"", "this is an ancient tunnel, it's carved from solid rock",[],[],[],[],[])

tunnel_l = scene_type(3,5,-9,"an underground tunnel","temperate","cloudy",False,False,False,False,False,True,False,2,"cave",False,False,"", "this is an ancient tunnel, it's carved from solid rock",[],[],[],[],[])
tunnel_m = scene_type(4,5,-9,"an underground tunnel","temperate","cloudy",False,False,False,False,False,True,False,2,"cave",False,False,"", "this is an ancient tunnel, it's carved from solid rock",[],[],[],[],[])
tunnel_n = scene_type(5,5,-9,"an underground tunnel","temperate","cloudy",False,False,False,False,False,True,False,2,"cave",False,False,"", "this is an ancient tunnel, it's carved from solid rock",[],[],[],[],[])

cavern_j = scene_type(2,5,-9,"a misty cavern","temperate","cloudy",False,False,False,False,False,True,False,1,"cave",False,False,"", "",[],[],[],[],[])
cavern_k = scene_type(2,4,-9,"a misty cavern","temperate","cloudy",False,False,False,False,False,True,True,1,"cave",False,False,"", "",[],[],[],[],[])
cavern_l = scene_type(1,5,-9,"a misty cavern","temperate","cloudy",False,False,False,False,False,True,True,1,"cave",False,False,"", "",[],[],[],[],[])
cavern_m = scene_type(2,6,-9,"a misty cavern","temperate","cloudy",False,False,False,False,False,True,True,1,"cave",False,False,"", "",[],[],[],[],[])












###--  UNIQUE IMPASSABLE TERRAIN  --###

cliffs_a = scene_type(1,0,0,"cliffs","temp_string","light_string",False,False,False,False,False,False,False,0,"dirt",False,False,"cliffs block your path","",[],[],[],[],[])
cliffs_b = scene_type(1,1,0,"cliffs","temp_string","light_string",False,False,False,False,False,False,False,0,"dirt",False,False,"cliffs block your path","",[],[],[],[],[])
cliffs_c = scene_type(1,2,0,"cliffs","temp_string","light_string",False,False,False,False,False,False,False,0,"dirt",False,False,"cliffs block your path","",[],[],[],[],[])
cliffs_d = scene_type(1,3,0,"cliffs","temp_string","light_string",False,False,False,False,False,False,False,0,"dirt",False,False,"cliffs block your path","",[],[],[],[],[])
cliffs_e = scene_type(1,4,0,"cliffs","temp_string","light_string",False,False,False,False,False,False,False,0,"dirt",False,False,"cliffs block your path","",[],[],[],[],[])
cliffs_f = scene_type(0,5,0,"cliffs","temp_string","light_string",False,False,False,False,False,False,False,0,"dirt",False,False,"cliffs block your path","",[],[],[],[],[])
lake_a = scene_type(0,7,0,"lake","temp_string","light_string",False,False,False,False,False,False,False,0,"water",False,False,"a deep lake blocks your path","",[],[],[],[],[])
lake_b = scene_type(1,7,0,"lake","temp_string","light_string",False,False,False,False,False,False,False,0,"water",False,False,"a deep lake blocks your path","",[],[],[],[],[])
lake_c = scene_type(0,8,0,"lake","temp_string","light_string",False,False,False,False,False,False,False,0,"water",False,False,"a deep lake blocks your path","",[],[],[],[],[])
lake_d = scene_type(1,8,0,"lake","temp_string","light_string",False,False,False,False,False,False,False,0,"water",False,False,"a deep lake blocks your path","",[],[],[],[],[])
lake_e = scene_type(0,6,0,"lake","temp_string","light_string",False,False,False,False,False,False,False,0,"water",False,False,"a deep lake blocks your path","",[],[],[],[],[])

river_a = scene_type(2,7,0,"river","temp_string","light_string",False,False,False,False,False,False,False,0,"water",False,False,"a river blocks your path","",[],[],[],[],[])
river_b = scene_type(3,7,0,"river","temp_string","light_string",False,False,False,False,False,False,False,0,"water",False,False,"a river blocks your path","",[],[],[],[],[])
river_c = scene_type(4,7,0,"river","temp_string","light_string",False,False,False,False,False,False,False,0,"water",False,False,"a river blocks your path","",[],[],[],[],[])
river_d = scene_type(5,7,0,"river","temp_string","light_string",False,False,False,False,False,False,False,0,"water",False,False,"a river blocks your path","",[],[],[],[],[])
river_e = scene_type(7,7,0,"river","temp_string","light_string",False,False,False,False,False,False,False,0,"water",False,False,"a river blocks your path","",[],[],[],[],[])
river_f = scene_type(8,7,0,"river","temp_string","light_string",False,False,False,False,False,False,False,0,"water",False,False,"a river blocks your path","",[],[],[],[],[])
river_g = scene_type(9,7,0,"river","temp_string","light_string",False,False,False,False,False,False,False,0,"water",False,False,"a river blocks your path","",[],[],[],[],[])
river_h = scene_type(10,7,0,"river","temp_string","light_string",False,False,False,False,False,False,False,0,"water",False,False,"a river blocks your path","",[],[],[],[],[])
river_i = scene_type(11,7,0,"river","temp_string","light_string",False,False,False,False,False,False,False,0,"water",False,False,"a river blocks your path","",[],[],[],[],[])
river_j = scene_type(12,7,0,"river","temp_string","light_string",False,False,False,False,False,False,False,0,"water",False,False,"a river blocks your path","",[],[],[],[],[])
river_k = scene_type(13,7,0,"river","temp_string","light_string",False,False,False,False,False,False,False,0,"water",False,False,"a river blocks your path","",[],[],[],[],[])
river_l = scene_type(14,7,0,"river","temp_string","light_string",False,False,False,False,False,False,False,0,"water",False,False,"a river blocks your path","",[],[],[],[],[])
river_m = scene_type(14,8,0,"river","temp_string","light_string",False,False,False,False,False,False,False,0,"water",False,False,"a river blocks your path","",[],[],[],[],[])
river_n = scene_type(15,8,0,"river","temp_string","light_string",False,False,False,False,False,False,False,0,"water",False,False,"a river blocks your path","",[],[],[],[],[])
river_o = scene_type(16,8,0,"river","temp_string","light_string",False,False,False,False,False,False,False,0,"water",False,False,"a river blocks your path","",[],[],[],[],[])
river_p = scene_type(17,8,0,"river","temp_string","light_string",False,False,False,False,False,False,False,0,"water",False,False,"a river blocks your path","",[],[],[],[],[])
river_p = scene_type(31,8,0,"river","temp_string","light_string",False,False,False,False,False,False,False,0,"water",False,False,"a river blocks your path","",[],[],[],[],[])

###--  IMPASSABLE TERRAIN  --###


ocean = scene_type(999,999,999,"the ocean","temp_string","light_string",False,False,False,False,False,False,False,0,"water",False,False,"the ocean blocks your escape","",[],[],[],[],[])

solid_cave_wall = scene_type(998,998,998,"a solid cave wall","temp_string","light_string",False,False,False,False,False,False,False,0,"dirt",False,False,"a sheer wall of rock blocks your path","",[],[],[],[],[])
solid_cave_ground = scene_type(997,997,997,"a solid cave floor","temp_string","light_string",False,False,False,False,False,False,False,0,"dirt",False,False,"a floor of rock blocks your path","",[],[],[],[],[])
ground = scene_type(996,996,996,"the ground","temp_string","light_string",False,False,False,False,False,False,False,0,"dirt",False,False,"the ground blocks your path","",[],[],[],[],[])
sky = scene_type(995,995,995,"the sky","temp_string","light_string",False,False,False,False,False,False,False,0,"seaside",False,False,"you cannot fly","",[],[],[],[],[])
solid_dungeon_wall = scene_type(994,994,994,"a solid dungeon wall","temp_string","light_string",False,False,False,False,False,False,False,0,"dirt",False,False,"a wall of stone brick blocks your path","",[],[],[],[],[])
solid_dungeon_ground = scene_type(993,993,993,"a solid dungeon floor","temp_string","light_string",False,False,False,False,False,False,False,0,"dirt",False,False,"a floor of stone brick blocks your path","",[],[],[],[],[])
