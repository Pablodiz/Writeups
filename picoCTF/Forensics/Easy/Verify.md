Sin haber leído correctamente el enunciado y viendo los contenidos de los ficheros, pensé que tenía que comparar el contenido con el hash objetivo: 
```bash
DIRECTORIO="files"
or file in "$DIRECTORIO"/*; do
contenido=$(cat $file);
if [ "$contenido" = "fba9f49bf22aa7188a155768ab0dfdc1f9b86c47976cd0f7c9003af2e20598f7" ]; 
then echo "$file: $(cat $file)";
fi; 
done
```

Cuando leí bien, vi que había que comparar el hash en SHA-256 de los ficheros con el hash entregado, y posteriormente decodificar el fichero cuyo hash coincidiera:

```bash
DIRECTORIO="files"
OBJETIVO="fba9f49bf22aa7188a155768ab0dfdc1f9b86c47976cd0f7c9003af2e20598f7"
for file in "$DIRECTORIO"/*; do
# La salida era <hash> <ruta al archivo>, así que corté la segunda parte
hash=$(sha256sum $file | cut -d ' ' -f1);
if [ "$hash" =  "$OBJETIVO" ]; 
then echo "Contenido de $file desencriptado: $(./decrypt.sh $file)";
fi; 
done
```

Fecha: 01/08/2024
