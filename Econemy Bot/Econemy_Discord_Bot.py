import discord 
import random
import json
import time
from discord.ext import commands 

image_path = 'C:\\Users\\talm\\Desktop\\vs Code (Projects)\\Game With Xzi1Bi2t\\Money.json'
DATA_FILE = 'C:\\Users\\talm\\Desktop\\vs Code (Projects)\\Game With Xzi1Bi2t\\Money.json'
token_path = "C:\\Users\\talm\\Desktop\\vs Code (Projects)\\DiscordBot\\Discord_Token.json"

with open(token_path, 'r') as f:
    config = json.load(f)
    TOKEN = config["Econemy_Bot_ID"]

shop_items = {
    "bread": 50,
    "pizza": 100,
    "level+": 200
}

rob_targets = {
    1: ("Old Lady",           100),
    2: ("Grocery Store",      250),
    3: ("Bank",               5000),
    4: ("Lemonade Stand",     300),
    5: ("House",              1000),
    6: ("Casino Vault",       2500),
    7: ("ATM",                400),
    8: ("Jewelry Store",      600),
    9: ("Luxury Car Dealership", 1650),
   10: ("Rich Friend",       25090),
}

intents = discord.Intents.default() 
intents.members = True 
intents.message_content = True 
bot = commands.Bot(command_prefix="!", intents=intents) 


def load_data():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

@bot.event 
async def on_ready(): 
    print(f'Logged in as {bot.user}') 

@bot.event 
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name='general')
    if channel:
        await channel.send(f"Welcome {member.mention}!")

@bot.command(name="rob")
async def rob_command(ctx):
    user = str(ctx.author.name)
    data = load_data()

    # Pick a random target
    target_id = random.randint(1, 10)
    target_name, reward = rob_targets[target_id]

    await ctx.send(f"{ctx.author.mention} is attempting to rob **{target_name}**…")
    time.sleep(1)

    # Ensure user exists
    if user not in data["Users"]:
        data["Users"][user] = {"Money": "0", "Level": "1"}

    user_money = int(data["Users"][user]["Money"])

    # 10% success chance
    if random.random() < 0.25:
        data["Users"][user]["Money"] = str(user_money + reward)
        save_data(data)
        await ctx.send(
            f"🎉 Success! You stole 💰 {reward} coins from the **{target_name}**!\n"
            f"You now have 💰 {data['Users'][user]['Money']} coins."
        )
    else:
        # Only remove money if user has enough
        lost_amount = min(user_money, reward)
        data["Users"][user]["Money"] = str(user_money - lost_amount)
        save_data(data)
        await ctx.send(
            f"❌ Robbery failed! You were caught trying to rob the **{target_name}** and lost 💰 {lost_amount} coins.\n"
            f"Your new balance is 💰 {data['Users'][user]['Money']} coins.")
        
@bot.command(name="say")
async def say(ctx, *, message: str):
    try:
        await ctx.send(message)
    except Exception as e:
        print(f"Error: {e}")
        await ctx.send("There was an error processing your message.")

@bot.command()
async def send_image_url(ctx):
    image_url = "https://s.namemc.com/2d/skin/face.png?id=3fca76a5129a4626&scale=4"
    await ctx.send("Check this out!", embed=discord.Embed().set_image(url=image_url))


#Can send files too like .json and more! need to change image_path
@bot.command()
async def send_photo(ctx):
    with open(image_path, 'rb') as f:
        picture = discord.File(f)
        await ctx.send("Here's a cool image!", file=picture)


@bot.command(name="work")
async def work_command(ctx):
    user = str(ctx.author.name)  # use username (you can also use str(ctx.author.id) for safer IDs)
    data = load_data()
    
    # If user not in data, add them
    if user not in data["Users"]:
        data["Users"][user] = {
            "Money": "0",
            "Level": "1"
        }

    # Add random amount of money
    amount = random.randint(10, 100)
    current_money = int(data["Users"][user]["Money"])
    data["Users"][user]["Money"] = str(current_money + amount)

    save_data(data)
    await ctx.send(f"{ctx.author.mention}, you worked and earned 💰 {amount} coins! You now have 💰 {data['Users'][user]['Money']} coins.")

