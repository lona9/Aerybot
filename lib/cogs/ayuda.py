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

    if language == "SP":

        embed = Embed(title="Información de Aery")

        fields = [("\u200B", "`ATENCIÓN`: Los comandos con prefijo funcionarán inestablemente hasta el 31 de agosto, después de esa fecha solo funcionarán los slash commands. Ambos estarán disponibles hasta esa fecha, pero sujetos a los blackouts de Discord, lo cual no depende de mi desarrollo. Disculpas por los inconvenientes, es culpa de Discord :P\nEscribe `/help` o `/commands` para ver los comandos disponibles. Si no puedes usarlos en tu servidor actualmente, reinvita a Aery para arreglar los permisos.\n[Link para reinvitar](https://discord.com/api/oauth2/authorize?client_id=804475973579833374&permissions=8&scope=bot%20applications.commands)", False)]

        for name, value, inline in fields:
          embed.add_field(name=name, value=value, inline=inline)

        embed.set_author(name='Aerybot', icon_url="https://cdn.discordapp.com/attachments/827220123299086447/827222701349404771/Summon_Aery_rune.png")
        embed.set_footer(text="Si presento problemas o necesitas más ayuda, envía un mensaje a lona#4817")

        await ctx.channel.send(embed=embed)

    else:
        embed = Embed(title="Informação de Aery")

        fields = [("\u200B", "`ATENÇÃO`: Comandos prefixados funcionarão instáveis ​​até 31 de agosto, após essa data apenas slash commands funcionarão. Ambos estarão disponíveis até essa data, mas sujeitos a apagões do Discord, que não dependem de mim. Desculpe pelo inconveniente, é culpa do Discord :P\nDigite `/help` ou `/commands` para ver os comandos disponíveis. Se você não pode usá-los em seu servidor atualmente, convide novamente Aery para corrigir as permissões\n[Link para convidar novamente](https://discord.com/api/oauth2/authorize?client_id=804475973579833374&permissions=8&scope=bot%20applications.commands)", False)]

        for name, value, inline in fields:
          embed.add_field(name=name, value=value, inline=inline)

        embed.set_author(name='Aerybot', icon_url="https://cdn.discordapp.com/attachments/827220123299086447/827222701349404771/Summon_Aery_rune.png")
        embed.set_footer(text="Se eu apresentar problemas ou você precisa de mais ajuda, envie uma mensagem a lona#4817")

        await ctx.channel.send(embed=embed)

  @command(name='invitacion', aliases=["invite"])
  async def invitacion(self, ctx):
    self.testchannel = self.bot.get_channel(827220123299086447)

    try:
        language = db.record("SELECT GuildLang FROM languages WHERE GuildID = ?", ctx.guild.id)

        language = str(language[0])

    except:
        language = "SP"

    if language == "SP":

        await ctx.channel.send("Puedes invitar a Aery a otros servers con [este link](https://discord.com/api/oauth2/authorize?client_id=804475973579833374&permissions=8&scope=bot%20applications.commands)")
    else:
        await ctx.channel.send("Você pode convidar Aery para outros servidores com o [seguinte link](https://discord.com/api/oauth2/authorize?client_id=804475973579833374&permissions=8&scope=bot%20applications.commands)")

    try:
      eventmsg = str(ctx.message.content) + ", guild: " + str(ctx.guild.name)
      await self.testchannel.send(eventmsg)

    except AttributeError:
      eventmsg = str(ctx.message.content) + ", guild: None"
      await self.testchannel.send(eventmsg)

  @Cog.listener()
  async def on_ready(self):
    if not self.bot.ready:
      self.bot.cogs_ready.ready_up("ayuda")

def setup(bot):
  bot.add_cog(Ayuda(bot))
