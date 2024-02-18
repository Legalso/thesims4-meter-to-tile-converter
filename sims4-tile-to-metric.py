#Criado para converter "tiles" do jogo The Sims 4 para metros.
#Nos jogos The Sims, um "tile" representa 3 pés (cerca de 0,9144 metros). Um "tile" do The Sims 4 é equivalente a aproximadamente 0,8361 metros quadrados. Se você deseja converter para metros, cada "tile" seria aproximadamente 0,2787 metros de cada lado.

meters = 0.2787;
print("Bem vindo ao conversor de tiles para metros!");

metersQuantity = input("Digite quantos metros deseja converter: ");

tiles = float(metersQuantity) / meters;

print("Para", metersQuantity, "metros", "a quantidade de tiles é:", int(tiles));