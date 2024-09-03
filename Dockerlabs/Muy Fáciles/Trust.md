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