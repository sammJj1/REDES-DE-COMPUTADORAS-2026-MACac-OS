a)
El fenomeno que se encuentra en la figura es el ruido, especificamente el Ruido Impulsivo
- **Naturaleza no continua:** A diferencia de los ruidos de magnitud constante que son razonablemente predecibles, el ruido impulsivo es discontinuo y se presenta de forma inesperada.
- **Forma física:** Está constituido por pulsos o picos irregulares de corta duración pero que alcanzan una amplitud relativamente grande.
- **Diversidad de causas:** Se genera por factores muy variados, entre los que destacan las perturbaciones electromagnéticas exteriores (como tormentas atmosféricas) o directamente por fallos y defectos en los propios sistemas de comunicación.
- **Impacto en transmisiones analógicas (bajo):** Generalmente no tiene gran trascendencia para los datos analógicos. Por ejemplo, en una transmisión de voz humana, este ruido solo se percibirá como chasquidos o crujidos muy cortos, sin que se llegue a perder la inteligibilidad del mensaje.
- **Impacto en transmisiones digitales (muy alto):** Es una de las fuentes principales de error en la comunicación digital de datos. Debido a las altas velocidades de transmisión actuales, los bits duran muy poco tiempo; por ello, un pico de ruido de apenas una fracción de segundo  puede destruir ráfagas completas de información 

b)

Las bandas más afectadas por este fenómeno son las de **frecuencias medias y altas** (como la banda SHF de 5 GHz vista en el TP01). Al tratarse de una perturbación breve y de alta energía, estas bandas se ven más perjudicadas porque, al transmitir a mayor velocidad y frecuencia, manejan una gran densidad de datos en muy poco tiempo; esto hace que un simple pulso de ruido corrompa una cantidad masiva de bits contiguos. Además, al utilizar canales de mayor ancho de banda, captan una mayor cantidad de energía de ruido de espectro ancho. En contraste, las bandas de baja frecuencia, al operar con tasas de bits más bajas y anchos de banda más estrechos, suelen generar y sufrir un volumen menor de errores por este tipo de interferencias puntuales.

c)
La SNR (_Signal-to-Noise Ratio_ o Relación Señal a Ruido) es una métrica que compara la potencia de la señal útil con la potencia del ruido de fondo en el canal de comunicación. Se expresa en decibelios (dB); una SNR alta indica que la señal es mucho más fuerte que el ruido (canal limpio), mientras que una SNR baja señala que el ruido interfiere fuertemente con la señal.

Esta métrica se relaciona directamente con el BER (_Bit Error Rate_ o Tasa de Error de Bits), el cual mide la proporción de bits que llegan erróneos en relación con el total transmitido. **Son inversamente proporcionales**: a mayor SNR, menor es el BER (pocos errores), y viceversa, si la SNR baja, el BER aumenta considerablemente debido a la dificultad del receptor para interpretar la información.