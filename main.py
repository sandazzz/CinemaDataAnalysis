from utils.filter_columns import filter_csv_columns
import pandas as pd

# Chemins vers les fichiers
cinema_file ="data/cinema.csv"

#df = pd.read_csv(cinema_file, sep=';')
#print(df)

#colonne utile à l'étude
#Les colonnes sélectionnées ont été choisies pour répondre directement à l'objectif de l'étude, 
# qui est de déterminer si les infrastructures cinématographiques (nombre d'écrans et fauteuils) 
# influencent significativement la fréquentation des cinémas. 
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

filtered_file = filter_csv_columns(cinema_file, columns, sep=";")

print(filtered_file)