## Recuperación de un mensaje con paridad bidimensional

---

> **Nota** Durante la clase capturamos y resolvimos el **Payload 2** (`SIZE 10,6`): lo armamos en la matriz, calculamos las paridades, ubicamos los errores y reconstruimos el mensaje. Los **Payloads 1 y 3** los resolvimos después de clase, con el mismo procedimiento.
> 
> No guardamos fotos ni capturas de pantalla de la configuración de red que usamos en el laboratorio (IP, máscara, puertos), y tampoco conservamos el archivo `.pcapng`. Por eso en las secciones 1 y 2 completamos solo lo que se puede afirmar con lo que sí registramos (el filtro usado y el contenido del paquete) y explicamos el procedimiento para el resto.
> 
> Seguimos el paso a paso de la guía y dejamos al final las respuestas a las reflexiones.

### 1. Averigüen su IP y su máscara (ipconfig / ip addr) y calculen la dirección de broadcast de la red. ¿Cuál es la dirección MAC de broadcast?

|Dato|Valor|
|---|---|
|IP de la computadora|No registrada (asignada por DHCP en la red del laboratorio)|
|Máscara de subred|No registrada|
|Dirección de broadcast|No registrada|
|MAC de broadcast|`FF:FF:FF:FF:FF:FF`|
|Filtro usado en Wireshark|`udp && eth.addr == ff:ff:ff:ff:ff:ff`|

**Cálculo del broadcast (procedimiento).** La dirección de broadcast se obtiene poniendo en 1 todos los bits de host de la IP; es decir, `broadcast = IP OR (NOT máscara)`. Por ejemplo, con `192.168.1.37/24`: la red es `192.168.1.0` y el broadcast es `192.168.1.255`.

La **MAC de broadcast** es siempre `FF:FF:FF:FF:FF:FF` (48 bits en 1): una trama con esa dirección de destino la reciben y procesan todas las placas del mismo dominio de difusión. Por eso el filtro `eth.addr == ff:ff:ff:ff:ff:ff` alcanzó para aislar el mensaje de la cátedra.

### 2. Capturar al menos 2 minutos con Wireshark

|Campo|Valor|
|---|---|
|Protocolo de transporte|**UDP**: el paquete apareció con el filtro `udp`. Tiene sentido, porque TCP es orientado a conexión y no admite difusión|
|IP de origen|No registrada|
|IP de destino|La dirección de broadcast de la red (no registrada)|
|Puertos de origen y destino|No registrados|
|Contenido|`5Ei.{"SIZE": "10,6", "PL": "...", "CHECK": "..."}`|

**Sobre el prefijo `5Ei.`.** El JSON empieza en el carácter `{`. Los cuatro caracteres anteriores no forman parte del mensaje: son bytes que quedaron en la selección al copiar el paquete como texto ASCII. Wireshark muestra los bytes imprimibles como su carácter y los no imprimibles como `.`. Sin el `.pcapng` no podemos confirmar a qué campo del encabezado corresponden.

### 3. Analizar la estructura del mensaje

La carga útil es un JSON con tres campos:

|Campo|Significado|
|---|---|
|`SIZE`|Tamaño de la matriz en formato `FILAS,COLUMNAS`. Cada columna es un **carácter** de 7 bits.|
|`PL`|Payload: `FILAS × COLUMNAS × 7` bits, escritos como texto de `0` y `1`.|
|`CHECK`|Bits de control: primero `FILAS` bits de paridad de fila (arriba → abajo) y luego `COLUMNAS × 7` bits de paridad de columna (izquierda → derecha).|

Por ejemplo, para `SIZE = 10,6`: `PL` tiene 10 × 6 × 7 = 420 bits (10 filas de 42 bits) y `CHECK` tiene 10 + 42 = 52 bits.

```json
{"SIZE": "10,6", "PL": "1111000...", "CHECK": "1000000100..."}
```

**Cómo interpretarlo:** el `PL` se parte en bloques **consecutivos** de `COLUMNAS × 7` bits (una fila cada uno), se calcula la paridad par de cada fila y de cada columna y se compara con el `CHECK`.

### 4, 5 y 6. Verificar el mensaje, corregir los errores y reconstruir

Procedimiento aplicado a cada payload:

