import os

ParaReemplazar = ['Carcaj del mediodía', 'Guardián invisible', 'Daga de hechicero', 'Espada de granizo', 'Cuchillo de ascuas', 'Recaudadora', 'Sombrero mortal de Rabadon', 'Viento huracanado', 'Ángel de la guarda', 'Filo infinito', 'Recordatorio letal', 'Grebas del berseker', 'Botas blindadas', 'Botas de hechicero', 'Látigo puntahierro', 'Chupasangre', 'Calibrador de Sterak', 'Rostro espiritual', 'Mecanoespada punki', 'Fuerza de trinidad', 'Perdición del liche', 'Bastón del Vacío', 'Medallón de los Solari de Hierro', 'Promesa de caballero', 'Capa solar', 'Malla de espinas', 'Protector pétreo de gárgola', 'Desconsuelo de Liandry', 'Bastón del arcángel', 'Incensario ardiente', 'Bastón de aguas fluidas', 'Gema avivadora', 'Desgarrador divino', 'Baile de la muerte', 'Daga dentada', 'Final del ingenio', 'Velo del hada de la muerte', 'Cuchilla negra', 'Rescoldo de Bami', 'Creagrietas', 'Verdugo de krakens', 'Lapa maliciosa', 'Segador de esencia']

ReemplazarPor = ['Carcaj de mediodía', 'Centinela invisible', 'Filo del Robahechizos', 'Hoja granizo', 'Cuchillo Ámbar', 'El Coleccionista', 'Sombrero mortífero de Rabadon', 'Fuerza del Viento', 'Ángel Guardián', 'Filo del infinito', 'Recordatorio mortal', 'Grebas de berserker', 'Punteras de acero revestidas', 'Botas del hechicero', 'Látigo férreo', 'Bebedor de sangre', 'Guantelete de Sterak', 'Apariencia espiritual', 'Sierraespada Quimopunk', 'Fuerza de la trinidad', 'Maldición del liche', 'Báculo del vacío', 'Relicario de los Solari de Hierro', 'Promesa del caballero', 'Égida de fuego solar', 'Cota de espinas', 'Armadura pétrea', 'Angustia de Liandry', 'Báculo del arcángel', 'Pebetero ardiente', 'Báculo de agua fluyente', 'Gemaluz', 'Cercenador divino', 'Danza de la muerte', 'Puñal serrado', 'Al filo de la Cordura', 'Velo de la banshee', 'Cuchilla oscura', 'Ceniza de Bami', 'Agrietador', 'Matakrakens', 'Mirada absorbente', 'Saqueador de esencias']

for champ in os.listdir('.'):
  if champ == "reemplazar.py" or champ == "aram.py" or champ == "normal.py":
    pass 
  else: 
    print(champ)
    original = open(champ, 'r')
    reemplazo = original.read()
    for i in range(len(ParaReemplazar)):
      reemplazo = reemplazo.replace(ParaReemplazar[i], ReemplazarPor[i])
    original.close()
    original = open(champ, 'w')
    original.write(reemplazo)
    original.truncate()
    original.close()