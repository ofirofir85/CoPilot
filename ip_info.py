from base_module import BaseModule
import win32api
import ipinfo
import keyboard
import pyperclip
import time

TOKEN = 'ca28d275177fa3'

class IPInfo(BaseModule):
    
    def run(self):
        handler = ipinfo.getHandler(TOKEN)
        details = handler.getDetails(self.get_ip())
        win32api.MessageBox(0, details.region, 'Title')
    
    def get_ip(self):
        return pyperclip.paste()
        
