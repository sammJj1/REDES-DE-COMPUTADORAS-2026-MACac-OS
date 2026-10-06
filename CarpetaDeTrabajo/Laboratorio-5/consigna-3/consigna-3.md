#### EXPERIMENTO TCP: Captura en loopback con filtro tcp.port == 12000
- Terminal A (Servidor)

![](/CarpetaDeTrabajo/Laboratorio-5/Consigna-3/Imagenes/ncatA-tcp.png)

- Terminal B (Cliente)

![](/CarpetaDeTrabajo/Laboratorio-5/Consigna-3/Imagenes/ncatB-tcp.png)

- *Captura en Wireshark:*

![](/CarpetaDeTrabajo/Laboratorio-5/Consigna-3/Imagenes/wireshark-tcp.png)

#### EXPERIMENTO UDP: Captura en loopback con filtro udp.port == 12001
- Terminal A (Servidor)

![](/CarpetaDeTrabajo/Laboratorio-5/Consigna-3/Imagenes/ncatA-udp.png)

- Terminal B (Cliente)

![](/CarpetaDeTrabajo/Laboratorio-5/Consigna-3/Imagenes/ncatB-udp.png)

- *Captura en Wireshark:*

![](/CarpetaDeTrabajo/Laboratorio-5/Consigna-3/Imagenes/wireshark-udp.png)

#### RESPUESTAS A LA CONSIGNAS EXPERIMENTALES
#### a) ¿Qué pasó en la red cuando ejecutaron el comando del cliente, antes de escribir el primer mensaje? Compárenlo con TCP

Cuando ejecutamos el comando del cliente, antes de escribir el primer mensaje "Hola", se dieron los siguientes comportamientos en la red:

- **En TCP:** se disparó el **Three-Way Handshake**, donde se transmitieron 3 paquetes
    
    1. Cliente -> Servidor: `[SYN]`
        
    2. Servidor -> Cliente: `[SYN, ACK]`
        
    3. Cliente -> Servidor: `[ACK]`

![](/CarpetaDeTrabajo/Laboratorio-5/Consigna-3/Imagenes/3a-1.png)

- **En UDP:** No pasó nada al ejecutar el cliente, ya que UDP es un protocolo no orientado a conexión

![](/CarpetaDeTrabajo/Laboratorio-5/Consigna-3/Imagenes/3a-2.png)

#### b) ¿Cuántos datagramas generó cada mensaje? ¿Hay algo parecido a un ACK?

Cada mensaje enviado en UDP generó 1 datagrama, sin la presencia de algo parecido a un ACK debido a que este no tiene un mecanismo de acuse de recibo. Envía al destino sin verificar si el receptor esta listo o los datos llegaron bien. 
En cambio, vemos que en TCP se generaron 2 segmentos con la presencia de ACK para asegurar la entrega.

#### c) Comparen el encabezado UDP con el encabezado TCP de un segmento con datos: ¿qué campos tiene cada uno? ¿Cuántos bytes ocupa cada encabezado?

- **Encabezado TCP:**
    
    - **Tamaño:** 20 bytes minimos
        
    - **Campos:** 
	    - Source Port
	    - Destination Port
	    - Sequence Number
	    - Acknowledgment Number
	    - Data Offset/Header Length
	    - Flags (SYN, ACK, PSH, FIN, RST)
	    - Window Size
	    - Checksum
	    - Urgent Pointer

![](/CarpetaDeTrabajo/Laboratorio-5/Consigna-3/Imagenes/3c-1.png)

- **Encabezado UDP:**
    
    - **Tamaño:** 8 bytes fijos
        
    - **Campos:** 
	    - Source Port 
	    - Destination Port 
	    - Length 
	    - Checksum
        
![](/CarpetaDeTrabajo/Laboratorio-5/Consigna-3/Imagenes/3c-2.png)

#### d) ¿Qué pasó en la red al cerrar el cliente con Ctrl+C? ¿Y en TCP?

- **En UDP:** Al cerrar el cliente, no ocurre nada en la red. Como no existe estado de conexión, el proceso local simplemente se cierra sin avisar al otro extremo.

- **En TCP:** Vemos un cierre forzado utilizando [RST, ACK], sin realizar el proceso de cierre ordenado con [FIN, ACK] del **Four-Way handshake**.

#### e) Para enviar la misma frase, ¿cuántos paquetes necesitaron en total con TCP y cuántos con UDP? ¿Qué "compran" con los paquetes extra de TCP?
Para enviar la misma frase:
- **UDP:** Se necesitó 1 paquete por mensaje.

![](/CarpetaDeTrabajo/Laboratorio-5/Consigna-3/Imagenes/3e-1.png)

 - **TCP:** Se necesitó 2 paquetes por mensaje.
	- 1 con los datos (PSH/ACK)
	- 1 de confirmación de recepción (ACK)

![](/CarpetaDeTrabajo/Laboratorio-5/Consigna-3/Imagenes/3e-2.png)

Esto se debe a que con los paquetes extra de TCP "compramos":
    
- **Confiabilidad:** Garantía de entrega (con retransmisión ante pérdida). El emisor sabe si llegó el mensaje por la confirmación ACK.
        
- **Ordenamiento:** Se asegura que el receptor lea los bytes en el orden exacto en que fueron emitidos, reconstruyendo el flujo si llegan desordenados.
        
- **Control de flujo y congestión:** Permite sincronizar la velocidad de emisión con la capacidad de procesamiento del receptor.


#### f) ¿Y si nadie escucha?
- **En TCP:**
    - El cliente envía un segmento `[SYN]` solicitando iniciar la conexión.
        
    - Como el puerto 12000 está cerrado, el destino responde con un segmento TCP con la bandera `[RST, ACK]` (Reset), indicando que el puerto no está activo y rechaza la conexión. 

![](/CarpetaDeTrabajo/Laboratorio-5/Consigna-3/Imagenes/3f-1.png)

- **En UDP:**
    - Al escibir un mensaje y darle Enter, el cliente envía el datagrama UDP al puerto 12001.
        
    - Como no hay ningún proceso escuchando en 12001, la pila de red receptora descarta el paquete y responde con un mensaje **ICMP: "Destination Unreachable (Port Unreachable)"**.

![](/CarpetaDeTrabajo/Laboratorio-5/Consigna-3/Imagenes/3f-2.png)