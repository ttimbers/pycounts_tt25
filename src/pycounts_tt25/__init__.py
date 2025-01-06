# read version from installed package
from importlib.metadata import version
__version__ = version("pycounts_tt25")


from pycounts_tt25.pycounts_tt25 import count_words
from pycounts_tt25.plotting import plot_words