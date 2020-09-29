import pandas as pd
pd.set_option("display.max_columns", None)
import numpy as np
import seaborn as sns
import palettable
import matplotlib.pyplot as plt
#%matplotlib inline
from jupyterthemes import jtplot
jtplot.style(theme='monokai', context='notebook', ticks=True, grid=False)

import numpy as np
import matplotlib.pyplot as plt
import math

t = np.linspace(0,2,2000)

#Square wave
def square_wave():
  f = 1
  t = np.linspace(0,2,2000)
  sqwave = np.sign(np.sin(2*np.pi*f*t))
  return sqwave 
 
# Input Signal
def Vi(v,w,t,p):
    """Calculate the input signal"""
    t = np.linspace(0,2,2000)
    Vin = np.asanyarray(v*np.sin((w*t)+ math.degrees(p)))
    return  Vin
    

print("Hey lets find the input signal")

num1 = float(input("Enter voltage : "))
num2 = float(input("Enter angular frequency(Hz) : "))
num3 = t
num4 = float(input("Enter phase shift : "))

#  print("The answer is" , Vi(num1,num2, num3, num4))

#Noise
noise = np.random.normal(0,0.5,2000)

#The System

def system(s,i):
    noise = np.random.normal(0,0.5,2000)
    return s*i+noise

shrink = float(input("Enter shrink to system"))

plt.plot(t, Vi(num1,num2, num3, num4))
plt.plot(t, system(shrink,Vi(num1,num2, num3, num4)))
plt.show()


def mixer(t):
    return (square_wave()*system(shrink,Vi(num1,num2, num3, num4))) 

plt.plot(t,mixer(t))
plt.show()


#Low Pass Filter

z = np.convolve( np.ones(200)/200, mixer(t),  mode = 'same') 

plt.plot(t,z)
plt.show()

#Averge of Mixer

filter = mixer(t)/2000

print(filter)
plt.plot(t, filter)
plt.plot(t, mixer(t))
plt.show()

inputmax = np.amax(Vi(num1,num2, num3, num4))

print(inputmax)
print(num1)

maxlist=[]
for x in range(10000):
    def mixer(t):
        return (square_wave()*system(shrink,Vi(num1,num2, num3, num4))) 
    z = np.convolve( np.ones(200)/200, mixer(t),  mode = 'same')  
    noise = np.random.normal(0,1,2000)
    peak = np.max(z)
    maxlist.append(peak)
    
print(maxlist)

maxarray = np.asarray(maxlist)
print(maxarray)

arb = np.random.rand(1)

print(arb)

average = sum(maxlist)/len(maxlist)

print("Average=",average )

Error= ((average-num1)/num1)*100
print("Error is", Error, "%")


#plt.plot(t, square_wave())
#plt.plot (t, hist)
#plt.hist(avgarray, bins='auto', facecolor='blue')
#plt.plot ( t, z4, "b")
#plt.plot(t, Vi(num1,num2,num3,num4), "k") 
plt.hist(maxlist,10)
#plt.plot(t, mixer4(t))
plt.show()
