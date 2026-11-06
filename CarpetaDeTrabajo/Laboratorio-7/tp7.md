# Trabajo Práctico N°7
## Recuperación de un mensaje con paridad bidimensional
---
> **Nota**  
> Como durante el transcurso del TP no logramos calcular las paridadades y reconstruir el mensaje original, proponemos la solución a los tres posibles mensajes recibidos. Continuamos a responder el paso a paso de la guía que está en el TP dejando al final las respuestas a las reflexiones. 

### 1. Averigüen su IP y su máscara (ipconfig / ip addr) y calculen la dirección de broadcast de la red. ¿Cuál es la dirección MAC de broadcast?

[TODO: completar con la salida de `ipconfig /all` o `ip addr`.]

| Dato | Valor |
|---|---|
| Interfaz Wi-Fi | [COMPLETAR] |
| IP de la computadora | [COMPLETAR] |
| Máscara de subred | [COMPLETAR] |
| Dirección de red | [COMPLETAR] |
| Dirección de broadcast | [COMPLETAR] |
| MAC de la computadora | [COMPLETAR] |
| MAC de broadcast | `FF:FF:FF:FF:FF:FF` |
| Archivo de captura | [COMPLETAR: `captura.pcapng`] |
| Filtro usado en Wireshark | `udp && eth.addr == ff:ff:ff:ff:ff:ff` |

**Cálculo del broadcast.** [TODO: explicar el cálculo a partir de la IP y la máscara.
Ejemplo: `192.168.1.37/24` → red `192.168.1.0`, broadcast `192.168.1.255`.]

### 2. Capturar al menos 2 minutos de wireshak 

Necesito captura de wireshark para completar:
| Campo | Valor |
|---|---|
| Protocolo de transporte | [CONFIRMAR] |
| IP de origen | [COMPLETAR] |
| IP de destino | [COMPLETAR: broadcast de la red] |
| Puerto de origen | [COMPLETAR] |
| Puerto de destino | [COMPLETAR] |
| Prefijo antes del JSON | `5Ei.` [TODO: explicar qué es] |

> **Nota:** en la captura analizada el contenido útil aparece como `5Ei.{"SIZE": ...}`.
> Hay que documentar qué representan esos cuatro caracteres (`5Ei.`) y a partir de qué
> byte empieza el JSON.

### 3. Analizar la estructura del mensaje

La carga útil es un JSON con tres campos:

| Campo | Significado |
|---|---|
| `SIZE` | Tamaño de la matriz en formato `FILAS,COLUMNAS`. Cada columna es un **carácter** de 7 bits. |
| `PL` | Payload: `FILAS × COLUMNAS × 7` bits, escritos como texto de `0` y `1`. |
| `CHECK` | Bits de control: primero `FILAS` bits de paridad de fila (arriba → abajo) y luego `COLUMNAS × 7` bits de paridad de columna (izquierda → derecha). |

Como por ejemplo:

```json
{"SIZE": "10,6", "PL": "1111000...", "CHECK": "1000000100..."}
```

### 4 , 5 y 6 Verificar mensaje, corrección de errores y recontrucción.
Pasemos a desarrollar cada payload: 
  - Aplicar ordenamiento en filas/columnas
  - Calcular paridad filas/columnas
  - Comparar con el check
  - Obtener todas la posible matrices que son solución de las discrepancias 
  - Descartar matrices candidatas que vuelvan a romper la paridad.
  - Si todas rompen la paridad en alguna otra locación, estaba mal el check.

#### Payload 1. 

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

Al procesarlo mediante `paridad.py`
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

Ahora comparamos con el check.
- Filas
```
  Calculado : 01110011
  Check     : 01111101
                  ^^^
          [marcas en pos 5, 6 y 7]              
```

- Columnas  
 ```
  Calculado : 0110111101110110111100001111001100001100110010001
  Check     : 0110111111110110011100101111001100001100110010001
                      ^       ^     ^
              [marcas en pos 9, 17 y 23]
 ```

Ahora tenemos matrices que pueden llegar a ser la solución, llamemosle matrices candidatas. Por ejemplo, convenientemente, si para la fila 5 usamos el error en la columna 9, fila 6 con la columan 17 y fila 7 con la columna 23 obtenemos la siguiente matriz

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
cuya decodificación es: 

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
Donde da la casualidad que es la solución correcta y no tenemos que seguir intentando con las demas combinaciones, pero no necesariamente teine que ser asi, obviamente es probable que las otras combinaciones rompan igualmente la paridad, en tal caso se descarta pero a fines prácticos es mas eficiente decodificar y revisar que sea una solución coherente. 

