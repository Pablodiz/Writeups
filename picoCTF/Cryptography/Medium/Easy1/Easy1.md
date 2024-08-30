Fecha: 30/08/2024
El reto nos da una flag encriptada (`UFJKXQZQUNB`) y una llave (`SOLVECRYPTO`), además de una matriz de letras. Investigando sobre la misma, encuentro que hay un tipo de cifrado llamado [Cifrado de Vigenère](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher). 

Para cifrar un mensaje, se suma mira el índice de cada letra de la flag encriptada y de la llave en un alfabeto, se suma y se hace el módulo `n` de la misma, siendo `n` la longitud del alfabeto. A continuación, se usa este resultado para obtener la letra con índice = resultado en el abecedario.

```python
for letra in range(len(mensaje)):
    indice_mensaje = abecedario.index(mensaje[letra])
    indice_llave = abecedario.index(llave[letra])
    resultado+=abecedario[(indice_mensaje-indice_llave)%num_letras]
    
```

Le doy la vuelta a este algoritmo, obteniendo el flag `picoCTF{CRYPTOISFUN}`
![fichero de python](./Easy1.py)
