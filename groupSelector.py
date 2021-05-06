import os
import discord
import random
from dotenv import load_dotenv

load_dotenv()

try:
    with open("users.txt", "r") as users_file:
        users = users_file.readlines()
except FileNotFoundError:
    users = []
f = open("users.txt", "a")


def add_user(user):
    if str(user) in users:
        print(str(user) + " tried to enter more than ones...")
    else:
        print("added " + str(user))
        f.writelines(str(user) + "\n")
        users.append(str(user))
        f.flush()


def is_himself(parnterA, partnerB):
    for i, u in enumerate(parnterA):
        if u == partnerB[i]:
            return True
    return False


class MyClient(discord.Client):
    # Login
    async def on_ready(self):
        print("Server started..")


    #Triggers when a message is sent (all kinds of messages)

    async def on_message(self, message):
        if message.author == client.user:
            return

        if message.content.startswith("grp"):
            msg = "Gruppen-Pool beitreten? Falls ja, antworte mit JA"
            await message.author.send(msg)

        if message.content.lower() == "ja" and str(message.channel.type) == "private":
            add_user(message.author)
            await message.author.send("Beigetreten")

        if message.content.startswith("shuffle"):
            partnerA = users[:]
            partnerB = users[:]

            while is_himself(partnerA, partnerB):
                print("Shuffling...")
                random.shuffle(partnerA)
                random.shuffle(partnerB)

            # u ist zb BISafa74#9048
            for i, u in enumerate(partnerA):
                user = discord.utils.get(message.guild.members, name=u.split("#")[0],
                                         discriminator=u.split("#"[1].replace("\n", "")))
                target = discord.utils.get(message.guild.members, name=partnerB[i].split("#")[0],
                                           discriminator=partnerB[i].split("#"[1].replace("\n", "")))
                await user.send("Partner: " + target.mention)
            await message.channel.send("Gruppen zugeteilt.")


client = MyClient()

client.run(os.getenv("DISCORD_TOKEN"))
