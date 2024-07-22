import cv2

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
        print("Unable to access camera")
        break

    #   Full screen
    #    cv2.namedWindow("camera", cv2.WND_PROP_FULLSCREEN)
    #    cv2.setWindowProperty("camera", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    #   Cropped to screen size and centered window
    cv2.namedWindow("camera", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("camera", screenWidth, screenHeight)
    cv2.moveWindow("camera", moveRight, moveDown)
    cv2.imshow("camera", frame)

    if cv2.waitKey(1) != -1:
        break

cap.release()
cv2.destroyAllWindows()
