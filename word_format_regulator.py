from base_module import BaseModule
from win32gui import GetWindowText, GetForegroundWindow
import keyboard
import time

SHORTCUT = ['alt', 'H', 'f', 'f', 'enter', 'alt', 'H', 'f', 's', 'enter', 'ctrl+5', 'alt', 'H', 'A', 'j','alt',"H","0","down"]
#SHORTCUT = ['alt', 'H', 'f', 'f', 'd', 'a', 'v', 'i', 'd', 'enter', 'alt', 'H', 'f', 's', '1', '2', 'enter', 'ctrl+5', 'alt', 'H', 'A', 'j', 'enter','alt',"H","0"]
FONT = "font"
SIZE = "size"
class WordFormatRegulator(BaseModule):
    
    def __init__(self):
        super().__init__({FONT:"Gisha",SIZE:"15"})

    def run(self):
        keyboard.release(self.config['hot_key'].split('+'))
        strokes=[]
        font_chars = [i for i in self.config[FONT].lower()]
        size_chars = [i for i in self.config[SIZE]]
        if 'Word' in GetWindowText(GetForegroundWindow()):
            strokes = SHORTCUT[:4] + font_chars + SHORTCUT[4:9] + size_chars + SHORTCUT[9:]
            for key in strokes:
                print(key)
                keyboard.send(key)
                #time.sleep(0.1) NO NEED TO SLEEP
