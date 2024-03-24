import discord
from discord.ext import commands
import os
from options import TOKEN
from random import choice

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents, help_command=None)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def wassup(ctx):
    await ctx.send('Салам дорогой друг! Этот бот для Discord говорит способы борьбы с ГП. Этот бот бета версия, так чтоооо если ты увидешь что бот лагает, знай, у этого автора руки ростут из... Ну ты понял откуда ростут руки :)')

@bot.command()
async def otvety_mail_ru(ctx):
    seq = ['Рациональное использование энергоресурсов и сокращение выбросов в атмосферу парниковых газов.', 
           'Переход от традиционных методов выработки энергии, связанных с сжиганием углеродного сырья, к нетрадиционной (альтернативной) энергетике: использованию солнечных батарей, ветряных, приливных, геотермальных электростанций и др.',
           'Снижение выбросов парниковых газов.',
           'Переход от автомобилей с бензиновым или дизельными двигателями, на электроавтомобили.']
    rand = choice(seq)
    await ctx.send(rand)

bot.run(TOKEN)