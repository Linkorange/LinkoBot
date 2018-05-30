import json
from quotes.quotes import quote_command_handling

# FIXME: As the file is imported in ../linkobot.py, I had to add the relative path from it and not from command_utils.py


def write_in_chat_from_cmd(full_cmd):
    """Returns a string given a command line according to the command_list.json JSON file"""
    cmd = full_cmd.split(' ')[0]
    with open('commands/command_list.json') as command_list_json:
        command_list = json.load(command_list_json)
        if cmd in command_list.keys():
            if command_list[cmd] == "complex_treatment":
                return complex_treatment(full_cmd)
            return command_list[cmd]
        return ''


def complex_treatment(cmd):
    """Defines more complex treatments than just returning a string given a command

    Usually this function passes commands to functions which will parse them and make some treatments"""
    core_command = cmd.split(' ')[0]
    if core_command == "quote":
        return quote_command_handling(cmd)
    return ''
