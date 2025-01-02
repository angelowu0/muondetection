from definitions import *
import matplotlib.pyplot as plt
import seaborn as sns


def display_muon_decay_hist(muon_events: list[MuonEvent]) -> None:
    """
    Displays Muon Events list as histogram using seaborn

    :param muon_events: list of muonevent objects
    """

    # creates a list of all decay times in microseconds
    decay_times = [i.decay_time / 1000 for i in muon_events]
    ax = sns.histplot(decay_times, kde=True, color="r", binwidth=1, discrete=True)
    ax.set_title("Muon Decay Times Frequency")
    ax.set_xlabel("Muon Decay Time (μs)")
    ax.set_ylabel("No. of Muon Decays")
    plt.show()
