import random
from time import sleep
from colorama import init
from colorama import Fore, Back, Style

init(autoreset=True)

all_game_items = []
all_ground_game_items = []

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
        self.item_amount = 1
        self.item_weight = 1 * self.item_amount

#ITEM IDS SERVE NO PURPOSE!

#unique items:

    #rope is unique item used to travel down and up on the z axis below 0
rope = item(109,"rope",120,False,False,0,"")
all_game_items.append(rope)
    #tent allows player to use "camp" command to heal fully, late game item.
tent = item(108,"tent",200,False,False,8,"")
all_game_items.append(tent)
    #torch changes description text in dark enviroments, need to implement encounter rate change at night and in dark areas
torch = item(110,"torch",80,False,False,0,"")
all_game_items.append(torch)

#########################################

#edible poisonous items
apple = item(100,"apple",5,True,True,1000,"")
all_game_items.append(apple)
rotten_food = item(100,"rotten food",5,True,True,100,"")
all_game_items.append(rotten_food)

#edible healing items
pear = item(101,"pear",20,True,False,10,"")
all_game_items.append(pear)
cabbage = item(101,"cabbage",2,True,False,10,"")
all_game_items.append(cabbage)
turnip = item(101,"turnip",5,True,False,10,"")
all_game_items.append(turnip)
banana = item(101,"banana",5,True,False,10,"")
all_game_items.append(banana)
pineapple = item(101,"pineapple",5,True,False,10,"")
all_game_items.append(pineapple)
mushroom = item(101,"mushroom",5,True,True,10,"")
all_game_items.append(mushroom)
magic_mushroom = item(101,"magic mushroom",5,True,False,10,"")
all_game_items.append(magic_mushroom)

mushroom_tea = item(108,"cup of mushroom tea",2,True,False,8,"")
all_game_items.append(mushroom_tea)
mushroom_brew = item(108,"mushroom brew",2,True,False,8250,"")
all_game_items.append(mushroom_brew)
cup = item(104,"cup",12,False,False,0,"")
all_game_items.append(cup)
mug = item(104,"mug",12,False,False,0,"")
all_game_items.append(mug)
tea_bag = item(107,"tea bag",1,False,False,0,"")
all_game_items.append(tea_bag)
cup_of_tea = item(108,"cup of tea",2,True,False,800,"")
all_game_items.append(cup_of_tea)
hp_potion = item(111,"hp potion",20,True,False,1000,"")
all_game_items.append(hp_potion)
super_hp_potion = item(111,"super hp potion",20,True,False,10000,"")
all_game_items.append(super_hp_potion)

#fish
fish_salmon = item(111,"salmon",20,True,False,10,"")
all_game_items.append(fish_salmon)
fish_trout = item(111,"trout",20,True,False,10,"")
all_game_items.append(fish_trout)
fish_herring = item(111,"herring",20,True,False,100,"")
all_game_items.append(fish_herring)
fish_baron_maryan = item(111,"baron maryan",20,True,False,1000,"")
all_game_items.append(fish_baron_maryan)

#??? items:
fire_orb = item(106,"fire orb",7,False,False,0,"")
all_game_items.append(fire_orb)
water_orb = item(106,"water orb",7,False,False,0,"")
all_game_items.append(water_orb)
earth_orb = item(106,"earth orb",7,False,False,0,"")
all_game_items.append(earth_orb)
air_orb = item(106,"air orb",7,False,False,0,"")
all_game_items.append(air_orb)

bones = item(112,"bones",2,False,False,0,"")
all_game_items.append(bones)
worms = item(102,"worms",500,False,False,0,"")
all_game_items.append(worms)

#key items:
beak_polish = item(103,"beak polish",10,False,False,0,"")
all_game_items.append(beak_polish)
pendant = item(105,"pendant",80,False,False,0,"")
all_game_items.append(pendant)
legion_seal = item(106,"legion seal",7,False,False,0,"")
all_game_items.append(legion_seal)
oak_key = item(106,"oak key",7,False,False,0,"")
all_game_items.append(oak_key)
jail_key = item(106,"jail key",7,False,False,0,"")
all_game_items.append(jail_key)
certificate_of_passage = item(106,"certificate of passage",100,False,False,0,"")
all_game_items.append(certificate_of_passage)

class ground_item(item):
    pass

#unique ground_items:

    #rope is unique item used to travel down and up on the z axis below 0
ground_rope = ground_item(109,"rope",120,False,False,0,"")
all_ground_game_items.append(ground_rope)
    #tent allows player to use "camp" command to heal fully, late game ground_item.
ground_tent = ground_item(108,"tent",200,True,False,8,"")
all_ground_game_items.append(ground_tent)
    #torch changes description text in dark enviroments, need to implement encounter rate change at night and in dark areas
