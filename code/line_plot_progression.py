import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import ticker
import matplotlib.dates as dates
import matplotlib.patches as patches

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
mpl.rcParams['axes.edgecolor'] = GRAY3          # Gray edge collors
mpl.rcParams['xtick.color'] = GRAY3             # Gray yticks
mpl.rcParams['ytick.color'] = GRAY3             # Gray xticks
mpl.rcParams['axes.labelcolor'] = GRAY3         # All axis lable colors
mpl.rcParams['text.color'] = GRAY3              # Text
mpl.rcParams['font.family'] = 'Sans'           # Font

dates = pd.date_range(start='2013-09-01', end='2015-05-01', freq='MS')
users = [5680,	7097,	9247,	10931,	20542,	25842,	28746,	29947,	32369,	30782,	30420,	32642,	33739,	36070,	38401,	39214,	50609,	61553,	82287,	89135,	94260]

def get_canvas():
    fig, ax = plt.subplots(figsize=(8.5, 4))

    ax.set_ylim(0, 100000)
    ax.yaxis.set_major_locator(ticker.MultipleLocator(10000))
    ax.yaxis.set_major_formatter(ticker.StrMethodFormatter("{x:,.0f}"))

    x_offset = 0.5
    ax.set_xlim(0-x_offset, len(dates)+x_offset-1)

    ax.xaxis.set_major_locator(ticker.FixedLocator(list(range(-1, len(dates)))))
    majors = [""] + dates.strftime("%b").tolist()
    ax.xaxis.set_major_formatter(ticker.FixedFormatter(majors))
    [tick.tick1line.set_markersize(0) for tick in ax.xaxis.get_major_ticks()];

    for i in range(len(dates)+1):
        length = 8e3
        if i in [0, 4, 16, 21]: length=14e3
        ax.annotate("", xy=(i-0.49, 500), xytext=(i-0.49,-length), xycoords="data",
                    arrowprops={"arrowstyle":"-", "linestyle":"-", "linewidth":1, "color": GRAY5}, annotation_clip=False)   
    for ix, yr in zip((1, 9, 17.5), (2013, 2014, 2015)):
        ax.text(ix, -14e3, yr, fontsize=9)

    ax.tick_params(axis='both', which='major', labelsize=8)

    # Anotations
    ax.text(-2.8, 110e3, 'Moonville: active users over time', fontsize=14, color=GRAY4)
    ax.text(-2.8, 75e3, 'Active users', rotation='vertical', fontsize=10, color=GRAY4)
    caption = 'Data source: ABC Report. For purpose of analysis "active user" is defined as the number of unique users in past 30 days'
    ax.text(-2.8, -20e3, caption, fontsize=8, color=GRAY4)

    return fig, ax

fig, ax = get_canvas()
ax.scatter(range(0, len(users[0:1])), users[0:1], color=BLUE2, s=40)
plt.savefig('plots/line_plot_progression_1_5.png', bbox_inches="tight")

fig, ax = get_canvas()
ax.plot(range(0, len(users[0:4])), users[0:4], color=BLUE2, lw=2.5, markevery=[0, 3], marker='o', markerfacecolor=WHITE1)
plt.savefig('plots/line_plot_progression_2_5.png', bbox_inches="tight")

fig, ax = get_canvas()
ax.plot(range(0, len(users[0:4])), users[0:4], color=BLUE3, lw=2.5, markevery=[0], marker='o', markerfacecolor=WHITE1)
ax.plot(range(3, len(users[0:7])), users[3:7], color=BLUE2, lw=2.5, markevery=[0, 3], marker='o', markerfacecolor=WHITE1)
plt.savefig('plots/line_plot_progression_3_5.png', bbox_inches="tight")

fig, ax = get_canvas()
ax.plot(range(0, len(users[0:7])), users[0:7], color=BLUE3, lw=2.5, markevery=[0], marker='o', markerfacecolor=WHITE1)
ax.plot(range(6, len(users[0:16])), users[6:16], color=BLUE2, lw=2.5, markevery=[0, 9], marker='o', markerfacecolor=WHITE1)
plt.savefig('plots/line_plot_progression_4_5.png', bbox_inches="tight")

fig, ax = get_canvas()
ax.plot(range(0, len(users[0:16])), users[0:16], color=BLUE3, lw=2.5, markevery=[0], marker='o', markerfacecolor=WHITE1)
ax.plot(range(15, len(users[0:21])), users[15:21], color=BLUE2, lw=2.5, markevery=[0, 5], marker='o', markerfacecolor=WHITE1)
plt.savefig('plots/line_plot_progression_5_5.png', bbox_inches="tight")

fig, ax = get_canvas()

ax.plot(range(0, len(users[0:21])), users[0:21], color=BLUE2, lw=2.5, markevery=[0, 3, 6, 15, 20], marker='o', markerfacecolor=WHITE1)

for ix, offset in zip([0, 3, 6, 15, 20], [-0.2, -1.3, -0.9, -1.3, -1.3]):
    ax.text(ix+offset, users[ix]+5e3, f"{users[ix]:,}", color=BLUE2, fontsize=11)

txt1 = [f"Sep-Dec 2013", f"Jan-Mar 2014", f"Mar-Dec 2014:", f"YTD 2015"]
txt2 = [
    f"Moonville\nlaunched with\n5K active users\nin Sep. Early\nfeedback was\nmixed; still, the\nnumber of\nactive users\nearly doubled\nin the first foud\nmonths.", 
    f"The number of\nactive users\nincreased with\nsteeper\ntrajectory as a\nresult of friends\nand family\npromotions.", 
    f"Growth was marginal\nthrough the rest of 2014 as\nwe halted marketing\nefforts to focus on quality\nimprovements.", 
    f"The revamped game\nplus partnerships\nwith social\nmedia channels\nhave been very\nsuccessful"
    ]

for ix, txt1 in zip([0, 3.5, 8, 14], txt1):
    ax.text(ix+0.2, 100e3, txt1, color=GRAY4, fontsize=8.5, fontweight='bold')

for ix, txt2 in zip([0, 3.5, 8, 14], txt2):
    ax.text(ix+0.2, 98e3, txt2, color=GRAY4, fontsize=8.5, fontweight='normal', va='top', ha='left')

# txt3 = "Given recent\ngrowth rate, we\nanticipate" r"$\bf{we\ will\n surpass\ 100K\ active\n users\ in\ June}$"
txt3 = "Given recent\ngrowth rate, we\nanticipate " + r"$\bf{we\ will}$" + "\n" + r"$\bf{surpass\ 100K\ active}$" + "\n" + r"$\bf{users\ in\ June}$"
ax.text(20.5, 40e3, txt3, ha='right', fontsize=8.5, color=BLUE2, clip_on=False)

plt.savefig('plots/line_plot_progression.png', bbox_inches="tight")
plt.show();