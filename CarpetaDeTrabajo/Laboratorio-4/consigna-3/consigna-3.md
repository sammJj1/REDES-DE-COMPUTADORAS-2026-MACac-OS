### a) Topología física

Se armó la siguiente topología en Packet Tracer:

- **1 Router** (2811) — `router-avion`, con dos interfaces FastEthernet en uso.
- **1 Switch** (2960) — `switch-avion`.
- **2 Servers**: uno simulando el sistema de entretenimiento de a bordo, y otro simulando el ISP / salida a Internet.
- **3 PCs**: una por cada segmento (Turista, Business, Admin).

**Conexiones:**

|Desde|Puerto|Hacia|Puerto|
|---|---|---|---|
|router-avion|Fa0/0|switch-avion|Fa0/1|
|router-avion|Fa0/1|Server-ISP|FastEthernet|
|switch-avion|Fa0/2|Server-Entretenimiento|FastEthernet|
|switch-avion|Fa0/3|PC-Turista|FastEthernet|
|switch-avion|Fa0/4|PC-Business|FastEthernet|
|switch-avion|Fa0/5|PC-Admin|FastEthernet|

El enlace router↔switch (Fa0/0 – Fa0/1) transporta las tres VLANs (10, 20 y 99) mediante un **trunk 802.1Q**, mientras que el enlace router↔Server-ISP es un enlace punto a punto independiente, sobre la red `200.0.0.0/30`.

Se utilizó como fondo del workspace una imagen de avión, replicando la disposición de clases (Turista / Business / Admin) sugerida en el enunciado.

**Diagrama de red completo (Packet Tracer):**

![[Topologia.png]]

---

### Direccionamiento IP utilizado

|Dispositivo|IP|Máscara|Gateway|
|---|---|---|---|
|PC-Turista|10.10.10.11|255.255.255.0|10.10.10.1|
|PC-Business|10.10.20.11|255.255.255.0|10.10.20.1|
|PC-Admin|10.10.99.11|255.255.255.0|10.10.99.1|
|Server-Entretenimiento|10.10.99.10|255.255.255.0|10.10.99.1|
|Server-ISP|200.0.0.2|255.255.255.252|200.0.0.1|

> **Nota:** el servidor de entretenimiento se ubicó dentro de la subred de Admin (10.10.99.0/24), conectado a un puerto access de VLAN 99 en el switch. El control de acceso de las demás clases hacia el servidor no se resuelve separándolo en su propia VLAN, sino mediante la ACL configurada en el router (ver más abajo).

---

### b) Configuración del switch

#### Creación de VLANs

```
switch-avion(config)#vlan 10
switch-avion(config-vlan)#name Turista
switch-avion(config-vlan)#vlan 20
switch-avion(config-vlan)#name Business
switch-avion(config-vlan)#vlan 99
switch-avion(config-vlan)#name Admin
switch-avion(config-vlan)#end
```

#### Asignación de puertos access

```
switch-avion(config)#interface fastEthernet 0/3
switch-avion(config-if)#switchport mode access
switch-avion(config-if)#switchport access vlan 10
switch-avion(config-if)#exit

switch-avion(config)#interface fastEthernet 0/4
switch-avion(config-if)#switchport mode access
switch-avion(config-if)#switchport access vlan 20
switch-avion(config-if)#exit

switch-avion(config)#interface fastEthernet 0/5
switch-avion(config-if)#switchport mode access
switch-avion(config-if)#switchport access vlan 99
switch-avion(config-if)#exit

switch-avion(config)#interface fastEthernet 0/2
switch-avion(config-if)#switchport mode access
switch-avion(config-if)#switchport access vlan 99
switch-avion(config-if)#exit
```

**Verificación — `show vlan brief`:**

```
VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Fa0/1, Fa0/6, Fa0/7, Fa0/8
                                                 Fa0/9, Fa0/10, Fa0/11, Fa0/12
                                                 Fa0/13, Fa0/14, Fa0/15, Fa0/16
                                                 Fa0/17, Fa0/18, Fa0/19, Fa0/20
                                                 Fa0/21, Fa0/22, Fa0/23, Fa0/24
                                                 Gig0/1, Gig0/2
10   Turista                          active    Fa0/3
20   Business                         active    Fa0/4
99   Admin                            active    Fa0/2, Fa0/5
1002 fddi-default                     active
1003 token-ring-default               active
1004 fddinet-default                  active
1005 trnet-default                    active
```

#### Configuración del enlace trunk hacia el router

