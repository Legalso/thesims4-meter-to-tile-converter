# Convertor de "tiles" do The Sims 4 para metros (m).
# Nos jogos The Sims, um "tile" representa 3 pés (cerca de 0,9144 metros). Um "tile" do The Sims 4 é equivalente a aproximadamente 0,8361 metros quadrados. Se você deseja converter para metros, cada "tile" seria aproximadamente 0,2787 metros de cada lado. Usamos a metade de um "tile" para calcular a área.

# Função para verificar se a entrada é um número
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

meters = 0.2787
print("Bem vindo ao conversor de tiles para metros!")

metersQuantity = input("Digite quantos metros deseja converter: ")

while not is_number(metersQuantity):
    metersQuantity = input("Digite quantos metros deseja converter: ")

#converte a string do input em float e calcula a quantidade quantos metros tem em tiles.
#um tile tem dois quadradinhos. no começo pensei nesse quadradinho como um tile, mas na verdade ele é metade de um real tile. por isso a divisão por 2.
tiles = (float(metersQuantity) / meters) / 2
#arredondar para cima se passar de 0.5, dessa maneira exibe apenas um número inteiro (ajuda a visualizar melhor).
tiles = round(tiles)
print("Para", metersQuantity, "metros", "a quantidade de tiles é:", tiles)