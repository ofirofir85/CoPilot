<<<<<<< HEAD
from text_cleaner import TextCleaner
import keyboard
from message_box import MessageBox
from ip_info import IPInfo
from convert_coordinate import ConvertCoordinate
from word_format_regulator import WordFormatRegulator

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
=======
from API.api import app
>>>>>>> 2e5f9f7af33d5f06c16585a44cf29c2dacd5b6b4

if __name__ == '__main__':
    app.run()