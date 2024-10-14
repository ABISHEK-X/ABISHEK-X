import cv2

import os

def collect_images (gesture, num_images=300):

cap = cv2.VideoCapture (0) os.makedirs(gesture, exist_ok=True)

count = 0 while count < num_images: ret, frame =

cap.read()

if not ret: break

cv2.imshow('Collecting Images', frame)

cv2.imwrite(os.path.join(gesture f'{gesture}_{count}.jpg'), frame) 1

count += 1

cv2.waitKey(100)

cap.release() cv2.destroyAllWindows()

if_name == '__main__': gestures = ['thumbs_up', 'thumbs_down', 'peace_sign', 'open_palm']

for gesture in gestures:

collect_images (gesture)