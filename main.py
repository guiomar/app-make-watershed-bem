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

#subjects_dir: path to the directory containing the FreeSurfer subjects reconstructions (SUBJECTS_DIR)
subjects_dir = __location__ 
#subject: Name of freesurfer subject folder
subject = 'output'

report = mne.Report(title='Report')

mne.bem.make_watershed_bem(subject, subjects_dir=subjects_dir)


report.add_bem(
    subject=subject,
    subjects_dir=subjects_dir,
    title="MRI & BEM",
    decim=40,
    width=256,
)

 
 # == SAVE REPORT ==
report.save(os.path.join('out_dir','report.html'))
