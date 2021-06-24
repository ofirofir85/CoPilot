import keyboard
from message_box import MessageBox
from ip_info import IPInfo

def main():
    mm = MessageBox()
    mm.config['message'] = 'test1'
    keyboard.add_hotkey(mm.config['hot_key'], mm.run)
    mm2 = MessageBox()
    mm2.config['message'] = 'test2'
    mm2.config['hot_key'] = 'alt+w'
    keyboard.add_hotkey(mm2.config['hot_key'], mm2.run)
    
    print(keyboard._hotkeys.items())
    keyboard.wait('esc')

if __name__ == '__main__':
    main()