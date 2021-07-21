# in command prompt, type "pip install pynput" to install pynput.
from pynput.keyboard import Key, Controller
import time

keyboard = Controller()
key = Key.left

time.sleep(2)
keyboard.press(key)
keyboard.release(key)
