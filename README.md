
# Detección de Objetos en Tiempo Real con YOLOv4

Este proyecto implementa un sistema de **detección de objetos en tiempo real** utilizando el modelo **YOLOv4** (You Only Look Once, versión 4) y su variante más ligera, **YOLOv4-tiny**. El sistema está diseñado para identificar y clasificar múltiples objetos en imágenes y videos a través de una cámara, siendo útil en aplicaciones como vigilancia, robótica e interacción humano-computadora.

---

## Características

- **Modelos Utilizados:**
  - **YOLOv4**: Optimizado para velocidad y precisión.
  - **YOLOv4-tiny**: Versión más ligera para ejecución rápida en dispositivos con recursos limitados.
  
- **Integración con CocoNames:**  
  Utiliza un archivo `coco.names` que contiene las categorías de objetos que el modelo puede detectar.

---

## Requisitos

- Python 3.x (o posterior).
- Bibliotecas necesarias:
  - `OpenCV`
  - `numpy`
  - `pandas`

---

## Instalación

### 1. Clonar el Repositorio

Clona este repositorio en tu máquina local utilizando el siguiente comando:

```bash
git clone https://github.com/Nicko-rgb/Detecci-n-de-Objetos.git
cd Detecci-n-de-Objetos
```

### 2. Crear un Entorno Virtual

Es recomendable crear un entorno virtual para gestionar las dependencias:

```bash
python -m venv yolo_env
source yolo_env/bin/activate   # En Linux/MacOS
yolo_env\Scripts\activate      # En Windows
```

### 3. Instalar Dependencias

Instala las bibliotecas necesarias ejecutando el siguiente comando:

```bash
pip install -r requirements.txt
```

### 4. Configuración del Modelo

Descarga los siguientes archivos y colócalos en el directorio principal del proyecto:

- [`yolov4.weights`](https://github.com/AlexeyAB/darknet/releases/download/yolov4/yolov4.weights)
- [`yolov4.cfg`](https://github.com/AlexeyAB/darknet/blob/master/cfg/yolov4.cfg)
- [`coco.names`](https://github.com/AlexeyAB/darknet/blob/master/data/coco.names)

O Descarga su variante mas ligera
- [`yolov4-tiny.weights`](https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v4_pre/yolov4-tiny.weights)
- [`yolov4-tiny.cfg`](https://raw.githubusercontent.com/AlexeyAB/darknet/master/cfg/yolov4-tiny.cfg)
- [`coco.names`](https://github.com/AlexeyAB/darknet/blob/master/data/coco.names)

Asegúrate de colocarlos correctamente en la carpeta del proyecto.

---

## Ejecución del Programa

Para iniciar la detección de objetos, ejecuta el script principal con el siguiente comando:

```bash
python detecta_objetos.py
```

---

## Créditos y Enlaces Útiles

- **Modelo YOLOv4:** [Darknet YOLO](https://github.com/AlexeyAB/darknet)  
- **Documentación Oficial de OpenCV:** [OpenCV](https://docs.opencv.org/)

---

### Notas Adicionales

Si encuentras problemas al ejecutar el modelo, verifica que los archivos `yolov4.weights`, `yolov4.cfg` y `coco.names` estén correctamente colocados y configurados en el script principal.
