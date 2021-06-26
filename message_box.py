from base_module import BaseModule
from module_utils import show_popup

MESSAGE = 'message'

class MessageBox(BaseModule):

    def __init__(self):
        message = 'deafult text'
        super().__init__({MESSAGE: message})
    
    def run(self):
        show_popup('Copilot', self.config[MESSAGE])