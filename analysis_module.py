"""

# EEG Signal Analysis Module

Created on Monday Apr 22 07:20:09 2024

File Name
----------
(File names are temporary, feel free to change)
analysis_module.py

Description
-------------
This script provides tools for analyzing MNE's EEG data:

1. load_eeg_data()

Authors
---------
Nick Hanna, Michael Gallo
"""

#%% Imports
from loadmat import loadmat

#%% Load EEG Data
def load_eeg_data(file_path):
    """
    Loads EEG data for a specific subject from a .mat file used in the Motor Imagery BCI study.
    This dataset includes multiple sessions, each containing EEG signals, trial information,
    class labels, and other metadata necessary for BCI analysis.

    Parameters:
    ----------
    file_path : str
        The path to the .mat file containing the EEG data and metadata.

    Returns:
    -------
    data : list of dicts
        A list where each element is a dictionary corresponding to a session of EEG recordings.
        Each dictionary contains the following keys:
        'X' : np.ndarray
            The EEG data recorded during the session, shaped (channels, time points).
        'trial' : np.ndarray
            Indices in 'X' where each trial starts, shaped (number_of_trials,).
        'y' : np.ndarray
            Labels for each trial indicating the performed motor imagery task, shaped (number_of_trials,).
        'fs' : int
            Sampling frequency of the EEG data.
        'classes' : list of str
            Names of the classes corresponding to labels in 'y'.
    """
    # Load and return the .mat file
    data = loadmat('data/S01T.mat')['data']
    # Account for the fact that matlab indices start at 1...
    for session_number in range(len(data)):
        data[session_number]['trial'] = data[session_number]['trial'] - 1
        data[session_number]['y'] = data[session_number]['y'] - 1

    return data
