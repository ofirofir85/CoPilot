import json
import win32api
import keyboard
import glob

HOT_KEY = 'hot_key'
ENABLED = 'enabled'
DEFAULT_HOT_KEY = 'alt+q'

BASE_CONFIG = {HOT_KEY: DEFAULT_HOT_KEY, ENABLED: True}

class BaseModule():
    def __init__(self, config={}):
        self.name = self.__class__.__name__
        if glob.glob(f'{self.name}.json'):
            self.load_config()

        else: #no config file found, creating default.
            self.config = {**BASE_CONFIG , **config}
            self.update_config(self.config)

    def update_config(self, new_config):
        with open(f'{self.name}.json', 'w') as f:
            json.dump(new_config, f)


    def load_config(self):
        with open(f'{self.name}.json', 'r') as f:
            self.config = json.load(f)

    def get_config(self):
        return self.config

    def run(self, *args, **kargs):
        pass
        