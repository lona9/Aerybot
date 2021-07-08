from discord.ext.commands import Cog
from discord.ext.commands import command
from discord import Embed
from ..db import db
import os
import pendulum
import datetime
from datetime import datetime

class Rotacion(Cog):
  def __init__(self, bot):
    self.bot = bot

  @command(name="rotacion", aliases=["rota"])
  async def rotacion(self, ctx):

    try:
        language = db.record("SELECT GuildLang FROM languages WHERE GuildID = ?", ctx.guild.id)

        language = str(language[0])

    except:
        language = "SP"

    self.testchannel = self.bot.get_channel(827220123299086447)
    channel = self.testchannel

    champs = "Anivia, Annie, Brand, Hecarim, Ivern, Jhin, Kennen, Kindred, Lux, Poppy, Pyke, Renekton, Sett, Sylas, Vayne"

    if language == "SP":

        await ctx.channel.send(
    		    f"**Los champs en rotación de esta semana son:** {champs}.")

    else:
        await ctx.channel.send(
    		    f"**Os champs na rotação dessa semana são:** {champs}")

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
      self.bot.cogs_ready.ready_up("rotacion")

def setup(bot):
  bot.add_cog(Rotacion(bot))
