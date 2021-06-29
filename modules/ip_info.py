from base_module import BaseModule
from module_utils import show_popup, get_highlighted, put_in_paste
import ipinfo
import re

TOKEN = 'ca28d275177fa3'

IP_REGEX = '(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}'

class IpInfo(BaseModule):
    
    def run(self):
        highlighted = get_highlighted()
        ip_match = re.search(IP_REGEX, highlighted)
        if ip_match:
            ip = ip_match.group()
            handler = ipinfo.getHandler(TOKEN)
            details = handler.getDetails(ip)
            show_popup('Ip Info', '{} - {}'.format(details.country_name, details.city))
            put_in_paste(details.region)
        else:
            show_popup('Error!', 'Invalid input. Not in IP format.')
        
