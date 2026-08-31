1) Vamos a empezar observando cómo se organiza la información dentro de una red local:   

    a) ¿Qué función cumple la capa de enlace dentro del modelo OSI? ¿Qué tipo de comunicación resuelve?   

    b) ¿Qué es una dirección MAC? ¿En qué se diferencia de una dirección IP?   

    c) ¿Qué es una trama Ethernet? Identificar sus principales campos y explicar brevemente para qué sirve cada uno.  

    d) ¿Qué información permite determinar qué protocolo de capa superior está transportando una trama Ethernet?  

---


a) La capa de enlace de datos es la encargada de la fiabilidad del enlace fisico, la encapsulación de tramas: obtiene lo que la capa de red genra, le agrega su propia cabecera y genera lo que se conoce como trama. También proporciona, a las capas superiores, el servicio de control y correccion de errores.  
Se encarga de las comunicaciones nodo a nodo, a diferencia con la capa de red que se encarga de llevar el paquete desde el origen hasta el destino mediante multiples redes, refiriéndonos a nodo como un switch, router u host. 


b) Una dirección MAC por sus siglas en inglés **Medium Access Control** es un identificador para la red local grabado en el hardware (en la ROM) de la tarjeta de red del end-device. Este indentificador solo es visible para la red local, no se expone al exterior, para esos casos es donde se usa la dirección **IP**
La **IP** es la dirección asignada por el Router a ese dispositvo en particular, y si es expuesta (cuando se lo requiera y mediante el router) a exterior.