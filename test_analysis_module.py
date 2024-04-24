"""

# EEG Signal Analysis Testing File

Created on Monday Apr 22 07:20:09 2024

File Name
----------
(File names are temporary, feel free to change)
test_analysis_module.py

Description
-------------
Performs an analysis of data loaded from MNE's copy of the kilowords dataset.

Authors
---------
Nick Hanna, Michael Gallo
"""

#%% Imports
import analysis_module
import numpy as np

#%% Load epochs from dataset
data = analysis_module.load_eeg_data('data/S01T.mat')

# For testing, shows some information about the dataset
# NOTE while it looks like the eeg information is all zeroes, there is information between
for i, obj in enumerate(data):
    print('\n==============================')
    print(f"Set {i} of training values")
    for key in obj.keys():
        print(f"Key: {key}")
        if type(obj) == list or type(obj) == np.ndarray:
            print(f"Data Shape: {obj[key].shape}")
        else:
            print(f"Data value: {obj[key]}")