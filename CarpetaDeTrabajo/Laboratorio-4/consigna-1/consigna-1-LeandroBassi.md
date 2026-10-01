## Alcance de Redes y Virtualización:

a) Investigar cómo se clasifican las redes según su alcance. Mencionar brevemente las características principales de cada una y colocar en cada cuadro de la Figura el acrónimo de red que corresponda.

|          **Tipos de RED**          |                                        **Descripción**                                               |
|------------------------------------|------------------------------------------------------------------------------------------------------|
|    **WAN** (*Wide Área Network*)   | Son todas aquellas que **cubren una extensa área geográfica, atraviesan rutas de acceso público y consiste en una serie de dispositivos de conmutación interconectados.**|
|    **MAN** (*Metropolitan Área Network*)  | Están entre las **LAN** y las **WAN**. Las **MAN** están concebidas para satisfacer estas necesidades de **capacidad a un coste reducido y con una eficacia mayor** |
|    **LAN** (*Local Área Network*)  | Interconecta varios dispositivos y proporciona un medio para el intercambio de información entre ellos. **Tienen menor alcance** que las *WAN* pero lo compensan con una **mayor velocidad de transmisión** |
|    **PAN** (*Personal Área Network*)  | Es una **red de corto alcance** diseñada para interconectar dispositivos electrónicos dentro del espacio inmediato de un usuario (típicamente de 10 metros o menos) facilitando la comunicación, sincronización, y transferencia de datos entre dispositivos personales. |


b) ¿Qué es una vLAN? ¿Cómo se clasifican?

Una **vLAN** es una (*Virtual Local Área Network*) es un **método para crear redes lógicas independientes dentro de una misma red física** lo que **permite que los dispositivos se agrupen por software** , es decir, *diferentes dispositivos dentro de una empresa pueden comunicarse como si estuvieran conectados al mismo cable, aislando su tráfico del resto de la red.*

Podemos clasificar a las **vLAN's** de dos formas: por el **método de asignación** (*cómo el switch decide a que red pertenece a un dispositivo*) y por su **propósito o función**

#### Método de Asignación:
* **Basadas en Puertos (Estáticas):** Es el más común. Se configura manualmente cada puerto físico del switch para que pertenezca a una VLAN específica.
* **Basadas en direcciones MAC (Dinámicas):** El switch asigna la VLAN leyendo la dirección MAC (el identificador físico) de la tarjeta de red del dispositivo.
* **Basadas en Protocolos:** El switch analiza el tráfico y agrupa los dispositivos según el protocolo de red que estén utilizando

#### Propósito en la Red:
* **vLAN de Datos:** Creada específicamente para transportar el tráfico normal generado por los usuarios.
* **vLAN predeterminada:** Es la red a la que pertenecen todos los puertos de un switch recién sacado de la caja.
* **vLAN nativa:** Se utiliza en los enlaces troncales para transportar el tráfico de dispositivos antiguos o que no tienen una etiqueta de VLAN asignada.
* **vLAN de Administración:** Se configura para que los administradores de sistemas puedan acceder a las configuraciones de los equipos de red.
* **vLAN de Voz:** Diseñada para priorizar el tráfico de telefonía IP

c) Investigar y resumir el protocolo IEEE 802.1Q. ¿Cómo se relaciona con las VLAN?

El estándar **IEEE 802.1Q** es el protocolo fundamental que **hace posible que las VLAN funcionen a gran escala en una red de múltiples dispositivos**. Mientras que una vLAN divide lógicamente un switch individual, el protocolo 802.1Q permite que esa división se extienda a través de varios switches o routers, **permitiendo que las redes compartan el mismo cable físico sin mezclar su información** (**enlace troncal**, *Trunk*). Esto se logra **modificando la trama Ethernet original inyectando una "etiqueta" de 4 bytes en medio del mensaje**.

d) En el contexto de los dos ítems anteriores ¿Qué es el Tagging?

El **Tagging** es el **proceso mediante el cual un switch inserta la cabecera 802.1Q dentro de una trama Ethernet para identificar a qué red virtual pertenece esa información** mientras viaja por un cable compartido.