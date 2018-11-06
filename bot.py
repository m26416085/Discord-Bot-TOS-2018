# import discord
# from discord.ext import commands
# import asyncio
# from itertools import cycle
#
# import youtube_dl
#
# token = 'NTA2ODEyNTk2NjE2NDI5NTgx.DsMdSQ.JuhJ7kxvlNqrpOEL7X0qSVTcDUg'
#
# client = commands.Bot(command_prefix = '.')
# status = ['Message1', 'Message2', 'Message3']
#
# #client.remove_command('help')
#
# players = {}
# queues = {}
#
# extensions = ['fun']
#
# def check_queue(id):
#     if queues[id] != []:
#         player = queues[id].pop(0)
#         players[id] = player
#         player.start()
#
# async def change_status():
#     await client.wait_until_ready()
#     msgstatus = cycle(status)
#
#     while not client.is_closed:
#         current_status = next(msgstatus)
#         await client.change_presence(game=discord.Game(name=current_status))
#         await asyncio.sleep(5)
#
# @client.event
# async def on_ready():
#     print('Bot online!')
#     #await client.change_presence(game=discord.Game(name='.help to get started'))
#
# @client.command()
# async def load(extension):
#     try:
#         client.load_extension(extension)
#         print('Loaded {}'.format(extension))
#     except Exception as error:
#         print('{} cannot be loaded. [{}]'.format(extension, error))
#
# @client.command()
# async def unload(extension):
#     try:
#         client.unload_extension(extension)
#         print('Unloaded {}'.format(extension))
#     except Exception as error:
#         print('{} cannot be unloaded. [{}]'.format(extension, error))
#
#
# @client.command(pass_context=True)
# async def join(ctx):
#     channel = ctx.message.author.voice.voice_channel
#     await client.join_voice_channel(channel)
#
# @client.command(pass_context=True)
# async def leave(ctx):
#     server = ctx.message.server
#     voice_client = client.voice_client_in(server)
#     await voice_client.disconnect()
#
# @client.command(pass_context=True)
# async def play(ctx, url):
#     server = ctx.message.server
#     voice_client = client.voice_client_in(server)
#     player = await voice_client.create_ytdl_player(url, after=lambda: check_queue(server.id))
#     players[server.id] = player
#     player.start()
#
# @client.command(pass_context = True)
# async def pause(ctx):
#     id = ctx.message.server.id
#     players[id].pause()
#
# @client.command(pass_context = True)
# async def stop(ctx):
#     id = ctx.message.server.id
#     players[id].stop()
#
# @client.command(pass_context = True)
# async def resume(ctx):
#     id = ctx.message.server.id
#     players[id].resume()
#
# @client.command(pass_context = True)
# async def queue(ctx, url):
#     server = ctx.message.server
#     voice_client = client.voice_client_in(server)
#     player = await voice_client.create_ytdl_player(url, after=lambda: check_queue(server.id))
#
#     if server.id in queues:
#         queues[server.id].append(player)
#     else:
#         queues[server.id] = [player]
#     await client.say('Video queued~')
#
# @client.event
# async def on_reaction_add(reaction , user):
#     channel = reaction.message.channel
#     await client.send_message(channel, '{} has added {} to the message: {}'.format(user.name, reaction.emoji, reaction.message.content))
#
# @client.event
# async def on_reaction_remove(reaction, user):
#     channel = reaction.message.channel
#     await client.send_message(channel, '{} has removed {} to the message: {}'.format(user.name, reaction.emoji, reaction.message.content))

# @client.command(pass_context = True)
# async def help(ctx):
#     author = ctx.message.author
#     channel = ctx.message.channel
#
#     embed = discord.Embed(
#         colour = discord.Colour.orange()
#     )
#
#     embed.set_author(name='Help')
#     embed.add_field(name='.ping', value='Returns Pong!', inline=False)
#
#     await client.send_message(author, embed = embed)
#     await client.send_message(channel, "I've send you a message :)")

# @client.command(pass_context = True)
# async def displayembed(ctx):
#     channel = ctx.message.channel
#     embed = discord.Embed(
#         title = 'Title',
#         description = 'This is a description',
#         colour = discord.Colour.blue()
#     )
#
#     embed.set_footer(text = 'This is a footer')
#     embed.set_image(url='https://cdn-ap-ec.yottaa.net/55b635db0b5344273c002031/d1fd69005c1501336a81123dfe2baf36.yottaa.net/v~4b.471/8-3-large.jpg?yocs=2u_&yoloc=ap')
#     embed.set_thumbnail(url='https://cdn-ap-ec.yottaa.net/55b635db0b5344273c002031/d1fd69005c1501336a81123dfe2baf36.yottaa.net/v~4b.471/8-3-large.jpg?yocs=2u_&yoloc=ap')
#     embed.set_author(name='Author Name', icon_url='https://cdn-ap-ec.yottaa.net/55b635db0b5344273c002031/d1fd69005c1501336a81123dfe2baf36.yottaa.net/v~4b.471/8-3-large.jpg?yocs=2u_&yoloc=ap')
#
#     embed.add_field(name='Field Name', value='Field Value', inline=False)
#     embed.add_field(name='Field Name', value='Field Value', inline=True)
#     embed.add_field(name='Field Name', value='Field Value', inline=True)
#
#     #await client.say(embed=embed)
#     await client.send_message(channel, embed=embed)

# @client.event
# async def on_member_join(member):
#     role = discord.utils.get(member.server.roles, name = "New Member")
#     await client.add_roles(member, role)
#
# @client.command(pass_context = True)
# async def clear(ctx, amount = 100):
#     channel = ctx.message.channel
#     messages = []
#     async for message in client.logs_from(channel, limit = int(amount) + 1):
#         messages.append(message)
#     await client.delete_messages(messages)
#     await client.say('Messages deleted!')

# @client.event
# async def on_message(message):
#     print('A user has sent a message.')
#     await client.process_commands(message)
#
# @client.command()
# async def ping():
#     await client.say('Pong!')
#
# @client.command()
# async def echo(*args):
#     output = ''
#     for word in args:
#         output += word
#         output += ' '
#     await client.say(output)

# @client.event
# async def on_message(message):
#     author = message.author
#     content = message.content
#     print('{}: {}'.format(author, content))
#
# @client.event
# async def on_message_delete(message):
#     author = message.author
#     content = message.content
#     channel = message.channel
#     await client.send_message(channel, '{}: {}'.format(author, content))

# client.loop.create_task(change_status())
#
# if __name__ == '__main__':
#     for extension in extensions:
#         try:
#             client.load_extension(extension)
#         except Exception as error:
#             print('{} cannot be loaded. [{}]'. format(extension, error))
#
#     client.run(token)