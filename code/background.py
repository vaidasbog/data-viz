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
mpl.rcParams['figure.figsize'] = 5, 3.5         # figure size
# dots per inch, magnifying effect
mpl.rcParams['figure.dpi'] = 100
mpl.rcParams['axes.spines.top'] = False         # Remove top spine
mpl.rcParams['axes.spines.right'] = False       # Remove right spine
mpl.rcParams['axes.edgecolor'] = GRAY5          # Gray edge collors
mpl.rcParams['xtick.color'] = GRAY5             # Gray yticks
mpl.rcParams['ytick.color'] = GRAY5             # Gray xticks
mpl.rcParams['text.color'] = GRAY5              # Text
mpl.rcParams['font.family'] = 'Arial'           # Font

# Data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
data = [4, 2, 3, 4, 4]

def change_background(ax, color_bg=WHITE1, color_elements=GRAY1, title='White background'):
    
    ax_plot = ax.plot(months, data, marker='o', lw=3, markersize=8, color=color_elements)
    ax.set_ylim(0, 5)
    ax.set_facecolor(color_bg)
    fig.patch.set_facecolor(color_bg)

    for tick in ax.xaxis.get_major_ticks():
        tick.tick1line.set_markersize(0)

    ax.spines['bottom'].set_color(color_elements)
    ax.spines['left'].set_color(color_elements)

    [t.set_color(color_elements) for t in ax.xaxis.get_ticklines()]
    [t.set_color(color_elements) for t in ax.xaxis.get_ticklabels()]

    [t.set_color(color_elements) for t in ax.yaxis.get_ticklines()]
    [t.set_color(color_elements) for t in ax.yaxis.get_ticklabels()]

    ax.text(-0.4, 5.7, title, fontsize=14, color=color_elements)

fig, ax = plt.subplots()
change_background(ax=ax, color_bg=WHITE1, color_elements=GRAY2, title='White background')
plt.savefig('plots/background_white.png', bbox_inches="tight")

fig, ax = plt.subplots()
change_background(ax=ax, color_bg=BLUE2, color_elements=WHITE1, title='Blue background')
plt.savefig('plots/background_blue.png', bbox_inches="tight")

fig, ax = plt.subplots()
change_background(ax=ax, color_bg=GRAY1, color_elements=WHITE1, title='Black background')
plt.savefig('plots/background_black.png', bbox_inches="tight")


