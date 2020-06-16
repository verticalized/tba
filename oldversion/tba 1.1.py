import random

###########################----GLOBAL_VARIABLES-----####################

time = 0
steps_x = 5
steps_y = -1
steps_z = 0
prev_x = 0
prev_y = 0
prev_z = 0
in_fight = False
dev_mode = 0

raining = 1
weather = 0
season = 3 # value from 0,3 that determines season
days = 19
months = 4
years = 1567

all_scene_types = []
all_game_items = []
all_ground_game_items = []
all_game_weapons = []
all_ground_game_weapons = []
all_game_armor = []
all_ground_game_armor = []

default_drop_table_items = []
default_drop_table_weapons = []
default_drop_table_armor = []

###########################------CLASSES------#########################
#to do list:

#add quest class and make bandit quest
#more enemies
#more spells
#make more locations, dungeons, undeground areas

class scene_type:
    def __init__(self, xpos, ypos, zpos, name, temp, light, safe, npc, passable, impass_msg, flavour, scene_inventory, scene_weapon_inventory, scene_armor_inventory):
        self.xpos = xpos
        self.ypos = ypos
        self.zpos = zpos
        self.name = name
        self.temp = temp
        self.light = light
        self.safe = safe
        self.npc = npc
        self.passable = passable
        self.impass_msg = impass_msg
        self.flavour = flavour
        self.scene_inventory = scene_inventory
        self.scene_weapon_inventory = scene_weapon_inventory
        self.scene_armor_inventory = scene_armor_inventory

        all_scene_types.append(self)

hills = scene_type(0,0,0,"the hills","temperate","sunny",True,True,True,"","rolling green hills",[],[],[])
large_tree = scene_type(1,0,0,"a large tree","temperate","shady",True,False,True,"","a very, very large oak tree",[],[],[])
birds_nest = scene_type(2,0,0,"a bird's nest","cosy","dimly lit",True,True,True,"","you are in a house made of twigs and branches",[],[],[])

forest_a = scene_type(3,0,0,"the dark forest","cold","shady",False,False,True,"","it's dark here",[],[],[])
forest_b = scene_type(3,1,0,"the dark forest","cold","shady",False,False,True,"","the smell of pine forest is very strong here",[],[],[])
forest_c = scene_type(4,0,0,"the dark forest","cold","shady",False,False,True,"","lots of trees...",[],[],[])
forest_d = scene_type(4,1,0,"the dark forest","cold","shady",False,False,True,"","there's a circle of rocks in a small clearing",[],[],[])
forest_e = scene_type(3,2,0,"the dark forest","cold","shady",False,False,True,"","small mushrooms litter the ground here",[],[],[])
forest_f = scene_type(2,1,0,"the dark forest","cold","shady",False,False,True,"","there is a smoke to the north",[],[],[])
forest_g = scene_type(4,2,0,"the dark forest","cold","shady",False,False,True,"","blaze it..",[],[],[])
forest_h = scene_type(4,-1,0,"the dark forest","cold","shady",False,False,True,"","the forest isn't so dense here",[],[],[])
forest_i = scene_type(3,-1,0,"the dark forest","cold","shady",False,False,True,"","",[],[],[])
forest_j = scene_type(2,-1,0,"the dark forest","cold","shady",False,False,True,"","",[],[],[])
forest_k = scene_type(1,-1,0,"the dark forest","cold","shady",False,False,True,"","",[],[],[])
forest_l = scene_type(1,1,0,"the dark forest","cold","shady",False,False,True,"","",[],[],[])
forest_m = scene_type(1,2,0,"the dark forest","cold","shady",False,False,True,"","",[],[],[])
forest_n = scene_type(2,3,0,"the dark forest","cold","shady",False,False,True,"","",[],[],[])

forest_cabin = scene_type(2,2,0,"the forest cabin","temperate","cloudy",True,True,True,"", "a nice log cabin, many strange objects are displayed on shelves and a large desk has piles of books next to it.",[],[],[])

grassland_a = scene_type(2,5,0,"grassland","cold","shady",False,False,True,"","wide open space, lots of grass",[],[],[])
grassland_b = scene_type(1,5,0,"grassland","cold","shady",False,False,True,"","wide open space, lots of grass",[],[],[])
grassland_c = scene_type(1,4,0,"grassland","cold","shady",False,False,True,"","wide open space, lots of grass",[],[],[])
grassland_d = scene_type(1,3,0,"grassland","cold","shady",False,False,True,"","wide open space, lots of grass",[],[],[])
grassland_e = scene_type(3,5,0,"grassland","cold","shady",False,False,True,"","wide open space, lots of grass",[],[],[])
grassland_f = scene_type(3,4,0,"grassland","cold","shady",False,False,True,"","wide open space, lots of grass",[],[],[])
grassland_g = scene_type(3,3,0,"grassland","cold","shady",False,False,True,"","wide open space, lots of grass",[],[],[])

grassland_h = scene_type(6,-1,0,"grassland","cold","shady",False,False,True,"","wide open space, lots of grass",[],[],[])
grassland_i = scene_type(7,-1,0,"grassland","cold","shady",False,False,True,"","wide open space, lots of grass",[],[],[])

crossroads = scene_type(5,0,0,"the crossroads","temperate","sunny",False,False,True,"","There is a sign pointing north labelled \' Dismurth \' ",[],[],[])
east_road = scene_type(6,0,0,"the east road","hot","sunny",False,False,True,"","this narrow road leads from the crossroads to the east",[],[],[])
north_road = scene_type(5,1,0,"the north road","hot","sunny",False,False,True,"","this road leads from the crossroads to the northern town of Dismurth, it looks well travelled",[],[],[])
dismurth_gates = scene_type(5,2,0,"the town gates of Dismurth","hot","sunny",True,True,True,"","",[],[],[])
dismurth_square = scene_type(5,3,0,"the town square of Dismurth","hot","sunny",True,True,True,"","",[],[],[])
dismurth_smith = scene_type(6,3,0,"the Blacksmith of Dismurth","hot","sunny",True,True,True,"","*a young man is working hard at the furnace*",[],[],[])
dismurth_barracks = scene_type(4,3,0,"the Barracks of Dismurth","warm","dimly liy",True,True,True,"","you are surrounded by bunks and weapon racks, there is a large table in the middle of the room, a fire crackles in the corner",[],[],[])
dismurth_farm = scene_type(6,2,0,"the Dismurth farmstead","hot","sunny",True,True,True,"","",[],[],[])
turnip_field = scene_type(7,2,0,"a turnip field","hot","sunny",True,True,True,"","turnips bruzzy",[],[],[])

fortress_gate = scene_type(7,0,0,"the bandit fortress gates","humid","sunny",False,False,True,"","",[],[],[])
fortress = scene_type(8,0,0,"the bandit fortress","humid","sunny",False,False,True,""," surrounded by a palisade wall",[],[],[])
wall_a = scene_type(8,1,0,"fortress wall","temp_string","light_string",False,False,False,"the large, wooden wall blocks your path","",[],[],[])
wall_b = scene_type(8,-1,0,"fortress wall","temp_string","light_string",False,False,False,"the large, wooden wall blocks your path","",[],[],[])
wall_c = scene_type(9,0,0,"fortress wall","temp_string","light_string",False,False,False,"the large, wooden wall blocks your path","",[],[],[])

