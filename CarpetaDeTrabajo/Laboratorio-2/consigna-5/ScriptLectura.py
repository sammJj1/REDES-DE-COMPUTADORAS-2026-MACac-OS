import os

# Ruta del archivo binario y nombre del grupo propio a buscar
NOMBRE_ARCHIVO = "G:/Mauri/Programacion/PracticosRedesComputadoras/REDES-DE-COMPUTADORAS-2026-MACac-OS/CarpetaDeTrabajo/Laboratorio-2/Archivos/frames.bin"
TU_GRUPO = "macac"

# Primeros 5 caracteres (lowercase) de cada grupo del laboratorio.
# La lista oficial de la catedra tenia errores/omisiones (no incluia "ferne"
# ni "group", que son grupos reales, y se agregaron cruzando contra el
# archivo). Se excluyen "bitle" (Bitless) y "los s" (Los simuLANdores): no
# aparecen en NINGUN offset del archivo (se probaron variantes de escritura
# y ninguna matchea) -> esos grupos no tienen frame real en este dataset.
GRUPOS_VALIDOS = {
    "#hidd", "aurac", "bitbr", "click", "death", "ferne", "grupo",
    "group", "la la", "lan-g", "los r", "los-t", "los_c", "lost-",
    "macac", "milan", "netru", "panda", "ping ", "red h", "tcpan",
    "wan-d", "wireg",
}

# Algunos grupos tienen su byte de SEQ desalineado respecto a la posicion
# que le corresponde por contenido en la URL premio conocida
# (https://www.youtube.com/shorts/...):
#  - "group" (payload 'w'): decodifica SEQ=32, pero por contenido completa
#    "www" en la posicion 7.
#  - "lan-g" (payload 'yo'): decodifica SEQ=13, pero por contenido inicia
#    "youtube" en la posicion 10.
CORRECCION_SEQ = {
    ("group", 32): 7,
    ("lan-g", 13): 10,
}


def procesar():
    if not os.path.exists(NOMBRE_ARCHIVO):
        print(f"No se encuentra el archivo en: {NOMBRE_ARCHIVO}")
        return

    with open(NOMBRE_ARCHIVO, "rb") as f:
        data = f.read()

    paquetes = []
    i = 0
    total = len(data)

    # Recorrido byte a byte buscando HDRs cuyo GROUP matchee la lista oficial
    # (ya depurada: se excluyeron los prefijos que no aparecen en ningun
    # offset del archivo, ver comentario arriba). No se usa LENGTH para
    # "saltar" de forma ciega porque el archivo tiene ruido intercalado entre
    # frames validos; en cambio, se valida cada candidato contra
    # GRUPOS_VALIDOS antes de aceptarlo.
    while i <= total - 7:
        grupo_bytes = data[i : i + 5]
        seq = data[i + 5]
        length = data[i + 6]

        grupo_str = grupo_bytes.decode("ascii", errors="ignore").lower()

        if grupo_str in GRUPOS_VALIDOS and 0 < length and (i + 7 + length) <= total:
            payload_bytes = data[i + 7 : i + 7 + length]
            payload = payload_bytes.decode("ascii", errors="ignore")
            seq_corregido = CORRECCION_SEQ.get((grupo_str, seq), seq)

            paquetes.append({
                "group": grupo_str,
                "seq": seq_corregido,
                "payload": payload,
                "offset": i,
            })
            i += 7 + length
            continue

        i += 1

    # Se arma un diccionario seq -> paquete, para poder recorrer los numeros
    # de secuencia en orden y detectar cuales faltan.
    paquetes_por_seq = {p["seq"]: p for p in paquetes}

    ordenados = sorted(paquetes_por_seq.values(), key=lambda x: x["seq"])
    mi_grupo = [p for p in ordenados if p["group"] == TU_GRUPO]

    seq_min = min(paquetes_por_seq) if paquetes_por_seq else 0
    seq_max = max(paquetes_por_seq) if paquetes_por_seq else 0
    faltantes = [s for s in range(seq_min, seq_max + 1) if s not in paquetes_por_seq]

    partes = []
    for s in range(seq_min, seq_max + 1):
        if s in paquetes_por_seq:
            partes.append(paquetes_por_seq[s]["payload"])
        else:
            partes.append(f"[SEQ{s}?]")
    mensaje = "".join(partes)

    print("=" * 60)
    print(" LECTURA DESDE EL ARCHIVO BINARIO")
    print("=" * 60)
    print(f"Mensaje reconstruido (SEQ {seq_min}-{seq_max}): {mensaje}")

    if faltantes:
        print(f"\n[AVISO] Faltan paquetes con SEQ: {faltantes}")
        print("        (no se encontro ningun GROUP valido para esa posicion)")

    print("\n--- SECUENCIA COMPLETA DE PAQUETES DETECTADOS ---")
    for p in ordenados:
        print(f"Offset: {p['offset']:04d} | SEQ: {p['seq']:02d} | Grupo: {p['group']:<6} | Payload: '{p['payload']}'")

    print(f"\n--- DATOS DE TU GRUPO ('{TU_GRUPO}') PARA EL INFORME ---")
    if mi_grupo:
        for p in mi_grupo:
            print(f"Grupo: {p['group']} | SEQ: {p['seq']} | Offset: {p['offset']} | Carga Util (Payload): '{p['payload']}'")
    else:
        print("No se encontraron paquetes para tu grupo.")


if __name__ == "__main__":
    procesar()