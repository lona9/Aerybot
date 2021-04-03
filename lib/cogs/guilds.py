from discord.ext.commands import Cog
from apscheduler.triggers.cron import CronTrigger
from discord import Activity, ActivityType
from discord.ext.commands import command

class Guilds(Cog):
  def __init__(self, bot):
    self.bot = bot

  @Cog.listener()
  async def on_guild_join(self, guild):
    lona = await self.bot.fetch_user(485054727755792410)
    await lona.send('aery se unió a {} ({} miembros)'.format(guild.name, guild.member_count))

  @Cog.listener()
  async def on_guild_remove(self, guild):
    lona = await self.bot.fetch_user(485054727755792410)
    await lona.send('aery fue expulsada de {} ({} miembros)'.format(guild.name, guild.member_count))

  @Cog.listener()
  async def on_ready(self):
    if not self.bot.ready:
      self.bot.cogs_ready.ready_up("guilds")

def setup(bot):
  bot.add_cog(Guilds(bot))