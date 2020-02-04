from __future__ import absolute_import, division, print_function, unicode_literals

#importing stuf!!
import warnings  
with warnings.catch_warnings():
	warnings.filterwarnings("ignore",category=FutureWarning)
	import tensorflow as tf
	from tensorflow.keras import datasets, layers, models
	import IPython.display as display
	from PIL import Image
	import numpy as np
	import matplotlib.pyplot as plt
	import os
	import glob
	import pathlib


print('ready') 

#makes figure that shows how many images
def show_batch(image_batch, label_batch):
  plt.figure(figsize=(10,10))
  print(label_batch.shape)
  for n in range(25):
      ax = plt.subplot(5,5,n+1)
      plt.imshow(image_batch[n])
      plt.title(CLASS_NAMES[int(label_batch[n])])
      plt.axis('off')
  plt.show()

AUTOTUNE = tf.data.experimental.AUTOTUNE

#focusing on that directory
data_dir = '/Users/brownscholar/Desktop/Internships/Climate/cnn_data'
data_dir = pathlib.Path(data_dir)

#counts the image
image_count = len(list(data_dir.glob('*/*.jpg')))
print(image_count)

#assigning names to the items?
CLASS_NAMES = np.array([item.name for item in data_dir.glob('*') if item.name != ".DS_Store"])
print(CLASS_NAMES)

seal_1 = list(data_dir.glob('big_boi/*'))

#assigns the number to the correct value
image_generator = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1./255)
BATCH_SIZE = 668
IMG_HEIGHT = 3024
IMG_WIDTH = 3024
STEPS_PER_EPOCH = np.ceil(image_count/BATCH_SIZE)


train_data_gen = image_generator.flow_from_directory(directory=str(data_dir),
                                                     batch_size=BATCH_SIZE,
                                                     shuffle=True,
                                                     target_size=(IMG_HEIGHT, IMG_WIDTH),
                                                     classes = list(CLASS_NAMES),
                                                     class_mode="sparse")

image_batch, label_batch = next(train_data_gen)
show_batch(image_batch, label_batch)

#creates model and adds layers to it
model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(1024, 768, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))

#shows the result of the model
print(model.summary())


model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

history = model.fit(x=image_batch, y=label_batch, epochs=10, 
                    validation_split=.20,)



