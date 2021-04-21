def direcao_categorica(direcao_em_graus):
    direcoes = ("N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW")
    indice = int(direcao_em_graus // 22.5)
    resto = direcao_em_graus % 22.5
    if resto > 11.25:
        indice += 1
    if indice == 16:
        indice = 0
    return direcoes[indice]

def velocidade_categorica(velocidade_kmh):
    velocidades = ('0-5 km/h', '5-10 km/h', '10-15 km/h', '15-20 km/h', '20-25 km/h', '25-30 km/h', '30-35 km/h', '35-40 km/h','40-45 km/h')
    indice = int(velocidade_kmh // 5)
    return velocidades[indice]

def ps_velocidade_categorica(velocidade_kmh):
    velocidades = ('0-10 km/h', '10-20 km/h', '20-30 km/h', '30-40 km/h', '40-50 km/h', '50-60 km/h', '60-70 km/h', '70-80 km/h', '80-90 km/h')
    indice = int(velocidade_kmh // 10)
    return velocidades[indice]

def chuva_categorica(chuva_mm):
    chuvas = ('5-20 mm', '20-35 mm', '35-50 mm', '50-65 mm', '65-80 mm', '80-95 mm', '95-110 mm', '110-125 mm', '125-130 mm')
    chuva_mm -= 5
    indice = int(chuva_mm // 15)
    return chuvas[indice]