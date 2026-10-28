## Parte 1
### 1. Investigación y aplicación 
Luego de una investigación de los estándares de conexión de cables rj45, se tomo la decisión de armar un cable directo con la norma T568B. El orden de los pines de derecha hacia izquierda visto desde el conector:
1. Blanco-Naranja
2. Naranja
3. Blanco-Verde
4. Azul
5. Blanco-Azul
6. Verde
7. Blanco-Marrón
8. Marrón

Proceso de investigación:
![](/CarpetaDeTrabajo/Laboratorio-6/Imagenes/Investigador.png)

 
### 2. Construcción y Verificación 
* Luego de investigar se construyo un cable de red de aproximadamente 1 metro.

![](/CarpetaDeTrabajo/Laboratorio-6/Imagenes/Imagen_cable.png)

* Mediante una inspección visual de un cable de otro grupo se verifico que los hilos estuvieran bien crimpeados y posicionados, se dio el cable a otro grupo asi realizan la inspección de nuestro cable tanto visual como con un tester. 

![](/CarpetaDeTrabajo/Laboratorio-6/Imagenes/Video_verificacion.gif)

## Parte 2

### 1. Configuración de la Red Local (LAN)
Se conectaron las computadoras de los grupos a un switch comun de 8 puertos utilizando los cables armados en la Parte 1. En nuestra PC se configuró de forma manual una dirección IPv4 estática con los siguientes parámetros:
* **Dirección IPv4:** `192.168.1.10`
* **Máscara de subred:** `255.255.255.0`
* **Puerta de enlace predeterminada (Default Gateway):** `192.168.1.1`
### 2. Pruebas de conectividad y servidor con ncat
* Se comprobó que las PCs estuvieran en la misma LAN usando el comando ping. Salió todo bien y se detectaron todos los paquetes.

![](/CarpetaDeTrabajo/Laboratorio-6/Imagenes/Ping-nuestrapc.png)

* Se creo un servidor en la computadora del otro grupo con el comando 
	```bash
     ncat -u -l 50
	```
* Desde nuestra computadora se enviaron mensajes al servidor en `192.168.1.110:5000` 
* Capturamos el trafico con la aplicación Wireshark 

![](/CarpetaDeTrabajo/Laboratorio-6/Imagenes/captura-wireshark.png)

### Cuestionario y Preguntas de la Parte 2

**a) ¿Se observa algún procedimiento de establecimiento de conexión antes de enviar los datos?**

No. Al utilizar **UDP** (User Datagram Protocol), que es un protocolo orientado a datagramas y sin conexión (*connectionless*), los mensajes se envían directamente sin realizar un protocolo de saludo previo de tres vías (*three-way handshake*), a diferencia de lo que ocurre en TCP.

**b) ¿Existe algún mecanismo de confirmación de recepción equivalente a los ACK de TCP?**

No a nivel de protocolo de transporte. UDP no incorpora mecanismos nativos de control de flujo, retransmisión de paquetes perdidos ni acuses de recibo (ACK). Si se requiere confirmación, esta debe ser implementada de manera explícita por la aplicación que corre por encima de UDP.

**c) ¿Qué ocurre si se envían mensajes mientras el receptor UDP no está ejecutándose?**

Los paquetes llegan igualmente a la interfaz de red de la máquina destino, pero al no haber ningún proceso escuchando en el puerto especificado (`5000`), el sistema operativo receptor descartará los datagramas y, dependiendo de la configuración de la red, podría responder con un mensaje ICMP de tipo "Puerto inaccesible", mientras que el emisor nunca se enterará de la pérdida si no maneja errores en la aplicación.

**d) ¿UDP garantiza que los mensajes lleguen en el mismo orden en que fueron enviados?**

No. Debido a que los datagramas pueden tomar rutas ligeramente distintas o sufrir retardos variables en la red (o por cómo los procesa la pila de red), UDP no garantiza el orden de entrega ni la entrega misma (es un protocolo "no fiable").

**e) ¿Qué aplicaciones reales utilizan UDP y por qué?**

UDP es utilizado ampliamente en aplicaciones donde la **velocidad y la baja latencia** son más críticas que la pérdida ocasional de datos. Ejemplos comunes:
* **Streaming de video y audio en vivo (IPTV, VoIP, Zoom, Discord):** Si se pierde un fotograma de video, es mejor descartarlo y seguir con el flujo actual que pausar la transmisión esperando una retransmisión.
* **Juegos multijugador en línea:** Para la sincronización constante de posiciones en tiempo real.
* **Sistemas de consultas rápidas (DNS, DHCP):** Donde el intercambio se reduce a una sola pregunta y una sola respuesta rápida.