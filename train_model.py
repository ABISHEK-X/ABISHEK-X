import tensorflow as tf import numpy as np from sklearn.model_selection import train_test_split

X = np.load('data/X.npy') y = np.load('data/y.npy')

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2)

base_model = tf.keras.applications. MobileNetV 2(input_shape=(64, 64, 3), include_top=False,

weights='imagenet')

base_model.trainable = False

model = tf.keras.Sequential([ base_model,

tf.keras.layers.GlobalAverage Poo ling2D(),

tf.keras.layers. Dense (4, activation='softmax')

])
model.compile(optimizer='adam', loss='sparse_categorical_crossen tropy', metrics=['accuracy']) history = model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=10, batch_size=32)

model.save('models/ gesture_model.h5')