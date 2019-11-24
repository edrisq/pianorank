# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 16:36:12 2019

@author: amisr
"""

from music21 import *

n = note.Note("D#3")
n.duration.type = 'half'
n.show()