import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

print("""
.__   __.   ______     ______ .___________.     ___      ___   ___    .______    _______   __      
|  \ |  |  /  __  \   /      ||           |    /   \     \  \ /  /    |   _  \  |       \ |  |     
|   \|  | |  |  |  | |  ,----'`---|  |----`   /  ^  \     \  V  /     |  |_)  | |  .--.  ||  |     
|  . `  | |  |  |  | |  |         |  |       /  /_\  \     >   <      |   ___/  |  |  |  ||  |     
|  |\   | |  `--'  | |  `----.    |  |      /  _____  \   /  .  \     |  |      |  '--'  ||  `----.
|__| \__|  \______/   \______|    |__|     /__/     \__\ /__/ \__\    | _|      |_______/ |_______|  ©                                                                                                                                                                           
""")

# Loading data :
DataFrame = df = pd.read_excel("Data_Input/Data_PDL.xlsx")
print("lists of PDL :")
print(df["Code"].drop_duplicates(inplace=False))
PDL: str = input("-->")

# set variables :
font1 = {'family': 'arial', 'color': 'Black', 'size': 14}
font2 = {'family': 'arial', 'color': 'Black', 'size': 10}
Y = df.loc[df['Code'] == PDL]['Profondeur (m)']
X = df.loc[df['Code'] == PDL]['Résistance de pointe (bars)']
x_max = df['Résistance de pointe (bars)'].max()
y_max = df['Profondeur (m)'].max()


# round up function for X and Y axis
def round_up_y(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier


def round_up_x(n):
    return int(math.ceil(n / 100.0)) * 100


x_max = round_up_x(int(x_max))
y_max = round_up_y(y_max)


# Single_plotting function
def plot():
    plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = False
    plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = True
    plt.plot(X, Y, color='r', label=PDL)
    plt.title("Essai au pénétromètre dynamique : " + PDL, fontdict=font1, pad=20)
    plt.xlabel("Résistance dynamique de pointe (Bars)", fontdict=font2)
    plt.ylabel("Profondeur (m) ", fontdict=font2)
    ax = plt.gca()

    # make arrows
    ax.plot((1), (0), ls="", marker=">", ms=10, color="k",
            transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot((0), (0), ls="", marker="v", ms=10, color="k",
            transform=ax.get_xaxis_transform(), clip_on=False)

    # set axes limits
    plt.xlim(0, x_max)
    plt.ylim(0, y_max)
    ax.xaxis.set_label_position('top')
    ax.xaxis.set_ticks(np.arange(0, x_max, 50))
    ax.yaxis.set_ticks(np.arange(0, y_max, 0.5))
    plt.xlim()
    plt.ylim()

    # plotting
    plt.gca().invert_yaxis()
    plt.grid(visible=True, which='major', color='black', linestyle='-', linewidth=0.2)
    plt.grid(visible=True, which='minor', color='gray', linestyle='-', alpha=0.2, linewidth=0.2)
    plt.minorticks_on()

    # Figure set_up :
    figure = plt.gcf()
    cm = 1 / 2.54
    figure.size = (20 * cm, 10 * cm)
    figure.tight_layout(pad=2.0)
    figure.set_size_inches(8.27, 11.69)
    plt.tight_layout(pad=3)
    plt.legend(bbox_to_anchor=(0, 0.01, 1, 0), loc="lower left", ncol=1)
    plt.savefig("Data_Output/Courbes des résistances de pointe du " + PDL + ".pdf", format='pdf', dpi=120)
    # plt.show()


# Multi_plotting function All in one !
def plot_all():
    plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = False
    plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = True

    for (Code, data) in df.groupby('Code'):
        plt.plot(data['Résistance de pointe (bars)'], data['Profondeur (m)'], label=Code)

    plt.title("Essai au pénétromètre dynamique ", fontdict=font1, pad=20)
    plt.xlabel("Résistance dynamique de pointe (Bars)", fontdict=font2)
    plt.ylabel("Profondeur (m) ", fontdict=font2)

    ax = plt.gca()
    # make arrows
    ax.plot((1), (0), ls="", marker=">", ms=10, color="k",
            transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot((0), (0), ls="", marker="v", ms=10, color="k",
            transform=ax.get_xaxis_transform(), clip_on=False)

    ax.xaxis.set_label_position('top')
    plt.margins(0)
    plt.xlim(0, x_max)
    plt.ylim(0, y_max)
    ax.xaxis.set_ticks(np.arange(0, x_max, 50))
    ax.yaxis.set_ticks(np.arange(0, y_max, 0.5))

    plt.gca().invert_yaxis()
    plt.grid(visible=True, which='major', color='black', linestyle='-', linewidth=0.2)
    plt.grid(visible=True, which='minor', color='gray', linestyle='-', alpha=0.2, linewidth=0.2)
    plt.minorticks_on()

    plt.legend(bbox_to_anchor=(0, 0.01, 1, 0), loc="lower center", mode="expand", ncol=5)
    figure = plt.gcf()
    cm = 1 / 2.54
    figure.size = (20 * cm, 10 * cm)
    figure.tight_layout(pad=2.0)
    figure.set_size_inches(8.27, 11.69)
    plt.tight_layout(pad=3)
    plt.savefig("Data_Output/Courbes des résistances de pointe PDL all in one.pdf", format='pdf', dpi=120)


# Conditions :
if PDL in df["Code"].values:
    plot()

elif PDL in ["ALL", "All", "all"]:
    plot_all()

elif PDL in ['EXIT', 'Exit', 'exit', 'QUIT', 'Quit', 'quit']:
    print("Goodbye!")

else:
    print("Réessayer!")
    PDL = input("-->")
