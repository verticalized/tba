import random
from time import sleep
from colorama import init
from colorama import Fore, Back, Style

init(autoreset=True)

class dialouge_option:
    def __init__(self, text, is_quit, is_buy_item, is_buy_weapon, is_buy_armor, is_buy_helmet, is_buy_shield, is_buy_spell, is_sell, is_talk, is_assault, is_give, is_quest, is_heal):
        self.text = text #text displayed for dialouge option
        self.is_quit = is_quit #option to allow user to leave dialouge
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
        self.is_heal = is_heal #etc...

dialouge_buy_item = dialouge_option("buy item",False,True,False,False,False,False,False,False,False,False,False,False,False)
dialouge_buy_weapon = dialouge_option("buy weapons",False,False,True,False,False,False,False,False,False,False,False,False,False)
dialouge_buy_armor = dialouge_option("buy armor",False,False,False,True,False,False,False,False,False,False,False,False,False)
dialouge_buy_helmet = dialouge_option("buy helmets",False,False,False,False,True,False,False,False,False,False,False,False,False)
dialouge_buy_shield = dialouge_option("buy shields",False,False,False,False,False,True,False,False,False,False,False,False,False)
dialouge_buy_spell = dialouge_option("buy spells",False,False,False,False,False,False,True,False,False,False,False,False,False)

dialouge_heal = dialouge_option("ask for healing",False,False,False,False,False,False,False,False,False,False,False,False,True)

dialouge_sell = dialouge_option("can I sell",False,False,False,False,False,False,False,True,False,False,False,False,False)
dialouge_talk = dialouge_option("heard any news?",False,False,False,False,False,False,False,False,True,False,False,False,False)
dialouge_gf = dialouge_option("prepare to die!",False,False,False,False,False,False,False,False,False,True,False,False,False)
dialouge_attack = dialouge_option("attack",False,False,False,False,False,False,False,False,False,True,False,False,False)
dialouge_give = dialouge_option("give me something!",False,False,False,False,False,False,False,False,False,False,True,False,False)
dialouge_quest = dialouge_option("do you have a quest?",False,False,False,False,False,False,False,False,False,False,False,True,False)

dialouge_quit= dialouge_option("Goodbye",True,False,False,False,False,False,False,False,False,False,False,False,False)

all_npcs = []

class npc:
    def __init__(self, first_name, last_name, title, npc_desc, greeting, is_animal, race, gender, faction, attire, assault_dialouge,talk_text):
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
        self.talk_text = talk_text

        self.dialouge_options_list = []
        self.dialouge_options_list.append(dialouge_quit)
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

npc_doctor = npc("Shmurlitz","Durlitz","Doctor","Healing professional","hello",False,"human","man","0","cloth clothes","0","I am a doctor and you are talking to me")

npc_jenkins = npc("old man","jenkins","Seer","Good for a chat!","hello",False,"human","man","0","cloth clothes","*the old man transforms into a goblin*","")
npc_john_doe = npc("John","Dough","Merchant","weapons merchant...","hello",False,"human","man","0","cloth clothes","oof","")
npc_jane_doe = npc("Haney","Dunorf","Peasant","runs an item shop...","'ello",False,"human","woman","0","cloth clothes","oof","")
npc_wizard_traenus = npc("Neil","Traenus","Head Wizard","a man of magic...","hello",False,"human","man","0","blue wizard robes","oof","")
npc_wizard_marbles = npc("Marbles","the dog","canine magic specialist","a dog of magic...","woof!",True,"dog","cute","0","0","WOOF!","")
npc_dismurth_smith = npc("George","Smith","Blacksmith","good at making horseshoes...","G'day",False,"dwarf","man","dwavern guild","cloth clothes","oof","")

npc_wizard_jim = npc("Jim","Greenmichs","Wizard","appreciates a fine brew and a mix...","yo",False,"human","man","0","blue wizard robes","oof","")
npc_wizard_tilly = npc("Tilly","the dog","wizard","an apprentice wizard puppy...","woof!",True,"dog","puppy","0","cloth clothes","oof","")

npc_merchant_ollie = npc("Ollie","Zed-ecks","Travelling Merchant","an exotic trader...","G'day",False,"human","man","0","fine clothes","oof","")
npc_merchant_dech = npc("Dechen","Knee-pah","Extractor","creative concoctions are his specialty...","G'day",False,"human","man","0","fine clothes","oof","")

npc_lib = npc("Lib","","The Mad","a man of many names","G'day",False,"human","man","0","fine clothes","oof","")
npc_king = npc("Daniel","Geedorah","King","known as the crown ruler...","G'day",False,"human","man","0","royal clothes","oof","")
npc_chris_cornwell = npc("Chris","Cornwell","Farmer","has a beautiful garden...","G'day",False,"human","man","0","farmer's clothes","oof","")


npc_cow = npc("cow","","","","moo",True,"cow","large","0","0","Moo!","")
npc_sheep = npc("sheep","","","","baaaa",True,"sheep","wooley","0","0","Baa!","")

npc_town_guard = npc("Joneses","Keeneye","Town Guard","Keeps an eye on the gate...","hello",False,"human","man","0","chain mail","Prepare to die, invader!","")
