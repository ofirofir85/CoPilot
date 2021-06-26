from base_module import BaseModule
from module_utils import show_popup, get_copied_data
import ipinfo
import keyboard
import pyperclip
import time

TOKEN = 'ca28d275177fa3'

class IPInfo(BaseModule):
    
    def run(self):
        handler = ipinfo.getHandler(TOKEN)
        ip = get_copied_data()
        print(ip)
        details = handler.getDetails(ip)
        print(details)
        show_popup('Ip Info', details.region)
        
