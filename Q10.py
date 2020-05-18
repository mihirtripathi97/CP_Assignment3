

import numpy as np
import matplotlib.pyplot as plt


noise = np.loadtxt("noise.txt", usecols = 0)
t = np.arange(0,np.size(noise),1)

#DFT of the noise

n_dft = np.fft.fft(noise, norm = 'ortho')
k = np.fft.fftfreq(np.size(t), d = 1)

#calculating power spectrum
p = (n_dft*np.conj(n_dft))/np.size(n_dft)

#print(p)

bins_data = np.zeros(10)
bin_ind = np.arange(1,np.size(bins_data)+1,1)

for i in range(np.size(bins_data)):
    s = 0
    
    for j in range(int(i*51),int(51*(i+1)),1):
        
        s = s + p[j]
    
    bins_data[i] = s/51



#ploting noise
plt.figure()
plt.plot(t,noise,'g.-',label = 'noise_data')
plt.xlabel('t')
plt.ylabel('Noise')
plt.legend()

#ploting dft of the noise
plt.figure()
plt.plot(k, np.real(n_dft),'b*', label = 'DFT of noise')
plt.xlabel('Frequency')
plt.ylabel('DFT of noise')
plt.legend()

#ploting power spectrum
plt.figure()
plt.plot(k,np.real(p),'k.', label = 'Power spectrum of the noise')
plt.xlabel('Frequency')
plt.ylabel('Power spectrum')
plt.legend()

#bin power spectrum
plt.figure()
plt.plot(bin_ind,np.real(bins_data),'r*',label = 'Binned power spectrum')
plt.xlabel('Bin number')
plt.ylabel('Power spectrum')
plt.legend()

plt.show()