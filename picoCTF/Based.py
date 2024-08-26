def bin_to_str(entrada:str):
    lista = entrada.split()
    resultado = ""
    for i in lista: 
        entero = int(i,2)
        hex_str = hex(entero)[2:] #Elimino el 0x con [2:]
        resultado+=bytes.fromhex(hex_str).decode('ascii')
    return resultado

def oct_to_str(entrada:str):
    lista = entrada.split()
    resultado = ""
    for i in lista: 
        entero = int(i,8)
        resultado+=chr(entero)
    return resultado

def hex_to_str(entrada: str):
    bytes_obj = bytes.fromhex(entrada)
    resultado = bytes_obj.decode("utf-8")
    return(resultado)


print(bin_to_str("01100011 01101111 01101100 01101111 01110010 01100001 01100100 01101111"))
print(oct_to_str("156 165 162 163 145"))
print(hex_to_str("636f6d7075746572"))