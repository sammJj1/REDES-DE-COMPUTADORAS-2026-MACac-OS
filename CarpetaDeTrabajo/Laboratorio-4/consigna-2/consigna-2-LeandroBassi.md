### a) Configuración de los pc's y switchs:
Creamos el sistema físico con los switchs y las computadoras siguiendo el diagrama propuesto, se configuro la ip, mask y gateway de las computadoras con los valores dados en la tabla.

### b) Asignación de contraseñas:

Mediante el uso de *show running config* pudimos observar que `service password-encryption` encriptó correctamente todas las contraseñas y que `enable secret` quedó protegida con hash tipo 5.

#### SW-1
```
SW-1#show running-config
Building configuration...

Current configuration : 1563 bytes
!
version 15.0
no service timestamps log datetime msec
no service timestamps debug datetime msec
service password-encryption
!
hostname SW-1
!
enable secret 5 $1$mERr$m0ysNRb73K4DsuGxNJ5t60
!
!
!
!
!
!
spanning-tree mode pvst
spanning-tree extend system-id
!
interface FastEthernet0/1

SW-1#show running-config
Building configuration...

Current configuration : 1563 bytes
!
version 15.0
no service timestamps log datetime msec
no service timestamps debug datetime msec
service password-encryption
!
hostname SW-1
!
enable secret 5 $1$mERr$m0ysNRb73K4DsuGxNJ5t60
!
!
!
!
!
!
spanning-tree mode pvst
spanning-tree extend system-id
!
interface FastEthernet0/1
 switchport access vlan 10
 switchport mode access
!
interface FastEthernet0/2
!
interface FastEthernet0/3
 shutdown
!
interface FastEthernet0/4
 shutdown
!
interface FastEthernet0/5
 shutdown
!
interface FastEthernet0/6
 shutdown
!
interface FastEthernet0/7
 shutdown
!
interface FastEthernet0/8
 shutdown
!
interface FastEthernet0/9
 shutdown
!
interface FastEthernet0/10
 shutdown
!
interface FastEthernet0/11
 shutdown
!
interface FastEthernet0/12
 shutdown
!
interface FastEthernet0/13
 shutdown
!
interface FastEthernet0/14
 shutdown
!
interface FastEthernet0/15
 shutdown
!
interface FastEthernet0/16
 shutdown
!
interface FastEthernet0/17
 shutdown
!
interface FastEthernet0/18
 shutdown
!
interface FastEthernet0/19
 shutdown
!
interface FastEthernet0/20
 shutdown
!
interface FastEthernet0/21
 shutdown
!
interface FastEthernet0/22
 shutdown
!
interface FastEthernet0/23
 shutdown
!
interface FastEthernet0/24
 shutdown
!
interface GigabitEthernet0/1
 shutdown
!
interface GigabitEthernet0/2
 shutdown
!
interface Vlan1
 no ip address
!
interface Vlan99
 ip address 192.168.1.11 255.255.255.0
!
!
!
!
line con 0
 password 7 087519185C4D514446
 login
!
line vty 0 4
 password 7 087519185C4D514446
 login
line vty 5 15
 password 7 087519185C4D514446
 login
!
!
!
!
end
```

#### SW-2
```
SW-2#show running-config
Building configuration...

Current configuration : 1563 bytes
!
version 15.0
no service timestamps log datetime msec
no service timestamps debug datetime msec
service password-encryption
!
hostname SW-2
!
enable secret 5 $1$mERr$m0ysNRb73K4DsuGxNJ5t60
!
!
!
!
!
!
spanning-tree mode pvst
spanning-tree extend system-id
!
interface FastEthernet0/1
 switchport access vlan 10
 switchport mode access
!
interface FastEthernet0/2
!
interface FastEthernet0/3
 shutdown
!
interface FastEthernet0/4
 shutdown
!
interface FastEthernet0/5
 shutdown
!
interface FastEthernet0/6
 shutdown
!
interface FastEthernet0/7
 shutdown
!
interface FastEthernet0/8
 shutdown
!
interface FastEthernet0/9
 shutdown
!
interface FastEthernet0/10
 shutdown
!
interface FastEthernet0/11
 shutdown
!
interface FastEthernet0/12
 shutdown
!
interface FastEthernet0/13
 shutdown
!
interface FastEthernet0/14
 shutdown
!
interface FastEthernet0/15
 shutdown
!
interface FastEthernet0/16
 shutdown
!
interface FastEthernet0/17
 shutdown
!
interface FastEthernet0/18
 shutdown
!
interface FastEthernet0/19
 shutdown
!
interface FastEthernet0/20
 shutdown
!
interface FastEthernet0/21
 shutdown
!
interface FastEthernet0/22
 shutdown
!
interface FastEthernet0/23
 shutdown
!
interface FastEthernet0/24
 shutdown
!
interface GigabitEthernet0/1
 shutdown
!
interface GigabitEthernet0/2
 shutdown
!
interface Vlan1
 no ip address
!
interface Vlan99
 ip address 192.168.1.12 255.255.255.0
!
!
!
!
line con 0
 password 7 087519185C4D514446
 login
!
line vty 0 4
 password 7 087519185C4D514446
 login
line vty 5 15
 password 7 087519185C4D514446
 login
!
!
!
!
end
```