```
switch-avion(config)#interface fastEthernet 0/1
switch-avion(config-if)#switchport mode trunk
switch-avion(config-if)#exit
```

**Verificación — antes de configurar el router (`show interfaces fastEthernet 0/1 switchport`):**

```
Administrative Mode: trunk
Operational Mode: down
```

> **Interpretación:** el modo administrativo ya estaba en `trunk`, pero el modo operativo permanecía `down` porque el otro extremo del enlace (el router) todavía no estaba configurado para hablar 802.1Q. Esto confirma que un trunk necesita negociación/coincidencia en ambos extremos para quedar activo.

**Verificación — después de configurar las subinterfaces del router:**

```
Administrative Mode: trunk
Operational Mode: trunk
```

> **Interpretación:** apenas el router comenzó a enviar tráfico etiquetado 802.1Q por su interfaz Fa0/0 (mediante las subinterfaces), el trunk pasó a estar operativo en ambos extremos, habilitando el transporte simultáneo de las VLANs 10, 20 y 99 por un único cable físico.

#### Configuración final consolidada — `show running-config`

```
Building configuration...

Current configuration : 1313 bytes
!
version 15.0
no service timestamps log datetime msec
no service timestamps debug datetime msec
no service password-encryption
!
hostname switch-avion
!
spanning-tree mode pvst
spanning-tree extend system-id
!
interface FastEthernet0/1
 switchport mode trunk
!
interface FastEthernet0/2
 switchport access vlan 99
 switchport mode access
!
interface FastEthernet0/3
 switchport access vlan 10
 switchport mode access
!
interface FastEthernet0/4
 switchport access vlan 20
 switchport mode access
!
interface FastEthernet0/5
 switchport access vlan 99
 switchport mode access
!
interface Vlan1
 no ip address
 shutdown
!
line con 0
!
line vty 0 4
 login
line vty 5 15
 login
!
end
```

> **Interpretación:** la configuración final del switch consolida el puerto Fa0/1 en modo trunk (hacia el router) y los puertos Fa0/2 a Fa0/5 en modo access, cada uno asignado a la VLAN correspondiente según el dispositivo conectado. Se omitieron en esta captura las interfaces sin configuración explícita (Fa0/6 a Gig0/2), que permanecen en la VLAN 1 por defecto sin uso en esta topología.

---

### c) Configuración del router

#### Interfaz física hacia el switch (sin IP propia)

```
router-avion(config)#interface fastEthernet 0/0
router-avion(config-if)#no shutdown
router-avion(config-if)#exit
```

#### Subinterfaces con encapsulación 802.1Q (una por VLAN)

```
router-avion(config)#interface fastEthernet 0/0.10
router-avion(config-subif)#encapsulation dot1Q 10
router-avion(config-subif)#ip address 10.10.10.1 255.255.255.0
router-avion(config-subif)#exit

router-avion(config)#interface fastEthernet 0/0.20
router-avion(config-subif)#encapsulation dot1Q 20
router-avion(config-subif)#ip address 10.10.20.1 255.255.255.0
router-avion(config-subif)#exit

router-avion(config)#interface fastEthernet 0/0.99
router-avion(config-subif)#encapsulation dot1Q 99
router-avion(config-subif)#ip address 10.10.99.1 255.255.255.0
router-avion(config-subif)#exit
```

> **Interpretación:** cada subinterfaz procesa únicamente el tráfico etiquetado con su VLAN ID correspondiente (comando `encapsulation dot1Q <vlan>`), actuando como el gateway de esa VLAN. Esta técnica —conocida como "router-on-a-stick"— permite rutear entre múltiples VLANs utilizando una sola interfaz física.

#### Interfaz hacia el Server-ISP

```
router-avion(config)#interface fastEthernet 0/1
router-avion(config-if)#ip address 200.0.0.1 255.255.255.252
router-avion(config-if)#no shutdown
router-avion(config-if)#exit
```

#### Ruta por defecto hacia el ISP

```
router-avion(config)#ip route 0.0.0.0 0.0.0.0 200.0.0.2
```

> **Interpretación:** esta ruta le indica al router que cualquier destino no encontrado en su tabla de rutas (por ejemplo, una IP de Internet real como 8.8.8.8) debe reenviarse hacia el Server-ISP. Sin esta ruta, el router responde con "Destination host unreachable" ante cualquier destino desconocido; con la ruta configurada, el paquete efectivamente viaja hacia el ISP y el resultado pasa a ser "Request timed out" si ese destino específico no existe en la simulación.

**Verificación — `show ip route`:**

