import os
import json
import mne

import matplotlib.pyplot as plt
import numpy as np


# Current path
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Load inputs from config.json
with open('config.json') as config_json:
    config = json.load(config_json)

# subjects_dir: path to the directory containing the FreeSurfer subjects reconstructions (SUBJECTS_DIR)
subjects_dir = config['output']
subjects_dir = os.path.dirname(subjects_dir)
#subjects_dir = os.environ['SUBJECTS_DIR']

# subject: Name of freesurfer subject folder
subject = 'output'
#subject_id=os.path.basename(os.path.normpath(sys.argv[2]))

# Start MNE-Report
report = mne.Report(title='Report')

# Make Watershed BEM
mne.bem.make_watershed_bem(subject, subjects_dir=subjects_dir)

# Add BEM to MNE-Report
report.add_bem(
    subject=subject,
    subjects_dir=subjects_dir,
    title="MRI & BEM",
    decim=40,
    width=256,
)

# == SAVE REPORT ==
report.save(os.path.join('out_dir_report','report.html'))
