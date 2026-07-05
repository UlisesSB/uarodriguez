# -*- coding: utf-8 -*-
import os

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "proyectos")

TEMPLATE = """<!DOCTYPE html>
<html lang="es" data-lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title_es} — Ulises Rodríguez</title>
<meta name="description" content="{summary_es_plain}">
<link rel="icon" href="../assets/img/logo.png">
<link rel="stylesheet" href="../assets/css/style.css">
</head>
<body>

<!-- ============ NAV ============ -->
<nav class="nav">
  <div class="nav-inner">
    <a href="../index.html#top" class="nav-brand">
      <img src="../assets/img/logo.png" alt="Logo Ulises Rodriguez">
      <span>
        Ulises Rodríguez
        <small>SB · Ing. en Computación</small>
      </span>
    </a>
    <ul class="nav-links">
      <li><a href="../index.html#perfil" lang="es">Perfil</a><a href="../index.html#perfil" lang="en">Profile</a></li>
      <li><a href="../index.html#habilidades" lang="es">Habilidades</a><a href="../index.html#habilidades" lang="en">Skills</a></li>
      <li><a href="../index.html#experiencia" lang="es">Experiencia</a><a href="../index.html#experiencia" lang="en">Experience</a></li>
      <li><a href="../index.html#proyectos" lang="es">Proyectos</a><a href="../index.html#proyectos" lang="en">Projects</a></li>
      <li><a href="../index.html#educacion" lang="es">Educación</a><a href="../index.html#educacion" lang="en">Education</a></li>
      <li><a href="../index.html#contacto" lang="es">Contacto</a><a href="../index.html#contacto" lang="en">Contact</a></li>
    </ul>
    <div class="nav-actions">
      <button class="lang-toggle" aria-label="Cambiar idioma / Switch language">
        <span class="l-es">ES</span>/<span class="l-en">EN</span>
      </button>
      <button class="nav-toggle" aria-label="Menu">
        <span></span><span></span><span></span>
      </button>
    </div>
  </div>
</nav>

<!-- ============ PROJECT HERO ============ -->
<header class="proj-hero">
  <div class="container">
    <a href="../index.html#proyectos" class="back-link">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 12H5M11 18l-6-6 6-6"/></svg>
      <span lang="es">Volver a proyectos</span><span lang="en">Back to projects</span>
    </a>
    <p class="eyebrow"><span class="sheet">{sheet_code}</span> <span lang="es">{category_es}</span><span lang="en">{category_en}</span></p>
    <h1 lang="es">{title_es}</h1>
    <h1 lang="en">{title_en}</h1>
    <p class="hero-desc" lang="es">{summary_es}</p>
    <p class="hero-desc" lang="en">{summary_en}</p>

    <div class="proj-hero-meta">
      <div class="item">
        <small lang="es">PERÍODO</small><small lang="en">PERIOD</small>
        <span>{date_es}</span>
      </div>
      <div class="item">
        <small lang="es">TIPO</small><small lang="en">TYPE</small>
        <span lang="es">{type_es}</span><span lang="en">{type_en}</span>
      </div>
      <div class="item">
        <small lang="es">STACK</small><small lang="en">STACK</small>
        <span>{stack_short}</span>
      </div>
    </div>
  </div>
</header>

<!-- ============ MAIN MEDIA ============ -->
<section style="padding-top:56px;">
  <div class="container">
    <div class="media-placeholder reveal">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><path d="M21 15l-5-5L5 21"/></svg>
      <span lang="es">Imagen principal del proyecto — reemplazar este bloque al subir contenido</span>
      <span lang="en">Main project image — replace this block when uploading content</span>
    </div>
  </div>
</section>

<!-- ============ BODY ============ -->
<section>
  <div class="container proj-body">
    <div class="reveal">
      <h2 lang="es">Descripción del proyecto</h2>
      <h2 lang="en">Project description</h2>
      <p style="color:var(--text-dim);margin-bottom:22px;" lang="es">{long_es}</p>
      <p style="color:var(--text-dim);margin-bottom:22px;" lang="en">{long_en}</p>
      <p class="placeholder-text" lang="es">Espacio reservado para la descripción técnica completa, decisiones de diseño, desafíos y resultados. Se completará al subir el informe/paper correspondiente.</p>
      <p class="placeholder-text" lang="en">Reserved space for the full technical write-up, design decisions, challenges and results. To be completed once the corresponding report/paper is uploaded.</p>

      <h2 style="margin-top:48px;" lang="es">Galería</h2>
      <h2 style="margin-top:48px;" lang="en">Gallery</h2>
      <div class="gallery-grid reveal">
        <div class="media-placeholder">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><path d="M21 15l-5-5L5 21"/></svg>
          <span lang="es">Imagen 1</span><span lang="en">Image 1</span>
        </div>
        <div class="media-placeholder">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><path d="M21 15l-5-5L5 21"/></svg>
          <span lang="es">Imagen 2</span><span lang="en">Image 2</span>
        </div>
        <div class="media-placeholder">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><path d="M21 15l-5-5L5 21"/></svg>
          <span lang="es">Imagen 3</span><span lang="en">Image 3</span>
        </div>
      </div>
    </div>

    <aside class="proj-side reveal">
      <div class="card">
        <h4 lang="es">Documentación</h4>
        <h4 lang="en">Documentation</h4>
        <a href="../assets/docs/proyectos/{slug}.pdf" class="btn btn-primary report-btn">
          <span lang="es">Descargar informe / paper</span><span lang="en">Download report / paper</span>
        </a>
        {repo_button}
      </div>
      <div class="card">
        <h4 lang="es">Tecnologías</h4>
        <h4 lang="en">Technologies</h4>
        <div class="tags">
          {tags_html}
        </div>
      </div>
    </aside>
  </div>
</section>

<footer>
  <div class="container footer-inner">
    <span>© <span data-year></span> Ulises Agustín Rodríguez — <span lang="es">Aguilares, Tucumán, Argentina</span><span lang="en">Aguilares, Tucumán, Argentina</span></span>
    <span>REV 1.0 · BUILD/2026</span>
  </div>
</footer>

<script src="../assets/js/main.js"></script>
</body>
</html>
"""

