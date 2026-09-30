# NOVA Growth Solutions: guía del sitio web

## 1. Qué hay en el paquete

| Archivo | Para qué sirve |
|---|---|
| `index.html` | El sitio completo en un solo archivo, con fuentes e imágenes incluidas. Funciona sin internet. |
| `og-image.jpg` | La imagen que aparece al compartir el enlace en WhatsApp, Facebook, LinkedIn o X. |
| `logo.png` | El logo que Google usa en los datos del negocio. |
| `sitemap.xml` y `robots.txt` | Ayudan a Google a encontrar el sitio. |
| `CNAME` | Le dice a GitHub Pages que use `novagrowth.solutions`. |
| `fuente/` | Los bloques originales, por si quieres pedirme cambios grandes más adelante. **No hace falta subir esta carpeta.** |

Los 6 primeros archivos van juntos en la misma carpeta al publicar.

---

## 2. Antes y después de publicar

### A. Dominio: ✅ `novagrowth.solutions` ya incluido

- El dominio ya está en el canonical, en las etiquetas para redes y en los datos para Google (schema). También está en `sitemap.xml` y `robots.txt`.
- El paquete trae un archivo **`CNAME`** con `novagrowth.solutions`. Súbelo junto con los demás archivos para que GitHub Pages reconozca el dominio automáticamente.
- En tu proveedor de dominio crea estos registros DNS:

  | Tipo | Nombre | Valor |
  |---|---|---|
  | A | @ | `185.199.108.153` |
  | A | @ | `185.199.109.153` |
  | A | @ | `185.199.110.153` |
  | A | @ | `185.199.111.153` |
  | CNAME | www | `TU-USUARIO.github.io` |

- Cuando el dominio funcione, activa **Enforce HTTPS** en Settings → Pages.

### B. Formulario (Formspree): ✅ conectado

- El formulario ya envía a `https://formspree.io/f/xljdvojz`.
- **Haz una prueba cuando el sitio esté publicado.** La primera vez, Formspree te pedirá confirmar el correo `growthsolutionsnova@gmail.com`.
- Si la persona hizo el **Growth Leak Check**, el resultado llega dentro del mensaje en el campo `leak_check`.
- Para cambiar de formulario en el futuro, busca `formspree.io/f/xljdvojz` en `index.html` y reemplaza el código.

### C. Publicar en GitHub Pages

1. Crea un repositorio público en GitHub, por ejemplo `nova-website`.
2. Sube los 6 archivos: `index.html`, `og-image.jpg`, `logo.png`, `sitemap.xml`, `robots.txt` y `CNAME`.
3. Ve a **Settings → Pages**. En **Source** elige **Deploy from a branch**, la rama `main` y la carpeta `/root`, y guarda.
4. En **Custom domain** debería aparecer `novagrowth.solutions` (lo toma del archivo `CNAME`). Configura el DNS como en el punto A y activa **Enforce HTTPS**.
5. Cuando esté en línea, entra a **Google Search Console**, agrega `novagrowth.solutions` y envía `https://novagrowth.solutions/sitemap.xml`.

---

## 3. Cómo actualizar lo más común

Todos los cambios se hacen en `index.html` con **Buscar y reemplazar**. Revisa el conteo de coincidencias para no dejar ninguna.

### Teléfono (aparece en 4 formatos)

| Formato | Veces | Uso |
|---|---|---|
| `(704) 390-4390` | 5 | Texto visible |
| `tel:+17043904390` | 5 | Botones de llamar |
| `wa.me/17043904390` | 6 | Botones de WhatsApp |
| `+1-704-390-4390` | 2 | Datos para Google |

### Correo

Busca `growthsolutionsnova@gmail.com` y reemplázalo (10 veces).

### Horario

Busca `Mon–Fri · 8 AM – 6 PM`. Hay que cambiarlo en tres partes:

- En el texto visible en inglés.
- En las traducciones: `Lun–Vie · 8 AM – 6 PM` (español) y `Seg–Sex · 8h – 18h` (portugués).
- En los datos para Google: busca `"opens": "08:00"` y `"closes": "18:00"`, que aparecen 2 veces cada uno.

### Cupos del Growth Plan (opcional)

La cuenta regresiva al cierre del mes funciona sola.

Si algún mes quieren mostrar también **los cupos que realmente quedan**:

1. Busca `data-left=""`.
2. Pon el número real, por ejemplo `data-left="3"`.
3. Aparece el medidor "3 of 7 open".
4. Para ocultarlo otra vez, déjalo vacío.

