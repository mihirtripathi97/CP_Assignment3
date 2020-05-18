


import numpy as np
import matplotlib.pyplot as plt
import time

def fft(L):
    aft = np.fft.fft(L,norm = 'ortho')
    return()
    
    

ffttime = []
scdtime = []

for lnt in range(4,100,1):
    
    L = 200*np.random.random_sample(lnt) - 100
    #L = np.arange(lnt)
    
    n = len(L)
    #print(n)
    
    t = 0
    
    for m in range (10):
        
        start = time.time()
        aft = np.fft.fft(L,norm = 'ortho')
        end = time.time()
        
        t = t + (end - start)
    
    t = t/10  
    
    ffttime.append(t)
    
     


    
    
    t = 0
    for p in range(10):
        start = time.time()
        
        AFT = []
        for i in range(n):
            S = 0    
    
            for m in range(n):
        
                S = S + (L[m]*np.exp(-1j*2.0*np.pi*i*m/n))
        
            AFT.append(S/np.sqrt(n) )
        
        end = time.time()
        
        t = t + (end - start)
        
    t = t/10
    
    scdtime.append(t)
    
        

    #print(aft)
    #print(AFT)

    

N = np.arange(4,100,dtype = int)

plt.plot(N,scdtime,c='g',label = 'Without np.fft')
plt.plot(N,ffttime,c='r',label = 'Numpy fft')
plt.xlabel("n(number of elements in array)")
plt.ylabel("Time(s)")
plt.legend()
plt.grid(True)
plt.show()


#The program typically takes 10-20s to run
    
                    







