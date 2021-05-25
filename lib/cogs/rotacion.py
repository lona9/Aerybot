from discord.ext.commands import Cog
from discord.ext.commands import command
from discord import Embed

class Rotacion(Cog):
  def __init__(self, bot):
    self.bot = bot

  @command(name="rotacion", aliases=["rota"])
  async def rotacion(self, ctx):
    self.testchannel = self.bot.get_channel(827220123299086447)
    channel = self.testchannel

    await ctx.channel.send(
		    "**Los champs en rotación de esta semana son:** Aurelion Sol, Braum, Camille, Cho'Gath, Diana, Dr. Mundo, Katarina, Maestro Yi, Nunu, Ornn, Quinn, Shyvana, Sivir, Xayah, Yuumi.")

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
