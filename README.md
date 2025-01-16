# CinemaDataAnalysis

# Guide : Création et utilisation de l'environnement virtuel (venv) 

Ce guide explique comment créer et configurer un environnement virtuel Python pour votre projet, en utilisant un fichier `requirements.txt`.

## Prérequis

- **Python** : Assurez-vous que Python est installé sur votre système. Vous pouvez vérifier la version de Python installée en exécutant la commande suivante :

  ```bash
  python --version
  ```
  ou
  ```bash
  python3 --version
  ```

- **Pip** : Pip est normalement inclus avec Python. Vous pouvez vérifier sa présence avec :

  ```bash
  pip --version
  ```

## Création de l'environnement virtuel

1. **Accédez au répertoire du projet** :
   Naviguez jusqu'à votre répertoire de projet :

   ```bash
   cd /chemin/vers/votre/projet
   ```

2. **Créez l'environnement virtuel** :
   Utilisez la commande suivante pour créer un environnement virtuel nommé `venv` :

   ```bash
   python -m venv venv
   ```
   ou, selon votre système :
   ```bash
   python3 -m venv venv
   ```

3. **Activez l'environnement virtuel** :
   - Sur **Windows** :
     ```bash
     venv\Scripts\activate
     ```
   - Sur **macOS/Linux** :
     ```bash
     source venv/bin/activate
     ```

   Une fois activé, le nom de votre environnement virtuel apparaît à gauche de l'invite de commande.

## Installation des dépendances

1. **Vérifiez la présence d'un fichier `requirements.txt`** :
   Assurez-vous que le fichier `requirements.txt` est situé à la racine de votre projet.

2. **Installez les dépendances** :
   Exécutez la commande suivante pour installer les bibliothèques listées dans le fichier `requirements.txt` :

   ```bash
   pip install -r requirements.txt
   ```

## Utilisation de l'environnement virtuel

- Tant que l'environnement virtuel est activé, toutes les commandes Python et Pip affecteront uniquement cet environnement.
- Pour **désactiver l'environnement virtuel**, utilisez :

  ```bash
  deactivate
  ```

## Gestion des dépendances

Si vous ajoutez de nouvelles bibliothèques à votre projet, pensez à mettre à jour le fichier `requirements.txt` :

```bash
pip freeze > requirements.txt
```

## Suppression de l'environnement virtuel

Pour supprimer un environnement virtuel, il suffit de supprimer le dossier `venv` :

```bash
rm -rf venv
```

## Réponses aux questions

### Exercice 3 - Question : Selon vous, quelle est la variable ayant le plus d’impact sur les entrées annuelles ?

Corrélation entre le nombre d'écrans et les entrées 2022 : 0.88
Corrélation entre le nombre de fauteuils et les entrées 2022 : 0.84

La variable "écrans" a un impact légèrement plus important sur les entrées annuelles que la variable "fauteuils".
Cela est visible à travers la corrélation légèrement plus élevée (0.88 contre 0.84).
Les visualisations montrent une tendance croissante plus marquée entre le nombre d'écrans et les entrées 2022, renforçant ainsi cette conclusion.

### Exercice 4 - Question : Selon les performances du modèle, le nombre d’écrans ou de fauteuils est-il un bon prédicteur des entrées ?

Bien que le nombre d'écrans et de fauteuils soient liés aux entrées, les performances du modèle (R² = 0.66) montrent qu'ils ne suffisent pas pour prédire précisément les entrées. D'autres facteurs influencent probablement les résultats et devraient être inclus pour améliorer les prédictions.