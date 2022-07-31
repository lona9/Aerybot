from discord.ext.commands import Cog
from discord.ext.commands import command
from discord import Embed
from ..db import db
import os
import pendulum
import datetime
from datetime import datetime

class Ayuda(Cog):
  def __init__(self, bot):
    self.bot = bot
    self.bot.remove_command("help")

  @command(name="ayuda", aliases=["info", "help"])
  async def ayuda(self, ctx):
    self.testchannel = self.bot.get_channel(827220123299086447)

    try:
        language = db.record("SELECT GuildLang FROM languages WHERE GuildID = ?", ctx.guild.id)

        language = str(language[0])

    except:
        language = "SP"

    fecha = "31/07/22"
    parche = "12.14"

    if language == "SP":

        embed = Embed(title="Información de Aery")

        fields = [("\u200B", "**IMPORTANTE**: Desde el 7 de agosto, Aerybot solo funcionará con slash commands. Si no puedes usarlos en tu servidor actualmente, reinvita a Aery para arreglar los permisos.\nLink para reinvitar: https://discord.com/api/oauth2/authorize?client_id=804475973579833374&permissions=8&scope=bot%20applications.commands", False)]

        for name, value, inline in fields:
          embed.add_field(name=name, value=value, inline=inline)

        embed.set_author(name='Aerybot', icon_url="https://cdn.discordapp.com/attachments/827220123299086447/827222701349404771/Summon_Aery_rune.png")
        embed.set_footer(text="Si presento problemas o necesitas más ayuda, envía un mensaje a lona#4817")

        await ctx.channel.send(embed=embed)

    else:
        embed = Embed(title="Informação de Aery")

        fields = [("\u200B", "**IMPORTANTE**: A partir de 7 de agosto, o Aerybot funcionará apenas com comandos de barra. Se você não pode usá-los em seu servidor atualmente, convide novamente Aery para corrigir as permissões\nLink para convidar novamente: https://discord.com/api/oauth2/authorize?client_id=804475973579833374&permissions=8&scope=bot%20applications.commands", False)]

        for name, value, inline in fields:
          embed.add_field(name=name, value=value, inline=inline)

        embed.set_author(name='Aerybot', icon_url="https://cdn.discordapp.com/attachments/827220123299086447/827222701349404771/Summon_Aery_rune.png")
        embed.set_footer(text="Se eu apresentar problemas ou você precisa de mais ajuda, envie uma mensagem a lona#4817")

        await ctx.channel.send(embed=embed)

    try:
      eventmsg = str(ctx.message.content) + ", guild: " + str(ctx.guild.name)
      await self.testchannel.send(eventmsg)

      with open(os.path.join("/root/aery/data/logs", "logs.txt"), "a") as file:
          tz = pendulum.timezone('America/La_Paz')
          datetime_cl = datetime.now(tz)
          timestamp = datetime_cl.strftime("%d/%m/%y %H:%M:%S")
          log_msg = timestamp + " " + eventmsg + "\n"
          file.write(log_msg)

    except AttributeError:
      eventmsg = str(ctx.message.content) + ", guild: None"
      await self.testchannel.send(eventmsg)

      with open(os.path.join("/root/aery/data/logs", "logs.txt"), "a") as file:
          tz = pendulum.timezone('America/La_Paz')
          datetime_cl = datetime.now(tz)
          timestamp = datetime_cl.strftime("%d/%m/%y %H:%M:%S")
          log_msg = timestamp + " " + eventmsg + "\n"
          file.write(log_msg)

#  @command(name="comandos", aliases=["comando"])
#  async def comandos(self, ctx):
#    self.testchannel = self.bot.get_channel(827220123299086447)

#    try:
#        language = db.record("SELECT GuildLang FROM languages WHERE GuildID = ?", ctx.guild.id)

#        language = str(language[0])

#    except:
#        language = "SP"

#    if language == "SP":

#        embed = Embed(title="Lista de comandos")

#        fields = [("\u200B", "Estos son los comandos que puedes utilizar y sus funciones:", False),
#          ("\u200B", ":small_blue_diamond: **aery info**: Información general del bot.\n:small_blue_diamond: **aery normal**: Escribir comando + nombre del champ para ver sus stats y builds para partidas normales (ej: aery normal ashe). \nSi el champ tiene más de una posición, puedes escribir la posición después del nombre para ver las stats específicas. Usar los nombres abreviados (mid, top, adc, supp, jg). Por ejemplo, escribir: *aery normal ekko jg*. El comando sin posición al final mostrará la información promedio para el champ considerando todas las posiciones.\n:small_blue_diamond: **aery aram:** Escribir comando + nombre del champ para ver sus stats y builds para partidas ARAM (ej: aery aram ashe)\n:small_blue_diamond: **aery invitacion:** Envía el link para invitar a Aery a otros servers.", False),
#          ("\u200B", ":small_blue_diamond: **aery lang:** Cambia el idioma de Aery a español/portugués (solo dentro de un server, no en DM)\n:small_blue_diamond: **aery support:** Envía tus preguntas, comentarios o sugerencias directamente a la programadora.", False),
#          ("\u200B", "Comandos deben ser escritos en minúsculas. Los nombres de champs se pueden con o sin mayúsculas, con o sin espacios, y con o sin caracteres especiales. Cada champ tiene un set de nombres aceptados, que incluye las abreviaciones más comunes.", False)]

