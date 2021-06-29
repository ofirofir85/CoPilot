from modules.base_module import BaseModule
from modules.module_utils import show_popup, get_highlighted, put_in_paste
from utm import from_latlon, to_latlon
import re

UTM_FORMAT = "UTM {slice}N {lat} E / {lon} N"
GWS_FORMAT = "WGS84 GEO {lat} E / {lon} N"
GWS_REGEX = '(\d{1,3}\.\d*)\s*E\s*/\s*(\d{1,3}\.\d*)\s*N.*'
UTM_REGEX = '(\d{1,3})([C-X]).*(\d{6,7}\.\d*)\s*E\s*/\s*(\d{6,7}\.\d*)\s*N.*'
        

class ConvertCoordinate(BaseModule):
    
    def run(self):
        orig = get_highlighted()
        gws_match = re.search(GWS_REGEX, orig)
        utm_match = re.search(UTM_REGEX, orig)
        if gws_match:
            lat, lon = gws_match.group(1, 2)
            raw_convertion = from_latlon(float(lat), float(lon))
            formated_convertion = UTM_FORMAT.format(slice=raw_convertion[2], lat=raw_convertion[0], lon=raw_convertion[1])
        if utm_match:
            slice, zone, lat, lon = utm_match.group(1, 2, 3, 4)
            raw_convertion = to_latlon(float(lat), float(lon), int(slice), zone_letter=zone)
            formated_convertion = GWS_FORMAT.format(lat=raw_convertion[0], lon=raw_convertion[1])

        if gws_match or utm_match:
            #show_popup('Converted coordinate', formated_convertion)
            put_in_paste(formated_convertion)
        else:
            show_popup('Error', 'Invalid input!')   
        
