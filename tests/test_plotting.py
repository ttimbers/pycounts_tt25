import pycounts_tt25
from matplotlib.testing.decorators import image_comparison
import matplotlib.pyplot as plt


@image_comparison(baseline_images=['plot_words'], remove_text=True,
                  extensions=['png'], style='mpl20')
def test_plot_words():
    counts = pycounts_tt25.count_words("tests/einstein.txt")
    fig = pycounts_tt25.plot_words(counts, n=10)

