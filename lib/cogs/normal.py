from discord.ext.commands import Cog
from discord.ext.commands import command
import os
import pendulum
import datetime
from datetime import datetime
from ..db import db

class Normal(Cog):
  def __init__(self, bot):
    self.bot = bot
    self.testchannel = self.bot.get_channel(827220123299086447)

  @command(name="normal")
  async def normal(self, ctx, *args):
    self.testchannel = self.bot.get_channel(827220123299086447)

    try:
        language = db.record("SELECT GuildLang FROM languages WHERE GuildID = ?", ctx.guild.id)

        language = str(language[0])

    except:
        language = "SP"

    if args == ():
        if language == "SP":
            await ctx.channel.send('¡Debes escribir el nombre de un champ después de *aery normal*!')
        else:
            await ctx.channel.send('Você deve escrever o nome de um champ após *aery normal*!')

    else:
      charsearch = "".join(args).lower().replace("'", "").replace(".", "")

      champions = {"aatrox": ["aatrox"],
                  "ahri": ["ahri"],
                  "akali": ["akali"],
                  "akalimiddle": ["akalimid"],
                  "akalitop": ["akalitop"],
                  "akshan": ["akshan"],
                  "akshanmiddle": ["akshanmid"],
                  "akshanadc": ["akshanadc"],
                  "alistar": ["alistar"],
                  "amumu": ["amumu"],
                  "anivia": ["anivia"],
                  "annie": ["annie"],
                  "aphelios": ["aphelios"],
                  "ashe": ["ashe"],
                  "aurelionsol": ["aurelion", "sol", "aurelionsol"],
                  "azir": ["azir"],
                  "bard": ["bard", "bardo"],
                  "belveth": ["belveth", "bel"],
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
                  "dianamiddle": ["dianamid"],
                  "dianajungle": ["dianajg"],
                  "drmundo": ["drmundo", "mundo"],
                  "drmundojungle": ["drmundojg", "mundojg"],
                  "drmundotop": ["mundotop", "drmundotop"],
                  "draven": ["draven"],
                  "ekko": ["ekko"],
                  "ekkojungle": ["ekkojg"],
                  "ekkomiddle": ["ekkomid"],
                  "elise": ["elise"],
                  "evelynn": ["evelynn", "eve"],
                  "ezreal": ["ez", "ezreal"],
                  "fiddlesticks": ["fiddlesticks", "fiddle"],
                  "fiora": ["fiora"],
                  "fizz": ["fizz"],
                  "galio": ["galio"],
                  "galiomiddle": ["galiomid"],
                  "gangplank": ["gangplank", "gang"],
                  "garen": ["garen"],
                  "gnar": ["gnar"],
                  "gragas": ["gragas"],
                  "gragasjungle": ["gragasjg"],
                  "gragastop": ["gragastop"],
                  "gragassupport": ["gragassupp"],
                  "graves": ["graves"],
                  "gwen": ["gwen"],
                  "hecarim": ["hecarim", "hec", "heca"],
                  "heimerdingermiddle": ["heimerdingermid", "heimmid", "heimermid"],
                  "heimerdingertop": ["heimerdingertop", "heimtop", "heimertop"],
                  "heimerdinger": ["heimerdinger", "heim", "heimer"],
                  "illaoi": ["illaoi"],
                  "irelia": ["irelia"],
                  "ireliatop": ["ireliatop"],
                  "ireliamiddle": ["ireliamid"],
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
                  "leesintop": ["leesintop", "leetop", "sintop"],
                  "leesinjungle": ["leesinjg", "leejg", "sinjg"],
                  "leona": ["leona"],
                  "lillia": ["lillia"],
                  "lissandra": ["liss", "lissandra"],
                  "lucian": ["lucian"],
                  "lucianadc": ["lucianadc"],
                  "lucianmiddle": ["lucianmiddle"],
                  "lulu": ["lulu"],
                  "lux": ["lux"],
                  "luxmiddle": ["luxmid"],
                  "luxsupport": ["luxsupp"],
                  "malphite": ["malphite", "malph"],
                  "malzahar": ["malzahar"],
                  "maokai": ["maokai"],
                  "maokaisupport": ["maokaisupp"],
                  "maokaitop": ["maokaitop"],
                  "masteryi": ["masteryi", "maestroyi", "yi"],
                  "missfortune": ["missfortune", "mf", "miss"],
                  "mordekaiser": ["mordekaiser", "morde"],
                  "morgana": ["morgana", "morg"],
                  "morganajungle": ["morganajg", "morgjg"],
                  "morganasupport": ["morganasupp", "morgsupp"],
                  "nami": ["nami"],
                  "nasus": ["nasus"],
                  "nautilus": ["nautilus", "nauti"],
                  "neeko": ["neeko"],
                  "neekomiddle": ["neekomid"],
                  "neekosupport": ["neekosupp"],
                  "nidalee": ["nidalee", "nida"],
                  "nocturne": ["nocturne", "noct"],
                  "nunu": ["nunu", "nunuywillump"],
                  "olaf": ["olaf"],
                  "orianna": ["orianna"],
                  "ornn": ["ornn"],
                  "pantheon": ["pantheon", "pant", "panth"],
                  "pantheonmiddle": ["pantheonmid", "pantmid", "panthmid"],
                  "pantheonsupport": ["pantheonsupp", "pantsupp", "panthsupp"],
                  "poppy": ["poppy"],
                  "poppyjungle": ["poppyjg"],
                  "poppytop": ["poppytop"],
                  "pyke": ["pyke", "paik"],
                  "qiyana": ["qiyana"],
                  "quinn": ["quinn"],
                  "rakan": ["rakan"],
                  "rammus": ["rammus"],
                  "reksai": ["reksai", "rek"],
                  "rell": ["rell"],
                  "renata": ["renata", "renataglasc"],
                  "renekton": ["renekton", "renek"],
                  "rengar": ["rengar"],
                  "rengarjungle": ["rengarjg"],
                  "rengartop": ["rengartop"],
                  "riven": ["riven"],
                  "rumble": ["rumble"],
                  "rumblejungle": ["rumblejg"],
                  "rumblemiddle": ["rumblemid"],
                  "rumbletop": ["rumbletop"],
                  "ryze": ["ryze"],
                  "ryzemiddle": ["ryzemid"],
                  "ryzetop": ["ryzetop"],
                  "samira": ["samira"],
                  "sejuani": ["sejuani"],
                  "senna": ["senna"],
                  "seraphine": ["seraphine", "sera", "seraph"],
                  "sett": ["sett"],
                  "setttop": ["setttop"],
                  "settsupport": ["settsupp"],
                  "shaco": ["shaco"],
                  "shacojungle": ["shacojg"],
                  "shacosupport": ["shacosupport"],
                  "shen": ["shen"],
                  "shyvana": ["shyvana", "shyvanna"],
                  "singed": ["singed"],
                  "sion": ["sion"],
                  "sivir": ["sivir"],
                  "skarner": ["skarner"],
                  "sona": ["sona"],
                  "soraka": ["soraka", "raka"],
                  "swain": ["swain"],
                  "swainadc": ["swainadc"],
                  "swainsupport": ["swainsupp"],
                  "sylas": ["sylas"],
                  "sylasmiddle": ["sylasmid"],
                  "sylastop": ["sylastop"],
                  "syndra": ["syndra"],
                  "tahmkench": ["tahmkench", "tahm", "kench"],
                  "tahmkenchadc": ["tahmkenchadc", "tahmadc", "kenchadc"],
                  "tahmkenchtop": ["tahmkenchtop", "tahmtop", "kenchtop"],
                  "tahmkenchsupport": ["tahmkenchsupp", "tahmsupp", "kenchsupp"],
                  "taliyah": ["taliyah"],
                  "talon": ["talon"],
                  "taric": ["taric"],
                  "teemo": ["teemo"],
                  "thresh": ["thresh"],
                  "tristana": ["tristana", "trist"],
                  "trundle": ["trundle"],
                  "trundlejungle": ["trundlejg"],
                  "trundletop": ["trundletop"],
                  "tryndamere": ["tryndamere", "trynd"],
                  "twistedfate": ["twistedfate", "tf"],
                  "twitch": ["twitch"],
                  "udyr": ["udyr"],
                  "urgot": ["urgot"],
                  "varus": ["varus"],
                  "vayne": ["vayne"],
                  "veigar": ["veigar", "veig", "vergas"],
                  "velkoz": ["velkoz", "vel"],
                  "velkozmiddle": ["velkozmid", "velmid"],
                  "velkozsupport": ["velkozsupp", "velsupp"],
                  "vex": ["vex"],
                  "vi": ["vi"],
                  "viego": ["viego"],
                  "viegojungle": ["viegojg"],
                  "viegomiddle": ["viegomid"],
                  "viktor": ["viktor"],
                  "vladimir": ["vladimir", "vlad"],
                  "vladimirmiddle": ["vladimirmid", "vladmid"],
                  "vladimirtop": ["vladimirtop", "vladtop"],
                  "volibear": ["volibear", "voli"],
                  "volibearjungle": ["volibearjg", "volijg"],
                  "volibeartop": ["volibeartop", "volitop"],
                  "warwick": ["warwick", "ww"],
                  "warwickjungle": ["warwickjg", "wwjg"],
                  "warwicktop": ["warwicktop", "wwtop"],
                  "monkeyking": ["wukong"],
                  "xayah": ["xayah"],
                  "xerath": ["xerath"],
                  "xerathsupport": ["xerathsupp"],
                  "xerathmiddle": ["xerathmid"],
                  "xinzhao": ["xin", "xinzhao"],
                  "yasuo": ["yasuo"],
                  "yone": ["yone"],
                  "yorick": ["yorick"],
                  "yuumi": ["yuumi"],
                  "zac": ["zac"],
                  "zed": ["zed"],
                  "zeri": ["zeri"],
                  "ziggs": ["ziggs"],
                  "ziggsmiddle": ["ziggsmid"],
                  "ziggsadc": ["ziggsadc"],
                  "zilean": ["zilean"],
                  "zoe": ["zoe"],
                  "zyra": ["zyra"]}


      def filename(x):
        if language == "SP":
            arampath = '/root/aery/data/normal/sp/'
            extension = '.txt'
            file = arampath + x + extension
            return file

        else:
            arampath = '/root/aery/data/normal/pt/'
            extension = '.txt'
            file = arampath + x + extension
            return file

      counter = 0

      for key, value in champions.items():
        if charsearch in value:
          counter += 1
          path = filename(key)
          if os.path.exists(path):
            with open(path, encoding="utf-8") as f:
              text = f.read()
              await ctx.channel.send(text)
          if language == 'SP':
              await ctx.channel.send("**ÚLTIMO AVISO**: El 31 de julio, Aerybot perderá sus permisos actuales y podría dejar de funcionar, debes expulsar y reinvitarla a tu servidor para mantener funcionalidad.\nSi invitaste al bot después del 1 de julio, puedes ignorar este mensaje.\nLink para reinvitar: https://discord.com/api/oauth2/authorize?client_id=804475973579833374&permissions=8&scope=bot%20applications.commands")
          else:
              await ctx.channel.send("**FINAL NOTICE**: **AVISO FINAL**: em 31 de julho, o Aerybot perderá suas permissões atuais e poderá parar de funcionar, você deve despejar e convidar novamente seu servidor para manter a funcionalidade.\nSe você convidou o bot após 1º de julho, ignore esta mensagem. \nLink para convidar novamente: https://discord.com/api/oauth2/authorize?client_id=804475973579833374&permissions=8&scope=bot%20applications.commands")

          try:
              eventmsg = str(ctx.message.content) + ", guild: " + str(ctx.guild.name)
              await self.testchannel.send(eventmsg)

          except AttributeError:
              eventmsg = str(ctx.message.content) + ", guild: None"
              await self.testchannel.send(eventmsg)

        else:
          pass

      if counter == 0:
          if language == "SP":
              await ctx.channel.send("¡No existe información para este champ! ¿Escribiste bien el nombre?")
          else:
              await ctx.channel.send("Não há informações para esse champ. Você soletrou o nome corretamente?")

  @Cog.listener()
  async def on_ready(self):
    if not self.bot.ready:
      self.bot.cogs_ready.ready_up("normal")

def setup(bot):
  bot.add_cog(Normal(bot))
