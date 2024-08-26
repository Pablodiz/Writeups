import base64
import string 
encoded = "YidkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVROclgyMHdNakV5TnpVNGZRPT0nCg=="

# Parece en b64 -> Lo decodificamos
decoded_1 = base64.b64decode(encoded).decode("utf-8")
print(decoded_1) # b'd3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrX20wMjEyNzU4fQ=='  -> Quitamos el b'...'

parte_interesa = "d3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrX20wMjEyNzU4fQ=="

# Lo que obtenemos sigue pareciendo b64 -> Decodificamos de nuevo
decoded_2 = base64.b64decode(parte_interesa).decode("utf-8")
print(decoded_2) # wpjvJAM{jhlzhy_k3jy9wa3k_m0212758} 

# Ya parece un flag -> Usamos la otra tag (caesar)
# El decodificado de caesar consiste en desplazar cada letra por una x veces más adelantada. Los números no varían
def decodificar_cesar(mensaje_cifrado, desplazamiento):
    mensaje_decodificado = ""

    for caracter in mensaje_cifrado:
        if caracter.isalpha():
            # Determinar el valor ASCII base
            base = ord('A') if caracter.isupper() else ord('a')
            # Decodificar el carácter
            nueva_posicion = (ord(caracter) - base - desplazamiento) % 26
            nuevo_caracter = chr(base + nueva_posicion)
            mensaje_decodificado += nuevo_caracter
        else:
            # No cambiar caracteres no alfabéticos
            mensaje_decodificado += caracter

    return mensaje_decodificado


# Podemos mirar todas las combinaciones:
alfabeto = alfabeto_minusculas = list(string.ascii_lowercase)
for i in range(len(alfabeto)):
    print(decodificar_cesar(decoded_2, i))
# Entre los resultados, obtenemos picoCTF{caesar_d3cr9pt3d_f0212758}

# Otra opción es, como sabemos que el flag empieza por "p", mirar directamente con esa distancia
print("El flag es: "+ decodificar_cesar(decoded_2, abs(ord('p')-ord(decoded_2[0]))))