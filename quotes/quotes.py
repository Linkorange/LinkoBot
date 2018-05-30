import json
import random
import re
import datetime


def quote_command_handling(cmd):
    """Handles a quote command

    Bound to return a string which will be displayed in the chat"""

    # !quote
    if cmd == "quote":
        return choose_random_quote()
    # !quote quote_name "quote_content" quote_author quote_year
    elif re.match(r'^quote (?P<name>\S+) "(?P<content>.+)" (?P<author>\S+) (?P<year>\d{4})$', cmd):
        reg = re.match(r'^quote (?P<name>\S+) "(?P<content>.+)" (?P<author>\S+) (?P<year>\d{4})$', cmd)
        return add_quote(reg.group('name'), reg.group('content'), reg.group('author'), int(reg.group('year')))
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
        quotes_dict = json.load(quotes_file)
        random_quote = quotes_dict[random.choice(list(quotes_dict.keys()))]

        return format_quote(random_quote['content'], random_quote['author'],
                            random_quote['year'])


def choose_given_quote(quote_name):
    """Chooses a quote from the JSON file given a name

    If the name is not found, then the function does nothing."""
    with open('quotes/quotes.json', 'r') as quotes_file:
        quotes_dict = json.load(quotes_file)
        if quote_name in quotes_dict.keys():
            quote = quotes_dict[quote_name]
            return format_quote(quote['content'], quote['author'], quote['year'])
        return ''


def add_quote(quote_name, content, author='Linkorange', year=datetime.datetime.now().year):
    """Add a new quote to the JSON file"""
    # Should add some quotes_dict variable here so it can be used out of the with scope
    with open('quotes/quotes.json', 'r+') as quotes_file:
        quotes_dict = json.load(quotes_file)

        if quote_name in quotes_dict.keys():
            return "Cannot write this quote - name already exists !"

        quotes_dict[quote_name] = {'content': content, 'author': author, 'year': year}
        quotes_file.seek(0)
        quotes_file.truncate()
        json.dump(quotes_dict, quotes_file)
        return "Quote successfully added !"


def format_quote(content, author, year):
    """Formats a quote in order to display it in chat"""
    return '"' + content + '", ' + str(year) + ', ' + author
