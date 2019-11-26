# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 23:05:36 2019

@author: amisr
"""

import pretty_midi
import numpy as np
from music21 import * 

parsed = converter.parse('test.mid') 
p = analysis.discrete.Ambitus()
s = stream.Stream(parsed)

for thisPitch in p.getPitchSpan(s):
    print(int(thisPitch.ps))
    
min, max = p.getPitchSpan(s)

min_pitch_diff_freq = min.freq440
max_pitch_diff_freq = max.freq440