Fecha: 07/08/2024
Empiezo haciendo un nmap completo, veo que tiene un apache en el puerto 80.

![](../Fáciles/Imágenes/Pasted%20image%2020240807002812.png)

Primero busqué vulnerabilidades en esos servicios, pero no las encontré con searchsploit

![](Imágenes/Pasted%20image%2020240807004257.png)

Al acceder a la página, veo que únicamente hay una imagen, que descargo para buscar información:

![](Imágenes/Pasted%20image%2020240807003049.png)

Uso exiftool y encuentro un usuario, por lo que usaré hydra para probar contraseñas con la wordlist rockyou.txt, encontrando que tiene la contraseña 123456
```
sudo exiftool imagen.jpeg
```

![](Imágenes/Pasted%20image%2020240807003223.png)

```
sudo hydra -l borazuwarah -P /usr/share/wordlists/rockyou.txt ssh://172.17.0.2
```

![](Imágenes/Pasted%20image%2020240807003336.png)

Me conecto por ssh y lo primero que hago es comprobar qué puedo hacer con sudo:

![](Imágenes/Pasted%20image%2020240807003448.png)

Puedo hacerme root simplemente haciendo `sudo bash` sin tener que introducir la contraseña: 

![](Imágenes/Pasted%20image%2020240807003640.png)

O hacer cualquier comando en la máquina con permisos de superusuario, por lo que haciendo `sudo su` e introduciendo la contraseña `123456` me hago root: 

![](Imágenes/Pasted%20image%2020240807003845.png)
