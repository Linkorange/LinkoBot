# FIXME: As the file is imported in ../linkobot.py, I had to add the relative path from it and not from command_utils.py
with open('commands/command_list.txt') as command_list_file:
    command_list = command_list_file.read().splitlines()

    def is_cmd_in_list(cmd, target):
        """Checks if the given command is in the command_list"""
        if target in command_list and cmd.split(' ')[0] == target:
            return True
        return False


if __name__ == "__main__":
    pass
