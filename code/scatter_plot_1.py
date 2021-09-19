import pandas
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import ticker

# Setting the stage
mpl.rcParams['figure.figsize'] = 6.5, 4         # figure size
# dots per inch, magnifying effect
mpl.rcParams['figure.dpi'] = 100
mpl.rcParams['axes.spines.top'] = False         # Remove top spine
mpl.rcParams['axes.spines.right'] = False       # Remove right spine
mpl.rcParams['axes.edgecolor'] = '#414040'      # Gray edge collors
mpl.rcParams['xtick.color'] = '#414040'         # Gray yticks
mpl.rcParams['ytick.color'] = '#414040'         # Gray xticks
mpl.rcParams['text.color'] = '#414040'          # Text
mpl.rcParams['font.family'] = 'Arial'           # Font

# Data
x = np.array([1100,	1177,	1239,	1294,	1378,	1481,	1540,	1712,	1650,	1817,	1971,	1984,	2135,	2211,	2225,	2200,	2256,
             2311,	2180,	2463,	2465,	1850,	2581,	2618,	2627,	2750,	2837,	3061,	3111,	3001,	3201,	3395,	3456,	3498,	3564,	3757])
y = np.array([2.4,	2.8,	2.2,	2.5,	1.9,	2,	2.2,	1.35,	2,	1.3,	1.2,	1.1,	1.35,	1.3,	1.3,	1.2,	1.1,
             1.2,	1.2,	1.4,	1.2,	1.2,	1.1,	0.8,	1.1,	1,	1.32,	1.25,	1.12,	1,	1.34,	1.65,	2.2,	1.8,	1.9,	1.7])

# Colors
GRAY1, GRAY2, GRAY3 = '#231F20', '#414040', '#555655'
GRAY4, GRAY5, GRAY6 = '#646369', '#76787B', '#828282'
GRAY7, GRAY8, GRAY9 = '#929497', '#A6A6A5', '#BFBEBE'
BLUE1, BLUE2, BLUE3, BLUE4 = '#174A7E', '#4A81BF', '#94B2D7', '#94AFC5'
RED1, RED2 = '#C3514E', '#E6BAB7'
GREEN1, GREEN2 = '#0C8040', '#9ABB59'
ORANGE1 = '#F79747'

fig, ax = plt.subplots()

colors = [GRAY9 if y_val < y.mean() else ORANGE1 for y_val in y]

ax.scatter(x, y, c=colors)                          # main scatter plot
ax.scatter(x.mean(), y.mean(), c=GRAY4, s=70)   # average point

ax.hlines(y.mean(), 0, x.mean()*0.82, ls='dashed', lw=1.5, color=GRAY4)
ax.hlines(y.mean(), x.mean()*1.05, 4000, ls='dashed', lw=1.5, color=GRAY4)

ax.text(x.mean()*0.85, y.mean()*0.97, 'AVG', fontsize=10, color=GRAY4)

ax.set_ylim(0, 3)
ax.set_xlim(0, 4000)

ax.set_xticks([0, 1000, 2000, 3000, 4000])

ax.yaxis.set_major_formatter(ticker.StrMethodFormatter("${x:.2f}"))
ax.xaxis.set_major_formatter(ticker.StrMethodFormatter("{x:,}"))

ax.text(0, -0.5, 'Miles drive per month', fontsize=10, color=GRAY4)
ax.text(-550, 2.3, 'Cost per mile', fontsize=10,
        color=GRAY4, rotation='vertical')
ax.text(-550, 3.3, 'Cost per mile by miles driven', fontsize=14, color=GRAY2)

plt.savefig('data-viz/plots/scatter_plot_1.png', bbox_inches="tight")
plt.show()
