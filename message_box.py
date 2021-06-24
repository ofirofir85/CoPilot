from base_module import BaseModule
import win32api

MESSAGE = 'message'

class MessageBox(BaseModule):

    def __init__(self):
        message = 'deafult text'
        super().__init__({MESSAGE: message})
    
    def run(self):
        win32api.MessageBox(0, self.config[MESSAGE], 'Title')
