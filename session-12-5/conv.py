import numpy as np

def sigmoid(output):
	return (1/(1+np.exp(-output)))


image = # make a 7x7 numpy array

conv_filter = # chose a filter size and make a numpy array of this size

stride = #chose a stride 

output_size = (image.shape(1)-filter_size)/stride # this is a mathematical formula

def matrix_dot_product(image_part, filter):
	# write a function that takes a part of one image and 
	# a filter and computes the dot product between them

def slide(image, position, filter,stride):
	# write a function that returns the next part of the image
	# to return the dot product

	x = position[0]
	y = position[1]
	filter_size = filter.shape[0]

	# find the new x and y coordinates

	return image[] # slice the image



	







