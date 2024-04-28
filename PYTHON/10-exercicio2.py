gameDescription = '''
  Fifa 23 é um jogo de futebol,
  desenvolvido pela EA Sports,
  e que possibilita jogar 
  localmente ou online.
'''

print(gameDescription[1:].replace("f", "$")) # Altera elementos

text = input("Escreva uma frase e substituirei a primeira letra na frase por $ exceto a própria primeira letra: ")

char = text[0].lower()

text_replace = text[1:].replace(char, "$")


print(char + text_replace) # Altera elementos

# Troca de caracteres

str1 = input("Escreva a palavra 1: ")
str2 = input("Escreva a palavra 2: ")

new_str = str2[:2] + str1[:2]

print(new_str)