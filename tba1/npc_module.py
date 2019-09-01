import random
from time import sleep
from colorama import init
from colorama import Fore, Back, Style

init(autoreset=True)

all_npcs = []

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