- Ordenar el `PL` en filas y columnas.
- Calcular la paridad de filas y columnas (`paridad.py`).
- Comparar con el `CHECK` y registrar el síndrome (filas y columnas que fallan).
- Obtener las matrices candidatas que explican las discrepancias.
- Descartar las candidatas que vuelvan a romper la paridad.
- Si todas rompen la paridad en otro lugar, el error estaba en el `CHECK`.

#### Payload 1 (resuelto después de clase)

```JSON
{"SIZE": "8,7","PL": "11010001110100111010011100001110011011101001011110101111111100111011111110101111010011101011100010110010101011101100011110111111011010101111111001111010001101111111001011101001110011010111111100010111000111011111001111001011111101010010101110111101000011000010100100011111111001101100101110000111101001110101111001010001010111101111001111010001100001111001011001010100000010000001000000100000", "CHECK": "011111010110111111110110011100101111001100001100110010001"}
```

Matriz recibida:

```text
1101000111010011101001110000111001101110100101111  https:/
0101111111100111011111110101111010011101011100010  /youtub
1100101010111011000111101111110110101011111110011  e.com/s
1101000110111111100101110100111001101011111110001  horts/q
0111000111011111001111001011111101010010101110111  8wgKzJw
1010000110000101001000111111110011011001011100001  Pa$?fea
1110100111010111100101000101011110111100111101000  turE=sh
1100001111001011001010100000010000001000000100000  are
```

Al procesarla con `paridad.py`:

```text
1101000111010011101001110000111001101110100101111 |0
0101111111100111011111110101111010011101011100010 |1
1100101010111011000111101111110110101011111110011 |1
1101000110111111100101110100111001101011111110001 |1
0111000111011111001111001011111101010010101110111 |0
1010000110000101001000111111110011011001011100001 |0
1110100111010111100101000101011110111100111101000 |1
1100001111001011001010100000010000001000000100000 |1
---------------------------------------------------
0110111101110110111100001111001100001100110010001
```

Comparación con el `CHECK`:

- Filas

```
  Calculado : 01110011
  Check     : 01111101
                  ^^^
          [fallan las filas 5, 6 y 7]
```

- Columnas

```
 Calculado : 0110111101110110111100001111001100001100110010001
 Check     : 0110111111110110011100101111001100001100110010001
                     ^       ^     ^
             [fallan las columnas 9, 17 y 23]
```

Hay 3 filas y 3 columnas en falla, así que hay 3! = 6 formas de emparejarlas (6 matrices candidatas), y las 6 cierran la paridad. Probamos primero el emparejamiento en orden (fila 5 con columna 9, fila 6 con columna 17 y fila 7 con columna 23):

|Fila|Columna|Bit recibido|Bit corregido|Carácter recibido|Carácter corregido|
|---|---|---|---|---|---|
|5|9|1|0|`w`|`W`|
|6|17|0|1|`$`|`4`|
|7|23|0|1|`E`|`e`|

```text
1101000111010011101001110000111001101110100101111
0101111111100111011111110101111010011101011100010
1100101010111011000111101111110110101011111110011
1101000110111111100101110100111001101011111110001
0111000101011111001111001011111101010010101110111
1010000110000101101000111111110011011001011100001
1110100111010111100101100101011110111100111101000
1100001111001011001010100000010000001000000100000
```

Su decodificación es:

```
https:/
/youtub
e.com/s
horts/q
8WgKzJw
Pa4?fea
ture=sh
are
```

Mensaje: `https://youtube.com/shorts/q8WgKzJwPa4?feature=share`

Este emparejamiento da un texto coherente (`ture`, en lugar de `turE`, y una URL válida). Igual hay que aclarar que la paridad sola no distingue entre las 6 candidatas: lo que decide es el contenido. Las otras cinco dejan un `$` dentro del identificador del video (los identificadores de YouTube solo usan letras, números, `-` y `_`) o rompen `?feature`. Por ejemplo, la candidata (5,17), (6,9), (7,23) da `q8wwKzJwPA$?feature=share`.

#### Payload 2 (resuelto en clase)

