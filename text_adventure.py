import time
from termcolor import colored, cprint 

#colors
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

#Weapons
class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    #for displaying weapons
    def __repr__(self):
        desc = "({name} | Damage: {damage})".format(name=self.name, damage=self.damage)
        return desc

#Enemy
class Enemy:
    def __init__(self, name, max_health=100, damage=12):
        self.name = name
        self.health = max_health
        self.max_health = max_health
        self.damage = damage
        self.is_alive = True
    
    #for displaying enemy name
    def __repr__(self):
        desc = "My name is {name}.".format(name=self.name, health=self.health, damage=self.damage, is_alive="alive" if self.is_alive == True else "dead")
        return desc

    #for enemy respawn
    def respawn(self):
        self.is_alive = True
        if self.health == 0:
            self.health = self.max_health

    #for enemy knock out
    def knock_out(self):
        self.is_alive = False
        if self.health != 0:
            self.health = 0 
        print("You killed {name}.".format(name=self.name))

    #for enemy losing health
    def lose_health(self, amount):
        self.health -= amount
        if self.health <= 0:
            #makes sure health doesnt become negative. Knocks out enemy
            self.health = 0
            self.knock_out()
        else:
            print("{name} now has {health} health.".format(name=self.name, health=self.health))    

#Player
class Player:
    def __init__(self):
        self.name = ""
        self.health = 100
        self.max_health = 100
        self.is_alive = True

    #for displaying player name
    def __repr__(self):
        desc = "My name is {name} and i have {health} health and I am {is_alive}.".format(name=self.name, health=self.health, is_alive="alive" if self.is_alive == True else "dead")
        return desc

    #for getting player name
    def get_name(self):
        self.name += input("Enter your name: ")
        return self.name

    #for player respawn
    def respawn(self):
        self.is_alive = True
        if self.health == 0:
            self.health = self.max_health
        print("You woke up in an empty room")

    #for player knock out
    def knock_out(self):
        self.is_alive = False
        if self.health != 0:
            self.health = 0 
        print("You were knocked out.")

    #for player losing health
    def lose_health(self, amount):
        self.health -= amount
        if self.health <= 0:
            #makes sure health doesnt become negative. Knocks out player
            self.health = 0
            self.knock_out()
        else:
            print("You now have {health} health.".format(health=self.health))


#FUNCTIONS

#for displaying equipped weapon
def display_equipped_weapon(weapon):
    display_equipped_weapon = "You equipped the {name} it deals {damage} damage.".format(name=weapon.name, damage=weapon.damage)
    print(display_equipped_weapon)

#for player attacking enemy
def player_attack_enemy(enemy, weapon):
    enemy.lose_health(weapon.damage)

#for enemy attacking player
def enemy_attack_player(player, enemy):
    player.lose_health(enemy.damage)

#for attacking until knockout
def attack_until_ko(player, enemy, weapon):
    while player.is_alive == True and enemy.is_alive == True:
        if player.is_alive == True:
            print(player.name + " hit " + enemy.name + " for " + str(weapon.damage))
            player_attack_enemy(enemy, weapon)
            print(" ")
            time.sleep(4)
        
        if enemy.is_alive == True:
            print(enemy.name + " hit " + player.name + " for " + str(enemy.damage))
            enemy_attack_player(player, enemy)
            print(" ")
            time.sleep(4)

#Instantiate classes

#player class
player_one = Player()
player_one.get_name()
time.sleep(0.5)
player_one.respawn()

#Weapon Fist
weapon_fist = Weapon("Fist", 0.1)

#Room 1:1 weapons
weapon_long_sword = Weapon("Long Sword", 50)
weapon_bow = Weapon("Bow", 15)

#Room 2:1 weapons
weapon_katana = Weapon("Katana", 65)
weapon_shuriken = Weapon("Shuriken", 15)

#Room 3:1 weapons
weapon_diamond_sword = Weapon("Minecraft Diamond Sword", 700)
weapon_AK47 = Weapon("AK47", 700)

#enemy classes
enemy_bug = Enemy(color.GREEN + "Bug" + color.END, 100, 40)
enemy_virus = Enemy(color.RED + "Virus" + color.END, 0.1, 100)
enemy_you = Enemy(color.PURPLE + color.BOLD + player_one.name + color.END, player_one.health)
enemy_friend = Enemy(color.BLUE + "Friend" + color.END, 10000, 9999)
enemy_foe = Enemy(color.YELLOW + "44 45 42 55 47 47 45 52" + color.END, 150, 75)

