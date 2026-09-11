Usando Wireshark, capturar tráfico generado por su propia computadora mientras acceden a una página web o ejecutan alguna aplicación que utilice la red (en general no hace falta hacer nada realmente, el tráfico normal de la computadora ya genera UNA BOCHA de paquetes a internet). 
a) Seleccionar una trama Ethernet e identificar las direcciones MAC de origen y destino. ¿A qué dispositivos creen que corresponden? 
b) Dentro de la misma trama, identificar el paquete IP. ¿Cuáles son las direcciones IP de origen y destino? (no importa si son versión 4 o versión 6) 
c) Comparar las direcciones MAC y las direcciones IP encontradas. ¿Representan lo mismo? 
d) Observar el campo EtherType. ¿Qué protocolo está encapsulado dentro de la trama analizada?


## 2)
![[Imagen-Wireshark.png]]



## a) Dirección Mac 
![[Imagen-Direccion-MAC.png]]
MAC Origen: 2c:98:11:60:91:bf (CloudNetwork_60:91:bf) → Placa de red de mi PC 
MAC Destino: 14:8c:4a:25:41:f2 (HuaweiTechno_25:41:f2) → Router 

Wireshark nos permite visualizarlos dado que los primeros 3 bytes de una dirección MAC identifican al fabricante, conocidos como OUI (Identificador Único de Organización). Así podemos ver que se trata de un paquete saliente, siendo el emisor físico local el adaptador de red de mi PC y el receptor local el router. 


## b) Direcciones IP
![[Imagen-direcciones-IP.png]]
P Origen: 192.168.1.16 (Src) -> IPv4 
IP Destino: 200.16.29.213 (Dst) -> IPv4


## c) Comparación entre direcciones MAC e IP
Las direcciones MAC e IP no representan lo mismo  
* Las direcciones MAC tienen alcance de tramo local (hop-by-hop) 
* Las direcciones IP tienen alcance global extremo a extremo (end-to-end) 
En este mismo ejemplo podemos observar como la IP de destino (200.16.29.213) identifica directamente al servidor web final en la red externa para viajar a través de múltiples puntos, mientras que la MAC solo identifica a mi router local.


##  d) Campo EtherType
![[Imagen-campo-EtherType.png]]
Según lo que indica el campo EtherType, el protocolo que está encapsulado dentro de la trama es IPv4 (0x0800).
