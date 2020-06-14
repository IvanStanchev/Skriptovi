from keras.datasets import mnist
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten
import matplotlib.pyplot as plt
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import numpy as np
from keras.preprocessing import image

from datetime import datetime as dt

time = dt.now()
(image_train,label_train),(image_test,label_test) = mnist.load_data()


image_train = image_train.reshape(60000,28,28,1)
image_test = image_test.reshape(10000,28,28,1)

label_train_one_hot = to_categorical(label_train)
label_test_one_hot = to_categorical(label_test)

model = Sequential()
model.add(Conv2D(64, kernel_size=3, activation='relu', input_shape=(28,28,1)))
model.add(Conv2D(32, kernel_size=3, activation='relu'))
model.add(Flatten())
model.add(Dense(10, activation='softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

hist = model.fit(image_train, label_train_one_hot, validation_data=(image_test, label_test_one_hot), epochs=3)

plt.plot(hist.history['accuracy'])
plt.plot(hist.history['val_accuracy'])
plt.title('Model Accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train','Val'], loc='upper left')
plt.show()

time = dt.now()-time
print("MODEL MADE IN:",time)

def LoadAndPredictONE(path):
	img_width, img_height = 28, 28
	img = image.load_img(path, target_size=(img_width, img_height))
	x = image.img_to_array(img)
	x = x.astype('float32')/255
	pixels = x
	x = x.reshape(-1, 28, 28, 1)
	
	prediction = model.predict(x)
	print("PREDICTIONS:",prediction,"\n\n\n")
	print("Predictions:",np.argmax(prediction, axis=1),"OK\n\n\n")
	plt.imshow(pixels, cmap='gray')
	plt.show()

def LoadAndPredictMULT():
	path = os.path.join(os.getcwd(),"numbers")
	for img in os.listdir(path):
		if ".jpg" not in img and ".jpeg" not in img and ".png" not in img:
			continue
		cpath = os.path.join(path,img)
		print("\n",cpath)
		LoadAndPredictONE(cpath)

LoadAndPredictMULT()



