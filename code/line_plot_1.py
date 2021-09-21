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

# Data
min = [9, 6, 7, 12, 12, 7, 7, 9, 8, 12, 13, 17, 14]
avg = [18, 12, 13, 18, 17, 13, 12, 14, 13, 18, 19, 24, 21]
max = [27, 17, 17, 26, 24, 20, 18, 21, 21, 28, 26, 36, 32]
date = pd.date_range(start='2014-09-01', end='2015-09-01',
                     freq='MS') + pd.Timedelta(14, unit='d')  # 15th of the month
data = pd.DataFrame({'date': date, 'min': min, 'avg': avg, 'max': max})

fig, ax = plt.subplots()

# Plots
ax.plot(data.date, data.avg, marker='o',
        markevery=[12], markersize=7, color=GRAY2)
ax.fill_between(data.date, data['min'], data['max'], alpha=0.2, color=GRAY7)

# Anotations
ax.text(data.date.min(), data['max'][0], 'MAX', fontsize=10, color=GRAY4)
ax.text(data.date.min(), data['min'][0], 'MIN', fontsize=10, color=GRAY4)
ax.text(data.date.min(), data['avg'][0] + 0.5, 'AVG',
        fontsize=10, fontweight='bold', color=GRAY1)
ax.text(data.date.max() + pd.Timedelta(10, unit='d'),
        data['avg'].iloc[-1]-0.5, str(data['avg'].iloc[-1]), fontsize=10, color=GRAY1)

# Axis labels
ax.text(data.date.min() - pd.Timedelta(60, unit='d'), 25.5,
        'Wait time (minutes)', fontsize=10, color=GRAY4, rotation='vertical')

# Title
ax.text(data.date.min() - pd.Timedelta(60, unit='d'), 47,
        'Passport control wait time', fontsize=14, color=GRAY2)
ax.text(data.date.min() - pd.Timedelta(60, unit='d'),
        44, 'Past 13 months', fontsize=10, color=GRAY4)

# Formatting date axis
# More here: https://matplotlib.org/stable/gallery/ticks_and_spines/centered_ticklabels.html#sphx-glr-gallery-ticks-and-spines-centered-ticklabels-py
ax.xaxis.set_major_locator(dates.MonthLocator())                # set locator
# removing dates from major ticks
ax.xaxis.set_major_formatter(ticker.NullFormatter())
# set minor locator on every 15th
ax.xaxis.set_minor_locator(dates.MonthLocator(bymonthday=16))
ax.xaxis.set_minor_formatter(dates.DateFormatter(
    '%b'))         # formatting to month

for tick in ax.xaxis.get_minor_ticks():
    tick.tick1line.set_markersize(0)
    tick.label1.set_horizontalalignment('center')

for ix, tick in enumerate(ax.xaxis.get_major_ticks()):
    if (ix == 0) | (ix == 4) | (ix == 13):
        tick.tick1line.set_markersize(30)
ax.text(data.date[1] + pd.Timedelta(5, unit='d'), -
        5, '2014', fontsize=10, color=GRAY3) 
ax.text(data.date[7] + pd.Timedelta(5, unit='d'), -
        5, '2015', fontsize=10, color=GRAY3)

ax.set_ylim(0, 40)
ax.set_xlim(data.date.min() - pd.Timedelta(14, unit='d'),
            data.date.max() + pd.Timedelta(16, unit='d'))

plt.savefig('plots/line_plot_1.png', bbox_inches="tight")
plt.show()