highlands = scene_type(10,10,0,"highlands","humid","sunny",False,False,True,"","",[],[],[])
moors = scene_type(11,11,0,"the moors","humid","sunny",False,False,True,"","damp grass and low stone walls form paddocks around you",[],[],[])
woods = scene_type(12,12,0,"woods","humid","sunny",False,False,True,"","",[],[],[])
plains_a = scene_type(-1,2,0,"plains","humid","sunny",False,False,True,"","sandy plains",[],[],[])
plains_b = scene_type(-1,1,0,"plains","humid","sunny",False,False,True,"","sandy plains",[],[],[])
crags = scene_type(15,15,0,"crags","temperate","cloudy",False,False,True,"", "some particularly generic crags, very rocky indeed",[],[],[])
fields = scene_type(16,16,0,"ordinary fields","temperate","cloudy",False,False,True,"", "some particularly generic fields",[],[],[])

south_road_a = scene_type(5,-1,0,"the south road","temperate","cloudy",True,False,True,"", "this road leads from the crossroads to the south ",[],[],[])
dismurth_bridge = scene_type(5,-2,0,"the Dismurth bridge","temperate","cloudy",True,False,True,"", "the water looks nice from here",[],[],[])
south_road_b = scene_type(5,-3,0,"the south road","temperate","cloudy",True,False,True,"", "this road continues from the crossroads to the south",[],[],[])


#south east cave
cave_entrance = scene_type(5,-4,0,"a cave entrance","temperate","cloudy",True,False,True,"", "there is a cave enterance in the ground here, looks like it goes straight down",[],[],[])
cave_a = scene_type(5,-4,-1,"a cave","temperate","cloudy",True,False,True,"", "this cave goes down further...",[],[],[])
cave_b = scene_type(5,-4,-2,"a cave","temperate","cloudy",True,False,True,"", "there is a cavern below..",[],[],[])
cavern_a = scene_type(5,-4,-3,"the center of a cavern","temperate","cloudy",True,False,True,"", "there is light coming from above...",[],[],[])
cavern_b = scene_type(5,-3,-3,"a cavern","temperate","cloudy",False,False,True,"", "",[],[],[])
cavern_c = scene_type(5,-5,-3,"a cavern","temperate","cloudy",False,False,True,"", "",[],[],[])
cavern_d = scene_type(6,-3,-3,"a cavern","temperate","cloudy",False,False,True,"", "",[],[],[])
cavern_e = scene_type(4,-3,-3,"a cavern","temperate","cloudy",False,False,True,"", "",[],[],[])
cavern_f = scene_type(4,-4,-3,"a cavern","temperate","cloudy",False,False,True,"", "",[],[],[])
cavern_g = scene_type(4,-5,-3,"a cavern","temperate","cloudy",False,False,True,"", "",[],[],[])
cavern_h = scene_type(6,-4,-3,"a cavern","temperate","cloudy",False,False,True,"", "",[],[],[])
cavern_i = scene_type(6,-5,-3,"a cavern","temperate","cloudy",False,False,True,"", "",[],[],[])

#north cave
north_cave_entrance = scene_type(2,4,0,"a cave entrance","temperate","cloudy",True,False,True,"", "there is a cave enterance in the ground here, looks like it goes straight down",[],[],[])
north_cave_a = scene_type(2,4,-1,"a cave","temperate","cloudy",True,False,True,"", "this cave goes down further...",[],[],[])
north_cave_b = scene_type(2,4,-2,"a cave","temperate","cloudy",True,False,True,"", "there is a tunnnel below..",[],[],[])
tunnel_a = scene_type(2,4,-3,"an underground tunnel","temperate","cloudy",True,False,True,"", "there is light coming from above...",[],[],[])
tunnel_b = scene_type(3,4,-3,"an underground tunnel","temperate","cloudy",True,False,True,"", "this is an ancient tunnel, i wonder why it's here",[],[],[])
tunnel_c = scene_type(4,4,-3,"an underground tunnel","temperate","cloudy",True,False,True,"", "there are carvings on the wall, they depict goblins fighting some kind of demonic creature.",[],[],[])
tunnel_d = scene_type(5,4,-3,"an underground tunnel","temperate","cloudy",True,False,True,"", "this is an ancient tunnel, i wonder why it's here",[],[],[])

tunnel_e = scene_type(5,3,-3,"an underground tunnel","temperate","cloudy",True,False,True,"", "this is an ancient tunnel, i wonder why it's here",[],[],[])
tunnel_f = scene_type(5,2,-3,"an underground tunnel","temperate","cloudy",True,False,True,"", "this is an ancient tunnel, i wonder why it's here",[],[],[])
tunnel_g = scene_type(5,1,-3,"an underground tunnel","temperate","cloudy",True,False,True,"", "this is an ancient tunnel, i wonder why it's here",[],[],[])
tunnel_h = scene_type(5,0,-3,"an underground tunnel","temperate","cloudy",True,False,True,"", "this is an ancient tunnel, i wonder why it's here",[],[],[])
tunnel_i = scene_type(5,-1,-3,"an underground tunnel","temperate","cloudy",True,False,True,"", "this is an ancient tunnel, i wonder why it's here",[],[],[])
tunnel_j = scene_type(5,-2,-3,"an underground tunnel","temperate","cloudy",True,False,True,"", "this is an ancient tunnel, i wonder why it's here",[],[],[])
tunnel_k = scene_type(5,-3,-3,"an underground tunnel","temperate","cloudy",True,False,True,"", "this is an ancient tunnel, i wonder why it's here",[],[],[])

cliffs_a = scene_type(-1,0,0,"cliffs","temp_string","light_string",False,False,False,"cliffs block your path","",[],[],[])
cliffs_b = scene_type(0,1,0,"cliffs","temp_string","light_string",False,False,False,"cliffs block your path","",[],[],[])
cliffs_c = scene_type(0,2,0,"cliffs","temp_string","light_string",False,False,False,"cliffs block your path","",[],[],[])
river_a = scene_type(1,-2,0,"river","temp_string","light_string",False,False,False,"a river blocks your path","",[],[],[])
river_b = scene_type(2,-2,0,"river","temp_string","light_string",False,False,False,"a river blocks your path","",[],[],[])
river_c = scene_type(3,-2,0,"river","temp_string","light_string",False,False,False,"a river blocks your path","",[],[],[])
river_d = scene_type(4,-2,0,"river","temp_string","light_string",False,False,False,"a river blocks your path","",[],[],[])
river_e = scene_type(6,-2,0,"river","temp_string","light_string",False,False,False,"a river blocks your path","",[],[],[])
river_f = scene_type(7,-2,0,"river","temp_string","light_string",False,False,False,"a river blocks your path","",[],[],[])
river_g = scene_type(8,-2,0,"river","temp_string","light_string",False,False,False,"a river blocks your path","",[],[],[])
lake_a = scene_type(0,-2,0,"lake","temp_string","light_string",False,False,False,"a deep lake blocks your path","",[],[],[])
lake_b = scene_type(0,-3,0,"lake","temp_string","light_string",False,False,False,"a deep lake blocks your path","",[],[],[])
lake_c = scene_type(-1,-2,0,"lake","temp_string","light_string",False,False,False,"a deep lake blocks your path","",[],[],[])
lake_d = scene_type(-1,-3,0,"lake","temp_string","light_string",False,False,False,"a deep lake blocks your path","",[],[],[])

