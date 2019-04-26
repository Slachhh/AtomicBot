import discord
from discord.ext import commands
from discord.voice_client import VoiceClient

startup_extensions= ["Music" ]
bot = commands.Bot("?")

@bot.event
async def on_ready():
    print("bot online")


class Main_Commands():
    def init(self, bot):
        self.bot=bot

@bot.command(pass_context=True)
async def pagan(ctx):
    await bot.say('We Have Pagan :sunglasses: ')


@bot.command(pass_context=True)
async def hola(ctx):
    await bot.say("Que Pagan te bendiga :sunglasses: ")



bot.run("BOT_TOKEN")
