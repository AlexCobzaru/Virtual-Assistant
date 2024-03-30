from __future__ import print_function
import datetime
from logging import shutdown
import os.path
import os
import webbrowser
import random
import time
from time import ctime
import datetime
import subprocess
import io

from Main_Package.TEXT_ELEMENT import TR
from Main_Package.SET_LANGUAGE import set_language
from Main_Package.CHANGE import change
from Main_Package.AUDIO import speak, get_audio
from Main_Package.READ import language


set_language(f"{language('language.txt')}")
output_language = language()

hour = datetime.datetime.now().hour
last_test_hour = hour - 2
check = 1

WAKE = [f"{TR(1)}",f"{TR(2)}",f"{TR(3)}",f"{TR(4)}",f"{TR(5)}"]
SHUT_DOWN = [f"{TR(82)}", f"{TR(83)}",f"{TR(84)}"]
NOTE_STRS = [f"{TR(98)}", f"{TR(99)}"]
NAME_STRS = [f"{TR(109)}", f"{TR(112)}", f"{TR(113)}", f"{TR(114)}", f"{TR(115)}"]

INPUT = [WAKE,SHUT_DOWN,NOTE_STRS,NAME_STRS,98,99,117,119,122,123,125,126,126,129,131,132,133,134,136,137,138,139,134,141,142,143,146,148,149,150,155,156]

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def russian_ruoulette():
    speak("Are you sure you want to play? If I lose the program will close, if you lose the computer will shut down.")
    answer = get_audio()
    if f"{TR(63)}" in answer:
        speak(f"{TR(64)}")
    else:
        player=1
        while True:
            bullet = random.randint(1,6)
            if bullet == 1:
                if player==1:
                    #print("\n The app closes")
                    os.system("taskkill /f /im assistant.exe /T")
                    break
                elif player ==2:
                    #print("\n The computer closes")
                    os.system("shutdown /s /t 1")
                    break
            else:
                if player == 1:
                    speak("There was no bullet this time, I escaped")
                else:
                    speak("There was no bullet this time, you escaped")

            if player == 1:
                player+=1
            else:
                speak(f"{TR(62)}")
                answer = get_audio()
                if f"{TR(63)}" in answer:
                    speak(f"{TR(64)}")
                    break
                else:
                    player = 1
                
def Close_Second_window():
    os.system("taskkill /f /im geckodriver.exe /T")

def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"

    with io.open(file_name, "w", encoding="utf-8") as f:
        f.write(text)
    
    subprocess.Popen(["notepad.exe", file_name])
    
    speak("is there more?")
    if text == "yes":
        f.write(text)

def remove_geckodriver_log():
    try:
        os.remove("geckodriver.log") 
    except:
        pass

def RockPaperScissors():
    OUTCOMES=[f"{TR(57)}",f"{TR(58)}",f"{TR(59)}"]
    while True:
        choise = random.choice(OUTCOMES)
        speak(f"{TR(60)}")
        text = get_audio()
        speak(f"{TR(61)}" + choise)
        speak(f"{TR(62)}")
        text = get_audio()
        if f"{TR(63)}" in text:
            speak(f"{TR(64)}")
            break

def workout():
    EXERCICES = [f" {TR(65)}",f" {TR(66)}",f" {TR(67)}"]
    pushups = 0
    pullups = 0
    crunches = 0
    pushupsmax = 30
    pullupsmax = 4
    crunchesmax = 10
    speak(f"{TR(68)}")
    time.sleep(1)
    while True:
        exercices = random.choice(EXERCICES)
        exercicesmax = f"{exercices}max"
        number = random.randint(1,30)

        speak(f"{TR(69)} {number}{exercices}")
        
        if f"{TR(65)}" in exercices:
            pushups = pushups + number
        if f"{TR(66)}" in exercices:
            crunches = crunches + number
        if f"{TR(67)}" in exercices:
            pullups = pullups + number

        speak(f"{TR(70)}")
        while True:
            text = get_audio()
            if f"{TR(71)}" in text:
                break

        speak(f"{TR(72)}")    
        text = get_audio()
        if f"{TR(63)}" in text:
            speak(f"{TR(73)}")
            if pushups != 0:
                speak(f"{pushups} {f'{TR(65)}'}")
            if crunches != 0:
                speak(f"{crunches} {f'{TR(66)}'}")
            if pullups != 0:
                speak(f"{pullups} {f'{TR(67)}'}")
            break

