import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties

def plotBarValues(labels, values, title, xlabel, ylabel):
    index = np.arange(len(labels))
    rects = plt.bar(index, values)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(index, labels, rotation=90)
    plt.title(title)
    plt.tight_layout()
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2., height+25, 
                '%d' % int(height), ha='center', va='bottom')
