import cv2
import mediapipe as mp
import time


# cap = cv2.VideoCapture(0)
# mpHands = mp.solutions.hands
# hands = mpHands.Hands(False)
# mpDraw = mp.solutions.drawing_utils
# cTime = 0
# pTime = 0


def camera_count():
    """Returns int value of available camera devices connected to the host device"""
    camera = 0
    while True:
        if (cv2.VideoCapture(camera).grab()) is True:
            camera = camera + 1
        else:
            cv2.destroyAllWindows()
            return int(camera)


print(camera_count())
# while True:
#     success, img = cap.read()
#     imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#     results = hands.process(imgRGB)
#     # print(results.multi_hand_landmarks)
#     if results.multi_hand_landmarks:
#         for handLms in results.multi_hand_landmarks:
#             for id , lm in enumerate(handLms.landmark):
#                 # print(id,lm)
#                 h, w , c = img.shape
#                 cx , cy = int(lm.x*w) ,int (lm.y*h)
#                 print ( id, cx, cy)
#                 if id ==4:
#                     cv2.circle(img,(cx,cy),15, (255,0,266), cv2.FILLED)
#             mpDraw.draw_landmarks(img, handLms , mpHands.HAND_CONNECTIONS)
#
#     cTime = time.time()
#     fps = 1 / (cTime-pTime)
#     pTime = cTime
#     cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,266),2)
#     cv2.imshow("Image", img)
#     cv2.waitKey(1)
