import discord
import asyncio
import pickle
import os
import random
from time import sleep

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith("!PatchNotes"):
        await client.send_message(message.channel, 'https://br.leagueoflegends.com/pt/news/game-updates/patch/notas-da-atualizacao-82')
    elif message.content.startswith("!Commandos"):
        await client.send_message(message.channel, 'PatchNotes, Info, Jhin, Yoda, Numero, Parar, 5minParar, GitHub ')
    elif message.content.startswith("!Info"):
        await client.send_message(message.channel, 'Bot feito por InvisibleMan#3939, python 3.6.4')
    elif message.content.startswith("!Jhin"):
        jhin = 0
        while jhin != 4:
            jhin += 1
            sleep (1)
            await client.send_message(message.channel, '{}'.format(jhin))
    elif message.content.startswith("!Yoda"):
        await client.send_message(message.channel, 'https://www.twitch.tv/yoda')
    elif message.content.startswith("!Numero"):
            x = random.randint(1, 10000000)
            await client.send_message(message.channel, '{}'.format(x))
    elif message.content.startswith("!Parar"):
        await client.send_message(message.channel, '''Parando por 30 segundos, aguarde e
não digite nenhum commando''')
        sleep(30)
        await client.send_message(message.channel, 'Voltando...')
        sleep(3)
    elif message.content.startswith("!5minParar"):
        await client.send_message(message.channel, 'Parando por 5 minutos, aguarde')
        sleep(300)
        await client.send_message(message.channel, 'Voltando...')
    elif message.content.startswith("!GitHub"):
        await client.send_message(message.channel, '')
    

    
client.run("NDA1ODMyMDU5Nzk0NDg5MzU1.DUqIIw.wbUhD7FOrM4ohuJVEkFMZS2nmV8")
