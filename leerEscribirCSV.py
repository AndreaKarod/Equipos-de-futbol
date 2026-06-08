import csv

equipos = []

def CalcularPuntos(equipo):
    puntos = equipo["ganados"] * 3 + equipo["empatados"] * 1
    return puntos

def LiderTabla(equipos):
    lider = None
    max_puntos = -1

    for equipo in equipos:
        puntos = CalcularPuntos(equipo)
        if puntos > max_puntos:
            max_puntos = puntos
            lider = equipo

    print(f"El líder del torneo es: {lider['equipo']} con {max_puntos} puntos.")
    print(f"Ganados: {lider['ganados']}, Empatados: {lider['empatados']}, Perdidos: {lider['perdidos']}, Goles a favor: {lider['goles_favor']}, Goles en contra: {lider['goles_contra']}, Diferencia de goles: {lider['diferencia_goles']}")

with open("input/equiposChampions.csv", "r") as archivo:
    lector = csv.DictReader(archivo)

    for fila in lector:
        print(fila)
        dictEquipos = {
            "equipo": fila["equipo"],
            "ganados": int(fila["ganados"]),
            "empatados": int(fila["empatados"]),
            "perdidos": int(fila["perdidos"]),
            "goles_favor": int(fila["goles_favor"]),
            "goles_contra": int(fila["goles_contra"]),
            "diferencia_goles": int(fila["goles_favor"]) - int(fila["goles_contra"])
        }
        equipos.append(dictEquipos)
equipos.sort(key=lambda x: CalcularPuntos(x), reverse=True)
with open("output/salidaChampions.csv", "w", newline="") as archivo:
    escritor = csv.writer(archivo)

    escritor.writerow(
        ["Posicion", " Equipo", " Ganados", " Empatados", " Perdidos", " Goles a favor", " Goles en contra", " Puntos", " Diferencia de goles"]
    )

    for posicion, equipo in enumerate(equipos, start=1):
        escritor.writerow(
            [posicion, equipo["equipo"], equipo["ganados"], equipo["empatados"], equipo["perdidos"], equipo["goles_favor"], equipo["goles_contra"], CalcularPuntos(equipo), equipo["diferencia_goles"]]
        )
    LiderTabla(equipos)
