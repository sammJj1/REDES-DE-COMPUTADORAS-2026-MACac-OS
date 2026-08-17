Consignas:
1) Repasar y resumir brevemente los fundamentos básicos y esenciales al respecto de: Ondas
Electromagnéticas, Modulación/Demodulación, Señales de tiempo continuo, Señales de tiempo discreto,
y luego responder las consignas a continuación:
a) Analizar el siguiente gráfico de una onda electromagnética
b) ¿Qué frecuencia y longitud de onda tiene esta onda?. Considerar que viaja exactamente a la
velocidad de la luz (C).
c) El espectro EM está dividido en regiones y bandas. Investigar y mencionar en qué región del
espectro opera esta onda, y más precisamente, en qué banda. Podés utilizar las definiciones de la
ITU.
d) Investigar qué dispositivos para comunicaciones de datos operan en esta banda y brindar al menos
un ejemplo.
e) ¿Qué fenómeno se quiere representar con la línea de trazos roja en la figura de la onda?
f) El fenómeno descrito en el ítem anterior, ¿Afecta al dispositivo que diste de ejemplo? ¿Podés notar esto en alguna experiencia de la vida cotidiana?
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

b)
Para este calculo tenemos que usar la informacion que provee la imagen, en la imagen podemos ver que compelta un ciclo la onda desde los 60mm a los 120mm, entoneces la longitud de onda $\lambda$ 
se puede calcular como la resta del valor final menos el valor inicial: $120mm -60mm = 60mm = \lambda$ , con este dato podemos usar la formula que relaciona a la longitud de onda con la velocidad de propagacion (sabiendo que la velocidad es la de la luz $c$ ) y calculamos la frecuencia $\lambda = c/f$, sustituyendo valores $0,006m = 299.792.458\frac{m}{s} /f =>299.792.458\frac{m}{s}/0,006m =f = 49.965.409.666\frac{1}{s}$ o simplifcando $4,996GHz$ 
c)
Sabemos por el punto anterior que la longitud de onda es de 60mm = 6cm, por lo tanto, este EM entra en la region de microondas, dicha region tiene una longitud de onda en el rango de 30cm.
Segun la clasificacion de bandas de la ITU, 5 GHz cae dentro de la banda SFH (Super high frecuency) que tambien se les llama ondas centimetricas que van desde 3 GHz a 30 GHz.

d)
Uno de los ejemplos mas conocidos son los routers/access points Wi-Fi que operan en la banda de 5 GHz, muy usada hoy porque tiene menos interferencia que la banda de 2,4 GHz (menos dispositivos la usan) aunque a costa de menor alcance

e) 
La curva roja representa el fenómeno de la atenuación: la potencia de la señal se va perdiendo con la distancia recorrida.

f)
Si, los dispositivos que nombre si son afectados por la atenuación, los router y access point que funcionan en la banda de 5GHz culpa de la atenuación no pueden llegar muy lejos, ya que esta señal se disipa mucho, un ejemplo de la vida cotidiana es el dicho de que la banda de 5GHz es para cuando estas cerca del router y la de 2,4GHz es cuando te alejas, que es un sistema que se usa en los routers actuales o access point en el cual te cambia de banda dependiendo tu distancia al router.

g)
i) En el caso de las transmisiones de telefonía celular afecta, ya que existe la atenuación tanto por aire, agua, paredes o simplemente la distancia, y esta señal llega mas débil y causa cortes, perdidas de datos o ni siquiera llega la señal.

ii) En el cable coaxial cuanto mas largo es el cable, mas se atenúa esta señal, ya que la resistencia eléctrica aumenta por ley de ohm $R = \frac{\rho L}{A}$ y esto causa que llegue mas débil con errores, perdida de calidad o que no se pueda interpretar correctamente la señal

iii) En la fibra óptica la señal luminosa también se atenúa mientras viaja, pero por absorción y dispersión de luz, esta señal llega con menor potencia al receptor óptico, si cae el nivel suficientemente bajo puede producir errores de transmisión o perdida completa de comunicación. 