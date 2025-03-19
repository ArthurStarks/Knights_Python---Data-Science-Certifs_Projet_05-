# Configuration Avancée et Sécurité 🔒

## 1. Sécurité Renforcée

### A. Configuration de l'Authentification
```python
# app.py
def configure_auth():
    """Configuration de l'authentification utilisateur"""
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False

    if not st.session_state.authenticated:
        username = st.text_input("Nom d'utilisateur")
        password = st.text_input("Mot de passe", type="password")
        
        if st.button("Connexion"):
            if verify_credentials(username, password):
                st.session_state.authenticated = True
                st.experimental_rerun()
            else:
                st.error("Identifiants invalides")
        return False
    return True
```

### B. Protection des Données Sensibles
```python
# config.py
class SecurityConfig:
    """Configuration de sécurité de l'application"""
    ALLOWED_ORIGINS = ['localhost', 'votre-domaine.com']
    MAX_UPLOAD_SIZE = 5 * 1024 * 1024  # 5MB
    ALLOWED_FILE_TYPES = ['.csv', '.xlsx']
    SESSION_TIMEOUT = 3600  # 1 heure
```

## 2. Optimisation des Performances

### A. Gestion de la Mémoire
```python
# utils.py
def optimize_dataframe(df):
    """Optimisation de la consommation mémoire du DataFrame"""
    optimized_df = df.copy()
    
    # Optimisation des types numériques
    for col in df.select_dtypes(['float64']):
        optimized_df[col] = pd.to_numeric(df[col], downcast='float')
    
    for col in df.select_dtypes(['int64']):
        optimized_df[col] = pd.to_numeric(df[col], downcast='integer')
    
    # Optimisation des chaînes
    for col in df.select_dtypes(['object']):
        if df[col].nunique() / len(df) < 0.5:  # Si moins de 50% de valeurs uniques
            optimized_df[col] = df[col].astype('category')
    
    return optimized_df
```

### B. Cache Intelligent
```python
# cache_manager.py
class CacheManager:
    """Gestionnaire de cache avancé"""
    def __init__(self):
        self.cache_timeout = 3600  # 1 heure
        self.max_cache_size = 1024 * 1024 * 100  # 100MB

    @st.cache_data(ttl=3600)
    def cache_data_with_timeout(self, data):
        """Cache avec expiration"""
        return data

    def clear_expired_cache(self):
        """Nettoyage du cache expiré"""
        st.cache_data.clear()
```

## 3. Monitoring et Diagnostics

### A. Système de Logs
```python
# logging_config.py
class LogManager:
    """Gestionnaire de logs personnalisé"""
    def __init__(self):
        self.logs = []
        self.max_logs = 1000

    def log_event(self, level, message, context=None):
        """Enregistre un événement"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = {
            'timestamp': timestamp,
            'level': level,
            'message': message,
            'context': context
        }
        self.logs.append(log_entry)
        
        if len(self.logs) > self.max_logs:
            self.logs.pop(0)

    def get_recent_logs(self, count=50):
        """Récupère les logs récents"""
        return self.logs[-count:]
```

### B. Surveillance des Performances
```python
# monitoring.py
class PerformanceMonitor:
    """Moniteur de performances"""
    def __init__(self):
        self.metrics = {}

    def start_timer(self, operation):
        """Démarre un chronomètre pour une opération"""
        self.metrics[operation] = {'start': time.time()}

    def end_timer(self, operation):
        """Termine le chronomètre et calcule la durée"""
        if operation in self.metrics:
            start = self.metrics[operation]['start']
            duration = time.time() - start
            self.metrics[operation]['duration'] = duration
            return duration
```

## 4. Interface Administrateur

### A. Panel d'Administration
```python
def show_admin_panel():
    """Affiche le panel d'administration"""
    st.sidebar.markdown("### Administration")
    
    if st.sidebar.checkbox("Afficher les Métriques"):
        show_performance_metrics()
    
    if st.sidebar.checkbox("Logs Système"):
        show_system_logs()
    
    if st.sidebar.checkbox("Gestion du Cache"):
        manage_cache()
```

### B. Gestion des Utilisateurs
```python
class UserManager:
    """Gestionnaire des utilisateurs"""
    def __init__(self):
        self.users = {}

    def add_user(self, username, role='user'):
        """Ajoute un nouvel utilisateur"""
        if username not in self.users:
            self.users[username] = {
                'role': role,
                'created_at': datetime.now(),
                'last_login': None
            }

    def update_last_login(self, username):
        """Met à jour la dernière connexion"""
        if username in self.users:
            self.users[username]['last_login'] = datetime.now()
```

## 5. Gestion des Erreurs

### A. Gestionnaire d'Erreurs Personnalisé
```python
def custom_error_handler(func):
    """Décorateur pour la gestion des erreurs"""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except FileNotFoundError:
            st.error("Fichier non trouvé. Vérifiez le chemin d'accès.")
        except pd.errors.EmptyDataError:
            st.error("Le fichier de données est vide.")
        except Exception as e:
            st.error(f"Erreur inattendue: {str(e)}")
            log_error(e)
    return wrapper
```

Would you like me to:
1. Add more security features?
2. Expand the monitoring system?
3. Add more administrative tools?
4. Include additional error handling scenarios? 