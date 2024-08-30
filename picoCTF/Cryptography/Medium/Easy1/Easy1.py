import string 
# Variables dadas
mensaje="UFJKXQZQUNB"
llave = "SOLVECRYPTO"
# Elementos que utilizaré
letras = string.ascii_uppercase
n_letras = len(letras)
resultado = ""
# Resolver
for i in range(len(mensaje)):
    indice_mensaje = letras.index(mensaje[i])
    indice_llave = letras.index(llave[i])
    resultado+=letras[(indice_mensaje-indice_llave)%n_letras]
    

print("picoCTF{" + resultado + "}")
