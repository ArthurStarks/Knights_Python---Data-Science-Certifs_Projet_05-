# Sea Level Predictor Dashboard - Technical Documentation

## 1. Project Overview
The Sea Level Predictor Dashboard is an interactive web application built with Streamlit that visualizes and analyzes sea level rise trends using EPA data.

## 2. Installation & Setup

### 2.1 Prerequisites
- Python 3.8+
- pip or conda package manager

### 2.2 Installation Steps
```bash
# Create virtual environment
python -m venv sealevel_env
source sealevel_env/bin/activate  # Linux/Mac
.\sealevel_env\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt
```

### 2.3 Running the Application
```bash
streamlit run app.py
```

## 3. Common Issues & Troubleshooting

### 3.1 Date Range Error
**Error**: `streamlit.errors.StreamlitAPIException: Date value should be date/datetime`
**Solution**: 
- Check date format conversion in load_data()
- Ensure Year column contains valid integers
- Verify datetime conversions are correct

### 3.2 Data Loading Error
**Error**: `FileNotFoundError: epa-sea-level.csv not found`
**Solution**:
- Verify CSV file exists in project root
- Check file permissions
- Ensure correct working directory

### 3.3 Prediction Range Error
**Error**: `ValueError: x and y must have same first dimension`
**Solution**:
- Check data filtering logic
- Verify prediction year range
- Ensure no missing values in data

## 4. Code Structure

### 4.1 Main Components
- `app.py`: Main application file
- `load_data()`: Data loading and preprocessing
- `create_prediction_data()`: Prediction calculations
- `main()`: Application entry point

### 4.2 Key Functions
```python
def load_data():
    # Loads and preprocesses data
    # Returns: pandas DataFrame

def create_prediction_data():
    # Creates prediction data using linear regression
    # Returns: years, predictions, slope, intercept, r2
```

## 5. Customization Guide

### 5.1 Adding New Features
1. Add new controls to sidebar
2. Update visualization logic
3. Add new statistical calculations

### 5.2 Modifying Predictions
1. Adjust prediction range in sidebar
2. Modify regression parameters
3. Update confidence intervals

## 6. Maintenance

### 6.1 Data Updates
1. Replace epa-sea-level.csv with new data
2. Ensure column names match expected format
3. Verify data types and ranges

### 6.2 Performance Optimization
1. Use caching for data loading
2. Optimize filtering operations
3. Minimize redundant calculations

## 7. Testing

### 7.1 Manual Testing Steps
1. Verify data loading
2. Check prediction calculations
3. Validate visualization updates
4. Test export functionality

### 7.2 Automated Testing
```python
# Example test case
def test_prediction_data():
    df = load_data()
    years, pred, slope, intercept, r2 = create_prediction_data(
        df, 2000, 2050, False
    )
    assert len(years) == 51
    assert all(pred.notna())
```

## 3. Sécurité et Performance

### A. Sécurité
```python
# Configuration recommandée
st.set_page_config(
    page_title="Prédicteur Niveau Mer",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Protection des données
st.secrets["key"] = "valeur"  # Pour les variables sensibles
```

### B. Optimisation
```python
# Cache des données
@st.cache_data
def load_data():
    return pd.read_csv("data.csv")

# Cache des calculs
@st.cache_resource
def perform_heavy_calculation():
    # calculs intensifs
    pass
```

## 4. Maintenance et Surveillance

### A. Logs et Monitoring
```python
# Configuration des logs
import logging

logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Exemple d'utilisation
logging.info("Application démarrée")
logging.error("Erreur détectée")
```

### B. Sauvegarde des Données
```bash
# Script de sauvegarde
#!/bin/bash
DATE=$(date +%Y%m%d)
cp data/epa-sea-level.csv backup/data_$DATE.csv
```

## 5. Résolution des Problèmes Courants

### A. Erreurs de Déploiement
1. **Erreur de Port**
   ```bash
   # Solution
   export PORT=8501
   streamlit run app.py
   ```

2. **Erreur de Dépendances**
   ```bash
   # Solution
   pip freeze > requirements.txt
   pip install -r requirements.txt
   ```

### B. Problèmes de Performance
1. **Optimisation de la Mémoire**
   ```python
   # Réduction de l'utilisation mémoire
   def optimize_dataframe(df):
       for col in df.select_dtypes(['float']):
           df[col] = pd.to_numeric(df[col], downcast='float')
       return df
   ```

2. **Gestion du Cache**
   ```python
   # Nettoyage périodique
   if st.button('Vider le Cache'):
       st.cache_data.clear()
   ```

## 6. Mise à Jour de l'Application

### A. Procédure de Mise à Jour
1. Test local
2. Push sur GitHub
3. Déploiement automatique

### B. Rollback
```bash
# En cas de problème
git reset --hard HEAD~1
git push -f origin main
```

## 7. Documentation Utilisateur

### A. Guide Rapide
```markdown
1. Accéder à l'URL de l'application
2. Sélectionner les paramètres d'analyse
3. Visualiser les résultats
4. Exporter les données si nécessaire
```

### B. Contact Support
Email: support@votre-app.com
Tickets: github.com/votre-repo/issues