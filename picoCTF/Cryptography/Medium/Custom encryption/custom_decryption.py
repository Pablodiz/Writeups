from custom_encryption import is_prime, generator, dynamic_xor_encrypt, encrypt
import itertools

# P y g son un número entre a y a+10 y b y b+10 respectivamente. Además, ambos son primos
def posibles_p_and_g(a:int , b:int):
    posibles_a = [i for i in range(a, a+10) if is_prime(i)]
    posibles_b = [i for i in range(b, b+10) if is_prime(i)]
    return [i for i in itertools.product(posibles_a, posibles_b)]



def decrypt(cipher, key):
    plaintext = ""
    for encrypted_value in cipher:
        decrypted_value = encrypted_value // (key * 311)
        plaintext += chr(decrypted_value)
    return plaintext
    
# Función usada para probar cuantas veces hay que usar dynamic_xor_encrypt para volver al original
def probar_xor_decrypt():
    contador = 0 
    llave = "trudeau"
    original = "abcde"
    encriptado = dynamic_xor_encrypt(original, llave)

    while  encriptado != original:
        encriptado=dynamic_xor_encrypt(encriptado, llave)
        contador+=1
    # El contador es 3
    
    encriptado = dynamic_xor_encrypt(original, llave)
    print(f"El texto encriptado es: {encriptado}")
    for _ in range(0,contador):
        encriptado=dynamic_xor_encrypt(encriptado, llave)
    print(f"El original es {original}, y el encriptado una vez desencriptado es: {encriptado}")

def dynamic_xor_decrypt(cipher_text, text_key):
    desencriptado = dynamic_xor_encrypt(cipher_text, text_key)
    for _ in range(0,3-1):
        desencriptado=dynamic_xor_encrypt(desencriptado, text_key)
    return desencriptado

def test_decrypt(cipher_text, text_key, a, b):
    lista = posibles_p_and_g(a,b)

    test_texto = 'picoCTF{aeiou}'
    semi_cipher = dynamic_xor_encrypt(test_texto, text_key)
    test_shared_key = 33

    #Compruebo las funciones que hice
    print(f"Funciona xor_decrypt? {test_texto==dynamic_xor_decrypt(dynamic_xor_encrypt(test_texto, text_key),text_key)}")
    print(f"Funciona decrypt? {semi_cipher==decrypt(encrypt(semi_cipher, test_shared_key),test_shared_key)}")

    for (p, g) in lista:
        u = generator(g, a, p)
        v = generator(g, b, p)
        key = generator(v, a, p)
        b_key = generator(u, b, p) 
        shared_key = None
        if key == b_key:
            shared_key = key
        else:
            print("Invalid key")
            return 
        semi_cipher = decrypt(cipher_text, shared_key)
        desencriptado = dynamic_xor_decrypt(semi_cipher, text_key)
        print(desencriptado)





if __name__=="__main__":
    a = 95
    b = 21
    message = [237915, 1850450, 1850450, 158610, 2458455, 2273410, 1744710, 1744710, 1797580, 1110270, 0, 2194105, 555135, 132175, 1797580, 0, 581570, 2273410, 26435, 1638970, 634440, 713745, 158610, 158610, 449395, 158610, 687310, 1348185, 845920, 1295315, 687310, 185045, 317220, 449395]
    test_decrypt(message, "trudeau", a, b)
    

    

