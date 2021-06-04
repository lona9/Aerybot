from discord.ext.commands import Cog
from discord.ext.commands import command

from ..db import db

class Guilds(Cog):
  def __init__(self, bot):
    self.bot = bot

  @command()
  async def guilds(self, ctx):
    guilds = len(self.bot.guilds)
    await ctx.channel.send(f"aery es parte de {guilds} guilds.")

  @command()
  async def lang(self, ctx):
    await ctx.channel.send("Escoge el lenguaje de Aery / Escolha o idioma do Aery:\n*sp*: español\n*pt*: português.")
    try:
        message = await self.bot.wait_for('message', timeout = 45.0, check=lambda message: message.author == ctx.author)
    except:
        await channel.send("Se acabó el tiempo / Acabou o tempo")
    else:
        if message.content.lower() == "sp" or "español":
            db.execute("UPDATE languages SET GuildLang = ?", "SP")

            await ctx.channel.send("Aery ahora está en español.")

            db.commit()

        elif message.content.lower() == "pt" or message.content.lower() == "portugués" or message.content.lower() == "português":
            db.execute("UPDATE languages SET GuildLang = ?", "PT")

            await ctx.channel.send("Aery esta agora em portugues.")

            db.commit()

        else:
            await ctx.channel.send("Debes escoger una opción válida / Você deve escolher uma opção válida")

  @Cog.listener()
  async def on_guild_join(self, guild):

    self.testchannel = self.bot.get_channel(827220123299086447)
    channel = self.testchannel

    await self.testchannel.send('aery se unió a {} ({} miembros)'.format(guild.name, guild.member_count))

  @Cog.listener()
  async def on_guild_remove(self, guild):

    self.testchannel = self.bot.get_channel(827220123299086447)
    channel = self.testchannel

    await self.testchannel.send('aery fue expulsada de {} ({} miembros)'.format(guild.name, guild.member_count))

  @Cog.listener()
  async def on_ready(self):
    if not self.bot.ready:
      self.bot.cogs_ready.ready_up("guilds")

def setup(bot):
  bot.add_cog(Guilds(bot))