#!give 30 player_test
@bot.command(name="give")
async def give_command(ctx, player_name: str, amount: int):
    data = load_data()
    sender = str(ctx.author.name)

    if sender not in data["Users"]:
        await ctx.send(f"{ctx.author.mention}, you need to work first before giving coins!")
        return

    if player_name not in data["Users"]:
        await ctx.send(f"{ctx.author.mention}, the player `{player_name}` does not exist.")
        return

    sender_money = int(data["Users"][sender]["Money"])
    if sender_money < amount:
        await ctx.send(f"{ctx.author.mention}, you don't have enough coins to give {amount}.")
        return

    # Transfer money
    data["Users"][sender]["Money"] = str(sender_money - amount)
    receiver_money = int(data["Users"][player_name]["Money"])
    data["Users"][player_name]["Money"] = str(receiver_money + amount)

    save_data(data)
    await ctx.send(f"{ctx.author.mention} gave 💰 {amount} coins to `{player_name}`.")

@bot.command(name="about")
async def about_command(ctx, player_name: str):
    data = load_data()

    if player_name not in data["Users"]:
        await ctx.send(f"{ctx.author.mention}, the player `{player_name}` does not exist.")
        return

    money = data["Users"][player_name]["Money"]
    level = data["Users"][player_name]["Level"]

    await ctx.send(
        f"**📄 Player Info:**\n"
        f"👤 Player: `{player_name}`\n"
        f"💰 Money: {money} coins\n"
        f"🆙 Level: {level}"
    )

@bot.command(name="command_list")
async def command_list(ctx):
    commands_text = (
        "**📜 Available Commands:**\n"
        "🔹 `!work` - Work and earn a random amount of coins.\n"
        "🔹 `!balance` - Check how many coins you have.\n"
        "🔹 `!give <player> <amount>` - Give coins to another player.\n"
        "🔹 `!about <player>` - View another player's money and level.\n"
        "🔹 `!shop` - View items available in the shop.\n"
        "🔹 `!buy <item>` - Buy an item from the shop.\n"
        "🔹 `!reset` - Reset your profile (admin only).\n"
        "🔹 `!say <message>` - Make the bot say something.\n"
        "🔹 `!command_list` - Show all available commands."
    )
    await ctx.send(commands_text)

@bot.command(name="shop")
async def shop_command(ctx):
    shop_text = "**🛒 Shop Items:**\n"
    for item, price in shop_items.items():
        shop_text += f"- {item} = 💰 {price} coins\n"
    shop_text += "\nUse `!buy <item>` to purchase something!"
    await ctx.send(shop_text)

@bot.command(name="buy")
async def buy_command(ctx, item_name: str):
    user = str(ctx.author.name)
    item_name = item_name.lower()
    if item_name not in shop_items:
        await ctx.send(f"{ctx.author.mention}, that item doesn't exist in the shop.")
        return
    data = load_data()
    if user not in data["Users"]:
        await ctx.send(f"{ctx.author.mention}, you need to work first with `!work`!")
        return
    user_money = int(data["Users"][user]["Money"])
    item_cost = shop_items[item_name]
    if user_money < item_cost:
        await ctx.send(f"{ctx.author.mention}, you don't have enough coins to buy {item_name}.")
        return
    # Deduct money
    data["Users"][user]["Money"] = str(user_money - item_cost)
    # If item is level+
    if item_name == "level+":
        current_level = int(data["Users"][user]["Level"])
        data["Users"][user]["Level"] = str(current_level + 1)
        message = f"You bought **{item_name}** and leveled up to 🆙 Level {data['Users'][user]['Level']}!"
    else:
        message = f"You bought **{item_name}** for 💰 {item_cost} coins!"
    save_data(data)
    await ctx.send(f"{ctx.author.mention}, {message}")

@bot.command(name="reset")
@commands.has_permissions(administrator=True)
async def reset_command(ctx):
    user = str(ctx.author.name)
    data = load_data()
    if user not in data["Users"]:
        await ctx.send(f"{ctx.author.mention}, you have no data to reset.")
        return
    data["Users"][user]["Money"] = "0"
    data["Users"][user]["Level"] = "1"
    save_data(data)
    await ctx.send(f"{ctx.author.mention}, your profile has been reset: 💰 0 coins, 🆙 Level 1.")

@reset_command.error
async def reset_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"{ctx.author.mention}, you need to be an **admin** to use `!reset`.")

@bot.command(name="balance")
async def balance_command(ctx):
    user = str(ctx.author.name)
    data = load_data()

    if user not in data["Users"]:
        data["Users"][user] = {
            "Money": "0",
            "Level": "1"
        }
        save_data(data)

    money = data["Users"][user]["Money"]
    await ctx.send(f"{ctx.author.mention}, you have 💰 {money} coins.")

print(f"Bot Token ID: {TOKEN}")
bot.run(TOKEN)