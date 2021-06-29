import json
from flask import Flask, request

from utils import keyboard_manager
from utils.keyboard_manager import KeyBoardManager
import os

app = Flask(__name__)
CATALOG_FILE = "catalog.json"
MY_MODULES_DIRECTORY = "my_modules"

@app.route('/get_catalog', methods=['GET'])
def get_catalog():
    with open(CATALOG_FILE, 'rb') as f:
        catalog_elements = json.loads(f.read())

    return catalog_elements

@app.route('/get_my_modules', methods=['GET'])
def get_my_modules():
    modules = {}
    for file in os.listdir(MY_MODULES_DIRECTORY):
        suffix = ".json"
        if file.endswith(suffix):
            module_name = file.split(".")[0]
            with open(os.path.join(MY_MODULES_DIRECTORY, file), "rb") as f:
                modules[module_name] = json.loads(f.read())

    return modules



@app.route('/install_module', methods=['POST'])
def install_module():
    module_config = json.loads(request.data)
    module_name = module_config['module_name']
    keyboard_manager.KeyBoardManager.install_module(module_name)
    return 'OK'


@app.route('/edit_module', methods=['POST'])
def edit_module():
    module_config = json.loads(request.data)
    keyboard_manager.KeyBoardManager.edit_module(module_config)
    return 'OK'


@app.route('/set_module_state', methods=['POST'])
def set_module_state():
    module_config = json.loads(request.data)
    instance = KeyBoardManager.create_instance(module_config['module_name'])
    keyboard_manager.KeyBoardManager.set_module_state(module_config, instance)
    return 'OK'


@app.route('/get_module_config', methods=['POST'])
def get_module_config():
    module_config = json.loads(request.data)
    file_name = module_config['module_name'].title().replace('_', '') + '.json'
    with open(file_name, 'rb') as f:
        j = f.read()

    return json.loads(j)


@app.route('/set_abbreviation', methods=['POST'])
def set_abbreviation():
    abbreviation_config = json.loads(request.data)
    KeyBoardManager.set_abbreviation(abbreviation_config)

    return "OK"
