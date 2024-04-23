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
   - Loads EEG data or downloads it over the internet, reads the data into epochs for further analysis.

Authors
---------
Nick Hanna, Michael Gallo
"""

#%% Imports
import mne

#%% Loading EEG Data
def load_eeg_data(data_directory=".") -> mne.Epochs:
    """
    Searches for kiloword dataset in `data_directory`. If not found, it downloads the dataset to:
    `${data_directory}/MNE-kiloword-data/kword_metadata-epo.fif`. Loads the epochs from dataset into a 
    variable and returns it for further analysis.
    
    Parameters:
    ----------
    data_directory <str>
        Path (with no trailing '/') from execution directory to location in which to store dataset folder.

    Returns:
    -------
    dataset_epochs <mne.Epochs>
        info <mne.Info>
            Information object with info about the sensors and methods of measurement.
        event_id <dict>
            Mapping from condition descriptions (strings) to integer event codes.
        ch_names <list of str>
            Channel names, in string format.
        selection <np.ndarray>
            Array of indices of selected epochs (i.e., epochs that were not rejected or ignored).
    """

    # Attempts to find path to the dataset, if it can't find the path it downloads the dataset, returns path to data file
    file_path = mne.datasets.kiloword.data_path(path=data_directory, force_update=False, update_path=True, download=True)
    # Reads the raw data from the fif file, as found/downloaded in previous step
    epochs_data = mne.read_epochs(f"{file_path}/kword_metadata-epo.fif")

    return epochs_data