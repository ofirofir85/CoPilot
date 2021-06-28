import win32api
import pyperclip
import keyboard
import time

def show_popup(title, message):
    win32api.MessageBox(0, message, title)

def put_in_paste(data):
    pyperclip.copy(data)

def get_copied_data():
    return pyperclip.paste()

def show_popup_and_put_paste(title, message):
    show_popup(title, message)
    put_in_paste(message)