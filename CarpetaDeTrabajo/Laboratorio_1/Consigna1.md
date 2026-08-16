Consignas:
1) Repasar y resumir brevemente los fundamentos básicos y esenciales al respecto de: Ondas
Electromagnéticas, Modulación/Demodulación, Señales de tiempo continuo, Señales de tiempo discreto,
y luego responder las consignas a continuación:
a) Analizar el siguiente gráfico de una onda electromagnética:
1
Trabajo Práctico N°1
________________________________________________________________________________________
b) ¿Qué frecuencia y longitud de onda tiene esta onda?. Considerar que viaja exactamente a la
velocidad de la luz (C).
c) El espectro EM está dividido en regiones y bandas. Investigar y mencionar en qué región del
espectro opera esta onda, y más precisamente, en qué banda. Podés utilizar las definiciones de la
ITU.
d) Investigar qué dispositivos para comunicaciones de datos operan en esta banda y brindar al menos
un ejemplo.
e) ¿Qué fenómeno se quiere representar con la línea de trazos roja en la figura de la onda?
f) El fenómeno descrito en el ítem anterior, ¿Afecta al dispositivo que diste de ejemplo? ¿Podés notar
esto en alguna experiencia de la vida cotidiana?
g) El fenómeno descrito anteriormente:
i) ¿Afecta a las transmisiones de telefonía celular?
ii) ¿Afecta a las transmisiones por cable coaxial?
iii) ¿Afecta a las transmisiones por fibra óptica?


RTA:

1)
**Ondas electromagneticas:**
La transmision de datos, tanto en medios guiados como en medios no guiados, se realiza mediante ondas electromagneticas, dichas ondas estan constituidas por una serie de frecuencias componentes. El conjunto de estas frecuencias es lo que llamamos su espectro, y el rango de frecuencias dentro de la señal es su ancho de banda.

**Modulacion y demodulacion:**
Los datos digitales o analogicos no siempre pueden inyectarse directamente en el canal fisico en su forma original. Para eso necesitamos la modulacion y la demodulacion. Modular nos permite mandar una señal en banda base hacia otra zona del espectro centrada en una frecuencia portadora y esto nos sirve para adaptar la señal al medio fisico y multiplexar.
Las tecnicas principales serian:
- Datos digitales a señales analogicas: Traducen bits a ondas analogicas modificando parametros de la portadora. Las tecnicas basicas son ASK (modulacion por desplazamiento de amplitud), FSK (modulacion por desplazamiento de frecuencia) y PSK (modulacion por desplazamiento de fase).
- Datos analogicos a señales digitales: Convierten señales analógicas en un flujo digital de bits mediante técnicas de digitalización como PCM (modulacion por impulsos codificados) o modulacion delta (DM).
- Datos analogicos a señales analogicos: Modulan una señal analogica sobre una portadora de alta frecuencia (AM,FM o PM) para transmision por radiofrecuencia o multiplexacion.

**Señales de tiempo continuo:**
Una señal analogica es aquella en la que la intensidad de la señal varia suave y continuamente en el tiempo, sin tener saltos o discontinuidades. Los datos analogicos son aquellos que la informacion que tienen se toma de valores de un rango continuo como por ejemplo la voz (audio) cuyas ondas acusticas se convierten en variaciones continuas de tension electrica, y el video, donde la intensidad de brillo varia analogamente conforme un haz de electrones barre la pantalla.

**Señales de tiempo discreto:**
Una señal digital es aquella que la intensidad se mantiene constante durante un determinado intervalo de tiempo y despues cambia bruscamente a otro nivel constante.
En el diseño de sistemas de comunicaciones, la señalizacion digital ofrece la gran ventaja de ser mas economica que la analogica y significativamente menos susceptible a las interferencias y al ruido, sin embargo, presenta la desventaja de sufrir una atenuacion de energiaa mucho mas acusada a medida que aumenta la distancia a traves del medio. Para mitigar esta degradacion a largas distancias, la transmision digital prescinde de los amplificadores analogicos tradicionales y utiliza en su lugar repetidores.


c)
Sabemos por el punto anterior que la longitud de onda es de 60mm = 6cm, por lo tanto, este EM entra en la region de microondas, dicha region tiene una longitud de onda en el rango de 30cm.
Segun la clasificacion de bandas de la ITU, 5 GHz cae dentro de la banda SFH (Super high frecuency) que tambien se les llama ondas centimetricas que van desde 3 GHz a 30 GHz.

D)
Uno de los ejemplos mas conocidos son los routers/access points Wi-Fi que operan en la banda de 5 GHz, muy usada hoy porque tiene menos interferencia que la banda de 2,4 GHz (menos dispositivos la usan) aunque a costa de menor alcance

E) 
La curva roja representa el fenómeno de la atenuación: la potencia de la señal se va perdiendo con la distancia recorrida.
