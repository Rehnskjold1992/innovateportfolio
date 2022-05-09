import wave, sys, time, random, os, winsound, getpass, hashlib
from random import shuffle, choice
from inputimeout import inputimeout, TimeoutOccurred
from playsound import playsound
from getpass import getpass
from msvcrt import getch,kbhit

character_name = "Lister" # remove whem imp
character = character_name
armory_choice = """\nA = Head to the secured armory.
B = Run in the opposite direction of Killy McKillsalot?\n"""
# decision = "decision"
vent_choice = """\nA = Kick the grate through and enter the med bay
B = Continue through the vent remaining quiet\n"""
armory_choice2 = """\nA = You head into the corridor towards the navigation deck
B = You attempt to gain entry to the med bay\n"""
corridor_combat_choice = """\nA = Head to the flight deck
B = Head to the escape pods\n"""
flight_deck_choice = """\nA = Head towards the Captain's quarters
B = Head towards the navigation room\n"""
captains_quarters_choice= """\nA = Hunker down and await potential help
B = Head towards the navigation room\n"""
navi_puzzle_failure_choice= """\nA = Run towards the escape pods
B = Run below deck, towards the reactor room\n"""
qte_choice = """\nA = Head towards the Comms room. 
B = Carry on down towards the lower decks in search of your comrades\n"""
qte_choice2 = """\nA = Head towards the armory with the keycard you obtained.
B = Continue on to the lower decks.\n"""
reactor_room_choice = """\nA = Initiate self-destruct sequence
B = Attempt to turn back\n"""
deus_ex_choice = """\nA = Continue looking around the navigation room.
B = Head to the reactor room to initiate the self-destruct\n"""
medbay_choice = """\nA = Use the ventilation system in an attempt to avoid detection
B = Check all the doors for an exit\n"""

