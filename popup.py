import matplotlib.pyplot as plt
import matplotlib.image as mpimg

pic = mpimg.imread('./images/excitement.jpeg')

plt.imshow(pic)
plt.show(block=False)
plt.pause(3)
plt.close()