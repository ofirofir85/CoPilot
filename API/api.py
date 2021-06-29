import json
from flask import Flask, request

from utils import keyboard_manager
from utils.keyboard_manager import KeyBoardManager

app = Flask(__name__)


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


@app.route('/get_config', methods=['POST'])
def get_config():
    module_config = json.loads(request.data)
    file_name = module_config['module_name'].title().replace('_', '') + '.json'
    with open(file_name, 'rb') as f:
        j = f.read()

    return json.loads(j)