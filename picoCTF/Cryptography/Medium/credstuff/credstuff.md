Fecha: 30/08/2024
Tenemos dos ficheros: `usernames.txt` y `passwords.txt`

Según el enunciado, debemos buscar la contraseña de `cultiris`, teniendo en cuenta que cada línea de usernames se corresponde con el mismo número de línea en passwords. 

Podría usar un lector de ficheros que cuente las líneas pero usaré bash: 

```bash
cat leak/usernames.txt | grep --line-number "cultiris" 
# Obtenemos 378:cultiris. Quitaré todos los caracteres a partir de : 
cat leak/usernames.txt | grep --line-number "cultiris" | sed -e "s/:.*//" 
# Obtenemos 378, el número de línea
# sed -n "<n>p" fichero me da la linea <n> del mismo, así que:
sed -n "$(cat leak/usernames.txt | grep --line-number "cultiris" | sed -e "s/:.*//")p" leak/passwords.txt
```

La salida del comando es `cvpbPGS{P7e1S_54I35_71Z3}`, la cual me recuerda a un cifrado cesar. Pruebo haciendo un script:

```python
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
```

Efectivamente, esto me devuelve el flag: `picoCTF{C7r1F_54V35_71M3}`
