from discord.ext.commands import Cog
from discord.ext.commands import command
import os

class Normal(Cog):
  def __init__(self, bot):
    self.bot = bot

  @command(name="normal")
  async def normal(self, ctx, *args):

    self.testchannel = self.bot.get_channel(827220123299086447)
    channel = self.testchannel

    if args == ():
      await ctx.channel.send('¡Debes escribir el nombre de un champ después de *aery aram*!')

    else:
      charsearch = "".join(args).lower().replace("'", "").replace(".", "")

      champions = {"aatrox": ["aatrox"],
                  "ahri": ["ahri"],
                  "akali": ["akali"],
                  "alistar": ["alistar"],
                  "amumu": ["amumu"],
                  "anivia": ["anivia"],
                  "annie": ["annie"],
                  "aphelios": ["aphelios"],
                  "ashe": ["ashe"],
                  "aurelionsol": ["aurelion", "sol", "aurelionsol"],
                  "azir": ["azir"],
                  "bard": ["bard", "bardo"],
                  "blitzcrank": ["blitz", "blitzcrank"],
                  "brand": ["brand"],
                  "braum": ["braum"],
                  "caitlyn": ["cait", "caitlyn"],
                  "camille": ["camille"],
                  "cassiopeia": ["cassiopeia", "cassio", "cassi"],
                  "chogath": ["chogath", "cho"],
                  "corki": ["corki"],
                  "darius": ["darius"],
                  "diana": ["diana"],
                  "drmundo": ["drmundo", "mundo", "dr"],
                  "draven": ["draven"],
                  "ekko": ["ekko"],
                  "elise": ["elise"],
                  "evelynn": ["evelynn", "eve"],
                  "ezreal": ["ez", "ezreal"],
                  "fiddlesticks": ["fiddlesticks", "fiddle"],
                  "fiora": ["fiora"],
                  "fizz": ["fizz"],
                  "galio": ["galio"],
                  "gangplank": ["gangplank", "gang"],
                  "garen": ["garen"],
                  "gnar": ["gnar"],
                  "gragas": ["gragas"],
                  "graves": ["graves"],
                  "gwen": ["gwen"],
                  "hecarim": ["hecarim", "hec", "heca"],
                  "heimerdinger": ["heimerdinger", "heim", "heimer"],
                  "illaoi": ["illaoi"],
                  "irelia": ["irelia"],
                  "ivern": ["ivern"],
                  "janna": ["janna"],
                  "jarvaniv": ["jarvaniv", "jarvan"],
                  "jax": ["jax"],
                  "jayce": ["jayce"],
                  "jhin": ["jhin", "jihn", "jin"],
                  "jinx": ["jinx"],
                  "kaisa": ["kaisa"],
                  "kalista": ["kalista"],
                  "karma": ["karma"],
                  "karthus": ["karthus"],
                  "kassadin": ["kassadin", "kass"],
                  "katarina": ["katarina", "kat", "kata"],
                  "kayle": ["kayle"],
                  "kayn": ["kayn"],
                  "kennen": ["kennen"],
                  "khazix": ["k6", "khazix"],
                  "kindred": ["kindred", "kind"],
                  "kled": ["kled"],
                  "kogmaw": ["kogmaw", "kog", "maw"],
                  "leblanc": ["leblanc"],
                  "leesin": ["leesin", "lee", "sin"],
                  "leona": ["leona"],
                  "lillia": ["lillia"],
                  "lissandra": ["liss", "lissandra"],
                  "lucian": ["lucian"],
                  "lulu": ["lulu"],
                  "lux": ["lux"],
                  "malphite": ["malphite", "malph"],
                  "malzahar": ["malzahar"],
                  "maokai": ["maokai"],
                  "masteryi": ["masteryi", "maestroyi", "yi"],
                  "missfortune": ["missfortune", "mf", "miss"],
                  "mordekaiser": ["mordekaiser", "morde"],
                  "morgana": ["morgana", "morg"],
                  "nami": ["nami"],
                  "nasus": ["nasus"],
                  "nautilus": ["nautilus", "nauti"],
                  "neeko": ["neeko"],
                  "nidalee": ["nidalee", "nida"],
                  "nocturne": ["nocturne", "noct"],
                  "nunu": ["nunu", "nunuywillump"],
                  "olaf": ["olaf"],
                  "orianna": ["orianna"],
                  "ornn": ["ornn"],
                  "pantheon": ["pantheon", "pant", "panth"],
                  "poppy": ["poppy"],
                  "pyke": ["pyke", "paik"],
                  "qiyana": ["quiyana"],
                  "quinn": ["quinn"],
                  "rakan": ["rakan"],
                  "rammus": ["rammus"],
                  "reksai": ["reksai", "rek"],
                  "rell": ["rell"],
                  "renekton": ["renekton", "renek"],
                  "rengar": ["rengar"],
                  "riven": ["riven"],
                  "rumble": ["rumble"],
                  "ryze": ["ryze"],
                  "samira": ["samira"],
                  "sejuani": ["sejuani"],
                  "senna": ["senna"],
                  "seraphine": ["seraphine", "sera", "seraph"],
                  "sett": ["sett"],
                  "shaco": ["shaco"],
                  "shen": ["shen"],
                  "shyvana": ["shyvana", "shyvanna"],
                  "singed": ["singed"],
                  "sion": ["sion"],
                  "sivir": ["sivir"],
                  "skarner": ["skarner"],
                  "sona": ["sona"],
                  "soraka": ["soraka", "raka"],
                  "swain": ["swain"],
                  "sylas": ["sylas"],
                  "syndra": ["syndra"],
                  "tahmkench": ["tahmkench", "tahm", "kench"],
                  "taliyah": ["taliyah"],
                  "talon": ["talon"],
                  "taric": ["taric"],
                  "teemo": ["teemo"],
                  "thresh": ["thresh"],
                  "tristana": ["tristana", "trist"],
                  "trundle": ["trundle"],
                  "tryndamere": ["tryndamere", "trynd"],
                  "twistedfate": ["twistedfate", "tf"],
                  "twitch": ["twitch"],
                  "udyr": ["udyr"],
                  "urgot": ["urgot"],
                  "varus": ["varus"],
                  "vayne": ["vayne"],
                  "veigar": ["veigar", "veig", "vergas"],
                  "velkoz": ["velkoz", "vel"],
                  "vi": ["vi"],
                  "viego": ["viego"],
                  "viktor": ["viktor"],
                  "vladimir": ["vladimir", "vlad"],
                  "volibear": ["volibear", "voli"],
                  "warwick": ["warwick", "ww"],
                  "monkeyking": ["wukong"],
                  "xayah": ["xayah"],
                  "xerath": ["xerath"],
                  "xinzhao": ["xin", "xinzhao"],
                  "yasuo": ["yasuo"],
                  "yone": ["yone"],
                  "yorick": ["yorick"],
                  "yuumi": ["yuumi"],
                  "zac": ["zac"],
                  "zed": ["zed"],
                  "ziggs": ["ziggs"],
                  "zilean": ["zilean"],
                  "zoe": ["zoe"],
                  "zyra": ["zyra"]}


      def filename(x):
        arampath = '/root/aery/data/normal/'
        extension = '.txt'
        file = arampath + x + extension
        return file

      counter = 0

      for key, value in champions.items():
        if charsearch in value:
          counter += 1
          path = filename(key)
          if os.path.exists(path):
            with open(path, encoding="latin-1") as f:
              text = f.read()
              await ctx.channel.send(text)

              try:
                eventmsg = str(ctx.message.content) + ", guild: " + str(ctx.guild.name)
                await self.testchannel.send(eventmsg)
              except AttributeError:
                eventmsg = str(ctx.message.content) + ", guild: None"
                await self.testchannel.send(eventmsg)
        else:
          pass

      if counter == 0:
        await ctx.channel.send("¡No existe información para este champ! ¿Escribiste bien el nombre?")

  @Cog.listener()
  async def on_ready(self):
    if not self.bot.ready:
      self.bot.cogs_ready.ready_up("normal")

def setup(bot):
  bot.add_cog(Normal(bot))
