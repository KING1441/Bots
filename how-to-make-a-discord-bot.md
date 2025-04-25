# how-to-make-a-discord-bot
1) Go to: https://discord.com/developers/applications.
2) Then click on: "New application".
3) Give it a name and click Create.
4) Give your bot an icon (optional).
5) Go to Tags and add a tag like *test (*you can put any tag you want, or none at all).
6) Now go to "Bot".
7) in "Bot" section, Turn on: Public Bot, Message Content Intent, Server Members Intent, Presence Intent then click on "Save Changes".
8) Go to "OAuth2", then to the "OAuth2 URL Generator, in the Scopes select: "Bot", In Bot Permissions, select: "Administrator".
9) Scroll down and make sure Integration Type is set to Guild Install, then copy the generated URL.  
10) Open the URL in your browser, log in with your Discord account, and add the bot to your server. 
11) Make a folder on your desktop and give it a name.
12) Open the folder in VS Code
13) Create a Python file (call it whatever you want, just make sure it ends with .py
14) Copy and paste this basic bot code:

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
\n
@bot.command(name="say")\n
async def say(ctx, *, message: str):
    try:
        await ctx.send(message)
    except Exception as e:
        print(f"Error: {e}")
        await ctx.send("There was an error processing your message.")

print(f"Bot Token ID: {TOKEN}")
bot.run(TOKEN)

---------------------------------------------------

15) To get your bot token, go back to https://discord.com/developers/applications
16) Click on your application
17) Go to the "Bot" tab
18) Click "Reset Token", enter your password
19) Copy and paste the token into your code where it says 'Your Bot Token'


