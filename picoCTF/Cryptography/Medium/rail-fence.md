El enunciado incluye el siguiente enlace a [Wikipedia](https://en.wikipedia.org/wiki/Rail_fence_cipher).

Al parecer, el mensaje está cifrado usando "Rail fence cipher", que consiste en disponer las letras en *N* "raíles" en una "valla" imaginaria haciendo zigzag. Por ejemplo, en una "vaya" de 3 raíles, el texto `WE ARE DISCOVERED. RUN AT ONCE` se dispondría: 

![](imágenes/Pasted%20image%2020240828224651.png)

Posteriormente, se lee horizontalmente cada línea. En el ejemplo: `WECRUOERDSOEERNTNEAIVDAC`

Para desencriptarlo: 
- Periodo = 2(*N* - 1) 
- *L* = longitud del string. 
- Siendo *L* múltiplo de *Periodo*, *K* = *L* / 2(*N* - 1). La longitud del primer y último string horizontal. Los strings intermedios tendrán longitud 2*K*. 
- Si no lo es, añadiremos 2 variables: 
	- x + 1 = nº diagonales 
	- y = nº de espacios vacíos en la última diagonal
- Para calcular estos valores, usaremos la siguiente ecuación, teniendo x e y los mínimos valores posibles: 
![](imágenes/Pasted%20image%2020240828230825.png)
- Para resolverlo, incrementaremos *x* de 1 en 1 hasta que el denominador sea mayor que *L*, y despejaremos *y* para obtener el valor. 

Utilizaremos estas medidas para separar el string cifrado en grupos, con el fin de verlo de forma más clara: `WECRUO ERDSOEERNTNE AIVDAC`. Disponiendo en una valla el mensaje podremos simplemente leer el contenido en zigzag. 


En nuestro caso, sabemos que tenemos 4 raíles y el flag cifrado es `Ta _7N6DDDhlg:W3D_H3C31N__0D3ef sHR053F38N43D0F i33___NA`. 

Haré un script en python para verlo de forma automatizada:
![](./rail_fence.py)

Obteniendo como resultado: 
`The flag is: WH3R3_D035_7H3_F3NC3_8361N_4ND_3ND_D00AFDD3`

Por lo que la flag es `picoCTF{WH3R3_D035_7H3_F3NC3_8361N_4ND_3ND_D00AFDD3}`