from speedrun_com_api.speedrun_com_api_utils import *
import datetime
import re


def wr_command_handling(full_cmd):
    """
    Handles the !wr command according to the number of parameters.

    :param full_cmd: The command entered in chat ('!' character excluded)
    :return: The message to display in chat
    """
    current_game, current_category, current_user = get_current_data()

    # !wr
    if full_cmd == 'wr':
        return wr_choose_category_or_sub_category(current_game, current_category)
    # !wr game category
    elif re.match(r'^\S+ (?P<game>\S+) (?P<category>\S+)$', full_cmd):
        r = re.match(r'^\S+ (?P<game>\S+) (?P<category>\S+)$', full_cmd)
        return wr_choose_category_or_sub_category(r.group('game'), r.group('category'))
    # Other
    return ''


def wr_without_sub_category(game, category):
    """
    Writes the WR message given a game and a category.
    Message looks like : "World Record in <game> <category> is <time> by <player>."

    :param game: the given game name (not it's ID)
    :param category: the given category code (not it's ID)
    :return: The message to write in chat if everything went well, an empty string otherwise.
    """
    game_id = get_element_id_from_name(game)
    category_id = get_id_category_from_name(game_id, category)

    # API request : http://www.speedrun.com/api/v1/users/{user_id}/personal-bests?game={game_id}
    # Fetches the personal best of the user from this game, and embed game, category and players to it
    uri = 'leaderboards/' + game_id + '/category/' + category_id + '?top=1&embed=players,category,game'
    response = speedrun_api_connect(uri)

    if 'data' in response.keys():
        data = response['data']
        category_name = data['category']['data']['name']
        game_name = data['game']['data']['names']['international']
        user_name = data['players']['data'][0]['names']['international']
        run = data['runs'][0]['run']
        wr_time_in_seconds = run['times']['primary_t']
        wr_time = str(datetime.timedelta(seconds=wr_time_in_seconds))

        return 'World Record for ' + game_name + ' ' + category_name + ' is ' + wr_time + ' by ' + user_name + '.'
    return ''


def wr_with_sub_categories(game, sub_category):
    """
    Writes the WR message given a game and a sub_category.
    Message looks like : "World Record in <game> <category> <sub_category> is <time> by <player>."

    :param game: the given game name (not it's ID)
    :param sub_category: the given sub category code (not it's ID)
    :return: The message to write in chat if everything went well, an empty string otherwise.
    """
    game_id = get_element_id_from_name(game)
    category_id, variable_id, sub_category_id = sub_categories_info(game_id, sub_category)

    # API request : http://www.speedrun.com/api/v1/users/{user_id}/personal-bests?game={game_id}
    # Fetches the personal bests of the user from this game
    uri = 'leaderboards/' + game_id + '/category/' + category_id\
          + '?top=1&embed=players,category,game,variables&var-' + variable_id + '=' + sub_category_id
    response = speedrun_api_connect(uri)

    if 'data' in response.keys():
        data = response['data']
        category_name = data['category']['data']['name']
        # set sub_category_name
        for variable_data in data['variables']['data']:
            if variable_data['id'] == variable_id:
                sub_category_name = variable_data['values']['values'][sub_category_id]['label']
        game_name = data['game']['data']['names']['international']
        user_name = data['players']['data'][0]['names']['international']
        run = data['runs'][0]['run']
        wr_time_in_seconds = run['times']['primary_t']
        wr_time = str(datetime.timedelta(seconds=wr_time_in_seconds))
        return 'World Record for ' + game_name + ' ' + category_name + ' ' + sub_category_name + ' is ' + wr_time + ' by ' + user_name + '.'
    return ''


def wr_choose_category_or_sub_category(game, category):
    """
    Chooses the function to use whether the game has sub_categories or not.
    :param game: The game's name
    :param category: The category code
    :return: the result after being processed by the right function
    """
    if has_sub_categories(game):
        return wr_with_sub_categories(game, category)
    return wr_without_sub_category(game, category)
