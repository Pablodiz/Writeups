Fecha: 13/08/2024
#LFI #FUZZING 

Empiezo con nmap: 
```
sudo nmap -p- -sS -sC -sV --min-rate 5000 -n -Pn 172.19.0.2 -oN scan
```

Encuentro ssh en el puerto 22 y http en el 80, ninguno de ellos vulnerable. Mirando la página, solo veo la típica página de apache que indica que el servicio está funcionando, sin ningún comentario especial. Usaré fuzzing para buscar directorios. Aunque otro días usé dirbuster, leyendo comentarios sobre herramientas de este tipo, veo que se habla muy bien de **ffuf** y de **feroxbuster**, diciendo que:
- Dirb y dirbuster están anticuadas. 
- Gobuster no tiene capacidad de recursión. 
Pruebo con `feroxbuster` 

```
feroxbuster -u http://172.19.0.2 -x php -x html -x txt -x js -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -o fuzzing --threads 300
```
![](Imágenes/Pasted%20image%2020240813015839.png)

Con ffuf, lo siguiente haría prácticamente lo mismo:
```
ffuf -c -recursion -w /usr/share/wordlists/directory-list-2.3-medium.txt -u http://172.19.0.2/FUZZ  -e .php,.html,.txt,.js -o fuzzing 
``` 

Haciendo `control+u` en http://172.19.0.2/wordpress encuentro el siguiente comentario: 

![](Imágenes/Pasted%20image%2020240813015744.png)

Pruebo añadiendo `/index.php` a la url y veo que no cambia la apariencia, por lo que puede que se pueda hacer path traversal (usar la url para acceder a archivos ocultos). Leyendo tutoriales, encuentro el comando que usar. El resultado será que si pongo de nombre de parámetro `love`, veré el contenido de /etc/passwd

```
ffuf -c  -u http://172.19.0.2/wordpress/index.php?FUZZ=/../../../../../../../etc/passwd -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -fw 183
```

-c añade color al output, haciéndolo más legible
-u es la url. FUZZ se sustituirá para buscar el nombre de un parámetro que muestre el contenido de /etc/passwd. 
-w la lista de palabras que se sustituirán por FUZZ en la url
-fw filtra las palabras de 183. Previamente, no puse el parámetro. Viendo el output, la gran mayoría (todas menos una) de las respuestas tenían 183 palabras (que es la cantidad de palabras de la página original), por lo que filtré esas opciones. 

![](Imágenes/Pasted%20image%2020240813024054.png)

Visito `http://172.19.0.2/wordpress/index.php?love=/../../../../../../../etc/passwd `

![](Imágenes/Pasted%20image%2020240813024254.png)

Encuentro dos usuarios, pedro y rosa. Probaré a usar hydra con rockyou.txt con ambos. 

```
hydra -L usuarios.txt -P /usr/share/wordlists/rockyou.txt ssh://172.19.0.2 -t 64
```


![](Imágenes/Pasted%20image%2020240813025040.png)

Encuentro las credenciales de rosa, entro en la máquina y veo que tiene permisos de root para cat y ls. Miro si hay alguna forma de explotarlos para convertirse en root en https://gtfobins.github.iopero no lo encuentro, así que uso ambas herramientas para explorar el sistema de archivos: 

![](Imágenes/Pasted%20image%2020240813025546.png)

Encuentro un archivo, secret.txt, con lo que aparentemente es un código hexadecimal. El output parece un código en base 32, así que lo desencripto también 

```
echo "4E5A5857435933464F4A3247433454424F4E58584732494B" | xxd -r -p | base32 -d

noacertarasosi
```

No puedo hacer su directamente, pero si a pedro:

![](Imágenes/Pasted%20image%2020240813030757.png)

Siendo Pedro, puedo ejecutar como root /usr/bin/env, lo cual uso () para hacerme root:

![](Imágenes/Pasted%20image%2020240813030856.png)
