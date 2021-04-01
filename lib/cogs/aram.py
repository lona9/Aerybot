from discord.ext.commands import Cog
from discord.ext.commands import command
from discord import Embed

class Aram(Cog):
  def __init__(self, bot):
    self.bot = bot

  @command(name="aram")
  async def aram(self, ctx):
    await ctx.channel.send(
		    "**Los champs en rotación de esta semana son:** Ekko, Jarvan IV, Jayce, Jinx, Kha'Zix, Lucian, Maokai, Mordekaiser, Neeko, Orianna, Rengar, Thresh, Twisted Fate, Zed, Zyra")

  @Cog.listener()
  async def on_ready(self):
    if not self.bot.ready:
      self.bot.cogs_ready.ready_up("aram")

def setup(bot):
  bot.add_cog(Aram(bot))