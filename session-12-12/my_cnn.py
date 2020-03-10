from __future__ import absolute_import, division, print_function, unicode_literals

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

data_dir = '/Users/helenfellow/Documents/Education /cnn_data'
data_dir = pathlib.Path(data_dir)

image_count = len(list(data_dir.glob('*/*.jpg')))
print(image_count)


CLASS_NAMES = np.array([item.name for item in data_dir.glob('*') if item.name != ".DS_Store"])
print(CLASS_NAMES)

seal_1 = list(data_dir.glob('seal_1/*'))


image_generator = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1./255)
BATCH_SIZE = 622
IMG_HEIGHT = 1024
IMG_WIDTH = 768
STEPS_PER_EPOCH = np.ceil(image_count/BATCH_SIZE)


train_data_gen = image_generator.flow_from_directory(directory=str(data_dir),
                                                     batch_size=BATCH_SIZE,
                                                     shuffle=True,
                                                     target_size=(IMG_HEIGHT, IMG_WIDTH),
                                                     classes = list(CLASS_NAMES),
                                                     class_mode="sparse")

image_batch, label_batch = next(train_data_gen)
show_batch(image_batch, label_batch)


## add model here like tensorflow tutorial:

# todo








# instead of the history line from the tutorial use this: 
history = model.fit(x=image_batch, y=label_batch, epochs=4, 
                    validation_split=.20,)