
  
    
# TheLinkoBot  
Because it's not just a random LinkoBot. It is THE LinkoBot.      
      
## Command List  
You can type several commands in chat preceded by a !, and the bot will react according the command.      
      
The command list is available below :      
`!help`\* `!bb` `!quote`\* `!discord` `!twitter` `!youtube` `!yt` `!sn` `!media` `!social` `!mstut` `!z2tut` `!aoltut` `!pbs` `!highlights` `!roll`\* `!pb`\*    

\* Some commands are a little more complex to use so be sure to check the Detailed Command List paragraph below.

      
      
## <a name="detailed"></a>Detailed command list  
Here you have the detailed list of every bot command and all their use cases.      
    
#### `!help` 
Provides the link to this README.md file. Also if you type `!help <command>` in chat, it will give you basic information about the given command.    
      
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
  
#### `!roll`  
Rolls one or more dices and displays the results in chat. Two commands are available :  
  
```!roll```: Rolls one six-sided dice.  
  
```!roll <n>d<p>```: Rolls a p-sided dice n times. For instance, the command ```!roll 3d20``` will roll a 20-sided dice then give the following result : ```2 17 11```.  
  
**Important note :** The max number of rolls is 9. The max size of a dice is 100. Thus, the commands ```!roll 2d101``` or ```!roll 10d10``` will not provide any result. This is in order to prevent spam.

#### `!pb`
Posts information about a personal best. By default, the PB given is my PB on the current game and category I'm doing on stream. But there is more :

`!pb` : Posts information about my personal best for the current game / category

`!pb <game> <category>` : Posts information about my personal best for a given game and category. Only the game/category I run are available (this command is not supposed to bring in all the data in speedrun.com API !)

`!pb <game> <category> <player>` : Posts information about the personal best of the given player for a given game and category. Only the game/category I run are available (therefore, you cannot access to someone's PB if I don't run their run/category).

**Note about typing issues :** I am aware that it's not clear what to type in the command to be sure to hit the right game or the right category (or sometimes the right player).

As such, I registered some players's usual nicknames, as well as each game's most used abbreviations. For categories though, only one code will work for each of them ; no big deal, you'll be able to find those codes in the paragraph "About games and categories" below.

For the rest, you'll be able to find this information in ids.json .

[ids.json]: <speedrun_com_api/ids.json>

## About games and categories
Here is the list of all the games and categories I run, with every category code.

#### Category codes

- ALTTP NMG Any% : `nmg`
- ALTTP NMG Low% : `low`
- ALTTP NMG Master Sword : `ms`
- ALTTP Low% OHKO : `ohko` (for the game, type for instance `alttpce` instead of `alttp` !)
- LADX Any% No S+Q/WW/OOB : `nosqwwoob`
- Zelda II 100% All Keys : `100ak`
- The Legend of Zelda Any% No Up+A : `noupa`
- The Legend of Zelda 2 players 1 controller : `2p1c` (for the game, type for instance `z1ce` instead of `z1` !)
- The Minish Cap Any% : `any`

#### About game names
I tried to insert the most used abbreviations for each game. For instance, for the game *The Legend of Zelda - A Link to the Past*, you can type `alttp`, `lttp`, or even `z3` and it will work.

Be careful that some games have a Category Extensions page on speedrun.com, which is considered as a different game from the original. This is why sometimes you need to type `-ce` after a game name to get data about a category. The concerned categories are detailed in the paragraph above.
