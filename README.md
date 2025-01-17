# Detección de Objetos en Tiempo Real con YOLOv4

Este proyecto implementa un sistema de **detección de objetos en tiempo real** utilizando el modelo **YOLOv4** (You Only Look Once, versión 4) y su variante más ligera, **YOLOv4-tiny**. El sistema está diseñado para identificar y clasificar múltiples objetos en imágenes y videos a través de una cámara, siendo útil en aplicaciones como vigilancia, robótica e interacción humano-computadora.

## Características

- **Modelos Utilizados:**
  - **YOLOv4**: Optimizado para velocidad y precisión.
  - **YOLOv4-tiny**: Versión más ligera para ejecución rápida en dispositivos con recursos limitados.
  
- **Integración con CocoNames**: Utiliza un archivo `coco.names` que contiene las categorías de objetos que el modelo puede detectar.

## Requisitos

- Python 3.x Posterior
- Bibliotecas necesarias:
  - OpenCV
  - numpy
  - pandas

## Instalación

### 1. Clonar el Repositorio

Clona este repositorio en tu máquina local:


### 2. Crear un Entorno Virtual

Es recomendable crear un entorno virtual para gestionar las dependencias:


### 3. Instalar Dependencias

Instala las bibliotecas necesarias:
<!-- mostrar un comando  -->
bash
pip install -r requirements.txt
bash


### 4. Configuración del Modelo

Descarga los siguientes archivos y colócalos en el directorio del proyecto:

- ```yolov4.weights```
- ```yolov4.cfg```
- ```coco.names```

Puedes encontrar estos archivos en el [repositorio oficial de YOLO](https://github.com/AlexeyAB/darknet).
Desplaza hacia abajo y busca los archivos

## Ejecución del Programa

Para iniciar la detección de objetos, ejecuta el script principal:

bash
python detecta_objetos.py 
bash

