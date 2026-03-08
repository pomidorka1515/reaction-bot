![demo](https://files.catbox.moe/3rckr8.gif)
# reaction-bot
a discord bot which automatically reacts to certain keywords
# config
 - `"token"` *(str)* - your discord bot token
 - `"reactions"` *(dict)*:
   - `"keyword"`: `<emoji type>`
   - emoji type: int (custom emoji ID), str (built-in emoji), list[int, int, int] (random emoji)
 - `"blacklist"` *(list)*: blacklist of user IDS (the bot will ignore them)
# important
you can only use custom emojis if the bot is inside the server which has that emoji (otherwise, it will fail)
probably dont use for multiple servers because it might lag

**credits to [mat](https://github.com/RadianceCascades) for the original code snippet**
