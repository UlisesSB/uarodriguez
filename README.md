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
(`<span class="proj-logo">`) al lado del título, con un ícono genérico
de placeholder. Para poner tu propio logo (1:1, se muestra chico a
propósito para acompañar el título, no como imagen protagonista):

1. Guardá el logo en `assets/img/proyectos/<slug>.png` (ej:
   `assets/img/proyectos/signal.png`, `assets/img/proyectos/ulumiglow.png`).
2. En `index.html`, buscá la tarjeta correspondiente y reemplazá el
   contenido de `<span class="proj-logo">...</span>` por:
   `<span class="proj-logo"><img src="assets/img/proyectos/signal.png" alt="Signal"></span>`
   (ajustando el nombre de archivo). El recuadro ya está dimensionado
   (32×32px) así que la imagen se recorta sola en un cuadrado prolijo.
