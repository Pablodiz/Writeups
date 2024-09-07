Fecha: 07/09/2024

Empiezo usando nmap: 
```bash
sudo nmap -p- -sS -sC -sV --min-rate 5000 -n -Pn 172.17.0.2 -oN scan
```

![](imágenes/Pasted%20image%2020240907190932.png)

Al mirar la página, hay un jenkins así que investigo como obtener información del mismo. Encuentro que puedo usar auxiliary/scanner/http/jenkins_enum

![](imágenes/Pasted%20image%2020240907200354.png)

Tras hacer `exploit`, obtengo la siguiente información: 
![](imágenes/Pasted%20image%2020240907200420.png)


Sobre la versión de jenkins, veo que hay una vulnerabilidad que me permite ver ficheros:
![](imágenes/Pasted%20image%2020240907201244.png)

Uso el script para ver /etc/passwd y veo dos usuarios "bobby" y "pinguinito":
![](imágenes/Pasted%20image%2020240907201641.png)

Usaré hydra para encontrar sus contraseñas, centrándome en "bobby" antes:
```bash
sudo hydra -l bobby -P /usr/share/wordlists/rockyou.txt ssh://172.17.0.2 -t 16 
```

![](imágenes/Pasted%20image%2020240907203026.png)

Me conecto y veo que puedo ejecutar python como si fuera "pinguinito", así que lo usaré para escalar privilegios. 
![](imágenes/Pasted%20image%2020240907203216.png)

```bash
sudo -u pinguinito /usr/bin/python3 -c "import os; os.system('/bin/bash')"
```

Como pinguinito, puedo ejecutar un script en python, así que compruebo mis permisos de escritura sobre el mismo: 
![](imágenes/Pasted%20image%2020240907203335.png)


![](imágenes/Pasted%20image%2020240907203813.png)

No puedo escribir sobre el mismo, pero como soy el propietario cambiaré los permisos para hacerlo y lo editaré para escalar privilegios:

![](imágenes/Pasted%20image%2020240907204002.png)