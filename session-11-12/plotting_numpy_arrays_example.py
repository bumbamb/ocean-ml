import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

# plotting the data
example = np.array([(4.3,-5,0),(2.5,1,-2),(-1.7,3,-.09),(1,1,1)])
plt.imshow(example,origin='lower')


# adding a line:
x1,y1 = [-.5,2.5],[-.5,2.5]
plt.plot(x1,y1, color = 'blue')

# adding a colorbar: 
cbar = plt.colorbar()

#labeling the colorbar:
cbar.set_label("colorbar-example-title")

# adding x and y labels:
plt.xlabel('x')
plt.ylabel('y')

# adding a title for the plot:
plt.title('Very Exciting Example Plot')

# changing the x ticks: 
#(try commenting this out and commenting it back in to see what it does)
plt.xticks(np.arange(3),[7,8,9])

# changing the y ticks:
# this goes: plt.yticks(number-of-ticks, [array-with-tick-values])
plt.yticks(np.arange(4),[12,17,22,27])

# adding a legend:
blue_line = mlines.Line2D([], [], color='blue',
                          markersize=15, label='This line means something!')
plt.legend(handles=[blue_line])

plt.show()

