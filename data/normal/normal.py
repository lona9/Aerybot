import os
from bs4 import BeautifulSoup

#first bulk [6:10]
fix1 = ['khazix', 'kaisa', 'viego', 'viktor'] #[9:13]
fix2 = ['aurelionsol', 'ekko', 'fizz', 'gangplank', 'jax', 'illaoi', 'irelia', 'leblanc', 'kayle', 'malphite', 'poppy', 'pantheon', 'singed', 'sion', 'twistedfate', 'yorick', 'zoe'] #[5:9]

filestofix = []

for champ in fix2:
    filename = champ + '.txt'
    filestofix.append(filename)

for champ in filestofix:
# for champ in os.listdir('files'):
  with open(os.path.join('files', champ)) as file:
    print(champ, 'iniciando')
    soup = BeautifulSoup(file, features='html5lib')

    ## NOMBRE
    nombre = soup.find('meta', attrs={'name': "twitter:title"})
    nombre = str(nombre).replace('<meta content="Builds de ', '').replace(' - Objetos / Runas / Emparejamientos - League of Legends" name="twitter:title"/>', '')

    ## POSICIÓN
    posicion = soup.find('div', 'bannerSubtitle').contents
    posicion = "".join(posicion)
    posicion = posicion.strip()

    ## PORCENTAJE DE VICTORIAS
    victorias = soup.find('div', "pie-chart small", id="graphDD2").contents[0]
    victorias = "".join(victorias).strip()

    ## HECHIZOS DEL INVOCADOR
    hechizos = []
    hechinv = soup.find_all('div', "iconsRow")[-1]
    hechizos1  = hechinv.find_all('img', alt=True)[-2]
    hechizos2 = hechinv.find_all('img', alt=True)[-1]
    alt1 = str(hechizos1.get('alt'))
    alt2 = str(hechizos2.get('alt'))
    hechizos.append(alt1)
    hechizos.append(alt2)
    if 'Destello' == hechizos[0]:
      hechizo1 = '<:Flash:804555481443336202>'
    elif 'Teleportar' == hechizos[0]:
      hechizo1 = '<:Teleport:804555481699713034>'
    elif 'Aplastar' == hechizos[0]:
      hechizo1 = '<:Smite:804555481494061086>'
    elif 'Marca' == hechizos[0]:
      hechizo1 = '<:Mark:804555480965709835>'
    elif 'Prender' == hechizos[0]:
      hechizo1 = '<:Ignite:804555481167298570>'
    elif 'Curar' == hechizos[0]:
      hechizo1 = '<:Heal:804555480819040336>'
    elif 'Fantasmal' == hechizos[0]:
      hechizo1 = '<:Ghost:804555480856002610>'
    elif 'Claridad' == hechizos[0]:
      hechizo1 = '<:Clarity:804555481489080370>'
    elif 'Limpiar' == hechizos[0]:
      hechizo1 = '<:Cleanse:804555480730304514>'
    elif 'Extenuación' == hechizos[0]:
      hechizo1 = '<:Exhaust:804555480843288586>'

    if 'Destello' == hechizos[1]:
      hechizo2 = '<:Flash:804555481443336202>'
    elif 'Teleportar' == hechizos[1]:
      hechizo2 = '<:Teleport:804555481699713034>'
    elif 'Aplastar' == hechizos[1]:
      hechizo2 = '<:Smite:804555481494061086>'
    elif 'Marca' == hechizos[1]:
      hechizo2 = '<:Mark:804555480965709835>'
    elif 'Prender' == hechizos[1]:
      hechizo2 = '<:Ignite:804555481167298570>'
    elif 'Curar' == hechizos[1]:
      hechizo2 = '<:Heal:804555480819040336>'
    elif 'Fantasmal' == hechizos[1]:
      hechizo2 = '<:Ghost:804555480856002610>'
    elif 'Claridad' == hechizos[1]:
      hechizo2 = '<:Clarity:804555481489080370>'
    elif 'Limpiar' == hechizos[1]:
      hechizo2 = '<:Cleanse:804555480730304514>'
    elif 'Extenuación' == hechizos[1]:
      hechizo2 = '<:Exhaust:804555480843288586>'


    ## RUNAS PRINCIPALES
    opaqueprrunes = soup.find('table', "perksTableOverview").find_all('div', attrs={'style': "opacity: 0.2;"})
    runasprincipales = []
    for runa in range(len(opaqueprrunes)):
      primagenes = opaqueprrunes[runa].find('img', alt=True)
      alts = primagenes.get('alt')
      runasprincipales.append(alts)

    # DOMINACION
    if 'Electrocutar' in runasprincipales or 'Depredador' in runasprincipales or 'Cosecha oscura' in runasprincipales or 'Luvia de cuchillas' in runasprincipales:
      runa1 = '<:dom:804451124085522442>'

      #LINEA 1
      if 'Electrocutar' not in runasprincipales:
        linea1pr = ' <:dom11:804447179758239744>:cd::cd::cd:'
      elif 'Depredador' not in runasprincipales:
        linea1pr = ' :cd:<:dom12:804447180362219551>:cd::cd:'
      elif 'Cosecha oscura' not in runasprincipales:
        linea1pr = ' :cd::cd:<:dom13:804447179828625438>:cd:'
      elif 'Lluvia de cuchillas' not in runasprincipales:
        linea1pr = ' :cd::cd::cd:<:dom14:804447179938070569>'

      #LINEA 2
      if 'Golpe bajo' not in runasprincipales:
        linea2pr = '   <:dom21:804457127800078397>:cd::cd:'
      elif 'Sabor a sangre' not in runasprincipales:
        linea2pr = '   :cd:<:dom22:804457129394176020>:cd:'
      elif 'Impacto repentino' not in runasprincipales:
        linea2pr = '   :cd::cd:<:dom23:804457130307485707>'

      #LINEA 3
      if 'Guardián zombi' not in runasprincipales:
        linea3pr = '   <:dom31:804457128914976788>:cd::cd:'
      elif 'Poro fantasmal' not in runasprincipales:
        linea3pr = '   :cd:<:dom32:804457128600272916>:cd:'
      elif 'Colección de globos oculares' not in runasprincipales:
        linea3pr = '   :cd::cd:<:dom33:804457129578332160>'

      #LINEA 4
      if 'Cazador voraz' not in runasprincipales:
        linea4pr = ' <:dom41:804457130379182120>:cd::cd::cd:'
      elif 'Cazador ingenioso' not in runasprincipales:
        linea4pr = ' :cd:<:dom42:804457129980461107>:cd::cd:'
      elif 'Cazador incesante' not in runasprincipales:
        linea4pr = ' :cd::cd:<:dom43:804457129183936582>:cd:'
      elif 'Cazador definitivo' not in runasprincipales:
        linea4pr = ' :cd::cd::cd:<:dom44:804457129732866048>'

    #PRECISION
    elif 'Ataque intensificado' in runasprincipales or 'Compás letal' in runasprincipales or 'Pies veloces' in runasprincipales or 'Conquistador' in runasprincipales:
      runa1 = '<:pres:804451123825606657>'

      #LINEA 1
      if 'Ataque intensificado' not in runasprincipales:
        linea1pr = ' <:precision11:804445926906658886>:cd::cd::cd:'
      elif 'Compás letal' not in runasprincipales:
        linea1pr = ' :cd:<:precision12:804446921522675733>:cd::cd:'
      elif 'Pieces veloces' not in runasprincipales:
        linea1pr = ' :cd::cd:<:precision13:804446921619931187>:cd:'
      elif 'Conquistador' not in runasprincipales:
        linea1pr = ' :cd::cd::cd:<:precision14:804446921631596585>'

      #LINEA 2
      if 'Supercuración' not in runasprincipales:
        linea2pr = '   <:precision21:804446921363685387>:cd::cd:'
      elif 'Triunfo' not in runasprincipales:
        linea2pr = '   :cd:<:precision22:804446921414541333>:cd:'
      elif 'Claridad mental' not in runasprincipales:
        linea2pr = '   :cd::cd:<:precision23:804446921628057630>'

      #LINEA 3
      if 'Leyenda: Presteza' not in runasprincipales:
        linea3pr = '   <:precision31:804446921660956702>:cd::cd:'
      elif 'Leyenda: Tenacidad' not in runasprincipales:
        linea3pr = '   :cd:<:precision32:804446921737371648>:cd:'
      elif 'Leyenda: Linaje' not in runasprincipales:
        linea3pr = '   :cd::cd:<:precision33:804446921644179516>'

      #LINEA 4
      if 'Golpe de gracia' not in runasprincipales:
        linea4pr = '   <:precision41:804446922151690300>:cd::cd:'
      elif 'Derribado' not in runasprincipales:
        linea4pr = '   :cd:<:precision42:804446921636053043>:cd:'
      elif 'Último esfuerzo' not in runasprincipales:
        linea4pr = '   :cd::cd:<:precision43:804446921941975080>'

    # VALOR
    elif 'Garras del inmortal' in runasprincipales or 'Reverberración' in runasprincipales or 'Protector' in runasprincipales:
      runa1 = '<:valor:804451124245561394>'
      #LINEA 1
      if 'Garras del inmortal' not in runasprincipales:
        linea1pr = '   <:valor11:804449943376232509>:cd::cd:'
      elif 'Reverberacción' not in runasprincipales:
        linea1pr = '   :cd:<:valor12:804449943775084614>:cd:'
      elif 'Protector' not in runasprincipales:
        linea1pr = '   :cd::cd:<:valor13:804449943497605171>'

      #LINEA 2
      if 'Demoler' not in runasprincipales:
        linea2pr = '   <:valor21:804449943984537690>:cd::cd:'
      elif 'Fuente de vida' not in runasprincipales: 
        linea2pr = '   :cd:<:valor22:804449944018223104>:cd:'
      elif 'Golpe de escudo' not in runasprincipales:
        linea2pr = '   :cd::cd:<:valor23:804449943876010024>'
      
      #LINEA 3
      if 'Condicionamiento' not in runasprincipales:
        linea3pr = '   <:valor31:804449943666425907>:cd::cd:'
      elif 'Fuerzas renovadas' not in runasprincipales:
        linea3pr = '   :cd:<:valor32:804449943959765002>:cd:'
      elif 'Revestimiento de huesos' not in runasprincipales:
        linea3pr = '   :cd::cd:<:valor33:804449943603118131>'
      
      #LINEA 4
      if 'Sobrecrecimiento' not in runasprincipales:
        linea4pr = '   <:valor41:804449944298586143>:cd::cd:'
      elif 'Revitalizar' not in runasprincipales:
        linea4pr = '   :cd:<:valor42:804449943615438919>:cd:'
      elif 'Inquebrantable' not in runasprincipales:
        linea4pr = '   :cd::cd:<:valor43:804449944001708043>'

    #BRUJERIA
    elif 'Invocar a Aery' in runasprincipales or 'Cometa arcano' in runasprincipales or 'Irrupción de fase' in runasprincipales:
      runa1 = '<:bruj:804451124236648478>'

      #LINEA 1
      if 'Invocar a Aery' not in runasprincipales:
        linea1pr = '   <:bruj11:804448796104589323>:cd::cd:'
      elif 'Cometa arcano' not in runasprincipales:
        linea1pr = '   :cd:<:bruj12:804448797001252864>:cd:'
      elif 'Irrupción de fase' not in runasprincipales:
        linea1pr = '   :cd::cd:<:bruj13:804448796787474433>'

      #LINEA 2
      if 'Orbe anulador' not in runasprincipales:
        linea2pr = '   <:bruj21:804448796972023829>:cd::cd:'
      elif 'Banda de maná' not in runasprincipales:
        linea2pr = '   :cd:<:bruj22:804448796553117707>:cd:'
      elif 'Capa del nimbo' not in runasprincipales:
        linea2pr = '   :cd::cd:<:bruj23:804448797425532928>'

      #LINEA 3
      if 'Trascendencia' not in runasprincipales:
        linea3pr = '   <:bruj31:804448797395910716>:cd::cd:'
      elif 'Celeridad' not in runasprincipales:
        linea3pr = '   :cd:<:bruj32:804448797346234369>:cd:'
      elif 'Concentración absoluta' not in runasprincipales:
        linea3pr = '   :cd::cd:<:bruj33:804448797509419098>'

      #LINEA 4
      if 'Piroláser' not in runasprincipales:
        linea4pr = '   <:bruj41:804448797597499402>:cd::cd:'
      elif 'Caminar sobre agua' not in runasprincipales:
        linea4pr = '   :cd:<:bruj42:804448797572595813>:cd:'
      elif 'Se avecina tormenta' not in runasprincipales:
        linea4pr = '   :cd::cd:<:bruj43:804448797631316069>'

    #PRECISION
    elif 'Mejora glacial' in runasprincipales or 'Libro de hechizos' in runasprincipales or 'Prototipo: Versatilidad' in runasprincipales:
      runa1 = '<:insp:804451124207681577>'

      #LINEA 1
      if 'Mejora glacial' not in runasprincipales:
        linea1pr = '   <:insp11:804450563936223283>:cd::cd:'
      elif 'Libro de hechizos' not in runasprincipales:
        linea1pr = '   :cd:<:insp12:804450563680501801>:cd:'
      elif 'Prototipo: Versatilidad' not in runasprincipales:
        linea1pr = '   :cd::cd:<:insp13:804450563856531547>'

      #LINEA 2
      if 'Destello hextech' not in runasprincipales:
        linea2pr = '   <:insp21:804450563911057458>:cd::cd:'
      elif 'Calzado mágico' not in runasprincipales:
        linea2pr = '   :cd:<:insp22:804450563793747989>:cd:'
      if 'Momento oportuno' not in runasprincipales:
        linea2pr = '   :cd::cd:<:insp23:804450563948675112>'

      #LINEA 3
      if 'Mercado del futuro' not in runasprincipales:
        linea3pr = '   <:insp31:804450564188536842>:cd::cd:'
      elif 'Desmaterializador de súbditos' not in runasprincipales:
        linea3pr = '   :cd:<:insp32:804450563915645008>:cd:'
      elif 'Entrega de galletas' not in runasprincipales:
        linea3pr = '   :cd::cd:<:insp33:804450564049731594>'

      #LINEA 4
      if 'Perspicacia cósmica' not in runasprincipales:
        linea4pr = '   <:insp41:804450563507879947>:cd::cd:'
      elif 'Velocidad de acercamiento' not in runasprincipales:
        linea4pr = '   :cd:<:insp42:804450563965452369>:cd:'
      elif 'Tónico de distorsión temporal' not in runasprincipales:
        linea4pr = '   :cd::cd:<:insp43:804450563952869452>'
        
    ## RUNAS SECUNDARIAS
    opaquesecrunes = soup.find('table', "perksTableOverview secondary").find_all('div', attrs={'style': "opacity: 0.2;"})
    runassecundarias = []
    for runa in range(len(opaquesecrunes)):
      secimagenes = opaquesecrunes[runa].find('img', alt=True)
      alts = secimagenes.get('alt')
      runassecundarias.append(alts)

    #DOMINACION
    if 'Golpe bajo' in runassecundarias or 'Sabor a sangre' in runassecundarias or 'Impacto repentino' in runassecundarias or 'Guardián zombi' in runassecundarias or 'Poro fantasmal' in runassecundarias or 'Impacto repentino' in runassecundarias:
      runa2 = '<:dom:804451124085522442>'

      #LINEA 2
      if 'Golpe bajo' not in runassecundarias:
        linea2sec = '   <:dom21:804457127800078397>:cd::cd:'
      elif 'Sabor a sangre' not in runassecundarias:
        linea2sec = '   :cd:<:dom22:804457129394176020>:cd:'
      elif 'Impacto repentino' not in runassecundarias:
        linea2sec = '   :cd::cd:<:dom23:804457130307485707>'
      else:
        linea2sec = '   :cd::cd::cd:'

      #LINEA 3
      if 'Guardián zombi' not in runassecundarias:
        linea3sec = '   <:dom31:804457128914976788>:cd::cd:'
      elif 'Poro fantasmal' not in runassecundarias:
        linea3sec = '   :cd:<:dom32:804457128600272916>:cd:'
      elif 'Colección de globos oculares' not in runassecundarias:
        linea3sec = '   :cd::cd:<:dom33:804457129578332160>'
      else:
        linea3sec = '   :cd::cd::cd:'

      #LINEA 4
      if 'Cazador voraz' not in runassecundarias:
        linea4sec = ' <:dom41:804457130379182120>:cd::cd::cd:'
      elif 'Cazador ingenioso' not in runassecundarias:
        linea4sec = ' :cd:<:dom42:804457129980461107>:cd::cd:'
      elif 'Cazador incesante' not in runassecundarias:
        linea4sec = ' :cd::cd:<:dom43:804457129183936582>:cd:'
      elif 'Cazador definitivo' not in runassecundarias:
        linea4sec = ' :cd::cd::cd:<:dom44:804457129732866048>'
      else:
        linea3sec = ' :cd::cd::cd::cd:'

    #PRECISION
    elif 'Supercuración' in runassecundarias or 'Triunfo' in runassecundarias or 'Claridad mental' in runassecundarias or 'Leyenda: Presteza' in runassecundarias or 'Leyenda: Tenacidad' in runassecundarias or 'Leyenda: Linaje' in runassecundarias:
      runa2 = '<:pres:804451123825606657>'

      #LINEA 2
      if 'Supercuración' not in runassecundarias:
        linea2sec = '   <:precision21:804446921363685387>:cd::cd:'
      elif 'Triunfo' not in runassecundarias:
        linea2sec = '   :cd:<:precision22:804446921414541333>:cd:'
      elif 'Claridad mental' not in runassecundarias:
        linea2sec = '   :cd::cd:<:precision23:804446921628057630>'
      else:
        linea2sec = '   :cd::cd::cd:'

      #LINEA 3
      if 'Leyenda: Presteza' not in runassecundarias:
        linea3sec = '   <:precision31:804446921660956702>:cd::cd:'
      elif 'Leyenda: Tenacidad' not in runassecundarias:
        linea3sec = '   :cd:<:precision32:804446921737371648>:cd:'
      elif 'Leyenda: Linaje' not in runassecundarias:
        linea3sec = '   :cd::cd:<:precision33:804446921644179516>'
      else:
        linea3sec = '   :cd::cd::cd:'

      #LINEA 4
      if 'Golpe de gracia' not in runassecundarias:
        linea4sec = '   <:precision41:804446922151690300>:cd::cd:'
      elif 'Derribado' not in runassecundarias:
        linea4sec = '   :cd:<:precision42:804446921636053043>:cd:'
      elif 'Último esfuerzo' not in runassecundarias:
        linea4sec = '   :cd::cd:<:precision43:804446921941975080>'
      else:
        linea4sec = '   :cd::cd::cd:'

    #VALOR
    elif 'Demoler' in runassecundarias or 'Fuente de vida' in runassecundarias or 'Golpe de escudo' in runassecundarias or 'Condicionamiento' in runassecundarias or 'Fuerzas renovadas' in runassecundarias or 'Revestimiento de huesos' in runassecundarias:
      runa2 = '<:valor:804451124245561394>'

      #LINEA 2
      if 'Demoler' not in runassecundarias:
        linea2sec = '   <:valor21:804449943984537690>:cd::cd:'
      elif 'Fuente de vida' not in runassecundarias: 
        linea2sec = '   :cd:<:valor22:804449944018223104>:cd:'
      elif 'Golpe de escudo' not in runassecundarias:
        linea2sec = '   :cd::cd:<:valor23:804449943876010024>'
      else:
        linea2sec = '   :cd::cd::cd:'
      
      #LINEA 3
      if 'Condicionamiento' not in runassecundarias:
        linea3sec = '   <:valor31:804449943666425907>:cd::cd:'
      elif 'Fuerzas renovadas' not in runassecundarias:
        linea3sec = '   :cd:<:valor32:804449943959765002>:cd:'
      elif 'Revestimiento de huesos' not in runassecundarias:
        linea3sec = '   :cd::cd:<:valor33:804449943603118131>'
      else:
        linea3sec = '   :cd::cd::cd:'
      
      #LINEA 4
      if 'Sobrecrecimiento' not in runassecundarias:
        linea4sec = '   <:valor41:804449944298586143>:cd::cd:'
      elif 'Revitalizar' not in runassecundarias:
        linea4sec = '   :cd:<:valor42:804449943615438919>:cd:'
      elif 'Inquebrantable' not in runassecundarias:
        linea4sec = '   :cd::cd:<:valor43:804449944001708043>'
      else:
        linea4sec = '   :cd::cd::cd:'

    #BRUJERIA
    elif 'Orbe anulador' in runassecundarias or 'Banda de maná' in runassecundarias or 'Capa del nimbo' in runassecundarias or 'Trascendencia' in runassecundarias or 'Celeridad' in runassecundarias or 'Concentración absoluta' in runassecundarias:
      runa2 = '<:bruj:804451124236648478>'

      #LINEA 2
      if 'Orbe anulador' not in runassecundarias:
        linea2sec = '   <:bruj21:804448796972023829>:cd::cd:'
      elif 'Banda de maná' not in runassecundarias:
        linea2sec = '   :cd:<:bruj22:804448796553117707>:cd:'
      elif 'Capa del nimbo' not in runassecundarias:
        linea2sec = '   :cd::cd:<:bruj23:804448797425532928>'
      else:
        linea2sec = '   :cd::cd::cd:'

      #LINEA 3
      if 'Trascendencia' not in runassecundarias:
        linea3sec = '   <:bruj31:804448797395910716>:cd::cd:'
      elif 'Celeridad' not in runassecundarias:
        linea3sec = '   :cd:<:bruj32:804448797346234369>:cd:'
      elif 'Concentración absoluta' not in runassecundarias:
        linea3sec = '   :cd::cd:<:bruj33:804448797509419098>'
      else:
        linea3sec = '   :cd::cd::cd:'

      #LINEA 4
      if 'Piroláser' not in runassecundarias:
        linea4sec = '   <:bruj41:804448797597499402>:cd::cd:'
      elif 'Caminar sobre agua' not in runassecundarias:
        linea4sec = '   :cd:<:bruj42:804448797572595813>:cd:'
      elif 'Se avecina tormenta' not in runassecundarias:
        linea4sec = '   :cd::cd:<:bruj43:804448797631316069>'
      else:
        linea4sec = '   :cd::cd::cd:'

    #INSPIRACION
    elif 'Destello hextech' in runassecundarias or 'Calzado mágico' in runassecundarias or 'Momento oportuno' in runassecundarias or 'Mercado del futuro' in runassecundarias or 'Desmaterializador de súbditos' in runassecundarias or 'Entrega de galletas' in runassecundarias:
      runa2 = '<:insp:804451124207681577>'

      #LINEA 2
      if 'Destello hextech' not in runassecundarias:
        linea2sec = '   <:insp21:804450563911057458>:cd::cd:'
      elif 'Calzado mágico' not in runassecundarias:
        linea2sec = '   :cd:<:insp22:804450563793747989>:cd:'
      elif 'Momento oportuno' not in runassecundarias:
        linea2sec = '   :cd::cd:<:insp23:804450563948675112>'
      else:
        linea2sec = '   :cd::cd::cd:'

      #LINEA 3
      if 'Mercado del futuro' not in runassecundarias:
        linea3sec = '   <:insp31:804450564188536842>:cd::cd:'
      elif 'Desmaterializador de súbditos' not in runassecundarias:
        linea3sec = '   :cd:<:insp32:804450563915645008>:cd:'
      elif 'Entrega de galletas' not in runassecundarias:
        linea3sec = '   :cd::cd:<:insp33:804450564049731594>'
      else:
        linea3sec = '   :cd::cd::cd:'

      #LINEA 4
      if 'Perspicacia cósmica' not in runassecundarias:
        linea4sec = '   <:insp41:804450563507879947>:cd::cd:'
      elif 'Velocidad de acercamiento' not in runassecundarias:
        linea4sec = '   :cd:<:insp42:804450563965452369>:cd:'
      elif 'Tónico de distorsión temporal' not in runassecundarias:
        linea4sec = '   :cd::cd:<:insp43:804450563952869452>'
      else:
        linea4sec = '   :cd::cd::cd:'

    #FRAGMENTOS
    fragmentos = runassecundarias[-6:]
    if '+9 de fuerza adaptable' not in fragmentos[:2]:
      fragmento1 = '<:5008:804451180172279808>'
    elif '+10% de velocidad de ataque' not in fragmentos[:2]:
      fragmento1 = '<:5005:804451179778015303>'
    elif '+8 de velocidad de habilidades ' not in fragmentos[:2]:
      fragmento1= '<:5007:804451180164022312>'

    if '+9 de fuerza adaptable' not in fragmentos[2:4]:
      fragmento2 = '<:5008:804451180172279808>'
    elif '+6 armadura' not in fragmentos[2:4]:
      fragmento2 = '<:5002:804451180104908870>'
    elif '+8 de resistencia mágica' not in fragmentos[2:4]:
      fragmento2 = '<:5003:804451180100452403>'

    if '+15-90 de vida (según el nivel)' not in fragmentos[-2:]:
      fragmento3 = '<:5001:804451180112642088>'
    if '+6 armadura' not in fragmentos[-2:]:
      fragmento3 = '<:5002:804451180104908870>'
    if '+8 de resistencia mágica' not in fragmentos[-2:]:
      fragmento3 = '<:5003:804451180100452403>'

    ## OBJETOS INICIALES Y FINALES
    objetos = soup.find_all('div', "championSpell small-margin")
    objinfin = []
    for obj in range(len(objetos)):
      imginfin = objetos[obj].find('img', alt=True)
      alts = imginfin.get('alt')
      objinfin.append(alts)
    x = len(objinfin) - 3
    objin = objinfin[:x]
    objin = ", ".join(objin)
    objfin = objinfin[-3:]
    objfin = ", ".join(objfin)

    ## BOTAS
    botas = soup.find_all('div', "championSpell")
    imgbotas = botas[9].find('img', alt=True)
    botas = imgbotas.get('alt')

    ### OBJETOS PRINCIPALES
    principales = soup.find_all('div', "championSpell")
    objs = []
    for obj in range(len(principales)):
      imgprincipales = principales[obj].find('img', alt=True)
      principalts = imgprincipales.get('alt')
      objs.append(principalts)
    objpr = objs[5:9]
    objpr = " > ".join(objpr)

    texto = ("**{}** *(Normal)*\n**Posición:** *{}*\n**Porcentaje de victorias:** {}\n**Hechizos del Invocador:** {} {}\n**Runas:** {} {}\n\n>{}\n>{}\n>{}\n>{}\n\n>{}\n>{}\n>{}\n>   {} {} {}\n\n**Build**\n**Botas:** {}\n**Objetos iniciales:** {}\n**Objetos principales:** {}\n**Objetos finales:** {}".format(nombre, posicion, victorias, hechizo1, hechizo2, runa1, runa2, linea1pr, linea2pr, linea3pr, linea4pr, linea2sec, linea3sec, linea4sec, fragmento1, fragmento2, fragmento3, botas, objin, objpr, objfin))

    f = open(champ, 'w+')
    f.write(texto)
    f.close()
    print(champ, 'terminado')