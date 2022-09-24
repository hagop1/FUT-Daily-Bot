import discord
import os
import requests

#IMPORTING .ENV FILES AND PLACING THEM IN VARIABLES
from dotenv import load_dotenv
from datetime import date

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
APIKEY = os.getenv('API_KEY')
APIHOST = os.getenv('API_HOST')

#COMMAND VARIABLES
teamname = None
playername = None
tournament = None
league = None
actual_date = date.today()
# user_input_date = input()

# today = input()

url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"

querystring = {"date":actual_date}

headers = {
    "X-RapidAPI-Key": APIKEY,
    "X-RapidAPI-Host": APIHOST}

response = requests.request("GET", url, headers=headers, params=querystring)

# print(response.text)
# print(today)

responded = response.text

# DUE TO LATEST DISCORD.PY AND BOT UPDATES INTENTS NEED TO BE SET
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

#CLIENT.EVENT IS A FUNCTION STARTER. IT MUST BE USED WHEN WRITTING A FUNCTION FOR THE BOT TO RUN ON.
#ON_READY IS THE FUNCTION THAT IS USED WHEN THE BOT GOES ONLINE
# @client.event
# async def on_ready():
#     print(f'We have logged in as {client.user}')
#     print(f'Your API KEY IS {APIKEY}')

#ON_MESSAGE FUNCTION IS USED WHEN A MESSAGE IS SENT ON THE SERVER AND THE BOT READS AND DETERMINES IF IT SHOULD RESPOND.
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # if actual_today == user_input_date:
        msg = await client.wait_for("message", check=check)
        if msg.content() == actual_date:
            await ctx.send(responded)
        if message.content.startswith('/Scores {actual_date}'): #ALL SCORES FOR CURRENT DAY
            await message.channel.send(responded)
    # else:
    #     print ("Date invalid")

    if message.content.startswith('/Scores {league}'): #LEAGUE
        await message.channel.send('')
    
    if message.content.startswith('/Score {teamname}'): #TEAM-NAME
        await message.channel.send('')

    if message.content.startswith('/Player-Stats {playername}'): #PLAYER-NAME
        await message.channel.send('')

    if message.content.startswith('/standings {tournament}'): #TOURNAMENT
        await message.channel.send('')

    if message.content.startswith('/standings {league}'): #LEAGUE
        await message.channel.send('')

client.run(TOKEN)
