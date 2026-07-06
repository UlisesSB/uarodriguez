# Portfolio — Ulises Agustín Rodríguez

Sitio estático (HTML/CSS/JS puro, sin build step) listo para publicar en
Cloudflare Pages.

## Estructura
```
index.html                     -> página principal (todas las secciones)
proyectos/*.html                -> ficha técnica de cada proyecto (plantillas)
assets/css/style.css             -> estilos (tema "schematic": grafito + rojo)
assets/js/main.js                -> selector de idioma, menú móvil, animaciones,
                                     filtro de proyectos, efecto de tipeo
assets/img/logo.png               -> tu logo (favicon + avatar del hero)
assets/docs/CV_Ulises_Rodriguez.pdf     -> (agregar) tu CV para el botón de descarga
assets/docs/proyectos/<slug>.pdf        -> (agregar) informe/paper de cada proyecto
build_projects.py                -> script que generó las páginas de /proyectos.
                                     Editá los datos de cada proyecto ahí y volvé
                                     a correr `python3 build_projects.py` si querés
                                     regenerarlas (pisa los archivos existentes).
```

## Cómo publicar en Cloudflare Pages
1. Subí esta carpeta completa a un repositorio de GitHub (o arrastrá el ZIP
   directo en el dashboard de Cloudflare Pages, "Deploy without Git").
2. En Cloudflare Pages: Create project -> conectar el repo (o subir carpeta).
3. Build command: (vacío, no hace falta)
   Output directory: / (raíz)
4. Conectá tu dominio custom desde la pestaña "Custom domains".

## Idioma
El sitio es bilingüe (ES/EN). Cada texto está duplicado con `lang="es"` /
`lang="en"` y el botón "ES/EN" del nav alterna el atributo `data-lang` en
`<html>`, que la hoja de estilos usa para mostrar/ocultar. Al agregar texto
nuevo, siempre duplicalo en ambos idiomas siguiendo ese mismo patrón.

## Completar contenido de cada proyecto
Cada página en /proyectos ya tiene la estructura final (hero, imagen
principal, descripción, galería de 3 imágenes, botón de informe/paper,
stack). Reemplazá los bloques marcados como "placeholder" (recuadro
punteado) por tus imágenes reales, y subí el PDF correspondiente a
assets/docs/proyectos/.

## Logos de cada proyecto
En el home, cada tarjeta de proyecto tiene un recuadro chico y punteado
(`<span class="proj-logo">`) al lado del título. El sitio ahora busca
la imagen automáticamente en varias ubicaciones típicas (ver
`assets/js/main.js`, función `loadFirstAvailableImage`), así que no
hace falta tocar el HTML — alcanza con subir el archivo. La ubicación
recomendada (la primera que se prueba) es:

```
assets/img/proyectos/<slug>.jpg
```

Con `<slug>` = el mismo nombre del archivo .html (signal, ulumiglow,
mri-glioma-yolo, transporte-riscv, db-ecommerce,
gestion-gastronomica). También revisa `proyectos/<slug>.jpg` y un
puñado de rutas más por si lo subiste en otro lugar.

## Foto de perfil
El logo del hero hace un flip automático hacia tu foto. Se busca en
varias rutas, la recomendada es:

```
assets/img/foto.jpg
```

⚠️ Los nombres de archivo son sensibles a mayúsculas/minúsculas en
Cloudflare Pages (a diferencia de Windows). "Foto.jpg" y "foto.jpg"
son archivos distintos para el servidor — si subiste uno y no aparece,
revisá que el nombre coincida exactamente (en minúsculas) con lo que
espera el sitio.
