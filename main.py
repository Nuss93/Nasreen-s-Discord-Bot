# imports discord.py library
import discord
# gets the TOKEN from .env file
import os
import requests
import json
import random
from replit import db

# instcance of client which is a connection to Discord
client = discord.Client()
sad_words = ["sad", "depressed", "unhappy", "angry", "miserable"]
starter_encouragements = [
    "If you're already sad, why go on with life anyways?",
    "Hang in there, the ceiling fan isn't too high", "Time to DIE",
    "It is time to end your life"
]

if "responding" not in db.keys():
    db["responding"] = True


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)


def update_encouragements(encouraging_message):
    if "encouragements" in db.keys():
        encouragements = db["encouragements"].value
        encouragements.append(encouraging_message)
        db["encouragements"] = encouragements
    else:
        db["encouragements"] = [encouraging_message]


def delete_encouragment(index):
    encouragements = db["encouragements"].value
    if len(encouragements) > index:
        del encouragements[index]
    db["encouragements"] = encouragements


# @client.event() decorator is used to register an event
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith('$lyrics'):
        quote = get_quote()
        await message.channel.send(quote)

    if db["responding"]:
        options = starter_encouragements
        if "encouragements" in db.keys():
            options = options + db["encouragements"].value

    if any(word in msg for word in sad_words):
        print(options)
        await message.channel.send(random.choice(options))

    if msg.startswith("$new"):
        encouraging_message = msg.split("$new ", 1)[1]
        # print(encouraging_message, type(encouraging_message))
        update_encouragements(encouraging_message)
        await message.channel.send("New encouraging message added.")

    if msg.startswith("$del"):
        encouragements = []
        if "encouragements" in db.keys():
            index = int(msg.split("$del", 1)[1])
            delete_encouragment(index)
            encouragements = db["encouragements"].value
        await message.channel.send(encouragements)

    if msg.startswith("$list"):
        encouragements = []
        if "encouragements" in db.keys():
            encouragements = db["encouragements"]
        await message.channel.send(encouragements)

    if msg.startswith("$responding"):
        value = msg.split("$responding ", 1)[1]
        print(value)

        if value.lower() == "true":
            db["responding"] = True
            await message.channel.send("Responding is on.")
        else:
            db["responding"] = False
            await message.channel.send("Responding is off.")


# my_secret = os.environ['TOKEN']
client.run(os.getenv('TOKEN'))