ocean = scene_type(999,999,999,"the ocean","temp_string","light_string",False,False,False,"the ocean blocks your escape","",[],[],[])
solid_cave_wall = scene_type(998,998,998,"a solid cave wall","temp_string","light_string",False,False,False,"a sheer wall of rock blocks your path","",[],[],[])
solid_cave_ground = scene_type(997,997,997,"a solid cave floor","temp_string","light_string",False,False,False,"a floor of rock blocks your path","",[],[],[])
ground = scene_type(996,996,996,"the ground","temp_string","light_string",False,False,False,"the ground blocks your path","",[],[],[])
sky = scene_type(995,995,995,"the sky","temp_string","light_string",False,False,False,"you are unable to move up","",[],[],[])

class player_stats:
    def __init__(self, name, level, xp, hp, gp, magic, strength, attack, maxhp, strength_xp, attack_xp, magic_xp, status_effect):
        self.name = name
        self.level = level
        self.xp = xp
        self.hp = hp
        self.gp = gp
        self.magic = magic
        self.strength = strength
        self.attack = attack
        self.maxhp = maxhp
        self.strength_xp = strength_xp
        self.attack_xp = attack_xp
        self.magic_xp = magic_xp
        self.status_effect = status_effect


player1 = player_stats("The Hero",1,1,900,500,2,2,5,900,0,0,0,0)

class quest:
    def __init__(self, name, quest_desc, xp, gp, reward):
        self.name = name
        self.quest_desc = quest_desc
        self.xp = xp
        self.gp = gp
        self.reward = reward

quest_1 = quest("The Bandit Menace","eliminate the local bandit population",200,80,[])

#########################################--ITEMS/WEAPONS/ARMOR/SPELLS--#############################################

class item:
    def __init__(self, id, name, value, edible, poisonous, hp):
        self.id = id
        self.name = name
        self.value = value
        self.edible = edible
        self.poisonous = poisonous
        self.hp = hp

        all_game_items.append(self)

apple = item(100,"apple",5,True,True,10)
pear = item(101,"pear",20,True,False,10)
worms = item(102,"worms",500,False,False,0)
beak_polish = item(103,"beak polish",10,False,False,0)
cup = item(104,"cup",12,False,False,0)
pendant = item(105,"pendant",80,False,False,0)
legion_seal = item(106,"legion seal",7,False,False,0)
tea_bag = item(107,"tea bag",1,False,False,0)
cup_of_tea = item(108,"cup of tea",2,True,False,8)
tent = item(108,"tent",20,True,False,8)
rope = item(109,"rope",5,False,False,0)
torch = item(110,"torch",5,False,False,0)
hp_potion = item(111,"hp potion",20,True,False,1000)
bones = item(112,"bones",2,False,False,0)

class ground_item:
    def __init__(self, name):
        self.name = name

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
ground_hp_potion = ground_item("bones")

class weapon:
    def __init__(self, id, name, value, type, level, attribute):
        self.id = id
        self.name = name
        self.value = value
        self.type = type
        self.level = level
        self.attribute = attribute

        all_game_weapons.append(self)

bird_sword = weapon(201,"bird sword",10,"sword",5,"air")
super_bird_sword = weapon(202,"super bird sword",180,"sword",50,"air")
iron_sword = weapon(203,"iron sword",8,"sword",5,"earth")
steel_sword = weapon(204,"steel sword",80,"sword",10,"earth")
iron_axe = weapon(205,"iron axe",8,"sword",5,"earth")
steel_axe = weapon(206,"steel axe",80,"sword",10,"earth")
greatsword = weapon(207,"greatsword",800,"large sword",32,"water")
ultra_greatsword = weapon(208,"ultra_greatsword",8000,"large sword",54,"water")
war_spear = weapon(209,"war spear",80,"spear",16,"fire")
lance = weapon(210,"lance",80,"spear",28,"air")


class ground_weapon:
    def __init__(self, name):
        self.name = name

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


class armor:
    def __init__(self, id, name, value, type, level, attribute):
        self.id = id
        self.name = name
        self.value = value
        self.type = type
        self.level = level
        self.attribute = attribute

        all_game_armor.append(self)

birdshirt = armor(301,"bird t shirt",100,"light",99,"air")
leather_armor = armor(302,"leather armor",10,"light",1,"water")
hard_leather_armor = armor(303,"hard leather armor",10,"light",10,"water")
iron_chain_mail = armor(304,"iron chain mail",40,"heavy",12,"earth")
iron_plate_armor = armor(305,"iron plate armor",100,"heavy",15,"earth")
steel_chain_mail = armor(306,"steel chain mail",400,"heavy",14,"earth")
steel_plate_armor = armor(307,"steel plate armor",1000,"heavy",22,"earth")
rags = armor(308,"rags",1,"light",1,"fire")
mage_robes = armor(309,"mage robes",1000,"mage",20,"air")
necro_robes = armor(309,"necromancer robes",1000,"mage",44,"air")

class ground_armor:
    def __init__(self, name):
        self.name = name

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

class spell:
    def __init__(self, name, utility, damage, attribute, xp, effect, spell_desc):
        self.name = name
        self.utility = utility
        self.damage = damage
        self.attribute = attribute
        self.xp = xp
        self.effect = effect
        self.spell_desc = spell_desc

############--COMBAT SPELLS--#############

#tier 1 spells
fireball = spell("fireball",False,100,"fire",200,0,"heavy fire damage")
hydro_barrage = spell("hydro barrage",False,100,"water",200,0,"heavy water damage")

#tier 2 spells
hydroblast = spell("hydroblast",False,60,"water",100,0,"light water damage")
fireblast = spell("fireblast",False,60,"fire",100,0,"light fire damage")

#####--HEALING SPELLS--####

#tier 1 spells
super_heal = spell("super heal",True,100,"holy",50,1,"a super healing spell")

#tier 2 spells
prayer = spell("prayer",True,100,"holy",50,1,"a light healing spell")

##################--STATUS EFFECT SPELLS--##############################

#status 2 spells
snare = spell("snare",True,5,"ice",70,2,"snares the enemy")

#status 3 spells
poison = spell("poison",True,5,"water",70,3,"poisons the enemy")

#status 4 spells
burn = spell("poison",True,5,"fire",70,4,"burns the enemy")
###################################--ENEMIES--##########################################

class enemy_stats:
    def __init__(self, name, level, xp, hp, gp, magic, strength, attack, maxhp, attribute, weakness, spellbook, drop_table_items, drop_table_weapons, drop_table_armor, status_effect):
        self.name = name
        self.level = level
        self.xp = xp
        self.hp = hp
        self.gp = gp
        self.magic = magic
        self.strength = strength
        self.attack = attack
        self.maxhp = maxhp
        self.attribute = attribute
        self.weakness = weakness
        self.spellbook = spellbook
        self.drop_table_items = drop_table_items
        self.drop_table_weapons = drop_table_weapons
        self.drop_table_armor = drop_table_armor
        self.status_effect = status_effect

        self.drop_table_items.extend(default_drop_table_items)
        self.drop_table_weapons.extend(default_drop_table_weapons)
        self.drop_table_armor.extend(default_drop_table_armor)

