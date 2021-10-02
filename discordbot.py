import discord
import asyncio

client = discord.Client()

token = "ODkzODM0OTY5NzQ5Nzk4OTIy.YVhOrw.JtrghpODP0pbdjoYgRBcg3BMUgo"

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

client.run(token)