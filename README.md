# reaction-bot
a discord bot which automatically reacts to certain keywords
# config
 - `"token"` *(str)* - your discord bot token
 - `"reactions"` *(dict)*:
   - `"keyword"`: `<emoji type>`
   - emoji type: int (custom emoji ID), str (built-in emoji), list[int, int, int] (random emoji)
 - `"blacklist"` *(list)*: blacklist of users (the bot will ignore them)
   
