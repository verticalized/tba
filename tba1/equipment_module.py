import random
from time import sleep
from colorama import init
from colorama import Fore, Back, Style

init(autoreset=True)

all_game_weapons = []
all_ground_game_weapons = []
all_game_armor = []
all_ground_game_armor = []
all_game_helmets = []
all_ground_game_helmets = []
all_game_shields = []
all_ground_game_shields = []

#ITEM IDS SERVE NO PURPOSE!

class weapon:
    def __init__(self, id, name, value, type, level, attribute, magic_bonus, strength_bonus, attack_bonus, defence_bonus, maxhp_bonus):
        self.id = id
        self.name = name

        self.value = value
        self.type = type
        self.level = level
        self.attribute = attribute
        self.magic_bonus = magic_bonus
        self.strength_bonus = strength_bonus
        self.attack_bonus = attack_bonus
        self.defence_bonus = defence_bonus
        self.maxhp_bonus = maxhp_bonus
        self.print_attribute = ""

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

        self.print_name = (Fore.BLACK + Style.BRIGHT + name + Style.RESET_ALL)

        all_game_weapons.append(self)

bird_sword = weapon(201,"bird sword",3,"sword",5,"air",5,9,15,12,10)
super_bird_sword = weapon(202,"super bird sword",180,"sword",50,"air",0,500,500,500,0)

wooden_staff = weapon(204,"wooden staff",80,"staff",5,"earth",20,2,2,20,0)
tall_staff = weapon(204,"tall staff",80,"staff",5,"earth",22,4,4,25,0)
iron_knife = weapon(203,"iron knife",1,"sword",2,"earth",0,8,8,1,1)
iron_spear = weapon(203,"iron spear",2,"spear",2,"earth",0,14,2,12,1)
iron_dagger = weapon(203,"iron dagger",2,"dagger",2,"earth",0,8,18,2,1)
steel_spear = weapon(204,"steel spear",80,"spear",10,"earth",0,18,24,28,0)

iron_sword = weapon(203,"iron sword",2,"sword",2,"earth",0,10,10,10,1)
steel_sword = weapon(204,"steel sword",80,"sword",10,"earth",0,20,20,20,0)
mithril_sword = weapon(204,"mithril sword",80,"sword",15,"water",0,30,30,30,0)
adamantite_sword = weapon(204,"adamantite sword",80,"sword",20,"earth",0,40,40,40,0)
rune_sword = weapon(204,"rune sword",80,"sword",25,"holy",0,50,50,50,0)

iron_axe = weapon(205,"iron axe",8,"axe",5,"earth",0,10,10,10,0)
steel_axe = weapon(206,"steel axe",80,"axe",10,"earth",0,20,20,20,0)
mithril_axe = weapon(206,"mithril axe",80,"axe",15,"water",0,30,30,30,0)
adamantite_axe = weapon(206,"adamantite axe",80,"axe",20,"earth",0,40,40,40,0)
rune_axe = weapon(206,"rune axe",80,"axe",25,"holy",0,50,50,50,0)

greatsword = weapon(207,"greatsword",800,"large sword",32,"water",0,40,40,40,0)
ultra_greatsword = weapon(208,"ultra greatsword",8000,"large sword",54,"water",0,60,60,60,0)
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


ground_wooden_staff = ground_weapon("wooden staff")
ground_tall_staff = ground_weapon("tall staff")
ground_iron_knife = ground_weapon("iron knife")
ground_iron_spear = ground_weapon("iron spear")
ground_iron_dagger = ground_weapon("iron dagger")
ground_steel_spear = ground_weapon("steel spear")

ground_iron_sword = ground_weapon("iron sword")
ground_steel_sword = ground_weapon("steel sword")
ground_iron_axe = ground_weapon("iron axe")
ground_steel_axe = ground_weapon("steel axe")

ground_greatsword = ground_weapon("greatsword")
ground_ultra_greatsword = ground_weapon("ultra greatsword")
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
iron_square_shield = shield(301,"iron square shield",100,"heavy",9,"air",1,2,2,10,200)
steel_square_shield = shield(301,"steel square shield",100,"heavy",18,"air",1,4,2,20,500)
mage_book = shield(301,"mage book",100,"light",99,"air",100,0,0,40,1000)

wooden_round_shield = shield(301,"wooden round shield",100,"light",1,"air",0,0,0,40,100)
magic_orb = shield(301,"magic orb",100,"light",1,"air",30,0,0,0,0)

class ground_shield:
    def __init__(self, name):
        self.name = name
        self.print_name = (Fore.BLACK + Style.BRIGHT + self.name + Style.RESET_ALL)

        all_ground_game_shields.append(self)

ground_bird_shield = ground_shield("bird shield")
ground_iron_square_shield = ground_shield("iron square shield")
ground_steel_square_shield = ground_shield("steel square shield")
ground_mage_book = ground_shield("mage book")

ground_wooden_round_shield = ground_shield("wooden round shield")
ground_magic_orb = ground_shield("magic orb")
