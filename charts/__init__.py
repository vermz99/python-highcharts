__author__ = 'arnout'

from plot import plot, plotasync, line, area, spline, pie
from server import run_server

from IPython.core import getipython
from IPython.core.display import display, HTML

from settings import default_settings, default_options, load_options
import data
import jsonencoder