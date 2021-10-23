
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
ORANGE1, ORANGE2 = '#F79747', '#FCD5B5'
WHITE1 = '#FFFFFF'

# Setting the stage
mpl.rcParams['figure.figsize'] = 6.5, 4         # figure size
mpl.rcParams['figure.dpi'] = 100                # dots per inch, magnifying effect
mpl.rcParams['axes.spines.top'] = False         # Remove top spine
mpl.rcParams['axes.spines.bottom'] = False      # Remove bottom spine
mpl.rcParams['axes.spines.right'] = False       # Remove right spine
mpl.rcParams['axes.edgecolor'] = WHITE1         # Gray edge collors
mpl.rcParams['xtick.color'] = GRAY4             # Gray xticks
mpl.rcParams['ytick.color'] = GRAY4             # Gray yticks
mpl.rcParams['ytick.left'] = False              # Remove y-axis ticks
mpl.rcParams['xtick.bottom'] = False             # Remove x-axis ticks
plt.rcParams['xtick.labelbottom'] = False       # Remove x-axis ticks
mpl.rcParams['text.color'] = GRAY4              # Text
mpl.rcParams['font.family'] = 'Arial'           # Font


# Data
data = pd.DataFrame({
    'Have not used': [0,	0,	0.02,	0.08,	0.06,	0.14,	0.19,	0.13,	0.22,	0.02,	0.29,	0.29,	0.33,	0.26,	0.51],
    'Not satisfied at all': [0.01,	0.02,	0.02,	0.01,	0.01,	0.01,	0.02,	0.01,	0.02,	0.08,	0.01,	0.01,	0.03,	0.09,	0.01],
    'Not very satisfied': [0.01,	0.02,	0.05,	0.04,	0.06,	0.05,	0.05,	0.06,	0.05,	0.14,	0.04,	0.04,	0.08,	0.14,	0.06],
    'Somewhat satisfied': [0.11,	0.13,	0.24,	0.21,	0.23,	0.2,	0.15,	0.23,	0.17,	0.24,	0.17,	0.23,	0.25,	0.24,	0.15],
    'Very satisfied': [0.4,	0.36,	0.34,	0.37,	0.36,	0.35,	0.26,	0.32,	0.27,	0.27,	0.28,	0.27,	0.18,	0.17,	0.16],
    'Completely satisfied': [0.47,	0.47,	0.33,	0.29,	0.28,	0.25,	0.33,	0.25,	0.27,	0.25,	0.21,	0.16,	0.13,	0.1,	0.11],
    'very + completely': [0.87,	0.83,	0.67,	0.66,	0.64,	0.6,	0.59,	0.57,	0.54,	0.52,	0.49,	0.43,	0.31,	0.27,	0.27]
}, index=['Feature A',	'Feature B',	'Feature C',	'Feature D',	'Feature E',	'Feature F',	'Feature G',	'Feature H',	'Feature I',	'Feature J',	'Feature K',	'Feature L',	'Feature M',	'Feature N',	'Feature O'])

data = data[::-1]


fig, ax = plt.subplots(figsize=(10, 6))

white_space = 0.002
ax1 = ax.barh(data.index, data['Have not used'], color='#cad7e2', edgecolor=WHITE1, label='Have not used')
ax2 = ax.barh(data.index, data['Not satisfied at all'], color=ORANGE2, left=ax1.datavalues+white_space, edgecolor=WHITE1, label='Not satisfied at all')
ax3 = ax.barh(data.index, data['Not very satisfied'], color=ORANGE2, left=ax1.datavalues+ax2.datavalues+white_space*2, edgecolor=WHITE1, label='Not very satisfied')
ax4 = ax.barh(data.index, data['Somewhat satisfied'], color=GRAY9, left=ax1.datavalues+ax2.datavalues+ax3.datavalues+white_space*3, edgecolor=WHITE1, label='Somewhat satisfied')
ax5 = ax.barh(data.index, data['Very satisfied'], color=BLUE3, left=ax1.datavalues+ax2.datavalues+ax3.datavalues+ax4.datavalues+white_space*4, edgecolor=WHITE1, label='Very satisfied')
ax6 = ax.barh(data.index, data['Completely satisfied'], color=BLUE3, left=ax1.datavalues+ax2.datavalues+ax3.datavalues+ax4.datavalues+ax5.datavalues+white_space*5, edgecolor=WHITE1, label='Completely satisfied')

