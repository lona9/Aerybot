from discord.ext.commands import Cog
from discord.ext.commands import command
import os
import pendulum
import datetime
from datetime import datetime
from ..db import db

class Guilds(Cog):
  def __init__(self, bot):
    self.bot = bot
    self.testchannel = self.bot.get_channel(827220123299086447)

  @command()
  async def guilds(self, ctx):
    guilds = len(self.bot.guilds)
    await ctx.channel.send(f"aery es parte de {guilds} guilds.")

  @command()
  async def lang(self, ctx):
    self.testchannel = self.bot.get_channel(827220123299086447)

    try:
        language = db.record("SELECT GuildLang FROM languages WHERE GuildID = ?", ctx.guild.id)

        language = str(language[0])

        await ctx.channel.send("Escoge el lenguaje de Aery / Escolha o idioma do Aery:\n**sp**: español\n**pt**: português.")

        try:
            message = await self.bot.wait_for('message', timeout = 15.0, check=lambda message: message.author == ctx.author)

            if message.content.lower() == "sp" or message.content.lower() == "español":
                db.execute("UPDATE languages SET GuildLang = ? WHERE GuildID = ?", "SP", ctx.guild.id)

                db.commit()

                await ctx.channel.send("Aery ahora está en español.")

                eventmsg = str(ctx.message.content) + " " + str(message.content) + ", guild: " + str(ctx.guild.name)

                await self.testchannel.send(eventmsg)

                with open(os.path.join("/root/aery/data/logs", "logs.txt"), "a") as file:
                    tz = pendulum.timezone('America/La_Paz')
                    datetime_cl = datetime.now(tz)
                    timestamp = datetime_cl.strftime("%d/%m/%y %H:%M:%S")
                    log_msg = timestamp + " " + eventmsg + "\n"
                    file.write(log_msg)


            elif message.content.lower() == "pt" or message.content.lower() == "portugués" or message.content.lower() == "português":
                db.execute("UPDATE languages SET GuildLang = ? WHERE GuildID = ?", "PT", ctx.guild.id)

                db.commit()

                await ctx.channel.send("Aery esta agora em portugues.")

                eventmsg = str(ctx.message.content) + " " + str(message.content) + ", guild: " + str(ctx.guild.name)

                await self.testchannel.send(eventmsg)

                with open(os.path.join("/root/aery/data/logs", "logs.txt"), "a") as file:
                    tz = pendulum.timezone('America/La_Paz')
                    datetime_cl = datetime.now(tz)
                    timestamp = datetime_cl.strftime("%d/%m/%y %H:%M:%S")
                    log_msg = timestamp + " " + eventmsg + "\n"
                    file.write(log_msg)

            else:
                await ctx.channel.send("Debes escoger una opción válida / Você deve escolher uma opção válida")

                eventmsg = str(ctx.message.content) + " " + "sin opción válida" + ", guild: " + str(ctx.guild.name)

                await self.testchannel.send(eventmsg)

                with open(os.path.join("/root/aery/data/logs", "logs.txt"), "a") as file:
                    tz = pendulum.timezone('America/La_Paz')
                    datetime_cl = datetime.now(tz)
                    timestamp = datetime_cl.strftime("%d/%m/%y %H:%M:%S")
                    log_msg = timestamp + " " + eventmsg + "\n"
                    file.write(log_msg)

        except:
            await ctx.channel.send("Se acabó el tiempo / Acabou o tempo")
            eventmsg = str(ctx.message.content) + " " + "timeout" + ", guild: " + str(ctx.guild.name)

            await self.testchannel.send(eventmsg)

            with open(os.path.join("/root/aery/data/logs", "logs.txt"), "a") as file:
                tz = pendulum.timezone('America/La_Paz')
                datetime_cl = datetime.now(tz)
                timestamp = datetime_cl.strftime("%d/%m/%y %H:%M:%S")
                log_msg = timestamp + " " + eventmsg + "\n"
                file.write(log_msg)

    except:
        await ctx.channel.send("Este comando solo puede ocuparse dentro de un servidor // Este comando só pode ser usado em um servidor.")

        eventmsg = str(ctx.message.content) + " " + "dm"
        await self.testchannel.send(eventmsg)

        with open(os.path.join("/root/aery/data/logs", "logs.txt"), "a") as file:
            tz = pendulum.timezone('America/La_Paz')
            datetime_cl = datetime.now(tz)
            timestamp = datetime_cl.strftime("%d/%m/%y %H:%M:%S")
            log_msg = timestamp + " " + eventmsg + "\n"
            file.write(log_msg)


  @Cog.listener()
  async def on_guild_join(self, guild):
    self.testchannel = self.bot.get_channel(827220123299086447)

    eventmsg = f'aery se unió a {guild.name} ({guild.member_count} miembros)'

    await self.testchannel.send(eventmsg)

    with open(os.path.join("/root/aery/data/logs", "logs.txt"), "a") as file:
        tz = pendulum.timezone('America/La_Paz')
        datetime_cl = datetime.now(tz)
        timestamp = datetime_cl.strftime("%d/%m/%y %H:%M:%S")
        log_msg = timestamp + " " + eventmsg + "\n"
        file.write(log_msg)

    db.execute("INSERT OR IGNORE INTO languages (GuildID) VALUES (?)", guild.id)
    db.commit()

  @Cog.listener()
  async def on_guild_remove(self, guild):
    self.testchannel = self.bot.get_channel(827220123299086447)

    eventmsg = f"aery fue expulsada de {guild.name} ({guild.member_count})"

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
      self.bot.cogs_ready.ready_up("guilds")

def setup(bot):
  bot.add_cog(Guilds(bot))
