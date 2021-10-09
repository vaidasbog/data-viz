import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import ticker
import matplotlib.dates as dates

GRAY1, GRAY2, GRAY3 = '#231F20', '#414040', '#555655'
GRAY4, GRAY5, GRAY6 = '#646369', '#76787B', '#828282'
GRAY7, GRAY8, GRAY9 = '#929497', '#A6A6A5', '#BFBEBE'
BLUE1, BLUE2, BLUE3, BLUE4 = '#174A7E', '#4A81BF', '#94B2D7', '#94AFC5'
RED1, RED2 = '#C3514E', '#E6BAB7'
GREEN1, GREEN2 = '#0C8040', '#9ABB59'
ORANGE1 = '#F79747'
WHITE1 = '#FFFFFF'

mpl.rcParams['figure.figsize'] = 6.5, 4         # figure size
mpl.rcParams['figure.dpi'] = 100                # dots per inch, magnifying effect
mpl.rcParams['axes.spines.top'] = False         # Remove top spine
mpl.rcParams['axes.spines.right'] = False       # Remove right spine
mpl.rcParams['axes.spines.left'] = False        # Remove left spine
mpl.rcParams['axes.edgecolor'] = GRAY5          # Gray edge collors
mpl.rcParams['xtick.color'] = GRAY5             # Gray yticks
mpl.rcParams['ytick.color'] = GRAY5             # Gray xticks
mpl.rcParams['ytick.labelleft'] = False         # Remove y-axis tick lables
mpl.rcParams['ytick.major.left'] = False        # Remove y-axis ticks
mpl.rcParams['text.color'] = GRAY5              # Text
mpl.rcParams['font.family'] = 'Arial'           # Font

segments = ['Segment 1', 'Segment 2', 'Segment 3', 'Segment 4', 'Segment 5', 'Segment 6', 'Segment 7']
us = [0.16, 0.07, 0.1, 0.1, 0.1, 0.32, 0.15]
our = [0.09, 0.1, 0.15, 0.18, 0.17, 0.2, 0.11]
data = pd.DataFrame({'US population': us, 'Our Customers': our}, index=segments)

fig, ax = plt.subplots()

width = 0.5
white_space = 0.004
bottom1 = pd.Series([0])
bottom2 = bottom1

for seg in data.index:
    color_bar, color_text, fontweight = GRAY9, GRAY6, 'normal'
    if seg in ['Segment 3', 'Segment 4', 'Segment 5']:
        color_bar, color_text, fontweight = BLUE1, BLUE1, 'medium'
    ax.bar(['US Population'], data.loc[seg]['US population'], width=width, bottom=bottom1, color=color_bar)
    ax.bar(['Our Customers'], data.loc[seg]['Our Customers'], width=width, bottom=bottom2, color=color_bar)

    ax.text(-0.7, bottom1 + data.loc[seg]['US population']*0.5, seg, color=color_text, fontweight=fontweight)

    bottom1 = bottom1 + data.loc[seg]['US population'] + white_space
    bottom2 = bottom2 + data.loc[seg]['Our Customers'] + white_space
    
for i in range(0, 14):
    color = GRAY5
    if i in range(4, 10):
        color=GRAY9
    ax.bar_label(ax.containers[i], labels=[f"{ax.containers[i].datavalues[0]:.0%}"], label_type='center', color=color, fontsize=10)

ax.set_xlim(-0.5, 1.5)

ax.text(-0.7, 1.2, 'Distribution by customer segment', color=GRAY4, fontsize=14)


ax.plot([0.3, 0.3], [0.24, 0.54], color=BLUE1)
ax.plot([1.3, 1.3], [0.19, 0.69], color=BLUE1)

ax.text(0.32, 0.36, '30%', color=BLUE1, fontweight='bold', fontsize=14)
ax.text(1.32, 0.4, '50%', color=BLUE1, fontweight='bold', fontsize=14)

plt.savefig('plots/bar_plot_1.png', bbox_inches="tight")
plt.show()


