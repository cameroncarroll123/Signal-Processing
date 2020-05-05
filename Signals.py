# -*- coding: utf-8 -*-
"""
Created on Mon May  4 18:20:45 2020

@author: Cameron
"""
import os
from scipy.io import wavfile
import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt
from math import pi


class Signals:
  def __init__(self, data, fs, blockSize = None):
    self.sampT = 1 / fs
    self.dataN = data.size
    self.waveDuration = self.sampT * self.dataN
    blockSize = self.dataN if blockSize is None else blockSize
    self.fftRes = fs / blockSize
    self.idx = np.arange(0, self.waveDuration,self.sampT)
    
path = os.getcwd() + "\questions.wav"
fs, m = wavfile.read(path)

sig = Signals(m, fs)

plt.figure()
plt.plot(sig.idx,m)