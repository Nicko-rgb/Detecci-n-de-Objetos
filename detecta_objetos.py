import cv2
import numpy as np

# Cargar el modelo YOLO
net = cv2.dnn.readNet("yolov4.weights", "yolov4.cfg")  # Asegúrate de tener estos archivos
#Una Opcion mas simple 
# net = cv2.dnn.readNet("yolov4-tiny.weights", "yolov4-tiny.cfg") 

layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

# Cargar las clases de objetos detectables
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

# Colores para cada clase
colors = np.random.uniform(0, 255, size=(len(classes), 3))

# Capturar video desde la cámara
cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    height, width, channels = frame.shape

    # Preparar la imagen para el modelo YOLO
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outputs = net.forward(output_layers)

    # Procesar las detecciones
    class_ids = []
    confidences = []
    boxes = []

    for output in outputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            if confidence > 0.3:  # Filtrar detecciones con confianza > 50%
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                # Coordenadas de la caja delimitadora
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    # Eliminar cajas delimitadoras duplicadas
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            confidence = confidences[i]
            color = colors[class_ids[i]]

            # Dibujar la caja delimitadora y la etiqueta
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            cv2.putText(frame, f"{label} {int(confidence * 100)}%", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    # Mostrar el video con las detecciones
    cv2.imshow("Object Detection", frame)

    # Salir del bucle con la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