```
Gateway of last resort is 200.0.0.2 to network 0.0.0.0

      10.0.0.0/8 is variably subnetted, 6 subnets, 2 masks
C        10.10.10.0/24 is directly connected, FastEthernet0/0.10
L        10.10.10.1/32 is directly connected, FastEthernet0/0.10
C        10.10.20.0/24 is directly connected, FastEthernet0/0.20
L        10.10.20.1/32 is directly connected, FastEthernet0/0.20
C        10.10.99.0/24 is directly connected, FastEthernet0/0.99
L        10.10.99.1/32 is directly connected, FastEthernet0/0.99
      200.0.0.0/24 is variably subnetted, 2 subnets, 2 masks
C        200.0.0.0/30 is directly connected, FastEthernet0/1
L        200.0.0.1/32 is directly connected, FastEthernet0/1
S*    0.0.0.0/0 [1/0] via 200.0.0.2
```

> **Interpretación:** la tabla de ruteo confirma las cuatro redes directamente conectadas (una por cada subinterfaz/VLAN, más el enlace al ISP), identificadas con `C` (connected) y `L` (local, la IP propia del router en esa red). La entrada `S*` marca la ruta estática por defecto (`0.0.0.0/0`) hacia `200.0.0.2`, indicada como "Gateway of last resort" — el destino al que se envía cualquier paquete que no coincida con ninguna red conocida.

---

### d) Configuración de DHCP

```
router-avion(config)#ip dhcp excluded-address 10.10.10.1 10.10.10.10
router-avion(config)#ip dhcp excluded-address 10.10.20.1 10.10.20.10
router-avion(config)#ip dhcp excluded-address 10.10.99.1 10.10.99.10

router-avion(config)#ip dhcp pool Turista
router-avion(dhcp-config)#network 10.10.10.0 255.255.255.0
router-avion(dhcp-config)#default-router 10.10.10.1
router-avion(dhcp-config)#dns-server 10.10.100.10
router-avion(dhcp-config)#exit

router-avion(config)#ip dhcp pool Business
router-avion(dhcp-config)#network 10.10.20.0 255.255.255.0
router-avion(dhcp-config)#default-router 10.10.20.1
router-avion(dhcp-config)#dns-server 8.8.8.8
router-avion(dhcp-config)#exit

router-avion(config)#ip dhcp pool Admin
router-avion(dhcp-config)#network 10.10.99.0 255.255.255.0
router-avion(dhcp-config)#default-router 10.10.99.1
router-avion(dhcp-config)#dns-server 8.8.8.8
router-avion(dhcp-config)#exit
```

**Verificación — `show ip dhcp pool`:**

```
Pool Turista :
Total addresses : 254
Leased addresses : 0
Excluded addresses : 3
Current index IP address range          Leased/Excluded/Total
10.10.10.1  10.10.10.1 - 10.10.10.254   0 / 3 / 254

Pool Business :
Total addresses : 254
Leased addresses : 0
Excluded addresses : 3
Current index IP address range          Leased/Excluded/Total
10.10.20.1  10.10.20.1 - 10.10.20.254   0 / 3 / 254

Pool Admin :
Total addresses : 254
Leased addresses : 0
Excluded addresses : 3
Current index IP address range          Leased/Excluded/Total
10.10.99.1  10.10.99.1 - 10.10.99.254   0 / 3 / 254
```

> **Interpretación:** los tres pools quedaron correctamente configurados, cada uno excluyendo las primeras 10 direcciones de su rango (reservadas para gateways, servidores e IPs estáticas). Las PCs de este TP se configuraron con IP estática para las pruebas, por lo que no se registran direcciones "leased" (arrendadas), aunque el servicio DHCP queda operativo y disponible.

---

### e) Configuración de NAT (salida a Internet solo para Business)

#### ACL estándar para definir qué tráfico se traduce

```
router-avion(config)#access-list 20 permit 10.10.20.0 0.0.0.255
```

#### Activación del NAT dinámico con sobrecarga (PAT)

```
router-avion(config)#ip nat inside source list 20 interface FastEthernet0/1 overload
```

#### Marcado de interfaces NAT inside / outside

```
router-avion(config)#interface fastEthernet 0/0.10
router-avion(config-subif)#ip nat inside
router-avion(config-subif)#exit

router-avion(config)#interface fastEthernet 0/0.20
router-avion(config-subif)#ip nat inside
router-avion(config-subif)#exit

router-avion(config)#interface fastEthernet 0/0.99
router-avion(config-subif)#ip nat inside
router-avion(config-subif)#exit

router-avion(config)#interface fastEthernet 0/1
router-avion(config-if)#ip nat outside
router-avion(config-if)#exit
```

