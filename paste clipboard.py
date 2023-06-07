import pyautogui,time

pyautogui.keyDown('alt')
time.sleep(.2)
pyautogui.press('tab')
time.sleep(.2)
pyautogui.keyUp('alt')

pyautogui.keyDown('ctrl')
time sleep(.2)
pyautogui.press('v')
time.sleep(.2)
pyautogui.press('ctrl')
pyautogui.press('enter')

##||in this way

from time import sleep
import ctypes

user32 = ctypes.windll.user32

user32.keybd_event(0x12, 0, 0, 0) #Alt
sleep(1)
user32.keybd_event(0x09, 0, 0, 0) #Tab
sleep(1)
user32.keybd_event(0x09, 0, 2, 0) #~Tab
sleep(0.1)
user32.keybd_event(0x12, 0, 2, 0) #~Alt
