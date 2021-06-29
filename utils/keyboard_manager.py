import importlib
import keyboard
import threading


class KeyBoardManager:
    is_running_abbreviations_thread = False

    @staticmethod
    def initialize_keyboard_abbreviation():
        thread = threading.Thread(target=KeyBoardManager.wait_abbreviation)
        thread.start()

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

    @staticmethod
    def wait_abbreviation():
        keyboard.wait()

    @staticmethod
    def set_abbreviation(abbreviation_config):
        if not KeyBoardManager.is_running_abbreviations_thread:
            KeyBoardManager.initialize_keyboard_abbreviation()
            KeyBoardManager.is_running_abbreviations_thread = True

        if abbreviation_config['enabled']:
            keyboard.add_abbreviation(abbreviation_config["word"],
                                      abbreviation_config["abbreviation"],
                                      timeout=1)
        else:
            try:
                keyboard.remove_abbreviation(abbreviation_config["word"])
            except Exception as e:
                print("The word {} has no abbreviation yet".format(abbreviation_config["word"]))