### c) Encriptado de contraseñas:
Una vez asignadas las contraseñas, las encriptamos con `service password-encryption`.

### d) Configuración de vLAN's para SW-1 y SW-2:
Se configuró la Vlan con la información dada.

### e) Desconexión de Interfaces inutilizadas:
Como solo voy a querer los primeros 2:
```
SW-1# interface range fastEthernet 0/3 - 24
SW-1# shutdown

SW-2# interface range fastEthernet 0/3 - 24
SW-2# shutdown
```

#### SW-1
```
SW-1#show ip interface brief
Interface              IP-Address      OK? Method Status                Protocol 
FastEthernet0/1        unassigned      YES manual up                    up 
FastEthernet0/2        unassigned      YES manual up                    up 
FastEthernet0/3        unassigned      YES manual administratively down down 
FastEthernet0/4        unassigned      YES manual administratively down down 
FastEthernet0/5        unassigned      YES manual administratively down down 
FastEthernet0/6        unassigned      YES manual administratively down down 
FastEthernet0/7        unassigned      YES manual administratively down down 
FastEthernet0/8        unassigned      YES manual administratively down down 
FastEthernet0/9        unassigned      YES manual administratively down down 
FastEthernet0/10       unassigned      YES manual administratively down down 
FastEthernet0/11       unassigned      YES manual administratively down down 
FastEthernet0/12       unassigned      YES manual administratively down down 
FastEthernet0/13       unassigned      YES manual administratively down down 
FastEthernet0/14       unassigned      YES manual administratively down down 
FastEthernet0/15       unassigned      YES manual administratively down down 
FastEthernet0/16       unassigned      YES manual administratively down down 
FastEthernet0/17       unassigned      YES manual administratively down down 
FastEthernet0/18       unassigned      YES manual administratively down down 
FastEthernet0/19       unassigned      YES manual administratively down down 
FastEthernet0/20       unassigned      YES manual administratively down down 
FastEthernet0/21       unassigned      YES manual administratively down down 
FastEthernet0/22       unassigned      YES manual administratively down down 
FastEthernet0/23       unassigned      YES manual administratively down down 
FastEthernet0/24       unassigned      YES manual administratively down down 
GigabitEthernet0/1     unassigned      YES manual administratively down down 
GigabitEthernet0/2     unassigned      YES manual administratively down down
```

#### SW-2

```
Interface              IP-Address      OK? Method Status                Protocol 
FastEthernet0/1        unassigned      YES manual up                    up 
FastEthernet0/2        unassigned      YES manual up                    up 
FastEthernet0/3        unassigned      YES manual administratively down down 
FastEthernet0/4        unassigned      YES manual administratively down down 
FastEthernet0/5        unassigned      YES manual administratively down down 
FastEthernet0/6        unassigned      YES manual administratively down down 
FastEthernet0/7        unassigned      YES manual administratively down down 
FastEthernet0/8        unassigned      YES manual administratively down down 
FastEthernet0/9        unassigned      YES manual administratively down down 
FastEthernet0/10       unassigned      YES manual administratively down down 
FastEthernet0/11       unassigned      YES manual administratively down down 
FastEthernet0/12       unassigned      YES manual administratively down down 
FastEthernet0/13       unassigned      YES manual administratively down down 
FastEthernet0/14       unassigned      YES manual administratively down down 
FastEthernet0/15       unassigned      YES manual administratively down down 
FastEthernet0/16       unassigned      YES manual administratively down down 
FastEthernet0/17       unassigned      YES manual administratively down down 
FastEthernet0/18       unassigned      YES manual administratively down down 
FastEthernet0/19       unassigned      YES manual administratively down down 
FastEthernet0/20       unassigned      YES manual administratively down down 
FastEthernet0/21       unassigned      YES manual administratively down down 
FastEthernet0/22       unassigned      YES manual administratively down down 
FastEthernet0/23       unassigned      YES manual administratively down down 
FastEthernet0/24       unassigned      YES manual administratively down down 
GigabitEthernet0/1     unassigned      YES manual administratively down down 
GigabitEthernet0/2     unassigned      YES manual administratively down down 
```
### f) Guardado de la configuración:
Se guardó la configuración para ambos switchs usando `write memory`

