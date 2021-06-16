from discord.ext.commands import Cog
from discord.ext.commands import command
from discord import Embed
from ..db import db

class Ayuda(Cog):
  def __init__(self, bot):
    self.bot = bot
    self.bot.remove_command("help")

  @command(name="ayuda", aliases=["info", "help"])
  async def ayuda(self, ctx):

    try:
        language = db.record("SELECT GuildLang FROM languages WHERE GuildID = ?", ctx.guild.id)

        language = str(language[0])

    except:
        language = "SP"

    self.testchannel = self.bot.get_channel(827220123299086447)
    channel = self.testchannel

    fecha = "14/06/21, 18:40"

    if language == "SP":

        embed = Embed(title="Información de Aery")

        fields = [("\u200B", "**Aerybot** quiere hacer más fácil y rápida la búsqueda de builds y runas para jugar League of Legends. Se actualiza una vez por semana, y toda la información es obtenida de las runas y builds más populares y con mejor winrate de acuerdo a League of Graphs.", False),
        ("\u200B", f"**NUEVO** Si quieres cambiarle el idioma al bot, escribe *aery lang* para cambiarlo a español/portugués.\n\nEscribe *aery comandos* para ver qué puede hacer Aerybot.\n\nEste bot fue actualizado por ultima vez el **{fecha}**.\n\nLos datos y builds fueron obtenidos de League of Graphs, para Todas las regiones, Platino+, **parche 11.12**.\n\nSi quieres invitar a este bot a otro server, puedes hacerlo con este link: https://discord.com/oauth2/authorize?client_id=804475973579833374&permissions=1074121728&scope=bot\n\nSi te gustó este bot, considera comprar un kofi a la creadora: https://www.ko-fi.com/lona9", False)]

        for name, value, inline in fields:
          embed.add_field(name=name, value=value, inline=inline)

        embed.set_author(name='Aerybot', icon_url="https://cdn.discordapp.com/attachments/827220123299086447/827222701349404771/Summon_Aery_rune.png")
        embed.set_footer(text="Si presento problemas o necesitas más ayuda, envía un mensaje a lona#4817")

        await ctx.channel.send(embed=embed)

    else:
        embed = Embed(title="Informação de Aery")

        fields = [("\u200B", "**Aerybot** quer fazer mais fácil e rápida a busca de builds e runas para jogar League of Legends. Se atualiza uma vez por semana, e toda a informação é obtida das runas e builds mais populares e com melhor winrate de acordo com League of Graphs.", False),
        ("\u200B", f"Escribe *aery comandos* para ver qué puede hacer Escreva aery comandos para ver o que pode fazer Aerybot.\n\nEsse bot foi atualizado pela última vez no **{fecha}**.\n\nOs dados e builds foram obtidos de League of Graphs, para Todas as regiões, Platino+, **parche 11.12**.\n**NUEVO** Se você quiser mudar o idioma do bot, escreva *aery lang* para mudar para espanhol/português.\n\nSe você quiser convidar o bot para outro server, pode fazê-lo com esse link: https://discord.com/oauth2/authorize?client_id=804475973579833374&permissions=1074121728&scope=bot\n\nSe você curtiu esse bot, considere comprar um kofi para a criadora: https://www.ko-fi.com/lona9", False)]

        for name, value, inline in fields:
          embed.add_field(name=name, value=value, inline=inline)

        embed.set_author(name='Aerybot', icon_url="https://cdn.discordapp.com/attachments/827220123299086447/827222701349404771/Summon_Aery_rune.png")
        embed.set_footer(text="Se eu apresentar problemas ou você precisa de mais ajuda, envie uma mensagem a lona#4817")

        await ctx.channel.send(embed=embed)

    try:
      eventmsg = str(ctx.message.content) + ", guild: " + str(ctx.guild.name)
      await self.testchannel.send(eventmsg)
    except AttributeError:
      eventmsg = str(ctx.message.content) + ", guild: None"
      await self.testchannel.send(eventmsg)

  @command(name="comandos", aliases=["comando"])
  async def comandos(self, ctx):

    try:
        language = db.record("SELECT GuildLang FROM languages WHERE GuildID = ?", ctx.guild.id)

        language = str(language[0])

    except:
        language = "SP"

    self.testchannel = self.bot.get_channel(827220123299086447)
    channel = self.testchannel

    if language == "SP":

        embed = Embed(title="Lista de comandos")

        fields = [("\u200B", "Estos son los comandos que puedes utilizar y sus funciones:", False),
          ("\u200B", ":small_blue_diamond: **aery info**: Información general del bot.\n:small_blue_diamond: **aery rotacion:** Rotación semanal actual.\n:small_blue_diamond: **aery normal**: Escribir comando + nombre del champ para ver sus stats y builds para partidas normales (ej: aery normal ashe). \nSi el champ tiene más de una posición, puedes escribir la posición después del nombre para ver las stats específicas. Usar los nombres abreviados (mid, top, adc, supp, jg). Por ejemplo, escribir: *aery normal ekko jg*. El comando sin posición al final mostrará la información promedio para el champ considerando todas las posiciones.\n:small_blue_diamond: **aery aram:** Escribir comando + nombre del champ para ver sus stats y builds para partidas ARAM (ej: aery aram ashe)\n:small_blue_diamond: **aery invitacion:** Envía el link para invitar a Aery a otros servers.", False),
          ("**NUEVO**", ":small_blue_diamond: **aery lang:** Cambia el idioma de Aery a español/portugués\n:small_blue_diamond: **aery support:** Envía tus preguntas, comentarios o sugerencias directamente a la programadora.", False),
          ("\u200B", "Comandos deben ser escritos en minúsculas. Los nombres de champs se pueden con o sin mayúsculas, con o sin espacios, y con o sin caracteres especiales. Cada champ tiene un set de nombres aceptados, que incluye las abreviaciones más comunes.", False)]

        for name, value, inline in fields:
          embed.add_field(name=name, value=value, inline=inline)
        embed.set_author(name='Aerybot', icon_url="https://cdn.discordapp.com/attachments/827220123299086447/827222701349404771/Summon_Aery_rune.png")
        embed.set_footer(text="Si presento problemas o necesitas más ayuda, menciona o envía un mensaje a lona#4817")

        await ctx.channel.send(embed=embed)

    else:
        embed = Embed(title="Lista de comandos")

        fields = [("\u200B", "Esses são os comandos que você pode usar e suas funções:", False),
          ("\u200B", ":small_blue_diamond: **aery info**: Informação geral do bot.\n:small_blue_diamond: **aery rotacion:** Rotação semanal atual.\n:small_blue_diamond: **aery normal**: Escrever comando + nome do champ para ver suas stats e builds para partidas normais (ej: aery normal ashe).\nSe o champ tiver mais de uma posição, você pode escrever a posição depois do nome para ver as stats específicas. Usar os nomes abreviados (mid, top, adc, supp, jg). Por exemplo, escrever: aery normal ekko jg. O comando sem posição no final vai mostrar a informação média para o champ considerando todas as posições.\n:small_blue_diamond: **aery aram:** Escrever comando + nome do champ para ver suas stats e builds para partidas ARAM (ej: aery aram ashe)\n:small_blue_diamond: **aery invitacion:** Envia o link para convidar a Aery a outros servers.\n:small_blue_diamond: **aery support:** Envie suas dúvidas, comentários e sugestões para o programador.", False),
          ("**NOVO**", "\n:small_blue_diamond: **aery support:** Envie suas dúvidas, comentários e sugestões para o programador.\n:small_blue_diamond: **aery lang:** Usa esse comando para mudar a língua do bot a português/espanhol", False),
          ("\u200B", "Comandos devem ser escritos com letras minúsculas. Os nomes dos champs se podem escrever com ou sem maiúsculas, com ou sem espaços, e com ou sem caráteres especiais. Cada champ tem um set de nomes aceitos, que inclui as abreviações mais comuns.", False)]

        for name, value, inline in fields:
          embed.add_field(name=name, value=value, inline=inline)
        embed.set_author(name='Aerybot', icon_url="https://cdn.discordapp.com/attachments/827220123299086447/827222701349404771/Summon_Aery_rune.png")
        embed.set_footer(text="Se eu apresentar problemas ou você precisa de mais ajuda, envie uma mensagem a lona#4817")

        await ctx.channel.send(embed=embed)

    try:
      eventmsg = str(ctx.message.content) + ", guild: " + str(ctx.guild.name)
      await self.testchannel.send(eventmsg)
    except AttributeError:
      eventmsg = str(ctx.message.content) + ", guild: None"
      await self.testchannel.send(eventmsg)

  @command(name='invitacion', aliases=["invite"])
  async def invitacion(self, ctx):
    try:
        language = db.record("SELECT GuildLang FROM languages WHERE GuildID = ?", ctx.guild.id)

        language = str(language[0])

    except:
        language = "SP"

    self.testchannel = self.bot.get_channel(827220123299086447)
    channel = self.testchannel

    if language == "SP":

        await ctx.channel.send("Puedes invitar a Aery a otros servers con el siguiente link: https://discord.com/oauth2/authorize?client_id=804475973579833374&permissions=1074121728&scope=bot")
    else:
        await ctx.channel.send("Você pode convidar Aery para outros servidores com o seguinte link: https://discord.com/oauth2/authorize?client_id=804475973579833374&permissions=1074121728&scope=bot")

    try:
      eventmsg = str(ctx.message.content) + ", guild: " + str(ctx.guild.name)
      await self.testchannel.send(eventmsg)
    except AttributeError:
      eventmsg = str(ctx.message.content) + ", guild: None"
      await self.testchannel.send(eventmsg)

  @command(name="support")
  async def support(self, ctx, *args):

    self.support = self.bot.get_channel(852601490581094420)
    channel = self.support

    args = str(" ".join(args))

    await self.support.send(f"{ctx.message.author}: {args}")
    await ctx.send(":white_check_mark:")

  @Cog.listener()
  async def on_ready(self):
    if not self.bot.ready:
      self.bot.cogs_ready.ready_up("ayuda")

def setup(bot):
  bot.add_cog(Ayuda(bot))
