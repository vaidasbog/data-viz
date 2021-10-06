
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
WHITE1 = '#FFFFFF'

# Setting the stage
mpl.rcParams['figure.figsize'] = 6.5, 4         # figure size
mpl.rcParams['figure.dpi'] = 100                # dots per inch, magnifying effect
mpl.rcParams['axes.spines.top'] = False         # Remove top spine
mpl.rcParams['axes.spines.right'] = False       # Remove right spine
mpl.rcParams['axes.spines.left'] = False        # Remove left spine
mpl.rcParams['axes.edgecolor'] = GRAY5          # Gray edge collors
mpl.rcParams['xtick.color'] = GRAY5             # Gray xticks
mpl.rcParams['ytick.color'] = GRAY5             # Gray yticks
mpl.rcParams['ytick.left'] = False              # Remove y-axis ticks
mpl.rcParams['ytick.labelleft'] = False         # Remove y-axis tick lables
mpl.rcParams['ytick.major.left'] = False        # Remove y-axis ticks
mpl.rcParams['text.color'] = GRAY5              # Text
mpl.rcParams['font.family'] = 'Arial'           # Font

# Data
OFFSET = 3e5
quarter = pd.date_range("2013-01-01", "2015-01-01", freq="Q")
revenues = [563000, 498000, 682000, 875000, 634000, 618000, 813000, 956000]
employees = [82, 91, 105, 112, 111, 109, 110, 110]
data = pd.DataFrame({'revenues': revenues, 'employees': employees}, index = quarter)
data = data.assign(emp_change = lambda df: (df['employees'])/df['employees'].shift(1) - 1)

# Making rev_proxy which we can use for employees
emp_proxy = [np.nan]*data.shape[0]
for ix, (r, c) in enumerate(zip(emp_proxy, data['emp_change'])):
    if ix == 0:
        emp_proxy[ix] = data['revenues'][ix] + OFFSET
    else:
        emp_proxy[ix] = emp_proxy[ix-1]*(1+c)
data['emp_proxy'] = emp_proxy
data

fig, ax = plt.subplots(figsize=(5.5, 4.5))

# Bar plot
width = 0.7
ax1 = ax.bar(range(len(quarter)), data['revenues'], width=width, color=BLUE2)
ax.bar_label(ax1, labels=['${:.1f}'.format(r/1e6) for r in data['revenues']], padding=-15, color=WHITE1)

# Line plot
ax2 = ax.plot(range(len(quarter)), data['emp_proxy'], marker='o', lw=2, color=BLUE1)
MRK_OFFSET = 0.7e5
for x in range(len(quarter)):
    ax.text(x-0.13, data['emp_proxy'][x]+MRK_OFFSET,  data['employees'][x], fontsize=10, color=BLUE1)


# Major locator
MJR_OFFSET = width/4
positions_mjr = [0-(width/2)-MJR_OFFSET, 4-(width/2)-MJR_OFFSET, 8-(width/2)-MJR_OFFSET]
ax.xaxis.set_major_locator(ticker.FixedLocator(positions_mjr))
ax.xaxis.set_major_formatter(ticker.NullFormatter())
for tick in ax.xaxis.get_major_ticks():
    tick.tick1line.set_markersize(30)

# Minor locator
MNR_OFFSET = MJR_OFFSET
positions_mnr = [i-(width/2)-MNR_OFFSET for i in range(0, 9) if i%4 != 0]
ax.xaxis.set_minor_locator(ticker.FixedLocator(positions_mnr))
for tick in ax.xaxis.get_minor_ticks():
    tick.tick2line.set_markersize(30)

# Quarters
tick_labels = ('Q' + quarter.quarter.astype(str)).tolist()
for ix, q in enumerate(tick_labels):
    ax.text(ix-MJR_OFFSET, -1e5, q, fontsize=10, color=GRAY5) 

# Years
ax.text(1.5 - 0.25, -2.1e5, '2015', fontsize=10, color=GRAY5) 
ax.text(5.5 - 0.25, -2.1e5, '2016', fontsize=10, color=GRAY5) 

ax.set_ylim(0, 1.5e6)
ax.set_xlim(0-(width/2)-MJR_OFFSET, 8-(width/2)-MJR_OFFSET)

# Anotations
ax.text(-0.5, 6e5, 'Revenue\n(millions)', fontsize=10, color=BLUE2) 
ax.text(-0.5, 11e5, '# of Sales\nEmployees', fontsize=10, color=BLUE1) 

plt.savefig('plots/bar_and_line_overlay_plot.png', bbox_inches="tight")
plt.show()


# %%
""" Alternative with not so fancy xticks
fig, ax = plt.subplots(figsize=(5.5, 4.5))

# Bar plot
width = 0.7
ax1 = ax.bar(range(len(quarter)), data['revenues'], width=width, color=BLUE2)
ax.bar_label(ax1, labels=['${:.1f}'.format(r/1e6) for r in data['revenues']], padding=-15, color=WHITE1)

# Line plot
ax2 = ax.plot(range(len(quarter)), data['emp_proxy'], marker='o', lw=2, color=BLUE1)
MRK_OFFSET = 0.7e5
for x in range(len(quarter)):
    ax.text(x-0.13, data['emp_proxy'][x]+MRK_OFFSET,  data['employees'][x], fontsize=10, color=BLUE1)

ax.set_ylim(0, 1.5e6)

positions_mjr = [1.5, 5.5]
ax.xaxis.set_major_locator(ticker.FixedLocator(positions_mjr))
[tick.tick1line.set_markersize(0) for tick in ax.xaxis.get_major_ticks()]
ax.set_xticklabels(['\n2015', '\n2016'], minor=False)

positions_mnr = range(8)
ax.xaxis.set_minor_locator(ticker.FixedLocator(positions_mnr))
[tick.tick1line.set_markersize(0) for tick in ax.xaxis.get_minor_ticks()]
ax.set_xticklabels(('Q' + quarter.quarter.astype(str)).tolist(), minor=True)

# Anotations
ax.text(-0.5, 6e5, 'Revenue\n(millions)', fontsize=10, color=BLUE2) 
ax.text(-0.5, 11e5, '# of Sales\nEmployees', fontsize=10, color=BLUE1) 
"""


