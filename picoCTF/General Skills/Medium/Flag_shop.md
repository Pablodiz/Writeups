Comprobando el [código](store.c) veo lo siguiente:

Para obtener el flag, el balance debe ser mayor que 100000

![](Imágenes/Pasted%20image%2020241031010434.png)

Viendo la otra opción, veo que se lee una cantidad de banderas que compras y, despues de multiplicarlo por otro número, se resta a tu balance. Se puede intentar que ese número sea negativo para aumentar nuestro balance. El máximo int en C es 2,147,483,647. A partir del mismo, el número "se convierte" en negativo. Como lo multiplicamos por 900, si introducimos un número suficientemente grande, por ejemplo 3,000,000 -> 900 * 3,000,000 = 2,700,000,000 >  2,147,483,647.
![](Imágenes/Pasted%20image%2020241031011559.png)

![](Imágenes/Pasted%20image%2020241031011336.png)

Con este balance, elijo la 1337 Flag y obtengo el flag

