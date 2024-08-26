Fecha: 01/08/2024

Me conecto al reto usando netcat y me piden que les convierta unas listas a palabras: binario, octal y hexadecimal respectivamente. Cada vez que me conecto es distinto, así que intenté que fuera cómodo obtener los resultados. 

Mensaje:
```
Let us see how data is stored
colorado
Please give the 01100011 01101111 01101100 01101111 01110010 01100001 01100100 01101111 as a word.
...
you have 45 seconds.....

Input:
colorado
Please give me the  156 165 162 163 145 as a word.
Input:
nurse
Please give me the 636f6d7075746572 as a word.
Input:
computer
You've beaten the challenge
Flag: picoCTF{learning_about_converting_values_00a975ff}

```

Código usado: 
```python
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
```


