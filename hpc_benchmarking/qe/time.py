# User will have to first install ALIGNN: https://github.com/atomgptlab/alignn
# To train the model, use the following command: train_alignn.py --root_dir "alignn/examples/sample_data" --config "alignn/examples/sample_data/config_example.json"
# Edit the config_example.json file with vim, nano, etc and modify hyperparameters of interest
# Put in resulting values into the script below to plot time (y1, y2, ...) vs hyperparameter (x)

import numpy as np
import matplotlib.pyplot as plt

rcparams = {"font.size": 14,
            "legend.frameon": False,
            "xtick.top": True,
            "xtick.direction": "in",
            "xtick.minor.visible": True,
            "xtick.major.size": 8,
            "xtick.minor.size": 4,
            "ytick.right": True,
            "ytick.direction": "in",
            "ytick.minor.visible": True,
            "ytick.major.size": 8,
            "ytick.minor.size": 4}
plt.rcParams.update(rcparams)

# Data
x = [3,15,30,60,120,240,450]
y1 = [4.71, 20.26, 43.02, 86.15, 189.34, 432.67, 860.40]
y2 = [1.80, 6.76, 12.81, 25.43, 58.83, 118.84, 231.63]

plt.figure()
plt.plot(x, y1, 'g-', marker='o', label='ALIGNN')
plt.plot(x, y2, 'b-', marker='s', label='ALIGNN-FF')

plt.xlabel("Number of Iterations")
plt.ylabel("Time(s)")
plt.legend()
plt.savefig('time_vs_epoch.pdf')
plt.show()