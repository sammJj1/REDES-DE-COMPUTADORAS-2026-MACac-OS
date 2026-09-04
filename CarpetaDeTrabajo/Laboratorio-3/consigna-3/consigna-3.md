a) 
TCP resuelve directamente los problemas de fiabilidad y coordinación de extremo a extremo que ni Ethernet ni IP abordan por sí mismos:

-  **Entrega ordenada:** Si los datagramas IP toman rutas distintas y llegan desordenados, TCP los reordena usando números de secuencia antes de entregarlos a la aplicación de usuario.
-  **Recuperación ante pérdidas:** Ethernet e IP descartan tramas y paquetes corruptos sin notificar al emisor. TCP utiliza confirmaciones (ACK) y temporizadores para retransmitir automáticamente cualquier dato perdido o dañado.
- **Eliminación de duplicados:** Identifica y descarta copias repetidas de paquetes que se hayan enviado dos veces debido a retrasos en la red o pérdidas de confirmaciones.
-  **Control de flujo extremo a extremo:** Evita que un emisor rápido sature la memoria temporal de un receptor lento utilizando un esquema de créditos (ventana deslizante) que limita la transmisión según la capacidad actual del destino.
-  **Control de congestión:** Detecta de forma implícita la saturación en los encaminadores de la red (a través de pérdidas o retardos elevados) y reduce dinámicamente el flujo de datos para aliviar la sobrecarga del sistema.
-  **Direccionamiento de procesos:** IP solo lleva la información hasta el computador de destino. TCP introduce los puertos para que el computador sepa exactamente a qué aplicación (ej. navegador, correo) debe entregarle los datos.
-  **Establecimiento de conexión seguro:** Coordina al emisor y al receptor mediante un diálogo en tres pasos (three-way handshake), asegurando que ambos extremos estén sincronizados y listos antes de iniciar la transmisión de datos reales.

b)
- **Puereto de origen (16 bits) y de destino (16 bits):** Identifican a los usuarios (procesos o aplicaciones) emisores y receptores en ambos extremos de la comunicacion.
- **Numero de secuencia (32 bits):** Numera de manera implicita cada octeto de datos individual que se transmite a traves de la conexion.
- **Numero de confirmacion (32 bits):** Contiene el numero de secuencia del siguiente octeto de datos que la entidad TCP receptora espera recibir de su par. Es aplicacable y valido unicamente si el indicador (flag) ACK se encuentra activo.
- **Longitud de cabecera (4 bits):** Permite al receptor saber exactamente donde terminal la informacionde control (metadatos) y donde comienzan los datos de usuario de la aplicacion. Especifica la longitud total de la cabecera TCP expresada en palabras de 32 bits.
- **Indicadores (Flags 6 bits):** Son bits de control individuales que sirven para gobernar el comportamiento de la conexion y coordinar los estados de sesion entre ambos extremos:
	-  **SYN (Synchronize):** Se activa durando el establecimiento de la conexion para sincronizar los numeros de secuencia iniciales (ISN)
	- **ACK (Acknowledgement):** Indica que el campo "Numero de confirmacion" contiene informacion valida de acuse de recibo.
	- **FIN (Finish):** Indica que el emisor ha terminado de enviar datos y solicita el inicio del cierre de la conexion.
	- **RST (Reset):** Fuerza el reinicio inmediato de la conexion debido a la deteccion de errores graves o desincronizacion.
	- **PSH (Push):** Activa la funcion de forzado de datos, ordenando a TCP transmitir los datos acumulados de inmediato hacia el usuario final sin esperar mas segmentos.
	- **URG (Urgent):** Señala que el segmento transporta datos urgentes o prioritarios.
