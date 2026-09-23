Alcance de Redes y Virtualización 
a) Investigar cómo se clasifican las redes según su alcance. Mencionar brevemente las características principales de cada una y colocar en cada cuadro de la Figura el acrónimo de red que corresponda. 
b) ¿Qué es una vLAN? ¿Cómo se clasifican? 
c) Investigar y resumir el protocolo IEEE 802.1Q. ¿Cómo se relaciona con las VLAN? 
d) En el contexto de los dos ítems anteriores ¿Qué es el Tagging?


a) Clasificación de redes por alcance 

| Red                             | Descripción                                                                    |
| ------------------------------- | ------------------------------------------------------------------------------ |
| PAN (Personal Area Network)     | El alcance es de pocos metros, dispositivos personales, por ejemplo bluetooth, |
| LAN (Local Area Network)        | El alcance local, una oficina, una casa, todo dentro de un establecimiento.    |
| MAN (Metropolitan Area Network) | El alcance de una ciudad                                                       |
| WAN (Wide Area Network)         | El alcance es de todo un país o continente, por ejemplo el internet mismo.     |
b) La Vlan, es una red LAN pero virtual, es un dominio de broadcast logico creado por software dentro de uno o mas switches físicos, no importa la ubicación de los puertos.
Hay varios tipos:
* Por puerto: La mas comun, cada puerto del switch se le asigna una Vlan.
* Por MAC address: la VLAN sigue al dispositivo segun su MAC.
* Por protocolo
* Por subred/ip


c) El estandar IEEE 802.1Q es el que define el tagging de Vlan. Este agrega un cambo de 4 bytes al frame Ethernet (Lleva una Vlan ID de 12 bits, hasta 4094 Vlan's) para la identificación en los routers y switches a que Vlan perteneces la trama cuando viajan por un mismo enlace (trunk).

d) Tagging: es el proceso de insertar esa etiqueta 802.1Q en la trama. Se usa en los **enlaces trunk** (entre switches, o switch-router) para que un solo cable físico pueda transportar tráfico de varias VLANs distintas, distinguiendo a cuál pertenece cada trama.