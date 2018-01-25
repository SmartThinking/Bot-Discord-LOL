import discord
import asyncio
import pickle
import os
import random
from time import sleep
from discord.ext import commands

client = discord.Client()

description = '''soriegedon'''

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
        await client.send_message(message.channel, 'PatchNotes, Info, Jhin, Yoda, Numero, GitHub ')
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
    elif message.content.startswith("!GitHub"):
        await client.send_message(message.channel, 'https://github.com/SmartThinking/Bot-Discord-LOL')
    elif message.content.startswith("!Ajuda"):
        await client.send_message(message.channel, '''Digite !Commandos para ver a lista de commandos, caso
tenha alguma pergunta, mande uma mensagem para InvisibleMan ou JosueElMotoboy''')

@client.event
async def on_member_join(member):
    channel = member.server.get_channel("391381717954330633")
    msg = 'Bem vindo {}, digite !Ajuda para começar.'.format(member.name)
    await client.send_message(channel, msg)
    
client.run("NDA1ODMyMDU5Nzk0NDg5MzU1.DUqIIw.wbUhD7FOrM4ohuJVEkFMZS2nmV8")
