import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('Bot is ready')

@client.command()
async def ping(ctx):
    await ctx.send('Pong!')

@client.command()
async def kick(ctx, member : discord.Member, *reason):
    await ctx.send('{} was kicked by ``{}`` for the reason: ``{}``'.format(member, ctx.author, ' '.join(reason)))
    await member.kick()

@client.command()
async def brb(ctx, time):
    await ctx.send(f'{ctx.author} sier han er brb i {time} minutter. {ctx.created_at}')


client.run('TOKEN')