import discord
import os
import requests
import emoji
# import urllib.request

#IMPORTING .ENV FILES AND PLACING THEM IN VARIABLES
from dotenv import load_dotenv
from datetime import date
from discord.ext.commands import Bot
from discord import app_commands
from emoji import emojize

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
APIKEY = os.getenv('API_KEY')
APIHOST = os.getenv('API_HOST')

#VARIABLES
actual_date = date.today()


#API URL'S
main_url = os.getenv('API_URL')
leagues_url = os.getenv('API_URL_LEAGUES')
fixture_url = os.getenv('API_URL_FIXTURES')
standings_url = os.getenv('API_URL_STANDINGS')

headers = {
    "X-RapidAPI-Key": APIKEY,
    "X-RapidAPI-Host": APIHOST}


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

@bot.command(name =  "fixtures")
async def _command(ctx):
    await ctx.send(emoji.emojize('Which league?\
        \n1. World Cup :earth_americas:\
        \n2. Champions League :crown:\
        \n3. Europa League :trophy:\
        \n4. Europa Conference League :soccer:\
        \n5. Premier League :England:\
        \n6. La Liga :Spain:\
        \n7. Seria A :Italy:\
        \n8. Bundesliga :Germany:\
        \n9. Ligue 1 :France:', language = 'alias'))

    @bot.event
    async def on_message(message):
        if message.content.startswith('1'): #World Cup
            channel = message.channel #sets variable to same channel user message was sent
            querystring = {"league":"1", "season":"2022", "date":"2022-11-20"}
            response_test = requests.request("GET", fixture_url, headers = headers, params = querystring )
            jsonResponse = response_test.json()
            #most possible World Cup games in a day is 4
            i = -1
            while i < 4:
                i += 1 
                embed = discord.Embed(
                                        title = "World Cup Fixtures",
                                        color = 0xFF9900,
                                        description = " "
                                    )
                embed.set_thumbnail(url = "https://github.com/hagop1/FUT-Daily-Bot/blob/Miher_Progress/logos/worldcuplogo.jpeg")
                embed.add_field(name = jsonResponse["response"][i]["teams"]["home"]["name"] + ' :regional_indicator_v::regional_indicator_s: ' + jsonResponse["response"][i]["teams"]["away"]["name"],value = " .", inline = False)
                embed.add_field(name = str(jsonResponse["response"][i]["score"]["fulltime"]["home"])
                    + " - "
                    + str(jsonResponse["response"][i]["score"]["fulltime"]["away"]), value = ".", inline = False)
                await ctx.send(embed = embed)
            

        elif message.content.startswith('2'): #Champions League
            channel = message.channel
            querystring = {"league":"2", "season":"2022", "date":actual_date}
            response_test = requests.request("GET", fixture_url, headers = headers, params = querystring )
            jsonResponse = response_test.json()
            i = -1
            while i < 10:
                i += 1
                embed = discord.Embed(
                                        title = "Champions League Fixtures",
                                        color = 0xFF9900,
                                        description = " "
                                    )
                embed.set_thumbnail(url = "https://github.com/hagop1/FUT-Daily-Bot/blob/in_progress/source/logos/PL.jpg?raw=true%22")
                embed.add_field(name = jsonResponse["response"][i]["teams"]["home"]["name"] + ' :regional_indicator_v::regional_indicator_s: ' + jsonResponse["response"][i]["teams"]["away"]["name"],value = " .", inline = False)
                embed.add_field(name = str(jsonResponse["response"][i]["score"]["fulltime"]["home"])
                    + " - "
                    + str(jsonResponse["response"][i]["score"]["fulltime"]["away"]), value = ".", inline = False)
                await ctx.send(embed = embed)
            

        elif message.content.startswith('3'): #Europa League
            channel = message.channel
            querystring = {"league":"3", "season":"2022", "date":actual_date}
            response_test = requests.request("GET", fixture_url, headers = headers, params = querystring )
            jsonResponse = response_test.json()
            i = -1
            while i < 10:
                i += 1
                embed = discord.Embed(
                                        title = "Europa League Fixtures",
                                        color = 0xFF9900,
                                        description = " "
                                    )
                embed.set_thumbnail(url = "https://github.com/hagop1/FUT-Daily-Bot/blob/in_progress/source/logos/PL.jpg?raw=true%22")
                embed.add_field(name = jsonResponse["response"][i]["teams"]["home"]["name"] + ' :regional_indicator_v::regional_indicator_s: ' + jsonResponse["response"][i]["teams"]["away"]["name"],value = " .", inline = False)
                embed.add_field(name = str(jsonResponse["response"][i]["score"]["fulltime"]["home"])
                    + " - "
                    + str(jsonResponse["response"][i]["score"]["fulltime"]["away"]), value = ".", inline = False)
                await ctx.send(embed = embed)

        elif message.content.startswith('4'): #Europa Conference League
            channel = message.channel
            querystring = {"league":"848", "season":"2022", "date":actual_date}
            response_test = requests.request("GET", fixture_url, headers = headers, params = querystring )
            jsonResponse = response_test.json()
            i = -1
            while i < 10:
                i += 1
                embed = discord.Embed(
                                        title = "Europa Conference League Fixtures",
                                        color = 0xFF9900,
                                        description = " "
                                    )
                embed.set_thumbnail(url = "https://github.com/hagop1/FUT-Daily-Bot/blob/in_progress/source/logos/PL.jpg?raw=true%22")
                embed.add_field(name = jsonResponse["response"][i]["teams"]["home"]["name"] + ' :regional_indicator_v::regional_indicator_s: ' + jsonResponse["response"][i]["teams"]["away"]["name"],value = " .", inline = False)
                embed.add_field(name = str(jsonResponse["response"][i]["score"]["fulltime"]["home"])
                    + " - "
                    + str(jsonResponse["response"][i]["score"]["fulltime"]["away"]), value = ".", inline = False)
                await ctx.send(embed = embed)

        elif message.content.startswith('5'): #Premier League
            channel = message.channel
            querystring = {"league":"39", "season":"2022", "date":actual_date}
            response_test = requests.request("GET", fixture_url, headers = headers, params = querystring )
            jsonResponse = response_test.json()
            i = -1
            while i < 10:
                i += 1
                embed = discord.Embed(
                                        title = "Premier League Fixtures",
                                        color = 0xFF9900,
                                        description = " "
                                    )
                embed.set_thumbnail(url = "https://github.com/hagop1/FUT-Daily-Bot/blob/in_progress/source/logos/PL.jpg?raw=true%22")
                embed.add_field(name = jsonResponse["response"][i]["teams"]["home"]["name"] + ' :regional_indicator_v::regional_indicator_s: ' + jsonResponse["response"][i]["teams"]["away"]["name"],value = " .", inline = False)
                embed.add_field(name = str(jsonResponse["response"][i]["score"]["fulltime"]["home"])
                    + " - "
                    + str(jsonResponse["response"][i]["score"]["fulltime"]["away"]), value = ".", inline = False)
                await ctx.send(embed = embed)
             

        elif message.content.startswith('6'): #La Liga
            channel = message.channel
            querystring = {"league":"140", "season":"2022", "date":actual_date}
            response_test = requests.request("GET", fixture_url, headers = headers, params = querystring )
            jsonResponse = response_test.json()
            i = -1
            while i < 10:
                i += 1
                embed = discord.Embed(
                                        title = "La Liga Fixtures",
                                        color = 0xFF9900,
                                        description = " "
                                    )
                embed.set_thumbnail(url = "https://github.com/hagop1/FUT-Daily-Bot/blob/in_progress/source/logos/PL.jpg?raw=true%22")
                embed.add_field(name = jsonResponse["response"][i]["teams"]["home"]["name"] + ' :regional_indicator_v::regional_indicator_s: ' + jsonResponse["response"][i]["teams"]["away"]["name"],value = " .", inline = False)
                embed.add_field(name = str(jsonResponse["response"][i]["score"]["fulltime"]["home"])
                    + " - "
                    + str(jsonResponse["response"][i]["score"]["fulltime"]["away"]), value = ".", inline = False)
                await ctx.send(embed = embed)

        elif message.content.startswith('7'): #Seria A
            channel = message.channel
            querystring = {"league":"135", "season":"2022", "date":actual_date}
            response_test = requests.request("GET", fixture_url, headers = headers, params = querystring )
            jsonResponse = response_test.json()
            i = -1
            while i < 10:
                i += 1
                embed = discord.Embed(
                                        title = "Serie A Fixtures",
                                        color = 0xFF9900,
                                        description = " "
                                    )
                embed.set_thumbnail(url = "https://github.com/hagop1/FUT-Daily-Bot/blob/in_progress/source/logos/PL.jpg?raw=true%22")
                embed.add_field(name = jsonResponse["response"][i]["teams"]["home"]["name"] + ' :regional_indicator_v::regional_indicator_s: ' + jsonResponse["response"][i]["teams"]["away"]["name"],value = " .", inline = False)
                embed.add_field(name = str(jsonResponse["response"][i]["score"]["fulltime"]["home"])
                    + " - "
                    + str(jsonResponse["response"][i]["score"]["fulltime"]["away"]), value = ".", inline = False)
                await ctx.send(embed = embed)

        elif message.content.startswith('8'): #Bundesliga
            channel = message.channel
            querystring = {"league":"78", "season":"2022", "date":actual_date}
            response_test = requests.request("GET", fixture_url, headers = headers, params = querystring )
            jsonResponse = response_test.json()
            i = -1
            while i < 10:
                i += 1
                embed = discord.Embed(
                                        title = "Bundesliga Fixtures",
                                        color = 0xFF9900,
                                        description = " "
                                    )
                embed.set_thumbnail(url = "https://github.com/hagop1/FUT-Daily-Bot/blob/in_progress/source/logos/PL.jpg?raw=true%22")
                embed.add_field(name = jsonResponse["response"][i]["teams"]["home"]["name"] + ' :regional_indicator_v::regional_indicator_s: ' + jsonResponse["response"][i]["teams"]["away"]["name"],value = " .", inline = False)
                embed.add_field(name = str(jsonResponse["response"][i]["score"]["fulltime"]["home"])
                    + " - "
                    + str(jsonResponse["response"][i]["score"]["fulltime"]["away"]), value = ".", inline = False)
                await ctx.send(embed = embed)

        elif message.content.startswith('9'): #Ligue 1
            channel = message.channel
            querystring = {"league":"61", "season":"2022", "date":actual_date}
            response_test = requests.request("GET", fixture_url, headers = headers, params = querystring )
            jsonResponse = response_test.json()
            i = -1
            while i < 10:
                i += 1
                embed = discord.Embed(
                                        title = "Ligue 1 Uber Eats Fixtures",
                                        color = 0xFF9900,
                                        description = " "
                                    )
                embed.set_thumbnail(url = "https://github.com/hagop1/FUT-Daily-Bot/blob/in_progress/source/logos/PL.jpg?raw=true%22")
                embed.add_field(name = jsonResponse["response"][i]["teams"]["home"]["name"] + ' :regional_indicator_v::regional_indicator_s: ' + jsonResponse["response"][i]["teams"]["away"]["name"],value = " .", inline = False)
                embed.add_field(name = str(jsonResponse["response"][i]["score"]["fulltime"]["home"])
                    + " - "
                    + str(jsonResponse["response"][i]["score"]["fulltime"]["away"]), value = ".", inline = False)
                await ctx.send(embed = embed)

        await bot.process_commands(message)

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
            ##############################################################################################
            # querystring = {"season" : "2022", "team" : "1"}
            # response_test = requests.request("GET", standings_url, headers = headers, params = querystring )
            # jsonResponse = response_test.json()

            # # embedVar = discord.Embed(title = "Premier league", description = jsonResponse, color = 0xFF9900)
            # # await message.channel.send(embed=embedVar)
            # await message.channel.send(jsonResponse["response"][0]["league"]["name"])
            # # await message.channel.send(jsonResponse["response"][0]["league"]["season"])
            # await message.channel.send(jsonResponse["response"][0]["league"]["country"])
            # await ctx.send(jsonResponse["response"][0]["league"]["logo"])
            ##############################################################################################

        elif message.content.startswith('2'):
            channel = message.channel
            ##############################################################################################
            # querystring = {"id": "39"}
            # response_test = requests.request("GET", leagues_url, headers=headers, params=querystring)
            # jsonResponse = response_test.json()

            # await message.channel.send(jsonResponse["response"][0]["league"]["name"])
            # await message.channel.send(jsonResponse["response"][0]["country"]["name"])
            # await ctx.send(jsonResponse["response"][0]["league"]["logo"])
            ##############################################################################################


        elif message.content.startswith('3'):
            channel = message.channel
            ##############################################################################################
            # querystring = {"season": "2022", "league": "39"}
            # response_test = requests.request("GET", standings_url, headers = headers, params = querystring)
            # jsonResponse = response_test.json()

            # await message.channel.send(jsonResponse["response"][0]["league"]["standings"][0][0]["rank"])
            # await message.channel.send(jsonResponse["response"][0]["league"]["standings"][0][0]["team"]["name"])
            # await message.channel.send(jsonResponse["response"][0]["league"]["standings"][0][0]["all"])
            # await ctx.send(jsonResponse["response"][0]["league"]["standings"][0][0]["team"]["logo"])
            ##############################################################################################

            # await message.channel.send(jsonResponse["response"][0]["league"]["standings"][0][1])
            # await message.channel.send(jsonResponse["response"][0]["league"]["standings"][0][2])

            # await message.channel.send(jsonResponse["response"][0]["league"]["name"])
            # await message.channel.send(jsonResponse["response"][14])
            # await message.channel.send(jsonResponse["response"][0]["seasons"][12]["coverage"]["fixtures"]["events"])


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