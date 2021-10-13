import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import ticker

GRAY1, GRAY2, GRAY3 = '#231F20', '#414040', '#555655'
GRAY4, GRAY5, GRAY6 = '#646369', '#76787B', '#828282'
GRAY7, GRAY8, GRAY9 = '#929497', '#A6A6A5', '#BFBEBE'
BLUE1, BLUE2, BLUE3, BLUE4 = '#174A7E', '#4A81BF', '#94B2D7', '#94AFC5'
RED1, RED2 = '#C3514E', '#E6BAB7'
GREEN1, GREEN2 = '#0C8040', '#9ABB59'
ORANGE1 = '#F79747'
WHITE1 = '#FFFFFF'

# Setting the stage
mpl.rcParams['figure.figsize'] = 6.5, 4         # figure size
mpl.rcParams['figure.dpi'] = 100                # dots per inch, magnifying effect
mpl.rcParams['axes.spines.top'] = False         # Remove top spine
mpl.rcParams['axes.spines.right'] = False       # Remove right spine
mpl.rcParams['axes.edgecolor'] = GRAY5          # Gray edge collors
mpl.rcParams['xtick.color'] = GRAY5             # Gray yticks
mpl.rcParams['ytick.color'] = GRAY5             # Gray xticks
mpl.rcParams['text.color'] = GRAY5              # Text
mpl.rcParams['font.family'] = 'Arial'           # Font

# Data
quarter = ['Q1',	'Q2',	'Q3',	'Q4',	'Q1',	'Q2',	'Q3',	'Q4',	'Q1',	'Q2',	'Q3']
miss = [0.05,	0.03,	0.06,	0.05,	0.06,	0.06,	0.12,	0.15,	0.2,	0.33,	0.42]
meet = [0.53,	0.62,	0.68,	0.7,	0.75,	0.59,	0.61,	0.62,	0.68,	0.62,	0.47]
exceed = [0.42,	0.35,	0.26,	0.25,	0.19,	0.35,	0.27,	0.23,	0.12,	0.05,	0.11]

fig, ax = plt.subplots(figsize=(9, 4))

width = 0.65
ax1 = ax.bar(range(len(quarter)), miss, color=RED1, width=width, label='Miss')
ax2 = ax.bar(range(len(quarter)), meet, bottom=ax1.datavalues, color=GRAY9, width=width, label='Meet')
ax3 = ax.bar(range(len(quarter)), exceed, bottom=ax2.datavalues + ax1.datavalues, color=GRAY6, width=width, label='Exceed')

#
ax.set_ylim(0, 1)
ax.set_xlim(-0.5, 10.5)

# Bar lables
ax.bar_label(ax1, labels=[f"{i:.0%}"  if ix > 5 else "" for ix, i in enumerate(miss)], label_type='center', color=WHITE1, fontsize=12);

# Y-axis formatting
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.1))
ax.yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1))     # Percent formatter

# X-axis formatting
ax.xaxis.set_major_locator(ticker.FixedLocator(list(range(-1, 11))))
majors = [""] + quarter
ax.xaxis.set_major_formatter(ticker.FixedFormatter(majors))
for tick in ax.xaxis.get_major_ticks():
    tick.tick1line.set_markersize(0)
for i in range(len(quarter)+1):
    length = 0.1
    if i in [0, 4, 8, 11]: length=0.2
    ax.annotate("", xy=(i-0.5, 0+0.005), xytext=(i-0.5,-length), xycoords="data",
                arrowprops={"arrowstyle":"-", "linestyle":"-", "linewidth":1, "color": GRAY5}, annotation_clip=False)
ax.text(1.25, -0.2, '2013', color=GRAY5, fontsize=12)
ax.text(5.25, -0.2, '2014', color=GRAY5, fontsize=12)
ax.text(8.75, -0.2, '2015', color=GRAY5, fontsize=12)

# Legend
ax.legend(loc='upper left', bbox_to_anchor=(-0.11, 1.2), ncol=3, frameon=False, handlelength=0.7, handletextpad=0.4, labelcolor=[RED1, GRAY9, GRAY6])

# Annotations
ax.text(-1.5, 0.665, "% of total projects", rotation='vertical', color=GRAY5)
caption = f"Data source: XYZ Dashboard; the total number of projects has increased overt time from 230 in early 2013 to nearly 270 in Q3 2015."
ax.text(-1.5, -0.3, caption, color=GRAY5, fontsize=9)

ax.text(-1.5, 1.21, f"Goal attainment over time", color=GRAY4, fontsize=15)

ax.text(6.5, 1.15, "As of Q3 2015,", color=GRAY4, fontsize=12)
ax.text(8.3, 1.15, "more than 1/3 of", color=RED1, fontsize=12, fontweight='bold')
ax.text(6.5, 1.08, "of projects are missing goals", color=RED1, fontsize=12, fontweight='bold')

plt.savefig('plots/bar_plot_2.png', bbox_inches="tight")
plt.show()

