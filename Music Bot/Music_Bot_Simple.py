import discord
from discord.ext import commands
import yt_dlp
import asyncio

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

FFMPEG_PATH = "C:\\Users\\user\\Desktop\\vs Code (Projects)\\Game With Xzi1Bi2t\\ffmpeg-7.1.1-full_build\\ffmpeg-7.1.1-full_build\\bin\\ffmpeg.exe"  # your ffmpeg.exe path

# yt_dlp options
ytdl_format_options = {
    'format': 'bestaudio/best',
    'quiet': True,
    'noplaylist': True,
    'default_search': 'auto',
}
# tell ffmpeg to reconnect on stream drop
ffmpeg_options = {
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
    'options': '-vn'
}

ytdl = yt_dlp.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')

    @classmethod
    async def from_url(cls, query, *, loop=None):
        loop = loop or asyncio.get_event_loop()
        # run extraction in threadpool
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(query, download=False))
        if 'entries' in data:
            data = data['entries'][0]
        return cls(
            discord.FFmpegPCMAudio(data['url'],
                                   executable=FFMPEG_PATH,
                                   before_options=ffmpeg_options['before_options'],
                                   options=ffmpeg_options['options']),
            data=data
        )

@bot.command(name="join")
async def join(ctx):
    if ctx.author.voice:
        await ctx.author.voice.channel.connect()
        await ctx.send("✅ Joined your voice channel.")
    else:
        await ctx.send("❌ You need to be in a voice channel first.")

@bot.command(name="play")
async def play(ctx, *, query: str):
    # auto-join if not already
    if ctx.voice_client is None:
        if ctx.author.voice:
            await ctx.author.voice.channel.connect()
        else:
            return await ctx.send("❌ You need to be in a voice channel.")
    # extract & prepare
    try:
        source = await YTDLSource.from_url(query, loop=bot.loop)
    except Exception as e:
        return await ctx.send(f"⚠️ Could not play: {e}")
    # stop any existing playback
    ctx.voice_client.stop()
    # play, wrapped in volume transformer so it actually comes through
    ctx.voice_client.play(source, after=lambda e: print('Player error:', e) if e else None)
    await ctx.send(f"▶️ Now playing: **{source.title}**")

@bot.command(name="leave")
async def leave(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send("👋 Left the voice channel.")
    else:
        await ctx.send("❌ I'm not connected to a voice channel.")

bot.run("MTMyNjUxMDkzMTAxODI1MjM2Mg.GPxfOe.XADwlwNzrHYBRCXzc9OiqWoLW2t4Q3mPErA_jE")
