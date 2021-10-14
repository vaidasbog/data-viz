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
# dots per inch, magnifying effect
mpl.rcParams['figure.dpi'] = 100
mpl.rcParams['axes.spines.top'] = False         # Remove top spine
mpl.rcParams['axes.spines.right'] = False       # Remove right spine
mpl.rcParams['axes.edgecolor'] = GRAY5          # Gray edge collors
mpl.rcParams['xtick.color'] = GRAY5             # Gray yticks
mpl.rcParams['ytick.color'] = GRAY5             # Gray xticks
mpl.rcParams['text.color'] = GRAY5              # Text
mpl.rcParams['font.family'] = 'Arial'           # Font


# %%
data = pd.DataFrame({
    'Unmet need': [0, 28, 50, 68, 91, 112],
    'Directors from acquisitions': [0, 3, 3, 3, 3, 3],
    'Promotions to director': [0, 7, 10, 13, 17, 21],
    "Today's directors": [191, 165, 148, 129, 111, 91],
    'Attrition': [0, -26, -43, -62, -80, -100]
}, index=["Today\n9/30/15", "FY16", "FY17", "FY18", "FY19", "FY20"])


fig, ax = plt.subplots()

width = 0.65
ax0 = ax.bar(range(0, 6), data['Attrition'], width=width,
             color=BLUE3, edgecolor=BLUE3, clip_on=False)
ax1 = ax.bar(range(0, 6), data["Today's directors"],
             width=width, color=BLUE2, edgecolor=BLUE2)
ax2 = ax.bar(range(0, 6), data["Promotions to director"], width=width,
             bottom=ax1.datavalues, color=GREEN1, edgecolor=GREEN1)
ax3 = ax.bar(range(0, 6), data["Directors from acquisitions"], width=width,
             bottom=ax1.datavalues+ax2.datavalues, color=GREEN2, edgecolor=GREEN2)
ax4 = ax.bar(range(0, 6), data["Unmet need"], width=width, bottom=ax1.datavalues +
             ax2.datavalues+ax3.datavalues, color=WHITE1, edgecolor=GRAY5, linewidth=0.6)

ax.set_ylim(0, 250)

# Anotations
ax.text(-1.3, 185, "# of directors", color=GRAY5,
        rotation='vertical', fontsize=11)
ax.text(5.5, -95, "Attrition", color=BLUE3, fontsize=11)
ax.text(5.5, 78, "Today's directors", color=BLUE2, fontsize=11)
ax.text(5.5, 95, "Promotions to director", color=GREEN1, fontsize=11)
ax.text(5.5, 111, "Directors from acquisitions", color=GREEN2, fontsize=11)
ax.text(5.5, 210, "Unmet need (gap)", color=GRAY5,
        fontsize=14, fontweight='bold')
ax.text(-1.3, 280, "Expected director population over time",
        color=GRAY5, fontsize=16, fontweight='normal')
ax.text(-1.3, -120, "A footnote explaining relevnat forecast assumptions and methodology would go here.",
        color=GRAY5, fontsize=9.5, fontweight='normal')

ax.text(0.87, 185, "28", color=GRAY5, fontsize=14, fontweight='bold')
ax.text(1.87, 190, "50", color=GRAY5, fontsize=14, fontweight='bold')
ax.text(2.87, 195, "68", color=GRAY5, fontsize=14, fontweight='bold')
ax.text(3.87, 200, "91", color=GRAY5, fontsize=14, fontweight='bold')
ax.text(4.8, 205, "112", color=GRAY5, fontsize=14, fontweight='bold')

ax.set_xticklabels([""]+data.index.tolist())
[tick.tick1line.set_markersize(0) for tick in ax.xaxis.get_major_ticks()]

plt.savefig('plots/bar_plot_3.png', bbox_inches="tight")
plt.show()