goblin = enemy_stats("goblin",1,5,100,10,0,5,2,100,"earth","earth",[],[],[],[],0)
hobgoblin = enemy_stats("hobgoblin",3,290,500,67,1,4,5,300,"earth","earth",[],[],[],[],0)
bandit = enemy_stats("bandit",2,10,200,0,0,5,2,100,"fire","earth",[],[],[],[],0)
legion_soldier = enemy_stats("legion soldier",28,500,1000,0,0,14,20,1000,"air","earth",[],[],[],[],0)
legion_spearman = enemy_stats("legion spearman",25,500,1050,0,0,16,10,1050,"air","earth",[],[],[],[],0)
mushroom_man = enemy_stats("mushroom man",67,800,100,10,0,5,2,100,"earth","earth",[],[],[],[],0)
bird_warrior = enemy_stats("bird warrior",101,5000,2807,1,0,30,22,100,"air","earth",[],[],[],[],0)

fire_elemental = enemy_stats("fire elemental",5,100,40,0,3,5,2,100,"fire","earth",[],[],[],[],0)
water_elemental = enemy_stats("water elemental",5,100,40,0,3,5,2,100,"water","earth",[],[],[],[],0)
earth_elemental = enemy_stats("earth elemental",5,100,40,0,3,5,2,100,"earth","earth",[],[],[],[],0)
air_elemental = enemy_stats("air elemental",5,100,40,0,3,5,2,100,"air","earth",[],[],[],[],0)

giant_snail = enemy_stats("giant snail",1,5,92,10,0,5,2,100,"earth","earth",[],[],[],[],0)
giant_spider = enemy_stats("giant spider",1,64,100,10,0,5,2,100,"earth","earth",[],[],[],[],0)
giant_moth = enemy_stats("giant moth",1,5,134,10,0,5,2,100,"earth","earth",[],[],[],[],0)

################------ENEMY_SPELLBOOKS------#############

hobgoblin.spellbook.append(fireblast)

fire_elemental.spellbook.append(fireblast)
fire_elemental.spellbook.append(fireblast)
fire_elemental.spellbook.append(fireblast)
fire_elemental.spellbook.append(fireblast)

water_elemental.spellbook.append(hydroblast)
water_elemental.spellbook.append(hydroblast)
water_elemental.spellbook.append(hydroblast)
water_elemental.spellbook.append(hydroblast)

############################----DROP_TABLES-###########################

##default drop tables
weapons_drop_table = []
large_weapons_drop_table = []
armor_drop_table = []

default_drop_table_items.append(bones.name)
default_drop_table_armor.append(rags.name)

weapons_drop_table.append(iron_sword.name)
weapons_drop_table.append(iron_axe.name)
weapons_drop_table.append(steel_sword.name)
weapons_drop_table.append(steel_axe.name)

large_weapons_drop_table.append(war_spear.name)
large_weapons_drop_table.append(greatsword.name)
large_weapons_drop_table.append(lance.name)
large_weapons_drop_table.append(ultra_greatsword.name)

armor_drop_table.append(leather_armor.name)
armor_drop_table.append(hard_leather_armor.name)
armor_drop_table.append(iron_chain_mail.name)
armor_drop_table.append(iron_plate_armor.name)


#####################################################################

goblin.drop_table_weapons.extend(weapons_drop_table)
hobgoblin.drop_table_weapons.extend(weapons_drop_table)
bandit.drop_table_weapons.extend(weapons_drop_table)

legion_soldier.drop_table_weapons.extend(large_weapons_drop_table)
legion_spearman.drop_table_weapons.extend(large_weapons_drop_table)
bird_warrior.drop_table_weapons.extend(large_weapons_drop_table)

###########################------LISTS------#########################

players = []

players.append(player1)

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

inventory.append(pear)
inventory.append(tent)
inventory.append(rope)
inventory.append(torch)
inventory.append(hp_potion)

# weapon_inventory.append(super_bird_sword)
# armor_inventory.append(iron_chain_mail)

equiped_armor = []
equiped_weapon = []

equiped_weapon.append(iron_sword)
equiped_armor.append(rags)

equiped_spells = []

equiped_spells.append(fireball)
equiped_spells.append(snare)
equiped_spells.append(fireblast)
equiped_spells.append(super_heal)
equiped_spells.append(poison)

#################

sir_kobious_inventory = []

sir_kobious_inventory.append(legion_seal)

old_man_inventory = []

old_man_inventory.append(pendant)

blacksmith_inventory = []

blacksmith_inventory.append(iron_chain_mail)
blacksmith_inventory.append(leather_armor)
blacksmith_inventory.append(iron_plate_armor)

bird_store_inventory = []
bird_store_armor = []
bird_store_weapon = []

bird_store_inventory.append(worms)
bird_store_inventory.append(beak_polish)

bird_store_armor.append(birdshirt)

bird_store_weapon.append(super_bird_sword)

#############################----COMBAT_FUNCTIONS----#########################

def func_choose_enemy():
    combat_mod = random.randint(0,100)
    combat_rating = random.randint(0,100)
    if dev_mode != 0:
        print("Combat mod:", combat_mod)
        print("Combat rating:", combat_rating)


    #rolls for which enemy to fight
    if steps_z == 0: #check if on surface

        if combat_mod < 25:
            if combat_rating >= 0 and combat_rating < 25:
                current_enemies.append(goblin)
            if combat_rating >= 25 and combat_rating < 50:
                current_enemies.append(goblin)
            if combat_rating >= 50 and combat_rating < 75:
                current_enemies.append(bandit)
            if combat_rating >= 75 and combat_rating <= 100:
                current_enemies.append(bandit)

        if combat_mod >= 25 and combat_mod <= 50:
            if combat_rating >= 0 and combat_rating < 25:
                current_enemies.append(fire_elemental)
            if combat_rating >= 25 and combat_rating < 50:
                current_enemies.append(bandit)
            if combat_rating >= 50 and combat_rating < 75:
                current_enemies.append(bandit)
            if combat_rating >= 75 and combat_rating <= 100:
                current_enemies.append(hobgoblin)

        if combat_mod >= 50 and combat_mod <= 75:
            if combat_rating >= 0 and combat_rating < 25:
                current_enemies.append(fire_elemental)
            if combat_rating >= 25 and combat_rating < 50:
                current_enemies.append(water_elemental)
            if combat_rating >= 50 and combat_rating < 75:
                current_enemies.append(bandit)
            if combat_rating >= 75 and combat_rating <= 100:
                current_enemies.append(hobgoblin)

        if combat_mod >= 75 and combat_mod <= 100:
            if combat_rating >= 0 and combat_rating < 25:
                current_enemies.append(legion_soldier)
            if combat_rating >= 25 and combat_rating < 50:
                current_enemies.append(legion_spearman)
            if combat_rating >= 50 and combat_rating < 75:
                current_enemies.append(mushroom_man)
            if combat_rating >= 75 and combat_rating <= 100:
                current_enemies.append(bird_warrior)

    if steps_z <= -1: #check if underground
        if combat_mod < 25:
            if combat_rating >= 0 and combat_rating < 25:
                current_enemies.append(goblin)
            if combat_rating >= 25 and combat_rating < 50:
                current_enemies.append(goblin)
            if combat_rating >= 50 and combat_rating < 75:
                current_enemies.append(bandit)
            if combat_rating >= 75 and combat_rating <= 100:
                current_enemies.append(bandit)

        if combat_mod >= 25 and combat_mod <= 50:
            if combat_rating >= 0 and combat_rating < 25:
                current_enemies.append(fire_elemental)
            if combat_rating >= 25 and combat_rating < 50:
                current_enemies.append(bandit)
            if combat_rating >= 50 and combat_rating < 75:
                current_enemies.append(bandit)
            if combat_rating >= 75 and combat_rating <= 100:
                current_enemies.append(hobgoblin)

        if combat_mod >= 50 and combat_mod <= 75:
            if combat_rating >= 0 and combat_rating < 25:
                current_enemies.append(fire_elemental)
            if combat_rating >= 25 and combat_rating < 50:
                current_enemies.append(water_elemental)
            if combat_rating >= 50 and combat_rating < 75:
                current_enemies.append(bandit)
            if combat_rating >= 75 and combat_rating <= 100:
                current_enemies.append(hobgoblin)

        if combat_mod >= 75 and combat_mod <= 100:
            if combat_rating >= 0 and combat_rating < 25:
                current_enemies.append(legion_soldier)
            if combat_rating >= 25 and combat_rating < 50:
                current_enemies.append(legion_spearman)
            if combat_rating >= 50 and combat_rating < 75:
                current_enemies.append(mushroom_man)
            if combat_rating >= 75 and combat_rating <= 100:
                current_enemies.append(bird_warrior)


