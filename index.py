import discord
from dotenv import load_dotenv
import os
from gtts import gTTS

load_dotenv()
token = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

tts_ativo = True
texto = ""

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  global texto
  texto = message.content
  
  if tts_ativo:
    gTTS(texto, lang='pt').save('audio.mp3')
    await message.channel.send(file=discord.File('audio.mp3'))
  
@client.event
async def on_ready():
  print("Speaker está pronto para falar")
  
client.run(token)