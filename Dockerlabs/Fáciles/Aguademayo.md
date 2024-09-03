Fecha: 13/08/2024

Lo primero que hago es nmap, encontrando un servidor http y ssh, ninguno con vulnerabilidades

```
sudo nmap -p- -sS -sC -sV --min-rate 5000 -n -Pn 172.17.0.2 -oN scan
```

Miro el html de la página y encuentro un comentario con el siguiente contenido: 

```
++++++++++[>++++++++++>++++++++++>++++++++++>++++++++++>++++++++++>++++++++++>++++++++++++>++++++++++>+++++++++++>++++++++++++>++++++++++>++++++++++++>++++++++++>+++++++++++>+++++++++++>+>+<<<<<<<<<<<<<<<<<-]>--.>+.>--.>+.>---.>+++.>---.>---.>+++.>---.>+..>-----..>---.>.>+.>+++.>.
```

Miro https://www.dcode.fr/es y veo varias posiblidades. Viéndolas, me tiene pinta de que es un `brainfuck`. Uso su herramienta para decodificarlo y me encuentro el siguiente mensaje: `bebeaguaqueessano` 
![](Imágenes/Pasted%20image%2020240813153408.png)

![](Imágenes/Pasted%20image%2020240813153539.png)

Ahora fuzzing de la url, y encuentro que hay existe http://172.17.0.2/images.

```
ffuf -c -recursion -w /usr/share/wordlists/directory-list-2.3-medium.txt -u http://172.17.0.2/FUZZ  -e .php,.html,.txt,.js -o fuzzing 
```

![](Imágenes/Pasted%20image%2020240813153735.png)

Descargo la imagen que hay e intento aplicar #esteganografía:
- Exiftool: no encuentro nada. 
- Steghid, usando como passphrase la frase encontrada anteriormente, no consigo nada. 

```
steghide --extract -sf imagen.jpg -xf steghide_extract -p bebeaguaqueessano
```

Pruebo algo más fácil: como la imagen se llama agua_ssh, intento conectarme por ssh con ese usuario. Efectivamente, entro a la máquina. 

Haciendo `sudo -l`, veo que puedo ejecutar `bettercap` como root. Lo hago, y veo que hay un comando que me deja ejecutar otros: 
![](Imágenes/Pasted%20image%2020240813155119.png)

Hago `! chmod +s /bin/bash` para setear el bit SETUID de /bin/bash. De esta forma, cuando haga sudo `/bin/bash -p` me quedaré con privilegios de root

![](Imágenes/Pasted%20image%2020240813155358.png)
