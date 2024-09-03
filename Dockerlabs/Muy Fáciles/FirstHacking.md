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
