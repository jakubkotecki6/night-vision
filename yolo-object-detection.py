import cv2
from ultralytics import YOLO

model = YOLO("best.pt")

cameraWidth, cameraHeight, cameraFramerate = 256, 192, 50
confidenceThreshold = 0.35

cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, cameraWidth)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, cameraHeight)
cap.set(cv2.CAP_PROP_FPS, cameraFramerate)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to capture frame")
        continue

    result = model.predict(frame, conf=confidenceThreshold)

    #   Full screen
    cv2.namedWindow("detection", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("detection", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    cv2.imshow("detection", result[0].plot())

    if cv2.waitKey(1) != -1:
        break

cap.release()
cv2.destroyAllWindows()
