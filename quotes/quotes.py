import json
import random
import re


def quote_command_handling(cmd):
    """Handles a quote command

    Bound to return a string which will be displayed in the chat"""

    # !quote
    if cmd == "quote":
        return choose_random_quote()
    # !quote quote_name "quote_content" quote_author
    elif re.match(r'^quote (?P<name>\S+) "(?P<content>.+)" (?P<author>\S+)$', cmd):
        reg = re.match(r'^quote (?P<name>\S+) "(?P<content>.+)" (?P<author>\S+)$', cmd)
        return add_quote(reg.group('name'), reg.group('content'), reg.group('author'))
    # !quote quote_name "quote_content"
    elif re.match(r'^quote (?P<name>\S+) "(?P<content>.+)"$', cmd):
        reg = re.match(r'^quote (?P<name>\S+) "(?P<content>.+)"$', cmd)
        return add_quote(reg.group('name'), reg.group('content'))
    # !quote quote_name
    elif re.match(r'^quote \S+$', cmd):
        quote_command, quote_name = cmd.split(' ')
        return choose_given_quote(quote_name)


def choose_random_quote():
    """Chooses a random quote from the JSON file"""
    # FIXME: As the file is imported in ../linkobot.py, I had to add the relative path from it and not from quotes.py
    with open('quotes/quotes.json', 'r') as quotes_file:
        quotes_list = json.load(quotes_file)
        i = random.randrange(len(quotes_list))

        return format_quote(quotes_list[i]['content'], quotes_list[i]['author'])


def choose_given_quote(quote_name):
    """Chooses a quote from the JSON file given a name

    If the name is not found, then the function does nothing."""
    with open('quotes.json', 'r') as quotes_file:
        quotes_list = json.load(quotes_file)
        for quote in quotes_list:
            if quote['name'] == quote_name:
                return format_quote(quote['content'], quote['author'])


def add_quote(quote_name, content, author='Linkorange'):
    """Add a new quote to the JSON file"""
    # Should add some quotes_list variable here so it can be used out of the with scope
    with open('quotes.json', 'r+') as quotes_file:
        quotes_list = json.load(quotes_file)
        can_write_in_list = True

        for quote in quotes_list:
            if quote['name'] == quote_name:
                can_write_in_list = False
                break

        if can_write_in_list:
            quotes_list.append({'name': quote_name, 'content': content, 'author': author})
            quotes_file.seek(0)
            quotes_file.truncate()
            json.dump(quotes_list, quotes_file)
            return "Quote successfully added !"


def format_quote(content, author):
    """Formats a quote in order to display it in chat"""
    return '"' + content + '", ' + author
