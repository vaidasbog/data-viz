import pandas
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import ticker

# Colors
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
mpl.rcParams['axes.spines.left'] = False        # Remove left spine
mpl.rcParams['axes.edgecolor'] = GRAY2          # Gray edge collors
mpl.rcParams['axes.linewidth'] = 0.4            # Axis line width
mpl.rcParams['xtick.color'] = GRAY2             # Gray yticks
mpl.rcParams['ytick.color'] = GRAY2             # Gray xticks
mpl.rcParams['ytick.labelleft'] = False         # Remove y-axis tick lables
mpl.rcParams['ytick.major.left'] = False        # Remove y-axis ticks
mpl.rcParams['text.color'] = GRAY2              # Text
mpl.rcParams['font.family'] = 'Arial'           # Font

# Data
begining = 100
hires = 30
transfers_in = 8
transfers_out = -12
exits = -10
ending = 116

# Plot
fig, ax = plt.subplots()

# Bar plots
width = 0.5
bar_1 = ax.bar(1, begining, width=width, color=BLUE2)
bar_2 = ax.bar(2, hires, bottom=begining, width=width, color=BLUE2)
bar_3 = ax.bar(3, transfers_in, bottom=begining+hires, width=width, color=BLUE2)
bar_4 = ax.bar(4, transfers_out, bottom=begining+hires+transfers_in, width=width, color=BLUE2)
bar_5 = ax.bar(5, exits, bottom=begining+hires+transfers_in+transfers_out, width=width, color=BLUE2)
bar_6 = ax.bar(6, ending, width=width, color=BLUE2)

# Vertical lines
ax.hlines(begining, 1-width/2, 2+width/2, colors=GRAY6, linestyles="--", linewidth=0.7)
ax.hlines(begining+hires, 2-width/2, 3+width/2, colors=GRAY6, linestyles="--", linewidth=0.7)
ax.hlines(begining+hires+transfers_in, 3-width/2, 4+width/2, colors=GRAY6, linestyles="--", linewidth=0.7)
ax.hlines(begining+hires+transfers_in+transfers_out, 4-width/2, 5+width/2, colors=GRAY6, linestyles="--", linewidth=0.7)
ax.hlines(begining+hires+transfers_in+transfers_out+exits, 5-width/2, 6+width/2, colors=GRAY6, linestyles="--", linewidth=0.7)

# Bar labls
ax.bar_label(bar_1, labels = [str(begining)], color=WHITE1, padding=-12, fontsize=9.5)
ax.bar_label(bar_2, labels = ["+"+str(hires)], color=WHITE1, padding=-12, fontsize=9.5)
ax.bar_label(bar_3, labels = ["+"+str(transfers_in)], color=WHITE1, padding=-11, fontsize=9.5)
ax.bar_label(bar_4, labels = ["-"+str(transfers_out)], color=WHITE1, padding=-15, fontsize=9.5)
ax.bar_label(bar_5, labels = ["-"+str(exits)], color=WHITE1, padding=-12, fontsize=9.5)
ax.bar_label(bar_6, labels = [str(ending)], color=WHITE1, padding=-12, fontsize=9.5)

# Title
ax.text(0, 165,  '2014 Headcount math', fontsize=14, color=GRAY2)
sub_title = "Though more employees transfered out of the team than traansfered in,\n"\
+"aggressive hiring means overall headcount (HC) increased 16% over the course of the year."
ax.text(0, 150, sub_title, fontsize=9, color=GRAY4)

ax.set_xlim(0.5, 6.5)

# Setting major x-ticks
major_ticks = [1, 2, 3, 4, 5, 6]                            # Defining major ticks
ax.set_xticks(major_ticks, minor=False)                     # Setting x-ticks
major_labels = ['1/1/2014', 'Hires', 'Transfrs in', 'Transfers out', 'Exits', '12/31/2014']
ax.set_xticklabels(major_labels, minor=False)               # Setting lables
ax.tick_params(axis="x", color=WHITE1, labelsize=9, pad=0.5)# Hiding ticks with white color

# Applying different length
long_ticks = [0.5, 1.5, 3.5, 5.5, 6.5]                  
for t in long_ticks:
    ax.annotate('', xy=(t, 1), xytext=(t, -20), arrowprops=dict(arrowstyle="-", edgecolor=GRAY2, lw=0.4))
small_ticks = [2.5, 4.5]
for t in small_ticks:
    ax.annotate('', xy=(t, 1), xytext=(t, -10), arrowprops=dict(arrowstyle="-", edgecolor=GRAY2, lw=0.4))

# Grouping axis labels
ax.text(0.6, -17, 'Begining HC', fontsize=9, color=GRAY4)
ax.text(2.2, -17, 'Additions', fontsize=9, color=GRAY4)
ax.text(4.2, -17, 'Deductions', fontsize=9, color=GRAY4)
ax.text(5.65, -17, 'Ending HC', fontsize=9, color=GRAY4)

plt.savefig('plots/waterfall_1.png', bbox_inches="tight")
plt.show()
