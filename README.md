# REDES-DE-COMPUTADORAS-2026-MACac-OS
### Instalación de Packet Tracer en Arch Linux (08-2026)

1. Iniciar sesión (con la cuenta de la UNC) en [netacad.com/resources/lab-downloads](https://www.netacad.com/resources/lab-downloads?courseLang=en-US)

2. Desplazarse hasta la opción **Cisco Packet Tracer**, en la sección de `Learning Resources`

3. Descargar la opción de Packet Tracer para `Ubuntu 64bit` (vas a terminar descargando algo como `CiscoPacketTracer_901_Ubuntu_64bit.deb`)

4. Descarga el `PKGBUILD` (la receta para instalar lo que descargamos de la web oficial)

   **4.1** Para descargarlo hace, donde mas te pinte:
   ```bash
   git clone --branch packettracer --single-branch https://github.com/archlinux/aur.git packettracer
   ```

   **4.2** Ahora tenes que modificar el `PKGBUILD` para la version del archivo .deb que descargamos. En la dirección que te pintó hace:
   ```bash
   sed -i 's/pkgver=9.0.0/pkgver=9.0.1/' PKGBUILD
   ```
   O modificalo con `nano PKGBUILD`

   **4.3** Copia el archivo .deb descargado de la web oficial a la carpeta donde está el `PKGBUILD`, por ejemplo en mi caso fué:
   ```bash
   cp ~Descargas/CiscoPacketTracer_901_Ubuntu_64bit.deb ~/Facultad-app/packettracer/
   ```

5. Ahora que tenés el `PKGBUILD` descargado de GitHub y el archivo .deb en el mismo directorio, ejecuta:
   ```bash
   makepkg -sic
   ```

6. Aceptar las licencias. Hace:
   ```bash
   mkdir -p ~/.local/share/applications
   /usr/lib/packettracer/packettracer.AppImage
   ```
   Capaz te pide `fuse2` y vos tengas otro, hace:
   ```bash
   sudo pacman -S fuse2
   ```
   e intentá nuevamente los comandos anteriores.
 7. Acepta la licencia.
 8. Se va a ejecutar packet tracer, necesitas iniciar sesión por primera vez.
 9. Listo, ya te debería salir en tu launcher de aplicaciones.
