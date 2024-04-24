#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
loadmat.py
Load a .mat file containing structs to create usable python structures.

- Code copied by DJ from https://stackoverflow.com/a/65195623 on 8/18/21
"""

import numpy as np
import scipy.io as sio

def _todict(matobj):
    """
    A recursive function which constructs from matobjects nested dictionaries.
    """
    dict = {}
    for strg in matobj._fieldnames:
        elem = matobj.__dict__[strg]
        if isinstance(elem, sio.matlab.mio5_params.mat_struct):
            dict[strg] = _todict(elem)
        elif isinstance(elem, np.ndarray) and elem.dtype.type is np.object_:
            # Recursively process each element in the ndarray that's a mat_struct
            dict[strg] = [_todict(el) if isinstance(el, sio.matlab.mio5_params.mat_struct) else el for el in elem]
        else:
            dict[strg] = elem
    return dict

def loadmat(filename):
    """
    this function should be called instead of direct scipy.io.loadmat
    as it cures the problem of not properly recovering python dictionaries
    from mat files. It calls the function check keys to cure all entries
    which are still mat-objects.
    """
    data = sio.loadmat(filename, struct_as_record=False, squeeze_me=True)
    return _check_keys(data)

def _check_keys(dict):
    """
    checks if entries in dictionary are mat-objects. If yes,
    todict is called to change them to nested dictionaries.
    """
    for key in dict:
        if isinstance(dict[key], sio.matlab.mio5_params.mat_struct):
            dict[key] = _todict(dict[key])
        elif isinstance(dict[key], np.ndarray) and dict[key].dtype.type is np.object_:
            dict[key] = [_todict(item) if isinstance(item, sio.matlab.mio5_params.mat_struct) else item for item in dict[key]]
    return dict
