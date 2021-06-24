import base_module

class MessageBox(BaseModule):

    MESSAGE = 'message'

    def __init__(self):
        my_param = 'deafult text'
        super().__init__({MESSAGE: my_param})
    
    def run(self):
        win32api.MessageBox(0, self.config[MESSAGE], 'Title')