def func_enemy_dead():

            print("\n//////////// " + enemy_stats.name.upper() + " IS DEAD //////////// \n")
            player1.gp = player1.gp + enemy_stats.gp
            player1.xp = player1.xp + enemy_stats.xp
            print(enemy_stats.gp)
            print("gold obtained \n")
            print(enemy_stats.xp)
            print("xp obtained \n")

            loot_spawn_chance_item = 0
            loot_chance_item = 0
            loot_amount_item = 0
            loot_spawn_chance_weapon = 0
            loot_chance_weapon = 0
            loot_amount_weapon = 0
            loot_spawn_chance_armor= 0
            loot_chance_armor = 0
            loot_amount_armor = 0
            loot_quality = 0

            loot_spawn_chance_item = random.randint(0,1)
            loot_spawn_chance_weapon = random.randint(0,1)
            loot_spawn_chance_armor = random.randint(0,1)

            if loot_spawn_chance_item == 1:
                if len(enemy_stats.drop_table_items) != 0:
                    for item.name in enemy_stats.drop_table_items:
                        loot_chance_item = random.randint(0,1)
                        if loot_chance_item == 1:
                            for ground_item in all_ground_game_items:
                                if ground_item.name == item.name:
                                    scene_type.scene_inventory.append(ground_item.name)
                                    print(enemy_stats.name + " dropped " + item.name + " \n")
                            loot_amount_item = random.randint(0,1)
                            if loot_amount_item == 1:
                                break

            if loot_spawn_chance_weapon == 1:
                if len(enemy_stats.drop_table_weapons) != 0:
                    for weapon.name in enemy_stats.drop_table_weapons:
                        loot_chance_weapon = random.randint(0,1)
                        if loot_chance_weapon == 1:
                            for ground_weapon in all_ground_game_weapons:
                                if ground_weapon.name == weapon.name:
                                    scene_type.scene_weapon_inventory.append(ground_weapon.name)
                                    print(enemy_stats.name + " dropped " + weapon.name + " \n" )
                            loot_amount_weapon = random.randint(0,1)
                            if loot_amount_weapon == 1:
                                break


            if loot_spawn_chance_armor == 1:
                if len(enemy_stats.drop_table_armor) != 0:
                    for armor.name in enemy_stats.drop_table_armor:
                        loot_chance_armor = random.randint(0,1)
                        if loot_chance_armor == 1:
                            for ground_armor in all_ground_game_armor:
                                if ground_armor.name == armor.name:
                                    scene_type.scene_inventory.append(ground_armor.name)
                                    print(enemy_stats.name + " dropped " + armor.name + " \n" )
                            loot_amount_armor = random.randint(0,1)
                            if loot_amount_armor == 1:
                                break

            del current_enemies[:]
            func_check_level()
            location_desc()

def func_player_spell():
    for enemy_stats in current_enemies:
        spell_damage = 0
        for spell in equiped_spells:
            if spell.name == spell_input:
                if spell.effect == 0:
                    spell_damage = spell.damage
                    print("you cast " + spell.name)
                    player_damage = (player1.level + spell_damage) * (player1.magic - enemy_stats.magic)
                    enemy_stats.hp = enemy_stats.hp - player_damage
                    print("\nspell damage: ")
                    print(spell_damage)
                    print("\nyou hit for:")
                    print(player_damage)
                    player1.magic_xp += (player1.magic + spell.xp + spell.damage)
                if spell.effect == 1:
                    spell_healing = spell.damage
                    print("you cast " + spell.name)
                    player_healing = (player1.level + spell_healing) * player1.magic
                    player_stats.hp = player_stats.hp + player_healing
                    if player_stats.hp > player_stats.maxhp:
                        player_stats.hp = player_stats.maxhp
                    print("\nspell healing: ")
                    print(spell_healing)
                    print("\nyou heal for:")
                    print(player_healing)
                    player1.magic_xp += (player1.magic + spell.xp + spell.damage)
                if spell.effect == 2:
                    enemy_stats.status_effect = 2
                    print("you freeze the " + enemy_stats.name)
                if spell.effect == 3:
                    enemy_stats.status_effect = 3
                    print("you poison the " + enemy_stats.name)
                if spell.effect == 4:
                    enemy_stats.status_effect = 4
                    print("you burn the " + enemy_stats.name)
    func_check_level()

def func_player_spell_non_combat():
    for spell in equiped_spells:
        if spell.name == spell_input:
            if spell.effect == 0:

                print("\nyou are not in combat...")

            if spell.effect == 1:
                spell_healing = spell.damage
                print("you cast " + spell.name)
                player_healing = (player1.level + spell_healing) * player1.magic
                player_stats.hp = player_stats.hp + player_healing
                if player_stats.hp > player_stats.maxhp:
                    player_stats.hp = player_stats.maxhp
                print("\nspell healing: ")
                print(spell_healing)
                print("\nyou heal for:")
                print(player_healing)
                player1.magic_xp += (player_healing)

def func_player_status_check():
    for player_stats in players:
        if player_stats.status_effect == 0:
            pass

        if player_stats.status_effect == 2:
            print("you are frozen and cannot move \n")
            defrost_chance = random.randint(0,1)
            if defrost_chance == 0:
                player_stats.status_effect = 0
                print("you broke free from the ice\n")
            else:
                player_stats.status_effect = 1
                print("you are still trapped by ice\n")

        if player_stats.status_effect == 3:
            player_poison_damage = (player_stats.maxhp/10)
            player_stats.hp -= enemy_poison_damage
            print("you took poison damage of:")
            print(player_poison_damage)

        if player_stats.status_effect == 4:
            player_burn_damage = (player_stats.maxhp/10)
            player_stats.hp -= player_burn_damage
            print("you took burn damage of:")
            print(player_burn_damage)

def func_enemy_status_check():
    if enemy_stats.status_effect == 0:
        func_enemy_attack()

    if enemy_stats.status_effect == 2:
        print("the " + enemy_stats.name + " is frozen and cannot move \n")
        defrost_chance = random.randint(0,1)
        if defrost_chance == 0:
            enemy_stats.status_effect = 0
            print("the " + enemy_stats.name + " broke free!\n")
        else:
            enemy_stats.status_effect = 1
            print("the " + enemy_stats.name + " is trapped by ice\n")

    if enemy_stats.status_effect == 3:
        enemy_poison_damage = (enemy_stats.maxhp/10)
        enemy_stats.hp -= enemy_poison_damage
        print("enemy took poison damage of:")
        print(enemy_poison_damage)
        func_check_enemy_dead()
        func_enemy_attack()

    if enemy_stats.status_effect == 4:
        enemy_burn_damage = (enemy_stats.maxhp/10)
        enemy_stats.hp -= enemy_burn_damage
        print("enemy took burn damage of:")
        print(enemy_burn_damage)
        func_check_enemy_dead()
        func_enemy_attack()

