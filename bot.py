import discord
import os
import requests
import emoji

#IMPORTING .ENV FILES AND PLACING THEM IN VARIABLES
from dotenv import load_dotenv
from datetime import date
from discord.ext.commands import Bot
from discord import app_commands
from emoji import emojize
# from leagueCommand import *

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

#API URL'S
main_url = os.getenv('API_URL')
fixture_url = os.getenv('API_URL_FIXTURES')
standings_url = os.getenv('API_URL_STANDINGS')

headers = {
    "X-RapidAPI-Key": APIKEY,
    "X-RapidAPI-Host": APIHOST}

# url_extension = {'league-standings':
#                     {'api':

#                     }
    
#                 }


# DUE TO LATEST DISCORD.PY AND BOT UPDATES INTENTS NEED TO BE SET
intents = discord.Intents.default()
intents.message_content = True

bot = Bot("!", intents = intents)

# class aclient(discord.Client):
#     def __init__(self):
#         super().__init__(intents = discord.Intents.default())
#         self.synced = False

#     async def on_ready(self):

# client = aclient()
# tree = app_commands.CommandsTree(client)



@bot.command(name =  "tournament")
async def _command(ctx):
    await ctx.send(emoji.emojize('Which tournament?\
        \n1. World Cup :earth_americas:\
        \n2. Champions League :crown:\
        \n3. Europa League :trophy:\
        \n4. Europa Conference League :soccer:', language = 'alias'))

    @bot.event
    async def on_message(message):
        if message.content.startswith('1'):
            channel = message.channel #sets variable to same channel user message was sent
            await channel.send('test tourney')

        elif message.content.startswith('2'):
            channel = message.channel
            await channel.send('la liga')

        elif message.content.startswith('3'):
            channel = message.channel
            await channel.send('seria a')

        elif message.content.startswith('4'):
            channel = message.channel
            await channel.send('bundesliga')

        elif message.content.startswith('5'):
            channel = message.channel
            await channel.send('ligue 1') 

        await bot.process_commands(message)


@bot.command(name = "league", help='Displays standings with all details')
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
            querystring = {"season" : "2022", "league" : "1"}
            response = requests.request("GET", standings_url, headers = headers, params = querystring )
            await channel.send(response.text)

        elif message.content.startswith('2'):
            channel = message.channel
            await channel.send('la liga')

        elif message.content.startswith('3'):
            channel = message.channel
            await channel.send('seria a')

        elif message.content.startswith('4'):
            channel = message.channel
            await channel.send('bundesliga')

        elif message.content.startswith('5'):
            channel = message.channel
            await channel.send('ligue 1') 

        await bot.process_commands(message)



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
