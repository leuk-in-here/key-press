##This script uses pynput, this works with latest version of Python

from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

##This creates a delay before the code starts -> 2 seconds delay, enough time to 
time.sleep(2)

##This section targets input.txt in the same folder as the script.py, create a txt file named input and chuck whatever you want in
f = open("input.txt", "r")

##This is the main section of the code ->opens f up and enumerates the lines till no more lines exist in the file. 
##time.sleep is a delay function. this is necessary if the input site is trying to prevent too fast of a keystroke input.
for cnt, line in enumerate(f):
    for char in line:
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(0.08)
        
##This line below codes for a line break at the end of each line, if you want it to print the entire file without line breaks, comment it out.       
    time.sleep(0.12)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.12)
                    
