import discord
from dotenv import load_dotenv
import os
from gtts import gTTS

load_dotenv()
token = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)

@tree.command(name="tts", description="Ativa ou desativa o TTS")
async def tts(interaction):
  await interaction.response.send_message("comando enviado")

tts_ativo = True
texto = ""

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  global texto
  texto = message.content
  
  if message.author.voice:
    canal = message.author.voice.channel
    await canal.connect()
  
  if tts_ativo:
    gTTS(texto, lang='pt').save('audio.mp3')
    await message.channel.send(file=discord.File('audio.mp3'))
  
@client.event
async def on_ready():
    await tree.sync()
    print("Speaker está pronto para falar")
  
client.run(token)