def group_and_sort_by_region(data, column):
    #Regroupe les données par région et calcule la moyenne pour une colonne donnée.
    #Retourne une série triée par ordre décroissant.
    
    return data.groupby("commune")[column].mean().sort_values(ascending=False)