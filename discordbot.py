import discord
import random

client = discord.Client()

elos = ['Prata', 'Gold', 'Platina', 'Diamante', 'Mestre', 'Challenger']

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
        await client.send_message(message.channel, 'https://br.leagueoflegends.com/pt/news/game-updates/patch/notas-da-atualizacao-83')
    elif message.content.startswith("!Commandos"):
        await client.send_message(message.channel, 'PatchNotes, Info, Yoda, Numero, GitHub, Regras, <ELO>, Importante')
    elif message.content.startswith("!Info"):
        await client.send_message(message.channel, '''Bot feito por InvisibleMan#3939, python 3.6.4. caso tenha conhecimento sobre a linguagem Python e queira ajudar, mande uma mensagem para InvisibleMan#3939''')
    elif message.content.startswith("!Yoda"):
        await client.send_message(message.channel, 'https://www.twitch.tv/yoda')
    elif message.content.startswith("!Numero"):
            author = message.author
            x = random.randint(1, 100)
            await client.send_message(message.channel, '{} gerou o número {}'.format(author, x))
    elif message.content.startswith("!GitHub"):
        await client.send_message(message.channel, 'https://github.com/SmartThinking/Bot-Discord-LOL')
    elif message.content.startswith("!Ajuda"):
        await client.send_message(message.channel, '''Digite !Commandos para ver a lista de commandos, caso
tenha alguma pergunta, mande uma mensagem para InvisibleMan ou JosueElMotoboy''')
    elif message.content.startswith("!Regras"):
        await client.send_message(message.channel, '''1.Não faça spam isso resultara em um mute dependendo do caso
2.Não xinge
3.Não peça para ser administrador
4.Não divulge canais no youtube e coisas do tipo sem permissão
5.Caso veja alguem quebrando regras avise os moderadores
''')
    elif message.content.startswith("!Prata"):
        author = message.author
        await client.send_message(message.channel, '@everyone {} acabou de se subir para o {}'.format(author, elos[0]))
    elif message.content.startswith("!Ouro"):
        author = message.author
        await client.send_message(message.channel, '@everyone {} acabou de se subir para o {}'.format(author, elos[1]))
    elif message.content.startswith("!Platina"):
        author = message.author
        await client.send_message(message.channel, '@everyone {} acabou de se subir para o {}'.format(author, elos[2]))
    elif message.content.startswith("!Diamante"):
        author = message.author
        await client.send_message(message.channel, '@everyone {} acabou de se subir para o {}'.format(author, elos[3]))
    elif message.content.startswith("!Mestre"):
        author = message.author
        await client.send_message(message.channel, '@everyone {} acabou de se subir para o {}'.format(author, elos[4]))
    elif message.content.startswith("!Challenger"):
        author = message.author
        await client.send_message(message.channel, '@everyone {} acabou de se subir para o {}'.format(author, elos[5]))
    elif message.content.startswith("!LevelUp"):
        author = message.author
        await client.send_message(message.channel, '@everyone {} acabou de subir de nivel'.format(author))
    elif message.content.startswith("!!!"):
        await client.send_message(message.channel, 'TeemoBot >>> DabBot')
    elif message.content.startswith("!Importante"):
        await client.send_message(message.channel, '''Rework do campeão Swain: https://www.youtube.com/watch?v=Y_3yqTId1Uo&feature=youtu.be ''')

@client.event
async def on_member_join(member):
    channel = member.server.get_channel("391381717954330633")
    msg = 'Bem vindo {}, digite !Ajuda para começar.'.format(member.name)
    await client.send_message(channel, msg)
    
client.run("SEGREDO")

