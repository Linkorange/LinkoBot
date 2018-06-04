import requests
import os.path
import json


def speedrun_api_connect(uri=''):
    """
    Connects to the speedrun.com API according to an URI and returns the JSON object response from it.

    :param uri: The URI defining parameters of the query
    :return: a JSON object corresponding to the query
    """
    abs_path = os.path.abspath(os.path.dirname(__file__))
    path_to_file = os.path.join(abs_path, '../NE_PAS_COMMIT/speedrun_com_api_oauth_key.txt')

    with open(path_to_file) as oauth_file:
        oauth_key = oauth_file.read()
        api_url = 'http://speedrun.com/api/v1/' + uri
        headers = {'Host': 'www.speedrun.com', 'X-API-Key': oauth_key, 'Accept': 'application/json'}
        return requests.get(api_url, headers=headers).json()


def get_current_game():
    """
    Returns the current game from the current_data.json file.
    :return: a string containing the current game.
    """
    abs_path = os.path.abspath(os.path.dirname(__file__))
    path_to_file = os.path.join(abs_path, 'current_data.json')

    with open(path_to_file) as current_game_json:
        return json.load(current_game_json)['game']


def get_current_category():
    """
    Returns the current category from the current_data.json file.
    :return: a string containing the current category.
    """
    abs_path = os.path.abspath(os.path.dirname(__file__))
    path_to_file = os.path.join(abs_path, 'current_data.json')

    with open(path_to_file) as current_game_json:
        return json.load(current_game_json)['game']


def get_current_sub_category():
    """
    Returns the current sub category from the current_data.json file.
    :return: a string containing the current sub category.
    """
    abs_path = os.path.abspath(os.path.dirname(__file__))
    path_to_file = os.path.join(abs_path, 'current_data.json')

    with open(path_to_file) as current_game_json:
        return json.load(current_game_json)['game']


def get_element_id_from_name(element_name):
    """
    Retrieves an element ID from the corresponding name in the ids.json file.

    :param element_name: the name to transform into an id
    :return: the ID corresponding to the given name. If the name is not found in the JSON, then returns it raw.
    """
    abs_path = os.path.abspath(os.path.dirname(__file__))
    path_to_file = os.path.join(abs_path, 'ids.json')
    with open(path_to_file) as ids_json_file:
        ids_json = json.load(ids_json_file)
        if element_name in ids_json['games']:
            return ids_json['games'][element_name]
        elif element_name in ids_json['users']:
            return ids_json['users'][element_name]
        return element_name


def get_id_category_from_name(game_id, category_name):
    """
    Retrieves a category ID in the ids.json file given a game name and a category name.

    :param game_id: the game's ID whose category is looked for
    :param category_name: the name to transform into an id
    :return: the ID corresponding to the given name. If the name is not found in the JSON, then returns it raw.
    """
    abs_path = os.path.abspath(os.path.dirname(__file__))
    path_to_file = os.path.join(abs_path, 'ids.json')
    with open(path_to_file) as ids_json_file:
        ids_json = json.load(ids_json_file)
        if game_id in ids_json['games-categories']:
            if category_name in ids_json['games-categories'][game_id]['categories']:
                return ids_json['games-categories'][game_id]['categories'][category_name]
        return category_name


def get_user_name(user):
    """
    Fetches the user name from speedrun.com API given a string.

    :param user: a string defining the user
    :return: The international name from a user
    """
    user_id = get_element_id_from_name(user)
    uri = 'users/' + user_id
    response = speedrun_api_connect(uri)
    if 'data' in response.keys():
        return response['data']['names']['international']
    return ''


def get_category_name(category_id):
    """
    Fetches the category name from speedrun.com API given a string.

    :param category_id: the ID of the desired category
    :return: The official category name
    """
    uri = 'categories/' + category_id
    response = speedrun_api_connect(uri)
    if 'data' in response.keys():
        return response['data']['name']
    return ''


def get_sub_category_name(game_id, sub_category):
    """
    Fetches the sub category name from speedrun.com API given a string.

    :param sub_category: a string defining the category
    :return: The official category name
    """
    category_id, variable_id, sub_category_id = sub_categories_info(game_id, sub_category)
    uri = 'categories/' + category_id + '/variables'
    response = speedrun_api_connect(uri)
    if 'data' in response.keys():
        for variable in response['data']:
            if variable['id'] == variable_id:
                if sub_category_id in variable['values']['values']:
                    return variable['values']['values'][sub_category_id]['label']
    return ''


def get_category_name_from_sub_category(game_id, sub_category):
    """
    Fetches the sub category name from speedrun.com API given a string.

    :param sub_category: a string defining the category
    :return: The official category name
    """
    category_id, variable_id, sub_category_id = sub_categories_info(game_id, sub_category)
    uri = 'categories/' + category_id
    response = speedrun_api_connect(uri)

    if 'data' in response.keys():
        return response['data']['name']
    return ''


def get_game_name(game):
    """
    Fetches the game name from speedrun.com API given a string.

    :param game: a string defining the game
    :return: The international game name
    """
    game_id = get_element_id_from_name(game)
    uri = 'games/' + game_id
    response = speedrun_api_connect(uri)
    if 'data' in response.keys():
        return response['data']['names']['international']
    return ''


def has_sub_category(game):
    """
    Determines if a game has sub categories or not
    For instance ALTTP has No Major Glitches (category) > Any% (sub category), while TMC has only Any% or 100%

    :param game: string corresponding to the name of the game
    :return: True if the given game has sub categories, False otherwise
    """
    abs_path = os.path.abspath(os.path.dirname(__file__))
    path_to_file = os.path.join(abs_path, 'ids.json')

    with open(path_to_file) as ids_json_file:
        ids_dict = json.load(ids_json_file)
        game_id = get_element_id_from_name(game)
        if game_id in ids_dict['games-categories']:
            return ids_dict['games-categories'][game_id]['has-sub-category']
        return False


def sub_categories_info(game_id, sub_category_name):
    abs_path = os.path.abspath(os.path.dirname(__file__))
    path_to_file = os.path.join(abs_path, 'ids.json')

    with open(path_to_file) as ids_json_file:
        ids_dict = json.load(ids_json_file)
        if game_id in ids_dict['games-categories']:
            sub_categories_dict = ids_dict['games-categories'][game_id]['categories']
            if sub_category_name in sub_categories_dict:
                sub_category_data = sub_categories_dict[sub_category_name]
                return sub_category_data['category'], sub_category_data['variable'], sub_category_data['sub-category']
        return None, None, None
