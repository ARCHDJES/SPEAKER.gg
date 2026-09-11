import discord
from dotenv import load_dotenv
import os

load_dotenv()

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
  print("Speaker está pronto para falar")