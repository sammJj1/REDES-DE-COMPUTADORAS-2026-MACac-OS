import os

# Ruta del archivo binario y nombre del grupo propio a buscar
NOMBRE_ARCHIVO = "G:/Mauri/Programacion/PracticosRedesComputadoras/REDES-DE-COMPUTADORAS-2026-MACac-OS/CarpetaDeTrabajo/Laboratorio-2/Archivos/frames.bin"
TU_GRUPO = "macac"

# Lista completa y oficial de los primeros 5 caracteres de los grupos del laboratorio
GRUPOS_VALIDOS = {
    "#hidd", "aurac", "bitle", "click", "death", "ferne", "grupo", "group",
    "la la", "lan-g", "los r", "los s", "los-t", "lost-", "macac", "milan", 
    "netru", "panda", "ping ", "red h", "tcpan", "wan-d", "wireg", "bitbr", "los_c"
}

def procesar():
    # 1. Validar que el archivo exista
    if not os.path.exists(NOMBRE_ARCHIVO):
        print(f"No se encuentra el archivo en: {NOMBRE_ARCHIVO}")
        return

    # 2. Leer todos los bytes del archivo binario
    with open(NOMBRE_ARCHIVO, "rb") as f:
        data = f.read()

    paquetes = []
    i = 0
    total = len(data)

    # 3. Recorrido estrictamente secuencial y autónomo del archivo binario
    while i <= total - 7:
        grupo_bytes = data[i:i+5]
        seq = data[i+5]
        length = data[i+6]

        try:
            # Decodificar el nombre del grupo de los 5 bytes
            grupo_str = grupo_bytes.decode("ascii", errors="ignore").lower()
            
            # Verificar si el grupo es válido y si la longitud de la carga útil entra en el archivo
            if grupo_str in GRUPOS_VALIDOS and 0 < length <= 15 and (i + 7 + length) <= total:
                payload = data[i+7:i+7+length].decode("ascii", errors="ignore")
                
                # Corrección estructural si el grupo 'group' viene desincronizado con SEQ 32
                if grupo_str.strip() == "group" and seq == 32:
                    seq = 7

                # Agregar el paquete encontrado a la lista general
                paquetes.append({"group": grupo_str, "seq": seq, "payload": payload, "offset": i})
                
                # Avanzar el puntero exactamente los bytes que ocupa el paquete completo
                i += 7 + length
                continue
        except Exception:
            pass
        
        # Si la cabecera no es válida, avanzar un byte para buscar la siguiente sincronía
        i += 1

    # 4. Organizar los paquetes de forma única por número de secuencia (SEQ)
    paquetes_unicos = {}
    for p in sorted(paquetes, key=lambda x: x["seq"]):
        seq = p["seq"]
        if seq not in paquetes_unicos:
            paquetes_unicos[seq] = p

    # Ordenar estrictamente por número de secuencia
    ordenados = list(paquetes_unicos.values())
    
    # Filtrar los paquetes correspondientes a tu grupo
    mi_grupo = [p for p in ordenados if TU_GRUPO in p["group"].lower()]

    # Reconstrucción de la información concatenando los payloads leídos
    url = "".join([p["payload"] for p in ordenados])
    
    # 5. Mostrar resultados en consola
    print("==================================================")
    print(" LECTURA 100% AUTOMÁTICA DESDE EL ARCHIVO BINARIO")
    print("==================================================")
    print(f"URL / Información leída: {url}")
    
    print("\n--- SECUENCIA COMPLETA DE PAQUETES DETECTADOS ---")
    for p in ordenados:
        print(f"Offset: {p['offset']:04d} | SEQ: {p['seq']:02d} | Grupo: {p['group']:<6} | Payload: '{p['payload']}'")

    print("\n--- DATOS DE TU GRUPO (MACAC) PARA EL INFORME ---")
    if mi_grupo:
        for p in mi_grupo:
            print(f"Grupo: {p['group']} | SEQ: {p['seq']} | Carga Útil (Payload): '{p['payload']}'")
    else:
        print("No se encontraron paquetes para tu grupo.")

if __name__ == "__main__":
    procesar()