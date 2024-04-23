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

#%% Load epochs from dataset
epochs_data = analysis_module.load_eeg_data()

# Examples
print(epochs_data.ch_names)