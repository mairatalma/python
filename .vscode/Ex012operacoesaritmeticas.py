#ordem de precedencia: Primeiro (). Segundo **. Terceiro *,/,//, %. Quarto + e -

nome = input("Qual o seu nome?")
idade = input("Qual sua idade?")
sexo = input("Qual seu gênero?")
status = input("Qual seu status?")
print("Prazer em te conhecer {}!".format(nome))
print("Prazer em te conhecer {}, {}, {}, {}!".format(nome, idade, sexo, status))

n1 = int(input("Um valor:"))
n2 = int(input("Outro valor:"))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print("A soma é {}, o produto é {}, a divisão é {:.3f}".format(s, m , d))
print("Divisão inteira é {} e potencia {}". format(di, e))

n10 = int(input("Um valor:"))
n09 = n10 - 1
n11 = n10 + 1
print("valor inteiro é {}, valor antecessor é {}, valor sucessor é {}".format(n10, n09, n11))

n15 = int(input("Número:"))
dobro = n15 * 2
triplo = n15 * 3
raiz = n15 ** 0.5
print("Número {}, dobro {}, triplo {}, raiz {}".format (n15, dobro, triplo, raiz))