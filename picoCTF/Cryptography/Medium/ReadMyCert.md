Fecha: 28/06/2024

Simplemente descargando el archivo y usando el lector de archivos de Kali Linux pude leer el flag: 

![](imágenes/Pasted%20image%2020240828223302.png)

`picoCTF{read_mycert_a7163be8}`

Podría haber usado el siguiente comando para obtener información sobre el archivo. El flag es el Common Name de la entidad que pidió el certificado: 
```
openssl req -in readmycert.csr  -noout -text
```

![](imágenes/Pasted%20image%2020240828223251.png)