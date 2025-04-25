import json

token_path = "C:\\Users\\user\\Desktop\\vs Code (Projects)\\DiscordBot\\Discord_Token.json"
#Change the path to your acc "user"

# Load the token from the JSON file
with open(token_path, 'r') as f:
    config = json.load(f)
    TOKEN = config["Geopolitical_Game_Bot_ID"]
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True 
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

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

# Run the bot 
print(f"Bot Token ID: {TOKEN}")
bot.run(TOKEN)
