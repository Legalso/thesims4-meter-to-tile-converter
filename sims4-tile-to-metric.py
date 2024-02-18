# Criado para converter "tiles" do jogo The Sims 4 para metros.
# Nos jogos The Sims, um "tile" representa 3 pés (cerca de 0,9144 metros). Um "tile" do The Sims 4 é equivalente a aproximadamente 0,8361 metros quadrados. Se você deseja converter para metros, cada "tile" seria aproximadamente 0,2787 metros de cada lado.

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

#every tile tem dois quadradinhos. no começo pensei nesse quadradinho como um tile, mas na verdade ele é metade de um tile. por isso a divisão por 2.
tiles = (float(metersQuantity) / meters) /2
print("Para", metersQuantity, "metros", "a quantidade de tiles é:", int(tiles))