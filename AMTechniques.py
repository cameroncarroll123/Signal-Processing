# -*- coding: utf-8 -*-
"""
Created on Sun May  3 18:57:01 2020

@author: Cameron
"""
import os
from scipy.io import wavfile
import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt
from math import pi
import Signals as sigs


path = os.getcwd() + "\questions.wav"
fs, m = wavfile.read(path)
# sd.play(m,fs)
# t0 = 1/fs #sec 
# N = m.size
# T = N * t0
# n = np.arange(0,T,t0)
# f0 = 1 / T
sig = sigs(m, fs)
n = np.range(0,sig.waveDuration,sig.sampT)

plt.figure()
plt.plot(n,m)

# M = np.fft.fft(m)/N
# f = np.fft.fftfreq(N,t0)

# plt.figure()
# plt.plot(f,M)

# carrierFreq = 250
# w = 2 * pi * carrierFreq
# carrier = np.cos(w * n)

# amSig = m * carrier

# plt.figure()
# plt.plot(n,m)