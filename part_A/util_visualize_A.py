import matplotlib.pyplot as plt
from string import ascii_uppercase



def ShowStationLocation(xN, yN, xS, yS, X=[], Y=[], value=None, title=None, ):

    ax = plt.gca()
    [
        ax.plot([xN[i], xS[j]], [yN[i], yS[j]], "g-")
        for j in range(len(X))
        if X[j]
        for i in range(len(Y))
        if Y[i][j]
    ]

    ax.plot([],[], 'g-', label='Connections')   # dummy to hold label

    ax.plot(xN, yN, "s", markersize=10, label='Neighbourhoods')
    ax.plot(xS, yS, "o", label='Possible station location')
    if title:
        ax.set_title(title)
    elif value:
        ax.set_title(f"Optimal value: ${value:,.2f}")


    # This part is case specific and not generally reusable
    # Makes x axes in A to J coordinates
  
    
    letters = ['O'] + list(ascii_uppercase)
    tick_positions = range(11)
    tick_labels = [letters[i] for i in tick_positions]

    ax.set_xticks(tick_positions)
    ax.set_xticklabels(tick_labels)


    ax.legend()

    plt.show()