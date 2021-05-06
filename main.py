import os
import discord
import random
from dotenv import load_dotenv

load_dotenv()


class MyClient(discord.Client):
    # Login method
    async def on_ready(self):
        print("Server started..")

    # Triggers when a message is send (all kinds of messages)
    async def on_message(self, message):
        if message.author == client.user:
            return

        if message.content.startswith("$msg"):
            await message.channel.send("Command call by: " + str(message.author))
            await message.author.send("You used the command $msg")


client = MyClient()
client.run(os.getenv("DISCORD_TOKEN"))
