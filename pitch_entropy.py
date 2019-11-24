# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 16:28:57 2019

@author: amisr
"""

from music21 import *
import collections
import numpy as np


parsed = converter.parse('test.mid') 

pitch_midi = np.zeros(len(parsed.pitches))

for i in range(len(parsed.pitches)):
    pitch_midi[i] = parsed.pitches[i].midi

pitch = collections.Counter(pitch_midi) # Counting occurences of distinct pitches


# ------------------- Computing the Pitch entropy ------------------------------------

total_pitches = 0

for x in pitch:
    total_pitches += pitch[x]
    
pitch_entropy = 0

for y in pitch:
    pitch_entropy -= (pitch[y]/total_pitches) * np.log2((pitch[y]/total_pitches))


print(pitch_entropy)
    
#-------------------------------------------------------------------------------------