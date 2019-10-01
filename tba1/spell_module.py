import random
from time import sleep
from colorama import init
from colorama import Fore, Back, Style

init(autoreset=True)

all_game_spells = []
all_game_status_conditions = []

class spell:
    def __init__(self, name, level, mp_cost, value, utility, damage, attribute, xp, effect, spell_desc):
        self.name = name
        self.level = level
        self.mp_cost = mp_cost
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

        all_game_spells.append(self)

############--COMBAT SPELLS--#############

#### status 0 spells DAMAGE - combat spells, also used for turns where enemy does nothing by doing 0 damage.
slime = spell("slime",5,5,5,True,0,"slime",0,0,"slurms mackenzie")

#low level damage spells
fire_bolt = spell("fire bolt",4,25,50,False,80,"fire",100,0,"fire damage")
ice_bolt = spell("ice bolt",4,25,50,False,80,"ice",100,0,"ice damage")

# arrow spells
fire_arrow = spell("fire arrow",18,50,500,False,80,"fire",100,0,"fire damage")
ice_arrow = spell("ice arrow",18,50,500,False,80,"ice",100,0,"ice damage")

# tier 1 damage spells
fireball = spell("fireball",30,75,5,False,1000,"fire",200,0,"heavy fire damage")
hydro_barrage = spell("hydro barrage",30,75,1000,False,100,"water",200,0,"heavy water damage")
holy_surge = spell("holy surge",30,75,1000,False,100,"holy",200,0,"heavy holy damage")
necro_surge = spell("necro surge",30,75,1000,False,100,"undead",200,0,"heavy undead damage")

# tier 2 damage spells
hydroblast = spell("hydroblast",8,25,250,False,60,"water",100,0,"light water damage")
fireblast = spell("fireblast",8,25,250,False,60,"fire",100,0,"light fire damage")
windblast = spell("windblast",8,25,250,False,60,"air",100,0,"light air damage")
earthblast = spell("earthblast",8,25,250,False,60,"earth",100,0,"light earth damage")
necroblast = spell("necroblast",8,25,250,False,60,"undead",100,0,"light undead damage")
holyblast = spell("holyblast",8,25,250,False,60,"holy",100,0,"light holy damage")

#### status -1 spells HEAL AND DAMAGE
life_drain = spell("life drain",5,5,5,True,100,"undead",50,1,"a life draining spell which heals the user")

##################--STATUS EFFECT/DEBUFF SPELLS--##############################

#### status 2 spells FREEZE
snare = spell("snare",5,5,500,True,5,"ice",70,2,"snares the enemy in ice")
blizzard = spell("blizzard",5,5,500,False,150,"ice",150,2,"freezes the enemy and does lots of damage")
cone_of_cold = spell("cone of cold",5,5,500,False,50,"ice",50,2,"freezes the enemy and does damage")
#### status 3 spells POISON
poison = spell("poison",5,5,50,True,5,"earth",70,3,"poisons the enemy")

#### status 4 spells BURN
burn = spell("burn",5,5,50,True,5,"fire",70,4,"burns the enemy")
mega_burn = spell("burn",30,5,5000,False,500,"fire",70,4,"MFB")

#### status 5 spells SLEEP
hypnosis = spell("hypnosis",50,5,50,True,5,"water",70,5,"puts the enemy to sleep")

#### status 6 spells BADLY POISON
toxic = spell("toxic",22,5,500,True,5,"earth",70,6,"badly poisons the enemy")

##################--BUFF/HEALING SPELLS--##############################

#### status 100 spells HEAL
mega_heal = spell("mega heal",15,5,1000,True,250,"holy",50,100,"a mega healing spell")

super_heal = spell("super heal",5,5,500,True,100,"holy",50,100,"a super healing spell")

prayer = spell("prayer",1,50,250,True,50,"holy",50,100,"a light healing spell")

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

knocked_out = status_condition("KO'd",1,False,False,False,False,False,False,False,False,False,False,False,False,False)
