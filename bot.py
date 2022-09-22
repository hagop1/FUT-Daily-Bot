import discord
import os

#IMPORTING .ENV FILES AND PLACING THEM IN VARIABLES
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
APIKEY = os.getenv('API_KEY')

# DUE TO LATEST DISCORD.PY AND BOT UPDATES INTENTS NEED TO BE SET
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

#CLIENT.EVENT IS A FUNCTION STARTER. IT MUST BE USED WHEN WRITTING A FUNCTION FOR THE BOT TO RUN ON.
#ON_READY IS THE FUNCTION THAT IS USED WHEN THE BOT GOES ONLINE
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    print(f'Your API KEY IS {APIKEY}')

#ON_MESSAGE FUNCTION IS USED WHEN A MESSAGE IS SENT ON THE SERVER AND THE BOT READS AND DETERMINES IF IT SHOULD RESPOND.
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$blig'):
        await message.channel.send('Hello!')

    if message.content.startswith('/Scores'):
        await message.channel.send('')
    
    if message.content.startswith('/Score {}'): #TEAM-NAME
        await message.channel.send('')

    if message.content.startswith('/Player-Stats {}'): #PLAYER-NAME
        await message.channel.send('')

    if message.content.startswith('/standings {}'): #TOURNAMENT
        await message.channel.send('')

client.run(TOKEN)
