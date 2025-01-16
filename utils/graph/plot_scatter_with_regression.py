#plot_scatter_with_regression.py

import matplotlib.pyplot as plt

# Fonction pour créer un nuage de points avec régression linéaire
def plot_scatter_with_regression(data, x_col, y_col, title):
    plt.figure(figsize=(8, 6))
    x = data[x_col]
    y = data[y_col]

    # Nuage de points
    plt.scatter(x, y, label="Données", alpha=0.7)

    # Calcul manuel de la régression linéaire
    x_mean = x.mean()
    y_mean = y.mean()
    slope = ((x - x_mean) * (y - y_mean)).sum() / ((x - x_mean) ** 2).sum()
    intercept = y_mean - slope * x_mean

    # Tracer la ligne de régression
    plt.plot(x, slope * x + intercept, color='red', label="Régression linéaire")

    plt.title(title)
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.legend()
    plt.grid(True)
    plt.show()
