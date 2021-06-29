import win32api
import pyperclip
import keyboard
import time
import winsound

def show_popup(title, message):
    win32api.MessageBox(0, message, title)

def put_in_paste(data):
    pyperclip.copy(data)

def get_copied_data():
    return pyperclip.paste()

def get_highlighted():
    orig_clip = get_copied_data()
    keyboard.release('alt')
    keyboard.send('ctrl+c')
    time.sleep(0.1)
    highlighted = get_copied_data()
    put_in_paste(orig_clip)
    return highlighted

def show_popup_and_put_paste(title, message):
    show_popup(title, message)
    put_in_paste(message)

def error_sound():
    winsound.MessageBeep(winsound.MB_ICONHAND)