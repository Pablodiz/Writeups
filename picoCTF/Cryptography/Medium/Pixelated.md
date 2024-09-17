Fecha: 18/09/2024

Viendo los nombres de las imágenes me imagino que habrá que mezclar ambas imágenes. Después de buscar como hacerlo, hago el siguiente script:

```python
from PIL import Image
import numpy as np 

# Abrir las imágenes
entradas = [Image.open(i) for i in ["./scrambled1.png", "./scrambled2.png"]]

# Comprobar que los tamaños son los mismos
for imagen in entradas:
    if imagen.size!=entradas[0].size:
        raise Exception("Los tamaños de imagenes deberian ser iguales")
        break
    else: 
        arr1 = np.array(entradas[0])
        arr2 = np.array(entradas[1])
        suma = (arr1 + arr2) % 256 # Hacer mod 256 en cada valor del array
        # Transformar el array de ints de 8 bits (0-255) en una Image
        result_img = Image.fromarray(suma.astype('uint8'))
        # Guardar esta imagen en un fichero
        result_img.save("./resultado.png")('uint8'))
        result_img.save("./resultado.png")
```

Obteniendo como resultado:

![](imágenes/Pasted%20image%2020240918000845.png)