```json
{"SIZE": "10,6", "PL": "111100011101001110100111000011100110111010010111101011111111001110111111101011110100111010111000101100101010111011000111101111110110101011111110011110100011011111110010111010011101110101111101011110000111101001011010111010001111101011000110001011110001111000110010010111111110011011001011100001111010011101011110010110110101111011110011110100011000011110010110010101000000100000010000001000000100000010000001000000100000", "CHECK": "1000000100101001111100001011110111100110101001011001"}
```

**Primer intento en clase.** Le pedimos a una IA que acomodara el `PL` en la matriz y la paridad no coincidía con el `CHECK`. El problema era que esa matriz no reproducía fielmente el `PL`: las filas 4 a 8 tenían bits corridos (algunas de 43 bits), así que cualquier paridad calculada sobre ella era inválida. Aprendimos que la fuente de verdad es el `PL` y que hay que partirlo en bloques consecutivos de 42 bits. Con el armado correcto:

Matriz recibida:

```
111100011101001110100111000011100110111010   xttps:
010111101011111111001110111111101011110100   //yout
111010111000101100101010111011000111101111   ube.co
110110101011111110011110100011011111110010   m/shor
111010011101110101111101011110000111101001   tw/WCi
011010111010001111101011000110001011110001   5h}1Eq
111000110010010111111110011011001011100001   qI?fea
111010011101011110010110110101111011110011   turm=s
110100011000011110010110010101000000100000   hare
010000001000000100000010000001000000100000   (relleno)
```

Al procesarla con `paridad.py`:

```
111100011101001110100111000011100110111010 |0
010111101011111111001110111111101011110100 |0
111010111000101100101010111011000111101111 |0
110110101011111110011110100011011111110010 |0
111010011101110101111101011110000111101001 |1
011010111010001111101011000110001011110001 |1
111000110010010111111110011011001011100001 |0
111010011101011110010110110101111011110011 |0
110100011000011110010110010101000000100000 |0
010000001000000100000010000001000000100000 |0
--------------------------------------------
100001111101001010110111000110101001011001
```

Comparación con el `CHECK`:

- Filas

```
  Calculado : 0000110000
  Check     : 1000000100
              ^   ^^ ^
             [fallan las filas 1, 5, 6 y 8]
```

- Columnas

```
 Calculado : 100001111101001010110111000110101001011001
 Check     : 101001111100001011110111100110101001011001
               ^        ^     ^      ^
             [fallan las columnas 3, 12, 18 y 25]
```

Hay 4! = 24 emparejamientos posibles. Al decodificar cada fila como 6 caracteres ASCII se ve qué columna corresponde a cada fila, porque solo una elección produce un carácter con sentido en cada caso:

|Fila|Columna|Bit recibido|Bit corregido|Carácter recibido|Carácter corregido|
|---|---|---|---|---|---|
|1|3|1|0|`x`|`h`|
|5|12|1|0|`w`|`s`|
|6|18|1|0|`}`|`u`|
|8|25|1|0|`m`|`e`|

Matriz corregida con su paridad:

```
110100011101001110100111000011100110111010 |1   https:
010111101011111111001110111111101011110100 |0   //yout
111010111000101100101010111011000111101111 |0   ube.co
110110101011111110011110100011011111110010 |0   m/shor
111010011100110101111101011110000111101001 |0   ts/WCi
011010111010001110101011000110001011110001 |0   5hu1Eq
111000110010010111111110011011001011100001 |0   qI?fea
111010011101011110010110010101111011110011 |1   ture=s
110100011000011110010110010101000000100000 |0   hare
010000001000000100000010000001000000100000 |0   (relleno)
--------------------------------------------
101001111100001011110111100110101001011001
```

Verificación: ya no hay discrepancias.

- Filas

```
  Calculado : 1000000100
  Check     : 1000000100
```

- Columnas

```
 Calculado : 101001111100001011110111100110101001011001
 Check     : 101001111100001011110111100110101001011001
```

Mensaje recuperado (las últimas posiciones son espacios de relleno, `0100000`):

```
https://youtube.com/shorts/WCi5hu1EqqI?feature=share
```

#### Payload 3 (resuelto después de clase)

```json
{"SIZE": "4,4", "PL": "1010001111001001100111101101110100101110000100001011101001010010110001111000001011011100100100100111001111011010", "CHECK": "10001110100011101010001110100000"}
```

Matriz recibida:

