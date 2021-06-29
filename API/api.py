import json
import copy
from flask import Flask, request
from flask_cors import CORS
from utils import keyboard_manager
from utils.keyboard_manager import KeyBoardManager
import os

app = Flask(__name__)
CORS(app, resources="*")

CATALOG_FILE = "catalog.json"
MY_MODULES_DIRECTORY = "my_modules"


@app.route('/get_catalog', methods=['GET'])
def get_catalog():
    parsed_elements = []
    with open(CATALOG_FILE, 'rb') as f:
        catalog_elements = json.loads(f.read())

    for catalog_element in catalog_elements:
        parsed_elements.append(catalog_elements[catalog_element])

    return {'data': parsed_elements}


@app.route('/get_my_modules', methods=['GET'])
def get_my_modules():
    exist_modules = []
    for file in os.listdir(MY_MODULES_DIRECTORY):
        print(file)
        suffix = ".json"
        if file.endswith(suffix):
            module_name = file.split(".")[0]
            exist_modules.append(module_name)
            print(exist_modules)

    parsed_elements = []
    with open(CATALOG_FILE, 'rb') as f:
        catalog_elements = json.loads(f.read())
       
    print(catalog_elements)
    for catalog_element in catalog_elements:
        if catalog_element in exist_modules:
            new_data = copy.deepcopy(catalog_elements[catalog_element])
            with open(MY_MODULES_DIRECTORY + '\\' + catalog_element + ".json", 'rb') as f:
                configuration = json.loads(f.read())
            new_data['configuration'] = configuration
            parsed_elements.append(new_data)

    print(parsed_elements)
    return {'data': parsed_elements}


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
    with open(MY_MODULES_DIRECTORY + '\\' + file_name, 'rb') as f:
        j = f.read()

    return json.loads(j)


@app.route('/set_abbreviation', methods=['POST'])
def set_abbreviation():
    abbreviation_config = json.loads(request.data)
    KeyBoardManager.set_abbreviation(abbreviation_config)

    return "OK"
