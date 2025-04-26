import discord
from discord.ext import commands
import json
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

token_path = "C:\\Users\\talm\\Desktop\\vs Code (Projects)\\DiscordBot\\Discord_Token.json"

with open(token_path, 'r') as f:
    config = json.load(f)
    TOKEN = config["Jack_Bot_ID"]


# File to store the counts
DATA_FILE = 'clicks.json'

# Initialize data
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump({"love_cola": 0, "dont_love_cola": 0}, f)

def load_data():
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

class ColaView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="I love cola", style=discord.ButtonStyle.success)
    async def love_cola(self, interaction: discord.Interaction, button: discord.ui.Button):
        data = load_data()
        data["love_cola"] += 1
        save_data(data)
        await interaction.response.send_message(f"Yay! You love cola! 🥤\nTotal loves: {data['love_cola']}", ephemeral=True)

    @discord.ui.button(label="I don't love cola", style=discord.ButtonStyle.danger)
    async def dont_love_cola(self, interaction: discord.Interaction, button: discord.ui.Button):
        data = load_data()
        data["dont_love_cola"] += 1
        save_data(data)
        await interaction.response.send_message(f"Oh no! Maybe another drink? 🍹\nTotal dislikes: {data['dont_love_cola']}", ephemeral=True)

@bot.command()
async def ask(ctx):
    view = ColaView()
    await ctx.send("You have two options:", view=view)

@bot.command()
async def stats(ctx):
    data = load_data()
    await ctx.send(f"🥤 Love Cola: {data['love_cola']}\n🍹 Don't Love Cola: {data['dont_love_cola']}")

@bot.event
async def on_ready():
    print(f"Bot is ready as {bot.user}")

bot.run(TOKEN)
