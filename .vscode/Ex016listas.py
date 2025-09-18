musicas = ["Always", "Falta você", "Turuturu"]
print(musicas)

#para acessar elementos específicos
print(musicas[0])
print(musicas[1])

#adicionar itens
musicas.append("Evidencias")
print(musicas)

#remover
musicas.remove("Falta você")
print(musicas)

#saber quantos itens
print(len(musicas))

musicas = ["Always", "Falta você", "Turuturu", "Evidencias", "Bateu saudade", "Galinha Pintadinha", "Luz nova", "Voa", "Moça", "Coração"]

reproduções = 56
curtidas = 100

if reproduções > 100 and curtidas > 20:
    print("Música adicionada à Playlist.")

musicas.append("You")

musicas.remove("Always")
musicas.remove("Turuturu")
print(musicas)
          