import random
from time import sleep
from colorama import init
from colorama import Fore, Back, Style

init(autoreset=True)

all_game_spells = []
all_game_status_conditions = []

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
fire_arrow = spell("fire arrow",18,5,False,80,"fire",100,0,"fire damage")
ice_arrow = spell("ice arrow",18,5,False,80,"ice",100,0,"ice damage")

# tier 1 damage spells
fireball = spell("fireball",30,5,False,1000,"fire",200,0,"heavy fire damage")
hydro_barrage = spell("hydro barrage",1000,5,False,100,"water",200,0,"heavy water damage")
holy_surge = spell("holy surge",30,1000,False,100,"holy",200,0,"heavy holy damage")
necro_surge = spell("necro surge",30,1000,False,100,"undead",200,0,"heavy undead damage")

# tier 2 damage spells
hydroblast = spell("hydroblast",8,500,False,60,"water",100,0,"light water damage")
fireblast = spell("fireblast",8,500,False,60,"fire",100,0,"light fire damage")
windblast = spell("windblast",8,500,False,60,"air",100,0,"light air damage")
earthblast = spell("earthblast",8,500,False,60,"earth",100,0,"light earth damage")
necroblast = spell("necroblast",8,500,False,60,"undead",100,0,"light undead damage")
holyblast = spell("holyblast",8,500,False,60,"holy",100,0,"light holy damage")

###########--HEALING SPELLS--##########

# status -1 spells HEAL AND DAMAGE

life_drain = spell("life drain",5,5,True,100,"undead",50,-1,"a life draining spell which heals the user")

# status 1 spells HEAL

mega_heal = spell("mega heal",15,1000,True,250,"holy",50,1,"a mega healing spell")

super_heal = spell("super heal",5,500,True,100,"holy",50,1,"a super healing spell")

prayer = spell("prayer",1,50,True,50,"holy",50,1,"a light healing spell")

##################--STATUS EFFECT SPELLS--##############################

#status 2 spells FREEZE
snare = spell("snare",5,5,True,5,"ice",70,2,"snares the enemy")

#status 3 spells POISON
poison = spell("poison",5,5,True,5,"earth",70,3,"poisons the enemy")

#status 4 spells BURN
burn = spell("burn",5,5,True,5,"fire",70,4,"burns the enemy")

##################--BUFFS/DEBUFFS--##############################

class status_condition:
    def __init__(self, name, scalar, is_freeze, is_asleep, is_poisoned, is_poisoned_bad, is_burning, is_str_up, is_atk_up, is_mgk_up, is_def_up, is_str_down, is_atk_down, is_mgk_down, is_def_down):
        self.name = name
        self.scalar = scalar
        self.is_freeze = is_freeze
        self.is_asleep = is_asleep
        self.is_poisoned = is_poisoned
        self.is_poisoned_bad = is_poisoned_bad
        self.is_burning = is_burning

        self.is_str_up = is_str_up
        self.is_atk_up = is_atk_up
        self.is_mgk_up = is_mgk_up
        self.is_def_up = is_def_up

        self.is_str_down = is_str_down
        self.is_atk_down = is_atk_down
        self.is_mgk_down = is_mgk_down
        self.is_def_down = is_def_down


        all_game_status_conditions.append(self)

frozen = status_condition("Frozen",1,True,False,False,False,False,False,False,False,False,False,False,False,False)
asleep = status_condition("Asleep",1,False,True,False,False,False,False,False,False,False,False,False,False,False)
poisoned = status_condition("Poisoned",1,False,False,True,False,False,False,False,False,False,False,False,False,False)
poisoned_bad = status_condition("Badly Poisoned",1,False,False,False,True,False,False,False,False,False,False,False,False,False)
burning = status_condition("Burning",1,False,False,False,False,True,False,False,False,False,False,False,False,False)

str_up_lvl_1 = status_condition("STR UP",1,False,False,False,False,False,True,False,False,False,False,False,False,False)
atk_up_lvl_1 = status_condition("ATK UP",1,False,False,False,False,False,False,True,False,False,False,False,False,False)
mgk_up_lvl_1 = status_condition("MGK UP",1,False,False,False,False,False,False,False,True,False,False,False,False,False)
def_up_lvl_1 = status_condition("DEF UP",1,False,False,False,False,False,False,False,False,True,False,False,False,False)

str_down_lvl_1 = status_condition("STR DOWN",1,False,False,False,False,False,False,False,False,False,True,False,False,False)
atk_down_lvl_1 = status_condition("ATK DOWN",1,False,False,False,False,False,False,False,False,False,False,True,False,False)
mgk_down_lvl_1 = status_condition("MGK DOWN",1,False,False,False,False,False,False,False,False,False,False,False,True,False)
def_down_lvl_1 = status_condition("DEF DOWN",1,False,False,False,False,False,False,False,False,False,False,False,False,True)
