import discord
from dpyConsole import Console
import sys

client = discord.Client(intents=discord.Intents.all())
my_console = Console(client)
    

reason = {1: "10m küfür",
              2: "20m adk",
              3: "10m ortam bozma",
              4: "5m uzatma",
              5: "15m kışkırtma",
              6: "90m manevi"}

pr_reason= lambda : (print(),[print(f"{x}) {y}") for x,y in reason.items()],print())

@client.event
async def on_ready():
    print("Ready")
    pr_reason()


@my_console.command()
async def v(*args):  
    channel= client.get_guild(538038727654768652).get_channel(710931359798919250)
    if len(args) != 2: pr_reason(); return 0 

    u_id, n = [int(i) for i in args] 

    await channel.send(f"!vmute {args[0]} {reason[n]}")
    print(f"{client.get_user(u_id)} kullanıcısına {reason[n][:3]} mute atıldı")


async def my_vchannel():
    for channel in client.get_guild(538038727654768652).voice_channels:
        for member in channel.members:
            if member.id == 386479423693651969: return channel
 
async def target_member(flag):
    vchannel = await my_vchannel()
    for member in vchannel.members:
        if "Atlantis Bot Komut" not in [str(i) for i in member.roles]:
            if flag == True: await member.edit(mute = "True")
            else: await member.edit(mute = "False")


@my_console.command()
async def god():
    await target_member(True)

@my_console.command()
async def ungod():
    await target_member(False)


     
        

        

my_console.start() 
client.run("",bot=False)
