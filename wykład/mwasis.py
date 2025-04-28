import matplotlib as mpl
import seaborn as sns

sns.set_theme()
import numpy as np


mpl.rcParams['lines.linewidth'] = 2
#mpl.rcParams['lines.linestyle'] = '--'

mpl.rcParams['axes.titlesize'] = 14
mpl.rcParams['axes.labelsize'] = 10
mpl.rcParams['figure.figsize'] = (5.3, 2.5)
mpl.rcParams['figure.dpi']= 180
mpl.rcParams['figure.facecolor']= '#FAFAFA'

# mpl.rcParams['axes.facecolor']='#FAFAFA'
# mpl.rcParams['savefig.facecolor']='#FAFAFA'

import os
import matplotlib_inline

os.environ["JAX_ENABLE_X64"] = "True"

from IPython.display import  Image,Markdown,Latex, display
#set_matplotlib_formats('svg', 'pdf')
matplotlib_inline.backend_inline.set_matplotlib_formats('svg', 'pdf')

def abline(slope, intercept,c):
    """Plot a line from slope and intercept"""
    axes = mpl.pyplot.gca()
    x_vals = np.array(axes.get_xlim())
    y_vals = intercept + slope * x_vals
    mpl.pyplot.plot(x_vals, y_vals, '--', color=c)

import tensorflow as tf
import tensorflow_probability as tfp

tfb = tfp.bijectors
tfd = tfp.distributions
tfb= tfp.bijectors

import numpy as np





import seaborn as sns  # noqa: F401, I001
import pandas as pd  # noqa: F401
import matplotlib.pyplot as plt # noqa: F401

import warnings

# Ignorowanie ostrzeżeń RuntimeWarning
warnings.filterwarnings("ignore")


def display_df(df:pd.DataFrame):
    display(Markdown(df.to_markdown()))