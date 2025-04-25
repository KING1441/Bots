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
import discord \n
from discord.ext import commands \n
\n
intents = discord.Intents.default() \n
intents.members = True \n
intents.message_content = True \n
bot = commands.Bot(command_prefix="!", intents=intents) \n
TOKEN = 'Your Bot Token' \n
\n
@bot.event \n
async def on_ready(): \n
    print(f'Logged in as {bot.user}') \n
\n
@bot.event \n
async def on_member_join(member):\n
    channel = discord.utils.get(member.guild.text_channels, name='general')\n
    if channel:\n
        await channel.send(f"Welcome {member.mention}!")\n
\n
@bot.command(name="say")\n
async def say(ctx, *, message: str):\n
    try:\n
        await ctx.send(message)\n
    except Exception as e:\n
        print(f"Error: {e}")\n
        await ctx.send("There was an error processing your message.")\n
\n
print(f"Bot Token ID: {TOKEN}")\n
bot.run(TOKEN)\n

---------------------------------------------------

15) To get your bot token, go back to https://discord.com/developers/applications
16) Click on your application
17) Go to the "Bot" tab
18) Click "Reset Token", enter your password
19) Copy and paste the token into your code where it says 'Your Bot Token'


