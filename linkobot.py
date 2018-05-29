import sys
import irc.bot
import requests
from quotes import quote_command_handling


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
            cmd = e.arguments[0]#.split(' ')[0][1:]
            print('Received command: ' + cmd)
            self.do_command(e, cmd[1:])
        return

    def do_command(self, e, cmd):
        c = self.connection

        if cmd.split(' ')[0] == 'bb':
            c.privmsg(self.channel, 'A sheet explaining everything about blue balls : https://goo.gl/7MH1MG')

        if cmd.split(' ')[0] == 'quote':
            c.privmsg(self.channel, quote_command_handling(cmd))


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