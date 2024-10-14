import cv2

import numpy as np

import os

def

preprocess_images(gesture_dirs):

data = []

labels = []

for label, gesture_dir in enumerate(gesture_dirs):

for img_file in

os.listdir(gesture_dir):

img_path = os.path.join(gesture_dir, img_file)

img = cv2.imread(img_path)

img =

cv2.resize(img, (64, 64)) / 255.0

data.append(img)

labels.append(label) return np.array(data), np.array(labels)

if_name

==

_main__':

gesture_dirs = ['data/

thumbs_up', 'data/thumbs_down',

'data/peace_sign', 'data/

open_palm']

X, y = preprocess_images(gesture_dirs) np.save('data/X.npy', X) np.save('data/y.npy', y)