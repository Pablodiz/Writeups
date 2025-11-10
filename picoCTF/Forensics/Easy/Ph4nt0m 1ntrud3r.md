18-10-2025

Tengo que analizar un archivo pcap. Con strings veo varias cosas base64. Buscando la solución para ver cómo reconstruírlo de forma cómoda, veo que la gente usa el comando:

```bash
tshark -r myNetworkTraffic.pcap -Y "tcp.len==12 || tcp.len==4" -T fields -e frame.time -e tcp.segment_data | sort -k4 | awk '{print $6}' | xxd -p -r | base64 -d
```

1. **Filtra** los paquetes TCP que tienen cargas específicas (4 o 12 bytes).
2. **Extrae** los datos de esos paquetes.
3. **Ordena** los paquetes (aunque eso puede fallar si no se hace correctamente).
4. **Concatena** las cargas TCP extraídas.
5. **Convierte** los datos hexadecimales a binario.
6. **Decodifica** el resultado como Base64.