import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$blig'):
        await message.channel.send('Hello!')

client.run('MTAyMjI2MzMzNjQ3MTEwOTc5Mg.Gu1CbV.eGAVD6ydQLXW1OvYlFEuxtEDsjan5X2lpPNoMw')
