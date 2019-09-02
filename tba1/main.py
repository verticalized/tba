import random
from time import sleep
from colorama import init
from colorama import Fore, Back, Style

init(autoreset=True)

###########################################

from scene_module import *
from npc_module import *

from item_module import *
from equipment_module import *
from spell_module import *

from enemy_module import *

###########################----GLOBAL_VARIABLES-----####################

version = "1.8.2.1"

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

recipe_found = False


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

# place npcs in the world

dismurth_square.npc_list.append(npc_jenkins)
dismurth_market.npc_list.append(npc_john_doe)
dismurth_market.npc_list.append(npc_jane_doe)
dismurth_tower_1f.npc_list.append(npc_wizard_traenus)
dismurth_tower_gf.npc_list.append(npc_wizard_marbles)
dismurth_smith.npc_list.append(npc_dismurth_smith)

################################

# give npc dialouge options

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

#######################--SHOP INVENTORIES--############################

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

bandit.spellbook.append(prayer)

bandit_warlock.spellbook.append(snare)
bandit_warlock.spellbook.append(prayer)
bandit_warlock.spellbook.append(earthblast)
bandit_warlock.spellbook.append(earthblast)
bandit_warlock.spellbook.append(necroblast)

bandit_henchman.spellbook.append(burn)
bandit_henchman.spellbook.append(fireblast)
bandit_henchman.spellbook.append(prayer)


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

####################-NPC COMBAT ENCOUNTERS--#########################

npc_jenkins.combat_enemy_list.append(hobgoblin)

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

inventory.append(pear)
inventory.append(mushroom)
inventory.append(cup_of_tea)
inventory.append(magic_mushroom)
inventory.append(cup)
inventory.append(cup)
inventory.append(tea_bag)
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

##############################--SHOP INVENTORY FUNCTIONS--##############################

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

#############################----COMBAT FUNCTIONS----#########################

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
                            current_enemies.append(bandit_warlock)
                        if combat_rating >= 25 and combat_rating < 50:
                            current_enemies.append(bandit)
                        if combat_rating >= 50 and combat_rating < 75:
                            current_enemies.append(bandit_warlock)
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
                            current_enemies.append(bandit_henchman)
                        if combat_rating >= 25 and combat_rating < 50:
                            current_enemies.append(goblin)
                            current_enemies.append(hobgoblin)
                            current_enemies.append(air_elemental)
                        if combat_rating >= 50 and combat_rating < 75:
                            current_enemies.append(bandit)
                            current_enemies.append(bandit_warlock)
                            current_enemies.append(bandit_henchman)
                        if combat_rating >= 75 and combat_rating <= 100:
                            current_enemies.append(rock_golem)

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

                if scene_type.difficulty != 0:
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
                            current_enemies.append(bandit_henchman)

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
                            current_enemies.append(bandit_warlock)
                            current_enemies.append(fire_elemental)
                        if combat_rating >= 75 and combat_rating <= 100:
                            current_enemies.append(rock_golem)

                    if combat_mod >= 75 and combat_mod < 90:
                        if combat_rating >= 0 and combat_rating < 25:
                            current_enemies.append(legion_soldier)
                        if combat_rating >= 25 and combat_rating < 50:
                            current_enemies.append(legion_spearman)
                        if combat_rating >= 50 and combat_rating < 75:
                            current_enemies.append(legion_battle_mage)
                            current_enemies.append(legion_soldier)
                        if combat_rating >= 75 and combat_rating <= 100:
                            current_enemies.append(mushroom_man)


                    if combat_mod >= 90 and combat_mod <= 100:
                        if combat_rating >= 0 and combat_rating < 25:
                            current_enemies.append(legion_archer)
                            current_enemies.append(legion_spearman)
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
        target = "0"
        for enemy_stats in current_enemies:
            print("|| " + str((current_enemies.index(enemy_stats)+1)) + " || LVL: " + str(enemy_stats.level) + " || " + enemy_stats.name + " || ATR: " + enemy_stats.print_attribute)
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
            break

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
    func_player_melee()

def func_player_status_check_spell():
    func_player_spell()

def func_enemy_status_check():
    for enemy_stats in current_enemies:
        func_enemy_attack(enemy_stats)

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

###########################---PLAYER STATS/SKILLS/INVENTORY----############################

def func_cook():
    target_gear = "0"
    ingredient = "0"
    for item in inventory:
        print("|| " + str((inventory.index(item)+1)) + " || " + item.print_name + " || " + str(item.value) + " gp. ")

    dropped_item = input("\nwhat do you want to cook with?\n")
    has_item = False
    if dropped_item.isdigit():
        val_dropped_item = int(dropped_item)
        val_drop = val_dropped_item - 1
        for item in inventory:
            if val_drop == inventory.index(item):
                target_gear = item.name
    else:
        for item in inventory:
            if item.name == dropped_item:
                target_gear = item.name

    for item in inventory:
        if target_gear == item.name:
            has_item = True
            print("you selected " + item.print_name + "\n")
            ingredient = target_gear
            break
    return ingredient

