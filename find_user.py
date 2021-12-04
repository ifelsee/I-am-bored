import discord
import time
from discord.ext import tasks

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@tasks.loop(seconds = 5) 
async def log():
    await client.wait_until_ready()
    for i in client.guilds:
        for channel in i.voice_channels:
            members = channel.members 
            for member in members:
                if member.id in []: 
                    print(member.name," ",channel.name )

    print("\n\n")
log.start()

client.run("",bot=False)
