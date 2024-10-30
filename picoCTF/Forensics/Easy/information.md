Descargo la imagen cat.jpg. Aplicando el siguiente comando: 
![](imágenes/Pasted%20Image%2020241030013501.png)

Pasando desde base64 el texto en license, obtengo el flag:
```
echo "cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9" | base64 -d
```
