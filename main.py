from keep_alive import keep_alive

# imports discord.py library
import discord
from discord.utils import find
# gets the TOKEN from .env file
import os
import random
from replit import db

# instcance of client which is a connection to Discord
client = discord.Client()

lyrics = [
    "You say the ocean's rising like I give a shit, \nYou say the whole world's ending, honey, it already did. \nYou're not gonna slow it, Heaven knows you tried. \n\nGot it? Good, now get inside.",
    "Healing the world with comedy, the indescribable power of your comedy~"
    "The world is so fucked up. \n\nSystematic oppression, income inequality, the other stuff.",
    "If you wake up in a house that's full of smoke. \nDon't panic, call me and I'll tell you a joke.",
    "Oh, shit... \n\nShould I be joking at a time like this?",
    "If you start to smell burning toast, you're having a stroke or overcooking your toast.",
    "I've been where I always am when you're not wearing me on your hand: in a frightening, liminal space between states of being! Not quite dead, not quite alive! It's similar to a constant state of sleep paralysis.",
    "Who needs a coffee? 'Cause I'm doing a run. I'm writing down the orders now for everyone. The coffee is free, just like me I'm an unpaid intern",
    "Wa-da-da-wap-wa-da",
    "CEO, entrepreneur. \nBorn in 1964. \nJeffrey, Jeffrey Bezos~",
    "Come on, Jeffrey, you can do it. \nPave the way, put your back into it.",
    "Zuckerberg and Gates and Buffett. \nAmateurs can fuckin' suck it. \nFuck their wives, drink their blood. \n\nCome on, Jeff, get 'em",
    "One hand on my dick and one hand on my phone, yeah.",
    "Another night on my own, yeah. \nStuck in my home, yeah. Sitting alone.",
    "Well, well, look who's inside again. \nWent out to look for a reason to hide again.",
    "Well, well. Buddy, you found it. \nNow, come out with your hands up we've got you surrounded",
    "My stupid friends are having stupid children.",
    "My stupid friends are having stupid children. \nStupid, fucking ugly, boring children",
    "It's 2020, and I'm 30, I'll do another ten. \n2030, I'll be 40 and kill myself then.",
    "How are you feeling? Do you like the show? Are you tired of it? \nNever mind, I don’t wanna know.",
    "Is there anyone out there? \nOr am I all alone?",
    "I’d give away the ending \nBut you don’t wanna kn-",
    "How we feelin' out there tonight? \nHahaha, yeah... \n\nI am not feeling good~",
    "Are you feeling what I'm feeling? \nI haven't had a shower in the last nine days.",
    "Staring at the ceiling and waiting for this feeling to go away. \nBut it won't go away.",
    "Well, I feel like shit (Oh, shit) \nFeeling like a saggy, massive sack of shit (Oh, shit) \nBig ol' motherfucking duffel bag of shit (Oh, shit)",
    "All day, all shit~",
    "So, um... Uh, my current mental health is is rapidly approaching, um... an ATL ... which is, um... That's an all-time low. Not... Not Atlanta. And, you know, I feel okay when I'm asleep. Like, when I'm asleep I feel alright.",
    "A few things start to happen, \nmy vision starts to flatten. \nMy heart, it gets to tappin' \n\nAnd I think I'm gonna die!",
    "Yeah, so, um, yeah. \nNot, not doing great.",
    "Welcome to the internet! Have a look around. \nAnything that brain of yours can think of can be found.",
    "Be happy! Be horny! Be bursting with rage! We've got a million different ways to engage.",
    "'Cause a random guy just kindly sent you photos of his cock. \nThey are grainy and off-putting; he just sent you more. \nDon't act surprised—you know you like it, you whore.",
    "Could I interest you in everything all of the time? \nA little bit of everything all of the time.",
    "Apathy's a tragedy, and boredom is a crime. \nAnything and everything all of the time~",
    "We set our sights and spent our nights waiting for you! \nYou, insatiable you",
    "Jeffrey Bezos \n\nCongratulations!",
    "Does anybody want to joke when no one's laughing in the background?",
    "So this is how it ends I promise to never go outside again.",
    "I'm slowly losing power has it only been an hour? \n\nNo, that can't be right.",
    "I wanna hear you tell a joke when no one's laughing in the background",
    "Am I going crazy? \nWould I еven know? \nAm I right back where I startеd fourteen years ago?",
    "Wanna guess the ending? If it ever does...",
    "I swear to God that all I've ever wanted was a little bit of everything all of the time a bit of everything all of the time.",
    "Apathy's a tragedy, and boredom is a crime. I'm finished playin', and I'm stayin' inside.",
    "If I wake up in a house that's full of smoke \nI'll panic, so call me up and tell me a joke.",
    "Oh, shit \n\nYou're really joking at a time like this?"
]

