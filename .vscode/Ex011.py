a = input("Digite algo: ")   #input() sempre retorna uma string (str).
print("O tipo primitivo desse valor é ", type(a)) #type(a) irá mostrar <class 'str'> para qualquer entrada.
print("Só tem espaços?", a.isspace())
print("É um número?", a.isnumeric())
print("É decimal?", a.isdecimal())
print("É alfabetico?", a.isalpha())
print("É um alfanúmerico?", a.isalnum())
print("Esta em maiuscula?", a.isupper())
print("Esta em minuscula?", a.islower())
print("Esta capitalizada?", a.istitle())

# a é objeto e todo objeto tem caracteristicas e realiza funcionalidades
# acima tem vários exemplos de métodos usados em python