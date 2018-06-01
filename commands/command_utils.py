import json
import os.path
from quotes.quotes import quote_command_handling
from roll.roll import roll

# Initializes the relative path for command_list.json
abs_path = os.path.abspath(os.path.dirname(__file__))
path_to_file = os.path.join(abs_path, 'command_list.json')


def write_in_chat_from_cmd(full_cmd):
    """Returns a string given a command line according to the command_list.json JSON file"""
    cmd = full_cmd.split(' ')[0]
    with open(path_to_file) as command_list_json:
        command_list = json.load(command_list_json)
        if cmd in command_list.keys():
            if command_list[cmd]['command'] == "complex_treatment":
                return complex_treatment(full_cmd)
            return command_list[cmd]['command']
        return ''


def complex_treatment(full_cmd):
    """Defines more complex treatments than just returning a string given a command

    Usually this function passes commands to functions which will parse them and make some treatments"""
    core_command = full_cmd.split(' ')[0]
    if core_command == 'quote':
        return quote_command_handling(full_cmd)
    elif core_command == 'help':
        return help_command(full_cmd)
    elif core_command == 'roll':
        return roll(full_cmd)
    return ''


def help_command(full_cmd):
    with open(path_to_file) as command_list_json:
        command_list = json.load(command_list_json)
        if full_cmd == 'help':
            return 'List of all commands and explanations there : https://github.com/Linkorange/LinkoBot'
        elif len(full_cmd.split(' ')) == 2:
            # cmd = string containing the command to have information about
            cmd = full_cmd.split(' ')[1]
            if cmd in command_list.keys():
                return command_list[cmd]['help']
            return ''
        return ''
