# Prédicteur du Niveau de la Mer 🌊

## Aperçu
Application interactive d'analyse et de prédiction du niveau de la mer utilisant les données de l'EPA (Environmental Protection Agency).

## Installation

### Prérequis
- Python 3.8 ou supérieur
- pip ou conda

### Installation rapide
```bash
# Créer un environnement virtuel
python -m venv env
source env/bin/activate  # Linux/Mac
.\env\Scripts\activate   # Windows

# Installer les dépendances
pip install -r requirements.txt

# Lancer l'application
streamlit run app.py
```

### Dépendances principales
- streamlit>=1.32.0
- pandas
- plotly>=5.18.0
- numpy
- scipy
- seaborn>=0.13.2

## Fonctionnalités
- 📊 Visualisation interactive des données
- 📈 Prédictions avec régression linéaire et polynomiale
- 🔍 Analyse statistique détaillée
- 💾 Export des données (CSV, Excel, JSON)

## Résolution des problèmes courants

### Erreur de date
**Erreur**: `streamlit.errors.StreamlitAPIException: Date value...`
**Solution**: Vérifier le format des dates dans le fichier source

### Erreur de chargement
**Solution**: Vérifier que le fichier `epa-sea-level.csv` est présent dans le répertoire

## Support
Pour toute question technique, consulter la documentation détaillée dans `/docs` 