"""
This module represent the keyboard manager, which response
to manage all the abbreviations and shortcuts which invoke different modules.
"""

import importlib
import keyboard
import threading


class KeyBoardManager:
    is_running_abbreviations_thread = False

    """
    Initialize new thread to manage and wait for all user's abbreviations.
    """
    @staticmethod
    def initialize_keyboard_abbreviation():
        thread = threading.Thread(target=KeyBoardManager.wait_abbreviation)
        thread.start()

    """
    A utility function which helps to create a specific instance from the relevant module 
    """
    @staticmethod
    def create_instance(module_name):
        module = importlib.import_module("modules.{}".format(module_name))
        new_class = getattr(module, module_name.title().replace('_', ''))
        instance = new_class()
        return instance

    """
    Install a new helpful module for the user
    """
    @staticmethod
    def install_module(module_name):
        # Call update_config
        KeyBoardManager.create_instance(module_name)

    """
    Change the module's configuration to a new one.
    """
    @staticmethod
    def edit_module(module_config):
        module_name = module_config['module_name']
        instance = KeyBoardManager.create_instance(module_name)
        instance.update_config(module_config)
        KeyBoardManager.set_module_state(module_config, instance)

    """
    Enable/Disable module's shortcut.
    """
    @staticmethod
    def set_module_state(module_config, instance):
        if module_config['enabled']:
            keyboard.add_hotkey(module_config['hot_key'], instance.run)
        else:
            keyboard.remove_hotkey(module_config['hot_key'])

    """
    This function is called from another thread, and actually waits for abbreviation to occur.
    """
    @staticmethod
    def wait_abbreviation():
        keyboard.wait()

    """
    Enable/Disable an abbreviation, and its configuration.
    """
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