def typewriter(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char =="\n":
            time.sleep(1)
        elif char == "." or char == "?" or char =="!":
            time.sleep(0.5)
        else:
            time.sleep(0.05)

def typewriter2(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char =="\n":
            time.sleep(1)
        elif char == "." or char == "?" or char =="!":
            time.sleep(2)
        else:
            time.sleep(0.05)

def typewriter3(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char =="\n":
            time.sleep(1)
        elif char == "." or char == "?" or char =="!":
            time.sleep(0.5)
        else:
            time.sleep(0.001)


def alien3():

    distanceFromLeft = 150

    while distanceFromLeft >= 80:
        print(" " * (distanceFromLeft - 1) +  r"        __.,,------.._  ")
        print(" " * (distanceFromLeft - 1) +  r"     ,'\"   _      _   \"`.")
        print(" " * (distanceFromLeft - 1) +  r"    /.__, ._  -=- _\"`    Y")
        print(" " * (distanceFromLeft - 1) +  r"   (.____.-.`      \"\"`   j ")
        print(" " * (distanceFromLeft - 1) +  r"    VvvvvvV`.Y,.    _.,-'       ,     ,     ,")
        print(" " * (distanceFromLeft - 1) +  r"        Y    ||,   '\"\         ,/    ,/    ./")
        print(" " * (distanceFromLeft - 1) +  r"        |   ,'  ,     `-..,'_,'/___,'/   ,'/   ,")
        print(" " * (distanceFromLeft - 1) +  r"   ..  ,;,,',-'\"\,\'  ,  .     '     ' \"\"\' \'--,/    .. ..")
        print(" " * (distanceFromLeft - 1) +  r" ,'. `.`---'     `, /  , Y -=-    ,'   ,   ,. .`-..||_|| ..")
        print(" " * (distanceFromLeft - 1) +  r"ff\\`. `._        /f ,'j j , ,' ,   , f ,  \=\ Y   || ||`||_..")
        print(" " * (distanceFromLeft - 1) +  r"l` \` `.`.\"`-..,-\' j  /./ /, , / , / /l \   \=\l   || `\' || ||...")
        print(" " * (distanceFromLeft - 1) +  r" `  `   `-._ `-.,-/ ,' /`\"/-/-/-/-\"''\"`.`.  `'.\--`'--..`'_`' || ,")
        print(" " * (distanceFromLeft - 1) +  r"            \"`-_,',  ,'  f    ,   /      `._    ``._     ,  `-.`'//         ,")
        print(" " * (distanceFromLeft - 1) +  r"          ,-\"'' _.,-'    l_,-'_,,'          \"`-._ . \"`. /|     `.'\ ,       |")
        print(" " * (distanceFromLeft - 1) +  r"        ,',.,-'\"          \=) ,`-.         ,    `-'._`.V |       \ // .. . /j")
        print(" " * (distanceFromLeft - 1) +  r"        |f\\               `._ )-.\"`.     /|         `.| |        `.`-||-\\/")
        print(" " * (distanceFromLeft - 1) +  r"        l` \`                 \"`._   \"`--' j          j' j          `-`---'")
        print(" " * (distanceFromLeft - 1) +  r"         `  `                     \"`_,-','/       ,-'\"  /")
        print(" " * (distanceFromLeft - 1) +  r"                                 ,'\",__,-'       /,, ,-'")
        print(" " * (distanceFromLeft - 1) +  r"                                 Vvv'            VVv'")
        time.sleep(0.05)
        os.system('cls')  
        distanceFromLeft -= 1
        if distanceFromLeft == 80:
            alienstatic()
            break
        else:
            os.system('cls')
            

def alienstatic():
    print(" " * 80 +  r"        __.,,------.._  ")
    print(" " * 80 +  r"     ,'\"   _      _   \"`.")
    print(" " * 80 +  r"    /.__, ._  -=- _\"`    Y")
    print(" " * 80 +  r"   (.____.-.`      \"\"`   j ")
    print(" " * 80 +  r"    VvvvvvV`.Y,.    _.,-'       ,     ,     ,")
    print(" " * 80 +  r"        Y    ||,   '\"\         ,/    ,/    ./")
    print(" " * 80 +  r"        |   ,'  ,     `-..,'_,'/___,'/   ,'/   ,")
    print(" " * 80 +  r"   ..  ,;,,',-'\"\,\'  ,  .     '     ' \"\"\' \'--,/    .. ..")
    print(" " * 80 +  r" ,'. `.`---'     `, /  , Y -=-    ,'   ,   ,. .`-..||_|| ..")
    print(" " * 80 +  r"ff\\`. `._        /f ,'j j , ,' ,   , f ,  \=\ Y   || ||`||_..")
    print(" " * 80 +  r"l` \` `.`.\"`-..,-\' j  /./ /, , / , / /l \   \=\l   || `\' || ||...")
    print(" " * 80 +  r" `  `   `-._ `-.,-/ ,' /`\"/-/-/-/-\"''\"`.`.  `'.\--`'--..`'_`' || ,")
    print(" " * 80 +  r"            \"`-_,',  ,'  f    ,   /      `._    ``._     ,  `-.`'//         ,")
    print(" " * 80 +  r"          ,-\"'' _.,-'    l_,-'_,,'          \"`-._ . \"`. /|     `.'\ ,       |")
    print(" " * 80 +  r"        ,',.,-'\"          \=) ,`-.         ,    `-'._`.V |       \ // .. . /j")
    print(" " * 80 +  r"        |f\\               `._ )-.\"`.     /|         `.| |        `.`-||-\\/")
    print(" " * 80 +  r"        l` \`                 \"`._   \"`--' j          j' j          `-`---'")
    print(" " * 80 +  r"         `  `                     \"`_,-','/       ,-'\"  /")
    print(" " * 80 +  r"                                 ,'\",__,-'       /,, ,-'")
    print(" " * 80 +  r"                                 Vvv'            VVv'")
    print(playerart)

def software_engineer_anim():
    os.system('cls' if os.name == 'nt' else 'clear')
    distanceFromLeft = 150
    while distanceFromLeft >= 80:
        print(" " * (distanceFromLeft - 1) +  r"         ,---,_          ,")
        print(" " * (distanceFromLeft - 1) +  r"         _>   `'-.  .--'/")
        print(" " * (distanceFromLeft - 1) +  r"    .--'` ._      `/   <_")
        print(" " * (distanceFromLeft - 1) +  r"     >,-' ._'.. ..__ . ' '-.")
        print(" " * (distanceFromLeft - 1) +  r"  .-'   .'`         `'.     '.")
        print(" " * (distanceFromLeft - 1) +  r"   >   / >`-.     .-'< \ , '._\ ")
        print(" " * (distanceFromLeft - 1) +  r"  /    ; '-._>   <_.-' ;  '._>")
        print(" " * (distanceFromLeft - 1) +  r"  `>  ,/  /___\ /___\  \_  /")
        print(" " * (distanceFromLeft - 1) +  r"  `.-|(|  \o_/  \o_/   |)|`")
        print(" " * (distanceFromLeft - 1) +  r"      \;        \      ;/")
        print(" " * (distanceFromLeft - 1) +  r"        \  .-,   )-.  /")
        print(" " * (distanceFromLeft - 1) +  r"         /`  .'-'.  `\ ")
        print(" " * (distanceFromLeft - 1) +  r"        ;_.-`.___.'-.;")
        time.sleep(0.05)
        os.system('cls')  
        distanceFromLeft -= 1
        if distanceFromLeft == 80:
            break
        else:
            os.system('cls')

def engineerstatic():
    distanceFromLeft = 150
    print(" " * 80 +  r"         ,---,_          ,")
    print(" " * 80 +  r"         _>   `'-.  .--'/")
    print(" " * 80 +  r"    .--'` ._      `/   <_")
    print(" " * 80 +  r"     >,-' ._'.. ..__ . ' '-.")
    print(" " * 80 +  r"  .-'   .'`         `'.     '.")
    print(" " * 80 +  r"   >   / >`-.     .-'< \ , '._\ ")
    print(" " * 80 +  r"  /    ; '-._>   <_.-' ;  '._>")
    print(" " * 80 +  r"  `>  ,/  /___\ /___\  \_  /")
    print(" " * 80 +  r"  `.-|(|  \o_/  \o_/   |)|`")
    print(" " * 80 +  r"      \;        \      ;/")
    print(" " * 80 +  r"        \  .-,   )-.  /")
    print(" " * 80 +  r"         /`  .'-'.  `\ ")
    print(" " * 80 +  r"        ;_.-`.___.'-.;")
    print(playerart)


#############################################################################################################
#hero_attributes Assigns attribures to the Lister Character_Loot has no function at the moment but could be called later
class Player (object):
    name = "????"
    health = 40
    maxhealth = 40
    strength = 10
    invent = {"Medkit" : 1, "Grenade" : 0, "Assault Rifle" : 0}
    key_card = False
    flight_data = False
    deus_ex = False

#enemy_attributes_Assigns the enemy attributes to Xeno
class Xeno (object):
    name = "Alien"
    health = 40
    strength = 8

#enemy_attributes_Assigns the enemy attributes to Software Engineer
class Engineer (object):
    name = "Crazed Software Engineer"
    health = 20
    strength = 6

class BossAlien (object):
    name = "Xenomorph"
    health = 50
    strength = 10


def win():
    
    print("""

   _____                            _         _       _   _                 _ 
  / ____|                          | |       | |     | | (_)               | |
 | |     ___  _ __   __ _ _ __ __ _| |_ _   _| | __ _| |_ _  ___  _ __  ___| |
 | |    / _ \| '_ \ / _` | '__/ _` | __| | | | |/ _` | __| |/ _ \| '_ \/ __| |
 | |___| (_) | | | | (_| | | | (_| | |_| |_| | | (_| | |_| | (_) | | | \__ \_|
  \_____\___/|_| |_|\__, |_|  \__,_|\__|\__,_|_|\__,_|\__|_|\___/|_| |_|___(_)
                     __/ |                                                    
                    |___/                                                     """)
    playsound("victory.wav")
    time.sleep(5)
    sys.exit()                

def loot(enemy):

    loot = ["Medkit", "Grenade", "Assault Rifle"]
    chanceloot = random.randint(0,2)
    lootdrop = loot[chanceloot]

    if enemy == BossAlien:
        Player.deus_ex = True
        # print("You found a Deus Ex!")
        time.sleep(1)
        return

    if enemy == Engineer:
        Player.key_card = True
        print("You found a Key Card!")
        time.sleep(1)
        return

    if enemy == Xeno:
        
        if lootdrop == "Medkit":
            Player.invent["Medkit"] +=1
            print("You have found a Medkit!")
            time.sleep(1)
            return

        if lootdrop == "Grenade":
            Player.invent["Grenade"] +=1
            print("You have found a Grenade!")
            time.sleep(1)
            return

        if lootdrop == "Assault Rifle":
            Player.invent["Assault Rifle"] +=1
            print("You have found an Assault Rifle!")
            time.sleep(1)
            return

#Game_Over_This gives an ending to the game and also a high score_referenced in option 1 & 2 below
def gameover(Player):
    if Player.health < 1:
        winsound.PlaySound(None, winsound.SND_PURGE)
        deathbyxeno() #replace with toms death (function)
         # Remove

### !!!Battle Mechanic!!! ###
def battlestate(Player, enemy):
    def healthbar(Player):
        healthDashes = 20
        health = Player.health
        maxHealth = Player.maxhealth
        dashConvert = int(Player.maxhealth/healthDashes)            # Get the number to divide by to convert health to dashes (being 10)
        currentDashes = int(health/dashConvert)              # Convert health to dash count: 80/10 => 8 dashes
        remainingHealth = healthDashes - currentDashes
        healthDisplay = '-' * currentDashes                  # Convert 8 to 8 dashes as a string:   "--------"
        remainingDisplay = ' ' * remainingHealth             # Convert 12 to 12 spaces as a string: "            "
        percent = str(int((health/maxHealth)*100)) + "%"
        print("\n|" + healthDisplay + remainingDisplay + "|")  # Print out textbased healthbar
        print("         " + percent)
        print(f"        Health")

    sndfile = "battle.wav"      #will play pokemon battle music if correct lib installed, if not comment out and import at top
    winsound.PlaySound(sndfile, winsound.SND_ASYNC)
    if enemy == Engineer:
        software_engineer_anim()
        os.system('cls' if os.name == 'nt' else 'clear')
        engineerstatic()
        typewriter(f"""\nA wild {enemy.name} has appeared!""")
        time.sleep(2)
    elif enemy == Xeno or BossAlien:
        alien3()
        os.system('cls' if os.name == 'nt' else 'clear')
        alienstatic()
        typewriter(f"""\nA wild {enemy.name} has appeared!""")
        time.sleep(2)

        

    while enemy.health > 0 : #while loop will repeat the option to run or fight as long as the enemy health is over 0
        
        
        def menu():
            os.system('cls' if os.name == 'nt' else 'clear')
            print("")
            
            if enemy == Engineer:
                engineerstatic()
                
            elif enemy == Xeno or BossAlien:
                alienstatic()
                    
        
            
        

        
                 

        healthbar(Player)
        choice = getpass(prompt="\n1. Fight \n2. Use item\n")
        if choice == "1":

            typewriter(f"You attack the {enemy.name}\n") #displays a message saying what enemy you are attacking
            hitchance = random.randint(1,10) #hitchance is an int from 1-10

            if hitchance > 5:#if hitchance is over 4 the attack is successful_gives a 50% chance of success_can be changed to make the game harder or easier
                if hitchance >= 8:
                    enemy.health = enemy.health - 5
                    playsound('playercrit.wav')
                    typewriter("Critical hit!\n")
                    
                
                    

                     

                enemy.health = enemy.health - Player.strength - random.randint(1,6)
                playsound('shortened lazer.wav')
                if enemy.health < 0:
                    enemy.health = 0
                typewriter(f"You shoot the {enemy.name}, their health is now {enemy.health}\n")
                               

                if enemy.health > 0:        #Enemy attacks player
                    hitchance = random.randint(1,10)
                    if hitchance >= 4:
                        Player.health = Player.health - enemy.strength - random.randint(1,6)
                        playsound('playerhit.wav')
                        if Player.health < 0:
                            Player.health = 0
                        typewriter(f"The {enemy.name} attacks, you now have {Player.health} health.\n")
                        os.system('cls' if os.name == 'nt' else 'clear')
                        
                        if enemy == "Engineer":
                            Player.health < 1
                            dead()
                        elif Player.health < 1:
                            deathbyxeno()
                            
                    else:
                        typewriter(f"The {enemy.name} misses.\n")
                        time.sleep(1)
                        os.system('cls' if os.name == 'nt' else 'clear')
    #reset enemy health_this will reset the health of the enemy after battle
                else:
                    enemy.health =  18
                                           
                    winsound.PlaySound(None, winsound.SND_PURGE)
                    typewriter(f"You have defeated the {enemy.name}.\n") #prints message when enemy defeated    
                    playsound('victory.wav')
                    loot(enemy)
                    return
                    break
                               
            else:
                playsound('nani.wav')
                typewriter("You miss.\n")       #<<<
                typewriter(f"The {enemy.name} takes advantage of your miss and hits you for a critical!\n")
                playsound('crit.wav')
                Player.health = Player.health - enemy.strength - random.randint(1,10) -2
                if Player.health < 0:
                    Player.health = 0
                typewriter(f"You have {Player.health} health remaining\n")
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
                if enemy == "Engineer":
                    Player.health < 1
                    deathbyxeno()
                elif Player.health < 1:
                    deathbyxeno()
            menu()    

        elif choice == "2": # Using items mechanic
            if Player.invent == {"Medkit" : 0, "Grenade" : 0, "Assault Rifle" : 0}: # Recognises whether invent has any items in it
                typewriter("You have no items!")
                time.sleep(1)
                menu()
            else:
                print("Use which item?\n") # If so, pick one
                for count, i in enumerate(Player.invent):
                    print(f"{count+1} =", i, Player.invent[i])
                print("4 = Exit Inventory")
            
                ch_item = getpass(prompt="")

                if ch_item == "1" and Player.invent["Medkit"] > 0: # Sep check for the item and how it is used
                    Player.health = 40
                    print("You use a Medkit!")
                    playsound('heal.wav')
                    typewriter(f"Your health is now, {Player.health}")
                    Player.invent["Medkit"] -= 1
                    time.sleep(2)
                    menu()
                elif ch_item == "1":
                    print("Sorry, you have no Medkits.")
                    time.sleep(2)
                    menu()
                elif ch_item == "2" and Player.invent["Grenade"] > 0:
                    enemy.health -= 20
                    typewriter("You throw a grenade\n")
                    playsound ('kaboom.wav')
                    typewriter(f"The {enemy.name} is hit by the blast. Its health is now, {enemy.health}.")
                    Player.invent["Grenade"] -= 1
                    time.sleep(1)
                    if enemy.health <= 0:
                        playsound('victory.wav')
                        loot(enemy)
                        return
                    menu()
                elif ch_item == "2":
                    print("Sorry, you have no Grenades.")
                    time.sleep(2)
                    menu()
                elif ch_item == "3" and Player.invent["Assault Rifle"] > 0:
                    Player.strength += 10
                    playsound('gun.wav')
                    typewriter(f"You equip an Assault Rifle, your attack is now, {Player.strength}")
                    Player.invent["Assault Rifle"] -= 1
                    menu()
                elif ch_item == "3":
                    print("Sorry, you don't have an Assault Rifle.")
                    time.sleep(2)
                    menu()
                elif ch_item == "4":
                    menu()
                else:
                    menu()
        else:
            menu()

###############################################################################################################

# def test():
#     print("This is option A")
#     input_check(decision, test, test2)

# def test2():
#     print("This is option B")
#     input_check(decision, test, test2)



def dead():
    print("\n""""
▓██   ██▓ ▒█████   █    ██    ▓█████▄  ██▓▓█████ ▓█████▄ 
 ▒██  ██▒▒██▒  ██▒ ██  ▓██▒   ▒██▀ ██▌▓██▒▓█   ▀ ▒██▀ ██▌
  ▒██ ██░▒██░  ██▒▓██  ▒██░   ░██   █▌▒██▒▒███   ░██   █▌
  ░ ▐██▓░▒██   ██░▓▓█  ░██░   ░▓█▄   ▌░██░▒▓█  ▄ ░▓█▄   ▌
  ░ ██▒▓░░ ████▓▒░▒▒█████▓    ░▒████▓ ░██░░▒████▒░▒████▓ 
   ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒     ▒▒▓  ▒ ░▓  ░░ ▒░ ░ ▒▒▓  ▒ 
 ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░     ░ ▒  ▒  ▒ ░ ░ ░  ░ ░ ▒  ▒ 
 ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░     ░ ░  ░  ▒ ░   ░    ░ ░  ░ 
 ░ ░         ░ ░     ░           ░     ░     ░  ░   ░    
 ░ ░                           ░                  ░      
""")
    playsound("scream.wav")
    time.sleep(2)
    sndfile = "gameover.wav"      
    winsound.PlaySound(sndfile, winsound.SND_ASYNC)
    choice = getpass(prompt="Press A to Continue.")
    
    if choice.upper() == "A":
        intro()
    else:
        sys.exit()


    
def vent_puzzle_success():
    os.system('cls' if os.name == 'nt' else 'clear')
    typewriter("""\nYou have successfully navigated the Konami ventilation system.
You find yourself directly above the foyer outside the Captain's quarters.
After removing the ventilation grill and dropping down you find yourself face to face with one of those creatures that has been tearing up the ship.""")
    battlestate(Player, BossAlien)
    captains_quarters()




def elevator():
    os.system('cls' if os.name == 'nt' else 'clear')
    distanceFromLeft = 0
    print(" " * (distanceFromLeft - 1) +  r"            .-----.----.-----.   ")
    print(" " * (distanceFromLeft - 1) +  r"           / /-.| |////| |.-\ \  ")
    print(" " * (distanceFromLeft - 1) +  r"          / /|_|| |////| ||_|\ \ ")
    print(" " * (distanceFromLeft - 1) +  r"         /  :   : |////| :   :  \ ")
    print(" " * (distanceFromLeft - 1) +  r"        /  /___:  |////|  :___\  \ ")
    print(" " * (distanceFromLeft - 1) +  r"       /   :   |_ |////| _|   :___\ ")
    print(" " * (distanceFromLeft - 1) +  r"      /   /    |_||////||_|    \   \ ")
    print(" " * (distanceFromLeft - 1) +  r"     /    :    |_||////||_|    :    \ ")
    print(" " * (distanceFromLeft - 1) +  r"    /____/____ |_||////||_| ____\____\ ")
    print(" " * (distanceFromLeft - 1) +  r"   /     :    |   |////|   |    :     \ ")
    print(" " * (distanceFromLeft - 1) +  r"  /     /     | _ |////| _ |     \     \ ")
    print(" " * (distanceFromLeft - 1) +  r"  \     :     || ||////|| ||     :     / ")
    print(" " * (distanceFromLeft - 1) +  r"   \   /    .'-\ ||////|| /-`.    \   / ")
    print(" " * (distanceFromLeft - 1) +  r"-----'-'---------'-'----'-'---------'-'-----")

    answer = "500"      # Loop requirment before use.
    options = []

    typewriter("""You approach the elevator console and attempt to disengage the emergency lockdown.\n
The particular bypass for this elevator has you balance an equation. Who are these security methods designed to keep out?\n\n\n""")
    time.sleep(5)

    for i in range(0, 3):       #Generate 3 random numbers
        options.insert(i, random.randint(1, 12))

    gen_ans = int((options[0]*options[1]) - options[2]) # Generates answer to test against

    try:
        while int(answer) != gen_ans: #While incorrect
            answer = inputimeout(prompt=f"""Find the value of X 
{options[0]} * {options[1]} = X + {options[2]}\n""", timeout=10) # Asks question with 10sec timer

            if answer.isdigit() and int(answer) != gen_ans:     #Error checking
                print("Try Again")
            elif str(answer) != gen_ans:     #original code had int(answer). typing a letter broke the error checking
                print("Must be a number!")
    except TimeoutOccurred:
        print(f"The correct answer was, {gen_ans}, ya big dummy")
        time.sleep(2)
        elevator_failure() # Fail condition if timer expires

    elevator_success()

def reactor_combat():
    os.system('cls' if os.name == 'nt' else 'clear')
    typewriter("""As you travel down further and further towards the reactor room, you come across another Xenomorph.""")
    time.sleep(2)
    battlestate(Player, BossAlien)
    os.system('cls' if os.name == 'nt' else 'clear')
    typewriter("""Having defeated the Xenomorph you continue onwards...""")
    time.sleep(1)
    reactor_room()


def attempt_to_leave():
    os.system('cls' if os.name == 'nt' else 'clear')
    typewriter("""You attempt to turn back. The self-destruct sequence cannot be engaged\n""")
    typewriter("Upon attempting to leave the reactor room, you are met by a tidal wave of Aliens and Xenomorphs.")
    time.sleep(2)
    deathbyxeno()

def self_destruct2():
    os.system('cls' if os.name == 'nt' else 'clear')
    typewriter("You input the self-destruct codes so ship go boom boom.")
    playsound("kaboom.wav")
    time.sleep(1)
    win()

def self_destruct_engaged():
    if Player.deus_ex == True:      
        self_destruct2()
        typewriter("""You possess the Deus Ex Machina, you can initiate the self-destruct sequence...\n
You must make a decision:
A = Initiate the Self-destruct.
B = Turn back.""")
        input_check(reactor_room_choice, self_destruct2, attempt_to_leave)
    attempt_to_leave()

def reactor_room():
    os.system('cls' if os.name == 'nt' else 'clear')
    typewriter("""Eventually you find yourself in the reactor room.
The reactor that powers the ship hums with an ominous energy in front of you.
A lone engineering terminal sits to one side of the reactor.
The terminal is asking for a self destruct sequence...
You must make a decision:""")
    input_check(reactor_room_choice, self_destruct_engaged, attempt_to_leave)

def vent_puzzle_fail():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
   ____                        _ 
  / __ \                      | |
 | |  | | ___   ___  _ __  ___| |
 | |  | |/ _ \ / _ \| '_ \/ __| |
 | |__| | (_) | (_) | |_) \__ \_|
  \____/ \___/ \___/| .__/|___(_)
                    | |          
                    |_|          """)
    typewriter("""\nIt seems have lost your way in the ventilation system, although you were certain you followed that Konami map precisely...
Many twists and turns later you begin to feel an unknown force pulling at you, which quickly becomes a strong suction which you lack the strength to resist.
It seems you've fallen foul of the ships timed ventilation system.""")
    dead_fan()

def dead_fan():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
    ______________$$$$$$$$$_____$$$$
    __________$$$$$______$$$$$__$$_$$
    _______$$$$_____$__$$$___$$$$$$$$$$
    _____$$$_________$$$________$$$$$$$$                           -
    ___$$$____________$$__________$$$$$$$
    __$$$______________$____________$$$$_$
    _$$$$______________$$____________$$$$$$                                                    -
    _$__$____________$$$$$$$________$_$$$_$                -
    $$___$$_________$$____$$$$___$$$$$$$$$$$                                  Awh heckkkkkkkkkkkkkkkkkkkkkk
    $___$$$$$$$___$$$_______$$$$$$$____$$$_$                            7_O_/
    $_$$$___$$$$$$$___________$$_______$$$_$                             (/
    $$$__________$$__________$$________$$$_$         -                   /\/'
    $_____________$$_________$_________$$$$$                             7
    $$_____________$$_______$$________$$$_$$
    _$______________$$$$$$$$$$________$$$_$                                           -
    _$$____________$$________$$$_____$$$_$$
    __$$__________$$__________$$$__$$$$$$$
    ___$$$______$$$_____________$_$$$$_$$
    _____$$$____$$_____________$$$$$$_$$
    _____$$$$$$___$__________$$$$$$$_$$                     -
    ____$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    _____$$$$$$$$$$$$$$$$$$$$$$$$$$$
    ________$$$$$$$$$$$$$$$$$$$$$
    ____________$$$$$$$$$$$
    """)
    dead()
import time, random, sys, os
from inputimeout import inputimeout, TimeoutOccurred

def software_engineer():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(r"          ,---,_          ,")
    print(r"          _>   `'-.  .--'/")
    print(r"     .--'` ._      `/   <_")
    print(r"      >,-' ._'.. ..__ . ' '-.")
    print(r"   .-'   .'`         `'.     '.")
    print(r"    >   / >`-.     .-'< \ , '._\ ")
    print(r"   /    ; '-._>   <_.-' ;  '._>")
    print(r"   `>  ,/  /___\ /___\  \_  /")
    print(r"   `.-|(|  \o_/  \o_/   |)|`")
    print(r"       \;        \      ;/")
    print(r"         \  .-,   )-.  /")
    print(r"          /`  .'-'.  `\ ")
    print(r"         ;_.-`.___.'-.;")

    print("")

    typewriter("""\nOn your way to the comms room you come across a survivor... 
infront of you there is a disheveled software engineer, clearly shaken by the situation on the ship he begins to mumble at you in
an indistinguisable manner. It turns out this guy is an intern from CodeNation.\n""")
    typewriter("The crazed sofware engineer asks:\n")
    
    questions = ["How would a quackers person get good luck?", "You can't have a bath without a...?", "Answer to the Ultimate Question of Life, the Universe, and Everything?"]
    print(random.choice(questions))

    print("A = Rabbits Foot\nB = Plastic Cheetah\nC = Wooden Dog\nD = Rubber Duck")

    answer = input("Answer: ")
    if answer != "D" and answer != "d":
        typewriter("""The software engineer becomes visibily agitated at your obviously incorrect answer...
his mumbling and erratic behaviour begins to turn violent.""") #Replace with combat func
        software_engineer_combat()   
    else:
        typewriter("""\nThe software engineer's mumbling takes on a lighter tone and he beckons you forward, swiping his keycard and opening the door he was positioned in front of.
Inside the room you find a veritable treasure trove of supplies, seemingly the software engineer was stockpiling equipment.
Encouraged to take whatever you can carry you don't notice that the crazed madman has slipped away back through the door and sealed it behind you.""") # not atk func here
        loot(Xeno)
        time.sleep(2)
        alien_mini_boss()
        

def software_engineer_combat():
    typewriter("""\nThe software engineer strips down to his underwear in a fervant craze, attaches a macbook pro to his wrist and pulls a knife from an unknown location.
This impromptu sword & board fighting style should be easy to overcome with physical force.""")
    battlestate(Player, Engineer)
    qte_success()


def alien_mini_boss():
    typewriter("""With the door sealed behind you, your only option is to press on. 
There must have been a reason that madman was stockpiling...""")
    os.system('cls' if os.name == 'nt' else 'clear')
    typewriter("""After continuing a short ways down the only open path, you notice in the distance at the end of the corridor there is a Xenomorph.
With the way behind you closed, and the only place this corridor leads being behind the Xenomorph your only option is to fight!
This is the final combat of this route, so make use of all your items.""")
    battlestate(Player, BossAlien)
    os.system('cls' if os.name == 'nt' else 'clear')
    typewriter("""\nThe Xenomorph drops to the floor, riddled with holes and bleeding profusely.
After giving it one more shot in the head because you don't believe in using movie tropes, you begin to step over it into the room behind it,
The communications room.""")
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    typewriter("""Using the various equipment in this room it is possible to send an SOS signal and await rescue.
Seems like the sensible thing to do /shrug.""")
    win()

def deathbyxeno():
    typewriter("\n""You become a Xeno's best attempt at a Jackson Pollock painting.")
    playsound("playerhit.wav")
    dead()

def fan_malfunction():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
   ____                        _ 
  / __ \                      | |
 | |  | | ___   ___  _ __  ___| |
 | |  | |/ _ \ / _ \| '_ \/ __| |
 | |__| | (_) | (_) | |_) \__ \_|
  \____/ \___/ \___/| .__/|___(_)
                    | |          
                    |_|          """)
    typewriter("""
The fan begins to go haywire, spinning out of control and starting to suck you towards it with overwhelming force, 
Your final thoughts as you begin to lose your grip, are 'Why did I sleep through Art class?'""")
    typewriter("\n""You finally succumb to the suction of the fan and are turned into chum as you pass through it.")
    dead_fan()


def alien():

    distanceFromLeft = 30

    while distanceFromLeft >= 0:
        print(" " * (distanceFromLeft - 1) +  r"        __.,,------.._  ")
        print(" " * (distanceFromLeft - 1) +  r"     ,'\"   _      _   \"`.")
        print(" " * (distanceFromLeft - 1) +  r"    /.__, ._  -=- _\"`    Y")
        print(" " * (distanceFromLeft - 1) +  r"   (.____.-.`      \"\"`   j ")
        print(" " * (distanceFromLeft - 1) +  r"    VvvvvvV`.Y,.    _.,-'       ,     ,     ,")
        print(" " * (distanceFromLeft - 1) +  r"        Y    ||,   '\"\         ,/    ,/    ./")
        print(" " * (distanceFromLeft - 1) +  r"        |   ,'  ,     `-..,'_,'/___,'/   ,'/   ,")
        print(" " * (distanceFromLeft - 1) +  r"   ..  ,;,,',-'\"\,\'  ,  .     '     ' \"\"\' \'--,/    .. ..")
        print(" " * (distanceFromLeft - 1) +  r" ,'. `.`---'     `, /  , Y -=-    ,'   ,   ,. .`-..||_|| ..")
        print(" " * (distanceFromLeft - 1) +  r"ff\\`. `._        /f ,'j j , ,' ,   , f ,  \=\ Y   || ||`||_..")
        print(" " * (distanceFromLeft - 1) +  r"l` \` `.`.\"`-..,-\' j  /./ /, , / , / /l \   \=\l   || `\' || ||...")
        print(" " * (distanceFromLeft - 1) +  r" `  `   `-._ `-.,-/ ,' /`\"/-/-/-/-\"''\"`.`.  `'.\--`'--..`'_`' || ,")
        print(" " * (distanceFromLeft - 1) +  r"            \"`-_,',  ,'  f    ,   /      `._    ``._     ,  `-.`'//         ,")
        print(" " * (distanceFromLeft - 1) +  r"          ,-\"'' _.,-'    l_,-'_,,'          \"`-._ . \"`. /|     `.'\ ,       |")
        print(" " * (distanceFromLeft - 1) +  r"        ,',.,-'\"          \=) ,`-.         ,    `-'._`.V |       \ // .. . /j")
        print(" " * (distanceFromLeft - 1) +  r"        |f\\               `._ )-.\"`.     /|         `.| |        `.`-||-\\/")
        print(" " * (distanceFromLeft - 1) +  r"        l` \`                 \"`._   \"`--' j          j' j          `-`---'")
        print(" " * (distanceFromLeft - 1) +  r"         `  `                     \"`_,-','/       ,-'\"  /")
        print(" " * (distanceFromLeft - 1) +  r"                                 ,'\",__,-'       /,, ,-'")
        print(" " * (distanceFromLeft - 1) +  r"                                 Vvv'            VVv'")
        time.sleep(0.05)
        os.system('cls')  
        distanceFromLeft -= 1
        if distanceFromLeft == 0:
            break
        else:
            os.system('cls')


def alien2():

    distanceFromLeft = 60

    while distanceFromLeft >= 0:
        print(" " * (distanceFromLeft - 1) +  r"        __.,,------.._  ")
        print(" " * (distanceFromLeft - 1) +  r"     ,'\"   _      _   \"`.")
        print(" " * (distanceFromLeft - 1) +  r"    /.__, ._  -=- _\"`    Y")
        print(" " * (distanceFromLeft - 1) +  r"   (.____.-.`      \"\"`   j ")
        print(" " * (distanceFromLeft - 1) +  r"    VvvvvvV`.Y,.    _.,-'       ,     ,     ,")
        print(" " * (distanceFromLeft - 1) +  r"        Y    ||,   '\"\         ,/    ,/    ./")
        print(" " * (distanceFromLeft - 1) +  r"        |   ,'  ,     `-..,'_,'/___,'/   ,'/   ,")
        print(" " * (distanceFromLeft - 1) +  r"   ..  ,;,,',-'\"\,\'  ,  .     '     ' \"\"\' \'--,/    .. ..")
        print(" " * (distanceFromLeft - 1) +  r" ,'. `.`---'     `, /  , Y -=-    ,'   ,   ,. .`-..||_|| ..")
        print(" " * (distanceFromLeft - 1) +  r"ff\\`. `._        /f ,'j j , ,' ,   , f ,  \=\ Y   || ||`||_..")
        print(" " * (distanceFromLeft - 1) +  r"l` \` `.`.\"`-..,-\' j  /./ /, , / , / /l \   \=\l   || `\' || ||...")
        print(" " * (distanceFromLeft - 1) +  r" `  `   `-._ `-.,-/ ,' /`\"/-/-/-/-\"''\"`.`.  `'.\--`'--..`'_`' || ,")
        print(" " * (distanceFromLeft - 1) +  r"            \"`-_,',  ,'  f    ,   /      `._    ``._     ,  `-.`'//         ,")
        print(" " * (distanceFromLeft - 1) +  r"          ,-\"'' _.,-'    l_,-'_,,'          \"`-._ . \"`. /|     `.'\ ,       |")
        print(" " * (distanceFromLeft - 1) +  r"        ,',.,-'\"          \=) ,`-.         ,    `-'._`.V |       \ // .. . /j")
        print(" " * (distanceFromLeft - 1) +  r"        |f\\               `._ )-.\"`.     /|         `.| |        `.`-||-\\/")
        print(" " * (distanceFromLeft - 1) +  r"        l` \`                 \"`._   \"`--' j          j' j          `-`---'")
        print(" " * (distanceFromLeft - 1) +  r"         `  `                     \"`_,-','/       ,-'\"  /")
        print(" " * (distanceFromLeft - 1) +  r"                                 ,'\",__,-'       /,, ,-'")
        print(" " * (distanceFromLeft - 1) +  r"                                 Vvv'            VVv'")
        time.sleep(0.01)
        os.system('cls')  
        distanceFromLeft -= 1
        if distanceFromLeft == 0:
            break
        else:
            os.system('cls')
    deathbyxeno()    

       

# def armory(description):
#     print(f"{description}")
#     input_check(decision, times_table_puzzle, print("Run")) # Called like this NO BRACKETS



def run_away():
    typewriter("""\nYou have chosen to run...""")
    corridor_escape()

def corridor_escape():
    typewriter("\n""""You choose to put as much distance between yourself and whatever darted past your door as quickly as possibly.
You barrel down the corridor, slamming into the tight corners as you go.
From behind, you hear a hurried scurrying slowly morph into a powerful galloping sound.""")
    typewriter2("\n""It's getting closer")
    typewriter("""\n
You run as fast as your legs will carry you.
You round a corner, peering over your shoulder trying to catch a glimpse of the creature chasing you.""")
    print("""
  _______ _    _ _    _ _____  _ 
 |__   __| |  | | |  | |  __ \| |
    | |  | |__| | |  | | |  | | |
    | |  |  __  | |  | | |  | | |
    | |  | |  | | |__| | |__| |_|
    |_|  |_|  |_|\____/|_____/(_)
                                  """)
    typewriter("""\nYou slam into a thick metal blast door and begin to panic as the galloping sound gets louder and louder.
You pick yourself up off the ground and begin mashing at the control panel in a desperate attempt to get the door to open.""")                                  
    time.sleep(5)
    qte()


def outoftime_armory():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
   ____        _            __   _______ _                
  / __ \      | |          / _| |__   __(_)               
 | |  | |_   _| |_    ___ | |_     | |   _ _ __ ___   ___ 
 | |  | | | | | __|  / _ \|  _|    | |  | | '_ ` _ \ / _ |
 | |__| | |_| | |_  | (_) | |      | |  | | | | | | |  __/
  \____/ \__,_|\__|  \___/|_|      |_|  |_|_| |_| |_|\___|""")
                                                          
                                                          

    typewriter("\n""""From behind you, a hurried scurrying begins to slowly morph into a powerful gallop.
Instinctively you turn from the console realising that you don't have any more time to spare and begin to run further down the corridors, slamming into the tight corners as you run.""")
    typewriter2("\n""It's. getting. closer.")
    armory_failure()

def elevator_exit():
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    typewriter("""The elevator reaches the top""")

def corridor_combat():
    os.system('cls' if os.name == 'nt' else 'clear')
    typewriter("""\nIn the connecting corridor, blocking your path there is the grizzly beasty""")
    time.sleep(1)
    battlestate(Player, Xeno)
    input_check(corridor_combat_choice, flight_deck, escape_pod)

def armory_puzzle():
    os.system('cls' if os.name == 'nt' else 'clear')
    typewriter("""On the terminal in front of you appears a personalised security system from the Chief Medical Officer.
Known for his eccentric nature throughout his tenure, you fear what kind of system he may have installed...

The instructions on screen state that the system will ask you to follow on from the opening line of famous classical literature.
How fitting for a man as pompous as the Chief Medical Officer...""")
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(2)
    distanceFromLeft = 0
    print(" " * (distanceFromLeft - 1) +  r"      __...--~~~~~-._   _.-~~~~~--...__")
    print(" " * (distanceFromLeft - 1) +  r"    //               `V'               \\")
    print(" " * (distanceFromLeft - 1) +  r"   //                 |                 \\")
    print(" " * (distanceFromLeft - 1) +  r"  //__...--~~~~~~-._  |  _.-~~~~~~--...__\\")
    print(" " * (distanceFromLeft - 1) +  r" //__.....----~~~~._\ | /_.~~~~----.....__\\")
    print(" " * (distanceFromLeft - 1) +  r"====================\\|//====================")
    print(" " * (distanceFromLeft - 1) +  r"                   `---`")
    time.sleep(2)
    text_answers = [[["Some years ago — never mind how long exactly — having no money to my name,\nand nothing particularly interesting to me on shore,\nI thought I would sail about a while and see a wetter part of the world.\n", 
    "Some years ago — never mind how long precisely — having little or no money in my purse,\nand nothing particular to interest me on shore,\nI thought I would sail about a little and see the watery part of the world.\n", 
    "Some years ago — it doesn't matter how long exactly — having little to no money in my purse,\nand nothing particular to interest me on shore,\nI thought I would sail about a little and see a more watery part of the world.\n", 
    "Some years ago — disregarding how long ago exactly — having little to no money in my purse,\nand nothing particularly interesting to me on shore,\nI thought I would set about seeing a more watery part of the world.\n"], 
    "Some years ago — never mind how long precisely — having little or no money in my purse,\nand nothing particular to interest me on shore,\nI thought I would sail about a little and see the watery part of the world.\n"],
    [["there came through the open door the heavy scent of the lilac, or the more delicate perfume of the pink flowering thorn.\n", 
    "there came through the opened door the heavy scent of lavander, or the more delicate scent of a flowering rose.\n", 
    "there came throughout the open room the heavy scent of lillies, or the more delicate scent of a flowering thorn.\n", 
    "there came throughout the room the heavy scent of lilac, or the more delicate perfume of the pink flowering thorn.\n"], 
    "there came through the open door the heavy scent of the lilac, or the more delicate perfume of the pink flowering thorn.\n"], 
    [["Over many a quaint and curious volume of forgotten lore\nWhile I nodded, nearly napping, suddenly there came a tapping,\nAs of someone gently tapping, tapping at my chamber.\n", 
    "Over many a quaint and queer volume of forgotten lore\nWhile I dipped, drowsily, suddenly there came a tapping,\nAs of someone gently tapping, tapping at my chamber.\n", 
    "Over many a quaint and curious volume of the Silmarillion\nWhile I nodded, nearly napping, suddenly there came a tapping,\nAs of someone gently rapping, rapping at my chamber.\n", 
    "Over many a quaint and curious volume of forgotten lore\nWhile I nodded, nearly napping, suddenly there came a tapping,\nAs of someone gently rapping, rapping at my chamber.\n"], 
    "Over many a quaint and curious volume of forgotten lore\nWhile I nodded, nearly napping, suddenly there came a tapping,\nAs of someone gently rapping, rapping at my chamber.\n"], 
    [["being watched keenly and closely by intelligences greater than man's and yet as mortal as his own;\n", 
    "being watched keenly and closely by an intelligence far greater than man's and yet as mortal as his own;\n", 
    "being watched closely and keenly by several intelligences greater than man's and yet as mortal as his own;\n", 
    "being watched keenly and closely by a certain intelligence greater than man's own; and yet as mortal as his own;\n"], 
    "being watched keenly and closely by intelligences greater than man's and yet as mortal as his own;\n"],
    [["Winston Smith, his chin nuzzled into his breast in an effort to escape the vicous winter wind, slipped quickly through the glass doors of Victory Villa,\n", 
    "Winston Smith, his chin firmly nuzzled into his breast in an attempt to escape the vile wind, slipped quickly through the glass doors of Victory Mansions,\n", 
    "Winston Smith, his chin nuzzled into his breast in an effort to escape the vile wind, slipped quickly through the glass doors of Victory Mansions,\n", 
    "I really wish people that haven't actually read 1984 would stop quoting it on the internet to try and prove their point.\n"], 
    "Winston Smith, his chin nuzzled into his breast in an effort to escape the vile wind, slipped quickly through the glass doors of Victory Mansions.\n"]]


    middle_man = choice(text_answers)
    correct = middle_man[1]
    data = middle_man[0]

    typewriter("""Select the line that follows, inputting 1, 2, 3 or 4:

""")
    time.sleep(2)
    if middle_man == text_answers[0]:
        typewriter("Call me Ishmael.\n")
        typewriter("")
        time.sleep(1)
    elif middle_man == text_answers[1]:
        typewriter("The studio was filled with the rich odour of roses, and when the light summer wind stirred amidst the trees of the garden,\n")
        typewriter("")
        time.sleep(1)
    elif middle_man == text_answers[2]:
        typewriter("Once upon a midnight dreary, as I pondered weak and weary,\n")
        typewriter("")
        time.sleep(1)
    elif middle_man == text_answers[3]:
        typewriter("No one would have believed in the last years of the nineteenth century that this world was\n")
        typewriter("")
        time.sleep(1)
    elif middle_man == text_answers[4]:
        typewriter("It was a bright cold day in April, and the clocks were striking thirteen.\n")
        typewriter("")
        time.sleep(1)

    shuffle(data)

    for count, i in enumerate(data):
        print(f"\n{count+1}: {i}")
        time.sleep(2)
    try:
        answer = inputimeout(prompt="\n>>>   ", timeout=30)
    except TimeoutOccurred:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("""
   ____        _            __   _______ _                
  / __ \      | |          / _| |__   __(_)               
 | |  | |_   _| |_    ___ | |_     | |   _ _ __ ___   ___ 
 | |  | | | | | __|  / _ \|  _|    | |  | | '_ ` _ \ / _ |
 | |__| | |_| | |_  | (_) | |      | |  | | | | | | |  __/
  \____/ \__,_|\__|  \___/|_|      |_|  |_|_| |_| |_|\___|


""")
        typewriter("""
The arbitrary timer has expired and commenced a lockout that can only be bypassed by the Chief Medical Officer himself.
With no where else to go you head out into the corridor towards the navigation deck.""") #Fail condition
        corridor_combat()
    if data[int(answer)-1] == correct:#Win Condition
        
        os.system('cls' if os.name == 'nt' else 'clear')
        print("""
       _____                             _ 
      / ____|                           | |
     | (___  _   _  ___ ___ ___  ___ ___| |
      \___ \| | | |/ __/ __/ _ \/ __/ __| |
      ____) | |_| | (_| (_|  __/\__ \__ \_|
     |_____/ \__,_|\___\___\___||___/___(_)

""") 
        typewriter("""You have successfully input the correct excerpt! 
As the door swings open a smug voice welcomes you into the room...
It's the voice of the Chief Medical Officer... although it is very clearly synthetic...
He used a recording of his own voice to welcome himself to his place of work...
He's even more pompous than you first thought.""")
        os.system('cls' if os.name == 'nt' else 'clear')
        typewriter("""As you enter the Medical bay, the door closes and seals itself behind you. 
While normal procedure for such a room on board your ship, the current situation adds an ominous overtone...
You shake off your trailing thoughts and begin to ransack the room for supplies to help you on your journey.\n""")
        time.sleep(1)
        medbay_interior()


    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("""
  ______    _ _          _ 
 |  ____|  (_) |        | |
 | |__ __ _ _| | ___  __| |
 |  __/ _` | | |/ _ \/ _` |
 | | | (_| | | |  __/ (_| |
 |_|  \__,_|_|_|\___|\__,_|
 
 """) #Fail Condition
        typewriter("""Unfortunately it seems you input the wrong answer and have commenced a lockout on the console that only the Chief Medical Officer's ID can override.
On the screen a mocking message reads... \"What do you only read 50 Shades of Grey? For shame!\"
With no way to continue on your chosen path you head out into the corridor towards the navigation deck""")     
        time.sleep(2)



def qte_failure():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
   ____        _            __   _______ _                
  / __ \      | |          / _| |__   __(_)               
 | |  | |_   _| |_    ___ | |_     | |   _ _ __ ___   ___ 
 | |  | | | | | __|  / _ \|  _|    | |  | | '_ ` _ \ / _ |
 | |__| | |_| | |_  | (_) | |      | |  | | | | | | |  __/
  \____/ \__,_|\__|  \___/|_|      |_|  |_|_| |_| |_|\___|""")
    time.sleep(1)
    typewriter("\nThe sound from behind you speeds up as it gets closer and closer, before you can even turn around...")
    os.system('cls' if os.name == 'nt' else 'clear')
    alien2()
    

def flight_deck():
    os.system('cls' if os.name == 'nt' else 'clear')
    typewriter("""You enter the flight deck, which is seemingly evacuated save for a few stragglers who were either caught by surprise or chose to stay behind.
Sprawled out over a communication terminal is the body of the ship's 2nd in command.
After moving his body from the terminal you begin to flick through important communications to find out what was going on.
Normally you have hidden audiologs or something in a game like this so you are certain there must be something important on this terminal...""")
    time.sleep(2)
    print("""
             __________________________________________________
            /                                                 /
           |    _________________________________________     |
           |   |                                         |    |
           |   |  C:\>run blow_this_thing_up.exe_        |    |
           |   |                                         |    |
           |   |   blow_this_thing_up.exe requires       |    |
           |   |   administrator privileges              |    |
           |   |   Please follow instructions found in   |    |
           |   |   the Captain's Quarters to run         |    |
           |   |   blow_this_thing_up.exe in admin mode  |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |_________________________________________|    |
           |                                                  |
            \_________________________________________________/
                   \___________________________________/
                ___________________________________________
             _-'    .-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.  --- `-_
          _-'.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.--.  .-.-.`-_
       _-'.-.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-`__`. .-.-.-.`-_
    _-'.-.-.-.-. .-----.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-----. .-.-.-.-.`-_
 _-'.-.-.-.-.-. .---.-. .-------------------------. .-.---. .---.-.-.-.`-_
:-------------------------------------------------------------------------:
`---._.-------------------------------------------------------------._.---'""")
    time.sleep(10)
    typewriter("""On this terminal there is information about initiating a self-destruct sequence. The higher-ups must not want whatever those \'things\' are to make it back to earth...
Before making your decision you decide to search the flight deck for additional supplies that may help in the coming challenges\n""")
    loot(Xeno)
    os.system('cls' if os.name == 'nt' else 'clear')
    typewriter("""\nYou gather your thoughts and what information you have up to this point...
You can head to the Captain's quarters in search of information on the self-destruct sequence, or you can head towards the navigation room in search of a way to escape.
You must make a decision:""")
    input_check(flight_deck_choice, captains_quarters, navi_room)

def captains_quarters():
    Player.health = 40
    os.system('cls' if os.name == 'nt' else 'clear')
    typewriter("""
In the Captain's quarters you find a hidden stash of supplies that fully restore your health, Yay!
There is a device on the Captain's table, similar in shape to that of a pen-drive or USB-stick. You're not exactly sure as you have only read about them in history books.
The drive has a sticker on the side that reads 'Deus Ex Machina'.""")
    Player.deus_ex = True
    print("\nYou found a Deus Ex!\n")
    time.sleep(1)
    typewriter("""You figure it may be important so you pocket it and continue to search the room for supplies.\n""")
    loot(Xeno)
    loot(Xeno)
    typewriter("""\nOnce you are certain that the room is well and truly empty you stop for a moment to formulate a plan.
The Captain's quarters are an easily defensible position with a heavy blast door and plenty of things inside that could be used as a make-shift barricade.
While you are not certain of the situation on the ship you are confident that your superior officers would not abandon you, help must be coming, right?
You must make a decision:""")
    input_check(captains_quarters_choice, overrun, navi_room)

def escape_pod_failure():
    typewriter("""
With no flight data installed, your pod ends up splatted against an asteroid like a bug on a windshield.""")
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(2)
    dead()

def escape_pod_success():
    typewriter("You upload the flight data!")
    os.system('cls' if os.name == 'nt' else 'clear')
    typewriter("\nYour pod dips and dashes between rocks, the complex calculations occuring in the auto-pilot are little distraction from the husk of a ship you leave behind.")
    typewriter("\nBut at least you're alive")
    time.sleep(2)
    win()

def escape_pod():
    os.system('cls' if os.name == 'nt' else 'clear')
    typewriter("""You head towards the escape pods...

The many escape pod bays are all empty, save for a lone escape pod at the far end of the room.
Clearly many of the ship's occupants managed to escape but did not think to wake you from your drunken stupor.
You hear hurried scuttling from behind you, so you charge towards the escape pod as quickly as you can and close the pod behind you.
The lone terminal inside the pod displays a large red button.....""")
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
/   /                                     /   /
| O |                                     | O |
|   |- - - - - - - - - - - - - - - - - - -|   |
| O |                                     | O |
|   |                                     |   |
| O |                                     | O |
|   |                                     |   |
| O |                                     | O |
|   |            E N G A G E              |   |
| O |                                     | O |
|   |               P O D                 |   |
| O |                                     | O |
|   |                                     |   |
| O |                                     | O |
|   |                                     |   |
| O |                                     | O |
|   |                                     |   |
| O |- - - - - - - - - - - - - - - - - - -| O |
|   |                                     |   |""")
    time.sleep(2)
    if Player.flight_data == True:
        escape_pod_success()  
    else:
        escape_pod_failure()



def navi_puzzle():

    symbols = ["0", "1", " ", " "]
    line = []
    counter = 0
    for i in range(118):
        x = random.randint(0, 3)
        line.append(symbols[x])
    
        counter += 1

    for i in range(300):

        if counter % 5 == 0:
            r_symbols = [random.randint(0, 117) for x in range(10)]

            for i in r_symbols:
                line[i] = symbols[random.randint(0, 3)]

        print(*line)
        counter += 1
        time.sleep(0.01)

    os.system('cls')

    counter = 0
    answer = "" 
    numbers = []
    operators = ["a", "s", "m"]
    seq = []

    for i in range(1,3):
        numbers.append(random.randint(1, 12))

    c_op = random.choice(operators)
    seq.append(numbers[0])

    if c_op == "a":
        for i in range(1, 7):
            seq.append(seq[-1] + numbers[1])
    elif c_op == "s":
        for i in range(1, 7):
            seq.append(seq[-1] - numbers[1])
    elif c_op == "m":
        numbers[1] = random.randint(1, 4)
        for i in range(1, 7):
            seq.append(seq[-1] * numbers[1])
    
    while answer != str(seq[5]):
        try:
            answer = inputimeout(prompt=f"What is the next number in this sequence? " + str(seq[0:5]), timeout=10)
            if answer.isdigit and answer != str(seq[5]):
                print("Try Again")
                counter += 1
            elif answer != str(seq[5]):
                print("Must be a number!")
                counter += 1
            if counter > 1:
                print(f"The correct answer was, {seq[5]}. Bet you never thought you'd use GCSE Maths again right?")
                sleep.time(2) # Fail condition (too many attempts)#######Fail Text goes here, write a paragraph you lazy git
                failed_navigation_puzzle()
                break
        except TimeoutOccurred:
            print(f"The correct answer was, {seq[5]}. Bet you never thought you'd use GCSE Maths again right?")
            failed_navigation_puzzle()
            break
    print("You received the Flight Data!")
    time.sleep(1)
    Player.flight_data = True
    escape_pod()#######win text goes here something about downloading flight data



# def navi_puzzle():
#     symbols = ["0", "1", " ", " "]
#     line = []
#     counter = 0
#     for i in range(118):
#         x = random.randint(0, 3)
#         line.append(symbols[x])
    
#         counter += 1

#     for i in range(300):

#         if counter % 5 == 0:
#             r_symbols = [random.randint(0, 117) for x in range(10)]

#             for i in r_symbols:
#                 line[i] = symbols[random.randint(0, 3)]

#         print(*line)
#         counter += 1
#         time.sleep(0.01)

#     os.system('cls')

#     counter = 0
#     answer = "" 
#     numbers = []
#     operators = ["a", "s", "m"]
#     seq = []

#     for i in range(1,3):
#         numbers.append(random.randint(1, 12))

#     c_op = random.choice(operators)
#     seq.append(numbers[0])

#     if c_op == "a":
#         for i in range(1, 7):
#             seq.append(seq[-1] + numbers[1])
#     elif c_op == "s":
#         for i in range(1, 7):
#             seq.append(seq[-1] - numbers[1])
#     elif c_op == "m":
#         numbers[1] = random.randint(1, 4)
#         for i in range(1, 7):
#             seq.append(seq[-1] * numbers[1])
    
#     while answer != str(seq[5]):
#         try:
#             answer = inputimeout(prompt=f"What is the next number in this sequence? " + str(seq[0:5]), timeout=10)
#             if answer.isdigit and answer != str(seq[5]):
#                 print("Try Again")
#                 counter += 1
#             elif answer != str(seq[5]):
#                 print("Must be a number!")
#                 counter += 1
#             if counter > 1:
#                 print(f"The correct answer was, {seq[5]}. Bet you never thought you'd use GCSE Maths again right?")
#                 sleep.time(2) # Fail condition (too many attempts)#######Fail Text goes here, write a paragraph you lazy git
#                 failed_navigation_puzzle()
#                 break
#         except TimeoutOccurred:
#             print(f"The correct answer was, {seq[5]}. Bet you never thought you'd use GCSE Maths again right?")
#             failed_navigation_puzzle() # Fail condition here too (ran out of time)############ same as above but with time
#             break
#     print("You received the Flight Data!")
#     time.sleep(1)
#     Player.flight_data = True
#     escape_pod()#######win text goes here something about downloading flight data
    
def elevator_failure():
    os.system('cls' if os.name == 'nt' else 'clear')
    typewriter("""You lock yourself out of the elevator console with your inability to balance the equation.
In the mean time you search the room for supplies.
A failed yet confident attempt at repurposing a fuel cell results in you decorating most of the room with your innards""")
    dead()

def overrun():
    typewriter("""You have chosen to hunker down...

You barricade the door and attempt to outlast whatever disaster has taken hold of the ship.
It's not long before you are discovered by the first monster and the proceeding fight produces enough sound that eventually more and more of these creatures are throwing themselves against your barricade.
In the brief moment before your death you wonder whether it was the right decision to place faith in your superiors in a corrupt capitalist society...""")
    deathbyxeno()

def navi_room2():
    os.system('cls' if os.name == 'nt' else 'clear')
    if Player.deus_ex == True:
        typewriter("""You possess the self-destruct codes.
In order to use them you'll need to head down to the reactor and initiate the sequence manually...
You must make a decision:\n""")
        input_check(deus_ex_choice, navi_room3, reactor_combat)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    
def navi_room():
    if Player.deus_ex == True:
        navi_room2()
    os.system('cls' if os.name == 'nt' else 'clear')
    naviroom3()
    
def navi_room3():    
    typewriter("""
In the navigation room there is a sea of overly-complex terminals written exclusively in Java Script code, the preferred language of the haggered middle-aged software developer.
With no understanding of Javascript because you were always too busy having friends and happiness in your life to bother learning it you have to input the raw code
into your magical machine thingy and decipher a way to download the auto-pilot flight data required to leave the asteroid field your ship was mining.
You're not quite sure how this machine works but you don't have enough time to get bogged down in context""")
    navi_puzzle()

def failed_navigation_puzzle():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""\n

  ______    _ _          _ 
 |  ____|  (_) |        | |
 | |__ __ _ _| | ___  __| |
 |  __/ _` | | |/ _ \/ _` |
 | | | (_| | | |  __/ (_| |
 |_|  \__,_|_|_|\___|\__,_|""")
    time.sleep(2)
    typewriter("""You failed to access the flight data for the escape pods.
A siren begins to ring out throughout the room.
A synthetic voice announces repeatedly 'UNAUTHORIZED ACCESS, UNAUTHORIZED ACCESS'...
Rather than stick around and find out what is going to investigate the noise you start to running.
You must make a decision:\n""")
    input_check(navi_puzzle_failure_choice, escape_pod, reactor_combat)
    




  
  ################### ending graphic would go here.CONTINUE




def armory_failure():
    print("\n"*3)
    typewriter3("""You continue running, seemingly faster than you have ever ran before, 
beads of sweat forming and falling from your face as you move as fast as your legs will carry you.
Your lungs begin to burn as the galloping sound creeps closer and closer.
You are not sure where you are heading, and it becomes apparent you cannot outrun whatever it is that is chasing you.""")
    typewriter("\n"*3)
    typewriter("""You round the next corner and resign yourself to having to fight whatever it is that is chasing you, when out of the corner of your eye you spot a large ventilation grill.
With no time to think you simply swing open the grill panel and dive inside...
You cannot catch your breath, nor process a thought in your panicked state, but at least you are alive, for now.
Mere seconds after you throw yourself into the vent, whatever was chasing you barrels round the corner, gurgling and hissing as it goes, yet you remain unnoticed.
Now situated directly beneath the metal flooring and seemingly safe your mind begins to overflow with a plethora of plans, proposals and postulations.
You decide to take your chances and see where this ventilation shaft leads...
As you continue down the shaft, through the various grates and grids you begin to get a grasp on where you are.
However, between where you are, and where you want to be there is a rather large obstacle that you are most certainly not a fan of.""")
    time.sleep(2)
    wire_cut_puzzle()
                                 

def input_check(description, action1, action2):
    
    typewriter(f"{description}")
    choice = input()
    if choice.upper() == "A":
        os.system('cls' if os.name == 'nt' else 'clear')
        action1()
    elif choice.upper() == "B":
        os.system('cls' if os.name == 'nt' else 'clear')
        action2()
    else:
        print("Please choose A or B.")
        input_check(description, action1, action2)
    choice = ""

# #########SUCCESS########
def armory_interior():
    if Player.key_card == True:
        os.system('cls' if os.name == 'nt' else 'clear')
        typewriter("You swipe the keycard over the security panel.")
        time.sleep(1)

    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
       _____                             _ 
      / ____|                           | |
     | (___  _   _  ___ ___ ___  ___ ___| |
      \___ \| | | |/ __/ __/ _ \/ __/ __| |
      ____) | |_| | (_| (_|  __/\__ \__ \_|
     |_____/ \__,_|\___\___\___||___/___(_)""")
    print("\n"*3)
    typewriter("\n""""After successfully disabling the security system to the armory, the heavy blast door swings open. As the door connects with the wall behind it
a metallic clang is sent echoing down the hall.
A sudden scurrying and a moist gurgling sound soon follow as the clang rings out.
Whatever it was that you saw run past your door is now almost certainly aware of your presence.....
You scarper through the door, slamming it shut behind you. The magnetic lock on the door allows you a brief respite to search the room for supplies.\n""")
    loot(Xeno)
    loot(Xeno)
    typewriter("\n""""After composing yourself and doing one last inventory check you decide to press on.
Directly in front of you is the corridor that leads to navigation and the escape pods, and to your left is the security locked med bay.
You must make a decision:""")
    input_check(armory_choice2, corridor_combat, armory_puzzle)


def multiply_puzzle():
    os.system('cls' if os.name == 'nt' else 'clear')
    typewriter("\n""""Next to the heavy blast door securing the armory there is a small security keypad.
This keypad will generate random, simple multiplications that need to be input before a timer locks you out for a set amount of time.
You ponder momentarily about who or what this security system is designed to stop...""")
    time.sleep(2)
    print("\n")
    print(r" _____________________")
    print(r"|  _________________  |")
    print(r"| | JO           0. | |")
    print(r"| |_________________| |")
    print(r"|  ___ ___ ___   ___  |")
    print(r"| | 7 | 8 | 9 | | + | |")
    print(r"| |___|___|___| |___| |")
    print(r"| | 4 | 5 | 6 | | - | |")
    print(r"| |___|___|___| |___| |")
    print(r"| | 1 | 2 | 3 | | x | |")
    print(r"| |___|___|___| |___| |")
    print(r"| | . | 0 | = | | / | |")
    print(r"| |___|___|___| |___| |")
    print(r"|_____________________|")

    print("\n")

    number1 = []
    answer = 500

    for i in range(0, 10):
        number1.append(random.randint(0, 12))

    for i in range(1, 6):
        try:
            while answer != str(number1[i] * number1[i+1]) and i != 6:                 # Loop checks contents of 'ans' against multiplied list elements.

                answer = inputimeout(prompt=f"{number1[i]} x {number1[i+1]}=", timeout=5)
            
                if answer.isdigit() and answer != str(number1[i] * number1[i+1]):                       # If statement handles errornous input.
                    print("Try Again")
                elif answer != str(number1[i] * number1[i+1]):
                    print("Must be a number!")
        except TimeoutOccurred:
                outoftime_armory() # Replace with fail condition
                i = 6
                break

    armory_interior()   # Win conditon here   

def qte():
    os.system('cls' if os.name == 'nt' else 'clear')
        
        
    print("Mash A followed by Enter to open the door in time.")
    time.sleep(2)
    distanceFromLeft = 10
    print(" " * (distanceFromLeft - 1) +  r"   _________")
    print(" " * (distanceFromLeft - 1) +  r"  |\_______/|")
    print(" " * (distanceFromLeft - 1) +  r"  ||   ____||")
    print(" " * (distanceFromLeft - 1) +  r"  ||  /    \|")
    print(" " * (distanceFromLeft - 1) +  r"  ||_||    ||")
    print(" " * (distanceFromLeft - 1) +  r"  |/_||____||")
    print(" " * (distanceFromLeft - 1) +  r"     |      |")
    print(" " * (distanceFromLeft - 1) +  r"     |      |")
    print(" " * (distanceFromLeft - 1) +  r"     | .... |")
    print(" " * (distanceFromLeft - 1) +  r"     | ---- |")
    print(r"")

    t = 10      #timer counter
    inputs = []

    print("Press A then Enter rapidly to mash the button repeatedly:")

    while len(inputs) < 20:     #Loop to count 20 inputs
        try:
            press = inputimeout(prompt="", timeout=t)   #Takes inputs with decreasing timer
            inputs.append(press)        #Stores input to be counted
            t -= 0.5        #Adjust timer
        except TimeoutOccurred:
            qte_failure() #replace with fail condition
            break

    time.sleep(1)
    while kbhit(): getch() # consume any pending keypresses
    qte_success()

def elevator_success():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""

   _____                             _ 
  / ____|                           | |
 | (___  _   _  ___ ___ ___  ___ ___| |
  \___ \| | | |/ __/ __/ _ \/ __/ __| |
  ____) | |_| | (_| (_|  __/\__ \__ \_|
 |_____/ \__,_|\___\___\___||___/___(_)""")
    typewriter("""
The elevator doors slide open, allowing you access to the upper decks.
You enter the elevator, and press the lone button inside.
The doors shut, the room shakes unexpectedly, then stands perfectly still for what seems like an eternity...
Suddenly the whole room around you jerks to life as the elevator shoots up to the upper decks.""")
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')
    typewriter("""The elevator reaches it's destination and the doors slide open revealing the connecting corridor between the sealed navigation rooms and the escape pods.
However there is a much more immediate obstacle in your way...""")
    time.sleep(2)
    corridor_combat()


def qte_success():
    time.sleep(1)
    if Player.key_card == True:
        os.system('cls' if os.name == 'nt' else 'clear')
        typewriter("""\n
After defeating the Crazed Software Engineer and realising that the mechanism to the door he was guarding was damaged in the previous fight, 
you turn back on yourself and consider once more which way to go. 
You can freely access the armory, or you can use the keycard to open the way into the armory.
You must make a decision:\n""")
        input_check(qte_choice2, armory_interior, carry_on)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""

   _____                             _ 
  / ____|                           | |
 | (___  _   _  ___ ___ ___  ___ ___| |
  \___ \| | | |/ __/ __/ _ \/ __/ __| |
  ____) | |_| | (_| (_|  __/\__ \__ \_|
 |_____/ \__,_|\___\___\___||___/___(_)""")
    time.sleep(3)
    while kbhit(): getch()
    typewriter("""
The door slides upwards just enough for you to slide under and close it behind yourself.
Shortly after closing, there is a large impact against the door, but for now, it holds...

You are now on the other side of the large blast door. You are still not sure what it was that was chasing you, but you have faith in your good friend Blasty Mcblastdoor.
There is an alternate route into the armoury from this corridor, although it will require a key card. With a good few centimetres of solid blast door between you and that thing you can take a moment
to catch your breath and think about your options...
You must make a decision:\n""")
    input_check(qte_choice, software_engineer, carry_on)   


def carry_on():
    os.system('cls' if os.name == 'nt' else 'clear')
    typewriter("""You decide to press on in search of your comrades in the lower decks...
    
The twisting corridors seem to go on for miles.
As you trudge through various parts of former comrades in search of survivors, a thought occurs to you.
Given the ferocity of the hostile entities, and the scenes they leave behind, you find it odd that there would be many survivors... and yet...
The thought strikes you like a bolt of lightning; there doesn't seem to be any of the higher ranking officers among the corpses.
They must be holding out in the upper decks or have used the escape pods. Still, the disproportionate amount of officers missing suggests something odd.
You shake the thought from your head and continue on...

Eventually you find yourself in the engine room. Scorch marks decorate the room around you.
There doesn't seem to be much in the way of supplies here as the corpses around you would indicate most things were used as make-shift weapons, unfortunately to very little effect.
There is an emergency elevator tucked away in the side of the room that leads to the upper decks.
During emergencies this elevator is sealed to prevent it's use, but you are confident in your ability to override it.
You walk on over to the elevator:
""")
    time.sleep(2)
    elevator()


def medbay_vent():
    os.system('cls' if os.name == 'nt' else 'clear')
    typewriter("""You blast the grate off of it's rivets with a powerful kick.
The heavy grill falls to the ground with a mighty crash likely announcing your presence to everyone or everything in this section of the ship.
You climb out of the vent and notice the supply cabinets stuffed with various supplies, stimulants and medical equipment.""")
    medbay_interior()

def medbay_interior():    
    ######################## looty bit goes here##########
    loot(Xeno)
    os.system('cls' if os.name == 'nt' else 'clear')
    typewriter("""\n
As soon as you are done loading yourself up with a cocktail of stimulants and stuffing the extra supplies into a backpack found by the door,
you begin to look around the room and attempt to formulate a plan.
Your thoughts are quickly interupted by loud scratching against the door that leads to the armory.
You walk towards the heavy blast door to investigate and are met with a loud thud against it.
The thudding and thumping against the door increases in ferocity as the door begins to groan and bend under each impact.
You need to leave.
You must make a decision:\n""")
    input_check(medbay_choice, vent_puzzle, medbay_choice)

def medbaychoice():
    os.system('cls' if os.name == 'nt' else 'clear')
    typewriter("""
You try to leave via several of the med bay's exits, but are met at every door by the same loud thudding noise.
After circling the exits you notice that the door leading directly to the flight deck is the only exit that is relatively quiet.
Obvious choice.
You leap over the table that seperates you and the door and begin to frantically interact with the panel.
""")
    ana_puzzle()



def vent_puzzle():
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')
    typewriter("""After crawling through the vents aimlessly for a short while, you are taken by surprise when you suddenly hit a short but steep decline. 
After sliding down no more than a few feet you realise that you are now in the section of the ventilation system above the officers quarters. 
A unique ventilation system designed by the infamous Konami company for the privileged officers, these ventilation systems
are known for their efficiency and for following a very unique yet similar layout.
You must navigate the maze...""")
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system('cls')
    pos = [0, 1]
    solution = ["W", "W", "S", "S", "A", "D", "A", "D"]

    def tracking():

        global space

        space = ["---", "---", "---"]
        
        if pos[0] == 0 and pos[1] == 0:
            space[0] = "X??"
            space[1] = "???"
            space[2] = "???"
        elif pos[0] == 0 and pos[1] == 1:
            space[0] = "?X?"
            space[1] = "???"
            space[2] = "???"
        elif pos[0] == 0 and pos[1] == 2:
            space[0] = "??X"
            space[1] = "???"
            space[2] = "???"
        elif pos[0] == 1 and pos[1] == 0:
            space[0] = "???"
            space[1] = "X??"
            space[2] = "???"
        elif pos[0] == 1 and pos[1] == 1:
            space[0] = "???"
            space[1] = "?X?"
            space[2] = "???"
        elif pos[0] == 1 and pos[1] == 2:
            space[0] = "???"
            space[1] = "??X"
            space[2] = "???"
        elif pos[0] == 2 and pos[1] == 0:
            space[0] = "???"
            space[1] = "???"
            space[2] = "X??"
        elif pos[0] == 2 and pos[1] == 1:
            space[0] = "???"
            space[1] = "???"
            space[2] = "?X?"
        elif pos[0] == 2 and pos[1] == 2:
            space[0] = "???"
            space[1] = "???"
            space[2] = "??X"

    def show_map():
        print (f" {space[2][0]} {space[2][1]} {space[2][2]} ")
        print (f" {space[1][0]} {space[1][1]} {space[1][2]} ")
        print (f" {space[0][0]} {space[0][1]} {space[0][2]} ")

    def choice():   #get a valid choice from the user
        
        dir1 = ["W", "A", "S", "D"]
        steps = []

        for i in range(0, 8):
            userChoice = input('Choose a direction (WASD)=(↑←↓→):')
            userChoice = userChoice.upper()

            if userChoice in dir1:
                if userChoice == "W":
                    pos[0] += 1
                if userChoice == "A":
                    pos[1] -= 1
                if userChoice == "S":
                    pos[0] -= 1
                if userChoice == "D":
                    pos[1] += 1
            else:
                print ('Invalid choice. Try again.')
                choice()

            steps.append(userChoice)
            
            if steps[i] == solution[i] and i > 7:
                vent_puzzle_success() #win condition here
            elif steps[i] != solution[i]:
                vent_puzzle_fail()
                break
            
            tracking()
            show_map()

    tracking()
    show_map()
    choice()

def ana_fail():
    print("""
  ______    _ _          _ 
 |  ____|  (_) |        | |
 | |__ __ _ _| | ___  __| |
 |  __/ _` | | |/ _ \/ _` |
 | | | (_| | | |  __/ (_| |
 |_|  \__,_|_|_|\___|\__,_|""")
    typewriter("""

The screen flashes for a brief moment before displaying a lockout screen stating you must try again in 5 minutes.
What an arbitrary timeout you think to yourself, before making a dash for the only other exit in the room... the ventilation system.
Sprinting across the room, ploughing through various bits of furniture and medical equipment, you dive into the ventilation system.""")
    time.sleep(5)
    vent_puzzle()


def ana_success():
    print("""

   _____                             _ 
  / ____|                           | |
 | (___  _   _  ___ ___ ___  ___ ___| |
  \___ \| | | |/ __/ __/ _ \/ __/ __| |
  ____) | |_| | (_| (_|  __/\__ \__ \_|
 |_____/ \__,_|\___\___\___||___/___(_)""")
    typewriter("""
    
The door to the flight deck swings open, as if beckoning you forward.
The flight deck door being of a higher security class almost guarantees that nothing can follow you through it...
At least for now.""")
    flight_deck()

def ana_puzzle():
    typewriter("""\nA familiar face appears on the screen before you.
The ships AI assistant asks for proof that you are not a robot by passing a captcha check.
After selecting all the images with traffic lights in them you are presented with a jumbled string of letters that the AI wishes you to unscramble. 
It seems this AI has a penchant for anagrams.\n""")
    time.sleep(2)
    distanceFromLeft = 0
    print(" " * (distanceFromLeft - 1) +  r"                         \\\\\\\\|/////\ ")
    print(" " * (distanceFromLeft - 1) +  r"                         \\\\\\\\\|//////\ ")
    print(" " * (distanceFromLeft - 1) +  r"                          \\\\\\\\I////////\ ")
    print(" " * (distanceFromLeft - 1) +  r"                           \\\\\\\I//////////\ ")
    print(" " * (distanceFromLeft - 1) +  r"                           \IIIIII\I\//////////\ ")
    print(" " * (distanceFromLeft - 1) +  r"                             /****/*\////////////\ ")
    print(" " * (distanceFromLeft - 1) +  r"                            /****/***\////////////\ ")
    print(" " * (distanceFromLeft - 1) +  r"                           /****/*****|////////////|")
    print(" " * (distanceFromLeft - 1) +  r"                J$$$$$$$$$$$$$$$******\////////////|")
    print(" " * (distanceFromLeft - 1) +  r"             J$$***************$$$$$***|///////////")
    print(" " * (distanceFromLeft - 1) +  r"            $$**********************$$L. \\\\\\\\\/")
    print(" " * (distanceFromLeft - 1) +  r"          .$***************************$$L")
    print(" " * (distanceFromLeft - 1) +  r"       .J$$$$$$$$$************************$L")
    print(" " * (distanceFromLeft - 1) +  r"     .J$$*********$$$$$$$$$$$***************$$")
    print(" " * (distanceFromLeft - 1) +  r"  J$$$***********************$$$$$$$$*********$")
    print(" " * (distanceFromLeft - 1) +  r" $$**********************************$$$$$$$***$")
    print(" " * (distanceFromLeft - 1) +  r" $*****************************************$$$$$")
    print(" " * (distanceFromLeft - 1) +  r"  $********$$$$$$*************************$***$$")
    print(" " * (distanceFromLeft - 1) +  r"  $******$$$$$$$$$$$$$$$$$$$$************$*****$$")
    print(" " * (distanceFromLeft - 1) +  r"   $**$$$$ $$$$$$$$$$$$$$$$$ $$$$$$$$****$******$")
    print(" " * (distanceFromLeft - 1) +  r"    ~~ $$$    %%$$$$$$$%%    $$$$$$$$$$$$$$****$")
    print(" " * (distanceFromLeft - 1) +  r"        $$$   %%  $$$  %%   $$$$$$$$$$$$$$*#$$*$")
    print(" " * (distanceFromLeft - 1) +  r"        $$$       $$$      $$$$$$$$$$$$$$*#****$")
    print(" " * (distanceFromLeft - 1) +  r"        $$$$$    $$$$$    $$$$$$$$$$$$$*#*****$")
    print(" " * (distanceFromLeft - 1) +  r"       $&&$$$$$$$$$$$$$$$$$$$$$$$$$$%**##*****$")
    print(" " * (distanceFromLeft - 1) +  r"      $&&&&&$$$$$$$$$$$$$$$$$$$$$$$%**#******$")
    print(" " * (distanceFromLeft - 1) +  r"     $&&&&&&&$$$$$$$$$$$$$$$$$$$$$$#########$  ---< Where's the ANAGRAMS?")
    print(" " * (distanceFromLeft - 1) +  r"    $&&&&&&&&&&% ~T$$$$$$$$$$$$$$T~********$        There was suppose to")
    print(" " * (distanceFromLeft - 1) +  r"    $&&&&&&&&T'       OOOOOOOOOOOO********$        be an earth-shattering")
    print(" " * (distanceFromLeft - 1) +  r"                    OOOOOOOOOOOOOOOO                     ANAGRAM!")
    print(" " * (distanceFromLeft - 1) +  r"                   OOOOOOOOOOOOOOOOOOO")
    print(" " * (distanceFromLeft - 1) +  r"                 OOOOOOOOOOOOOOOOOOOOOO ")
    print(" " * (distanceFromLeft - 1) +  r"                OOO/OOOOOOOOOOOOO/OOOOOO")
    print(r"")


    answer = ""
    counter = 0
    words = ["alien", "rocket", "planet", "asteroid", "galaxy", "pulsar", "nebula", "gravity", "wormhole", "satellite", "vacuum"]

    chosen = random.choice(words)

    def scramble(word):
        s_as_l = list(chosen)
        random.shuffle(s_as_l)
        return ''.join(s_as_l)

    while answer != chosen:
        answer = input("Rearrange these letters to make a word: " + scramble(chosen) + " ")
        if answer == chosen:
            ana_success() #Replace with win condition
        else:
            print("Try Again")
            counter += 1
        
        if counter > 1:
            ana_fail #Replace with fail condition
            break

def wire_cut_puzzle():
    os.system('cls' if os.name == 'nt' else 'clear')
    distanceFromLeft = 0
    wire_sol = ["C", "A", "B"]
    wire_choice = ""
    typewriter("\n""""In front of you is the fuse box that controls the large fan that is preventing you from progressing down this ventiliation shaft.""""\n")
    print(" " * (distanceFromLeft - 1) +  r"             .--------------.")
    print(" " * (distanceFromLeft - 1) +  r"          ___|  _  _  _  _  |____________________________")
    print(" " * (distanceFromLeft - 1) +  r"         /   |  || || || ||_|___             _      _   /;")
    print(" " * (distanceFromLeft - 1) +  r"        /.--------------.      /|___       +(_)    (/) //")
    print(" " * (distanceFromLeft - 1) +  r"       / |  _  _  _  _  |     / ___ \      _  OUT     //")
    print(" " * (distanceFromLeft - 1) +  r"      /  |  || || || || |____/ ___ \(\)  -(_)        //")
    print(" " * (distanceFromLeft - 1) +  r"     /   |  || || || || |    | /  \(\)   _          //")
    print(" " * (distanceFromLeft - 1) +  r"    /    |______________|____|/   (\)  -(_)        //")
    print(" " * (distanceFromLeft - 1) +  r"   / _                                 _  BAT _   //")
    print(" " * (distanceFromLeft - 1) +  r"  / (\) MJP                          +(_) 9v (=) //")
    print(" " * (distanceFromLeft - 1) +  r" /______________________________________________//")
    print(" " * (distanceFromLeft - 1) +  r" `----------------------------------------------'")
    
    typewriter("""There is a small poster situated above it with instructions on how to deactivate the fan.
Cut the wires in this order:
Periwinkle,
Vermillion,
Viridian,
Any other combination will cause the fan to malfunction.
After pondering the sesquipedalian altiloquence of it's designer for a moment, you turn towards the circuitry in an attempt to understand the instructions""""\n")
    print("""You are presented with 3 wires: 
A = Red, B = Green and C = Blue.""")
    print("\n")

    wire_choice = input("Which wire will you cut? ")

    if wire_choice.capitalize() != wire_sol[0]:
        fan_malfunction() # replace
    else:
        wire_choice = input("Which wire will you cut next? ")

        if wire_choice.capitalize() != wire_sol[1]:
            fan_malfunction() # replace
        else:
            wire_choice = input("Which wire will you cut next? ")

            if wire_choice.capitalize() != wire_sol[2]:
                fan_malfunction() # replace
    
    fan_success()      # Replace with real next step.


def fan_success():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
       _____                             _ 
      / ____|                           | |
     | (___  _   _  ___ ___ ___  ___ ___| |
      \___ \| | | |/ __/ __/ _ \/ __/ __| |
      ____) | |_| | (_| (_|  __/\__ \__ \_|
     |_____/ \__,_|\___\___\___||___/___(_)""")
    print("\n"*3)
    typewriter("""You successfully disabled the fan and were able to proceed down the ventilation shaft.
With a few more twists, turns, unders and overs, you find yourself positioned directly above the med bay, peering through the thin metal grate blocking your way.
The grate is sealed shut from this side and while you are confident you can kick it through, you are aware that the noise will likely alert any nearby hostile entity.
You notice that the room looks almost untouched for a medical bay on a ship in the middle of such a crisis,
it is likely that the room is well stocked with supples.
You must make a decision:""")
    input_check(vent_choice, medbay_vent, vent_puzzle)                                     
                                       

                                       
                                       
 
                                       


def intro():
    introanim()
    os.system('cls' if os.name == 'nt' else 'clear')
    character_name = input("Please enter your name: ")
    os.system('cls' if os.name == 'nt' else 'clear')
    typewriter(f"Hello, {character_name}")
    time.sleep(2)

#     typewriter("\n""You awaken in a groggy haze and attempt to piece together your fragmented consciousness.")

#     time.sleep(2)

#     typewriter(f"\n"'''Before you can fully adjust yourself to your newly discovered 'Galactic hangover',
# you are snapped to your senses by a blood-curdling screech that reverberates throughout your entire body.''')
#     playsound("scream.wav")
#     time.sleep(2)
#     ##########################################################put monster scream/graphics or animations here
#     typewriter("\n"*3)
#     typewriter(f'''Trembling, you timidly traverse the room, navigating the maze of hastily evacuated bunkbeds.
# As you move towards the only exit in the room, your gaze remains fixated upon the malfunctioning mechanical door that separates the crew quarters from the connecting corridor.''')
#     typewriter2("\n""Open. Shut. Open. Shut. Open. Shut.")
#     time.sleep(2)
#     ###########################################################scream animation again
#     os.system('cls' if os.name == 'nt' else 'clear')
#     alien()
#     typewriter("\n"'''An amorphous mass of black, leathery flesh darts past the door, heading deeper into the crew quarters.
# Without realising it, you suddenly find yourself with your hand upon the door, preventing it from moving.
# You brace yourself, mustering what courage you can before throwing yourself into seemingly certain death.''')
#     typewriter2("\n""...")
#     typewriter("\n"'''Upon entering the corridor your senses are assaulted by a scene of overwhelming primal carnage.
# A sea of your former comrades fills the corridor. 
# As you take one last deep breath to compose yourself and formulate a plan, the familiar combination of potassium nitrate and blood washes over you.
# You must make a decision:''')
    input_check(armory_choice, multiply_puzzle, run_away)



playerart = """                      ______
                   ,-~   _  ^^~-.,
                 ,^        -,____ ^,         
                /           (____)  |      
               ;  .---._    | | || _|     
               | |      ~-.,\ | |!/ |     
               ( |    ~<-.,_^\|_7^ ,|     
               | |      ", 77>   (T/|   
               |  \_      )/<,/^\)i(|
               (    ^~-,  |________||
               ^!,_    / /, ,'^~^',!!_,..---.
                \_ "-./ /   (-~^~-))' =,__,..>-,
                  ^-,__/#w,_  '^' /~-,_/^\      )
               /\  ( <_    ^~~--T^ ~=, \  \_,-=~^\ 
  .-==,    _,=^_,.-"_  ^~*.(_  /_)    \ \,=\      )
 /-~;  \,-~ .-~  _,/ \    ___[8]_      \ T_),--~^^)
   _/   \,,..==~^_,.=,\   _.-~O   ~     \_\_\_,.-=}
 ,{       _,.-<~^\  \ \\      ()  .=~^^~=. \_\_,./
,{ ^T^ _ /  \  \  \  \ \)    [|   \ih8code>
  ^T~ ^ { \  \ _\.-|=-T~\\    () ()\<||>,' )
   +     \ |=~T  !       Y    [|()  \ ,'  / """

def player_animation():
    print(playerart)

begin = "\nWe hope you enjoy our game. Team 6: Danny C and Tom S"
def introanim():
    global begin
    distanceFromLeft = 0
    while distanceFromLeft <= 30:
        print(r"     ___       __       __   _______ .__   __.         ______   ______   ____    ____  __   _______      __       _______.  ______    __          ___   .___________. __    ______   .__   __. ")
        print(r"    /   \     |  |     |  | |   ____||  \ |  |  _     /      | /  __  \  \   \  /   / |  | |       \    |  |     /       | /  __  \  |  |        /   \  |           ||  |  /  __  \  |  \ |  | ")
        print(r"   /  ^  \    |  |     |  | |  |__   |   \|  | (_)   |  ,----'|  |  |  |  \   \/   /  |  | |  .--.  |   |  |    |   (----`|  |  |  | |  |       /  ^  \ `---|  |----`|  | |  |  |  | |   \|  | ")
        print(r"  /  /_\  \   |  |     |  | |   __|  |  . `  |       |  |     |  |  |  |   \      /   |  | |  |  |  |   |  |     \   \    |  |  |  | |  |      /  /_\  \    |  |     |  | |  |  |  | |  . `  | ")
        print(r" /  _____  \  |  `----.|  | |  |____ |  |\   |  _    |  `----.|  `--'  |    \    /    |  | |  '--'  |   |  | .----)   |   |  `--'  | |  `----./  _____  \   |  |     |  | |  `--'  | |  |\   | ")
        print(r"/__/     \__\ |_______||__| |_______||__| \__| (_)    \______| \______/      \__/     |__| |_______/    |__| |_______/     \______/  |_______/__/     \__\  |__|     |__|  \______/  |__| \__| ")
        print("\n")
        print(" " * distanceFromLeft + r"___________________          _-_")
        print(" " * distanceFromLeft + r"\__(==========/_=_/ ____.---'---`---.____")
        print(" " * distanceFromLeft + r"            \_ \    \----._________.----/")
        print(" " * distanceFromLeft + r"              \ \   /  /    `-_-'")
        print(" " * distanceFromLeft + r"          __,--`.`-'..'-_")
        print(" " * distanceFromLeft + r"         /____          ||")
        print(" " * distanceFromLeft + r"             `--.____,-'")
        time.sleep(0.1)  
        distanceFromLeft += 1
        if distanceFromLeft == 30:
            distanceFromLeft = 0
            typewriter(begin)
            time.sleep(2)
            return
        else:
            os.system('cls')







########initiate here
intro()
###################


