import discord
import asyncio
import os

client = discord.Client()

token = "ODkzODM0OTY5NzQ5Nzk4OTIy.YVhOrw.FFNmOzyHJclVZk08pu16-jGO4hA"

@client.event
async def on_ready():

    print(client.user.name)
    print('성공적으로 김윤상이 실행되었습니다 (˵⚈ε⚈˵)')
    game = discord.game('병신!')
    await client.change_presence(status=discord.status.online, activity=game)

@client.event
async def on_message(message):
   if message.content == "김윤상":
    await message.channel.send('병신!!!')

access_token =  os.environ['BOT_TOKEN']
client.run(access_token)
