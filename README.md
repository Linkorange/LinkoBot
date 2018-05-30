
# LinkoBot  
A personal, orange bot on Twitch  
  
## Command List  
You can type several commands in chat preceded by a !, and the bot will react according the command.  
  
The command list is available below :  
`!bb` `!quote`\* `discord` `twitter` `youtube` `yt` `sn` `media` `social` `mstut` `z2tut` `aoltut` `pbs` `highlights` 
  
\* Some commands are a little more complex to use so be sure to check the Detailed Command List paragraph below.  
  
## <a name="detailed"></a>Detailed command list  
Here you have the detailed list of every bot command and all their use cases.  
  
#### `!bb`  
Returns a link to a Google Sheets explaning everything about blue balls. The Google Sheets in question can be found [here](https://goo.gl/7MH1MG)  
  
#### `!quote`  
Manages the quotes according several commands:  
  
```!quote```: Returns a random quote from the current [quotes.json] file.  
  
```!quote <quote_name>```: Returns a quote with the given name from the current [quotes.json] file. If no quote is found with this name, then the command does nothing.  
  
```!quote <quote_name> "<quote_content>"```: Writes a new quote for a given name. If the name already exists, then a warning message is sent to the user.
  
```!quote <quote_name> "<quote_content>" <quote_author>```: Writes a new quote for a given name and adds a precision about the author of the quote. By default, the author of the quote is 'Linkorange', aka me.  

```!quote <quote_name> "<quote_content>" <quote_author> <quote_year>```: Writes a new quote for a given name and adds a precision about the author of the quote and the year it was spoken. By default, the year is the current year. 

**Important note** : the double quotes surrounding the quote content are mandatory, otherwise the command will not be recognized.
  
[quotes.json]: <quotes/quotes.json>

#### `!discord`
Posts an invite link to the Discord server related to my Twitch channel.

#### `!twitter`
Posts a link to my Twitter account.

#### `!youtube` and `!yt`
Posts a link to my Youtube channel.

#### `!sn`, `!media` and `!social`
Provides the links to the social networks I can be found at, which currently are Discord, Twitter, and Youtube.

#### `!mstut`
Gives a link to a French tutorial video series of the Master Sword category in ALTTP

#### `!z2tut` and `!aoltut`
Gives a link to a French tutorial video series of the 100% All Keys category in Zelda II - The Adventure of Link

#### `!pbs`
Provides a link to a Youtube playlist containing all my currents PBs, which is up to date compared to the data of speedrun.com sometimes.

#### `!highlights`
Provides a link to a Youtube playlist containing all my stream highlights. In the future, a more interactive command surrounding highlights via Twitch API will be developed.
