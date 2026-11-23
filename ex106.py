
arquivo = open("banco-temperaturas-julho.txt", "r")

data_consulta = input("Digite a data (aaaa-mm-dd): ")

temperaturas = []

for linha in arquivo:
    dados = linha.split()

    data = dados[0]
    temperatura = float(dados[2])

    if data == data_consulta:
        temperaturas.append(temperatura)

arquivo.close()

if len(temperaturas) > 0:

    minima = min(temperaturas)
    maxima = max(temperaturas)

    amplitude = maxima - minima

    print("\nData:", data_consulta)
    print("Temperatura mínima:", minima, "°C")
    print("Temperatura máxima:", maxima, "°C")
    print("Amplitude térmica:", amplitude, "°C")

else:
    print("\nA data informada não foi encontrada no arquivo.")