```
1010001111001001100111101101   Qr3m
1101001011100001000010111010   i8!:
0101001011000111100000101101   )1p-
1100100100100111001111011010   dIgZ
```

Su paridad es:

```
1010001111001001100111101101 |0
1101001011100001000010111010 |1
0101001011000111100000101101 |1
1100100100100111001111011010 |1
------------------------------
1110101011001000001010100000
```

Comparación con el `CHECK`:

- Filas

```
  Calculado : 0111
  Check     : 1000
              ^^^^
            [fallan las filas 1, 2, 3 y 4]
```

- Columnas

```
 Calculado : 1110101011001000001010100000
 Check     : 1110100011101010001110100000
                   ^   ^   ^    ^
             [fallan las columnas 7, 11, 15 y 20]
```

##### Las 24 matrices candidatas

Cada fila se corrige invirtiendo el bit de la columna que le toca. Como hay 4 filas y 4 columnas en falla, se generan `4! = 24` matrices; **las 24 vuelven a dar la paridad del `CHECK`**, así que la paridad no alcanza para decidir.

|#|Errores|Decodificación|¿Texto coherente?|
|---|---|---|---|
|1|1°(1,7); 2°(2,11); 3°(3,15); 4°(4,20)|`Pr3mi0!:)10-dIeZ`|**Sí**: se puede leer como _Pr3mi0!_ (¡Premio!) `:)` 10-dIeZ|
|2|1°(1,7); 2°(2,11); 3°(3,20); 4°(4,15)|`Pr3mi0!:)1r-dI'Z`|No|
|3|1°(1,7); 2°(2,15); 3°(3,11); 4°(4,20)|`Pr3mi8a:)9p-dIeZ`|No|
|4|1°(1,7); 2°(2,15); 3°(3,20); 4°(4,11)|`Pr3mi8a:)1r-dAgZ`|No|
|5|1°(1,7); 2°(2,20); 3°(3,11); 4°(4,15)|`Pr3mi8#:)9p-dI'Z`|No|
|6|1°(1,7); 2°(2,20); 3°(3,15); 4°(4,11)|`Pr3mi8#:)10-dAgZ`|No|
|7|1°(1,11); 2°(2,7); 3°(3,15); 4°(4,20)|`Qz3mh8!:)10-dIeZ`|No|
|8|1°(1,11); 2°(2,7); 3°(3,20); 4°(4,15)|`Qz3mh8!:)1r-dI'Z`|No|
|9|1°(1,11); 2°(2,15); 3°(3,7); 4°(4,20)|`Qz3mi8a:(1p-dIeZ`|No|
|10|1°(1,11); 2°(2,15); 3°(3,20); 4°(4,7)|`Qz3mi8a:)1r-eIgZ`|No|
|11|1°(1,11); 2°(2,20); 3°(3,7); 4°(4,15)|`Qz3mi8#:(1p-dI'Z`|No|
|12|1°(1,11); 2°(2,20); 3°(3,15); 4°(4,7)|`Qz3mi8#:)10-eIgZ`|No|
|13|1°(1,15); 2°(2,7); 3°(3,11); 4°(4,20)|`Qrsmh8!:)9p-dIeZ`|No|
|14|1°(1,15); 2°(2,7); 3°(3,20); 4°(4,11)|`Qrsmh8!:)1r-dAgZ`|No|
|15|1°(1,15); 2°(2,11); 3°(3,7); 4°(4,20)|`Qrsmi0!:(1p-dIeZ`|No|
|16|1°(1,15); 2°(2,11); 3°(3,20); 4°(4,7)|`Qrsmi0!:)1r-eIgZ`|No|
|17|1°(1,15); 2°(2,20); 3°(3,7); 4°(4,11)|`Qrsmi8#:(1p-dAgZ`|No|
|18|1°(1,15); 2°(2,20); 3°(3,11); 4°(4,7)|`Qrsmi8#:)9p-eIgZ`|No|
|19|1°(1,20); 2°(2,7); 3°(3,11); 4°(4,15)|`Qr1mh8!:)9p-dI'Z`|No|
|20|1°(1,20); 2°(2,7); 3°(3,15); 4°(4,11)|`Qr1mh8!:)10-dAgZ`|No|
|21|1°(1,20); 2°(2,11); 3°(3,7); 4°(4,15)|`Qr1mi0!:(1p-dI'Z`|No|
|22|1°(1,20); 2°(2,11); 3°(3,15); 4°(4,7)|`Qr1mi0!:)10-eIgZ`|No|
|23|1°(1,20); 2°(2,15); 3°(3,7); 4°(4,11)|`Qr1mi8a:(1p-dAgZ`|No|
|24|1°(1,20); 2°(2,15); 3°(3,11); 4°(4,7)|`Qr1mi8a:)9p-eIgZ`|No|

