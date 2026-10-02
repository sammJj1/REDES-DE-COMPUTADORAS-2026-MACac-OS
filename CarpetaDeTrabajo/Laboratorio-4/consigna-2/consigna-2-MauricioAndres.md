### a) Configuracion inicial de los switch y pc
Se creo el sistema físico con los switch y las computadoras siguiendo el diagrama dado, se configuro la ip, mask y gateway de las computadoras con los valores dados en la tabla. Los puertos físicos que usamos en los switch fueron, switch-1 puerto fastEthernet 0/6 hacia PCA, switch-2 puerto fastEthernet 0/18 hacia PCB. 
### b) Asignación de contraseñas (privilegiada, consola y VTY)

**Verificación — `show running-config`**

Se observa que `service password-encryption` encriptó correctamente todas las contraseñas de línea (tipo 7), y que `enable secret` quedó protegida con hash tipo 5 (irreversible), tal como se espera de este comando.

#### switch-1

```
Building configuration...

Current configuration : 1262 bytes
version 15.0
no service timestamps log datetime msec
no service timestamps debug datetime msec
service password-encryption

hostname switch-1

enable secret 5 $1$mERr$G5o59nGkzi4Bu3paGylpF/

spanning-tree mode pvst
spanning-tree extend system-id

interface Vlan1
 no ip address
 shutdown

line con 0
 password 7 080243401D0B041B1B05095578787066
 login
line vty 0 4
 password 7 080243401D0B040106125C557F65
 login
line vty 5 15
 password 7 080243401D0B040106125C557F65
 login
end
```

#### swith-2

```
Building configuration...

Current configuration : 1261 bytes
version 15.0
no service timestamps log datetime msec
no service timestamps debug datetime msec
service password-encryption

hostname swith-2

enable secret 5 $1$mERr$G5o59nGkzi4Bu3paGylpF/

spanning-tree mode pvst
spanning-tree extend system-id

interface Vlan1
 no ip address
 shutdown

line con 0
 password 7 080243401D0B041B1B05095578787066
 login
line vty 0 4
 password 7 080243401D0B040106125C557F65
 login
line vty 5 15
 password 7 080243401D0B040106125C557F65
 login
end
```

> **Interpretación:** la contraseña de `enable secret` aparece encriptada con hash MD5 (tipo 5), que es de un solo sentido — no puede revertirse a texto plano. Las contraseñas de consola y VTY, en cambio, quedaron encriptadas con el algoritmo tipo 7 gracias a `service password-encryption`; este método es débil y reversible con herramientas conocidas, por lo que Cisco recomienda siempre usar `enable secret` en vez de `enable password` para el acceso privilegiado.

---


### c) Encriptación contraseñas. 
Despues de asignar las contraseñas, se uso una encriptación mediante el comando service password-encryption, que encripto la contraseña de consola y vty.

### d) Configuración Vlan
Se hizo una configuración inicial de la Vlan por defecto, Vlan 1 con las tablas de direcciones provista.

### e) Desconexión de interfases sin utilizar 
#### switch-1 `interface range fastEthernet 0/2 - 5`
#### switch-1 `shutdown`
#### switch-1 `interface range fastEthernet 0/7 - 24`
#### switch-1 `shutdown`
```
Interface IP-Address OK? Method Status Protocol

FastEthernet0/1 unassigned YES manual up up

FastEthernet0/2 unassigned YES manual administratively down down

FastEthernet0/3 unassigned YES manual administratively down down

FastEthernet0/4 unassigned YES manual administratively down down

FastEthernet0/5 unassigned YES manual administratively down down

FastEthernet0/6 unassigned YES manual up up

FastEthernet0/7 unassigned YES manual administratively down down

FastEthernet0/8 unassigned YES manual administratively down down

FastEthernet0/9 unassigned YES manual administratively down down

FastEthernet0/10 unassigned YES manual administratively down down

FastEthernet0/11 unassigned YES manual administratively down down

FastEthernet0/12 unassigned YES manual administratively down down

FastEthernet0/13 unassigned YES manual administratively down down

FastEthernet0/14 unassigned YES manual administratively down down

FastEthernet0/15 unassigned YES manual administratively down down

FastEthernet0/16 unassigned YES manual administratively down down

FastEthernet0/17 unassigned YES manual administratively down down

FastEthernet0/18 unassigned YES manual administratively down down

FastEthernet0/19 unassigned YES manual administratively down down

FastEthernet0/20 unassigned YES manual administratively down down

FastEthernet0/21 unassigned YES manual administratively down down

FastEthernet0/22 unassigned YES manual administratively down down

FastEthernet0/23 unassigned YES manual administratively down down

FastEthernet0/24 unassigned YES manual administratively down down

GigabitEthernet0/1 unassigned YES manual administratively down down

GigabitEthernet0/2 unassigned YES manual administratively down down
```