def func_check_enemy_dead():
    for enemy_stats in current_enemies:
        if enemy_stats.hp <= 0:
            in_fight = False
            func_enemy_dead()


def func_enemy_attack():
    for enemy_stats in current_enemies:
        if (not enemy_stats.spellbook):
            func_enemy_melee()
            break
        else:
            player_magic_level = 0
            enemy_spell_damage = 0
            spell_damage = 0
            for player_stats in players:
                player_magic_level = player_stats.magic
            for enemy_stats in current_enemies:
                for spell in enemy_stats.spellbook:
                    spellchance = random.randint(0,1)
                    if spellchance == 1:
                        print("\n" + enemy_stats.name + " casts a :")
                        print(spell.name)
                        spell_damage = spell.damage
                        enemy_spell_damage = (enemy_stats.level + spell_damage) * enemy_stats.magic
                        enemy_spell_damage = enemy_spell_damage - player_magic_level
                        player_stats.hp = player_stats.hp - (enemy_spell_damage - player1.strength)
                        print("\nyour magic defence level:")
                        print(player_magic_level)
                        print("\n" + enemy_stats.name + " hit you for")
                        print(enemy_spell_damage)
                        if player_stats.hp <= 0:
                            print("\nYOU ARE DEAD \n")
                            in_fight = False
                            del current_enemies[:]
                            game_start = 0
                        break
                    else:
                        func_enemy_melee()
                        break

def func_player_melee():
    for enemy_stats in current_enemies:
        player_weapon_level = 0
        for weapon in equiped_weapon:
            player_weapon_level = weapon.level
        player_damage = (player1.attack + player_weapon_level) * player1.strength
        enemy_stats.hp = enemy_stats.hp - player_damage
        print("\nyour weapon level: ")
        print(player_weapon_level)
        print("\nyou hit for:")
        print(player_damage)
        player1.attack_xp += (player1.attack * (player_damage))

def func_enemy_melee():
    for player_stats in players:
        player_armor_level = 0
        enemy_damage = 0
        for armor in equiped_armor:
            player_armor_level = armor.level
        for enemy_stats in current_enemies:
            enemy_damage = (enemy_stats.attack * enemy_stats.strength)
        enemy_damage = (enemy_damage - player_armor_level) - player1.strength
        player_stats.hp = player_stats.hp - enemy_damage
        print("\nyour armor level:")
        print(player_armor_level)
        print("\n" + enemy_stats.name + " hit you for")
        print(enemy_damage)
        player1.strength_xp += (player1.strength * (enemy_damage))
        if player_stats.hp <= 0:
            print("\nYOU ARE DEAD \n")
            in_fight = False
            del current_enemies[:]
            game_start = 0

#############################----FUNCTIONS----#########################

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
            scene_type.temp = "hot"
        if season == 1:
            scene_type.temp = "chilly"
        if season == 2:
            scene_type.temp = "very cold"
        if season == 3:
            scene_type.temp = "temperate"

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
                    scene_type.light = " and very dark, but slightly illuminated by your torch"
                else:
                    scene_type.light = " and very dark"

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
                        scene_type.light = ", very dark and lightly raining, your torch illuminates the area"
                    if raining >= 2 and steps_z >= 0:
                        scene_type.light = ", very dark and raining heavily, your torch illuminates the area"
                    if raining == 0 and steps_z >= 0:
                        scene_type.light = " and very dark, but well illuminated by your torch"
                else:
                    if raining == 1 and steps_z >= 0:
                        scene_type.light = ", very dark and lightly raining"
                    if raining >= 2 and steps_z >= 0:
                        scene_type.light = ", very dark and raining heavily"
                    if raining == 0 and steps_z >= 0:
                        scene_type.light = " and very dark"
            if is_night == False and season == 3:
                if raining == 1 and steps_z >= 0:
                    scene_type.light = " and lightly raining"
                if raining >= 2 and steps_z >= 0:
                    scene_type.light = " and raining heavily"
                if raining == 0 and steps_z >= 0:
                    scene_type.light = " and very overcast"
            if is_night == False and season != 3:
                if raining == 1 and steps_z >= 0:
                    scene_type.light = " and lightly raining"
                if raining >= 2 and steps_z >= 0:
                    scene_type.light = " and raining heavily"
                if raining == 0 and steps_z >= 0:
                    scene_type.light = " and very sunny"

def func_check_level():
    for player_stats in players:
        if player_stats.magic_xp >= (player_stats.magic ** 3):
            player_stats.magic += 1
            print("your magic level is now: ", player_stats.magic)
            func_check_level()

        if player_stats.strength_xp >= (player_stats.strength ** 3):
            player_stats.strength += 1
            print("your strength level is now: ", player_stats.strength)
            func_check_level()

        if player_stats.attack_xp >= (player_stats.attack ** 3):
            player_stats.attack += 1
            print("your attack level is now: ", player_stats.attack)
            func_check_level()

        if player_stats.xp >= (player_stats.level ** 3):
            player_stats.level += 1
            print("you are now level: ", player_stats.level)
            func_check_level()

        player_stats.maxhp = (player_stats.level * 100) + (player_stats.strength * 10) + (player_stats.attack * 10) + (player_stats.magic * 10)

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
        if steps_z <= -1:
            del location_north[:]
            location_north.append(solid_cave_wall)

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
        if steps_z <= -1:
            del location_south[:]
            location_south.append(solid_cave_wall)

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
        if steps_z <= -1:
            del location_east[:]
            location_east.append(solid_cave_wall)

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
        if steps_z <= -1:
            del location_west[:]
            location_west.append(solid_cave_wall)

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
        if steps_z <= -1:
            del location_down[:]
            location_down.append(solid_cave_ground)

def player_up_check():
    location_found = False
    for scene_type in all_scene_types:
        if steps_y == scene_type.ypos and steps_x == scene_type.xpos and steps_z+1 == scene_type.zpos:
            location_found = True
            del location_up[:]
            location_up.append(scene_type)
            break
    if location_found == False:
        if steps_z <= -1:
            del location_up[:]
            location_up.append(solid_cave_wall)
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
        for scene_type in location:
            print(scene_type.temp)
            print(scene_type.light)
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
        if dev_mode >= 2:
            for scene_type in all_scene_types:
                print(scene_type.name, scene_type.xpos, scene_type.ypos, scene_type.zpos)
    for scene_type in location:
        print("\nyou are in " + scene_type.name + "\n")
        print("it is " + scene_type.temp + "" + scene_type.light + ".")
        print("\"" + scene_type.flavour + "\" \n")
        if  len(scene_type.scene_inventory) != 0 or len(scene_type.scene_weapon_inventory) != 0 or len(scene_type.scene_armor_inventory) != 0:
            print("on the ground is:")
        else:
            print("there is nothing on the ground. \n")
        for ground_item.name in scene_type.scene_inventory:
            print(ground_item.name)
        for ground_weapon.name in scene_type.scene_weapon_inventory:
            print(ground_weapon.name)
        for ground_armor.name in scene_type.scene_armor_inventory:
            print(ground_armor.name)
        print(" ")


    func_rain()

    for scene_type in location_north:
        print("to your north is " + scene_type.name + "")
    for scene_type in location_south:
        print("to your south is " + scene_type.name + "")
    for scene_type in location_east:
        print("to your east is " + scene_type.name + "")
    for scene_type in location_west:
        print("to your west is " + scene_type.name + "")
    for scene_type in location_down:
        print("below you is " + scene_type.name + "")
    for scene_type in location_up:
        print("above you is " + scene_type.name + "")

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
func_check_level()