Detalle de la candidata 1 (en los cuatro casos el bit recibido es 1 y el corregido es 0):

|Fila|Columna|Carácter recibido|Carácter corregido|
|---|---|---|---|
|1|7|`Q`|`P`|
|2|11|`8`|`0`|
|3|15|`p`|`0`|
|4|20|`g`|`e`|

#### Síntesis

|Mensaje|Dónde se resolvió|`SIZE`|Síndrome|Correcciones|Estado|Contenido|
|---|---|---|---|---|---|---|
|Payload 1|Después de clase|`8,7`|filas 5, 6, 7; cols 9, 17, 23|3 bits|Recuperado|URL de YouTube|
|Payload 2|**En clase**|`10,6`|filas 1, 5, 6, 8; cols 3, 12, 18, 25|4 bits|Recuperado|URL de YouTube|
|Payload 3|Después de clase|`4,4`|todas las filas; cols 7, 11, 15, 20|4 bits → 24 candidatas|Ambiguo: la paridad no decide|`Pr3mi0!:)10-dIeZ` (la más plausible)|

---

# Reflexiones e investigación

### Reflexión 1. Errores en dos bits y bits de control

#### Errores en dos bits de filas y columnas distintas

La comprobación de paridad falla en 2 filas y en 2 columnas. Al cruzarlas se forman 4 intersecciones posibles (los vértices de un rectángulo dentro de la matriz). El receptor **detecta** que hubo errores, pero no puede **corregirlos** con certeza: tanto los dos bits de una diagonal como los de la otra explican el mismo síndrome, y elegir mal agrega dos errores nuevos. Es la misma situación de los Payloads 1, 2 y 3, a mayor escala: con _k_ filas y _k_ columnas en falla hay _k!_ emparejamientos que cierran la paridad, y lo único que permitió decidir fue el contenido del texto.

Hay dos casos relacionados que conviene mencionar:

- Si los dos errores están **en la misma fila**, la paridad de esa fila vuelve a cerrar y solo fallan 2 columnas; se detecta el error, pero no se sabe en qué fila está.
- Si 4 errores forman exactamente un **rectángulo**, todas las paridades cierran y el error **no se detecta**.

#### Si se daña un bit de control (bit de paridad)

Falla únicamente 1 fila (si el bit dañado es de paridad de fila) o 1 columna (si es de paridad de columna), y el otro eje no muestra ningún fallo. Un error en un bit de datos siempre hace fallar una fila **y** una columna a la vez, así que este patrón "huérfano" indica que el dañado es el bit de control. La matriz de datos está intacta y se puede usar tal como llegó; el bit de control se corrige (o se descarta) sin tocar los datos.

### Reflexión 2. "Leer y adivinar" vs. código

#### ¿Sirve adivinar por contexto para información crítica?

No. Las contraseñas, los números de cuenta, las direcciones IP o URL y las claves criptográficas no tienen redundancia semántica ni contexto gramatical. Cambiar un solo bit en un número de cuenta cambia su valor o su destino, y no hay forma de deducir el contenido original por contexto. Los propios mensajes del laboratorio lo muestran: en `https://youtube.com/shorts/WCi5hu1EqqI` el identificador del video (`WCi5hu1EqqI`) es una secuencia arbitraria. Si `u` se convierte en `}` se nota, pero si una letra se convierte en otra letra válida, el link apunta a otro video (o a ninguno) y no hay contexto que lo delate.

#### ¿Qué aporta el código frente a "leer y adivinar"?

Aporta un mecanismo preciso, algorítmico y automatizable de detección y corrección de errores (FEC), independiente del significado de los datos:

- **Detecta** el error aunque el resultado "se lea bien" (por ejemplo, `$` ↔ `4` en el Payload 1).
- **Localiza** el bit erróneo (fila × columna) en lugar de suponerlo.
- **Automatiza** la corrección: las placas de red y los sistemas de comunicación pueden procesar y corregir tramas bit a bit en tiempo real, sin intervención humana ni suposiciones.

### Reflexión 3. ¿Pudieron confirmar que su corrección es correcta? ¿Cómo?

Sí para los Payloads 1 y 2, con dos verificaciones independientes:

1. **Verificación matemática (síndrome nulo).** Se recalculó la paridad de cada fila y columna sobre la matriz corregida y se comparó con el `CHECK`: en ambos casos coinciden todos los bits de control (ver la matriz final del Payload 2).
2. **Verificación del contenido.** Con `decodificar_mensaje.py` se pasó la matriz corregida a texto ASCII y se comprobó que el resultado es coherente: una URL bien formada.

La guía advierte que _un mensaje que "se lee bien" no es necesariamente correcto_, y el Payload 3 lo muestra: las 24 candidatas cierran la paridad y varias "se leen" razonablemente. Ahí la paridad no puede confirmar nada y solo queda elegir la candidata más plausible; no se puede asegurar que sea la correcta. Lo mismo vale, en menor medida, para los Payloads 1 y 2: con más de un error, la paridad bidimensional deja varias candidatas y la confirmación final depende del contenido.

### Reflexión 4. Hamming (7,4)

#### Cómo funciona

El código **Hamming (7,4)** trabaja con bloques de **7 bits**: 4 son datos y 3 son bits de paridad. A diferencia de la paridad bidimensional, donde las paridades van al final de filas y columnas, Hamming ubica los bits de control en las posiciones que son **potencias de dos** (1, 2 y 4) y los datos en las restantes (3, 5, 6 y 7):

|Posición|1|2|3|4|5|6|7|
|---|---|---|---|---|---|---|---|
|Contenido|p1|p2|d1|p3|d2|d3|d4|

Cada bit de paridad controla las posiciones cuyo número en binario tiene un 1 en "su" bit:

- **p1** (bit 0) controla las posiciones 1, 3, 5, 7 → `p1 = d1 ⊕ d2 ⊕ d4`
- **p2** (bit 1) controla las posiciones 2, 3, 6, 7 → `p2 = d1 ⊕ d3 ⊕ d4`
- **p3** (bit 2) controla las posiciones 4, 5, 6, 7 → `p3 = d2 ⊕ d3 ⊕ d4`

Al recibir el bloque, el receptor recalcula las tres paridades sobre sus posiciones. Los resultados forman un número binario de 3 bits, el **síndrome** `s = s3 s2 s1`:

- Si `s = 000`, no se detectaron errores.
- Si `s ≠ 000`, su valor en decimal es **exactamente la posición** del bit alterado (de 1 a 7), suponiendo un único error. Se invierte ese bit y se recupera el bloque.

Funciona porque cada posición tiene un número binario distinto: un error en la posición 6 (`110`) rompe p2 y p3 pero no p1, y el síndrome resultante es `110` = 6.

**Ejemplo.** El primer bloque de datos del Payload 2 es `1101` (d1 = 1, d2 = 1, d3 = 0, d4 = 1):

- `p1 = 1⊕1⊕1 = 1`, `p2 = 1⊕0⊕1 = 0`, `p3 = 1⊕0⊕1 = 0`
- Palabra transmitida: `1 0 1 0 1 0 1` → `1010101`
- Si llega con la posición 3 invertida, `1000101`: el síndrome vale s1 = 1, s2 = 1, s3 = 0 → `011` = 3. Se invierte la posición 3 y se recupera `1010101`, cuyos datos son `1101`.

#### Por qué es superior a la paridad bidimensional del laboratorio

- **Corrige sin ambigüedad.** La paridad bidimensional solo localiza con certeza **un** error en toda la matriz. Con 2 o más errores aparecen _k!_ candidatas (6 en el Payload 1, 24 en los Payloads 2 y 3) y hay que "leer y adivinar", justo lo que el código debía evitar. Hamming corrige **un error por bloque de 7 bits**, así que si los errores caen en bloques distintos los corrige todos de forma automática y sin mirar el contenido.
- **Es local y rápido.** Cada bloque se decodifica apenas llegan sus 7 bits, con 3 XOR; no hace falta recibir la matriz completa ni el `CHECK` del final. Es fácil de implementar en hardware.
- **Protege a los propios bits de control.** Un error en p1, p2 o p3 también da un síndrome (1, 2 o 4) y se corrige igual que un error de datos.