> **Interpretación:** las tres subinterfaces se marcaron como `inside` (incluida la de Turista), ya que el NAT en sí mismo no es lo que restringe el acceso a Internet de Turista — esa restricción la impone la ACL de seguridad (ver punto f). El NAT solo traduce el tráfico que matchea la ACL 20 (únicamente el originado en 10.10.20.0/24); el tráfico de las demás VLANs simplemente nunca activa la traducción porque no cumple ese criterio.

**Verificación — `show ip nat translations` (tras un ping desde PC-Business hacia 200.0.0.2):**

```
Pro  Inside global     Inside local      Outside local     Outside global
icmp 200.0.0.1:23      10.10.20.11:23    200.0.0.2:23      200.0.0.2:23
icmp 200.0.0.1:24      10.10.20.11:24    200.0.0.2:24      200.0.0.2:24
icmp 200.0.0.1:25      10.10.20.11:25    200.0.0.2:25      200.0.0.2:25
icmp 200.0.0.1:26      10.10.20.11:26    200.0.0.2:26      200.0.0.2:26
```

> **Interpretación:** se observan 4 entradas de traducción, una por cada paquete ICMP echo del ping. La IP privada de PC-Business (`10.10.20.11`) fue traducida a la IP pública del router (`200.0.0.1`), diferenciando cada sesión por el número de puerto/ID (columna derecha de cada par). Esto confirma el funcionamiento del NAT con sobrecarga (PAT): múltiples conexiones desde la misma IP interna comparten una única IP pública, distinguidas por puerto.

---

### f) Configuración de la ACL (bloqueo de Internet a Turista)

```
router-avion(config)#access-list 100 permit ip 10.10.10.0 0.0.0.255 10.10.99.0 0.0.0.255
router-avion(config)#access-list 100 deny ip 10.10.10.0 0.0.0.255 any
router-avion(config)#access-list 100 permit ip any any
```

```
router-avion(config)#interface fastEthernet 0/0.10
router-avion(config-subif)#ip access-group 100 in
router-avion(config-subif)#exit
```

> **Interpretación:**
> 
> - La primera línea permite explícitamente el tráfico de Turista (10.10.10.0/24) hacia la red de Admin (10.10.99.0/24), donde reside el servidor de entretenimiento — esta línea debe ir primero, ya que las ACLs se procesan secuencialmente y se detienen en el primer match.
> - La segunda línea deniega cualquier otro tráfico originado en Turista, bloqueando efectivamente el acceso a Internet y a otras VLANs.
> - La tercera línea permite todo el resto del tráfico (Business, Admin, tráfico de retorno), y es obligatoria porque toda ACL tiene un `deny all` implícito al final; sin esta línea se bloquearía también el tráfico legítimo de las demás VLANs.
> - La ACL se aplicó con dirección `in` en la subinterfaz de VLAN 10, ya que filtra tráfico **originado en** esa red (entrante al router desde Turista), no tráfico con destino a ella.
> - Esta implementación difiere levemente de la ayuda sugerida en el enunciado (que solo incluía el `deny` + `permit any any`), ya que aplicar únicamente esas dos líneas habría bloqueado también el acceso de Turista al servidor de entretenimiento, incumpliendo el primer caso de la tabla de pruebas. El enunciado habilita expresamente estas adaptaciones ("pueden modificar lo que necesiten en tanto el espíritu de la actividad se mantenga").

**Verificación — `show access-lists`:**

```
Standard IP access list 20
    10 permit 10.10.20.0 0.0.0.255 (28 match(es))
Extended IP access list 100
    10 permit ip 10.10.10.0 0.0.0.255 10.10.99.0 0.0.0.255 (20 match(es))
    20 deny ip 10.10.10.0 0.0.0.255 any (8 match(es))
    30 permit ip any any (15 match(es))
```

> **Interpretación:** el contador de "matches" junto a cada línea muestra cuántos paquetes coincidieron con esa regla desde que se configuró. Se observa que la línea 10 de la ACL 100 (permiso hacia el servidor de entretenimiento) tuvo actividad, confirmando que Turista efectivamente accedió al servidor; la línea 20 (deny hacia cualquier otro destino) también registró coincidencias, correspondientes a los intentos de ping bloqueados hacia Internet.

#### Configuración final consolidada del router — `show running-config`

