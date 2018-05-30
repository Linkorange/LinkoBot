import sys
import irc.bot
import requests
from quotes.quotes import quote_command_handling
from commands.command_utils import is_cmd_in_list


class LinkoBot(irc.bot.SingleServerIRCBot):
    def __init__(self, username, client_id, token, channel):
        self.client_id = client_id
        self.token = token
        self.channel = '#' + channel

        # Get the channel ID
        url = 'https://api.twitch.tv/kraken/users?login=' + channel
        headers = {'Client-ID': client_id, 'Accept': 'application/vnd.twitchtv.v5+json'}
        r = requests.get(url, headers = headers).json()
        self.channel_id = r['users'][0]['_id']

        # Create IRC bot connection
        server = 'irc.chat.twitch.tv'
        port = 6667
        print('Connecting to ' + server + ' on port ' + str(port) + '...')
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port, 'oauth:'+token)], username, username)

    def on_welcome(self, c, e):
        print('Joining ' + self.channel + '...')
        c.cap('REQ', ':twitch.tv/membership')
        c.cap('REQ', ':twitch.tv/tags')
        c.cap('REQ', ':twitch.tv/commands')
        c.join(self.channel)
        print('Joined channel ' + self.channel)

    def on_pubmsg(self, c, e):
        if e.arguments[0][:1] == '!':
            cmd = e.arguments[0]
            print('Received command: ' + cmd)
            self.do_command(e, cmd[1:])
        return

    def do_command(self, e, cmd):
        c = self.connection

        if is_cmd_in_list(cmd, 'bb'):
            self.display_message_in_chat(c, 'A sheet explaining everything about blue balls : https://goo.gl/7MH1MG')

        if is_cmd_in_list(cmd, 'quote'):
            self.display_message_in_chat(c, quote_command_handling(cmd))

        if is_cmd_in_list(cmd, 'discord'):
            self.display_message_in_chat(c, 'Join my Discord server ! https://discord.gg/bqeugS')

        if is_cmd_in_list(cmd, 'twitter'):
            self.display_message_in_chat(c, 'Follow me on Twitter ! https://twitter.com/Linkorange')

        if is_cmd_in_list(cmd, 'yt'):
            self.display_message_in_chat(c, 'See all my videos on my Youtube channel:'
                                         + 'https://www.youtube.com/user/Linkorange')

        if is_cmd_in_list(cmd, 'youtube'):
            self.display_message_in_chat(c, 'See all my videos on my Youtube channel:'
                                         + 'https://www.youtube.com/user/Linkorange')

        if is_cmd_in_list(cmd, 'sn'):
            self.display_message_in_chat(c, 'Follow me on Twitter ! https://twitter.com/Linkorange '
                                         + 'And don\'t forget to join my Discord server :) https://discord.gg/bqeugS'
                                         + 'Also find all my videos on https://www.youtube.com/user/Linkorange')

    def display_message_in_chat(self, c, message):
        c.privmsg(self.channel, message)


def main():
    if len(sys.argv) != 5:
        print("Usage: twitchbot ")
        sys.exit(1)

    username = sys.argv[1]
    client_id = sys.argv[2]
    token = sys.argv[3]
    channel = sys.argv[4]

    bot = LinkoBot(username, client_id, token, channel)
    bot.start()


if __name__ == "__main__":
    main()