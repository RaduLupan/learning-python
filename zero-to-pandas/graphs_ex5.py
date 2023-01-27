'''
This example imports the matplotlib.pyplot and seaborn libraries, as well as the urlretrieve and PIL modules
from urllib.request and the numpy library. 
It then uses urlretrieve to download an image from a given URL and store it as 'chart.jpg'. 
The image is then opened with the Image module and stored as an array in img_array. 
A grid, title, axis and image are all plotted using plt from matplotlib.pyplot to display the image with its associated title.
'''
import matplotlib.pyplot as plt
import seaborn as sns

from urllib.request import urlretrieve
from PIL import Image

import numpy as np 

urlretrieve('https://i.imgur.com/SkPbq.jpg', 'chart.jpg');

img = Image.open('chart.jpg')

img_array = np.array(img)
print(img_array.shape)

plt.grid(False)
plt.title('A data science meme')
plt.axis('off')
plt.imshow(img);
