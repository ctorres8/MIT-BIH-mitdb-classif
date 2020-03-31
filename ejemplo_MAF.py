# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 15:12:07 2020

@author: crist
"""

import numpy as np
from scipy import signal as sig
import matplotlib.pyplot as plt
import scipy.io as sio


ECG = sio.loadmat('100m.mat')

"""

100m 2 360 650000
100m.mat 16+192 200/mV 11 0 -29 27021 0 MLII
100m.mat 16+192 200/mV 11 0 -13 3668 0 V5
# 69 M 1085 1629 x1
# Aldomet, Inderal
#Creator: wfdb2mat
#Source: record mitdb/100

"""

ecg_ii = ECG['val'][0]
ecg_v5 = ECG['val'][1]
N_ecg_ii = len(ecg_ii)
N_ecg_v5 = len(ecg_v5)


fs = 360 #Hz
f_nyq = fs/2 # 180 Hz

w=