```
Building configuration...

Current configuration : 1749 bytes
!
version 15.1
no service timestamps log datetime msec
no service timestamps debug datetime msec
no service password-encryption
!
hostname router-avion
!
ip dhcp excluded-address 10.10.10.1 10.10.10.10
ip dhcp excluded-address 10.10.20.1 10.10.20.10
ip dhcp excluded-address 10.10.99.1 10.10.99.10
!
ip dhcp pool Turista
 network 10.10.10.0 255.255.255.0
 default-router 10.10.10.1
 dns-server 10.10.100.10
ip dhcp pool Business
 network 10.10.20.0 255.255.255.0
 default-router 10.10.20.1
 dns-server 8.8.8.8
ip dhcp pool Admin
 network 10.10.99.0 255.255.255.0
 default-router 10.10.99.1
 dns-server 8.8.8.8
!
ip cef
no ipv6 cef
!
license udi pid CISCO2811/K9 sn FTX1017NCD7-
!
spanning-tree mode pvst
!
interface FastEthernet0/0
 no ip address
 duplex auto
 speed auto
!
interface FastEthernet0/0.10
 encapsulation dot1Q 10
 ip address 10.10.10.1 255.255.255.0
 ip nat inside
 ip access-group 100 in
!
interface FastEthernet0/0.20
 encapsulation dot1Q 20
 ip address 10.10.20.1 255.255.255.0
 ip nat inside
!
interface FastEthernet0/0.99
 encapsulation dot1Q 99
 ip address 10.10.99.1 255.255.255.0
 ip nat inside
!
interface FastEthernet0/1
 ip address 200.0.0.1 255.255.255.252
 ip nat outside
 duplex auto
 speed auto
!
interface Vlan1
 no ip address
 shutdown
!
ip nat inside source list 20 interface FastEthernet0/1 overload
ip classless
ip route 0.0.0.0 0.0.0.0 200.0.0.2
!
ip flow-export version 9
!
access-list 20 permit 10.10.20.0 0.0.0.255
access-list 100 permit ip 10.10.10.0 0.0.0.255 10.10.99.0 0.0.0.255
access-list 100 deny ip 10.10.10.0 0.0.0.255 any
access-list 100 permit ip any any
!
line con 0
!
line aux 0
!
line vty 0 4
 login
!
end
```

> **Interpretación:** esta configuración consolidada resume toda la Parte 3: subinterfaces 802.1Q por VLAN, marcado NAT inside/outside, regla de NAT con overload, ruta por defecto, y las dos ACLs (20 para el NAT, 100 para el control de acceso de Turista) — esta última aplicada únicamente en dirección `in` sobre la subinterfaz de VLAN 10, corrigiendo una duplicación inicial en la que había quedado también aplicada en dirección `out` por error durante las pruebas.

---

### g) Pruebas finales — tabla de verificación

|Prueba|Desde|Hacia|Resultado obtenido|
|---|---|---|---|
|Ping al servidor de entretenimiento|PC-Turista|10.10.99.10|✅ Responde|
|Ping a Internet (simulado: Server-ISP)|PC-Turista|200.0.0.2|❌ Destination host unreachable|
|Ping al servidor de entretenimiento|PC-Business|10.10.99.10|✅ Responde|
|Ping a Internet (simulado: Server-ISP)|PC-Business|200.0.0.2|✅ Responde|
|Ping a Turista|PC-Admin|10.10.10.11|✅ Responde|
|Ping a Business|PC-Admin|10.10.20.11|✅ Responde|
|Ping a Internet (simulado: Server-ISP)|PC-Admin|200.0.0.2|✅ Responde|

> **Nota metodológica:** dado que Packet Tracer no posee conexión real a Internet, se utilizó la IP del Server-ISP (`200.0.0.2`) como destino representativo de "Internet" en lugar de una IP pública real (ej. 8.8.8.8). Al probar con una IP inexistente en la simulación (como 8.8.8.8) sin ruta por defecto configurada, el router responde con "Destination host unreachable"; una vez agregada la ruta por defecto, la misma prueba resulta en "Request timed out" al no existir ese host en la red simulada — comportamiento distinto y complementario al bloqueo activo por ACL observado en las pruebas de Turista.

> **Conclusión general:** la combinación de VLANs (segmentación de dominios de broadcast), NAT con sobrecarga (traducción y control de qué tráfico sale a Internet) y ACL extendida (control de acceso entre VLANs) permitió implementar exitosamente la política de acceso solicitada: Turista con acceso restringido únicamente al servidor local, Business con acceso al servidor e Internet, y Admin con acceso total a toda la red.