#### Limitaciones

- **Costo en redundancia.** La eficiencia es 4/7 ≈ **57 %**. En el Payload 2, la paridad bidimensional usa 420 + 52 = 472 bits (≈ 89 % de eficiencia), mientras que Hamming (7,4) necesita 735. Hamming gana en capacidad de corrección, no en eficiencia.
- **Un solo error por bloque.** Corrige 1 bit por bloque. Con 2 errores en el mismo bloque el síndrome es distinto de cero (se nota que algo anda mal), pero apunta a una posición equivocada y el decodificador "corrige" mal, dejando 3 bits erróneos. Hamming (7,4) puede **detectar** 2 errores solo si se lo usa como detector, sin corregir. Para corregir 1 error y además detectar 2 a la vez se usa la versión extendida **Hamming (8,4) / SECDED**, que agrega un bit de paridad global.
- Con 3 o más errores en un bloque no hay garantía de detección.

#### Aplicación a la carga útil del desafío (Payload 2)

Tomamos los 420 bits ya corregidos del Payload 2 y los partimos en 105 bloques de 4 bits. Cada bloque se codifica en 7 bits, lo que da un payload de 105 × 7 = **735 bits**. El paquete que proponemos transmitir mantiene el formato JSON del laboratorio; el campo `CHECK` ya no hace falta, porque la redundancia viaja dentro de cada bloque:

```json
{"SIZE": "10,6", "CODE": "HAMMING(7,4)", "PL": "101010111010011010101100001110110100001111000000000101101100110001011000110010001111101101011111111111111100001101100111111111101101011111111001100001011001100111110000011001101010101011010001011001111000001111011001111111111100110101101011111110010110000111110110101000011000111111111110101010001011000110010111100101010100011111010101000111111100000001111101101001001011011010001011011100000010110101101001111001100110010101011111111101001001011010000110101010010010111111110010110110011001111000110011111000000011111011010000111101001010010110010010100110010100101001011011111111000011101010111010011110000000111100110011100110010010110011000000000111000011010010000000010101000000001001100000000011100001101001000000001010100000000"}
```

**Cómo lo recupera el receptor:**

1. Parte `PL` en bloques de 7 bits.
2. Calcula el síndrome de cada bloque; si es distinto de cero, invierte el bit de esa posición.
3. Extrae d1, d2, d3, d4 (posiciones 3, 5, 6 y 7), concatena los 420 bits de datos y los decodifica de a 7 bits como ASCII, igual que antes.

**Comprobación.** Simulamos que el canal daña los mismos 4 bits de datos que llegaron alterados en clase. Esos bits caen en los bloques 1, 45, 57 y 80, uno en cada bloque, así que el decodificador Hamming los corrige los cuatro automáticamente y devuelve `https://youtube.com/shorts/WCi5hu1EqqI?feature=share`. No hay candidatas que comparar ni texto que interpretar, a diferencia de lo que tuvimos que hacer con la paridad bidimensional.

## 7. Conclusiones

- El mensaje de la cátedra viajaba por **UDP a la dirección de broadcast** (MAC `FF:FF:FF:FF:FF:FF`), por lo que cualquier equipo de la red podía capturarlo con Wireshark.
- La paridad bidimensional **detecta** errores muy bien, pero solo **corrige con certeza un único error** por matriz. En los tres payloads hubo entre 3 y 4 errores, y la elección final entre las candidatas dependió de leer el texto. En el Payload 3 esto no alcanzó para decidir con seguridad.
- Armar bien la matriz es tan importante como calcular la paridad: en clase el primer intento falló porque la matriz no respetaba el `PL`.
- Para datos sin redundancia semántica (URLs, claves, números) "leer y adivinar" no sirve; hace falta un código que localice los errores. **Hamming (7,4)** lo logra bloque a bloque y corrige errores repartidos sin ambigüedad, a cambio de más bits de redundancia.