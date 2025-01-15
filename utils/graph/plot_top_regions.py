#plot_top_regions

import matplotlib.pyplot as plt

def plot_top_regions(data, column, top=10):

    top_regions = data.head(top)
    plt.figure(figsize=(10, 6))
    top_regions.plot(kind="bar")
    plt.title(f"{column} pour les {top} premières régions")
    plt.xlabel("Commune")
    plt.ylabel(column)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()
