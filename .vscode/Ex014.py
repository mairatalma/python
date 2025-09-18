curtidas = 75
comentários = 10
curtidas_e_comentarios = curtidas + comentários
compartilhamentos = 1

if curtidas > 50 and comentários > 5:
    print("Mostrar postagem popular.")
else:
    print("Postagem não popular.")

if curtidas > 100 or compartilhamentos > 10:
    print("Destacar postagem")
else:
    print("Portagem não será destacada.")

if curtidas < 20 or compartilhamentos <2:
    print("Ocultar postagem pouco popular")

else:
    print("Postagem será exibida")

if 20 <= curtidas <= 50 and comentários >=3:  #Se o número de curtidas está entre 20 e 50 (inclusive) e o número de comentários é maior ou igual a 3,
    print("Enviar notificação de engajamento médio.")

else: #senão (qualquer outro caso)
    print("Postagem sem engajamento médio.")

if curtidas_e_comentarios > 100:
    print("Destacar postagens com muitas interações.")
else:
    print("Postagem sem destaque")