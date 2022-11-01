from pynput import keyboard 
import pyautogui
import time

pyautogui.size() 
(1920, 1080) # sets screen size

def mouse_movment_and_click():
    pyautogui.moveTo(1055, 200,0.25)
    pyautogui.click()
    pyautogui.moveTo(x=1055, y=500)
    time.sleep(3)
    pyautogui.click()
    time.sleep(3)
    pyautogui.press('f')

# The key combination to check
COMBINATIONS = [
    {keyboard.KeyCode(char='z')}, #these 2 lines bsaicly make it so no matter what order the two keys are pressed it will still register
    {keyboard.KeyCode(char='x')}

]

# The currently active modifier
current = set() # basicaly an empty check box

def execute(): # when the hotkeys pressed do this
    mouse_movment_and_click()
def on_press(key):
    if any([key in COMBO for COMBO in COMBINATIONS]): # checks if any key in the COMBINATIONS have been pressed
        current.add(key) # if so add key to set (basicaly putting a tick in the box)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
            execute()

def on_release(key): #removes check from check box
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.remove(key)

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

pyautogui.alert('To play next episode press.') # makes an alert box pop up

#By Myerme

#to do: add feature to replay command inace doesnt work properly, try make it run smother add multiple hot keys find a way to make some keys 3d print or somthing for in bed ]

