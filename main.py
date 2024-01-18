import mne
import json
import os
import os.path as op
import matplotlib.pyplot as plt
from pathlib import Path
import tempfile
import numpy as np
import scipy.ndimage
import matplotlib.pyplot as plt
import sys

#workaround for -- _tkinter.TclError: invalid command name ".!canvas"
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


import mne


# Current path
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Load inputs from config.json
with open('config.json') as config_json:
    config = json.load(config_json)

# Read the location

#subj_dir is supposed to be the subjects directory in FREESURFER SUBJECTS_DIR, but because we are on Brainlife, the freesurfer datatype points to a directory (???)
#We suppose that 'output' is going to serve as subject ID
subj_dir = __location__
subj = 'output'

report = mne.Report(title='Report')

mne.bem.make_watershed_bem(subj, subjects_dir=subj_dir)

report.add_html(title='Counts of correct responses',html='<dev>'+'Correct responses: '+str(correct_response_count)+
       'Incorrect responses: '+str(incorrect_response_count)+'</dev>')
 
 # == SAVE REPORT ==
report.save(os.path.join('out_dir','report.html'))

 # == SAVE FILE ==
epochs.save(os.path.join('out_dir', 'meg-epo.fif'), overwrite=True)
