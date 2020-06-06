
# coding: utf-8

# In[2]:

#番外編pyaudio test

import pyaudio
import numpy as np

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32,
               channels=1,
               rate=44100,
               frames_per_buffer=1024,
               output=True)

sample = np.sin(np.arange(50000) / 20)

print("play")
stream.write(sample.astype(np.float32).tostring())
stream.close()

