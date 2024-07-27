import cv2
from ultralytics import YOLO

model = YOLO("best.pt")

cameraWidth, cameraHeight, cameraFramerate = 256, 192, 50
screenWidth, screenHeight = 320, 192
moveRight, moveDown = int((720 - screenWidth) / 2), int((480 - screenHeight) / 2)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, cameraWidth)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, cameraHeight)
cap.set(cv2.CAP_PROP_FPS, cameraFramerate)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to capture frame")
        continue

    result = model.predict(frame, conf=0.15)

    #   Full screen
    cv2.namedWindow("frame", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("frame", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    #   Cropped to screen size and centered window
    #cv2.namedWindow("frame", cv2.WINDOW_NORMAL)
    #cv2.resizeWindow("frame", screenWidth, screenHeight)
    #cv2.moveWindow("frame", moveRight, moveDown)
    cv2.imshow("frame", result[0].plot())

    if cv2.waitKey(1) != -1:
        break

cap.release()
cv2.destroyAllWindows()
