"""
Module de prédiction du niveau de la mer.

Ce module implémente un modèle de prédiction du niveau de la mer utilisant
des techniques avancées de régression et d'analyse temporelle.
"""

from typing import Tuple, List, Optional, Dict, Any
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from scipy import stats
import logging
from dataclasses import dataclass
from datetime import datetime

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class ModelConfig:
    """Configuration du modèle de prédiction."""
    polynomial_degree: int = 3
    confidence_level: float = 0.95
    prediction_years: int = 80
    seasonal_period: int = 12
    min_data_points: int = 100

class SeaLevelPredictor:
    """
    Classe principale pour la prédiction du niveau de la mer.
    
    Cette classe implémente un modèle de prédiction sophistiqué utilisant
    la régression polynomiale et l'analyse saisonnière.
    """
    
    def __init__(self, config: ModelConfig = ModelConfig()):
        """
        Initialise le prédicteur avec une configuration donnée.
        
        Args:
            config: Configuration du modèle
        """
        self.config = config
        self.model = None
        self.poly_features = PolynomialFeatures(degree=config.polynomial_degree)
        self.data: Optional[pd.DataFrame] = None
        self._validate_config()
        
    def _validate_config(self) -> None:
        """Valide la configuration du modèle."""
        if self.config.confidence_level <= 0 or self.config.confidence_level >= 1:
            raise ValueError("Le niveau de confiance doit être entre 0 et 1")
        if self.config.polynomial_degree < 1:
            raise ValueError("Le degré polynomial doit être positif")
            
    def prepare_data(self, data: pd.DataFrame) -> None:
        """
        Prépare les données pour l'entraînement.
        
        Args:
            data: DataFrame contenant les données historiques
        """
        try:
            # Validation des données
            required_columns = ['date', 'level']
            if not all(col in data.columns for col in required_columns):
                raise ValueError(f"Les colonnes requises sont: {required_columns}")
            
            # Conversion des dates
            data['date'] = pd.to_datetime(data['date'])
            data['year'] = data['date'].dt.year
            
            # Normalisation des données
            data['level_normalized'] = (data['level'] - data['level'].mean()) / data['level'].std()
            
            self.data = data
            logger.info(f"Données préparées avec succès: {len(data)} points")
            
        except Exception as e:
            logger.error(f"Erreur lors de la préparation des données: {str(e)}")
            raise
            
    def train(self) -> Dict[str, float]:
        """
        Entraîne le modèle sur les données préparées.
        
        Returns:
            Dict contenant les métriques de performance
        """
        if self.data is None:
            raise ValueError("Les données doivent être préparées avant l'entraînement")
            
        try:
            # Préparation des features
            X = self.poly_features.fit_transform(self.data[['year']].values)
            y = self.data['level_normalized'].values
            
            # Entraînement du modèle
            self.model = LinearRegression()
            self.model.fit(X, y)
            
            # Calcul des métriques
            y_pred = self.model.predict(X)
            r2 = self.model.score(X, y)
            mse = np.mean((y - y_pred) ** 2)
            
            metrics = {
                'r2_score': r2,
                'mse': mse,
                'rmse': np.sqrt(mse)
            }
            
            logger.info(f"Modèle entraîné avec succès. R²: {r2:.4f}")
            return metrics
            
        except Exception as e:
            logger.error(f"Erreur lors de l'entraînement: {str(e)}")
            raise
            
    def predict(self, years: Optional[List[int]] = None) -> pd.DataFrame:
        """
        Génère des prédictions pour les années spécifiées.
        
        Args:
            years: Liste des années pour la prédiction
            
        Returns:
            DataFrame contenant les prédictions et intervalles de confiance
        """
        if self.model is None:
            raise ValueError("Le modèle doit être entraîné avant la prédiction")
            
        try:
            # Génération des années de prédiction si non spécifiées
            if years is None:
                last_year = self.data['year'].max()
                years = list(range(last_year + 1, last_year + self.config.prediction_years + 1))
            
            # Préparation des features pour la prédiction
            X_pred = self.poly_features.transform(np.array(years).reshape(-1, 1))
            
            # Prédictions
            y_pred = self.model.predict(X_pred)
            
            # Calcul des intervalles de confiance
            std_err = np.sqrt(np.sum((self.data['level_normalized'] - self.model.predict(
                self.poly_features.transform(self.data[['year']].values)
            )) ** 2) / (len(self.data) - len(self.model.coef_)))
            
            t_value = stats.t.ppf((1 + self.config.confidence_level) / 2, len(self.data) - len(self.model.coef_))
            confidence_interval = t_value * std_err
            
            # Création du DataFrame de résultats
            results = pd.DataFrame({
                'year': years,
                'predicted_level': y_pred * self.data['level'].std() + self.data['level'].mean(),
                'lower_bound': (y_pred - confidence_interval) * self.data['level'].std() + self.data['level'].mean(),
                'upper_bound': (y_pred + confidence_interval) * self.data['level'].std() + self.data['level'].mean()
            })
            
            logger.info(f"Prédictions générées pour {len(years)} années")
            return results
            
        except Exception as e:
            logger.error(f"Erreur lors de la prédiction: {str(e)}")
            raise
            
    def analyze_seasonality(self) -> Dict[str, Any]:
        """
        Analyse la composante saisonnière des données.
        
        Returns:
            Dict contenant les résultats de l'analyse saisonnière
        """
        if self.data is None:
            raise ValueError("Les données doivent être préparées avant l'analyse")
            
        try:
            # Décomposition saisonnière
            seasonal_data = self.data.set_index('date')
            seasonal_data = seasonal_data.resample('M').mean()
            
            # Calcul des statistiques saisonnières
            seasonal_stats = {
                'mean': seasonal_data['level'].mean(),
                'std': seasonal_data['level'].std(),
                'min': seasonal_data['level'].min(),
                'max': seasonal_data['level'].max()
            }
            
            logger.info("Analyse saisonnière effectuée avec succès")
            return seasonal_stats
            
        except Exception as e:
            logger.error(f"Erreur lors de l'analyse saisonnière: {str(e)}")
            raise
            
    def get_model_summary(self) -> Dict[str, Any]:
        """
        Génère un résumé complet du modèle.
        
        Returns:
            Dict contenant les informations du modèle
        """
        if self.model is None:
            raise ValueError("Le modèle doit être entraîné avant de générer le résumé")
            
        try:
            summary = {
                'coefficients': self.model.coef_.tolist(),
                'intercept': float(self.model.intercept_),
                'polynomial_degree': self.config.polynomial_degree,
                'confidence_level': self.config.confidence_level,
                'data_points': len(self.data) if self.data is not None else 0,
                'feature_names': self.poly_features.get_feature_names(['year'])
            }
            
            return summary
            
        except Exception as e:
            logger.error(f"Erreur lors de la génération du résumé: {str(e)}")
            raise

def main():
    """Fonction principale pour tester le modèle."""
    try:
        # Configuration du modèle
        config = ModelConfig(
            polynomial_degree=3,
            confidence_level=0.95,
            prediction_years=80
        )
        
        # Création du prédicteur
        predictor = SeaLevelPredictor(config)
        
        # Chargement des données (exemple)
        data = pd.read_csv('epa-sea-level.csv')
        
        # Préparation et entraînement
        predictor.prepare_data(data)
        metrics = predictor.train()
        
        # Génération des prédictions
        predictions = predictor.predict()
        
        # Analyse saisonnière
        seasonality = predictor.analyze_seasonality()
        
        # Affichage des résultats
        print("\nMétriques du modèle:")
        for metric, value in metrics.items():
            print(f"{metric}: {value:.4f}")
            
        print("\nRésumé des prédictions:")
        print(predictions.head())
        
        print("\nAnalyse saisonnière:")
        for stat, value in seasonality.items():
            print(f"{stat}: {value:.4f}")
            
    except Exception as e:
        logger.error(f"Erreur dans la fonction principale: {str(e)}")
        raise

if __name__ == "__main__":
    main() 