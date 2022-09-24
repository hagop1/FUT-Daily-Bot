import discord
import os
import requests
import emoji

#IMPORTING .ENV FILES AND PLACING THEM IN VARIABLES
from dotenv import load_dotenv
from datetime import date
from discord.ext.commands import Bot
from emoji import emojize

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

client = discord.Client(intents = intents)
bot = Bot("!", intents = intents)

#CLIENT.EVENT IS A FUNCTION STARTER. IT MUST BE USED WHEN WRITTING A FUNCTION FOR THE BOT TO RUN ON.
#ON_READY IS THE FUNCTION THAT IS USED WHEN THE BOT GOES ONLINE
# @client.event
# async def on_ready():
#     print(f'We have logged in as {client.user}')
#     print(f'Your API KEY IS {APIKEY}')


@bot.command(name = "league")
async def _command(ctx):
    await ctx.send(emoji.emojize('What league?\
        \n1. Premier League :England:\
        \n2. La Liga :Spain:\
        \n3. Seria A :Italy:\
        \n4. Bundesliga :Germany:\
        \n5. Ligue 1 :France:'))

@bot.event
async def on_message(message):
    if message.content.startswith('1'):
        channel = message.channel #sets variable to same channel user message was sent
        await channel.send('premier leagueee')
    await bot.process_commands(message)
    



    # def check(msg):
    #     return msg.author == ctx.author and \
    #     msg.channel == ctx.channel and msg.content in ["1", "2", "3", "4", "5"]

    # msg = await client.wait_for("message", check=check)
    # if msg.content() == "1": #Premier league
    #     await ctx.send("print premier league")

    # elif msg.content() == "2": #La Liga
    #     await ctx.send("print la liga")

    # elif msg.content() == "3": #Seria A
    #     await ctx.send("print seria a")

    # elif msg.content() == "4": #Bundesliga
    #     await ctx.send("print bundesliga")

    # elif msg.content() == "5": #Ligue 1
    #     await ctx.send("print ligue 1")

    # times_used = times_used + 1



#ON_MESSAGE FUNCTION IS USED WHEN A MESSAGE IS SENT ON THE SERVER AND THE BOT READS AND DETERMINES IF IT SHOULD RESPOND.
# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

#     # if actual_today == user_input_date:
#         msg = await client.wait_for("message", check=check)
#         if msg.content() == actual_date:
#             await ctx.send(responded)
#         if message.content.startswith('/Scores {actual_date}'): #ALL SCORES FOR CURRENT DAY
#             await message.channel.send(responded)
#     # else:
#     #     print ("Date invalid")

#     if message.content.startswith('/Scores {league}'): #LEAGUE
#         await message.channel.send('')
    
#     if message.content.startswith('/Score {teamname}'): #TEAM-NAME
#         await message.channel.send('')

#     if message.content.startswith('/Player-Stats {playername}'): #PLAYER-NAME
#         await message.channel.send('')

#     if message.content.startswith('/standings {tournament}'): #TOURNAMENT
#         await message.channel.send('')

#     if message.content.startswith('/standings {league}'): #LEAGUE
#         await message.channel.send('')

bot.run(TOKEN)
