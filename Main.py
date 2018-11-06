import discord
from discord.ext import commands
import datetime

token = ''

client = commands.Bot(command_prefix='-')

client.remove_command('help')

@client.event
async def on_ready():
    print('Bot online!')
    await client.change_presence(game=discord.Game(name='-help to get started'))

@client.command(pass_context = True)
async def help(ctx):
    channel = ctx.message.channel
    embed = discord.Embed(
        colour = discord.Colour.blue()
    )

    embed.set_thumbnail(url=client.user.avatar_url)
    #embed.set_author(name='TOS 2018 BOT')
    embed.add_field(name=':heart_eyes: **TOS 2018 BOT**', value='Author `26416085` & `26416088`', inline=False)

    embed.add_field(name='**COMMANDS**', value="Use `-` before any commands. Ex. `-join`", inline=False)
    embed.add_field(name='**MUSIC**', value='`join` `play` `pause` `skip` `stop` `queue`', inline=False)
    embed.add_field(name='**HANGMAN**', value='Field Value', inline=False)
    embed.add_field(name='**MANAGE SERVER**', value='Field Value', inline=False)

    embed.set_image(url='http://www.bobbiefox.com/wp-content/uploads/2016/10/Images_ThankYou_Script.png')

    embed.set_footer(text=datetime.date.today())

    #await client.say(embed=embed)
    await client.send_message(channel, embed = embed)

client.run(token)