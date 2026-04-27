# this code is only for linux .!!! it may cause some lag in mouse

import cv2
import time
import math
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import subprocess

# ----------------------------
# Model
# ----------------------------
MODEL_PATH = "/home/abdou-pd/CODE/advanced CV/pretrained_models/hand_landmarker.task"

options = vision.HandLandmarkerOptions(
    base_options=python.BaseOptions(model_asset_path=MODEL_PATH),
    running_mode=vision.RunningMode.VIDEO,
    num_hands=2
)

landmarker = vision.HandLandmarker.create_from_options(options)

# ----------------------------
# Hand connections
# ----------------------------
HAND_CONNECTIONS = [
    (0,1),(1,2),(2,3),(3,4),
    (0,5),(5,6),(6,7),(7,8),
    (5,9),(9,10),(10,11),(11,12),
    (9,13),(13,14),(14,15),(15,16),
    (13,17),(17,18),(18,19),(19,20),
    (0,17)
]

THUMB_TIP = 4
INDEX_TIP = 8

# ----------------------------
# Webcam
# ----------------------------
cap = cv2.VideoCapture(0)
prev_time = time.time()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    mp_image = mp.Image(
        image_format=mp.ImageFormat.SRGB,
        data=rgb
    )

    timestamp_ms = int(time.time() * 1000)
    
    result = landmarker.detect_for_video(mp_image, timestamp_ms)

    h, w, _ = frame.shape

    # ----------------------------
    # Draw landmarks + distance
    # ----------------------------
    if result.hand_landmarks:
        for hand in result.hand_landmarks:
            points = []

            # landmarks
            for lm in hand:
                x, y = int(lm.x * w), int(lm.y * h)
                points.append((x, y))
                cv2.circle(frame, (x, y), 4, (0, 255, 0), -1)

            # connections
            for a, b in HAND_CONNECTIONS:
                cv2.line(frame, points[a], points[b], (255, 0, 0), 2)

            # ----------------------------
            # Thumb ↔ Index distance
            # ----------------------------
            x1, y1 = points[THUMB_TIP]
            x2, y2 = points[INDEX_TIP]

            distance = math.hypot(x2 - x1, y2 - y1)
            



            # draw distance line
            cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 255), 3)

            # draw distance value
            cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
            cv2.putText(
                frame,
                f"{int(distance)} px",
                (cx, cy - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 255),
                2
            )
            print(f'Point X={int(x2)} Y={int(y2)}')
            subprocess.run(["sudo",'ydotool','mousemove',str(x1*3.047),str(y1*2.51)])
            if distance<30 : subprocess.run(["sudo",'ydotool','click',"0xC0"])

    # ----------------------------
    # FPS
    # ----------------------------
    curr_time = time.time()
    fps = 1 / (curr_time - prev_time)
    prev_time = curr_time

    cv2.putText(
        frame, f"FPS: {int(fps)}",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        1, (0, 255, 0), 2
    )
    #cv2.putText(frame , f'Point {int(x)}',(450,25),cv2.FONT_HERSHEY_TRIPLEX,1.0, (255.255,100),2)
 

    cv2.imshow("Hand Landmarker", frame)

    if cv2.waitKey(1) & 0xFF == ord('d'):
        break

cap.release()
cv2.destroyAllWindows()
