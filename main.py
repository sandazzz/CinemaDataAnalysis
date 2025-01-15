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

if __name__ == "__main__":
    main()
