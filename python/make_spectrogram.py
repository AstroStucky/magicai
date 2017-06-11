# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 08:50:37 2017

@author: Thomas Stucky
"""

from ibmseti import ibmseti
import matplotlib.pyplot as plt
import numpy as np
import zipfile

zz = zipfile.ZipFile( 'basic4.zip' )

aca = ibmseti.compamp.SimCompamp( data.read() )
spec = aca.get_spectrogram()

fig, ax = plt.subplots(figsize=(10, 5))   

ax.imshow(np.log(spec), aspect = 0.5*float(spec.shape[1]) / spec.shape[0])
