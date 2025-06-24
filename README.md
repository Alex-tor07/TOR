# TOR - Entorno  Modular para Desarrollo Web y Monitorización

TOR es una herramienta desarrollada en Python que automatiza la creación y gestión de entornos Docker para desarrollo web y monitorización. Incluye una interfaz gráfica (GUI) construida con Tkinter, que permite lanzar contenedores, gestionar servicios y visualizar métricas y logs de forma sencilla.

## 🔧 Tecnologías utilizadas

- **Docker & Docker Compose**
- **Python** (API + GUI con Tkinter)
- **Apache, PHP, MySQL, PhpMyAdmin**
- **Bind9 para DNS local**
- **Prometheus, Grafana, Telegraf, Loki, InfluxDB** para monitorización
- **Gedit**, scripts Bash, redes virtuales

## 🧪 Características

- Creación de entornos modulares:
  - Entorno web (Laravel, WordPress u otros)
  - Entorno de monitorización completo
- Gestión de contenedores desde una API gráfica
- Automatización de despliegues desde scripts
- Terminal embebida para ejecutar comandos dentro del contenedor principal (server)
- Reinicio de servicios y visualización de logs
- Botón “Ayuda” con apuntes personalizados

## 🎯 Objetivo

Este proyecto fue desarrollado como Trabajo de Fin de Grado del ciclo ASIR. Busca simular un entorno DevOps real para desarrolladores y administradores de sistemas, con herramientas modernas y automatización.

## 📦 Instalación

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/Alex-tor07/TOR
2. Instalar las imágenes de Docker necesarias y configurar un entorno de Python aislado del sistema anfitrión.
   ```bash
   cd TOR/instaladores
   ./entorno_api.sh
   ./img_entorno.sh
 3. Ejecución de la API.
    ```bash
     cd TOR
     ./run_api.sh
 4. Directorios para desarrolla los proyectos web.
     ```bash
     cd TOR/entornos/desarrollo_web/disco_duro/server_m/datos/localhost/ 
     cd TOR/entornos/desarrollo_web/disco_duro/server_m/datos/public_html
   
 5. Leer la ayuda de la API, para conocer puertos red y contraseñas.

## 🔧 Requisitos
 - Sistema Linux
 - Docker
 - python
 - gedit
## 🎥 Video sobre el proyecto
[![Logo del video](https://img.youtube.com/vi/mXYSBbR64i0/0.jpg)](https://youtu.be/mXYSBbR64i0)