#        for name, value, inline in fields:
#          embed.add_field(name=name, value=value, inline=inline)
#        embed.set_author(name='Aerybot', icon_url="https://cdn.discordapp.com/attachments/827220123299086447/827222701349404771/Summon_Aery_rune.png")
#        embed.set_footer(text="Si presento problemas o necesitas más ayuda, menciona o envía un mensaje a lona#4817")

#        await ctx.channel.send(embed=embed)

#    else:
#        embed = Embed(title="Lista de comandos")

#        fields = [("\u200B", "Esses são os comandos que você pode usar e suas funções:", False),
#          ("\u200B", ":small_blue_diamond: **aery info**: Informação geral do bot.\n:small_blue_diamond: **aery normal**: Escrever comando + nome do champ para ver suas stats e builds para partidas normais (ej: aery normal ashe).\nSe o champ tiver mais de uma posição, você pode escrever a posição depois do nome para ver as stats específicas. Usar os nomes abreviados (mid, top, adc, supp, jg). Por exemplo, escrever: aery normal ekko jg. O comando sem posição no final vai mostrar a informação média para o champ considerando todas as posições.\n:small_blue_diamond: **aery aram:** Escrever comando + nome do champ para ver suas stats e builds para partidas ARAM (ej: aery aram ashe)\n:small_blue_diamond: **aery invitacion:** Envia o link para convidar a Aery a outros servers.\n:small_blue_diamond: **aery support:** Envie suas dúvidas, comentários e sugestões para o programador.", False),
#          ("\u200B", "\n:small_blue_diamond: **aery support:** Envie suas dúvidas, comentários e sugestões para o programador.\n:small_blue_diamond: **aery lang:** Usa esse comando para mudar a língua do bot a português/espanhol (Apenas dentro de um servidor, sem DM)", False),
#          ("\u200B", "Comandos devem ser escritos com letras minúsculas. Os nomes dos champs se podem escrever com ou sem maiúsculas, com ou sem espaços, e com ou sem caráteres especiais. Cada champ tem um set de nomes aceitos, que inclui as abreviações mais comuns.", False)]

#        for name, value, inline in fields:
#          embed.add_field(name=name, value=value, inline=inline)
#        embed.set_author(name='Aerybot', icon_url="https://cdn.discordapp.com/attachments/827220123299086447/827222701349404771/Summon_Aery_rune.png")
#        embed.set_footer(text="Se eu apresentar problemas ou você precisa de mais ajuda, envie uma mensagem a lona#4817")

#        await ctx.channel.send(embed=embed)

  @command(name='invitacion', aliases=["invite"])
  async def invitacion(self, ctx):
    self.testchannel = self.bot.get_channel(827220123299086447)

    try:
        language = db.record("SELECT GuildLang FROM languages WHERE GuildID = ?", ctx.guild.id)

        language = str(language[0])

    except:
        language = "SP"

    if language == "SP":

        await ctx.channel.send("Puedes invitar a Aery a otros servers con el siguiente link: https://discord.com/api/oauth2/authorize?client_id=804475973579833374&permissions=8&scope=bot%20applications.commands")
    else:
        await ctx.channel.send("Você pode convidar Aery para outros servidores com o seguinte link: https://discord.com/api/oauth2/authorize?client_id=804475973579833374&permissions=8&scope=bot%20applications.commands")

    try:
      eventmsg = str(ctx.message.content) + ", guild: " + str(ctx.guild.name)
      await self.testchannel.send(eventmsg)

      with open(os.path.join("/root/aery/data/logs", "logs.txt"), "a") as file:
          tz = pendulum.timezone('America/La_Paz')
          datetime_cl = datetime.now(tz)
          timestamp = datetime_cl.strftime("%d/%m/%y %H:%M:%S")
          log_msg = timestamp + " " + eventmsg + "\n"
          file.write(log_msg)

    except AttributeError:
      eventmsg = str(ctx.message.content) + ", guild: None"
      await self.testchannel.send(eventmsg)

      with open(os.path.join("/root/aery/data/logs", "logs.txt"), "a") as file:
          tz = pendulum.timezone('America/La_Paz')
          datetime_cl = datetime.now(tz)
          timestamp = datetime_cl.strftime("%d/%m/%y %H:%M:%S")
          log_msg = timestamp + " " + eventmsg + "\n"
          file.write(log_msg)

  @Cog.listener()
  async def on_ready(self):
    if not self.bot.ready:
      self.bot.cogs_ready.ready_up("ayuda")

def setup(bot):
  bot.add_cog(Ayuda(bot))
