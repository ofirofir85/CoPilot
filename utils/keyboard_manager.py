from modules import message_box,ip_info
import importlib
import keyboard


class KeyBoardManager:

    @staticmethod
    def create_instance(module_name):
        module = importlib.import_module("modules.{}".format(module_name))
        new_class = getattr(module, module_name.title().replace('_', ''))
        instance = new_class()
        return instance

    @staticmethod
    def install_module(module_name):
        # Call update_config
        KeyBoardManager.create_instance(module_name)

    @staticmethod
    def edit_module(module_config):
        module_name = module_config['module_name']
        instance = KeyBoardManager.create_instance(module_name)
        instance.update_config(module_config)
        KeyBoardManager.set_module_state(module_config, instance)

    @staticmethod
    def set_module_state(module_config, instance):
        if module_config['enabled']:
            keyboard.add_hotkey(module_config['hot_key'], instance.run)
        else:
            keyboard.remove_hotkey(module_config['hot_key'])