import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

from utils.filter_columns import filter_csv_columns
from utils.calculate_average_entries_per_seat import calculate_average_entries_per_seat
from utils.group_and_sort_by_region import group_and_sort_by_region
from utils.calculate_and_display_correlation import calculate_and_display_correlation
from utils.graph.plot_top_regions import plot_top_regions
from utils.graph.plot_scatter_with_regression import plot_scatter_with_regression

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

    #Exercice 2

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

    #Exercice 3

    # Voir uniquement les données pour 2022
    data_2022 = filtered_data[filtered_data['entrées 2022'].notnull()]

    # Calculer et afficher les corrélations
    print("Calcul des corrélations :")
    corr_screens = calculate_and_display_correlation(data_2022, "écrans", "entrées 2022")
    corr_seats = calculate_and_display_correlation(data_2022, "fauteuils", "entrées 2022")

    # Créer les nuages de points
    print("Création des visualisations :")
    plot_scatter_with_regression(data_2022, "écrans", "entrées 2022", "Relation entre le nombre d'écrans et les entrées 2022")
    plot_scatter_with_regression(data_2022, "fauteuils", "entrées 2022", "Relation entre le nombre de fauteuils et les entrées 2022")

    # Conclusion basée sur les corrélations
    if abs(corr_screens) > abs(corr_seats):
        print("La variable 'écrans' a un impact plus important sur les entrées annuelles.")
    else:
        print("La variable 'fauteuils' a un impact plus important sur les entrées annuelles.")

    # Exercice 4
    print("\nExercice 4 : Modèle de régression linéaire")

    # Diviser les données en variables explicatives et cible pour 2021
    features = ["écrans", "fauteuils", "population de la commune"]
    target = "entrées 2021"

    data_2021 = filtered_data[filtered_data[target].notnull()]
    X = data_2021[features]
    y = data_2021[target]

    # Diviser en ensembles d'entraînement et de test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Entraîner le modèle de régression linéaire
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Évaluer les performances du modèle
    y_pred_train = model.predict(X_train)
    y_pred_test = model.predict(X_test)

    r2_train = r2_score(y_train, y_pred_train)
    r2_test = r2_score(y_test, y_pred_test)
    mae_test = mean_absolute_error(y_test, y_pred_test)

    print(f"Coefficient de détermination (R2) sur l'ensemble d'entraînement : {r2_train:.2f}")
    print(f"Coefficient de détermination (R2) sur l'ensemble de test : {r2_test:.2f}")
    print(f"Erreur moyenne absolue (MAE) sur l'ensemble de test : {mae_test:.2f}")

    # Tester le modèle sur les données de 2022
    X_2022 = data_2022[features]
    y_2022 = data_2022["entrées 2022"]
    y_pred_2022 = model.predict(X_2022)

    # Comparer les prédictions avec les valeurs réelles
    comparison = pd.DataFrame({"Réel": y_2022, "Prédit": y_pred_2022})
    print("\nComparaison des prédictions avec les valeurs réelles pour 2022 :")
    print(comparison.head(10))

if __name__ == "__main__":
    main()