### g) Testeo de la comunicación:

#### PC-A -> PC-B

```
C:\>ping 192.168.10.4

Pinging 192.168.10.4 with 32 bytes of data:

Reply from 192.168.10.4: bytes=32 time<1ms TTL=128
Reply from 192.168.10.4: bytes=32 time<1ms TTL=128
Reply from 192.168.10.4: bytes=32 time<1ms TTL=128
Reply from 192.168.10.4: bytes=32 time<1ms TTL=128

Ping statistics for 192.168.10.4:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 0ms, Average = 0ms
```

> **Análisis de los Resultados:** El éxito de ambos pings confirma que tanto las computadoras como los switches comparten el mismo dominio de difusión inicial (la VLAN 1 predeterminada). Al encontrarse en esta misma red lógica, el tráfico fluye directamente a nivel de la capa de enlace de datos (capa 2) resolviendo direcciones MAC, lo que permite una comunicación directa sin requerir la intervención de un router.

### h) Creación de vLAN´s en ambos switchs:

```
SW-1(config)#vlan 10
SW-1(config-vlan)#name Laboratorio
SW-1(config-vlan)#vlan 20
SW-1(config-vlan)#name Bar
SW-1(config-vlan)#vlan 99
SW-1(config-vlan)#name Management
```

```
SW-2(config)#vlan 10
SW-2(config-vlan)#name Laboratorio
SW-2(config-vlan)#vlan 20
SW-2(config-vlan)#name Bar
SW-2(config-vlan)#vlan 99
SW-2(config-vlan)#name Management
```
### i) & l) Verificación de vLAN's

#### SW-1:

```
SW-1#show ip interface brief
Interface              IP-Address      OK? Method Status                Protocol 
FastEthernet0/1        unassigned      YES manual up                    up 
FastEthernet0/2        unassigned      YES manual up                    up 
FastEthernet0/3        unassigned      YES manual administratively down down 
FastEthernet0/4        unassigned      YES manual administratively down down 
FastEthernet0/5        unassigned      YES manual administratively down down 
FastEthernet0/6        unassigned      YES manual administratively down down 
FastEthernet0/7        unassigned      YES manual administratively down down 
FastEthernet0/8        unassigned      YES manual administratively down down 
FastEthernet0/9        unassigned      YES manual administratively down down 
FastEthernet0/10       unassigned      YES manual administratively down down 
FastEthernet0/11       unassigned      YES manual administratively down down 
FastEthernet0/12       unassigned      YES manual administratively down down 
FastEthernet0/13       unassigned      YES manual administratively down down 
FastEthernet0/14       unassigned      YES manual administratively down down 
FastEthernet0/15       unassigned      YES manual administratively down down 
FastEthernet0/16       unassigned      YES manual administratively down down 
FastEthernet0/17       unassigned      YES manual administratively down down 
FastEthernet0/18       unassigned      YES manual administratively down down 
FastEthernet0/19       unassigned      YES manual administratively down down 
FastEthernet0/20       unassigned      YES manual administratively down down 
FastEthernet0/21       unassigned      YES manual administratively down down 
FastEthernet0/22       unassigned      YES manual administratively down down 
FastEthernet0/23       unassigned      YES manual administratively down down 
FastEthernet0/24       unassigned      YES manual administratively down down 
GigabitEthernet0/1     unassigned      YES manual administratively down down 
GigabitEthernet0/2     unassigned      YES manual administratively down down 
Vlan1                  unassigned      YES manual up                    up 
Vlan99                 192.168.1.11    YES manual up                    up
```

