import numpy as np
import matplotlib.pyplot as plt

def f(X):
    y=[]
    for x in X:
        if(abs(x)<=1):
            y.append(1)
        else:
            y.append(0)
    return(y)



xmin = -5.0
xmax = 5.0
n = 256



x = np.linspace(xmin,xmax,n)
dx = x[1]-x[0]



y = f(x) 

    
nft = np.fft.fft(y, norm='ortho')

cnv = np.fft.ifft(nft*nft, norm='ortho')

fcnv = dx*np.sqrt(n)*cnv

s_fcnv = np.fft.fftshift(fcnv)  #shifiting zero frequency part to the center 



plt.scatter(x,np.real(s_fcnv),c='b',label='Convolution')
plt.plot(x,y,c='k',label='Box Function')

plt.legend()
plt.title("Convolution of box function with itself")
plt.show()