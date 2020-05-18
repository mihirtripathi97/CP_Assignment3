import numpy as np
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm

def f(x,y):
    return(np.exp(-(x**2+y**2)))

def fk_g(kx,ky):
    
    kx,ky = np.meshgrid(kx,ky)
    y =np.exp(-(kx**2+ky**2)/4)/2 
    return(y)
    


xmin = -10
xmax = 10
ymin = -10
ymax = 10
n = 64
a = np.zeros([n,2])

dy = (ymax-ymin)/(n-1)
dx = (xmax-xmin)/(n-1)


xarr = np.linspace(xmin,xmax,n)
yarr = np.linspace(ymin,ymax,n)

X, Y = np.meshgrid(xarr, yarr)

f_x = f(X,Y)
f_q = np.fft.fft2(f_x,norm='ortho')

kxarr = 2*np.pi*np.fft.fftfreq(n,d=dx)
kyarr = 2*np.pi*np.fft.fftfreq(n,d=dy)

ftrx = np.exp(-1j*kxarr*xmin)
ftry = np.exp(-1j*kyarr*ymin)

aft = (dx*dy*(n/(2.0*np.pi))*ftrx*ftry*f_q)
Kx , Ky = np.meshgrid(kxarr,kyarr)


fig = plt.figure(figsize = plt.figaspect(0.5))

ax = fig.gca(projection = '3d')
ax.set_xlabel("k_x")
ax.set_ylabel("k_y")

surf = ax.contour3D(Kx, Ky, abs(aft),100)

plt.title('Using np.fft2 (Numericall)')
plt.show()

fig = plt.figure(figsize = plt.figaspect(0.5))
ax = fig.gca(projection = '3d')
ax.set_xlabel("k_x")
ax.set_ylabel("k_y")

surf2 = ax.contour3D(Kx, Ky, fk_g(kxarr,kyarr),100)

plt.title('Analytical solution')
plt.show()




        