ground_torch = ground_item(110,"torch",80,False,False,0,"")
all_ground_game_items.append(ground_torch)

#########################################

#edible poisonous ground_items
ground_apple = ground_item(100,"apple",5,True,True,1000,"")
all_ground_game_items.append(ground_apple)
ground_rotten_food = ground_item(100,"rotten food",5,True,True,100,"")
all_ground_game_items.append(ground_rotten_food)

#edible healing ground_items
ground_pear = ground_item(101,"pear",20,True,False,10,"")
all_ground_game_items.append(ground_pear)
ground_cabbage = ground_item(101,"cabbage",2,True,False,10,"")
all_ground_game_items.append(ground_cabbage)
ground_turnip = ground_item(101,"turnip",5,True,False,10,"")
all_ground_game_items.append(ground_turnip)
ground_banana = ground_item(101,"banana",5,True,False,10,"")
all_ground_game_items.append(ground_banana)
ground_pineapple = ground_item(101,"pineapple",5,True,False,10,"")
all_ground_game_items.append(ground_pineapple)
ground_mushroom = ground_item(101,"mushroom",5,True,True,10,"")
all_ground_game_items.append(ground_mushroom)
ground_magic_mushroom = ground_item(101,"magic mushroom",5,True,False,10,"")
all_ground_game_items.append(ground_magic_mushroom)

ground_mushroom_tea = ground_item(108,"cup of mushroom tea",2,True,False,8,"")
all_ground_game_items.append(ground_mushroom_tea)
ground_mushroom_brew = ground_item(108,"mushroom brew",2,True,False,8250,"")
all_ground_game_items.append(ground_mushroom_brew)
ground_cup = ground_item(104,"cup",12,False,False,0,"")
all_ground_game_items.append(ground_cup)
ground_mug = ground_item(104,"mug",12,False,False,0,"")
all_ground_game_items.append(ground_mug)
ground_tea_bag = ground_item(107,"tea bag",1,False,False,0,"")
all_ground_game_items.append(ground_tea_bag)
ground_cup_of_tea = ground_item(108,"cup of tea",2,True,False,800,"")
all_ground_game_items.append(ground_cup_of_tea)
ground_hp_potion = ground_item(111,"hp potion",20,True,False,1000,"")
all_ground_game_items.append(ground_hp_potion)
ground_super_hp_potion = ground_item(111,"super hp potion",20,True,False,10000,"")
all_ground_game_items.append(ground_super_hp_potion)

#fish
ground_fish_salmon = ground_item(111,"salmon",20,True,False,10,"")
all_ground_game_items.append(ground_fish_salmon)
ground_fish_trout = ground_item(111,"trout",20,True,False,10,"")
all_ground_game_items.append(ground_fish_trout)
ground_fish_herring = ground_item(111,"herring",20,True,False,100,"")
all_ground_game_items.append(ground_fish_herring)
ground_fish_baron_maryan = ground_item(111,"baron maryan",20,True,False,1000,"")
all_ground_game_items.append(ground_fish_baron_maryan)

#??? ground_items:
ground_fire_orb = ground_item(106,"fire orb",7,False,False,0,"")
all_ground_game_items.append(ground_fire_orb)
ground_water_orb = ground_item(106,"water orb",7,False,False,0,"")
all_ground_game_items.append(ground_water_orb)
ground_earth_orb = ground_item(106,"earth orb",7,False,False,0,"")
all_ground_game_items.append(ground_earth_orb)
ground_air_orb = ground_item(106,"air orb",7,False,False,0,"")
all_ground_game_items.append(ground_air_orb)

ground_bones = ground_item(112,"bones",2,False,False,0,"")
all_ground_game_items.append(ground_bones)
ground_worms = ground_item(102,"worms",500,False,False,0,"")
all_ground_game_items.append(ground_worms)

#key ground_items:
ground_beak_polish = ground_item(103,"beak polish",10,False,False,0,"")
all_ground_game_items.append(ground_beak_polish)
ground_pendant = ground_item(105,"pendant",80,False,False,0,"")
all_ground_game_items.append(ground_pendant)
ground_legion_seal = ground_item(106,"legion seal",7,False,False,0,"")
all_ground_game_items.append(ground_legion_seal)
ground_oak_key = ground_item(106,"oak key",7,False,False,0,"")
all_ground_game_items.append(ground_oak_key)
ground_jail_key = ground_item(106,"jail key",7,False,False,0,"")
all_ground_game_items.append(ground_jail_key)
ground_certificate_of_passage = ground_item(106,"certificate of passage",100,False,False,0,"")
all_ground_game_items.append(ground_certificate_of_passage)
