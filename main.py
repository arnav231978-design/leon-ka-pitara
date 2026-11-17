
import os
import discord
from discord import app_commands

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.members = True

class LeonBot(discord.Client):
    def __init__(self):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()
        print("Slash commands synced!")

bot = LeonBot()

@bot.event
async def on_ready():
    print(f"Leon Ka Pitara is online as {bot.user}")

@bot.tree.command(name="ping", description="Check if Leon Ka Pitara is online")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(
        "💜 Leon Ka Pitara is online and ready!"
    )

if not TOKEN:
    raise RuntimeError("DISCORD_TOKEN is missing!")

bot.run(TOKEN)
      
