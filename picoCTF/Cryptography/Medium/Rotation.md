Fecha: 16/09/2024
El mensaje encriptado es el siguiente:
```
xqkwKBN{z0bib1wv_l3kzgxb3l_25l7k61j}
```

Pienso que podría ser por César, así que pruebo:

```python
import string
letras_minusculas = list(string.ascii_lowercase)
letras_mayusculas = list(string.ascii_uppercase)

entrada = "xqkwKBN{z0bib1wv_l3kzgxb3l_25l7k61j}"

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
```

Y obtengo el flag:
![](imágenes/Pasted%20image%2020240916231726.png)
