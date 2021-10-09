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
mpl.rcParams['axes.edgecolor'] = GRAY2          # Gray edge collors
mpl.rcParams['xtick.color'] = GRAY2             # Gray yticks
mpl.rcParams['ytick.color'] = GRAY2             # Gray xticks
mpl.rcParams['text.color'] = GRAY2              # Text
mpl.rcParams['font.family'] = 'Arial'           # Font

dates = pd.date_range('2014-01-01', '2014-12-31', freq='MS').strftime('%b')
received = [160, 184, 241, 149, 180, 161, 132, 202, 160, 139, 149, 177]
processed = [160, 184, 237, 148, 181, 150, 123, 156, 126, 104, 124, 140]

fig, ax = plt.subplots()

ax1 = ax.plot(dates, received, color=GRAY7, lw=3, marker='o', markevery=list(range(7, 12)))
ax2 = ax.plot(dates, processed, color=BLUE1, lw=3, marker='o', markevery=list(range(7, 12)))
ax3 = ax.plot([4, 4], [0, 250], color = GRAY7)

X_OFFSET, Y_OFFSET = -0.4, 15
for i in range(7, 12):
    ax.text(i+X_OFFSET, ax1[0].get_ydata()[i]+Y_OFFSET, f"{ax1[0].get_ydata()[i]: .0f}", fontsize=11, fontweight='normal', color=GRAY7)
    ax.text(i+X_OFFSET, ax2[0].get_ydata()[i]-Y_OFFSET*1.8, f"{ax2[0].get_ydata()[i]: .0f}", fontsize=11, fontweight='normal', color=BLUE1)
    if i == 11:
        ax.text(i + 0.5, ax1[0].get_ydata()[i], f"Received", fontsize=15, fontweight='normal', color=GRAY7)
        ax.text(i + 0.5, ax2[0].get_ydata()[i], f"Processed", fontsize=15, fontweight='normal', color=BLUE1)

ax.set_ylim(0, 300)
ax.set_xlim(0, 12)

ax.text(-1.3, 420, f"Please approve the hire of 2 FTEs", fontsize=20, fontweight='bold', color=GRAY5)
ax.text(-1.3, 395, f"to backfill those who quit in the past year", fontsize=12, fontweight='normal', color=GRAY5)
ax.text(-1.3, 340, f"Ticket volume over time", fontsize=16, fontweight='normal', color=GRAY5)
ax.text(-0.25, -45, f"2014", fontsize=10, fontweight='normal', color=GRAY3)
ax.text(-1.3, 200, f"Number of tickets", fontsize=10, fontweight='normal', color=GRAY3, rotation='vertical')

ax.text(-0.25, -45, f"2014", fontsize=10, fontweight='normal', color=GRAY3)

caption = (f"Data source: XYZ Dashboard, as of 13/31/2014 | A detailed analysis on tickets processed per person\n" + 
f"and time to resolve issues was undertaken to inform this request and can be provided if needed.")
ax.text(-1.3, -85, caption, fontsize=10, fontweight='normal', color=GRAY3)

explanation = (r"$\bf{2\ employees\ quit\ in\ May.}$" + "We nearly kept up with incoming\n"
+ f"volume in the following two months, but fell behind with the\n"
+ f"increase in Aug and havent been able to catch up since");
ax.text(4, 260, explanation, fontsize=10, fontweight='normal', color=GRAY5)

plt.savefig('plots/line_plot_2.png', bbox_inches="tight")
plt.show()