for player_stats in players:
    player_stats.hp = player_stats.maxhp # has to be last as max hp is calculated from all other stats


########## GAME START #########
print("Welcome to Bill & Phoebe's Adventure! \n")

# name = raw_input("Please enter your name: \n")
# for player_stats in players:
#     player_stats.name = name

while game_start == 1:

    func_check_level()
    player_position_check()
    location_desc()

    for scene_type in location:

        if scene_type.npc == True:
            print("there is someone here. \n")
        if scene_type.safe == False and in_fight == False:
            combat_chance = random.randint(0,100)
            if combat_chance > 50:
                in_fight = False
                print("it is peaceful and safe here at the moment... \n")
            if combat_chance < 50:
                in_fight = True
            if in_fight == True: #init combat
                func_choose_enemy()
                for enemy_stats in current_enemies:
                    # challenge_mod = random.randint(0,1)
                    # if challenge_mod == 0:
                    #     enemy_stats.maxhp = random.randint(1,50)+30/2 + ((0 + enemy_stats.maxhp) * enemy_stats.level)
                    # if challenge_mod == 1:
                    #     enemy_stats.maxhp = random.randint(1,50)+300/2 + ((0 + enemy_stats.maxhp) * enemy_stats.level)
                    enemy_stats.hp = (0 + enemy_stats.maxhp)
                    enemy_stats.gp = random.randint(0,10) * enemy_stats.maxhp
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

                    combat_input = raw_input("combat input: \n")

                    if combat_input == "run":
                        in_fight = False
                        print("you ran away! \n")
                        del current_enemies[:]
                        location_desc()

                    elif combat_input == "hit":
                        func_enemy_status_check()
                        func_player_melee()
                        func_check_enemy_dead()

                    elif combat_input == "spell":
                        print("\nYour equipped spells: \n")
                        for spell in equiped_spells:
                            print(spell.name)
                        print("")
                        spell_input = raw_input("which spell will you cast? \n")
                        has_spell = 0
                        for spell in equiped_spells:
                            if spell.name == spell_input:
                                has_spell = 1
                                func_enemy_status_check()
                                func_player_spell()
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

    func_check_level()

    input = raw_input("////////----input----/////// \n")

    if input == "look":
        pass


    elif input == "help":
        print("commands: \n north \n south \n east \n west \n down \n up \n equip \n stats \n drop \n pickup \n consume \n inv \n spellbook \n wait \n camp \n quit")

    elif input == "north":
        has_moved = True
        for scene_type in location_north:
            if scene_type.passable == True:
                steps_y += 1
                prev_y = steps_y
                prev_y -= 1
            else:
                print(scene_type.impass_msg + ", you have not moved.")

    elif input == "south":
        has_moved = True
        for scene_type in location_south:
            if scene_type.passable == True:
                steps_y -= 1
                prev_y = steps_y
                prev_y += 1
            else:
                print(scene_type.impass_msg + ", you have not moved")

    elif input == "east":
        for scene_type in location_east:
            if scene_type.passable == True:
                steps_x += 1
                prev_x = steps_x
                prev_x -= 1
            else:
                print(scene_type.impass_msg + ", you have not moved")

    elif input == "west":
        has_moved = True
        for scene_type in location_west:
            if scene_type.passable == True:
                steps_x -= 1
                prev_x = steps_x
                prev_x += 1
            else:
                print(scene_type.impass_msg + ", you have not moved")

    elif input == "down":
        has_rope = False
        for item in inventory:
            if item.name == "rope":
                has_rope = True
                for scene_type in location_down:
                    if scene_type.passable == True:
                        steps_z -= 1
                        prev_z = steps_z
                        prev_z += 1
                    else:
                        print(scene_type.impass_msg + ", you have not moved")
        if has_rope == False:
            print("you need a rope to climb up.")

    elif input == "up":
        has_rope = False
        for item in inventory:
            if item.name == "rope":
                has_rope = True
                for scene_type in location_up:
                    if scene_type.passable == True:
                        steps_z += 1
                        prev_z = steps_z
                        prev_z -= 1
                    else:
                        print(scene_type.impass_msg + ", you have not moved.")
        if has_rope == False:
            print("you need a rope to climb up.")

####################################################

    elif input == "equip":
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

        print("your gear:")
        for weapon in weapon_inventory:
            print(weapon.name)
        for armor in armor_inventory:
            print(armor.name)
        gear_equip = raw_input("what do you want to equip? \n")
        for weapon in weapon_inventory:
            if weapon.name == gear_equip:
                weapon_inventory.remove(weapon)
                del equiped_weapon[:]
                equiped_weapon.append(weapon)
                if current_weapon != "0":
                    for weapon in all_game_weapons:
                        if weapon.name == current_weapon:
                            weapon_inventory.append(weapon)
                break
        for armor in armor_inventory:
            if armor.name == gear_equip:
                armor_inventory.remove(armor)
                del equiped_armor[:]
                equiped_armor.append(armor)
                if current_armor != "0":
                    for armor in all_game_armor:
                        if armor.name == current_armor:
                            armor_inventory.append(armor)
                break

    elif input == "stats":
        for player1 in players:
            print("your stats: \n")
            print("name: " + player1.name)
            print("level: ", player1.level)
            print("xp: ", player1.xp)
            print("hp: ", player1.hp)
            print("maxhp: ", player1.maxhp)
            print("gold: ", player1.gp)
            print("magic:", player1.magic)
            print("magic xp:", player1.magic_xp)
            print("strength: ", player1.strength)
            print("strength xp: ", player1.strength_xp)
            print("attack: ", player1.attack)
            print("attack xp: ", player1.attack_xp)

            print("gear: \n")
            if len(equiped_armor) != 0:
                for armor in equiped_armor:
                    print("your armor stats: \n")
                    print("name: " + armor.name)
                    print("level: ", armor.level)
                    print("type: ", armor.type)
                    print("attribute: ", armor.attribute)
                print(" \n")
            else:
                print("you have no armor... \n")

            if len(equiped_weapon) != 0:
                for weapon in equiped_weapon:
                    print("your weapon stats: \n")
                    print("name: " + weapon.name)
                    print("level: ", weapon.level)
                    print("type: ", weapon.type)
                    print("attribute: ", weapon.attribute)
                print(" \n")
            else:
                print("you have no weapon... \n")

    elif input == "drop":
        dropped_item = raw_input("Which item do you want to drop? \n")
        has_item = False
        for item in inventory:
            if dropped_item == item.name:
                has_item = True
                print("you drop " + item.name + "\n")
                inventory.remove(item)
                break
        if has_item == True:
            for ground_item in all_ground_game_items:
                if ground_item.name == dropped_item:
                    scene_type.scene_inventory.append(ground_item.name)
                    break

        for weapon in weapon_inventory:
            if dropped_item == weapon.name:
                has_item = True
                print("you drop " + weapon.name + "\n")
                weapon_inventory.remove(weapon)
                break
        if has_item == True:
            for ground_weapon in all_ground_game_weapons:
                if ground_weapon.name == dropped_item:
                    scene_type.scene_weapon_inventory.append(ground_weapon.name)
                    break

        for armor in armor_inventory:
            if dropped_item == armor.name:
                has_item = True
                print("you drop " + armor.name + "\n")
                armor_inventory.remove(armor)
                break
        if has_item == True:
            for ground_armor in all_ground_game_armor:
                if ground_armor.name == dropped_item:
                    scene_type.scene_armor_inventory.append(ground_armor.name)
                    break

        if has_item == False:
            print("you don't have " + dropped_item + " in your inventory\n")

    elif input == "pickup":
        pickedup_item = raw_input("Which item do you want to pickup? \n")
        has_item = False
        for ground_item.name in scene_type.scene_inventory:
            if ground_item.name == pickedup_item:
                has_item = True
                print("you pickup " + ground_item.name + "\n")
                scene_type.scene_inventory.remove(ground_item.name)
                for item in all_game_items:
                    if item.name == pickedup_item:
                        inventory.append(item)
                        break
                break

        for ground_weapon.name in scene_type.scene_weapon_inventory:
            if ground_weapon.name == pickedup_item:
                has_item = True
                print("you pickup " + ground_weapon.name + "\n")
                scene_type.scene_weapon_inventory.remove(ground_weapon.name)
                for weapon in all_game_weapons:
                    if weapon.name == pickedup_item:
                        weapon_inventory.append(weapon)
                        break
                break

        for ground_armor.name in scene_type.scene_armor_inventory:
            if ground_armor.name == pickedup_item:
                has_item = True
                print("you pickup " + ground_armor.name + "\n")
                scene_type.scene_armor_inventory.remove(ground_armor.name)
                for armor in all_game_armor:
                    if armor.name == pickedup_item:
                        armor_inventory.append(armor)
                        break
                break

        if has_item == False:
            print("that is not on the ground.\n")

    elif input == "consume":
        eaten_item = raw_input("Which item do you want to consume? \n")
        has_item = False
        for item in inventory:
            if eaten_item == item.name:
                has_item = True
                if item.edible == True:
                    if item.poisonous == False:
                        print("you consume " + item.name)
                        player1.hp = player1.hp + item.hp
                        if player1.hp > player1.maxhp:
                            player1.hp = player1.maxhp
                    else:
                        print("you consume " + item.name)
                        player1.hp = player1.hp - item.hp
                        print("you feel sick")
                        if player1.hp <= 0:
                            print("\nYOU ARE DEAD \n")
                            game_start = 0
                    inventory.remove(item)
                    break
                else:
                    print("you can't consume " + item.name)
                    break

        if has_item == False:
            print("you don't have " + eaten_item)

