from base_module import BaseModule
from module_utils import show_popup, get_copied_data

MESSAGE = 'message'

class MessageBox(BaseModule):

    def __init__(self):
        message = 'deafult text'
        super().__init__({MESSAGE: message})
    
    def run(self):
        message = get_copied_data()
        if not message:
            message = self.config[MESSAGE]
        show_popup('Copilot', message)