def workout_check(a):
    check = 0
    speak(f"{TR(74)}")
    text = get_audio()
    if not f"{TR(63)}" in text:
        workout()
    else:
        speak(f"{TR(75)}")
    return check

def Help_Menu():
    speak("\n      This is a list with all the commands available      \n")
    for i in INPUT:
        if isinstance(i, list):
            print(f"\n {i}")
        else:
            print(f"\n {TR(i)}")

def greetings():
    if hour >= 4 and hour<11:
        speak(f"\n {TR(76)} {Nume}.")
    elif hour >=11 and hour<18:
        speak(f"\n {TR(77)} {Nume}.")
    else:
        speak(f"\n {TR(78)} {Nume}.")

name = change('name of owner.txt', f" {TR(79)}")

Nume = name.verify()

remove_geckodriver_log()
clear_terminal()
print('\n Say "Help Menu" to see the commands you can say')
greetings()

while True:
    hour = datetime.datetime.now().hour

    if hour == 18 and check == 1: check = workout_check(check)
    if hour == 19: check = 1

    text = get_audio()

    if f"{TR(156)}" in text:
        Help_Menu()

    for phrase in WAKE:
        if phrase in text:
            speak(f"{TR(81)}")
            text = get_audio()

            for phrase in SHUT_DOWN:
                if phrase in text:
                    speak(f"{TR(85)}")
                    text = get_audio() 
                    if f"{TR(63)}" in text or f"{TR(86)}" in text: 
                        speak(f"{TR(87)}")
                    else:
                        if hour >= 4 and hour < 11:
                            speak(f" {TR(88)}\n\n\n")
                            
                        elif hour >= 11 and hour < 18:
                            speak(f"{TR(89)}\n\n\n")   

                        elif hour >= 18 and hour < 22:
                            speak(f"{TR(90)}\n\n\n")

                        else:
                            speak(f"{TR(91)}\n\n\n")
                        
                        os.system("shutdown /s /t 1")

            for phrase in NOTE_STRS:
                if phrase in text:
                    speak(f" {TR(100)}")
                    note_text = get_audio()
                    note(note_text)
                    speak(f" {TR(101)}")
                        
            for phrase in NAME_STRS:
                if phrase in text:
                    if f"{TR(109)}" in text or f"{TR(112)}" in text or f"{TR(113)}" in text or f"{TR(114)}" in text  or f"{TR(115)}" in text:
                        name.change()
                    speak(f"{TR(116)}")

            if f"{TR(156)}" in text:
                Help_Menu()

            if f"{TR(117)}" in text:
                russian_ruoulette()

            if f"{TR(119)}" in text:
                speak(f"{TR(120)}")

            if f"{TR(122)}" in text:
                RockPaperScissors()

            if f"{TR(123)}" in text:
                speak(f"{TR(124)}")

            if f"{TR(125)}" in text or f"{TR(126)}" in text or f"{TR(127)}" in text:
                speak(f" {f'{TR(128)}'} {name.verify()}")

            if f"{TR(129)}" in text:
                speak(f"{TR(130)}")

            if f"{TR(131)}" in text or f"{TR(132)}" in text or f"{TR(133)}" in text or f"{TR(134)}" in text:
                speak(f"{TR(135)}")

            if f"{TR(136)}" in text or f"{TR(137)}" in text or f"{TR(138)}" in text:
                date = ctime()
                speak(date)
            
            if f"{TR(139)}" in text:
                workout()

            if f"{TR(140)}" in text or f"{TR(141)}" in text or f"{TR(142)}" in text:
                date = ctime()
                speak(date)

            if f"{TR(143)}" in text:
                speak(f"{TR(144)}")
                search = get_audio()
                url = 'https:///www.google.com/search?q=' + search
                webbrowser.get().open_new_tab(url)
                speak(f"{TR(145)}" + search )

            if f"{TR(146)}" in text:
                speak(f"{TR(147)}")
                location = get_audio()
                url = 'https:///www.google.nl/maps/place/' + location + '/&amp;'
                webbrowser.get().open_new_tab(url)
                speak(f"{TR(145)}" + location )
            
            if f"{TR(148)}" in text or f"{TR(149)}" in text or f"{TR(150)}" in text:
                speak(f"{TR(151)}\n\n\n")
                break

            if f"{TR(155)}" in text:
                index = text.find(f"{TR(155)}")
                result = text[index + len(f"{TR(155)}"):].strip()
                speak(f"{result} is {TR(int(result))}")