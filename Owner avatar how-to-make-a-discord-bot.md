# how-to-make-a-discord-bot
1) go to: https://discord.com/developers/applications
2) then click on: "New application"
3) give it a name a allow it
4) give your bot icon
5) go to Tags and add tag: "*test" (*you can put any tag that u want, or not put one at all)
6) Now go to "Bot"
7) in "Bot", Turn on: Public Bot, Message Content Intent, Server Members Intent, Presence Intent then click on "Save Changes"
8) now go to "OAuth2" in the "OAuth2 URL Generator", in the Scopes select "Bot" then go to "Bot Permissions" in it give him Administrator
9) skroll down, make sure that Integration Type is "Guild Install", then copy the url   
10) open the url, in google login and add him to the server. 
11) make a folder in the desktop, give it a name, then open the folder with vs code.
12) after that make a file call it whater you want (remember the end is .py), copy the Basic code:
13) remember to replace the token with your bot token (TOKEN = 'Your Bot Token') 
14) to get your bot token you need to go to https://discord.com/developers/applications, then the bot, then click on the "Reset Token" button enter your password, copy and past it in the code
---------------------------------------------------
Basic Code:
---------------------------------------------------
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True 
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)
TOKEN = 'Your Bot Token'

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name='general')
    if channel:
        await channel.send(f"Welcome {member.mention}!")

@bot.command(name="say")
async def say(ctx, *, message: str):
    try:
        await ctx.send(message)
    except Exception as e:
        print(f"Error: {e}")
        await ctx.send("There was an error processing your message.")

print(f"Bot Token ID: {TOKEN}")
bot.run(TOKEN)
---------------------------------------------------
