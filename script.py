##This script uses pynput, this works with latest version of Python

from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

time.sleep(2)

##This line targets input.txt in the same folder as the script.py, create a txt file named input and chuck whatever you want in
f = open("input.txt", "r")
for cnt, line in enumerate(f):
    for char in line:
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(0.08)
        
##This line below codes for enter, if you want it to print the entire file without line breaks, comment it out.       
    time.sleep(0.12)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.12)
                    
