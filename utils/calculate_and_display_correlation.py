# Fonction pour calculer et afficher la corrélation entre deux colonnes
def calculate_and_display_correlation(data, column1, column2):
    correlation = data[column1].corr(data[column2])
    print(f"Corrélation entre {column1} et {column2} : {correlation:.2f}")
    return correlation