```
SW-1#show vlan brief

VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Fa0/2, Fa0/3, Fa0/4, Fa0/5
                                                Fa0/6, Fa0/7, Fa0/8, Fa0/9
                                                Fa0/10, Fa0/11, Fa0/12, Fa0/13
                                                Fa0/14, Fa0/15, Fa0/16, Fa0/17
                                                Fa0/18, Fa0/19, Fa0/20, Fa0/21
                                                Fa0/22, Fa0/23, Fa0/24, Gig0/1
                                                Gig0/2
10   Laboratorio                      active    Fa0/1
20   Bar                              active    
99   Management                       active    
1002 fddi-default                     active    
1003 token-ring-default               active    
1004 fddinet-default                  active    
1005 trnet-default                    active 
```

#### SW-2

```
SW-2#show ip interface brief
Interface              IP-Address      OK? Method Status                Protocol 
FastEthernet0/1        unassigned      YES manual up                    up 
FastEthernet0/2        unassigned      YES manual up                    up 
FastEthernet0/3        unassigned      YES manual administratively down down 
FastEthernet0/4        unassigned      YES manual administratively down down 
FastEthernet0/5        unassigned      YES manual administratively down down 
FastEthernet0/6        unassigned      YES manual administratively down down 
FastEthernet0/7        unassigned      YES manual administratively down down 
FastEthernet0/8        unassigned      YES manual administratively down down 
FastEthernet0/9        unassigned      YES manual administratively down down 
FastEthernet0/10       unassigned      YES manual administratively down down 
FastEthernet0/11       unassigned      YES manual administratively down down 
FastEthernet0/12       unassigned      YES manual administratively down down 
FastEthernet0/13       unassigned      YES manual administratively down down 
FastEthernet0/14       unassigned      YES manual administratively down down 
FastEthernet0/15       unassigned      YES manual administratively down down 
FastEthernet0/16       unassigned      YES manual administratively down down 
FastEthernet0/17       unassigned      YES manual administratively down down 
FastEthernet0/18       unassigned      YES manual administratively down down 
FastEthernet0/19       unassigned      YES manual administratively down down 
FastEthernet0/20       unassigned      YES manual administratively down down 
FastEthernet0/21       unassigned      YES manual administratively down down 
FastEthernet0/22       unassigned      YES manual administratively down down 
FastEthernet0/23       unassigned      YES manual administratively down down 
FastEthernet0/24       unassigned      YES manual administratively down down 
GigabitEthernet0/1     unassigned      YES manual administratively down down 
GigabitEthernet0/2     unassigned      YES manual administratively down down 
Vlan1                  unassigned      YES manual up                    up 
Vlan99                 192.168.1.12    YES manual up                    up
```

```
SW-2#show vlan brief

VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Fa0/2, Fa0/3, Fa0/4, Fa0/5
                                                Fa0/6, Fa0/7, Fa0/8, Fa0/9
                                                Fa0/10, Fa0/11, Fa0/12, Fa0/13
                                                Fa0/14, Fa0/15, Fa0/16, Fa0/17
                                                Fa0/18, Fa0/19, Fa0/20, Fa0/21
                                                Fa0/22, Fa0/23, Fa0/24, Gig0/1
                                                Gig0/2
10   Laboratorio                      active    Fa0/1
20   Bar                              active    
99   Management                       active    
1002 fddi-default                     active    
1003 token-ring-default               active    
1004 fddinet-default                  active    
1005 trnet-default                    active
```

> **Análisis de los resultados:**
> 
> - **VLAN 1 (Predeterminada):** En los equipos Cisco que no han sido configurados, esta es la red virtual activa por defecto. Agrupa la totalidad de las interfaces físicas hasta que el administrador las asigne a otras redes.
> - **VLANs reservadas (1002 al 1005):** Estas redes vienen creadas de fábrica para brindar soporte a tecnologías más antiguas (como FDDI y Token Ring) y no tienen ninguna función dentro de los alcances de este trabajo práctico.
> - **Asignación de puertos de acceso:** Las interfaces **Fa0/1** en el SW-1 y **Fa0/2** en el SW-2 fueron removidas con éxito de la VLAN por defecto y quedaron operando exclusivamente dentro de la **VLAN 10** (Laboratorio).
> - **Estado de la administración:** Las interfaces **VLAN 99** en ambos switches ya poseen sus direcciones IP correspondientes (`192.168.1.11` y `192.168.1.12`). Al establecer el enlace físico Fa0/1 <-> Fa0/1 como troncal **802.1Q**, la interfaz virtual cambió su estado a `Protocol: up`, logrando que los equipos puedan comunicarse a nivel de management.
> - Comportamiento del enlace troncal (Trunk): Antes de aplicar esta configuración, la comunicación entre las VLANs 10 y 99 estaba bloqueada entre los switches, ya que el puerto Fa0/1 funcionaba en modo de acceso (transportando únicamente tráfico nativo de la VLAN 1). Al ejecutar switchport mode trunk en las dos terminales, el enlace adquirió la capacidad de encapsular y transportar el tráfico etiquetado (802.1Q) de múltiples VLANs simultáneamente. Esta acción fue la clave para recuperar tanto el intercambio de paquetes entre la PC-A y la PC-B (VLAN 10), como la conexión administrativa entre los switches (VLAN 99).

