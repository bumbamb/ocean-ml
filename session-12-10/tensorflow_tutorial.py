from __future__ import absolute_import, division, print_function, unicode_literals
with warnings.catch_warnings():
	warnings.filterwarnings("ignore",category=FutureWarning)
	import tensorflow as tf
	from tensorflow.keras import datasets, layers, models
	import matplotlib.pyplot as plt

# rest of code from tutorial 