##################################################

    elif input == "inv":
        if len(inventory) != 0:
            print("\nInventory: \n")
            for item in inventory:
                print(item.name)
            for armor in armor_inventory:
                print(armor.name)
            for weapon in weapon_inventory:
                print(weapon.name)
            print(" \n")
        else:
            print("you have no items... \n")

    elif input == "wait":
        for scene_type in location:
            print("\nYou wait in " + scene_type.name + " ... \n")

    elif input == "camp":
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

    elif input == "spell":
        print("\nYour equipped utility spells: \n")
        for spell in equiped_spells:
            if spell.effect == 1:
                print(spell.name)
        print("")
        spell_input = raw_input("which spell will you cast? \n")
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


    elif input == "spellbook":
        for spell in equiped_spells:
            print(spell.name, spell.spell_desc)
            print("\n")

#################----DIALOGUE----################

    elif input == "talk":
        for scene_type in location:
            if scene_type.npc == True:
                for scene_type in location:
                    if scene_type == birds_nest:

                        if (not equiped_weapon):
                            print "\nHello you look as though you could do with some supplies skwark!"
                            print "Here you go!\n"
                            inventory.append(worms)
                            equiped_weapon.append(bird_sword)
                            response = raw_input("bird expects a response...\n")
                            if response == "skwark!":
                                print("\n I like you skwark!\n")
                            else:
                                inventory.remove(worms)
                                print("*the bird snatches your worms and scowls*\n")
                        else:
                            print("hello welcome to the bird shop for birds skwark!\n")
                            response = raw_input("would you like to purchase any items?\n")
                            if response == "yes":
                                print("bird shop inventory:\n")
                                print("gold: ", player1.gp)
                                for item in bird_store_inventory:
                                    print(item.name + " ----- ", item.value, " gp. ")
                                bought_item = raw_input("please choose an item to buy skwark!\n")
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
                            elif response == "no":
                                print("I have other wares.\n")
                                response2 = raw_input("would you like to purchase any armor skwark!?\n")
                                if response2 == "yes":
                                    print("bird shop armory:\n")
                                    print("gold: ", player1.gp)
                                    for armor in bird_store_armor:
                                        print(armor.name + " ----- ", armor.value, " gp. ")
                                    bought_item = raw_input("\nplease choose some armor to buy skwark!\n")
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

                                        print("pardon!? skwark!\n")
                            else:

                                print("okay seeya! skwark!\n")

                    for scene_type in location:
                        if scene_type == hills:
                            print("\nhello I am an old man, I have travelled very far")
                            response = raw_input("I found this pendant *cough*, would you like it?\n")
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
                            response = raw_input("do you wish to learn the magic I have created?\n")
                            if response == "yes":
                                for player_stats in players:
                                    if player_stats.magic >= 10:
                                        equiped_spells.append(hydro_barrage)
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
                            response = raw_input("Before you can pass, you must answer this question, What is the meaning of life?\n")
                            if response == "fat doinks":
                                print("\nYou may enter, for you understand true path of righteousness \n")
                            else:
                                print("\njust kidding haha \n")

                    for scene_type in location:
                        if scene_type == dismurth_square:
                            print("\nhello")
                            response = raw_input("my name is Sir Kobious, I am from the glorious legion, do you support the legion!?\n")
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
                            response = raw_input("I am the blacksmith, would you like to purchase anything?\n")
                            if response == "yes":
                                print("gold: ", player1.gp)
                                print("blacksmith inventory:\n")
                                for armor in blacksmith_inventory:
                                    print(armor.name + " ----- ", armor.value, " gp. ")
                                bought_item = raw_input("please, choose an item to buy\n")
                                has_item = False
                                for armor in blacksmith_inventory:
                                    if bought_item == armor.name:
                                        has_item = True
                                        if player1.gp >= armor.value:
                                            player1.gp -= armor.value
                                            del equiped_armor [:]
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
                            response = raw_input("Those damn bandits keep attacking raiding our stores, you look like you can handle a fight, would you help us?\n")
                            if response == "yes":
                                print("\nthank you, their fortress is south of here, you might find them there, be careful! \n")

                            else:
                                print("Goodbye.\n")


            else:
                print "there is nobody to talk to\n"

#################################################

    elif input == "dev":
        dev_mode += 1
        if dev_mode >= 3:
            dev_mode = 0

    elif input == "quit":
        game_start = 0

    else:
        print "invalid command\n"

    time += 1
    if time >= 24:
        time = 0
        print("the sun has risen...")
        days += 1
        if days >= 30:
            days = 1
            months += 1
            if months >= 13:
                months = 1
                years += 1
                print("Happy new year " + player1.name + "! \nThe year is now:")
                print(years)

    if time == 12:
        print("the sun has gone down...")
