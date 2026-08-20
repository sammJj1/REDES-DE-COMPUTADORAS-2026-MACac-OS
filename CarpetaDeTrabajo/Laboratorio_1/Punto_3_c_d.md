#### c) Otras técnicas de modulación basadas en los mismos principios

Investigando un poco más sobre PSK, encontramos que no es la única variante que existe, sino que hay varias que parten de la misma idea (mover la fase de la portadora) pero le agregan alguna mejora:

- **DPSK (PSK diferencial):** acá lo que cambia es que la fase no se compara contra una referencia fija, sino contra el bit anterior. Si el bit es `0`, se manda con la misma fase que el bit de antes; si es `1`, se invierte. La ventaja es que el receptor no necesita estar perfectamente sincronizado con el transmisor, porque solo tiene que "acordarse" de la fase anterior.

- **QPSK:** en vez de usar 2 fases como BPSK (0° y 180°), usa 4 fases distintas (separadas cada 90°). Eso hace que cada pulso de señal ahora puede representar 2 bits en vez de 1, entonces se puede mandar el doble de información sin necesitar más ancho de banda.

- **OQPSK:** es básicamente QPSK pero con un pequeño retraso agregado a una de las dos partes de la señal, para que nunca salte de fase de golpe (máximo 90° por vez, no 180° como en QPSK normal). Esto lo hace más estable en canales "más ruidosos" o no ideales.

- **PSK multinivel (M-PSK):** es la misma lógica pero llevada más lejos ya que en vez de 4 fases se pueden usar 8 o más. Cuantas más fases, más bits por señal se pueden mandar, pero también es más fácil que el receptor confunda una fase con otra si hay ruido de por medio.

- **QAM:** esta ya no es puramente PSK, sino que combina PSK con ASK (varía fase y amplitud a la vez). Es como una versión más "avanzada" de QPSK. Es la que se usa en cosas como el ADSL o algunas conexiones de banda ancha.

#### d) ¿Qué es el BER y cuál técnica tiene mejores prestaciones?

El **BER** es la probabilidad de que un bit se "pierda" o llegue mal cuando se transmite. 

¿Y de qué depende que el BER sea más alto o más bajo? Principalmente de un valor llamado **Eb/N0**, que compara cuánta energía tiene cada bit transmitido contra cuánto ruido hay en el canal. Entonces si cada bit viaja con más energía en relación al ruido de fondo, es más difícil que el receptor lo confunda, y el BER baja.

Comparando las técnicas que presentamos en el inciso anterior, encontramos lo siguiente:

- **BPSK y DPSK son las que mejor BER tienen.** Usan solo 2 fases posibles (separadas 180° entre sí), entonces quedan bien distanciadas una de la otra en el "círculo de fase". Aunque haya ruido, es difícil que el receptor confunda una fase con la otra.
- **A medida que se suman niveles** (QPSK con 4 fases, PSK multinivel con 8 o más), se gana velocidad de transmisión, porque cada señal representa más bits a la vez. Pero tiene un costo: al haber más fases, quedan más "pegadas" entre sí en ese mismo círculo, entonces cualquier ruido las hace más fáciles de confundir. Por eso el BER tiende a empeorar a medida que se agregan niveles.

**Podemos concluir que** de las técnicas de PSK que presentamos, **BPSK y DPSK son las que mejor rinden en términos de BER**, justamente por ser las más simples (solo 2 fases). El "costo" de usar variantes más avanzadas como QPSK o PSK multinivel para mandar más datos es aceptar que el sistema se vuelve más sensible al ruido.