# Custom highlighting
pad = -30
ax1[0].set_color('#5d80a5')
ax1[0].set_edgecolor(WHITE1)
ax.bar_label(ax1, labels=[f"{val: .0%}" if ix == 0 else f"" for ix, val in enumerate(data.iloc[:, 0])], label_type='edge', padding=pad, color=WHITE1);

ax2[1].set_color(ORANGE1), ax2[5].set_color(ORANGE1)
ax2[1].set_edgecolor(WHITE1), ax2[5].set_edgecolor(WHITE1)
ax.bar_label(ax2, labels=[f"{val: .0%}" if ix in [1, 5] else f"" for ix, val in enumerate(data.iloc[:, 1])], label_type='edge', padding=pad, color=WHITE1);

ax3[1].set_color(ORANGE1), ax3[5].set_color(ORANGE1)
ax3[1].set_edgecolor(WHITE1), ax3[5].set_edgecolor(WHITE1)
ax.bar_label(ax3, labels=[f"{val: .0%}" if ix in [1, 5] else f"" for ix, val in enumerate(data.iloc[:, 2])], label_type='edge', padding=pad, color=WHITE1);

ax5[13].set_color(BLUE1), ax5[14].set_color(BLUE1)
ax5[13].set_edgecolor(WHITE1), ax5[14].set_edgecolor(WHITE1)
ax.bar_label(ax5, labels=[f"{val: .0%}" if ix in [13, 14] else f"" for ix, val in enumerate(data.iloc[:, 4])], label_type='edge', padding=pad, color=WHITE1);

ax6[13].set_color(BLUE1), ax6[14].set_color(BLUE1)
ax6[13].set_edgecolor(WHITE1), ax6[14].set_edgecolor(WHITE1)
ax.bar_label(ax6, labels=[f"{val: .0%}" if ix in [13, 14] else f"" for ix, val in enumerate(data.iloc[:, 4])], label_type='edge', padding=pad, color=WHITE1);

# Legend
ax.legend(loc='upper left', bbox_to_anchor=(-0.17, 1.07), ncol=6, frameon=False, handlelength=0.7, handletextpad=0.4, labelcolor=[BLUE3, ORANGE1, ORANGE1, GRAY5, BLUE2, BLUE2])

# Annotations
ax.text(-0.17, 18.5, 'User satisfaction varies greatly by feature' + ' '*90, fontsize=16,backgroundcolor=GRAY7,color=WHITE1)
ax.text(-0.17, 17, 'Product X User Satisfaction: ' r"$\bf{Features}$" , fontsize=14, color=GRAY5)
caption = 'Respones based on survey question: "How satisfied have ypu been with each of these features?\n'+ 'Need more details here to put this data into context; How many people completed survey? What proportion of users does this represent?\n' + 'Do those who complete the survey look like the overall population demographic-wise? When was the survey conducted?'
ax.text(-0.17, -2.5, caption , fontsize=8, color=GRAY6)


ax.text(1.05, 12.5, 'Features A and B\ncontinue to top user\nsatisfaction', fontsize=12, color=WHITE1, backgroundcolor=BLUE1)
ax.text(1.05, 6, 'Users are least\nsatisfied with\nFeatures J and N;\nwhat improvements\ncan we make here\nfor a better user\nexperience?', fontsize=12, color=WHITE1, backgroundcolor=ORANGE1)
ax.text(1.05, 0, 'Feature O is least\nused. What steps\ncan we proactively\ntake with existing\nusers to increase\nutiliztion?', fontsize=12, color=WHITE1, backgroundcolor=BLUE2)

plt.savefig('plots/hbar_plot_3.png', bbox_inches="tight")
plt.show();


