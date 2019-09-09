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

        all_game_items.append(self)

#ITEM IDS SERVE NO PURPOSE!

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

mushroom = item(101,"mushroom",5,True,True,10,"")
magic_mushroom = item(101,"magic mushroom",5,True,False,10,"")
mushroom_tea = item(108,"cup of mushroom tea",2,True,False,8,"")
mushroom_brew = item(108,"mushroom brew",2,True,False,8250,"")

cup_of_tea = item(108,"cup of tea",2,True,False,800,"")
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
mug = item(104,"mug",12,False,False,0,"")
worms = item(102,"worms",500,False,False,0,"")
tea_bag = item(107,"tea bag",1,False,False,0,"")

class ground_item:
    def __init__(self, name):
        self.name = name
        self.print_name = (Fore.BLACK + Style.BRIGHT + self.name + Style.RESET_ALL)
        self.item_amount = 1
        self.item_weight = 1
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
ground_mushroom_brew = ground_item("mushroom brew")
ground_mug = ground_item("mug")
ground_magic_mushroom = ground_item("magic mushroom")


ground_oak_key = ground_item("oak key")
ground_jail_key = ground_item("jail key")
ground_certificate_of_passage = ground_item("certificate of passage")
