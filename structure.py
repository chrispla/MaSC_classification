import glob
import numpy as np
import librosa
import os
import msaf

#File reading
all_dirs = []
for root, dirs, files in os.walk('./Test1'): #change directory here
        for name in files:
            if '.wav' in name:
                filedir = os.path.join(root, name)
                all_dirs.append(filedir)
print(len(all_dirs))

all_struct = []
for i in range(len(all_dirs)):
    #boundaries, labels = msaf.process(all_dirs[i], boundaries_id="foote", labels_id="cnmf")
    librosa.load(all_dirs[i])
    #boundaries, labels = msaf.process(all_dirs[i])
    #all_struct.append([boundaries, labels])
    #print(str(i) + ": " + str(boundaries))
   
