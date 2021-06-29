from base_module import BaseModule
from win32gui import GetWindowText, GetForegroundWindow
import keyboard

SHORTCUT = ['alt', 'H', 'F', 'F']

class David12(BaseModule):
    
    def run(self):
        if 'Word' in GetWindowText(GetForegroundWindow()):
            for key in SHORTCUT:
                keyboard.send(key)
