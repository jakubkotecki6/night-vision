import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 256)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 192)
cap.set(cv2.CAP_PROP_FPS, 50)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Unable to access camera")
        break

    cv2.namedWindow("camera", cv2.WINDOW_NORMAL)
    cv2.setWindowProperty("camera", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow('camera', frame)
    if cv2.waitKey(30) == 27:
        break

cap.release()
cv2.destroyAllWindows()
