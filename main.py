import discord
import requests
import json
import os

client = discord.Client()

champions = ['annie', 'ekko', 'yasuo']

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return quote

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(msg: discord.Message):
    if msg.author == client.user:
        return
    
    message = msg.content

    if message.startswith("!!counter"):
        champ = message.split()[1]
        if champ.lower() in champions:
            await msg.channel.send(f"{get_quote()}\n\nO meglio, impara a giocare -A.C.")
        else:
            await msg.channel.send("Scrivi $counter <campione> per info su come counterare un campione")

token = os.environ.get("TOKEN")
client.run(token)