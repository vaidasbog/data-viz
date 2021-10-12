import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import ticker
import matplotlib.dates as dates
import matplotlib.patches as patches

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
mpl.rcParams['axes.edgecolor'] = GRAY2          # Gray edge collors
mpl.rcParams['xtick.color'] = GRAY2             # Gray yticks
mpl.rcParams['ytick.color'] = GRAY2             # Gray xticks
mpl.rcParams['text.color'] = GRAY2              # Text
mpl.rcParams['font.family'] = 'Arial'           # Font

# Data
years = ['2006', '2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
sales = [52,54 ,60 ,64 ,78 ,86 ,91 ,100 ,108 ,119 ,131 ,144 ,158]

fig, ax = plt.subplots(figsize=(8.5, 4))

ax1 = plt.plot(years[:-4], sales[:-4], '-o', markevery=[0, 3, 4, 8], color=BLUE2, lw=3, markerfacecolor=WHITE1, zorder=2, clip_on=False)
ax2 = plt.plot(years[-5:], sales[-5:], '--', color=BLUE2, lw=2, zorder=1, marker='o', markersize=5, clip_on=False)

ax.set_ylim(0, 180)
ax.set_xlim(-0.5, len(years)-0.5)

# Annotations
for i in range(9, 13):
    ax.text(i-0.25, sales[i]+9, f"${sales[i]}", color=BLUE2, fontsize=12)
ax.text(8-0.25, sales[8]+9, f"${sales[8]}", color=BLUE2, fontsize=12, fontweight='bold')

txt1 = [f"2006-09:", f"2010:", f"2011-14:", f"2015 & beyond:"]
txt2 = [
    f"annual sales\ngrowth of\n7-8%", 
    f"more marked\nincrease of\n22% sales\nyear over\nyear, drive\nby a, b, c", 
    f"another period\nof steady growth\nof 8-9% annually", 
    f"assumed 10% year\nover year increas\nin sales"]
for ix, txt1 in zip([0, 2, 4, 7.5], txt1):
    ax.text(ix+0.2, 175, txt1, color=BLUE2, fontsize=12, fontweight='bold')

ax.text(0+0.2, 146, txt2[0], color=GRAY4, fontsize=11, fontweight='normal')
ax.text(2+0.2, 118, txt2[1], color=GRAY4, fontsize=11, fontweight='normal')
ax.text(4+0.2, 146, txt2[2], color=GRAY4, fontsize=11, fontweight='normal')
ax.text(7.5+0.2, 146, txt2[3], color=GRAY4, fontsize=11, fontweight='normal')

ax.text(-1.7, 126, "Sales ($Billion)", color=GRAY4, fontsize=11, fontweight='normal', rotation='vertical')

ax.text(-1.7, 200, "Sales over time", color=GRAY4, fontsize=16, fontweight='normal')

ax.text(3.5, -30, "ACTUAL", color=GRAY4, fontsize=12, fontweight='normal')
ax.text(9.5, -30, "FORECAST", color=GRAY4, fontsize=12, fontweight='normal')

ax.text(-1.7, -60, 
"Data source: Sales Dashboard; annual figures are as of 12/31 of the given year." +
"\n*Use this footnote to explain what is driving the 10% annual growth forecast assumption", color=GRAY4)

# Y-axis formatting
ax.yaxis.set_major_formatter(ticker.StrMethodFormatter('${x:,.0f}'))

# X-axis ticks
for tick in ax.xaxis.get_major_ticks():
    tick.tick1line.set_markersize(0)

for i in range(len(years)+1):
    length = 20
    if i in [0, 9, 13]: length=35
    ax.annotate("", xy=(i-0.49, 1), xytext=(i-0.49,-length), xycoords="data",
                arrowprops={"arrowstyle":"-", "linestyle":"-", "linewidth":1, "color": GRAY5}, annotation_clip=False)

# Gray rectangle
rect = patches.Rectangle((8.5, -35), 4, 35, linewidth=1, edgecolor=GRAY9, facecolor=GRAY9, clip_on=False, alpha=0.5)
ax.add_patch(rect)

plt.savefig('plots/line_plot_3.png', bbox_inches="tight")
plt.show()


