from discord.ext.commands import Cog
from discord.ext.commands import command
from discord import Embed

class Rotacion(Cog):
  def __init__(self, bot):
    self.bot = bot

  @command(name="rotacion", aliases=["rota"])
  async def rotacion(self, ctx):
    await ctx.channel.send(
		    "**Los champs en rotación de esta semana son:** Ekko, Jarvan IV, Jayce, Jinx, Kha'Zix, Lucian, Maokai, Mordekaiser, Neeko, Orianna, Rengar, Thresh, Twisted Fate, Zed, Zyra")

  @Cog.listener()
  async def on_ready(self):
    if not self.bot.ready:
      self.bot.cogs_ready.ready_up("rotacion")

def setup(bot):
  bot.add_cog(Rotacion(bot))