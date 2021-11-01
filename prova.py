def imprime_tabela():
    print("------- Relatório Frota Taxis --------")
    print("Taxi Distância (km) Consumo (litros)")
    print("--------------------------------------")
    for i in range(0, len(distancias)):
       print(f"Taxi{i+1: <9} {distancias[i]: <18} {consumo[i]}")
    print("--------------------------------------")

def calcula_distancia_total_percorrida():
    total = sum(distancias)
    print(f"Distância total percorrida: {total} km")

def calcula_consumo_total():
   total = sum(consumo)
   print(f"Consumo total de combustível pelos taxis: {total} Litros")
   

def calcula_media_geral():
    print(f"Média geral de consumo: {sum(distancias) / sum(consumo)} km/litro")

def imprime_consumo_medio_frota():
    print("------- Relatório Frota Taxis --------")
    print("Taxi  Consumo médio")
    print("--------------------------------------")
    for i in range(0, len(distancias)):
        print(f"Taxi {i + 1: <4}  {distancias[i] / consumo[i]: <8} km/l")
    print("--------------------------------------")

def imprime_maior_menor_consumo():
     var = 0
     j = 100000
     taxiMaior = 0
     taxiMenor = 0
     for i in range(0, len(distancias)):
        if (var < consumo[i]):
            var = consumo[i]
            taxiMaior = i+1
        if (j > consumo[i]):
            j = consumo[i]
            taxiMenor = i+1

     print(f"Taxi {taxiMaior} apresentou o maior consumo: {var} em km/l> km/l")
     print(f"Taxi {taxiMenor} apresentou o menor consumo: {j} em km/l> km/l")

##### ATENÇÃO: NÃO ALTERAR NADA DAQUI PRA BAIXO ######
def main():
    imprime_tabela()
    calcula_distancia_total_percorrida()
    calcula_consumo_total()
    calcula_media_geral()
    imprime_consumo_medio_frota()
    imprime_maior_menor_consumo()

distancias = [1233, 999, 1566, 1348, 1088, 875, 1576, 1321]
consumo = [120, 87, 130, 140, 95, 70, 145, 125]

if __name__ == '__main__':
    main()