### Paylod 2 

```json
{"SIZE": "10,6", "PL": "111100011101001110100111000011100110111010010111101011111111001110111111101011110100111010111000101100101010111011000111101111110110101011111110011110100011011111110010111010011101110101111101011110000111101001011010111010001111101011000110001011110001111000110010010111111110011011001011100001111010011101011110010110110101111011110011110100011000011110010110010101000000100000010000001000000100000010000001000000100000", "CHECK": "1000000100101001111100001011110111100110101001011001"}

```
Matriz recibida: 
```
111100011101001110100111000011100110111010
010111101011111111001110111111101011110100
111010111000101100101010111011000111101111
110110101011111110011110100011011111110010
111010011101110101111101011110000111101001
011010111010001111101011000110001011110001
111000110010010111111110011011001011100001
111010011101011110010110110101111011110011
110100011000011110010110010101000000100000
010000001000000100000010000001000000100000
```

Al procesarla mediante `paridad.py`: 

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

Ahora la comparamos con el check: 
- Filas:
```
  Calculado : 1000000100
  Check     : 0000110000
              ^   ^^ ^ 
             [Marcas en 1, 5, 6 y 8]              
```

- Columnas  
 ```
  Calculado : 101001111100001011110111100110101001011001
  Check     : 100001111101001010110111000110101001011001
                ^        ^     ^      ^            
              [Marcas en 3, 12, 18 y 25]  
 ```

Consideremos la matris con los errores en:
(f1,c3) ; (f5,c12); (f6;c18) y (f8,c25)

obtenemos la decodificación: 
```
https:
//yout
ube.co
m/shor
ts/WCi
5hu1Eq
qI?fea
ture=s
hare 
```

Donde, observamos que es solución del mensaje (PREMIO 2). 

Igualmente se puede verificar con la matriz de paridad:

```
110100011101001110100111000011100110111010 |1
010111101011111111001110111111101011110100 |0
111010111000101100101010111011000111101111 |0
110110101011111110011110100011011111110010 |0
111010011100110101111101011110000111101001 |0
011010111010001110101011000110001011110001 |0
111000110010010111111110011011001011100001 |0
111010011101011110010110010101111011110011 |1
110100011000011110010110010101000000100000 |0
010000001000000100000010000001000000100000 |0
--------------------------------------------
101001111100001011110111100110101001011001
```
donde vemos que no hay discrepancias. 
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

### Payload 3 

```json
{"SIZE": "4,4", "PL": "1010001111001001100111101101110100101110000100001011101001010010110001111000001011011100100100100111001111011010", "CHECK": "10001110100011101010001110100000"}
``` 

Matriz recibida: 
```
1010001111001001100111101101
1101001011100001000010111010
0101001011000111100000101101
1100100100100111001111011010
```

Cuya paridad es: 
```
1010001111001001100111101101 |0
1101001011100001000010111010 |1
0101001011000111100000101101 |1
1100100100100111001111011010 |1
------------------------------
1110101011001000001010100000
```

Comparamos con el check: 
- Filas 
```
  Calculado : 0111
  Check     : 1000           
              ^^^^ 
            [Marcas en 1, 2, 3 y 4]
```
- Columnas  
 ```
  Calculado : 1110101011001000001010100000
  Check     : 1110100011101010001110100000
                    ^   ^   ^    ^                           
              [Marcas en 7, 11, 15 y 20]
 ```


##### Las 24 matrices candidatas

Cada fila se corrige invirtiendo el bit de la columna que le toca. Como hay 4 filas
y 4 columnas en falla, se generan `4! = 24` matrices; **las 24 vuelven a dar la
paridad del `CHECK`** (por eso la paridad no alcanza para decidir).

