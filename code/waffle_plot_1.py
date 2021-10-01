import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from pywaffle import Waffle

GRAY1, GRAY2, GRAY3 = '#231F20', '#414040', '#555655'
GRAY4, GRAY5, GRAY6 = '#646369', '#76787B', '#828282'
GRAY7, GRAY8, GRAY9 = '#929497', '#A6A6A5', '#BFBEBE'
BLUE1, BLUE2, BLUE3, BLUE4 = '#174A7E', '#4A81BF', '#94B2D7', '#94AFC5'
RED1, RED2 = '#C3514E', '#E6BAB7'
GREEN1, GREEN2 = '#0C8040', '#9ABB59'
ORANGE1 = '#F79747'

mpl.rcParams['font.family'] = 'Arial'           # Font

fig = plt.figure(
    FigureClass=Waffle,
    rows=10,
    columns=10,  # Either rows or columns could be omitted
    values=[1]*100,
    colors=[
        GRAY9, GRAY9, GRAY9, GRAY9, GRAY9, GRAY9, GRAY9, GRAY9, GRAY9, GRAY9,
        GRAY9, GRAY9, GRAY9, GRAY9, GRAY9, GRAY9, GRAY9, GRAY9, GRAY9, GRAY9,
        GRAY9, GRAY9, GRAY9, GRAY9, GRAY9, GRAY9, GRAY9, GRAY9, GRAY9, GRAY9,
        GRAY9, GRAY9, GRAY9, GRAY9, GRAY9, GRAY9, GRAY9, GRAY9, GRAY9, GRAY9,
        GRAY9, GRAY9, GRAY9, GRAY9, GRAY9, GRAY9, GRAY9, GRAY9, GRAY9, GRAY9,
        GRAY7, GRAY7, GRAY7, GRAY7, GRAY7, GRAY9, GRAY9, GRAY9, GRAY9, GRAY9,
        GRAY7, GRAY7, GRAY7, GRAY7, GRAY7, GRAY9, GRAY9, GRAY9, GRAY9, GRAY9,
        BLUE2, BLUE2, BLUE2, GRAY7, GRAY7, GRAY9, GRAY9, GRAY9, GRAY9, GRAY9,
        BLUE2, BLUE2, BLUE2, GRAY7, GRAY7, GRAY9, GRAY9, GRAY9, GRAY9, GRAY9,
        BLUE2, BLUE2, BLUE2, GRAY7, GRAY7, GRAY9, GRAY9, GRAY9, GRAY9, GRAY9
    ],
    interval_ratio_x=0.1,
    interval_ratio_y=0.1
)

txt1 = "Out of every " + r"$\bf{" + str(100) +"}$\n" + r"$\bf{phone\ screens}$"
txt2 = "We bring " + r"$\bf{" + str(25) +"}$\n" + r"$\bf{candidates\ on\ site}$" + "\nfor interviews"
txt3 = "and\n" + r"$\bf{extend\ 9\ offers.}$"
fig.text(x=0.75, y=0.91, s=txt1, ha="left", va="center", fontsize=13, color=GRAY8)
fig.text(x=0.75, y=0.42, s=txt2, ha="left", va="center", fontsize=13, color=GRAY8)
fig.text(x=0.75, y=0.15, s=txt3, ha="left", va="center", fontsize=13, color=BLUE2)

plt.savefig('plots/waffle_plot_1.png', bbox_inches="tight")
plt.show()
