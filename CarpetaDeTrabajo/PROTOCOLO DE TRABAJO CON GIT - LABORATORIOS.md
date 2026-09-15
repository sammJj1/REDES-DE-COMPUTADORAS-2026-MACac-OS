# 🚀 Protocolo de Git - Trabajos Prácticos y Laboratorios

### 1. Estructura Obligatoria de Carpetas
Cada trabajo práctico/laboratorio y sus consignas deben organizarse de la siguiente manera. No se admiten archivos sueltos ni nombres alternativos.
```text
/Laboratorio_X/ (o /TP_X/)
  ├── /consigna-1/
  │    ├── consigna-1.md
  │    └── /Imagenes/
  ├── /consigna-2/
  │    ├── consigna-2.md
  │    └── /Imagenes/
  └── ...
```
* **Imágenes:** Van **únicamente** dentro de la carpeta `Imagenes` de su respectiva consigna (ej. `/Laboratorio_2/consigna-4/Imagenes/`).

---

### 2. Regla de Oro: Una Consigna = Una Branch
* **La branch representa a la consigna, no a la persona.** 
* Nomenclatura obligatoria: `TP-[número]-consigna-x` (ej: `TP-2-consigna-4`).
* Si varias personas trabajan en la misma consigna, **todos usan exactamente la misma branch** y editan el mismo archivo (`consigna-x.md`).
* ❌ **Prohibido:** Crear branches personales (`TP-2-consigna-4-juan`) ni duplicar archivos Markdown (`consigna-4-juan.md`).

---

### 3. Flujo de Trabajo Diario
1. **Actualizar:** Antes de arrancar, bajá los últimos cambios de tu equipo desde la branch de la consigna:
   ```bash
   git pull origin TP-[número]-consigna-x
   ```
2. **Trabajar:** Hacé tus cambios, subí tus commits y hacé `push` a esa misma branch:
   ```bash
   git add .
   git commit -m "mensaje descriptivo"
   git push origin TP-[número]-consigna-x
   ```
3. **Conflictos internos:** Si hay choques entre compañeros de la misma consigna, **se resuelven obligatoriamente dentro de la branch de esa consigna**.

---

### 4. Integración y Pull Requests
1. **Hacia la branch intermedia:** Una vez terminada y sin conflictos la consigna en su branch, se hace un Pull Request hacia la branch general del trabajo práctico (ej. **`LABORATORIO 2`** o **`TP 2`**), donde se van uniendo todas las consignas.
2. **Hacia `main`:** Recién cuando todas las consignas están integradas y revisadas en la branch general del trabajo, se hace el Pull Request final hacia `main`.