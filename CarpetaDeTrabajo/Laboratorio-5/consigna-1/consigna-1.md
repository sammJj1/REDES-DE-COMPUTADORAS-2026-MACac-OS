# 1. ICMP y primer contacto con Wireshark.

#### a) ¿Qué es ICMP y para qué se usa? ¿Transporta datos de aplicaciones como lo hacen TCP o UDP?

El ICMP (Internet Connection Message Protocol) como lo dice su nombre es un protocolo. El objetivo es proporcionar un medio para trnasferir mensajes desde los dispositivos de encaminamiento y otros computadores. Proporciona  información de retroalimentación sobre los (posibles) problemas relacionados en la comunicación.  
ICMP no está involucrado en el trnasporte de datos activamente como TCP o UDP, está involucrado en la retroalimentación de esos datos.

#### b) ¿Qué relación tiene con IP? ¿Viaja dentro de IP, al lado de IP o debajo de IP? ¿Cómo sabe el receptor que el contenido de un paquete IP es ICMP?

Se dice que los mensajes *ICMP* son usuarios de *IP* porque se encapsulan en la cabecera de esta ultima. El receptor sabe que el contenido es un paquete ICMP por que en la cabecera existe una distinción sobre el tipo de protocolo.  
Para IPv4 los mas relevantes son: 

| Valor del campo | Protocolo | 
|   ---           |   ---     |
|  1              | ICMP      |   
|  6              |   TCP     | 
|  17             | UDP       | 

#### c) ¿Qué hace ping? ¿Qué son un Echo Request y un Echo Reply? ¿Qué campos de ICMP permiten distinguirlos?

Un `ping` es un comando que envia un conjunto de paquetes y espera activamente un *ACK*, ademas que toma el tiempo que les toma devolver el ACK.

`Echo Request` y `Echo Reply` son un tipo de mensaje ICMP usados como mecanismo para corroborar si la conexión entre dos dispositivos es posible. El receptor del *Echo Request* está obligado a responder con un mensaje *Echo Reply*, al mensaje de *Echo Request*  se le asigna un ID y un numero de secuencia que coinciden con el paquete de *Echo Reply*.  
Entonces un mensaje  ICMP tiene el siguiente formato: 

```text
0               8               16                              31
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|     Tipo      |    Código     |     Suma de comprobación      |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|         Identificador         |      Número de secuencia      |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                        Datos opcionales                       |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```