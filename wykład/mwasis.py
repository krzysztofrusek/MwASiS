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

"""
Stdout/stderr redirector, at the OS level, using file descriptors.

This also works under windows.
"""

__docformat__ = "restructuredtext en"

#-------------------------------------------------------------------------------
#  Copyright (C) 2008  The IPython Development Team
#
#  Distributed under the terms of the BSD License.  The full license is in
#  the file COPYING, distributed as part of this software.
#-------------------------------------------------------------------------------


import os
import sys

STDOUT = 1
STDERR = 2

class FDRedirector(object):
    """ Class to redirect output (stdout or stderr) at the OS level using
        file descriptors.
    """ 

    def __init__(self, fd=STDOUT):
        """ fd is the file descriptor of the outpout you want to capture.
            It can be STDOUT or STERR.
        """
        self.fd = fd
        self.started = False
        self.piper = None
        self.pipew = None

    def start(self):
        """ Setup the redirection.
        """
        if not self.started:
            self.oldhandle = os.dup(self.fd)
            self.piper, self.pipew = os.pipe()
            os.dup2(self.pipew, self.fd)
            os.close(self.pipew)

            self.started = True

    def flush(self):
        """ Flush the captured output, similar to the flush method of any
        stream.
        """
        if self.fd == STDOUT:
            sys.stdout.flush()
        elif self.fd == STDERR:
            sys.stderr.flush()

    def stop(self):
        """ Unset the redirection and return the captured output. 
        """
        if self.started:
            self.flush()
            os.dup2(self.oldhandle, self.fd)
            os.close(self.oldhandle)
            f = os.fdopen(self.piper, 'r')
            output = f.read()
            f.close()

            self.started = False
            return output
        else:
            return ''

    def getvalue(self):
        """ Return the output captured since the last getvalue, or the
        start of the redirection.
        """
        output = self.stop()
        self.start()
        return output
# https://github.com/bitemyapp/ipython/blob/master/IPython/kernel/core/fd_redirector.py

from silence_tensorflow import silence_tensorflow
silence_tensorflow()

import os
import matplotlib_inline


import logging

# Suppress absl warnings
try:
    absl_logger = logging.getLogger('absl')
    absl_logger.setLevel(logging.ERROR) # Or logging.CRITICAL
except AttributeError: # In case absl is not found or used directly
    pass

# You can also try a more general approach if the specific logger name is unknown
# logging.basicConfig(level=logging.ERROR) # This might be too broad


os.environ["JAX_ENABLE_X64"] = "True"
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '4'  # 0: DEBUG, 1: INFO, 2: WARNING, 3: ERROR, 4: FATAL
# os.environ['XLA_FLAGS'] = '--tf_xla_logging_level=0'

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

import scipy
import scipy.stats as stats