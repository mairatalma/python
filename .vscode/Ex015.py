reproduções = 100
numero_curtidas = 5
reproduções_curtidas = reproduções + numero_curtidas
musica_favorita_1 = "Always"
musica_favorita_2 = "Buquê De Flores"
musica_favotira_3 = "Falta você"
interações = 3
comentarios = 6

if reproduções > 100 and numero_curtidas > 20:
    print("Música adicionada à playlis")
else:
    print("Musica não atende aos critérios")

if reproduções > 200 or numero_curtidas > 50:
    print("Música destacada na Playlist.")
else:
    print("Musica não destacada")

if reproduções < 50 or numero_curtidas < 10:
    print("Música removida da Playlist.")
else:
    print("A música continua na Playlist.")

if interações > 250:
    print("Recomende esta música para seus amigos!")
else:
    print("A música não foi recomendada.")

if comentarios > 30:
    print("Música com muitos comentários destacada!")
else:
    print("A música não será destacada por comentários.")