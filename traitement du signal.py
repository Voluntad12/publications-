import numpy as np
import matplotlib.pyplot as plt
from scipy import misc 
from scipy.interpolate import interp1d
from scipy import optimize 

#x=np.linspace(0,20,100)
#y= x + 4*np.sin(x) +np.random.randn(x.shape[0])
#plt.plot(x,y)

from scipy import signal
#nous voulons éliminer la tendance linéire 
#new_y= signal.detrend(y)
#plt.plot(x, new_y)

#La trasnformation du Fourier 

from scipy import fftpack
x=np.linspace(0,30,100)
y=3*np.sin(x)+2*np.sin(5*x)+np.sin(10*x)+np.random.randn(x.shape[0])  
#plt.plot(x,y)

fourier=fftpack.fft(y)
power=np.abs(fourier)
frequences=fftpack.fftfreq(y.size)
#plt.plot(np.abs(frequences),power)

fourier[power<100] =0
#plt.plot(np.abs(frequences),np.abs(fourier))

filtre=fftpack.ifft(fourier)
#plt.plot(x,filtre)

#la morphologie 
from scipy import ndimage 
np.random.seed(0)
X=np.zeros((32,32))
X[10:-10,10:-10]=1
X[np.random.randint(0,32,30),np.random.randint(0,32,30)]=1
#plt.imshow(X)

open_X=ndimage.binary_opening(X)
#plt.imshow(open_X) #pas vraiment efficace 

# extraire les bactéries 
image=plt.imread('Bacterie.jpg')
image=image[:,:,0]#tableau à deux dimensions 
#plt.imshow(image)
image_2=np.copy(image)
#plt.hist(image_2.ravel(), bins=255)
#plt.show()
image=image<160
#plt.imshow(image)
open_X=ndimage.binary_opening(image)
#plt.imshow(open_X)
label_image, n_labels= ndimage.label(open_X)
print(n_labels)
#plt.imshow(label_image)
sizes=ndimage.sum(open_X, label_image, range(n_labels))
plt.scatter(range(n_labels),sizes)

