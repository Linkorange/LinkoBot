from speedrun_com_api.speedrun_com_api_utils import *
import datetime
import re


def pb_command_handling(full_cmd):
    """
    Handles the !pb command according to the number of parameters.

    :param full_cmd: The command entered in chat ('!' character excluded)
    :return: The message to display in chat
    """
    current_game, current_category, current_user = get_current_data()

    # !pb
    if full_cmd == 'pb':
        return pb_choose_cat_or_not(current_user, current_game, current_category)
    # !pb game
    # TODO find something to make this command viable (same for the !wr command)
    # !pb game category
    elif re.match(r'^\S+ (?P<game>\S+) (?P<category>\S+)$', full_cmd):
        r = re.match(r'^\S+ (?P<game>\S+) (?P<category>\S+)$', full_cmd)
        return pb_choose_cat_or_not(current_user, r.group('game'), r.group('category'))
    # !pb game category player
    elif re.match(r'^\S+ (?P<game>\S+) (?P<category>\S+) (?P<player>\S+)$', full_cmd):
        r = re.match(r'^\S+ (?P<game>\S+) (?P<category>\S+) (?P<player>\S+)$', full_cmd)
        return pb_choose_cat_or_not(r.group('player'), r.group('game'), r.group('category'))
    # Other
    return ''


def pb_without_sub_category(user, game, category):
    """
    Writes the PB message for a user given a game and a category.
    Message looks like : "<user>'s personal best for <game> <category> is <time> (<place>th)"

    :param user: the given user name (not it's ID)
    :param game: the given game name (not it's ID)
    :param category: the given category code (not it's ID)
    :return: The message to write in chat if everything went well, an empty string otherwise.
    """
    game_id = get_element_id_from_name(game)
    user_id = get_element_id_from_name(user)
    category_id = get_id_category_from_name(game_id, category)

    # API request : http://www.speedrun.com/api/v1/users/{user_id}/personal-bests?game={game_id}
    # Fetches the personal best of the user from this game, and embed game, category and players to it
    uri = 'users/' + user_id + '/personal-bests?game=' + game_id + '&embed=game,category,players'
    pbs_dict = speedrun_api_connect(uri)

    if 'data' in pbs_dict:
        for run_data in pbs_dict['data']:
            user_name = run_data['players']['data'][0]['names']['international']
            category_name = run_data['category']['data']['name']
            game_name = run_data['game']['data']['names']['international']
            run = run_data['run']
            place = run_data['place']
            # Filters by category
            if run['category'] == category_id:
                pb_time_in_seconds = run['times']['primary_t']
                pb_time = str(datetime.timedelta(seconds=pb_time_in_seconds))

                return user_name + '\'s personal best for ' + game_name + ' ' + category_name\
                       + ' is ' + pb_time + '. (' + str(place) + 'th)'

    return ''


def pb_with_sub_categories(user, game, sub_category):
    """
    Writes the PB message for a user given a game and a sub_category.
    Message looks like : "<user>'s personal best for <game> <category> <sub_category> is <time> (<place>th)"

    :param user: the given user name (not it's ID)
    :param game: the given game name (not it's ID)
    :param sub_category: the given sub category code (not it's ID)
    :return: The message to write in chat if everything went well, an empty string otherwise.
    """
    game_id = get_element_id_from_name(game)
    user_id = get_element_id_from_name(user)

    # API request : http://www.speedrun.com/api/v1/users/{user_id}/personal-bests?game={game_id}
    # Fetches the personal bests of the user from this game
    uri = 'users/' + user_id + '/personal-bests?game=' + game_id + '&embed=game,category,players,category.variables'
    pbs_dict = speedrun_api_connect(uri)

    if 'data' in pbs_dict:
        category_id, variable_id, sub_category_id = sub_categories_info(game_id, sub_category)

        for run_data in pbs_dict['data']:
            user_name = run_data['players']['data'][0]['names']['international']
            game_name = run_data['game']['data']['names']['international']
            category_name = run_data['category']['data']['name']
            # This loop is here for the sub category name / couldn't find something else than this
            for variable_data in run_data['category']['data']['variables']['data']:
                if variable_data['id'] == variable_id:
                    sub_category_name = variable_data['values']['values'][sub_category_id]['label']
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


def pb_choose_cat_or_not(user, game, category):
    """
    Chooses the function to use whether the game has sub_categories or not.
    :param game: The game's name
    :param category: The category code
    :return: the result after being processed by the right function
    """
    if has_sub_categories(game):
        return pb_with_sub_categories(user, game, category)
    return pb_without_sub_category(user, game, category)
