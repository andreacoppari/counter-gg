import discord
import requests
import json
import os

from get_champions import get_champ_list as champ_list

client = discord.Client()

champions = champ_list()

def get_enemy_tips(champ: str):
    res = ""
    with open("champions_data.json", "r", encoding="utf8") as ch:
        data = json.load(ch)
        if not data[champ]:
            return "You spelled the champion wrong or this champ doesn't exist"
        tips = data[champ]["enemy_tips"]
        if len(tips) == 0:
            return " - Sorry! no tips available yet!\n"
        for tip in tips:
            res += f" - {tip}\n"
        return res

def get_ally_tips(champ: str):
    res = ""
    with open("champions_data.json", "r", encoding="utf8") as ch:
        data = json.load(ch)
        if not data[champ]:
            return "You spelled the champion wrong or this champ doesn't exist"
        tips = data[champ]["ally_tips"]
        if len(tips) == 0:
            return " - Sorry! no tips available yet!"
        for tip in tips:
            res += f" - {tip}\n"
        return res

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

    if message.startswith("!!help") or message.startswith("!!h"):
        await msg.channel.send(
            '''Here's the list of available commands:\n
    !!help (or !!h) to display this message\n
    !!counter <champ> (or !!c <champ>) for tips on how to counter a champ\n
    !!tips <champ> (or !!t <champ>) for tips on how to play your champ\n
    !!lost (or !!depressed) to get a random motivational quote
        ''')

    if message.startswith("!!counter") or message.startswith("!!c"):
        champ = message.split()[1].lower().capitalize()
        if champ in champions:
            await msg.channel.send(f"Here's a list of tips to defeat {champ}:\n{get_enemy_tips(champ)}Good luck!")
        else:
            await msg.channel.send("Type !!counter <champ> or !!c <champ> to get tips on how to defeat a champ")

    if message.startswith("!!tips") or message.startswith("!!t"):
        champ = message.split()[1].lower().capitalize()
        if champ in champions:
            await msg.channel.send(f"Here's a list of tips for {champ}:\n{get_ally_tips(champ)}Good luck!")
        else:
            await msg.channel.send("Type !!tips <champ> or !!t <champ> to get tips on how to play a champ")

    if message.startswith("!!lost") or message.startswith("!!depressed"):
        await msg.channel.send(get_quote())

token = os.environ.get("TOKEN")
client.run(token)