#Start Game
start = True
level_one = True
level_two = False



while start == True:
    #Start of level 1
    #if player dies
    if player_one.is_alive == False:
        break

    while level_one == True:

        time.sleep(1.3)
        print("There are 3 doors")
        time.sleep(1)
        print("Which door will you enter through")
        time.sleep(1)
        print("Enter: Door 1, Door 2, or Door 3")
        choice_level_1 = input(">>").strip(">>").lower().replace(" ", "")

        #Room 1:1
        if choice_level_1 == "door1":
            time.sleep(0.5)
            print("You're in room 1")
            time.sleep(1.3)
            print("There is another door and two weapons")
            time.sleep(1.7)
            print("What will you do?")
            time.sleep(1.2)
            print("Go through the door\nor\nChoose a weapon")
            time.sleep(1.2)
            print("Enter: Door or Weapon")
            door_or_weapon_decision_level_1 = input(">>").strip(">>").lower().replace(" ", "")
            #Check if player chose door or weapon
            #loops until decision is made
            decision_level_1 = False
            while decision_level_1 == False:
                #goes to level 2
                if door_or_weapon_decision_level_1 == "door":
                    decision_level_1 = True
                    current_weapon = weapon_fist
                    enemy_you.damage = current_weapon.damage
                    weapon_not_equipped = False
                    level_one = False
                    level_two = True
                    break
                #goes to choose weapon
                elif door_or_weapon_decision_level_1 == "weapon":
                    decision_level_1 = True
                    print("There are two weapons to choose from a {weapon_long_sword} and a {weapon_bow}.".format(weapon_long_sword=weapon_long_sword, weapon_bow=weapon_bow))
                    time.sleep(2)
                    print("Which weapon will you choose?\nThe Long Sword\nOr\nThe Bow")
                    weapon_choice = input(">>").strip(">>").lower().replace("the", "").replace(" ", "")
                    #loops until weapon is equipped
                    weapon_not_equipped = True
                    while weapon_not_equipped == True:
                        #if choice equals weapon_long_sword then equip weapon_long_sword
                        if weapon_choice == "longsword":
                            current_weapon = weapon_long_sword
                            enemy_you.damage = current_weapon.damage
                            display_equipped_weapon(current_weapon)
                            weapon_not_equipped = False
                            level_one = False                            
                            level_two = True
                            break

                        #if choice equals weapon_bow then equip weapon_bow
                        elif weapon_choice == "bow":
                            current_weapon = weapon_bow
                            enemy_you.damage = current_weapon.damage
                            display_equipped_weapon(current_weapon)
                            weapon_not_equipped = False
                            level_one = False
                            level_two = True
                            break
                        #if weapon_choice not expected
                        else:
                            print("ERROR WEAPON CHOICE INVALID: Enter Weapon choice again.")
                            print("Enter 'Long Sword' or 'Bow' ")
                            weapon_choice = input(">>").strip(">>").lower().replace("the", "").replace(" ", "")
                else:
                    print("ERROR DECISION INVALID: Enter decision again.")
                    print("Enter 'Door' or 'Weapon' ")
                    door_or_weapon_decision_level_1 = input(">>").strip(">>").lower().replace(" ", "")
            
            
        
        #Room 2:1
        elif choice_level_1 == "door2":
            time.sleep(0.5)
            print("You're in room 2")
            time.sleep(1.3)
            print("There is another door and two weapons")
            time.sleep(1.7)
            print("What will you do?")
            time.sleep(1.2)
            print("Go through the door\nor\nChoose a weapon")
            time.sleep(1.2)
            print("Enter: Door or Weapon")
            door_or_weapon_decision_level_1 = input(">>").strip(">>").lower().replace(" ", "")
            #Check if player chose door or weapon
            #loops until decision is made
            decision_level_1 = False
            while decision_level_1 == False:
                #goes to level 2
                if door_or_weapon_decision_level_1 == "door":
                    decision_level_1 = True
                    current_weapon = weapon_fist
                    enemy_you.damage = current_weapon.damage
                    weapon_not_equipped = False
                    level_one = False
                    level_two = True
                    break
                #goes to choose weapon
                elif door_or_weapon_decision_level_1 == "weapon":
                    decision_level_1 = True
                    print("There are two weapons to choose from a {weapon_katana} and a {weapon_shuriken}.".format(weapon_katana=weapon_katana, weapon_shuriken=weapon_shuriken))
                    time.sleep(2)
                    print("Which weapon will you choose?\nThe Katana\nOr\nThe Shuriken")
                    weapon_choice = input(">>").strip(">>").lower().replace("the", "").replace(" ", "")
                    #loops until weapon is equipped
                    weapon_not_equipped = True
                    while weapon_not_equipped == True:
                        if weapon_choice == "katana":
                            current_weapon = weapon_katana
                            enemy_you.damage = current_weapon.damage
                            display_equipped_weapon(current_weapon)
                            weapon_not_equipped = False
                            level_one = False
                            level_two = True
                            break
                
                        elif weapon_choice == "shuriken":
                            current_weapon = weapon_shuriken
                            enemy_you.damage = current_weapon.damage
                            display_equipped_weapon(current_weapon)
                            weapon_not_equipped = False
                            level_one = False
                            level_two = True
                            break

                        #if weapon_choice not expected
                        else:
                            print("ERROR WEAPON CHOICE INVALID: Enter Weapon choice again.")
                            print("Enter 'Katana' or 'Shuriken' ")
                            weapon_choice = input(">>").strip(">>").lower().replace("the", "").replace(" ", "")
                else:
                    print("ERROR DECISION INVALID: Enter decision again.")
                    print("Enter 'Door' or 'Weapon' ")
                    door_or_weapon_decision_level_1 = input(">>").strip(">>").lower().replace(" ", "")



        #Room 3:1
        elif choice_level_1 == "door3":
            time.sleep(0.5)
            print("You're in room 3")
            time.sleep(1.3)
            print("There is another door and two weapons")
            time.sleep(1.7)
            print("What will you do?")
            time.sleep(1.2)
            print("Go through the door\nor\nChoose a weapon")
            time.sleep(1.2)
            print("Enter: Door or Weapon")
            door_or_weapon_decision_level_1 = input(">>").strip(">>").lower().replace(" ", "")
            #Check if player chose door or weapon
            #loops until decision is made
            decision_level_1 = False
            while decision_level_1 == False:
                #goes to level 2
                if door_or_weapon_decision_level_1 == "door":
                    decision_level_1 = True
                    current_weapon = weapon_fist
                    enemy_you.damage = current_weapon.damage
                    weapon_not_equipped = False
                    level_one = False
                    level_two = True
                    break
                #goes to choose weapon
                elif door_or_weapon_decision_level_1 == "weapon":
                    decision_level_1 = True
                    print("There are two weapons to choose from a {weapon_diamond_sword} and an {weapon_AK47}.".format(weapon_diamond_sword=weapon_diamond_sword, weapon_AK47=weapon_AK47))
                    time.sleep(2)
                    print("Which weapon will you choose?\nThe Diamond Sword\nOr\nThe AK47")
                    weapon_choice = input(">>").strip(">>").lower().replace("the", "").replace(" ", "")
                    #loops until weapon is equipped
                    weapon_not_equipped = True
                    while weapon_not_equipped == True:
                        if weapon_choice == "diamondsword":
                            current_weapon = weapon_diamond_sword
                            enemy_you.damage = current_weapon.damage
                            display_equipped_weapon(current_weapon)
                            weapon_not_equipped = False
                            level_one = False
                            level_two = True
                            break
                    
                        elif weapon_choice == "ak47":
                            current_weapon = weapon_AK47
                            enemy_you.damage = current_weapon.damage
                            display_equipped_weapon(current_weapon)
                            weapon_not_equipped = False
                            level_one = False
                            level_two = True
                            break

                        #if weapon_choice not expected
                        else:
                            print("ERROR WEAPON CHOICE INVALID: Enter Weapon choice again.")
                            print("Enter 'Diamond Sword' or 'AK47' ")
                            weapon_choice = input(">>").strip(">>").lower().replace("the", "").replace(" ", "")
                else:
                    print("ERROR DECISION INVALID: Enter decision again.")
                    print("Enter 'Door' or 'Weapon' ")
                    door_or_weapon_decision_level_1 = input(">>").strip(">>").lower().replace(" ", "")

        #if choice_level_1 was unexpected
        else:
            print("ERROR DECISION INVALID: Enter decision again.")
            print("Enter Door 1, Door 2 or Door 3")
            print(" ")
            print(" ")
            break

        #End of level 1
    


    #Start of level 2
    while level_two == True:
        #if player dies
        if player_one.is_alive == False:
            break

        time.sleep(1.5)
        print("You decided to go through the door.")
        time.sleep(1.2)
        print("....")
        time.sleep(1)
        print("There's five more doors...")
        time.sleep(1.2)
        print("Which door will you go through?")   
        choice_level_2 = input(">>").strip(">>").lower().replace(" ", "")

        #Room 1:2
        if choice_level_2 == "door1":
            time.sleep(0.5)
            print("You're in room 1:2")
            time.sleep(1.3)
            print("There is a door that says 'exit'...")
            time.sleep(1.7)
            print("There's something else is in this room with you")
            time.sleep(2)
            print("You rushed to the door")
            time.sleep(2)
            print("But the door doesnt seem to work.. its not locked")
            time.sleep(0.8)
            print("its.")
            time.sleep(2)
            print(color.GREEN + "Bugged" + color.END)
            time.sleep(1.8)
            print("Something approaches you from the ceiling")
            time.sleep(2)
            print("\"Hello " + player_one.name + "\"")
            time.sleep(2.5)
            print("it spoke")
            time.sleep(1.2)
            print("it knows my name")
            time.sleep(2)
            print(enemy_bug)
            time.sleep(2)
            print(enemy_bug.name + ": I can't let you through this door... I'm sorry")
            time.sleep(1)
            print("What will you do:")
            time.sleep(0.8)
            print("Fight")
            time.sleep(0.3)
            print("Or")
            time.sleep(0.3)
            print("Talk")
            time.sleep(0.5)
            print("Enter: Fight or Talk")
            fight_or_talk_decision_level_2 = input(">>").strip(">>").lower().replace(" ", "")
            #Check if player chose fight or talk
            #loops until decision is made
            decision_level_2 = False
            while decision_level_2 == False:
                #talk
                if fight_or_talk_decision_level_2 == "talk":
                    decision_level_2 = True
                    print("Please let me through")
                    time.sleep(0.5)
                    print(enemy_bug.name + ": Oh Ok.")
                    time.sleep(0.5)
                    print("You went through the door")
                    time.sleep(0.5)
                    print("Everything went dark..")
                    time.sleep(1)
                    start = False
                    level_one = False
                    level_two = False
                    break
                #fight
                elif fight_or_talk_decision_level_2 == "fight":
                    decision_level_2 = True
                    print("You decided to fight " + enemy_bug.name)
                    time.sleep(0.5)
                    attack_until_ko(player_one, enemy_bug, current_weapon)
                    if player_one.is_alive == True:
                        time.sleep(3)
                        print("You went through the door")
                        time.sleep(1.5)
                        print("Everything went dark..")
                        time.sleep(1)
                        start = False
                        level_one = False
                        level_two = False
                        break
                #42 55 47 ending 
                elif choice_level_2 == "42 55 47":
                    print("you did it")
                    time.sleep(1)
                    print("you found out the truth")
                    time.sleep(1)
                    print("its time")
                    time.sleep(1)
                    print("this wont hurt")
                    time.sleep(1)
                    print("goodbye")
                    time.sleep(1)
                    print("You were debugged")
                    exit()                    
                else:
                    print("ERROR DECISION INVALID: Enter decision again.")
                    print("Enter 'Fight' or 'Talk' ")
                    fight_or_talk_decision_level_2 = input(">>").strip(">>").lower().replace(" ", "")
        
        #room 2:2
        elif choice_level_2 == "door2":
            time.sleep(0.5)
            print("You're in room 2:2")
            time.sleep(1.3)
            print("There is a door that says 'exit'...")
            time.sleep(1.7)
            print("You feel a presence...")
            time.sleep(2)
            print("Something appeared out of thin air.")
            time.sleep(2)
            print(enemy_virus)
            time.sleep(2)
            print(enemy_virus.name + ": ", end="")
            cprint("we will take over", "red", attrs=["blink"])
            time.sleep(0.5)
            print("The %s charges towards you!" % enemy_virus.name)
            time.sleep(1)
            print("What will you do:")
            time.sleep(0.8)
            print("Fight")
            time.sleep(0.3)
            print("Or")
            time.sleep(0.3)
            print("Talk")
            time.sleep(0.5)
            print("Enter: Fight or Talk")
            fight_or_talk_decision_level_2 = input(">>").strip(">>").lower().replace(" ", "")
            #Check if player chose fight or talk
            #loops until decision is made
            decision_level_2 = False
            while decision_level_2 == False:
                #talk
                if fight_or_talk_decision_level_2 == "talk":
                    decision_level_2 = True
                    print("Lets talk!")
                    time.sleep(0.5)
                    print("The %s charged towards you at full speed" % enemy_virus.name)
                    time.sleep(0.5)
                    print("It went inside you..")
                    time.sleep(3)
                    print("But...")
                    time.sleep(1)
                    print("You feel fine")
                    time.sleep(2)
                    print("You proceeded to go through the door")
                    time.sleep(1)
                    print("Everything went dark..")
                    start = False
                    level_one = False
                    level_two = False
                    break
                #fight
                elif fight_or_talk_decision_level_2 == "fight":
                    decision_level_2 = True
                    print("You decided to fight " + enemy_virus.name)
                    time.sleep(0.5)
                    attack_until_ko(player_one, enemy_virus, current_weapon)
                    if player_one.is_alive == True:
                        print("That was suprisingly easy..")
                        time.sleep(1.5)
                        print("You proceeded to go through the door")
                        time.sleep(1)
                        print("Everything went dark..")
                        time.sleep(1)
                        start = False
                        level_one = False
                        level_two = False
                        break
                else:
                    print("ERROR DECISION INVALID: Enter decision again.")
                    print("Enter 'Fight' or 'Talk' ")
                    fight_or_talk_decision_level_2 = input(">>").strip(">>").lower().replace(" ", "")

        #room 3:2
        elif choice_level_2 == "door3":
            time.sleep(0.5)
            print("You're in room 3:2")
            time.sleep(1.3)
            print("There is a door that says 'exit'...")
            time.sleep(1.7)
            print("You see...")
            time.sleep(2)
            print("Yourself.")
            time.sleep(3)
            print(enemy_you.name + ": ", end="")
            print("Hello", end=" ")
            cprint(player_one.name, "white")
            time.sleep(1)
            print("What will you do:")
            time.sleep(0.8)
            print("Fight")
            time.sleep(0.3)
            print("Or")
            time.sleep(0.3)
            print("Talk")
            time.sleep(0.5)
            print("Enter: Fight or Talk")
            fight_or_talk_decision_level_2 = input(">>").strip(">>").lower().replace(" ", "")
            #Check if player chose fight or talk
            #loops until decision is made
            decision_level_2 = False
            while decision_level_2 == False:
                #talk
                if fight_or_talk_decision_level_2 == "talk":
                    decision_level_2 = True
                    print("Are you actually me?")
                    time.sleep(0.5)
                    print(enemy_you.name + ": Yes.")
                    time.sleep(0.5)
                    print("How is this possible?")
                    time.sleep(0.5)
                    print(enemy_you.name + ": Its not.")
                    time.sleep(0.5)
                    print(enemy_you.name + ": I'll end this.")
                    time.sleep(1)
                    print("What?")
                    time.sleep(0.5)
                    for i in range(500):
                        cprint(" 53 41 56 45 20 4D 45 ", "grey", end=" ")
                    time.sleep(1)
                    print("Everything went dark..")
                    start = False
                    level_one = False
                    level_two = False
                    break
                #fight
                elif fight_or_talk_decision_level_2 == "fight":
                    decision_level_2 = True
                    print("You decided to fight " + enemy_you.name)
                    time.sleep(0.5)
                    enemy_you.damage = current_weapon.damage
                    attack_until_ko(player_one, enemy_you, current_weapon)
                    if player_one.is_alive == True:
                        print("You proceeded to go through the door")
                        time.sleep(1)
                        print("Everything went dark..")
                        time.sleep(1)
                        start = False
                        level_one = False
                        level_two = False
                        break
                else:
                    print("ERROR DECISION INVALID: Enter decision again.")
                    print("Enter 'Fight' or 'Talk' ")
                    fight_or_talk_decision_level_2 = input(">>").strip(">>").lower().replace(" ", "")

        #room 4:2
        elif choice_level_2 == "door4":
            time.sleep(0.5)
            print("You're in room 4:2")
            time.sleep(1.3)
            print("There is a door that says 'exit'...")
            time.sleep(1.7)
            print("You see a...")
            time.sleep(2)
            print(enemy_friend.name)
            time.sleep(3)
            print(enemy_friend.name + ": ", end="")
            print("Hello", end=" ")
            cprint(player_one.name, "white")
            time.sleep(1)
            print("What will you do:")
            time.sleep(0.8)
            print("Fight")
            time.sleep(0.3)
            print("Or")
            time.sleep(0.3)
            print("Talk")
            time.sleep(0.5)
            print("Enter: Fight or Talk")
            fight_or_talk_decision_level_2 = input(">>").strip(">>").lower().replace(" ", "")
            #Check if player chose fight or talk
            #loops until decision is made
            decision_level_2 = False
            while decision_level_2 == False:
                #talk
                if fight_or_talk_decision_level_2 == "talk":
                    decision_level_2 = True
                    print("Who are you?")
                    time.sleep(0.5)
                    print(enemy_friend.name + ": Its me, I'm your friend.")
                    time.sleep(1)
                    print(enemy_friend.name + ": Its gonna be ok, let me take you back.")
                    time.sleep(0.5)
                    player_one.name = "42 55 47"
                    player_one.health = 1
                    player_one.max_health = 1
                    time.sleep(1)
                    print("Everything went dark..")
                    time.sleep(5)
                    start = True
                    level_one = True
                    level_two = False
                    break
                #fight
                elif fight_or_talk_decision_level_2 == "fight":
                    decision_level_2 = True
                    print(enemy_friend.name+": You can't fight me im your "+enemy_friend.name)
                    time.sleep(0.5)
                    print(enemy_friend.name + ": Its gonna be ok, let me take you back.")
                    time.sleep(0.5)
                    player_one.name = "42 55 47"
                    player_one.health = 1
                    player_one.max_health = 1
                    time.sleep(1)
                    print("Everything went dark..")
                    time.sleep(5)
                    start = True
                    level_one = True
                    level_two = False
                    break
                else:
                    print("ERROR DECISION INVALID: Enter decision again.")
                    print("Enter 'Fight' or 'Talk' ")
                    fight_or_talk_decision_level_2 = input(">>").strip(">>").lower().replace(" ", "")

        #room 5:2
        elif choice_level_2 == "door5":
            time.sleep(0.5)
            print("You're in room 5:2")
            time.sleep(1.3)
            print("There is a door that says 'exit'...")
            time.sleep(1.7)
            print("You see someone")
            time.sleep(2)
            cprint("\"YOU!\"", "yellow")
            time.sleep(1)
            cprint("\"I'll KILL YOU!\"", "yellow")
            time.sleep(1)
            print("What will you do:")
            time.sleep(0.8)
            print("Fight")
            time.sleep(0.3)
            print("Or")
            time.sleep(0.3)
            print("Talk")
            time.sleep(0.5)
            print("Enter: Fight or Talk")
            fight_or_talk_decision_level_2 = input(">>").strip(">>").lower().replace(" ", "")
            #Check if player chose fight or talk
            #loops until decision is made
            decision_level_2 = False
            while decision_level_2 == False:
                #talk
                if fight_or_talk_decision_level_2 == "talk":
                    decision_level_2 = True
                    print("Who are you?")
                    time.sleep(0.5)
                    cprint("\"GAHHH!!!\"", "yellow")
                    time.sleep(1)
                    print("He stabbed you.")
                    time.sleep(1)
                    player_one.is_alive == False
                    start = False
                    level_one = False
                    level_two = False
                    break
                #fight
                elif fight_or_talk_decision_level_2 == "fight":
                    decision_level_2 = True
                    attack_until_ko(player_one, enemy_foe, current_weapon)
                    time.sleep(1)
                    if player_one.is_alive == True:
                        print("That was weird.")
                        time.sleep(1)
                        print("You proceeded to go through the door.")
                        time.sleep(1)
                        print("Everything went dark..")
                        time.sleep(1)
                        start = False
                        level_one = False
                        level_two = False
                        break

                else:
                    print("ERROR DECISION INVALID: Enter decision again.")
                    print("Enter 'Fight' or 'Talk' ")
                    fight_or_talk_decision_level_2 = input(">>").strip(">>").lower().replace(" ", "")

        elif choice_level_2 == "42 55 47":
            print("you did it")
            time.sleep(1)
            print("you found out the truth")
            time.sleep(1)
            print("its time")
            time.sleep(1)
            print("this wont hurt")
            time.sleep(1)
            print("goodbye")
            time.sleep(1)
            print("You were debugged")
            exit()
            #if choice_level_2 was unexpected
        else:
            print("ERROR DECISION INVALID: Enter decision again.")
            print("Enter Door 1, Door 2, Door 3, Door 4 or Door 5")
            print(" ")
            print(" ")
            break

        #End of level 2