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
mpl.rcParams['axes.spines.bottom'] = False      # Remove bottom spine
mpl.rcParams['axes.spines.right'] = False       # Remove right spine
mpl.rcParams['axes.spines.left'] = False        # Remove left spine
mpl.rcParams['axes.edgecolor'] = GRAY2          # Gray edge collors
mpl.rcParams['xtick.color'] = GRAY2             # Gray xticks
mpl.rcParams['ytick.color'] = GRAY2             # Gray yticks
mpl.rcParams['ytick.left'] = False              # Remove y-axis ticks
mpl.rcParams['ytick.labelleft'] = False         # Remove y-axis tick lables
mpl.rcParams['xtick.bottom'] = False            # Remove y-axis ticks
mpl.rcParams['xtick.labelbottom'] = True            # Remove y-axis tick lables
mpl.rcParams['text.color'] = GRAY2              # Text
mpl.rcParams['font.family'] = 'Arial'           # Font

# Data
area = ['Education',	'Agriculture & rural development',	'Poverty reduction',	'Reconstruction',	'Economic growth',	'Health',	'Job creation',	'Governanace',	'Anti-corruption',	'Transport',	'Energy',	'Law & Justice',	'Basic infrastructure',	'Public sector reform',	'Public financial management']
most = [0.24,	0.17,	0.15,	0.09,	0.07,	0.03,	0.04,	0.05,	0.04,	0.04,	0.03,	0.02,	0.02,	0.02,	0.02]
most_2 = [0.14,	0.12,	0.1,	0.05,	0.05,	0.07,	0.06,	0.05,	0.04,	0.04,	0.04,	0.03,	0.03,	0.03,	0.03]
most_3 = [0.07,	0.08,	0.07,	0.04,	0.05,	0.06,	0.05,	0.04,	0.06,	0.04,	0.04,	0.04,	0.03,	0.03,	0.03]
overall = [0.45,	0.37,	0.32,	0.18,	0.17,	0.16,	0.15,	0.14,	0.14,	0.12,	0.11,	0.09,	0.08,	0.08,	0.08]

data=pd.DataFrame({'Most Important': most, '2nd Most Important': most_2, '3rd Most Important': most_3, 'Overall': overall}, index=area)
data.sort_values(by='Overall', inplace=True, ascending=True)
data

fig, ax = plt.subplots(figsize=(8, 8))

height = 0.6

color_ax1 = [GRAY5 if i in range(12) else BLUE1 for i in range(data.shape[0])]
ax1 = ax.barh(data.index, data['Most Important'], color=color_ax1, height=height)

color_ax2 = [GRAY7 if i in range(12) else BLUE2 for i in range(data.shape[0])]
ax2 = ax.barh(data.index, data['2nd Most Important'], color=color_ax2, left=ax1.datavalues, height=height)

color_ax3 = [GRAY9 if i in range(12) else BLUE3 for i in range(data.shape[0])]
ax3 = ax.barh(data.index, data['3rd Most Important'], color=color_ax3, left=ax1.datavalues + ax2.datavalues, height=height)

# Bar labels
color_ax3_bl = [GRAY5 if i in range(12) else BLUE1 for i in range(data.shape[0])]
for ix in range(data.shape[0]):
    pad_x = 0.01 if ix > 4 else 0.00125
    pad_y = -0.1
    ax.text(pad_x, ix+pad_y, f"{data['Most Important'][ix]:.0%}", color=WHITE1, fontsize=8)
    ax.text(ax1.datavalues[ix] + pad_x, ix+pad_y, f"{data['2nd Most Important'][ix]:.0%}", color=WHITE1, fontsize=8)
    ax.text(ax1.datavalues[ix] + ax2.datavalues[ix] + pad_x, ix+pad_y, f"{data['3rd Most Important'][ix]:.0%}", color=color_ax3_bl[ix], fontsize=8)

color_tick_label = [GRAY5 if i in range(12) else BLUE1 for i in range(data.shape[0])]
fw_tick_label = ['normal' if i in range(12) else 'bold' for i in range(data.shape[0])]
[ax.text(-0.04, i-0.1, f"{data['Overall'][i]:.0%}", color=color_tick_label[i], fontweight=fw_tick_label[i], fontsize=12) for i in range(data.shape[0])]
[ax.text(-0.05, i-0.1, f"{data.index[i]}", color=color_tick_label[i], fontweight=fw_tick_label[i], fontsize=12, ha="right") for i in range(data.shape[0])];

names = f"PRIORITY   TOTAL %  " + r"$\bf{Most}$" + " important | " + r"$\bf{2nd}$" + " Most important | " + r"$\bf{3rd}$" + " Most important"
ax.text(-.1, 15, names, color=GRAY5, fontsize=9);

ax.annotate("", xy=(-0.25, 16), xytext=(0.46, 16), xycoords="data", arrowprops={"arrowstyle":"-", "linestyle":"-", "linewidth":1.5, "color": GRAY9}, annotation_clip=False)
ax.annotate("", xy=(-0.25, -1), xytext=(0.46, -1), xycoords="data", arrowprops={"arrowstyle":"-", "linestyle":"-", "linewidth":1.5, "color": GRAY9}, annotation_clip=False)
ax.tick_params(axis='x', labelsize=0) # to Set Matplotlib Tick Labels Font Size

caption = f"N = 4,392. Based on responses to item. When considering development priorities, which one development priority is the most important? Which one is\n"+f"the second most important priority? Which one is the third most important priority? Respondents chose from a list. Top 15 shown."
ax.text(-0.25, -2, caption, color=GRAY5, fontsize=9, clip_on=False)

ax.text(-0.25, 16.5, 'Top 15 development priorities, according to survey', color=GRAY5, fontsize=14, clip_on=False)

plt.savefig('plots/hbar_plot_2.png', bbox_inches="tight")
plt.show()