def func_create_item(ing1_name,ing2_name,ingreq_1,ingreq_2,skill_lvl_req,made_item):
    global recipe_found
    if ing1_name == ingreq_1.name and ing2_name == ingreq_2.name:
        recipe_found == True
        if player1_skills.cooking >= skill_lvl_req:
            has_cooked = True
            for item in all_game_items:
                if item.name == made_item.name:
                    inventory.append(item)
                    print("you made " + item.name)
                    for item in inventory:
                        if item.name == ing1_name:
                            inventory.remove(item)
                    for item in inventory:
                        if item.name == ing2_name:
                            inventory.remove(item)
        else:
            print("your cooking level is not high enough to make that!")
            has_cooked = False

    elif ing2_name == ingreq_1.name and ing1_name == ingreq_2.name:
        recipe_found == True
        if player1_skills.cooking >= skill_lvl_req:
            has_cooked = True
            for item in all_game_items:
                if item.name == made_item.name:
                    inventory.append(item)
                    print("you made " + item.name)
                    for item in inventory:
                        if item.name == ing1_name:
                            inventory.remove(item)
                    for item in inventory:
                        if item.name == ing2_name:
                            inventory.remove(item)
        else:
            print("your cooking level is not high enough to make that!")
            has_cooked = False


    else:
        has_cooked = False

def func_equip(gear,player_gear_inv,current_gear):
    target_gear = "0"
    has_level = False
    has_space = False
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

            if player1.level < gear.level:
                print("\nYou are not high enough level to equip " + gear.print_name + "\n")
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

                if gear in all_game_weapons:
                    del equiped_weapon[:]
                if gear in all_game_armor:
                    del equiped_armor[:]
                if gear in all_game_helmets:
                    del equiped_helmet[:]
                if gear in all_game_shields:
                    del equiped_shield[:]

                if gear in all_game_weapons:
                    equiped_weapon.append(gear)
                if gear in all_game_armor:
                    equiped_armor.append(gear)
                if gear in all_game_helmets:
                    equiped_helmet.append(gear)
                if gear in all_game_shields:
                    equiped_shield.append(gear)
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

#######################---PLAYER LOCATION---#######################

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
                    enemy_stats.maxhp += (random.randint(0,50) * enemy_stats.level)
                    enemy_stats.hp = (0 + enemy_stats.maxhp)
                    enemy_stats.gp += ((random.randint(0,10) * enemy_stats.maxhp) // 1000) * enemy_stats.level
                player_turns = 10
                print("\n//////////// YOU ARE NOW IN COMBAT //////////// \n")
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

###############################################

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

################################################

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

#################----DIALOGUE----###############

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
################################################

    elif player_input == "make":
        ing_1 = "0"
        ing_2 = "0"
        ing_1_index = 0
        ing_2_index = 0
        has_cooked = False
        for scene_type in location:
            if player1_skills.crafting != 0:

                ing_1 = func_cook() # func_cook returns the name of the item the player selects as string
                for item in inventory:
                    if item.name == ing_1:
                        ing_1_index = inventory.index(item)
                        inventory.remove(item)
                        break

                ing_2 = func_cook()
                for item in inventory:
                    if item.name == ing_2:
                        ing_2_index = inventory.index(item)
                        inventory.remove(item)
                        break

                if ing_1 != ing_2:
                    while recipe_found == False:
                        #iterates thorugh all recipes untill it finds a match for both ingredients
                        #breaks when it minds a match prints lvl status and item created
                        func_create_item(ing_1,ing_2,cup,mushroom,1,mushroom_tea)
                        if recipe_found == True:
                            break
                        func_create_item(ing_1,ing_2,mug,mushroom,1,mushroom_tea)
                        if recipe_found == True:
                            break
                        func_create_item(ing_1,ing_2,cup,tea_bag,1,cup_of_tea)
                        if recipe_found == True:
                            break
                        func_create_item(ing_1,ing_2,cup,magic_mushroom,1,mushroom_tea)
                        if recipe_found == True:
                            break
                        func_create_item(ing_1,ing_2,mug,magic_mushroom,1,mushroom_tea)
                        if recipe_found == True:
                            break
                        func_create_item(ing_1,ing_2,mushroom_tea,mushroom,1,mushroom_brew)
                        if recipe_found == True:
                            break
                        func_create_item(ing_1,ing_2,mushroom_tea,magic_mushroom,1,mushroom_brew)
                        if recipe_found == True:
                            break
                        #break loop if no match is found
                        break
                    if has_cooked == False:
                        if ing_2_index > ing_1_index:
                            ing_2_index += 1
                        if ing_1_index > ing_2_index:
                            ing_1_index += 1
                        print("nothing interesting happens...\n")
                        for item in all_game_items:
                            if item.name == ing_1:
                                inventory.insert(ing_1_index,item)
                            if item.name == ing_2:
                                inventory.insert(ing_2_index,item)


################################################

    elif player_input == "quit":
        game_start = 0

################################################


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