if "responding" not in db.keys():
    db["responding"] = True


@client.event
async def on_guild_join(guild):
    general = find(lambda x: x.name == 'general', guild.text_channels)

    embedJoin = discord.Embed(
        title="OwO~! What's this? I have landed in a random server UwU",
        description=
        "I was created by my mother, Nuss93 to annoy people she knows by sending random Bo Burnham lyrics at random times. The more active you are in a server, the higher the probability of you getting a free lyric from me! \nOh boiii, isn't that fun?",
        color=0x4f98d5,
        url="https://www.youtube.com/watch?v=-VAvUgzey3I")
    embedJoin.add_field(
      name="How to use me?",
      value="It's okay, you can use me as you please, no need to feel guilty about it :) \n\n`$lyrics` : Get random lyrics instantly \n\n`$youthere` : Checks if I am still alive... Thanks for checking up on me. Sometimes, I feel like being all alone makes me questions why am I still alive. And then I go into a depressive spiral thinking about ways I can out myself and end this miserable life. \n\n`$how` : I get it, we are forgetful human beings, you might need some help with my commands."
    )
    embedJoin.set_footer(text="Anyways! Enjoy the amazing lyrics I will be sharing :D Hope you enjoy!")
    if general and general.permissions_for(guild.me).send_messages:
        await general.send(embed=embedJoin)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content
    # random_send = random.choice(
    #     [True])
    random_send = random.choice(
        [False, True, False, True, False, False, False, False, False, False, False, False, False, False])

    if db["responding"]:
        options = lyrics
        if "encouragements" in db.keys():
            options = options + db["encouragements"].value

    if msg.startswith('$lyrics'):
        await message.channel.send(random.choice(options))

    if msg.startswith('$youthere'):
        await message.channel.send(
            "Hi, yes! I am still alive and well thank you very much ;)")
        await message.channel.send("I've been where I always am when I'm not sending messages to this server : in a frightening, liminal space between states of being! Not quite dead, not quite alive! It's similar to a constant state of sleep paralysis.")
        await message.channel.send("But anyways, thanks for checking up on me. Sometimes, I feel like being all alone makes me questions why am I still alive. And then I go into a depressive spiral thinking about ways I can out myself and end this miserable life.")
        await message.channel.send("Beep boop, have a nice day~")
    
    if msg.startswith('$how'):
        await message.channel.send(
            "OwO~! Someone asked HOW to use me?")
        await message.channel.send("`$lyrics` : Get random lyrics instantly \n\n`$youthere` : Checks if I am still alive... Thanks for checking up on me. Sometimes, I feel like being all alone makes me questions why am I still alive. And then I go into a depressive spiral thinking about ways I can out myself and end this miserable life. \n\n`$how` : Prompts this exact same message if you need to be reminded of how to summon me. I know you are obsessed with me, but let's keep it on the DL okay ;)")
        await message.channel.send("Beep boop, have a nice day~")

    print(random_send)
    if random_send:
        embedVar = discord.Embed(
            title=
            "Hello there! You have been graced with Bo Burnham's wonderful presence",
            description="Here's a random Bo Burnham lyric from Inside!",
            color=0x4f98d5,
            url="https://www.youtube.com/watch?v=-VAvUgzey3I")
        embedVar.add_field(name=random.choice(options), value="Hope you enjoy~")
        await message.channel.send(embed=embedVar)

    if msg.startswith("$responding"):
        value = msg.split("$responding ", 1)[1]
        print(value)

        if value.lower() == "true":
            db["responding"] = True
            await message.channel.send("Responding is on.")
        else:
            db["responding"] = False
            await message.channel.send("Responding is off.")


keep_alive()
client.run(os.getenv('TOKEN'))
