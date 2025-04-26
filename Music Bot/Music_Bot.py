import discord
from discord.ext import commands
from discord import app_commands
import json
import random
import yt_dlp
import asyncio
import logging

GUILD_ID = discord.Object(id=1334196633445072918) #Change it to a server ID


#
#error for the bot:
# check the server id need to match your server
# first look for the path: click on ctrl + f, sartch vc.play change the path
# ask chatgpt for help send him errors and the code


# Initialize bot and logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

games = {}
queue = []

# Use commands.Bot with intents
intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix="!", intents=intents)

class MusicPlayer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        # Reconnect if the bot disconnects unintentionally
        if member == self.bot.user and before.channel is not None and after.channel is None:
            if not self.explicit_disconnect:
                try:
                    await asyncio.sleep(1)  # Small delay before reconnecting
                    await before.channel.connect()
                except discord.ClientException:
                    print("Failed to reconnect to the voice channel.")
            else:
                # Reset the flag after intentional disconnection
                self.explicit_disconnect = False

    @app_commands.command(name="join", description="Join the user's current voice channel.")
    async def join(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)

        if interaction.user.voice is None:
            await interaction.followup.send("You need to be in a voice channel to use this command.")
            return

        channel = interaction.user.voice.channel
        try:
            await channel.connect(reconnect=True)
            await interaction.followup.send(f"Joined {channel} successfully!")
        except discord.ClientException as e:
            await interaction.followup.send(f"Error: {e}")
        except Exception as e:
            await interaction.followup.send(f"An unexpected error occurred: {e}")

    @app_commands.command(name="play", description="Play a song")
    async def play(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)

        vc = interaction.guild.voice_client
        if vc is None:
            await interaction.followup.send("I need to be in a voice channel to play a song.")
            return

        if not queue:
            await interaction.followup.send("Please download a song first.")
            return

        audio_file = queue.pop(0)
        if vc.is_playing():
            vc.stop()
        
        vc.play(discord.FFmpegPCMAudio(audio_file, executable="C:\\Users\\talm\\Desktop\\vs Code (Projects)\\Game With Xzi1Bi2t\\ffmpeg-7.1.1-full_build\\ffmpeg-7.1.1-full_build\\bin\\ffmpeg.exe"), after=lambda e: logger.info(f"Finished playing: {e}"))
        await interaction.followup.send(f"Now playing: {audio_file}")

    @app_commands.command(name="download", description="Download a song from YouTube")
    async def download(self, interaction: discord.Interaction, url: str):
        await interaction.response.defer(ephemeral=True)

        if interaction.guild.voice_client is None:
            await interaction.followup.send("I need to be in a voice channel to download a song.")
            return

        options = {
    "format": "bestaudio/best",
    "ffmpeg_location": "C:\\Users\\talm\\Desktop\\vs Code (Projects)\\Game With Xzi1Bi2t\\ffmpeg-7.1.1-full_build\\ffmpeg-7.1.1-full_build\\bin\\ffmpeg.exe",  # <-- Replace this!
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "opus",
            "preferredquality": "192",
        }
    ],
    "outtmpl": "downloads/%(title)s.%(ext)s",
    "quiet": True,
}


        try:
            with yt_dlp.YoutubeDL(options) as ydl:
                info = ydl.extract_info(url, download=True)
                audio_file = ydl.prepare_filename(info).rsplit(".", 1)[0] + ".opus"

            queue.append(audio_file)
            await interaction.followup.send(f"Downloaded and added to the queue: {audio_file}")
        except Exception as e:
            await interaction.followup.send(f"Failed to download the audio: {e}")

    @app_commands.command(name="leave", description="Leave the voice channel")
    async def leave(self, interaction: discord.Interaction):
        if interaction.guild.voice_client:
            self.explicit_disconnect = True  # Set the flag for intentional disconnection
            await interaction.guild.voice_client.disconnect()
            await interaction.response.send_message("Disconnected from the voice channel!")
        else:
            await interaction.response.send_message("I'm not in a voice channel.", ephemeral=True)

    @app_commands.command(name="pause", description="Pauses the song")
    async def pause(self, interaction: discord.Interaction):
        if interaction.guild.voice_client:
            if interaction.guild.voice_client.is_playing():
                interaction.guild.voice_client.pause()
                await interaction.response.send_message("Paused the song!")
            else:
                await interaction.response.send_message("The song is already paused.", ephemeral=True)
        else:
            await interaction.response.send_message("I'm not in a voice channel.", ephemeral=True)

    @app_commands.command(name="resume", description="Resumes the song")
    async def resume(self, interaction: discord.Interaction):
        if interaction.guild.voice_client:
            if interaction.guild.voice_client.is_paused():
                interaction.guild.voice_client.resume()
                await interaction.response.send_message("Resumed the song!")
            else:
                await interaction.response.send_message("The song is already playing.", ephemeral=True)
        else:
            await interaction.response.send_message("I'm not in a voice channel.", ephemeral=True)
    
    @app_commands.command(name="queue", description="Displays the current queue")
    async def queue(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"The queue is: {queue}")

    @app_commands.command(name="stop", description="Stops the music")
    async def stop(self, interaction: discord.Interaction):
        if interaction.guild.voice_client:
            interaction.guild.voice_client.stop()
            await interaction.response.send_message("Stopped the music!")
        else:
            await interaction.response.send_message("I'm not in a voice channel.", ephemeral=True)
    
    @app_commands.command(name="remove", description="Removes a song from the list")
    async def remove(self, interaction: discord.Interaction, index: int):
        if interaction.guild.voice_client:
            if 0 <= index < len(queue):
                audio_file = queue.pop(index)
                await interaction.response.send_message(f"Removed {audio_file} from the queue")
            else:
                await interaction.response.send_message("Invalid index", ephemeral=True)
        else:
            await interaction.response.send_message("I'm not in a voice channel.", ephemeral=True)

    async def cog_load(self):
        self.bot.tree.add_command(self.join, guild=GUILD_ID)
        self.bot.tree.add_command(self.play, guild=GUILD_ID)
        self.bot.tree.add_command(self.download, guild=GUILD_ID)
        self.bot.tree.add_command(self.leave, guild=GUILD_ID)
        self.bot.tree.add_command(self.pause, guild=GUILD_ID)
        self.bot.tree.add_command(self.resume, guild=GUILD_ID)
        self.bot.tree.add_command(self.queue, guild=GUILD_ID)
        self.bot.tree.add_command(self.stop, guild=GUILD_ID)
        self.bot.tree.add_command(self.remove, guild=GUILD_ID)


