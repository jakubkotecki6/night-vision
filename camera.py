import cv2

cameraWidth, cameraHeight, cameraFramerate = 256, 192, 50

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, cameraWidth)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, cameraHeight)
cap.set(cv2.CAP_PROP_FPS, cameraFramerate)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame")
        break

        #   Full screen
    cv2.namedWindow("camera", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("camera", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    cv2.imshow("camera", frame)

    if cv2.waitKey(1) != -1:
        break

cap.release()
cv2.destroyAllWindows()