### j) Asignación de PC-A a la VLAN Laboratorio

En **SW-1**, el puerto conectado a PC-A (Fa0/1) se configuró en modo access y se lo asignó a la VLAN 10:

```
SW-1(config)#interface fastEthernet 0/1
SW-1(config-if)#switchport mode access
SW-1(config-if)#switchport access vlan 10
SW-1(config-if)#exit
```

> **Análisis de los cambios en SW-1:** La interfaz Fa0/1 dejó de formar parte de la VLAN 1 (predeterminada) para integrarse a la VLAN 10 (Laboratorio). Esto queda demostrado al observar la salida del comando `show vlan brief` del paso previo, donde el puerto ya se visualiza dentro de esta nueva red virtual. La principal consecuencia de esta reasignación es que la PC-A ahora opera en un dominio de broadcast (difusión) completamente separado del que utiliza la PC-B.

---

### k) Reubicación de la IP management

Se retiró la IP de la interfaz vLAN1 y se la reconfiguró sobre la interfaz vLAN99, siguiendo la tabla de direccionamiento:

```
SW-1(config)#interface vlan 1
SW-1(config-if)#no ip address
SW-1(config-if)#interface vlan 99
SW-1(config-if)#ip address 192.168.1.11 255.255.255.0
SW-1(config-if)#end
```

**Verificación:**

```
Vlan1     unassigned      YES manual up   up
Vlan99    192.168.1.11    YES manual up   down
```

> **Análisis de las interfaces**: La VLAN 1 aparece sin dirección IP pero mantiene su estado en `up/up` debido a que aún conserva puertos físicos conectados y activos asociados a ella. Por otro lado, la interfaz de la VLAN 99 registra un Status: `up` pero con su `Protocol: down`. Esto indica que la configuración de la IP fue exitosa, pero la red virtual todavía no tiene puertos físicos asignados. En los equipos Cisco, una interfaz virtual (SVI) requiere que al menos un puerto perteneciente a esa VLAN esté operativo para que el protocolo cambie a estado up.

---

### m) Asignación de PC-B a VLAN Laboratorio y reubicación de management (SW-2)

Repitiendo los pasos de los puntos j) y k) para SW-2:

```
SW-2(config)#interface fastEthernet 0/2
SW-2(config-if)#switchport mode access
Sw-2(config-if)#switchport access vlan 10
Sw-2(config-if)#exit

SW-2(config)#interface vlan 1
SW-2(config-if)#no ip address
SW-2(config-if)#interface vlan 99
SW-2(config-if)#ip address 192.168.1.12 255.255.255.0
SW-2(config-if)#end
```

> **Análisis de los resultados en SW-2:** Tal como evidencia el comando `show vlan brief`, la interfaz Fa0/2 correspondiente a la PC-B se integró exitosamente a la VLAN 10 (Laboratorio). Al agrupar ambas computadoras (PC-A y PC-B) bajo la misma red virtual, se sientan las bases para que vuelvan a comunicarse, dependiendo exclusivamente de que el enlace troncal (trunk) entre los switches permita el paso de esta VLAN. En cuanto a la administración del equipo, su dirección IP (`192.168.1.12`) fue migrada de la VLAN 1 hacia la VLAN 99. Esto produjo exactamente el mismo efecto que en el primer switch: la nueva interfaz se mantuvo temporalmente en estado `Protocol: down` a la espera de que se estableciera la conexión troncal entre ambos dispositivos.