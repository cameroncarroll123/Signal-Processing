# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 18:53:34 2020

@author: Cameron
"""

from math import pi
import numpy as np
import matplotlib.pyplot as plt


f = 100
T = 1 / f
timeStep = .0001
t = np.arange(0,3*T,timeStep)
w = 2 * pi * f

sig = np.cos(w * t)

plt.figure()
plt.plot(t,sig)

SIG = np.fft.fftshift(np.fft.fft(sig))
# SIG = np.fft.fft(sig)
fz = t/(t.size*timeStep)
# fz = np.fft.fftfreq(t.size,.01)
plt.figure()
plt.plot(fz,SIG)