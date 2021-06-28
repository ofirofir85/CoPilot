from base_module import BaseModule
from module_utils import show_popup, get_copied_data, put_in_paste
import ipinfo

TOKEN = 'ca28d275177fa3'

class IPInfo(BaseModule):
    
    def run(self):
        handler = ipinfo.getHandler(TOKEN)
        ip = get_copied_data()
        print(ip)
        details = handler.getDetails(ip)
        print(details)
        show_popup('Ip Info', details.region)
        put_in_paste(details.region)
        
