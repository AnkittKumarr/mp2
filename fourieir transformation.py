import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
def f(x,L):
 if 0<=x<L:
  return np.sin(x)
 elif L<=x<2*L:
  return 0
 else:
  return 0
def fourier_cofficients(n_terms,L):
 a_cofficients=[]
 b_cofficients=[]
 for n in range(1,n_terms+1):
  an, _ =quad(lambda x:f(x,L)*np.cos(n*np.pi*x/L),-L,L)
  bn, _=quad(lambda x:f(x,L)*np.sin(n*np.pi*x/L),-L,L)
  an*=1/L
  bn*=1/L
  a_cofficients.append(an)
  b_cofficients.append(bn)
  return a_cofficients,b_cofficients
def half_rectified_wave(x,n_terms,L):
 a0=0
 half_rectified_wave=a0/2
 for n in range(1,n_terms+1):
  an=1/L*quad(lambda x:f(x,L)*np.cos(n*np.pi*x/L),-L,L)[0]
 bn=0
 if n%2!=0:
  bn=1/L*quad(lambda x:f(x,L)*np.sin(n*np.pi*x/L),-L,L)[0]
 half_rectified_wave+=an*np.cos(n*np.pi*x/L)+bn*np.sin(n*np.pi*x/L)
 return half_rectified_wave
 x_values=np.linspace(-20,20,1000)
 L=np.pi
 n_cofficients=20
 a_cofficients,b_cofficients=fourier_cofficients(n_cofficients,L)
 half_rectified_wave_values=half_rectified_wave(x_values,n_cofficients,L)
 print('fourier series cofficients:')
 for n in range(len(a_cofficients)):
  an=a_cofficients[n]
 bn=b_cofficients[n]
 print("a"+str(n+1)+" "+str(round(an,4))+" "+"b"+str(n+1)+" "+str(round(bn,4)))
 plt.subplot(2,2,1)
 plt.plot(x_values,half_rectified_wave_values)
 plt.title('SQUARE WAVE')
 plt.ylabel('amplitude')
 plt.xlabel('x')
 plt.grid(True)
 plt.subplot(2,2,2)
 plt.bar(range(1,n_cofficients+1),a_cofficients)
 plt.title('Fourier Coefficients (an) vs. n')
 plt.ylabel('An')
 plt.xlabel("n")
 plt.grid(True)
 plt.subplot(2,2,3)
 plt.bar(range(1,n_cofficients+1),b_cofficients)
 plt.title('Fourier Coefficients (bn) vs. n')
 plt.ylabel('Bn')
 plt.xlabel('n')
 plt.grid(True)
 plt.tight_layout()
 plt.show()