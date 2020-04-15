import random
from time import sleep
from colorama import init
from colorama import Fore, Back, Style
import pygame

pygame.init()
init(autoreset=True)

from item_module import *
from equipment_module import *
from spell_module import *

all_game_enemies = []

spr_no_sprite = pygame.image.load("no_sprite1.png")

spr_goblin = pygame.image.load("goblin1.png")
spr_goblin2 = pygame.image.load("goblin2.png")
spr_ghost = pygame.image.load("ghost1.png")
spr_imp = pygame.image.load("imp1.png")
spr_imp2 = pygame.image.load("imp2.png")
spr_wolf = pygame.image.load("wolf1.png")
spr_ice_wolf = pygame.image.load("ice_wolf1.png")

spr_cow = pygame.image.load("cow1.png")
spr_sheep = pygame.image.load("sheep1.png")

spr_fire_ele = pygame.image.load("fire_ele1.png")
spr_air_ele = pygame.image.load("air_ele1.png")
spr_water_ele = pygame.image.load("water_ele1.png")
spr_earth_ele = pygame.image.load("earth_ele1.png")


class enemy_stats:
    def __init__(self, name, level, xp, hp, maxhp, mp, maxmp, magic, strength, attack, gp, attribute, weakness, spellbook, drop_table_items, drop_table_weapons, drop_table_armor, drop_table_helmets, drop_table_shields, status_effect, sprite_variable):
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
        self.weakness = weakness
        self.spellbook = spellbook
        self.drop_table_items = drop_table_items
        self.drop_table_weapons = drop_table_weapons
        self.drop_table_armor = drop_table_armor
        self.drop_table_helmets = drop_table_helmets
        self.drop_table_shields = drop_table_shields

        self.drop_table_items_always = []
        self.drop_table_weapons_always = []
        self.drop_table_armor_always = []
        self.drop_table_helmets_always = []
        self.drop_table_shields_always = []

        self.status_effect = status_effect
        self.sprite_variable = sprite_variable
        self.enemy_sprite = spr_no_sprite
        self.status_effect_list = []

        self.print_name = (Fore.RED + Style.DIM + self.name + Style.RESET_ALL)

        if self.attribute == "fire":
            self.print_attribute = (Fore.RED + Style.NORMAL + attribute + Style.RESET_ALL)
        if self.attribute == "water":
            self.print_attribute = (Fore.BLUE + Style.BRIGHT + attribute + Style.RESET_ALL)
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
            self.print_attribute = (Fore.CYAN + Style.BRIGHT + attribute + Style.RESET_ALL)

        if sprite_variable == "imp":
            self.enemy_sprite = spr_imp
        if sprite_variable == "imp2":
            self.enemy_sprite = spr_imp2
        if sprite_variable == "goblin":
            self.enemy_sprite = spr_goblin
        if sprite_variable == "goblin2":
            self.enemy_sprite = spr_goblin2
        if sprite_variable == "ghost":
            self.enemy_sprite = spr_ghost
        if sprite_variable == "cow":
            self.enemy_sprite = spr_cow
        if sprite_variable == "sheep":
            self.enemy_sprite = spr_sheep
        if sprite_variable == "fire_ele":
            self.enemy_sprite = spr_fire_ele
        if sprite_variable == "air_ele":
            self.enemy_sprite = spr_air_ele
        if sprite_variable == "water_ele":
            self.enemy_sprite = spr_water_ele
        if sprite_variable == "earth_ele":
            self.enemy_sprite = spr_earth_ele
        if sprite_variable == "wolf":
            self.enemy_sprite = spr_wolf
        if sprite_variable == "ice_wolf":
            self.enemy_sprite = spr_ice_wolf


        all_game_enemies.append(self)

# Attributes: name, level, xp, hp, maxhp, mp, maxmp, magic, strength, attack, gp, attribute, weakness,
# Lists: spellbook, drop_table_items, drop_table_weapons, drop_table_armor, drop_table_helmets, drop_table_shields,
# Status: status_effect

imp = enemy_stats("imp",2,2,400,400,100,100,1,16,16,100,"fire","holy",[],[bones],[staff_of_fire,staff_of_ice],[],[],[],0,"imp")
goon = enemy_stats("goon",2,3,300,300,100,100,1,16,14,100,"earth","fire",[],[bones],[iron_sword],[],[],[],0,"imp2")

wolf = enemy_stats("mangy wolf",2,4,150,150,100,100,1,17,16,100,"earth","water",[],[meat,bones],[],[],[],[],0,"wolf")
ice_wolf = enemy_stats("ice wolf",2,4,200,200,100,100,1,17,16,100,"ice","fire",[],[meat,bones],[wooden_staff],[],[],[],0,"ice_wolf")

goblin = enemy_stats("goblin",2,5,80,80,100,100,11,12,10,100,"earth","fire",[],[bones],[wooden_staff,tall_staff,staff_of_earth,iron_axe],[],[],[],0,"goblin")
hobgoblin = enemy_stats("hobgoblin",4,12,100,100,100,100,8,10,5,300,"earth","fire",[],[bones],[wooden_staff,iron_knife,staff_of_earth,short_dagger],[],[],[],0,"goblin2")
hobgoblin_berzerker = enemy_stats("hobgoblin berzerker",9,22,1000,1000,100,100,1,12,10,300,"earth","fire",[],[bones],[wooden_staff,tall_staff,staff_of_earth,iron_dagger],[],[],[],0,"goblin2")