- **Ventana (Window 16 bits)**: Implementa el control de flujo dinamico de extremo a extremo mediante el esquema de creditos de TCP
- **Suma de verificacion (Checksum 16 bits)**: Proporciona un mecanismo robusto de deteccion de errores de bits en la transmision.
- **Puntero Urgente (16 bits)**: Valido unicamente si el flag URG esta activo. Este valor suma al numero de secuencia del segmento para señalar con precision el numero de secuencia del ultimo octeto que compone la secuencia de datos urgentes en transito.
-  **Reservado (3 o 4 bits):** Sirve para su uso futuro. Se dejo alli previendo que, si en el futuro el protocolo TCP necesitaba actualizarse con nuevas caracteristicas, hubiera espacio disponible.
- **Opciones:** Facilitan la negociacion de parametros adicionales no obligatorios en el estandar basico.
   


c)
**AN (Acknowledgement Number):** Significa Numero de confirmacion, es un campo de 32 bits de longitud ubicado de manera fija en la cabecera de todos los segmentos TCP.
**Octeto:** Grupo de 8 bits, tecnicamente lo mismo que un byte, pero en la computacion antigua los bytes podian ser de 7bits o 9bits, entonces un octeto siempre representa 8 bits.

**Three way handshake (Establecimiento de la conexion):** El objetivo de este mecanismo es garantizar que ambas entidades se aseguren de que la otra existe, negocien parametros opcionales y sincronicen sus numeros de secuencia iniciales (ISN) para evitar confusiones con conexiones anteriores.

- **Paso 1 (SYN):** El emisor (A) inicia la conexión enviando un segmento de control especial denominado SYN con su número de secuencia inicial, denotado como i.
- **Paso 2 (SYN/ACK):** El receptor (B) recibe el SYN y responde enviando un segmento con los indicadores SYN y ACK activos. Este mensaje cumple una doble función: confirma la recepción del SYN del emisor esperando el octeto i+1  (mediante el número de confirmación AN = i + 1) y propone su propio número de secuencia inicial para su sentido de transmisión, denotado como j.
- **Paso 3 (ACK):** El emisor (A) confirma el SYN/ACK del receptor enviando un segmento final con el indicador ACK activo que referencia el número de secuencia esperado por el receptor (i + 1) y confirma el ISN de este último (AN = j + 1)
Tras este intercambio, la conexion pasa al estado establecida y queda abierta la asociacion logica temporal de forma bidireccional y fiable.

**Four way handshake (Cierre de la conexion):** Dado que TCP permite el flujo de datos simultaneo en ambos sentidos, cada extremo de la transmision debe cerrar su via de datos de forma independiente y coordinada para asegurar que no se pierda ninguna informacion que viaje con retraso por la red. El cierre ordenado se hace asi:

- **Paso 1 (FINAL de A):** Cuando el emisor de (A) no tiene mas datos que transmitir, su aplicacion solicita el cierre, lo que provoca el envio de un segmento FIN (i) al receptor. A partir de este momento, A entra en estado de espera (FIN WAIT).
- **Paso 2 (ACK de B):** El receptor (B) recibe el segmento FIN de A y le devuelve una confirmación ACK (AN = i + 1). En este instante, la vía de datos de A hacia B queda cerrada, pero B entra en el estado _CLOSE WAIT_, lo que significa que B aún puede continuar transmitiendo datos pendientes hacia A si su aplicación lo requiere, y A debe seguir aceptándolos
- **Paso 3 (FIN de B):** Una vez que el receptor (B) termina de enviar todos sus datos acumulados y decide que es momento de cerrar su sentido de transmision, envia su propio segmento de control FIN (j) hacia A.
- **Paso 4 (ACK de A):** El emisor (A) recibe el segmento FIN de B y responde enviando un segmento ACK de confirmacion final (AN = j +1)


d)

![[Pasted image 20260904153118.png|574]]

e)
![[Pasted image 20260904153634.png|700]]

![[Pasted image 20260904154159.png]]

f) Llegamos a la conclusion de que es bastante inseguro usar un Wi-Fi publico de cualquier sitio. Cualquier persona podria estar usando wireshark y viendo todas las cosas que estoy mandando asi como nosotros vimos los paquetes que mandamos.