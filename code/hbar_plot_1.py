import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.ticker as ticker

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
# mpl.rcParams['axes.spines.top'] = False         # Remove top spine
mpl.rcParams['axes.spines.bottom'] = False      # Remove bottom spine
mpl.rcParams['axes.spines.right'] = False       # Remove right spine
mpl.rcParams['axes.spines.left'] = False        # Remove left spine
mpl.rcParams['axes.edgecolor'] = GRAY2          # Gray edge collors
mpl.rcParams['xtick.color'] = GRAY2             # Gray xticks
mpl.rcParams['ytick.color'] = GRAY2             # Gray yticks
mpl.rcParams['ytick.left'] = False              # Remove y-axis ticks
mpl.rcParams['text.color'] = GRAY2              # Text
mpl.rcParams['font.family'] = 'Arial'           # Font

# Data
a = [0.05, 0.05, 0.30, 0.27, 0.33]
b = [0.06, 0.11, 0.35, 0.28, 0.2]
c = [0.06, 0.14, 0.45, 0.15, 0.2]
d = [0.08, 0.32, 0.2, 0.23, 0.17]
e = [0.16, 0.25, 0.32, 0.18, 0.09]
index = ['Survey item A', 'Survey item B', 'Suvey item C', 'Survey item D', 'Survey item E']
columns = ['Strongly Disagree', 'Disagree', 'Neutral', 'Agree', 'Strongly agree']

data = pd.DataFrame([a, b, c, d, e], index=index, columns=columns)
data = data.loc[data.index[::-1], :] # reversing column order

# Plot
fig, ax = plt.subplots()
height = 0.5

left = pd.Series([0, 0, 0, 0, 0], index=data.index)
for col in data.columns:
    if col in columns[0:2]:
        ax.barh(data.index, data[col], height=height, left=left, color=GRAY4)
    elif col in [columns[2]]:
        ax.barh(data.index, data[col], height=height, left=left, color=GRAY8)
    else: 
        ax.barh(data.index, data[col], height=height, left=left, color=BLUE1)
    left = left + data[col] + 0.002 # Small increment to add white space

ax.xaxis.set_ticks_position('top')      # Moving x-axis labels to the top
ax.set_xlim(0, 1)                       # x b/w 0 & 1
ax.xaxis.set_major_formatter(ticker.PercentFormatter(xmax=1))     # Percent formatter

# Title
ax.text(-0.19, 6,  'Survey results', fontsize=14, color=GRAY2)

# Legend
ax.text(-0.02, 5.5,  columns[0], fontsize=10, color=GRAY4, weight='bold'); ax.text(0.22, 5.5,  ' | ', fontsize=10, color=GRAY2)
ax.text(0.25, 5.5,  columns[1], fontsize=10, color=GRAY4, weight='bold'); ax.text(0.37, 5.5,  ' | ', fontsize=10, color=GRAY2)
ax.text(0.4, 5.5,  columns[2], fontsize=10, color=GRAY8, weight='bold'); ax.text(0.5, 5.5,  ' | ', fontsize=10, color=GRAY2)
ax.text(0.53, 5.5,  columns[3], fontsize=10, color=BLUE1, weight='bold'); ax.text(0.61, 5.5,  ' | ', fontsize=10, color=GRAY2)
ax.text(0.64, 5.5,  columns[4], fontsize=10, color=BLUE1, weight='bold')

ax.text(-0.02, 5.05,  'Percent of total', fontsize=10, color=GRAY2)

plt.savefig('plots/hbar_plot_1.png', bbox_inches="tight")
plt.show()