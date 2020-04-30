# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 18:53:34 2020

@author: Cameron
"""

from math import pi
import numpy as np
import matplotlib.pyplot as plt

# Sampling rate
fs = 2000 #Hz 

# Sample period
t0 = 1/fs #sec 

# Length of signal in time domain (3 secounds)
T = 3 #sec

# Samples n = 0 - T - 1 spaced by sample period
n = np.arange(0,T,t0) 

# Size of signal (number of samples)
N = n.size 

# Spacing in the frequency domain
f0 = 1/T 

# Signal creation
sigFreq = 250
w = 2 * pi * sigFreq
sig = np.sin(w * n)

plt.figure()
plt.plot(n,sig)

# Implementaion with calculating f myself
SIGf = np.fft.fftshift(np.fft.fft(sig))/N
f = np.arange(-fs/2,fs/2,f0)
sig2 = np.fft.ifft(np.fft.fftshift(SIGf*N))

# Implementation with fftfreq
# SIGf = np.fft.fft(sig)/N
# f = np.fft.fftfreq(N,t0)
# sig2 = np.fft.ifft(SIGf*N)

# Correct quantization errors that will show up in phase
SIGf[np.abs(SIGf) < .0000000001] = 0

plt.figure()
plt.stem(f,np.abs(SIGf),use_line_collection = True)
plt.figure()
plt.stem(f,np.angle(SIGf),use_line_collection = True)
plt.figure()
plt.plot(n,np.real(sig2))