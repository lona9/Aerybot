from discord.ext.commands import Cog
from discord.ext.commands import command
from discord import Embed
from ..db import db

class Rotacion(Cog):
  def __init__(self, bot):
    self.bot = bot

  @command(name="rotacion", aliases=["rota"])
  async def rotacion(self, ctx):

    language = db.record("SELECT GuildLang FROM languages WHERE GuildID = ?", ctx.guild.id)

    language = str(language[0])

    self.testchannel = self.bot.get_channel(827220123299086447)
    channel = self.testchannel

    champs = "Aatrox, Akali, Amumu, Aphelios, Bardo, Gangplank, Karthus, Kayn, Lee Sin, Samira, Soraka, Tahm Kench, Teemo, Twisted Fate, Vladimir"

    if language == "SP":

        await ctx.channel.send(
    		    f"**Los champs en rotación de esta semana son:** {champs}.")

    else:
        await ctx.channel.send(
    		    f"**Os champs na rotação dessa semana são:** {champs}")

    try:
      eventmsg = str(ctx.message.content) + ", guild: " + str(ctx.guild.name)
      await self.testchannel.send(eventmsg)
    except AttributeError:
      eventmsg = str(ctx.message.content) + ", guild: None"
      await self.testchannel.send(eventmsg)

  @Cog.listener()
  async def on_ready(self):
    if not self.bot.ready:
      self.bot.cogs_ready.ready_up("rotacion")

def setup(bot):
  bot.add_cog(Rotacion(bot))
