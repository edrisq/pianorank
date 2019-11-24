# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 18:00:31 2019

@author: amisr
"""

from music21 import *
import pretty_midi
import numpy as np

midi_data = pretty_midi.PrettyMIDI('test.mid')

tempo = midi_data.estimate_tempo() #  Returns an empirical tempo estimate according to inner-onset intervals

parsed = converter.parse('test.mid') 

fe = features.jSymbolic.AverageNoteDurationFeature(parsed) # Average Note Duration
feature = fe.extract()
print(feature.vector)

fe2 = features.jSymbolic.ChangesOfMeterFeature(parsed) # Has time signature changed in the piece?
feature2 = fe2.extract()
print(feature2.vector)

# ------------------- Computing the Playing Speed ------------------------------------

x1 = stream.Stream(parsed)
sum = 0
for x in x1.flat.notes:
    sum+=x.beat
    
    
PS = (60/tempo) * (sum/len(x1.flat.notes))
    
#-------------------------------------------------------------------------------------