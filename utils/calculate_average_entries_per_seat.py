def calculate_average_entries_per_seat(data, year):
    #Ajoute une colonne pour les entrées moyennes par fauteuil pour une année donnée.
    
    column_name = f"entrées moyennes par fauteuil {year}"
    data[column_name] = data[f"entrées {year}"] / data["fauteuils"]
    return column_name
