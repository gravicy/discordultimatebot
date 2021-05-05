from random import random

import discord

class MyClient(discord.Client):
    #Login method
    async def on_ready(self):
        print("Im logged in...")

    #Triggers when a message is send (all kinds of messages)
    async def on_message(self, message):
        if message.author == client.user:
            return

        if message.content == "$help":
            await message.channel.send("Für Schere Stein Papier spielen: $rps eingeben, \n"
                                       " wobei r = rock, p = paper & s = scissors")

        if message.content.startswith("$rps"):
            playerChoice = message.content.split(' ') [1]
            choiceParam = 0
            if playerChoice.lower() == "rock":
                choiceParam = 1
            if playerChoice.lower() == "paper":
                choiceParam = 2
            if playerChoice.lower == "scissors":
                choiceParam = 3
            else:
                await message.channel.send("Ungültige Eingabe..")
                return
            result = random.randint(0, 2)
            #Rock
            if playerChoice == "rock" and result == 0:
                await message.channel.send("Draw...")
            elif playerChoice == "rock" and result == 1:
                await message.channel.send("You've lost!")
            elif playerChoice == "rock" and result == 2:
                await message.channel.send("You've won!")

            #Paper
            if playerChoice == "paper" and result == 0:
                await message.channel.send("You've won!")
            elif playerChoice == "paper" and result == 1:
                await message.channel.send("Draw...")
            elif playerChoice == "paper" and result == 2:
                await message.channel.send("You've lost!")

            #Scissors
            if playerChoice == "scissors" and result == 0:
                await message.channel.send("You've lost!")
            elif playerChoice == "scissors" and result == 1:
                await message.channel.send("You've won!")
            elif playerChoice == "scissors" and result == 2:
                await message.channel.send("Draw...")


client = MyClient()
client.run("ODM5NjA0NDA3NDkwNzA3NDc2.YJMEiQ.zApp961J7u-0kyoFKfc684cAy7k")