Usen solo el número real. Un número inventado es publicidad engañosa y resta confianza.

### Activar testimonios (cuando tengan citas reales)

1. Busca `id="testimonials"` y borra la palabra `hidden` que está en esa misma línea.
2. Reemplaza los textos entre corchetes:
   - `[Real quote from ...]` por la cita.
   - `[Name]` por el nombre.
   - `[Month Year]` por el mes y año.
3. Para agregar más testimonios, copia un bloque `<figure class="tcard">…</figure>` completo y edítalo.

### Fotos de Quéren y David

1. Guarda las fotos como `queren.jpg` y `david.jpg`, verticales, de unos 600×800 px y menos de 150 KB cada una. Súbelas junto a `index.html`.
2. Busca `<span class="founder__mono" aria-hidden="true">QB</span>` y reemplázalo por:
   `<img src="queren.jpg" alt="Quéren Barbosa, co-founder of NOVA" loading="lazy">`
3. Haz lo mismo con `DV` y `david.jpg`.

### Redes sociales (cuando existan)

En el footer busca el comentario `<!-- SOCIAL:` y agrega debajo una línea por red:
`<li><a href="https://instagram.com/tuusuario" target="_blank" rel="noopener">Instagram</a></li>`

### Cambiar un texto (y sus traducciones)

1. Busca el texto en inglés y cámbialo. Aparece en el contenido visible.
2. El mismo texto aparece también dentro de `const I18N = {`, una vez en `"es"` y otra en `"pt"`. Ahí cambia la clave en inglés (a la izquierda) y la traducción (a la derecha).
3. Si solo cambias el inglés, esa frase queda en inglés al elegir ES o PT. El sitio no se rompe.

### Idiomas

- El sitio **siempre abre en inglés**. El visitante cambia con los botones **EN · ES · PT**.
- Para compartir un enlace directo en otro idioma, agrega `?lang=es` o `?lang=pt` al final. Por ejemplo: `https://novagrowthsolutions.com/?lang=es`.

---

## 4. Palabras clave de SEO usadas

**Locales (Charlotte):**

1. small business marketing Charlotte NC
2. website design Charlotte NC
3. local SEO Charlotte
4. marketing agency Charlotte NC
5. business automation Charlotte
6. Google Business Profile optimization Charlotte
7. CRM setup for small business (Charlotte)

**Nacionales y de nicho:**

8. business growth partner
9. small business growth consulting
10. marketing for home service businesses
11. contractor marketing agency
12. lead follow-up automation
13. AI automation for small business
14. custom software for small business
15. free growth plan / free marketing audit

Están en el título, la meta descripción, las meta keywords, los encabezados, el FAQ y los datos estructurados.

Conviene validar el volumen real de estas búsquedas en Google Keyword Planner después del lanzamiento.

---

## 5. Resultado de la revisión final

| Prueba | Resultado |
|---|---|
| Lighthouse escritorio | Rendimiento 99 · Accesibilidad 100 · Buenas prácticas 100 · SEO 92 en la prueba local (sube a 100 con el dominio ya incluido) |
| Lighthouse móvil (4G lento simulado, con gzip) | Rendimiento 90 · Accesibilidad 100 · Buenas prácticas 100 · SEO 92 |
| Auditoría de accesibilidad (axe, WCAG 2.1 AA) | 0 errores en modo claro, oscuro y móvil |
| JSON-LD (datos para Google) | Válido: ProfessionalService, ItemList de servicios, FAQPage (11 preguntas) y BreadcrumbList |
| Encabezados | 1 solo H1, luego H2 y H3 en orden lógico |
| Imágenes | 4 capturas con carga diferida y texto alternativo, de 26 a 57 KB cada una |
| Sin JavaScript | Todo el contenido visible; el formulario envía por el método normal |
| Consola | Sin errores |
| Scroll horizontal | Ninguno, de 320 px a 1440 px |
| Peso del archivo | 606 KB (unos 340 KB comprimido, que es lo que descarga el visitante en GitHub Pages) |

---

## 6. Ideas para después

- **SEO en español y portugués:** hoy Google indexa sobre todo la versión en inglés, porque todo está en un solo archivo. Para posicionar en búsquedas en ES/PT conviene crear páginas separadas (`/es/` y `/pt/`).
- **Casos con números:** cuando tengan datos medibles de sus clientes (más llamadas, más reseñas), agréguenlos en la línea "Result" de cada caso.
- **Google Business Profile de NOVA:** créenlo con la misma dirección, teléfono y horario del sitio.
