import cv2

import numpy as np

import tensorflow as tf

model =

tf.keras.models.load_model('mode ls/gesture_model.h5')
You

def predict_gesture(frame):

img = cv2.resize(frame, (64, 64)) / 255.0

img = np.expand_dims(img,

axis=0)

predictions = model.predict(img) return np.argmax(predictions)

cap = cv2.VideoCapture(0) gesture_labels = ['thumbs_up', 'thumbs_down', 'peace_sign', 'open_palm']

while True:

ret, frame = cap.read()

if not ret: break gesture = predict_gesture(frame) cv2.putText(frame, gesture_labels [gesture], (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2) cv2.imshow('Gesture Recognition', frame)

if cv2.waitKey(1) & 0xFF == ord('q'):

break

cap.release() cv2.destroyAllWindows()