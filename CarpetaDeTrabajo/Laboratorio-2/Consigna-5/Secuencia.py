import os

# Ruta de tu archivo binario
NOMBRE_ARCHIVO = "G:/Mauri/Programacion/PracticosRedesComputadoras/REDES-DE-COMPUTADORAS-2026-MACac-OS/CarpetaDeTrabajo/Laboratorio-2/Archivos/frames.bin"

def buscar_por_secuencia():
    if not os.path.exists(NOMBRE_ARCHIVO):
        print(f"No se encuentra el archivo en: {NOMBRE_ARCHIVO}")
        return

    with open(NOMBRE_ARCHIVO, "rb") as f:
        data = f.read()

    print("==================================================")
    print(" INSPECCIÓN PURA POR NÚMERO DE SECUENCIA (SEQ)")
    print("==================================================")

    paquetes_encontrados = {}
    i = 0
    total = len(data)

    # Recorremos el archivo buscando paquetes de forma estructural
    while i <= total - 7:
        grupo_bytes = data[i:i+5]
        seq = data[i+5]
        length = data[i+6]

        try:
            # Validamos que el length sea coherente (entre 1 y 15 bytes) y entre en el archivo
            if 0 < length <= 15 and (i + 7 + length) <= total:
                # Si el SEQ está dentro del rango que nos interesa (1 a 25)
                if 1 <= seq <= 25:
                    grupo_str = grupo_bytes.decode("ascii", errors="replace")
                    payload = data[i+7:i+7+length].decode("ascii", errors="replace")
                    
                    # Guardamos el hallazgo
                    if seq not in paquetes_encontrados:
                        paquetes_encontrados[seq] = []
                    paquetes_encontrados[seq].append({
                        "grupo_leido": grupo_str,
                        "payload": payload,
                        "offset": i
                    })
                
                i += 7 + length
                continue
        except Exception:
            pass
        
        i += 1

    # Mostramos los resultados ordenados por SEQ del 1 al 25
    for s in range(1, 26):
        if s in paquetes_encontrados:
            print(f"\n--- SECUENCIA (SEQ): {s:02d} ---")
            for p in paquetes_encontrados[s]:
                print(f"  -> Offset: {p['offset']:04d} | Grupo Leído (5 bytes): '{p['grupo_leido']}' | Payload: '{p['payload']}'")
        else:
            print(f"\n--- SECUENCIA (SEQ): {s:02d} --- [NO ENCONTRADA DIRECTAMENTE]")

if __name__ == "__main__":
    buscar_por_secuencia()