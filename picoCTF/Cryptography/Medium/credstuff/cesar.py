import string
letras_minusculas = list(string.ascii_lowercase)
letras_mayusculas = list(string.ascii_uppercase)

entrada = "cvpbPGS{P7e1S_54I35_71Z3}"

n_letras = len(letras_minusculas)

for i in range(n_letras):
    salida = ""
    for caracter in entrada:
        if caracter.isupper():
            salida += letras_mayusculas[(letras_mayusculas.index(caracter)+i)%n_letras]
        elif caracter.islower():
            salida += letras_minusculas[(letras_minusculas.index(caracter)+i)%n_letras]
        else:
            salida+=caracter
    if salida[0:4]=="pico":
        print(salida)