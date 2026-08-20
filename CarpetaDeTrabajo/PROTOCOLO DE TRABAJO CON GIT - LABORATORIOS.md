OBJETIVO

Este protocolo establece una metodología de trabajo para el desarrollo del Laboratorio 2 utilizando Git y GitHub.

El objetivo principal es mantener el repositorio organizado y evitar:

- Branches duplicadas para una misma consigna.
- Versiones diferentes del mismo archivo.
- Conflictos innecesarios entre integrantes.
- Problemas con el merge de archivos Markdown.
- Archivos de imágenes desorganizados.
- Cambios de distintas consignas mezclados en un mismo Pull Request.

La regla principal es:

SI TRABAJAS EN UNA CONSIGNA, TRABAJAS SOBRE LA BRANCH DE ESA CONSIGNA.

La branch representa a la consigna y no a una persona.


ESTRUCTURA DEL LABORATORIO 2

El Laboratorio 2 deberá estar organizado de la siguiente manera:

/Laboratorio_2/
    /consigna-1/
        consigna-1.md
        /Imagenes/

    /consigna-2/
        consigna-2.md
        /Imagenes/

    /consigna-3/
        consigna-3.md
        /Imagenes/

    ...

    /consigna-x/
        consigna-x.md
        /Imagenes/


Cada consigna deberá tener obligatoriamente su propia carpeta.

Dentro de esa carpeta deberán existir:

1. El archivo Markdown de la consigna.
2. Una carpeta llamada EXACTAMENTE: Imagenes

Las imágenes utilizadas dentro del archivo .md deberán almacenarse dentro de esta carpeta.

Por ejemplo, para la consigna 4:

/Laboratorio_2/consigna-4/
    consigna-4.md
    /Imagenes/
        imagen1.png
        imagen2.jpg
        diagrama.png

No se deberán guardar imágenes directamente dentro de /Laboratorio_2/ ni en otras ubicaciones.


BRANCHES

Cada consigna tendrá UNA ÚNICA branch de trabajo.

Las branches deberán seguir obligatoriamente la siguiente nomenclatura:

rama-consigna-x

Por ejemplo:

rama-consigna-1
rama-consigna-2
rama-consigna-3
rama-consigna-4

La relación entre branch, carpeta y archivo será:

Branch:
rama-consigna-4

Carpeta:
Laboratorio_2/consigna-4/

Archivo:
Laboratorio_2/consigna-4/consigna-4.md

Imágenes:
Laboratorio_2/consigna-4/Imagenes/


UNA CONSIGNA = UNA BRANCH

Una consigna debe tener una única branch de trabajo.

Si tres personas trabajan sobre la consigna 4, las tres personas trabajan sobre:

rama-consigna-4

NO se deben crear branches individuales como:

rama-consigna-4-mauricio
rama-consigna-4-valen
rama-consigna-4-mauricio-final-v3-0.3.2-ultrafinal

La branch representa a la CONSIGNA, no a la PERSONA.

Por lo tanto:

Consigna 4
    |
    +-- rama-consigna-4
            |
            +-- Integrante A
            +-- Integrante B
            +-- Integrante C


METODOLOGÍA DE TRABAJO

Esta es la regla más importante del protocolo.

Si una persona está trabajando en la consigna 4, debe trabajar exclusivamente sobre:

rama-consigna-4

Los demás integrantes que trabajen sobre la misma consigna también deben utilizar:

rama-consigna-4

Todos deben trabajar sobre los mismos archivos:

/Laboratorio_2/consigna-4/
    consigna-4.md
    Imagenes/


NO se deben crear copias del archivo Markdown.

NO se deben crear branches personales para continuar la misma consigna.

NO se debe crear otro archivo para reemplazar al existente.

Por ejemplo, NO:

consigna-4-mauricio.md
consigna-4-valen.md
consigna-4-branko.md

Todos trabajan sobre:

consigna-4.md


Cuando un integrante realiza cambios y los sube a la branch, los demás integrantes deberán obtener esos cambios desde la MISMA branch.

Si están trabajando en la consigna 4:

git pull origin rama-consigna-4

Los cambios de una consigna en desarrollo se obtienen desde la branch de esa consigna.

NO se debe utilizar main para compartir cambios que todavía pertenecen a una consigna en desarrollo.


TRABAJO CON VARIOS INTEGRANTES

Ejemplo:

Tres integrantes trabajan sobre la consigna 4.

Todos utilizan:

rama-consigna-4

Los tres modifican:

/Laboratorio_2/consigna-4/consigna-4.md

y, si es necesario, agregan o modifican imágenes dentro de:

/Laboratorio_2/consigna-4/Imagenes/


El flujo será:

Integrante A realiza cambios
        |
        v
      commit
        |
        v
      push
        |
        v
rama-consigna-4
        |
        v
Integrante B hace pull
        |
        v
continúa trabajando

De esta manera, los integrantes siempre trabajan sobre la versión más reciente disponible de la consigna.


CONFLICTOS

