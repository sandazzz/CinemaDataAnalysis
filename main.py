import pandas as pd
import matplotlib.pyplot as plt
from utils.filter_columns import filter_csv_columns
from utils.graph.plot_top_regions import plot_top_regions

def calculate_average_entries_per_seat(data, year):
    #Ajoute une colonne pour les entrées moyennes par fauteuil pour une année donnée.
    
    column_name = f"entrées moyennes par fauteuil {year}"
    data[column_name] = data[f"entrées {year}"] / data["fauteuils"]
    return column_name

def group_and_sort_by_region(data, column):
    #Regroupe les données par région et calcule la moyenne pour une colonne donnée.
    #Retourne une série triée par ordre décroissant.
    
    return data.groupby("commune")[column].mean().sort_values(ascending=False)

# Fonction pour filtrer les données pour l'année 2022
def filter_data_for_2022(data):
    return data[data['entrées 2022'].notnull()]

# Fonction pour calculer et afficher la corrélation entre deux colonnes
def calculate_and_display_correlation(data, column1, column2):
    correlation = data[column1].corr(data[column2])
    print(f"Corrélation entre {column1} et {column2} : {correlation:.2f}")
    return correlation

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

def main():
    # Chemin vers le fichier
    cinema_file = "data/cinema.csv"

    # Colonnes utiles
    #Les colonnes sélectionnées ont été choisies pour répondre directement à l'objectif de l'étude, 
    #qui est de déterminer si les infrastructures cinématographiques (nombre d'écrans et fauteuils) 
    #influencent significativement la fréquentation des cinémas. 
    columns = [
        "région administrative",
        "commune",
        "population de la commune",
        "écrans",
        "fauteuils",
        "entrées 2021",
        "entrées 2022",
        "label Art et Essai"
    ]

    # Charger et filtrer les données
    filtered_data = filter_csv_columns(cinema_file, columns, sep=";")

    if filtered_data.empty:
        print("Les données ne contiennent pas les colonnes nécessaires.")
        return

    # Calcul des entrées moyennes par fauteuil en 2022
    average_entries_per_seat = calculate_average_entries_per_seat(filtered_data, 2022)

    # Regrouper par région
    region_stats = group_and_sort_by_region(filtered_data, average_entries_per_seat)

    # Identifier les 3 meilleures et 3 pires régions
    top_3_regions = region_stats.head(3)
    bottom_3_regions = region_stats.tail(3)

    print("Top 3 régions avec les meilleures entrées moyennes par fauteuil en 2022:")
    print(top_3_regions)

    print("\nBottom 3 régions avec les pires entrées moyennes par fauteuil en 2022:")
    print(bottom_3_regions)

    # Visualiser les données des 10 premières régions
    plot_top_regions(region_stats, average_entries_per_seat)

    # Filtrer pour garder uniquement l'année 2022
    data_2022 = filter_data_for_2022(filtered_data)

    # Calculer et afficher les corrélations
    print("Calcul des corrélations :")
    corr_screens = calculate_and_display_correlation(data_2022, "écrans", "entrées 2022")
    corr_seats = calculate_and_display_correlation(data_2022, "fauteuils", "entrées 2022")

    # Créer les visualisations
    print("Création des visualisations :")
    plot_scatter_with_regression(data_2022, "écrans", "entrées 2022", "Relation entre le nombre d'écrans et les entrées 2022")
    plot_scatter_with_regression(data_2022, "fauteuils", "entrées 2022", "Relation entre le nombre de fauteuils et les entrées 2022")

    # Conclusion basée sur les corrélations
    if abs(corr_screens) > abs(corr_seats):
        print("La variable 'écrans' a un impact plus important sur les entrées annuelles.")
    else:
        print("La variable 'fauteuils' a un impact plus important sur les entrées annuelles.")

if __name__ == "__main__":
    main()
