import json
import discord
from discord.ext import commands

token_path = "C:\\Users\\user\\Desktop\\vs Code (Projects)\\DiscordBot\\Discord_Token.json"
data_path = "C:\\Users\\user\\Desktop\\vs Code (Projects)\\DiscordBot\\Data.json"
#Change the path to your acc "user"

# Load the token
with open(token_path, 'r') as f:
    config = json.load(f)
    TOKEN = config["Geopolitical_Game_Bot_ID"]

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

# !say command
@bot.command(name="say")
async def say(ctx, *, message: str):
    await ctx.send(message)

# !add_Data [username] [AA] [country]
@bot.command(name="add_Data")
async def add_data(ctx, username: str, aa: str, country: str):
    try:
        with open(data_path, 'r') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {"data": {"users": {}}}

    data["data"]["users"][username] = {
        "AA": aa,
        "Countrys": country
    }

    with open(data_path, 'w') as f:
        json.dump(data, f, indent=4)

    await ctx.send(f"User `{username}` added with AA: `{aa}` and country: `{country}`.")

# !remove_user [username]
@bot.command(name="remove_user")
async def remove_user(ctx, username: str):
    try:
        with open(data_path, 'r') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        await ctx.send("Data file not found or is corrupted.")
        return

    if username in data.get("data", {}).get("users", {}):
        del data["data"]["users"][username]
        with open(data_path, 'w') as f:
            json.dump(data, f, indent=4)
        await ctx.send(f"User `{username}` has been removed.")
    else:
        await ctx.send(f"User `{username}` not found.")

@bot.command(name="command_list")
async def command_list(ctx):
    commands_info = (
        "Here are all of the commands:\n"
        "`!say [message]` – echo back a message\n"
        "`!add_Data [username] [AA] [country]` – add or update a user\n"
        "`!remove_user [username]` – remove a user\n"
        "`!command_list` – show this list\n"
        "```Test``` - test"
    )
    await ctx.send(commands_info)

# Run the bot
print(f"Bot Token ID: {TOKEN}")
bot.run(TOKEN)
