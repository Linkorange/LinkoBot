from speedrun_com_api.speedrun_com_api_utils import *
import datetime
import re
import json


def pb_command_handling(full_cmd):
    """
    Handles the !pb command according to the number of parameters.

    :param full_cmd: The command entered in chat ('!' character excluded)
    :return:
    """
    abs_path = os.path.abspath(os.path.dirname(__file__))
    path_to_file = os.path.join(abs_path, 'current_data.json')

    with open(path_to_file) as current_data_json_file:
        current_data_json = json.load(current_data_json_file)
        current_game = current_data_json['game']
        current_user = current_data_json['user']
        current_category = current_data_json['category']

        print(full_cmd)

        # !pb
        if full_cmd == 'pb':
            return choose_cat_or_not(current_user, current_game, current_category)
        # !pb game TODO find something to make this command viable
        # elif re.match(r'^\S (?P<game>\S)$', full_cmd):
        #     r = re.match(r'^\S (?P<game>\S)$', full_cmd)
        #     return choose_cat_or_not(current_user, r.group('game'), current_category)
        # !pb game category
        elif re.match(r'^\S+ (?P<game>\S+) (?P<category>\S+)$', full_cmd):
            r = re.match(r'^\S+ (?P<game>\S+) (?P<category>\S+)$', full_cmd)
            return choose_cat_or_not(current_user, r.group('game'), r.group('category'))
        # !pb game category player
        elif re.match(r'^\S+ (?P<game>\S+) (?P<category>\S+) (?P<player>\S+)$', full_cmd):
            r = re.match(r'^\S+ (?P<game>\S+) (?P<category>\S+) (?P<player>\S+)$', full_cmd)
            return choose_cat_or_not(r.group('player'), r.group('game'), r.group('category'))
        # Other
        return ''


def pb_without_sub_cat(user, game, category):
    """
    Writes the PB message for a user given a game and a category.
    Message looks like : "<user>'s personal best for <game> <category> is <time> (<place>th)"

    Total of API requests number for 1 call : 4 API requests

    :param user:
    :param game: default
    :param category: default
    :return:
    """
    game_id = get_element_id_from_name(game)
    user_id = get_element_id_from_name(user)
    category_id = get_id_category_from_name(game_id, category)

    # API request : http://www.speedrun.com/api/v1/users/{user_id}/personal-bests?game={game_id}
    # Fetches the personal bests of the user from this game
    uri = 'users/' + user_id + '/personal-bests?game=' + game_id
    pbs_dict = speedrun_api_connect(uri)

    if 'data' in pbs_dict:
        # Here are 3 API requests
        user_name = get_user_name(user)
        category_name = get_category_name(category_id)
        game_name = get_game_name(game)

        for run_data in pbs_dict['data']:
            run = run_data['run']
            place = run_data['place']
            # Filters by category
            if run['category'] == category_id:
                pb_time_in_seconds = run['times']['primary_t']
                pb_time = str(datetime.timedelta(seconds=pb_time_in_seconds))

                return user_name + '\'s personal best for ' + game_name + ' ' + category_name\
                       + ' is ' + pb_time + '. (' + str(place) + 'th)'

    return ''


def pb_with_sub_cat(user='linkorange', game='', sub_category=''):
    """
    Writes the PB message for a user given a game and a sub_category.
    Message looks like : "<user>'s personal best for <game> <category> is <time> (<place>th)"

    :param user:
    :param game: default
    :param sub_category: default
    :return:
    """
    game_id = get_element_id_from_name(game)
    user_id = get_element_id_from_name(user)

    # API request : http://www.speedrun.com/api/v1/users/{user_id}/personal-bests?game={game_id}
    # Fetches the personal bests of the user from this game
    uri = 'users/' + user_id + '/personal-bests?game=' + game_id
    pbs_dict = speedrun_api_connect(uri)

    if 'data' in pbs_dict:
        # Here are 4 API requests
        user_name = get_user_name(user)
        category_name = get_category_name_from_sub_category(game_id, sub_category)
        sub_category_name = get_sub_category_name(game_id, sub_category)
        game_name = get_game_name(game)

        category_id, variable_id, sub_category_id = sub_categories_info(game_id, sub_category)

        for run_data in pbs_dict['data']:
            run = run_data['run']
            place = run_data['place']
            # Filters by category
            if run['category'] == category_id:

                if variable_id in run['values'].keys() and run['values'][variable_id] == sub_category_id:
                    pb_time_in_seconds = run['times']['primary_t']
                    pb_time = str(datetime.timedelta(seconds=pb_time_in_seconds))

                    return user_name + '\'s personal best for ' + game_name + ' ' + category_name\
                           + ' ' + sub_category_name + ' is ' + pb_time + '. (' + str(place) + 'th)'
    return ''


def choose_cat_or_not(user, game, category):
    if has_sub_category(game):
        return pb_with_sub_cat(user, game, category)
    return pb_without_sub_cat(user, game, category)