Todos los conflictos relacionados con una consigna DEBEN resolverse dentro de la branch de esa consigna.

Por ejemplo, si existen conflictos entre los cambios de dos integrantes de la consigna 4, estos deberán resolverse en:

rama-consigna-4

ANTES de realizar el Pull Request hacia main.

Main NO es el lugar donde se deben resolver los conflictos internos de una consigna.

La branch de la consigna debe llegar al Pull Request en un estado correcto, revisado y sin conflictos pendientes.

Por lo tanto:

rama-consigna-4
        |
        | resolver conflictos
        |
        v
rama-consigna-4
        |
        | Pull Request
        v
main


PULL REQUEST Y MERGE

Cuando una consigna esté completamente terminada, revisada y sin conflictos, se realizará el Pull Request desde la branch correspondiente hacia main.

Por ejemplo:

rama-consigna-4
        |
        | Pull Request
        v
main

El Pull Request debe contener ÚNICAMENTE los cambios correspondientes a esa consigna.

Un Pull Request de:

rama-consigna-4

no debe incluir cambios de:

- consigna-5
- consigna-6
- otras consignas
- archivos personales
- archivos temporales
- copias de archivos Markdown
- cambios que no correspondan a la consigna 4

El objetivo es que cada Pull Request represente una única consigna terminada.


MAIN

Main debe contener únicamente consignas terminadas, revisadas e integradas.

Al finalizar la consigna 4, main deberá contener:

/Laboratorio_2/
    /consigna-1/
        consigna-1.md
        /Imagenes/

    /consigna-2/
        consigna-2.md
        /Imagenes/

    /consigna-3/
        consigna-3.md
        /Imagenes/

    /consigna-4/
        consigna-4.md
        /Imagenes/


La consigna 4 llega a main como una unidad:

/Laboratorio_2/consigna-4/
    consigna-4.md
    Imagenes/


De esta manera, el archivo Markdown y todas las imágenes que utiliza quedan juntos y se evita que las rutas de las imágenes se rompan al mover o modificar archivos.


REGLAS FUNDAMENTALES

1. UNA CONSIGNA = UNA BRANCH.

Si trabajas en la consigna 4, trabajas en rama-consigna-4.

2. UNA CONSIGNA = UNA CARPETA.

Cada consigna debe estar dentro de:

/Laboratorio_2/consigna-x/

3. UNA CONSIGNA = UN ARCHIVO MARKDOWN.

Dentro de la carpeta debe existir:

consigna-x.md

No se crean copias ni versiones alternativas del archivo.

4. TODAS LAS IMÁGENES DE LA CONSIGNA DEBEN ESTAR EN:

/Laboratorio_2/consigna-x/Imagenes/

La carpeta debe llamarse obligatoriamente "Imagenes".

5. VARIAS PERSONAS TRABAJANDO EN LA MISMA CONSIGNA UTILIZAN LA MISMA BRANCH.

No se crean branches personales para una misma consigna.

6. LOS CAMBIOS ENTRE INTEGRANTES SE COMPARTEN MEDIANTE LA BRANCH DE LA CONSIGNA.

Si estás trabajando en consigna 4, obtienes los últimos cambios desde:

rama-consigna-4

y no desde main mientras la consigna esté en desarrollo.

7. LOS CONFLICTOS INTERNOS DE UNA CONSIGNA SE RESUELVEN EN SU PROPIA BRANCH.

La branch debe estar correctamente integrada y sin conflictos antes de solicitar el Pull Request.

8. CADA PULL REQUEST CORRESPONDE A UNA ÚNICA CONSIGNA.

Un Pull Request de rama-consigna-x debe contener únicamente los cambios de esa consigna.

9. MAIN SOLO RECIBE CONSIGNAS TERMINADAS Y REVISADAS.

El objetivo es que main permanezca limpio, organizado y estable.

10. LA ESTRUCTURA FINAL DEBE MANTENER LAS CONSIGNAS ORDENADAS.

Por ejemplo:

/Laboratorio_2/
    /consigna-1/
        consigna-1.md
        Imagenes/

    /consigna-2/
        consigna-2.md
        Imagenes/

    /consigna-3/
        consigna-3.md
        Imagenes/

    /consigna-4/
        consigna-4.md
        Imagenes/


FLUJO GENERAL

Para cada consigna se seguirá siempre el mismo proceso:

                    MAIN
                      |
                      v
              rama-consigna-x
                      |
          +-----------+-----------+
          |           |           |
          v           v           v
      Persona A   Persona B   Persona C
          |           |           |
          +-----------+-----------+
                      |
              commits / push / pull
                      |
                      v
              rama-consigna-x
                      |
               resolver conflictos
                      |
                 revisar trabajo
                      |
                Pull Request
                      |
                      v
                     MAIN
                      |
                      v
              Consigna terminada


La branch es el espacio de trabajo de la consigna.

Main es el espacio de integración de las consignas terminadas.

Nunca se debe utilizar main como espacio de trabajo compartido para una consigna que todavía está en desarrollo.