#### switch-2 `interface range fastEthernet 0/2 - 17`
#### switch-2 `shutdown`
#### switch-2 `interface range fastEthernet 0/19 - 24`
#### switch-2 `shutdown`
```
swith-2#show ip interface brief

Interface IP-Address OK? Method Status Protocol

FastEthernet0/1 unassigned YES manual up up

FastEthernet0/2 unassigned YES manual administratively down down

FastEthernet0/3 unassigned YES manual administratively down down

FastEthernet0/4 unassigned YES manual administratively down down

FastEthernet0/5 unassigned YES manual administratively down down

FastEthernet0/6 unassigned YES manual administratively down down

FastEthernet0/7 unassigned YES manual administratively down down

FastEthernet0/8 unassigned YES manual administratively down down

FastEthernet0/9 unassigned YES manual administratively down down

FastEthernet0/10 unassigned YES manual administratively down down

FastEthernet0/11 unassigned YES manual administratively down down

FastEthernet0/12 unassigned YES manual administratively down down

FastEthernet0/13 unassigned YES manual administratively down down

FastEthernet0/14 unassigned YES manual administratively down down

FastEthernet0/15 unassigned YES manual administratively down down

FastEthernet0/16 unassigned YES manual administratively down down

FastEthernet0/17 unassigned YES manual administratively down down

FastEthernet0/18 unassigned YES manual up up

FastEthernet0/19 unassigned YES manual administratively down down

FastEthernet0/20 unassigned YES manual administratively down down

FastEthernet0/21 unassigned YES manual administratively down down

FastEthernet0/22 unassigned YES manual administratively down down

FastEthernet0/23 unassigned YES manual administratively down down

FastEthernet0/24 unassigned YES manual administratively down down

GigabitEthernet0/1 unassigned YES manual administratively down down

GigabitEthernet0/2 unassigned YES manual administratively down down
```
### f) Guardado de configuración
####`copy running-config startup-config`
### g) Test de comunicación — Ping entre PC-A y PC-B
![[Ping PCA a PCB.png]]
![[Ping PCB a PCA.png]]

> **Interpretación:** ambos pings fueron exitosos. En este punto PC-A y PC-B, junto con SW-1 y SW-2, se encuentran todos dentro del mismo dominio de broadcast (VLAN 1, la VLAN por defecto), por lo que la comunicación ocurre íntegramente a nivel de capa 2 (direcciones MAC), sin necesidad de un router.

---

### h) Creación de Vlan para ambos switches
```
sw1(config)#vlan 10
sw1(config-vlan)#name Laboratorio
sw1(config-vlan)#vlan 20
sw1(config-vlan)#name Bar
sw1(config-vlan)#vlan 99
sw1(config-vlan)#name Management
```

```
sw2(config)#vlan 10
sw2(config-vlan)#name Laboratorio
sw2(config-vlan)#vlan 20
sw2(config-vlan)#name Bar
sw2(config-vlan)#vlan 99
sw2(config-vlan)#name Management
```
### i) / l) Verificación de VLANs e interfaces

#### switch-1 — `show ip interface brief`

```
Interface              IP-Address      OK? Method Status                Protocol
FastEthernet0/1        unassigned      YES manual up                    up
FastEthernet0/2        unassigned      YES manual administratively down down
FastEthernet0/3        unassigned      YES manual administratively down down
FastEthernet0/4        unassigned      YES manual administratively down down
FastEthernet0/5        unassigned      YES manual administratively down down
FastEthernet0/6        unassigned      YES manual up                    up
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

#### switch-1 — `show vlan brief`

```
VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Fa0/2, Fa0/3, Fa0/4, Fa0/5
                                                 Fa0/7, Fa0/8, Fa0/9, Fa0/10
                                                 Fa0/11, Fa0/12, Fa0/13, Fa0/14
                                                 Fa0/15, Fa0/16, Fa0/17, Fa0/18
                                                 Fa0/19, Fa0/20, Fa0/21, Fa0/22
                                                 Fa0/23, Fa0/24, Gig0/1, Gig0/2
10   Laboratorio                      active    Fa0/6
20   Bar                              active
99   Management                       active
1002 fddi-default                     active
1003 token-ring-default               active
1004 fddinet-default                  active
1005 trnet-default                    active
```

#### swith-2 — `show ip interface brief`

```
Interface              IP-Address      OK? Method Status                Protocol
FastEthernet0/1        unassigned      YES manual up                    up
FastEthernet0/2        unassigned      YES manual administratively down down
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
FastEthernet0/18       unassigned      YES manual up                    up
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

#### swith-2 — `show vlan brief`

```
VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Fa0/2, Fa0/3, Fa0/4, Fa0/5
                                                 Fa0/6, Fa0/7, Fa0/8, Fa0/9
                                                 Fa0/10, Fa0/11, Fa0/12, Fa0/13
                                                 Fa0/14, Fa0/15, Fa0/16, Fa0/17
                                                 Fa0/19, Fa0/20, Fa0/21, Fa0/22
                                                 Fa0/23, Fa0/24, Gig0/1, Gig0/2
10   Laboratorio                      active    Fa0/18
20   Bar                              active
99   Management                       active
1002 fddi-default                     active
1003 token-ring-default               active
1004 fddinet-default                  active
1005 trnet-default                    active
```

