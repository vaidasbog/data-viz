import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import ticker
import matplotlib.dates as dates

# Colors
GRAY1, GRAY2, GRAY3 = '#231F20', '#414040', '#555655'
GRAY4, GRAY5, GRAY6 = '#646369', '#76787B', '#828282'
GRAY7, GRAY8, GRAY9 = '#929497', '#A6A6A5', '#BFBEBE'
BLUE1, BLUE2, BLUE3, BLUE4 = '#174A7E', '#4A81BF', '#94B2D7', '#94AFC5'
RED1, RED2 = '#C3514E', '#E6BAB7'
GREEN1, GREEN2 = '#0C8040', '#9ABB59'
ORANGE1 = '#F79747'

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

days_last_year = list(range(31))
money_last_year = [0,	3867,	5736,	8352,	10784,	11573,	13756,	14112,	15836,	17836,	19710,	20174,	24967,	26937,	27947,	29753,	32957,	34027,	34532,	36345,	39271,	43287,	43900,	44783,	45937,	46735,	47110,	48037,	49736,	50123,	51400]
days_this_year = list(range(11))
money_this_year = [0,	4962,	8163,	12746,	15736,	23658,	25735,	27562,	28563,	31967,	33967]

fig, ax = plt.subplots()

ax1 = plt.plot(days_last_year, money_last_year, color=BLUE3, lw=1, marker='o', markevery=[30], markersize=5)
ax2 = plt.plot(days_this_year, money_this_year, color=BLUE2, lw=3, marker='o', markevery=[10], markersize=7)

# Limits
ax.set_xlim(0, 31)
ax.set_ylim(0, 60000)

# X-axis formatting
ax.yaxis.set_major_formatter(ticker.StrMethodFormatter('${x:,.0f}'))

# Annotations
ax.text(days_last_year[-1]+0.5, money_last_year[-1]*1.06, f"Last year", fontsize=10, fontweight='normal', color=BLUE3)
ax.text(days_last_year[-1]+0.5, money_last_year[-1]*0.98, f"${money_last_year[-1]:,}", fontsize=10, fontweight='normal', color=BLUE3)

ax.text(days_this_year[-1]-3.7, money_this_year[-1]*1.12, f"Progress to date", fontsize=14, fontweight='normal', color=BLUE2)
ax.text(days_this_year[-1]+0.7, money_this_year[-1]*0.98, f"${money_this_year[-1]:,}", fontsize=14, fontweight='bold', color=BLUE2)

ax.text(-0.1, -8e3, f"Days since campaign lounch", fontsize=10, fontweight='normal', color=GRAY5)
ax.text(-5.5, 45e3, f"Money raised", fontsize=10, fontweight='normal', color=GRAY5, rotation='vertical')
ax.text(-5.5, 70000, f"Annual giving campaign progress", fontsize=14, fontweight='normal', color=GRAY5)

ax.annotate("", xy=(-0.7, 50000), xytext=(0.7,50000), xycoords="data",
             arrowprops={"arrowstyle":"-", "linestyle":"-", "linewidth":1, "color": GRAY5}, annotation_clip=False)
ax.text(1, 49e3, f"GOAL", fontsize=10, fontweight='normal', color=GRAY5)

ax.annotate("", xy=(3.5, 50000), xytext=(30.4,50000), xycoords="data",
             arrowprops={"arrowstyle":"-", "linestyle":"-", "linewidth":1, "color": GRAY5}, annotation_clip=False)

# Remove tick at 50,000
for ix, tick in enumerate(ax.yaxis.get_major_ticks()):
    if ix==5:
        tick.tick1line.set_markersize(0)

plt.savefig('plots/progress_line_plot.png', bbox_inches="tight")
plt.show()