bandit = enemy_stats("bandit",5,10,2000,2000,1000,1000,1,12,6,100,"fire","earth",[],[bones],[iron_sword,iron_dagger],[],[],[],0,"")
bandit_warlock = enemy_stats("bandit warlock",8,28,2000,2000,5000,5000,18,5,2,70,"fire","earth",[],[bones],[tall_staff],[],[],[],0,"")
bandit_henchman = enemy_stats("bandit henchman",12,50,2000,2000,2200,2200,10,12,4,230,"fire","earth",[],[bones],[steel_sword,steel_axe],[],[],[],0,"")

legion_soldier = enemy_stats("legion soldier",28,500,10000,10000,100,100,10,14,20,1000,"air","earth",[],[bones],[],[],[],[],0,"")
legion_spearman = enemy_stats("legion spearman",25,500,10500,10500,100,100,10,16,10,1050,"air","earth",[],[bones],[],[],[],[],0,"")
legion_archer = enemy_stats("legion archer",23,500,8700,8700,100,100,10,11,22,654,"air","earth",[],[bones],[],[],[],[],0,"")
legion_battle_mage = enemy_stats("legion battle mage",29,500,12400,12400,1000,1000,45,5,6,2245,"air","earth",[],[bones],[],[],[],[],0,"")

elf_warrior = enemy_stats("elf warrior",32,100,15000,15000,2000,2000,10,20,22,100,"earth","fire",[],[bones],[],[],[],[],0,"")
elf_mage = enemy_stats("elf mage",35,500,18400,18400,10000,10000,65,5,6,3245,"earth","fire",[],[bones],[],[],[],[],0,"")
elf_thief = enemy_stats("elf thief",38,500,18800,18800,1000,1000,5,50,60,3245,"earth","fire",[],[bones],[],[],[],[],0,"")

mossy_giant = enemy_stats("mossy giant",40,5000,22400,22400,10000,10000,65,80,10,3245,"earth","fire",[],[bones],[],[],[],[],0,"")

giant_wasp = enemy_stats("giant wasp",42,500,12800,12800,1000,1000,5,50,60,3245,"earth","fire",[],[bones],[],[],[],[],0,"")
fire_demon = enemy_stats("fire demon",45,500,14800,14800,1000,1000,50,50,60,3245,"fire","water",[],[bones],[],[],[],[],0,"")

elf_ranger = enemy_stats("elf ranger",50,500,18800,18800,1000,1000,50,52,63,3245,"earth","fire",[],[bones],[],[],[],[],0,"")
elf_necromancer = enemy_stats("elf necromancer",48,500,16200,16200,1000,1000,60,22,33,3245,"earth","holy",[],[bones],[],[],[],[],0,"")

ice_golem = enemy_stats("ice golem",64,800,11230,11230,100,100,0,52,22,2230,"ice","fire",[],[],[],[],[],[],0,"")
rock_golem = enemy_stats("rock golem",62,800,10520,10520,100,100,0,55,18,20230,"earth","water",[],[],[],[],[],[],0,"")
mushroom_man = enemy_stats("mushroom man",67,800,10230,10230,100,100,0,50,20,10230,"earth","fire",[],[],[],[],[],[],0,"")
magical_mushroom_man = enemy_stats("magic mushroom man",62,800,10230,10230,100,100,45,20,20,10230,"earth","fire",[],[],[],[],[],[],0,"")

bird_warrior = enemy_stats("bird warrior",191,100000,2408070,2408070,1000000,1000000,100,300,220,1000,"air","water",[],[bones],[],[],[],[],0,"")#leg

fire_elemental = enemy_stats("fire elemental",8,200,3200,3200,1000,1000,18,5,2,100,"fire","water",[],[],[],[],[],[],0,"fire_ele")
water_elemental = enemy_stats("water elemental",8,200,3800,3800,1000,1000,18,5,2,100,"water","earth",[],[],[],[],[],[],0,"water_ele")
earth_elemental = enemy_stats("earth elemental",8,100,3200,3200,1000,1000,13,5,2,100,"earth","water",[],[],[],[],[],[],0,"earth_ele")
air_elemental = enemy_stats("air elemental",8,100,3000,3000,1000,1000,13,5,2,100,"air","earth",[],[],[],[],[],[],0,"air_ele")

giant_snail = enemy_stats("giant snail",14,10,9300,9300,100,100,0,12,2,930,"earth","earth",[],[],[],[],[],[],0,"")
giant_spider = enemy_stats("giant spider",33,64,23000,23000,100,100,0,50,2,2300,"earth","fire",[],[],[],[],[],[],0,"")
giant_moth = enemy_stats("giant moth",18,5,13400,13400,100,100,0,10,20,100,"earth","air",[],[],[],[],[],[],0,"")

big_slug = enemy_stats("big slug",100,500,1035000,1035000,100,100,0,0,0,0,"slime","salt",[],[],[],[],[],[],0,"")#legendary

skeleton_mage = enemy_stats("skeleton mage",101,4202,60070,60070,100,100,53,30,22,100,"undead","holy",[],[bones],[],[],[],[],0,"")
skeleton_warrior = enemy_stats("skeleton warrior",101,50922,92070,92070,100,100,0,63,42,100,"undead","holy",[],[bones],[],[],[],[],0,"")

## npc enemies
cow = enemy_stats("cow",2,2,200,200,100,100,1,8,7,100,"fire","holy",[],[meat,bones],[],[],[],[],0,"cow")
sheep = enemy_stats("sheep",2,2,100,100,100,100,1,6,5,100,"fire","holy",[],[meat,bones],[],[],[],[],0,"sheep")
town_guard = enemy_stats("town guard",20,20,8000,8000,100,100,1,60,40,100,"holy","fire",[],[bones],[],[],[],[],0,"")