def tag(t):
    return '<span class="tag">{}</span>'.format(t)

projects = [
    dict(
        slug="ulisesglow",
        sheet_code="PRJ.01",
        title_es='Ambilight "UlisesGlow"',
        title_en='Ambilight "UlisesGlow"',
        category_es="Hardware &amp; software · Proyecto personal",
        category_en="Hardware &amp; software · Personal project",
        type_es="Proyecto personal / código abierto",
        type_en="Personal project / open source",
        date_es="2024 — 2025",
        stack_short="ESP32 · PWM · Python",
        summary_es='Sistema de iluminación ambiental sincronizada con el contenido de la pantalla, desarrollado de punta a punta: electrónica, firmware y software de escritorio.',
        summary_en='Ambient lighting system synchronized to on-screen content, developed end to end: electronics, firmware and desktop software.',
        long_es='Desarrollo integral de hardware y software para iluminación ambiental sincronizada. Incluye programación de firmware para ESP32 (control PWM), una aplicación de escritorio en Python para el procesamiento de imágenes en tiempo real, comunicación serial entre software y microcontrolador, y empaquetado de binarios de instalación para Windows. Se diseñó y ejecutó también la etapa de potencia del circuito. El proyecto es de código abierto: diseño de PCB y esquema de conexión electrónica disponibles en GitHub.',
        long_en='End-to-end hardware and software development for synchronized ambient lighting. Includes ESP32 firmware programming (PWM control), a Python desktop application for real-time image processing, serial communication between software and microcontroller, and packaged Windows installers. The circuit\'s power stage was also designed and built in-house. The project is open source: PCB design and wiring schematics are available on GitHub.',
        tags=["ESP32","PWM","Python","Comunicación serial","Diseño de PCB","Etapa de potencia"],
        repo="https://github.com/UlisesSB",
    ),
    dict(
        slug="transporte-riscv",
        sheet_code="PRJ.02",
        title_es="Sistema de gestión para transporte (RISC-V)",
        title_en="Transit fare-management system (RISC-V)",
        category_es="Sistemas con microprocesadores",
        category_en="Microprocessor systems",
        type_es="Proyecto académico",
        type_en="Academic project",
        date_es="Cátedra de Sistemas con Microprocesadores",
        stack_short="RISC-V · Assembly",
        summary_es='Diseño teórico, simulación y programación de bajo nivel sobre arquitectura RISC-V aplicados a un servicio de transporte público.',
        summary_en='Theoretical design, simulation and low-level programming on RISC-V architecture applied to a public-transit service.',
        long_es='Diseño teórico, simulación y programación de bajo nivel basados en arquitectura RISC-V para un servicio de transporte. Desarrollo de la lógica interna de cobro, conteo de pasajeros y geolocalización, interactuando directamente con registros y protocolos de comunicación de hardware.',
        long_en='Theoretical design, simulation and low-level programming based on RISC-V architecture for a transit service. Development of the internal fare-collection logic, passenger counting and geolocation, interacting directly with hardware registers and communication protocols.',
        tags=["RISC-V","Assembly","Simulación","Registros de hardware","Protocolos de comunicación"],
        repo=None,
    ),
    dict(
        slug="db-ecommerce",
        sheet_code="PRJ.03",
        title_es="Arquitectura de base de datos para e-commerce",
        title_en="Database architecture for e-commerce",
        category_es="Bases de datos",
        category_en="Databases",
        type_es="Proyecto académico",
        type_en="Academic project",
        date_es="Cátedra de Base de Datos",
        stack_short="SQL · MongoDB",
        summary_es='Diseño e implementación de una base de datos híbrida SQL/NoSQL con foco en seguridad, roles y consultas analíticas.',
        summary_en='Design and implementation of a hybrid SQL/NoSQL database focused on security, roles and analytical queries.',
        long_es='Diseño conceptual, lógico e implementación física de una base de datos híbrida utilizando SQL (InnoDB) y NoSQL (MongoDB). Creación de consultas analíticas, gestión de permisos por roles de usuario y aplicación de seguridad de datos mediante hashing SHA-256 con salt.',
        long_en='Conceptual and logical design, and physical implementation of a hybrid database using SQL (InnoDB) and NoSQL (MongoDB). Creation of analytical queries, role-based user permission management, and data security through SHA-256 hashing with salt.',
        tags=["SQL (InnoDB)","MongoDB","Modelado de datos","SHA-256","Gestión de roles"],
        repo=None,
    ),
    dict(
        slug="gestion-gastronomica",
        sheet_code="PRJ.04",
        title_es="Sistema de gestión para establecimiento gastronómico",
        title_en="Restaurant management system",
        category_es="Ingeniería de software",
        category_en="Software engineering",
        type_es="Proyecto académico",
        type_en="Academic project",
        date_es="Cátedra de Ingeniería de Software",
        stack_short="Aplicación web · Base de datos",
        summary_es='Aplicación web para la gestión integral de un establecimiento gastronómico, cubriendo todo el ciclo de ingeniería de software.',
        summary_en='Web application for the end-to-end management of a food-service establishment, covering the full software-engineering lifecycle.',
        long_es='Desarrollo integral de la ingeniería de software asociada a la documentación, implementación y diseño de una aplicación web para la gestión de un establecimiento gastronómico, junto con el diseño de su base de datos. Abarca desde el relevamiento y especificación de requisitos hasta el diseño de la arquitectura de datos y la implementación funcional del sistema.',
        long_en='Full software-engineering lifecycle covering documentation, design and implementation of a web application for managing a food-service establishment, along with its database design. Spans requirements gathering and specification through to data architecture design and functional implementation.',
        tags=["Aplicación web","Base de datos","Documentación técnica","UML"],
        repo=None,
    ),
    dict(
        slug="mri-glioma-yolo",
        sheet_code="PRJ.05",
        title_es="Clasificación binaria de gliomas en imágenes de MRI",
        title_en="Binary glioma classification in brain MRI",
        category_es="Inteligencia artificial",
        category_en="Artificial intelligence",
        type_es="Proyecto académico",
        type_en="Academic project",
        date_es="Proyecto académico independiente",
        stack_short="YOLO · Python",
        summary_es='Modelo de visión por computadora para la detección binaria de gliomas en resonancias magnéticas cerebrales.',
        summary_en='Computer-vision model for binary glioma detection in brain MRI scans.',
        long_es='Desarrollo de un modelo de clasificación binaria sobre imágenes de resonancia magnética (MRI) del cerebro, orientado a reconocer la presencia de gliomas, utilizando la familia de arquitecturas de IA YOLO adaptada a la clasificación de imágenes médicas.',
        long_en='Development of a binary classification model over brain magnetic resonance imaging (MRI), aimed at recognizing the presence of gliomas, using the YOLO family of AI architectures adapted for medical image classification.',
        tags=["YOLO","Python","Deep Learning","Procesamiento de imágenes médicas"],
        repo=None,
    ),
    dict(
        slug="signal",
        sheet_code="PRJ.06",
        title_es='"Signal" — Circuito audiorrítmico',
        title_en='"Signal" — Audio-reactive circuit',
        category_es="Electrónica · Proyecto personal",
        category_en="Electronics · Personal project",
        type_es="Proyecto personal",
        type_en="Personal project",
        date_es="Proyecto personal",
        stack_short="Electrónica analógica · PCB",
        summary_es='Circuito 100% electrónico que ajusta volumen de audio y controla luces intermitentes reactivas a agudos, medios y graves.',
        summary_en='Fully electronic circuit that adjusts audio volume and drives intermittent lights reacting to highs, mids and lows.',
        long_es='Circuito completamente electrónico que, a partir de una entrada de audio, permite ajustar el volumen mientras un set de luces reacciona de forma intermitente a los agudos, medios y graves de la señal. Se realizó el diseño electrónico de todas las etapas del circuito, el diseño y la fabricación manual de las placas de cobre correspondientes, la soldadura y el cálculo de componentes, además del modelado e impresión 3D de la carcasa.',
        long_en='A fully electronic circuit that, from an audio input, allows volume adjustment while a set of lights reacts intermittently to the highs, mids and lows of the signal. The project included the electronic design of every stage of the circuit, the design and hand-fabrication of the corresponding copper boards, soldering and component calculation, plus 3D modeling and printing of the enclosure.',
        tags=["Electrónica analógica","Fabricación de PCB","Soldadura","Modelado 3D","Impresión 3D"],
        repo=None,
    ),
]

