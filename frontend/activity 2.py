import wave, sys, time, random, os, winsound, getpass, hashlib
from random import shuffle, choice
from inputimeout import inputimeout, TimeoutOccurred
from playsound import playsound
from getpass import getpass
from msvcrt import getch,kbhit

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

def try_again():
    quiz_game()

def quiz_game():
    os.system('cls' if os.name == 'nt' else 'clear')
    typewriter("""""")
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
    text_answers = [[["We got one!\n", 
    "We got one!\n", 
    "We gots one!\n", 
    "We have one!\n"], 
    "We've got him.\n"],
    [["Ghostbusters!\n", 
    "Your local council!\n", 
    "Nigel!\n", 
    "Bill Murray!\n"], 
    "Ghostbusters!\n"], 
    [["I feel so slimy.\n", 
    "I feel so funky.\n", 
    "I feel so disgusting.\n", 
    "I feel so sticky.\n"], 
    "I feel so slimy.\n"], 
    [["It would be bad.\n", 
    "That would be bad.\n", 
    "It would be bad.\n", 
    "It wouldn't be good\n"], 
    "It would not be good\n"],
    [["We kicked its ass!\n", 
    "We kicked it's ass!\n", 
    "We kicked their ass!\n", 
    "We kicked its behind\n"], 
    "We kicked its ass!\n"]]


    middle_man = choice(text_answers)
    correct = middle_man[1]
    data = middle_man[0]

    typewriter("""Select the line that follows, inputting 1, 2, 3 or 4:

""")
    time.sleep(2)
    if middle_man == text_answers[0]:
        typewriter("Drop everything, Venkman.\n")
        typewriter("")
        time.sleep(1)
    elif middle_man == text_answers[1]:
        typewriter("Who ya gonna call?\n")
        typewriter("")
        time.sleep(1)
    elif middle_man == text_answers[2]:
        typewriter("He slimed me.\n")
        typewriter("")
        time.sleep(1)
    elif middle_man == text_answers[3]:
        typewriter("Don't. Cross. The streams.\n")
        typewriter("")
        time.sleep(1)
    elif middle_man == text_answers[4]:
        typewriter("We came! We saw!\n")
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
        typewriter("""You ran out of time!""") #Fail condition
        try_again()
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
        typewriter("""You have successfully input the correct answer!""")
        os.system('cls' if os.name == 'nt' else 'clear')
        typewriter("""Congratulations!\n""")
        time.sleep(1)
        try_again()


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
        typewriter("""Unfortunately you input the wrong answer!""")     
        time.sleep(2)
        try_again()
quiz_game()