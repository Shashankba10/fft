import numpy as np
import matplotlib.pyplot as plt

from scipy.fft import fft,ifft
#taking input
X=eval(input("enter the input sequence:"))

# ploting the input
plt.subplot(2,2,1)
n=np.arange(0,len(X),1)
plt.stem(n,X,"r")
plt.show
plt.grid()

plt.xlabel("n")
plt.ylabel("x")
plt.title("input sequence")



#caluting fft
y=fft(X)

#ploting fft
plt.subplot(2,2,2)
po=np.arange(0,len(y),1)
plt.stem(po,abs(y))
plt.show
plt.grid()
plt.xlabel("n")
plt.ylabel("fft seqence")
plt.title("magnitude spectrum")
print("fft of given sequence is:",y)



#calucating idft

y1=ifft
print("idft of given sequence is ",y1.real) #printing only real vaue

#ploting idft
plt.subplot(2,2,3)
po=np.arange(0,len(y1),1)
plt.stem(po,y1)
plt.show
plt.grid()
plt.xlabel("n")
plt.ylabel("idft sequence")
plt.title("idft")
