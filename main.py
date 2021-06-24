import keyboard
from message_box import MessageBox

def main():
    mm = MessageBox()
    keyboard.add_hotkey(mm.config['hot_key'], mm.run)
    keyboard.wait('esc')

if __name__ == '__main__':
    main()