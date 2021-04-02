from discord.ext.commands import Cog
from discord.ext.commands import command
from discord import Embed

class Ayuda(Cog):
  def __init__(self, bot):
    self.bot = bot

  @command(name="ayuda", aliases=["info"])
  async def ayuda(self, ctx):
    
    embed = Embed(title="Información de Aery")

    fields = [("\u200B", "Escribe *aery comandos* para ver qué puede hacer Aerybot.\n\nEste bot fue actualizado por ultima vez el **30/03/21 a las 16:02**\n\nLos datos y builds fueron obtenidos de League of Graphs, para Todas las regiones, Platino+, **parche 11.6**.\n\nSi quieres invitar a este bot a otro server, puedes hacerlo con este link: https://discord.com/oauth2/authorize?client_id=804475973579833374&permissions=1074121728&scope=bot\n\nSi te gustó este bot, considera comprar un kofi a la creadora: https://www.ko-fi.com/lona9", False)]

    for name, value, inline in fields:
      embed.add_field(name=name, value=value, inline=inline)

    embed.set_author(name='Aerybot', icon_url="https://cdn.discordapp.com/attachments/827220123299086447/827222701349404771/Summon_Aery_rune.png")
    embed.set_footer(text="Si presento problemas o necesitas más ayuda, envía un mensaje a lona#4817")

    await ctx.channel.send(embed=embed)

  @command(name="comandos", aliases=["comando"])
  async def comandos(self, ctx):

    embed = Embed(title="Lista de comandos", colour=0xFF0000)
    
    fields = [("\u200B", "Estos son los comandos que puedes utilizar y sus funciones:", False),
      ("\u200B", ":small_blue_diamond: **aery info**: Información general del bot.\n:small_blue_diamond: **aery rotacion:** Rotación semanal actual.\n:small_blue_diamond: **aery normal**: Escribir comando + nombre del champ para ver sus stats y builds para partidas normales (ej: aery normal ashe).\n:small_blue_diamond: **aery aram:** Escribir comando + nombre del champ para ver sus stats y builds para partidas ARAM (ej: aery aram ashe)\n:small_blue_diamond: **aery invitacion:** Envía un DM con un link de invitación al server.", False),
      ("\u200B", "Comandos deben ser escritos en minúsculas. Los nombres de champs se pueden con o sin mayúsculas, con o sin espacios, y con o sin caracteres especiales. Cada champ tiene un set de nombres aceptados, que incluye las abreviaciones más comunes.", False)]

    for name, value, inline in fields:
      embed.add_field(name=name, value=value, inline=inline)
    embed.set_author(name='Aerybot', icon_url="https://cdn.discordapp.com/attachments/827220123299086447/827222701349404771/Summon_Aery_rune.png")
    embed.set_footer(text="Si presento problemas o necesitas más ayuda, menciona o envía un mensaje a lona#4817")

    await ctx.channel.send(embed=embed)

  @command(name='invitacion', aliases=["invite"])
  async def invitacion(self, ctx, *argument):
    invitelink = await ctx.channel.create_invite(max_age=86400,unique=True)

    await ctx.author.send('¡Aquí está el link de invitación al servidor que pediste! Debes usarlo en las siguientes 24 horas antes de que expire. ')
    await ctx.author.send(invitelink)

  @Cog.listener()
  async def on_ready(self):
    if not self.bot.ready:
      self.bot.cogs_ready.ready_up("ayuda")

def setup(bot):
  bot.add_cog(Ayuda(bot))