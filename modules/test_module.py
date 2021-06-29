from modules.text_cleaner import TextCleaner
import keyboard
from modules.message_box import MessageBox
from modules.ip_info import IPInfo
from modules.convert_coordinate import ConvertCoordinate
from modules.word_format_regulator import WordFormatRegulator

def main():
    mm = MessageBox()
    mm.config['message'] = 'test1'
    keyboard.add_hotkey(mm.config['hot_key'], mm.run)
    mm2 = MessageBox()
    mm2.config['message'] = 'test2'
    mm2.config['hot_key'] = 'alt+w'
    keyboard.add_hotkey(mm2.config['hot_key'], mm2.run)

    ip = IPInfo()
    ip.config['hot_key'] = 'alt+r'
    keyboard.add_hotkey(ip.config['hot_key'], ip.run)
    
    tc = TextCleaner()
    tc.config['hot_key'] = 'alt+k'
    keyboard.add_hotkey(tc.config['hot_key'], tc.run)

    cc = ConvertCoordinate()
    cc.config['hot_key'] = 'alt+n'
    keyboard.add_hotkey(cc.config['hot_key'], cc.run)

    wfr = WordFormatRegulator()
    wfr.config['hot_key'] = 'ctrl+alt+b'
    keyboard.add_hotkey(wfr.config['hot_key'], wfr.run)

    keyboard.wait('esc')