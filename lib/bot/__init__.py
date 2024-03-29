import discord
from asyncio import sleep
from discord import Intents
import pendulum
import datetime
from datetime import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from discord.ext.commands import Bot as BotBase
from discord.ext.commands import Context
from discord.ext.commands import CommandNotFound


from ..db import db

PREFIX = "aery "

OWNER_IDS = [485054727755792410]

COGS = ["ayuda", "aram", "normal"]

class Ready(object):
  def __init__(self):
    for cog in COGS:
      setattr(self, cog, False)

  def ready_up(self, cog):
    setattr(self, cog, True)
    print(f" {cog} cog ready")

  def all_ready(self):
    return all([getattr(self, cog) for cog in COGS])


class Bot(BotBase):
  def __init__(self):
    self.PREFIX = PREFIX
    self.ready = False
    self.cogs_ready = Ready()
    self.guild = None
    self.scheduler = AsyncIOScheduler()

    intents = Intents.default()

    db.autosave(self.scheduler)

    super().__init__(
      command_prefix=PREFIX,
      owner_ids=OWNER_IDS,
      intents=Intents.default()
      )

  def setup(self):
    for cog in COGS:
      self.load_extension(f"lib.cogs.{cog}")
      print(f" {cog} cog loaded")

    print("setup complete")

  def update_db(self):
    db.multiexec("INSERT OR IGNORE INTO languages (GuildID) VALUES (?)",
					 ((guild.id,) for guild in self.guilds))

    for guild in self.guilds:
        db.execute("UPDATE languages SET GuildName = ?, GuildSize = ? WHERE GuildID = ?",
        guild.name, guild.member_count, guild.id)

    db.commit()

    to_remove = []
    stored_guilds = db.column("SELECT GuildID FROM languages")
    for id_ in stored_guilds:
      if not self.guilds:
        to_remove.append(id_)

    db.multiexec("DELETE FROM languages WHERE GuildID = ?",
					 ((id_,) for id_ in to_remove))

    db.commit()

  def run(self, version):
      self.VERSION = version

      print("running setup...")
      self.setup()

      with open("./lib/bot/.env", "r", encoding="utf-8") as tf:
        self.TOKEN = tf.read()

      print('running bot...')
      super().run(self.TOKEN, reconnect=True)

  async def process_commands(self, message):
    ctx = await self.get_context(message, cls=Context)

    if ctx.command is not None:
      if self.ready:
        await self.invoke(ctx)

      else:
        await ctx.send("Aún no estoy lista para recibir comandos, por favor espera unos segundos.")

  async def on_connect(self):

    tz = pendulum.timezone('America/La_Paz')
    datetime_cl = datetime.now(tz)
    timestamp = datetime_cl.strftime("%d/%m/%y %H:%M:%S")

    print(f'{timestamp} - bot connected')


  async def on_disconnect(self):
    tz = pendulum.timezone('America/La_Paz')
    datetime_cl = datetime.now(tz)
    timestamp = datetime_cl.strftime("%d/%m/%y %H:%M:%S")

    print(f'{timestamp} - offline')


  async def on_error(self, err, *args, **kwargs):
    if err == "on_command_error":
      pass

    await self.testchannel.send("Ocurrió un error.")

    raise

  async def on_command_error(self, ctx, exc):
    if isinstance(exc, CommandNotFound):
      pass

    elif hasattr(exc, "original"):
      raise exc

    else:
      raise exc

  async def on_ready(self):
    if not self.ready:

      self.testchannel = self.get_channel(827220123299086447)
      channel = self.testchannel

      self.scheduler.start()
      self.update_db()

      await self.testchannel.send("Estoy lista, estoy lista, estoy lista, estoy lista!")
      self.ready = True
      print("bot ready")

      meta = self.get_cog("Meta")
      await meta.set()

    else:
      tz = pendulum.timezone('America/La_Paz')
      datetime_cl = datetime.now(tz)
      timestamp = datetime_cl.strftime("%d/%m/%y %H:%M:%S")

      print(f"{timestamp} - reconnected")

  async def on_message(self, message):
    if not message.author.bot:
      await self.process_commands(message)

bot = Bot()