os.makedirs(OUT, exist_ok=True)

for p in projects:
    tags_html = "\n          ".join(tag(t) for t in p["tags"])
    if p["repo"]:
        repo_button = (
            '<a href="{repo}" target="_blank" rel="noopener" class="btn report-btn">'
            '<span lang="es">Ver repositorio</span><span lang="en">View repository</span></a>'
        ).format(repo=p["repo"])
    else:
        repo_button = (
            '<a href="#" class="btn report-btn" style="opacity:.5;pointer-events:none;">'
            '<span lang="es">Repositorio (próximamente)</span><span lang="en">Repository (coming soon)</span></a>'
        )

    html = TEMPLATE.format(
        slug=p["slug"],
        sheet_code=p["sheet_code"],
        title_es=p["title_es"],
        title_en=p["title_en"],
        category_es=p["category_es"],
        category_en=p["category_en"],
        type_es=p["type_es"],
        type_en=p["type_en"],
        date_es=p["date_es"],
        stack_short=p["stack_short"],
        summary_es=p["summary_es"],
        summary_en=p["summary_en"],
        summary_es_plain=p["summary_es"],
        long_es=p["long_es"],
        long_en=p["long_en"],
        tags_html=tags_html,
        repo_button=repo_button,
    )
    with open(os.path.join(OUT, p["slug"] + ".html"), "w", encoding="utf-8") as f:
        f.write(html)

print("OK -", len(projects), "project pages generated")
