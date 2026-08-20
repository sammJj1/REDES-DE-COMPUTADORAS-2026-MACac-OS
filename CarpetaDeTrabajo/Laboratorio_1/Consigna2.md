2) Comunicar datos a través de cualquier medio es, en esencia, un proceso que consiste en modificar el comportamiento de una señal en el tiempo. En esta materia nos concentramos en la transmisión de datos, hoy por hoy, dominado por las señales digitales. Analicemos el siguiente sistema:

### a) Tipo y modo de transmisión

Según su direccionalidad y características temporales, se representa una transmisión Simplex (unidireccional), debido a que la señal fluye en una sola dirección. Además, es Sincrónica ya que hay una señal de clock dedicada que sincroniza los tiempos de ambos.

### b) Transmisión de datos rapida y bidireccional

Si buscamos transmitir datos rápidamente y de forma bidireccional, el anterior paradigma no es el mejor ya que es Simplex. En este caso, conviene usar una transmisión Full duplex, el cual permite transmitir y recibir datos en ambas direcciones al mismo tiempo, ideal para maximizar velocidad bidireccional.

### c) Representación de la señal digital

Si quisiéramos transmitir la 4ta letra del nombre de nuestro grupo (**MACac OS**), la cual es **“a”**, la señal se vería representada de esta manera:

![](/CarpetaDeTrabajo/Laboratorio_1/imag/senal-codificada.png)

* En codificación ASCII, el caracter **“a”** equivale a **97** en decimal.
* Convirtiendo 97 a binario, obtenemos el byte: `0110 0001`.


### d) Medición y marcas temporales

Para determinar el valor digital de la señal, las marcas temporales en las que mediríamos serían a la **mitad del intervalo**, por ejemplo en **T0**, **T2** y **T4**. Ya que si medimos la señal justo donde comienza el cambio temporal, como en el caso de **T3**, nos encontramos con una tensión intermedia que puede generar errores de lectura. De esta manera, nos aseguramos de que el cambio de tensión ya se encuentra estable y tenemos un nivel **1** o **0** claro y definido.

![](/CarpetaDeTrabajo/Laboratorio_1/imag/marcas-temporales.png)
