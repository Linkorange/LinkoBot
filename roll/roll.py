from random import randrange
import re


def roll(full_cmd):
    if full_cmd == 'roll':
        return str(randrange(6) + 1)
    elif len(full_cmd.split(' ')) == 2:
        r = re.match(r'^(?P<roll_number>[1-9])d(?P<dice_limit>100|\d{0,2})$', full_cmd.split(' ')[1])
        if r:
            roll_number = int(r.group('roll_number'))
            dice_limit = int(r.group('dice_limit'))

            rolls_list = []
            i = 0
            while i < roll_number:
                rolls_list.append(str(randrange(dice_limit) + 1))
                i += 1
            print(str(rolls_list))
            return " ".join(rolls_list)
        return ''
    return ''