| # | Errores | Decodificación | ¿Texto coherente? |
|---|---|---|---|
| 1 | 1°(1,7); 2°(2,11); 3°(3,15); 4°(4,20) | `Pr3mi0!:)10-dIeZ` | **Sí** — Podemos interpretarlo como: *Premio* `:)` 10-Diez|
| 2 | 1°(1,7); 2°(2,11); 3°(3,20); 4°(4,15) | `Pr3mi0!:)1r-dI'Z` | No |
| 3 | 1°(1,7); 2°(2,15); 3°(3,11); 4°(4,20) | `Pr3mi8a:)9p-dIeZ` | No |
| 4 | 1°(1,7); 2°(2,15); 3°(3,20); 4°(4,11) | `Pr3mi8a:)1r-dAgZ` | No |
| 5 | 1°(1,7); 2°(2,20); 3°(3,11); 4°(4,15) | `Pr3mi8#:)9p-dI'Z` | No |
| 6 | 1°(1,7); 2°(2,20); 3°(3,15); 4°(4,11) | `Pr3mi8#:)10-dAgZ` | No |
| 7 | 1°(1,11); 2°(2,7); 3°(3,15); 4°(4,20) | `Qz3mh8!:)10-dIeZ` | No |
| 8 | 1°(1,11); 2°(2,7); 3°(3,20); 4°(4,15) | `Qz3mh8!:)1r-dI'Z` | No |
| 9 | 1°(1,11); 2°(2,15); 3°(3,7); 4°(4,20) | `Qz3mi8a:(1p-dIeZ` | No |
| 10 | 1°(1,11); 2°(2,15); 3°(3,20); 4°(4,7) | `Qz3mi8a:)1r-eIgZ` | No |
| 11 | 1°(1,11); 2°(2,20); 3°(3,7); 4°(4,15) | `Qz3mi8#:(1p-dI'Z` | No |
| 12 | 1°(1,11); 2°(2,20); 3°(3,15); 4°(4,7) | `Qz3mi8#:)10-eIgZ` | No |
| 13 | 1°(1,15); 2°(2,7); 3°(3,11); 4°(4,20) | `Qrsmh8!:)9p-dIeZ` | No |
| 14 | 1°(1,15); 2°(2,7); 3°(3,20); 4°(4,11) | `Qrsmh8!:)1r-dAgZ` | No |
| 15 | 1°(1,15); 2°(2,11); 3°(3,7); 4°(4,20) | `Qrsmi0!:(1p-dIeZ` | No |
| 16 | 1°(1,15); 2°(2,11); 3°(3,20); 4°(4,7) | `Qrsmi0!:)1r-eIgZ` | No |
| 17 | 1°(1,15); 2°(2,20); 3°(3,7); 4°(4,11) | `Qrsmi8#:(1p-dAgZ` | No |
| 18 | 1°(1,15); 2°(2,20); 3°(3,11); 4°(4,7) | `Qrsmi8#:)9p-eIgZ` | No |
| 19 | 1°(1,20); 2°(2,7); 3°(3,11); 4°(4,15) | `Qr1mh8!:)9p-dI'Z` | No |
| 20 | 1°(1,20); 2°(2,7); 3°(3,15); 4°(4,11) | `Qr1mh8!:)10-dAgZ` | No |
| 21 | 1°(1,20); 2°(2,11); 3°(3,7); 4°(4,15) | `Qr1mi0!:(1p-dI'Z` | No |
| 22 | 1°(1,20); 2°(2,11); 3°(3,15); 4°(4,7) | `Qr1mi0!:)10-eIgZ` | No |
| 23 | 1°(1,20); 2°(2,15); 3°(3,7); 4°(4,11) | `Qr1mi8a:(1p-dAgZ` | No |
| 24 | 1°(1,20); 2°(2,15); 3°(3,11); 4°(4,7) | `Qr1mi8a:)9p-eIgZ` | No |

#### Síntesis

| Mensaje | `SIZE` | Síndrome | Correcciones | Estado | Contenido |
|---|---|---|---|---|---|
| `payload1` | `8,7` | filas 5,6,7; cols 9,17,23 | 3 bits | Recuperado | URL de YouTube |
| `payload2` | `10,6` | filas 1,5,6,8; cols 3,12,18,25 | 4 bits | Recuperado | URL de YouTube |
| `payload3` | `4,4` | todas las filas; cols 7,11,15,20 | 4 bits → 24 candidatos | Ambiguo: la paridad no decide | `Pr3mi0!:)10-dIeZ` (el más plausible) |

---


# Reflexiones e investigación

### 6.1 Errores en dos bits y bits de control


### 6.2 “Leer y adivinar” vs. código

### 6.3 Diseño de un código para el paquete


### 6.4 Hamming (7,4)

---

## 7. Conclusiones

---
