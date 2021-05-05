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

        if message.content == "$help":
            await message.channel.send("Für Schere, Stein, Papier spielen: $rps [EINGABE] eingeben, \n"
                                       " wobei unter EINGABE:  r = rock, p = paper & s = scissors")

        if message.content.startswith("$rps"):
            playerChoice = message.content.split(' ')[1]
            await message.channel.send("Players choice: " + playerChoice)

            computerChoice = ["Rock", "Paper", "Scissors"]

            result = random.randint(0, 2)

            if playerChoice == "r" or "p" or "s":

                #Rock
                if playerChoice == "r" and result == 0:
                    await message.channel.send("Computer had: " + computerChoice[0])
                    await message.channel.send("Draw...")
                elif playerChoice == "r" and result == 1:
                    await message.channel.send("Computer had: " + computerChoice[1])
                    await message.channel.send("You've lost!")
                elif playerChoice == "r" and result == 2:
                    await message.channel.send("Computer had: " + computerChoice[2])
                    await message.channel.send("You've won!")

                #Paper
                if playerChoice == "p" and result == 0:
                    await message.channel.send("Computer had: " + computerChoice[0])
                    await message.channel.send("You've won!")
                elif playerChoice == "p" and result == 1:
                    await message.channel.send("Computer had: " + computerChoice[1])
                    await message.channel.send("Draw...")
                elif playerChoice == "p" and result == 2:
                    await message.channel.send("Computer had: " + computerChoice[2])
                    await message.channel.send("You've lost!")

                #Scissors
                if playerChoice == "s" and result == 0:
                    await message.channel.send("Computer had: " + computerChoice[0])
                    await message.channel.send("You've lost!")
                elif playerChoice == "s" and result == 1:
                    await message.channel.send("Computer had: " + computerChoice[1])
                    await message.channel.send("You've won!")
                elif playerChoice == "s" and result == 2:
                    await message.channel.send("Computer had: " + computerChoice[2])
                    await message.channel.send("Draw...")

            else:
                await message.channel.send("Ungültige Eingabe..")
                return


client = MyClient()
client.run("ODM5NjA0NDA3NDkwNzA3NDc2.YJMEiQ.zApp961J7u-0kyoFKfc684cAy7k")