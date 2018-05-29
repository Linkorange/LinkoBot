# LinkoBot
A personal bot on Twitch

## Command List
You can type several commands in chat preceded by a !, and the bot will react according the command.

The command list is available below :
`!bb` `!quote`*
\* Some commands are a little more complex to use so be sure to check the Detailed Command List paragraph

## Detailed command list
Here you have the detailed list of every bot command and all their uses.

#### `!bb`
Returns a link to a Google Sheets explaning everything about blue balls. The Google Sheets in question can be found [here](https://goo.gl/7MH1MG)

#### `!quote`
Manages the quotes according several commands:
```!quote```: Returns a random quote in memory
```!quote <quote_name>```: Returns a quote with the given name. If no quote is found with this name, then the command does nothing.
```!quote <quote_name> <quote_content>```: Writes a new quote for a given name. If the name already exists, then a warning message is sent to the user.
```!quote <quote_name> <quote_content> <quote_author>```: Writes a new quote for a given name and adds a precision about the author of the quote. By default, the author of the quote is 'Linkorange', aka me.