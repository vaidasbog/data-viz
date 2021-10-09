
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

mpl.rcParams['figure.figsize'] = 6.5, 4         # figure size
mpl.rcParams['figure.dpi'] = 100                # dots per inch, magnifying effect
mpl.rcParams['axes.spines.top'] = False         # Remove top spine
mpl.rcParams['axes.spines.right'] = False       # Remove right spine
mpl.rcParams['axes.spines.left'] = False        # Remove left spine
mpl.rcParams['axes.edgecolor'] = GRAY2          # Gray edge collors
mpl.rcParams['xtick.color'] = GRAY2             # Gray yticks
mpl.rcParams['ytick.color'] = GRAY2             # Gray xticks
mpl.rcParams['ytick.labelleft'] = False         # Remove y-axis tick lables
mpl.rcParams['ytick.major.left'] = False        # Remove y-axis ticks
mpl.rcParams['text.color'] = GRAY2              # Text
mpl.rcParams['font.family'] = 'Arial'           # Font

ix = ['2008',	'2009', '2010', '2011', '2012']
all = [41.4, 40.0, 38.0, 37.0, 36.7]
lsth = [26.8, 25.0, 23.0, 23.2, 23.4]
hsg = [35.9, 34.0, 31.0, 30.5, 30.1]
sc = [42.5, 41.0, 37.0, 36.7, 36.5]
bdm = [61.5, 61.0, 59.0, 55.0, 56.7]

data = pd.DataFrame({
    'All': all,
    'Less than high school': lsth,
    'High school graduate': hsg,
    'Some college': sc,
    "Bachelor's degree or more": bdm,
    }, index=ix)


fig, ax = plt.subplots(figsize=(3, 4))

ax1 = ax.plot(data.index, data['Less than high school'], color=GRAY9, lw=3,  markevery=[0, 4], markersize=6, marker='o')
ax2 = ax.plot(data.index, data['High school graduate'], color=GRAY9, lw=3,  markevery=[0, 4], markersize=6, marker='o')
ax3 = ax.plot(data.index, data['Some college'], color=GRAY9, lw=3,  markevery=[0, 4], markersize=6, marker='o')
ax4 = ax.plot(data.index, data["Bachelor's degree or more"], color=ORANGE1, lw=3,  markevery=[0, 4], markersize=6, marker='o')

# Annotations
X_OFFSET, Y_OFFSET = -0.7, -1
for ix, axis in enumerate([ax1, ax2, ax3, ax4]):
    if ix==3:
        ax.text(0+X_OFFSET, axis[0].get_ydata()[0]+Y_OFFSET, f"{axis[0].get_ydata()[0]: .0f}", fontsize=12, fontweight='bold', color=ORANGE1)
        ax.text(3-X_OFFSET*1.7, axis[0].get_ydata()[4]+Y_OFFSET, f"{axis[0].get_ydata()[4]: .0f}", fontsize=12, fontweight='bold', color=ORANGE1)
    else:
        ax.text(0+X_OFFSET, axis[0].get_ydata()[0]+Y_OFFSET, f"{axis[0].get_ydata()[0]: .0f}", fontsize=12, color=GRAY9)
        ax.text(3-X_OFFSET*1.7, axis[0].get_ydata()[4]+Y_OFFSET, f"{axis[0].get_ydata()[4]: .0f}", fontsize=12, color=GRAY9)

ax.text(0-4, ax1[0].get_ydata()[0]+Y_OFFSET, f"Less than high school", fontsize=12, color=GRAY9)
ax.text(0-3.3, ax2[0].get_ydata()[0]+Y_OFFSET, f"High school grad", fontsize=12, color=GRAY9)
ax.text(0-2.8, ax3[0].get_ydata()[0]+Y_OFFSET, f"Some college", fontsize=12, color=GRAY9)
ax.text(0-4.65, ax4[0].get_ydata()[0]+Y_OFFSET, f"Bachelor's degree or more", fontsize=12, color=ORANGE1)

ax.text(0-4.65, 85, f"New marriage rate by education", fontsize=16, fontweight='semibold', color=GRAY5)
ax.text(0-4.65, 80, f"Number of newly merried adults pr 1,000 marriage eligible adults", fontsize=12, color=GRAY5)

ax.set_ylim(0, 70)
ax.set_xlim(-.25, 4.25)
 
plt.savefig('plots/slopegraph_1.png', bbox_inches="tight")
plt.show()