> **Interpretación:**
> 
> - La **VLAN 1 (default)** es la VLAN utilizada por defecto en cualquier switch Cisco sin configurar: todos los puertos pertenecen a ella hasta que se reasignan manualmente.
> - Las VLANs **1002–1005** son reservadas para tecnologías legacy (FDDI, Token Ring) y vienen preconfiguradas de fábrica; no se utilizan en este TP.
> - Los puertos **Fa0/6** (SW-1) y **Fa0/18** (SW-2) quedaron correctamente asignados a la **VLAN 10 (Laboratorio)**, sacándolos de la VLAN 1.
> - La interfaz **Vlan99** ya tiene IP configurada en ambos switches (`192.168.1.11` y `192.168.1.12`) y, tras convertir el enlace Fa0/1↔Fa0/1 en **trunk 802.1Q**, pasó a `Protocol: up`, habilitando la comunicación de management entre switches.
> - Antes de configurar el trunk, el tráfico de VLAN 10 y VLAN 99 no podía cruzar entre SW-1 y SW-2, porque el enlace Fa0/1 se encontraba en modo **access** sobre VLAN 1: un puerto access solo transporta la VLAN a la que pertenece. Al aplicar `switchport mode trunk` en ambos extremos, el enlace pasó a transportar tráfico etiquetado (802.1Q) de todas las VLANs, restableciendo la conectividad tanto entre PC-A y PC-B (VLAN 10) como entre las interfaces de management de los switches (VLAN 99).

### j) Asignación de PC-A a la VLAN Laboratorio

En **SW-1**, el puerto conectado a PC-A (Fa0/6) se configuró en modo access y se lo asignó a la VLAN 10:

```
sw1(config)#interface fastEthernet 0/6
sw1(config-if)#switchport mode access
sw1(config-if)#switchport access vlan 10
sw1(config-if)#exit
```

> **Interpretación:** el puerto Fa0/6 pasó a pertenecer a la VLAN 10 (Laboratorio) en lugar de la VLAN 1 (default), lo cual se confirma en el `show vlan brief` de SW-1 (sección i/l), donde Fa0/6 figura bajo la VLAN 10. A partir de este cambio, PC-A pertenece a un dominio de broadcast distinto al de PC-B (que en este punto aún permanecía en VLAN 1), por lo que la comunicación entre ambas se interrumpiría hasta completar el punto m).

---

### k) Reubicación de la IP de management: VLAN 1 → VLAN 99 (SW-1)

Se retiró la IP de la interfaz Vlan1 y se la reconfiguró sobre la interfaz Vlan99, siguiendo la tabla de direccionamiento:

```
sw1(config)#interface vlan 1
sw1(config-if)#no ip address
sw1(config-if)#interface vlan 99
sw1(config-if)#ip address 192.168.1.11 255.255.255.0
sw1(config-if)#end
```

**Verificación inmediata — `show ip interface brief` (antes del trunk):**

```
Vlan1     unassigned      YES manual up   up
Vlan99    192.168.1.11    YES manual up   down
```

> **Interpretación:** la interfaz Vlan1 quedó sin IP pero `up/up`, porque todavía existían puertos físicos activos en esa VLAN. La interfaz Vlan99, en cambio, mostró `Status: up` pero **`Protocol: down`**: la IP estaba correctamente configurada, pero no había ningún puerto físico asignado a la VLAN 99 en ese momento (una SVI solo pasa a `Protocol: up` cuando al menos un puerto físico de su VLAN está activo). Este comportamiento se resolvió más adelante, al convertir el enlace Fa0/1↔Fa0/1 en trunk 802.1Q (ver interpretación del punto i/l), lo que permitió que el tráfico de VLAN 99 circulara entre switches y la interfaz pasara a `up/up`, tal como se observa en la verificación final del punto i/l.

---

### m) Asignación de PC-B a VLAN Laboratorio y reubicación de management (SW-2)

Repitiendo el procedimiento de los puntos j) y k) para SW-2:

```
sw2(config)#interface fastEthernet 0/18
sw2(config-if)#switchport mode access
sw2(config-if)#switchport access vlan 10
sw2(config-if)#exit

sw2(config)#interface vlan 1
sw2(config-if)#no ip address
sw2(config-if)#interface vlan 99
sw2(config-if)#ip address 192.168.1.12 255.255.255.0
sw2(config-if)#end
```

> **Interpretación:** el puerto Fa0/18 (conectado a PC-B) quedó asignado a la VLAN 10 (Laboratorio), tal como se ve en el `show vlan brief` de SW-2 (sección i/l). Con PC-A y PC-B nuevamente en la misma VLAN, se restableció la posibilidad de comunicación entre ambas (sujeta a que el enlace troncal entre switches transporte dicha VLAN, ver punto i/l). La IP de management se reubicó de Vlan1 a Vlan99 (`192.168.1.12`), replicando en SW-2 el mismo comportamiento observado en SW-1: la interfaz quedó inicialmente con `Protocol: down` hasta la configuración del trunk entre switches.


