# 4) 
### a)	
En una comunicación digital, la sincronización es el requisito esencial por el cual el receptor conoce la velocidad exacta a la que se transmiten los datos para poder muestrear la línea a intervalos constantes y correctos, determinando con precisión cada bit recibido.
Sin sincronización, las diferencias de velocidad entre los relojes del emisor y del receptor (deriva de reloj) provocarían errores de lectura de bits de forma acumulativa.

Sincronización de bits: Consiste en determinar la temporización de cada bit individual (su velocidad, duración y separación) para que el receptor pueda muestrear el medio físico exactamente en el instante central de cada intervalo de bit
Esto evita errores de interpretación de si el bit es un '0' o un '1'.

Sincronización de trama: Se sitúa a un nivel jerárquico superior y consiste en permitir que el receptor identifique de manera inequívoca el comienzo y el final de un bloque completo de datos (la trama)

### b) 
#### Una trama (frame) es la unidad de datos básica de la capa de enlace que encapsula un bloque de datos (normalmente un paquete de la capa superior como un datagrama IP) junto con información de control y delimitación necesaria para su envío a través del medio físico.

Diferencias entre sus tres partes principales:
#### Encabezado (Header): Es la sección inicial de la trama que contiene información de control indispensable para el protocolo, como direcciones físicas de origen y destino, identificadores del tipo de protocolo superior, o números de secuencia.

#### Carga útil (Payload): Es el cuerpo de datos útil que se desea transmitir; típicamente transporta el paquete de datos de la capa inmediatamente superior que se encapsuló en la trama.

#### Tráiler o Cola (Trailer): Es la sección final de la trama que se sitúa a continuación de la carga útil.


### c) 

El preámbulo es una secuencia de bytes (por ejemplo, en Ethernet consta de 7 u 8 bytes con un patrón alternante de ceros y unos como 10101010) que precede a la trama física en el canal.

Función: Su propósito principal es "despertar" a los circuitos receptores y permitir que sus relojes se sincronicen con la velocidad del reloj del emisor antes de que lleguen los datos reales.
Los últimos bits del preámbulo actúan como un delimitador de inicio que alerta al receptor de que la información útil está por comenzar. No forma parte de los datos útiles o de control lógico del mensaje del usuario, es un mecanismo auxiliar puramente físico que es interpretado y posteriormente descartado por el hardware del receptor tras lograr la sincronización de reloj.

### d) 
Métodos para determinar dónde termina una trama
Para delimitar las fronteras de una trama y saber dónde termina, los protocolos implementan diferentes mecanismos:

Longitud fija: La red o el protocolo definen un tamaño de paquete estricto e inalterable para cada unidad. Un ejemplo clásico es ATM (Asynchronous Transfer Mode), que divide el tráfico en bloques fijos denominados celdas de exactamente 53 bytes
 En este esquema, el receptor no necesita buscar un delimitador de fin; solo cuenta de forma fija los bytes recibidos para extraer cada celda

Campo que indique la longitud: La cabecera de la trama incluye un campo con un número binario que especifica explícitamente el tamaño de la trama o de la carga útil en bytes o palabras.
[Protocolos como UDP (con su campo Longitud) o IPv4 (con Longitud Total) emplean este método].

Al leer este campo en la cabecera, el receptor calcula exactamente en qué posición de bit terminará la trama actual.

Caracteres o secuencias delimitadoras (Flags/Banderas): Se define un patrón de bits único y preestablecido(un flag) para marcar los límites inicial y final de la trama. 
Para garantizar que esta secuencia no aparezca accidentalmente dentro de los datos del usuario y cause una terminación prematura, se implementa la inserción de bits (bit stuffing): el emisor introduce automáticamente un cero extra cada vez que detecta cinco unos consecutivos en los datos, y el receptor elimina este cero al procesar la trama.


Tráiler o Cola (Trailer): Es la parte final de la trama, ubicada después de la carga útil. Contiene el FCS (Frame Check Sequence), el campo donde se guarda el código de verificación de errores. Este código se genera con la técnica de CRC (Cyclic Redundancy Check), calculada por el emisor sobre el contenido de la trama (sin contar los delimitadores). El receptor repite el mismo cálculo al recibirla, y si no coincide con lo que vino en el FCS, asume que hubo un error y la descarta. Normalmente se usa un CRC de 16 bits, aunque para tramas más largas se puede usar uno de 32 bits para mayor confiabilidad. 
