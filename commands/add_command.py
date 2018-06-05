import json
import sys
import os.path


# Initializes the relative path for command_list.json
abs_path = os.path.abspath(os.path.dirname(__file__))
path_to_file = os.path.join(abs_path, 'command_list.json')


def add_command(cmd_name, cmd_msg='', help_msg=''):
    with open(path_to_file, 'r+') as command_list_json:
        command_list = json.load(command_list_json)
        command_list[cmd_name] = {'command': cmd_msg, 'help': help_msg}

        command_list_json.seek(0)
        command_list_json.truncate()
        json.dump(command_list, command_list_json)
        print('Successfully added the following command in command_list.json : '
              + str({cmd_name: command_list[cmd_name]}))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        add_command(sys.argv[1])
    elif len(sys.argv) == 3:
        add_command(sys.argv[1], sys.argv[2])
    elif len(sys.argv) == 4:
        add_command(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print('Wrong number of arguments ! Type "add_command.py <cmd_name> [<cmd_msg>] [<help_msg>]"')
