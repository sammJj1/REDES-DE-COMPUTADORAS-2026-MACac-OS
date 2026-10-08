Luego de una lectura de código tanto del server y el cliente se abrieron 2 terminales y se ejecutaron los siguientes códigos:


En la terminal del server se corre el código del servidor.
````
PS G:\Mauri\Programacion,facultad y trabajo\Programacion\Python> python tcp_server.py
[servidor TCP] escuchando en 127.0.0.1:12000 ...
[servidor TCP] conexión aceptada desde 127.0.0.1:56618
[servidor TCP] recibido (21 bytes): 'hola como estas amigo'
[servidor TCP] respuesta enviada: 'Recibido: hola como estas amigo'
[servidor TCP] el cliente cerró la conexión 
````

En la terminal del cliente se corre el código del cliente:
````
PS G:\Mauri\Programacion,facultad y trabajo\Programacion\Python> python tcp_client.py 127.0.0.1 "hola como estas amigo"
[cliente TCP] conectado a 127.0.0.1:12000 desde 127.0.0.1:56618
[cliente TCP] enviado: 'hola como estas amigo'
[cliente TCP] respuesta (31 bytes): 'Recibido: hola como estas amigo'
````


| Llamada   | ¿Donde se ejecuta? | ¿Genera trafico? | Segmentos que observan                                                                                                                                                                     |
| --------- | ------------------ | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| socket()  | servidor y cliente | no               |                                                                                                                                                                                            |
| bind()    | servidor           | no               |                                                                                                                                                                                            |
| listen()  | servidor           | no               |                                                                                                                                                                                            |
| connect() | cliente            | si               | 17-SYN <br>19-ACK (Inicia y completa el three-way handshake)                                                                                                                               |
| accept()  | servidor           | si               | 18-SYN-ACK (respuesta del servidor)                                                                                                                                                        |
| sendall() | ambos              | si               | Cliente<br>20-PSH,ACK (Envío de datos del mensaje)<br>23-ACK (Confirmación del cliente) <br><br>Servidor<br>21-ACK (Confirmación del servidor)<br>22-PSH,ACK (Envío de datos de respuesta) |
| recv()    | ambos              | no               |                                                                                                                                                                                            |
| close()   | ambos              | si               | Cliente<br>24-FIN,ACK <br>27-ACK(Confirmación del cliente)<br>Server<br>25-ACK(Confirmación del server)<br>26-FIN,ACK                                                                      |
 ![[CarpetaDeTrabajo/Laboratorio-5/consigna-4/Imagenes/Wireshark-local.png]]

