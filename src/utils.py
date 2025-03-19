def validate_data_quality(df: pd.DataFrame) -> List[str]:
    """
    Validate data quality and return warnings
    """
    warnings = []
    
    # Check for missing values
    missing = df.isnull().sum()
    if missing.any():
        warnings.append(f"Missing values detected: {missing.to_dict()}")
    
    # Check for outliers using IQR method
    Q1 = df['CSIRO Adjusted Sea Level'].quantile(0.25)
    Q3 = df['CSIRO Adjusted Sea Level'].quantile(0.75)
    IQR = Q3 - Q1
    outliers = df[
        (df['CSIRO Adjusted Sea Level'] < (Q1 - 1.5 * IQR)) |
        (df['CSIRO Adjusted Sea Level'] > (Q3 + 1.5 * IQR))
    ]
    if not outliers.empty:
        warnings.append(f"Found {len(outliers)} potential outliers")
    
    return warnings

def handle_errors(func):
    """
    Decorator for error handling
    """
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            st.error(f"Error in {func.__name__}: {str(e)}")
            st.stop()
    return wrapper 