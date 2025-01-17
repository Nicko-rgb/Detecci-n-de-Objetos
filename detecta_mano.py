import cv2
import mediapipe as mp
import time
import random

# Inicializar cámara
cap = cv2.VideoCapture(0)

# Mediapipe configuración
mphands = mp.solutions.hands
hands = mphands.Hands(False)
mpDraw = mp.solutions.drawing_utils

# Variables de tiempo para calcular FPS
pTime = 0
cTime = 0

# Configuración del juego
objects = []  # Lista de objetos (cada objeto es un diccionario con 'x', 'y', 'radius')
score = 0     # Contador de objetos cogidos
game_running = True

# Crear función para generar nuevos objetos
def generate_object():
    x = random.randint(50, 590)  # Coordenada x aleatoria
    y = 0                        # Inicia en la parte superior
    radius = random.randint(20, 40)  # Tamaño del objeto
    return {'x': x, 'y': y, 'radius': radius}

# Main Loop
while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)  # Espejar imagen
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    # Detección de manos
    hand_positions = []
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                if id == 8:  # Índice del dedo (punta)
                    hand_positions.append((cx, cy))
                    cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)
            mpDraw.draw_landmarks(img, handLms, mphands.HAND_CONNECTIONS)

    # Generar nuevos objetos cada cierto tiempo
    if len(objects) < 5:  # Máximo 5 objetos en pantalla
        objects.append(generate_object())

    # Dibujar y mover los objetos
    for obj in objects[:]:
        obj['y'] += 5  # Mover hacia abajo
        cv2.circle(img, (obj['x'], obj['y']), obj['radius'], (0, 255, 0), -1)

        # Detección de colisión
        for hx, hy in hand_positions:
            distance = ((hx - obj['x'])**2 + (hy - obj['y'])**2)**0.5
            if distance < obj['radius']:
                score += 1
                objects.remove(obj)
                break

        # Eliminar objetos que salgan de la pantalla
        if obj['y'] > img.shape[0]:
            objects.remove(obj)

    # Mostrar puntuación y botón de salida
    cv2.rectangle(img, (0, 0), (200, 70), (0, 0, 0), -1)
    cv2.putText(img, f'Score: {score}', (10, 40), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)
    cv2.putText(img, 'Press Q to Quit', (300, 40), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)

    # Calcular y mostrar FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (500, 40), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)

    # Mostrar imagen en ventana
    cv2.imshow("Interactive Game", img)
    
    # Salir del juego
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
