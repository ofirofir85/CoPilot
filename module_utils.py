import win32api
import pyperclip

def show_popup(title, message):
    win32api.MessageBox(0, message, title)

def put_in_paste(data):
    pyperclip.copy(data)

def get_copied_data():
    return pyperclip.paste()