# Register the cog in the client
@client.event
async def on_ready():
    logger.info(f"Logged in as {client.user}")
    try:
        if "MusicPlayer" not in client.cogs:
            await client.add_cog(MusicPlayer(client))
        await client.tree.sync(guild=GUILD_ID)
        logger.info("Commands synced successfully!")
    except Exception as e:
        logger.error(f"Error during on_ready setup: {e}")


@client.tree.command(name="add_data", description="Registers data.", guild=GUILD_ID)
async def addData(interaction: discord.Interaction, user: str, password: str):
    try:
        with open("data.json", "r") as file:
            data = json.load(file)

        if user in data["users"]:
            await interaction.response.send_message("This user already exists")
            return

        data["users"][user] = {"username": user, "password": password}

        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)

        await interaction.response.send_message("User registered successfully")
    except Exception as e:
        logger.error(f"Error: {e}")


@client.tree.command(name="remove_data", description="Removes data.", guild=GUILD_ID)
async def removeData(interaction: discord.Interaction, user: str):
    try:
        with open("data.json", "r") as file:
            data = json.load(file)

        if user not in data["users"]:
            await interaction.response.send_message("This user does not exist")
            return

        del data["users"][user]

        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)

        await interaction.response.send_message("Data removed successfully")
    except Exception as e:
        logger.error(f"Error: {e}")


@client.tree.command(name="command_list", description="Lists all of the commands.", guild=GUILD_ID)
async def listCommands(interaction: discord.Interaction):
    commands = [cmd.name for cmd in client.tree.get_commands(guild=GUILD_ID)]
    command_str = "\n".join(commands)
    await interaction.response.send_message(f"Here are all of the slash commands:\n```\n{command_str}\n```")


@client.tree.command(name="start_guess", description="Start a guessing game!", guild=GUILD_ID)
async def start_guess(interaction: discord.Interaction):
    if interaction.user in games:
        await interaction.response.send_message("You are already in a game")
        return
    games[interaction.user] = {"number": random.randint(1, 100), "attempts": 0}
    await interaction.response.send_message("Guess a number between 1 and 100")


@client.tree.command(name="guess", description="Guess a number", guild=GUILD_ID)
async def guess(interaction: discord.Interaction, guess: int):
    if interaction.user not in games:
        await interaction.response.send_message("You need to start a game first")
        return
    answer = games[interaction.user]["number"]
    games[interaction.user]["attempts"] += 1
    if guess > answer:
        await interaction.response.send_message("Too high")
    elif guess < answer:
        await interaction.response.send_message("Too low")
    else:
        await interaction.response.send_message(f"Congratulations! You guessed the number in {games[interaction.user]['attempts']} attempts")
        games.pop(interaction.user)


@client.tree.command(name="stop_guessing", description="Stop your guessing game", guild=GUILD_ID)
async def stop_guessing(interaction: discord.Interaction):
    if interaction.user not in games:
        await interaction.response.send_message("You are not in a game")
        return
    games.pop(interaction.user)
    await interaction.response.send_message("Game stopped")


# Run the bot
try:
    client.run('MTMyNjUxMDkzMTAxODI1MjM2Mg.GPxfOe.XADwlwNzrHYBRCXzc9OiqWoLW2t4Q3mPErA_jE')
except Exception as e:
    logger.error(f"An error occurred while running the bot: {e}")