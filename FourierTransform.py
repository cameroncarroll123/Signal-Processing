# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 18:53:34 2020

@author: Cameron
"""

from math import pi
import numpy as np
import matplotlib.pyplot as plt

fs = 200 #Hz sampling rate
t0 = 1/fs #sec sample period
T = 3 #Sec
n = np.arange(0,T,t0) #Samples
N = n.size
f0 = 1/T
fz = np.arange(-fs/2,fs/2,f0)


f = 50
w = 2 * pi * f
sig = np.sin(w * n)

plt.figure()
plt.plot(n,sig)

# SIGf = np.fft.fftshift(np.fft.fft(sig))/N
SIGf = np.fft.fft(sig)/N
SIGf[np.abs(SIGf) < .000000001] = 0
sig = np.fft.ifft(SIGf*N)
# fz = np.arange(-F/2,F/2,f0)
fz = np.fft.fftfreq(N,t0)
plt.figure()
plt.stem(fz,np.abs(SIGf),use_line_collection = True)
plt.figure()
plt.stem(fz,np.angle(SIGf),use_line_collection = True)
plt.figure()
plt.plot(n,np.real(sig))