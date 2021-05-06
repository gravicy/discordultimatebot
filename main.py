import random
import discord

class MyClient(discord.Client):
    #Login method
    async def on_ready(self):
        print("Server started..")

    #Triggers when a message is send (all kinds of messages)
    async def on_message(self, message):
        if message.author == client.user:
            return

        if message.content.startswith("$msg"):
            await message.channel.send("Command call by: " + str(message.author))
            await message.author.send("You used the command $msg")
client = MyClient()
client.run("ODM5NjA0NDA3NDkwNzA3NDc2.YJMEiQ.arS0qfaKPEw3CyXeCzEtM56mJMw")