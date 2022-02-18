#Template to get XP every message and automatically levels up
import leveling

@client.event
async def on_message(message):
    lvlmember = message.author.id
    leveling.addxp(lvlmember,"1")
    Level = leveling.getlvl(lvlmember)
    if int(leveling.getxp(lvlmember)) > 10:
        leveling.addlvl(lvlmember,"1")
        Level = leveling.getlvl(lvlmember)
        await message.channel.send(f"{message.author.mention} Ranked up to Level {Level}")
    
    await client.process_commands(message)