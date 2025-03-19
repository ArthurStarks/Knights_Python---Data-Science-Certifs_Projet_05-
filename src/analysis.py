def add_advanced_statistics(df: pd.DataFrame) -> Dict[str, Any]:
    """
    Calculate advanced statistical metrics
    """
    stats = {}
    
    # Calculate rate of change
    df['Annual_Change'] = df['CSIRO Adjusted Sea Level'].diff()
    stats['acceleration'] = df['Annual_Change'].mean()
    
    # Calculate decadal averages
    df['Decade'] = (df['Year'] // 10) * 10
    decadal_means = df.groupby('Decade')['CSIRO Adjusted Sea Level'].mean()
    stats['decadal_trends'] = decadal_means
    
    # Calculate volatility
    stats['volatility'] = df['CSIRO Adjusted Sea Level'].std()
    
    return stats

def seasonal_decomposition(df: pd.DataFrame) -> Dict[str, pd.Series]:
    """
    Perform seasonal decomposition of the time series
    """
    from statsmodels.tsa.seasonal import seasonal_decompose
    
    # Ensure data is sorted by date
    df_sorted = df.sort_values('Date')
    
    # Perform decomposition
    decomposition = seasonal_decompose(
        df_sorted['CSIRO Adjusted Sea Level'],
        period=12,  # Annual cycle
        extrapolate_trend='freq'
    )
    
    return {
        'trend': decomposition.trend,
        'seasonal': decomposition.seasonal,
        'residual': decomposition.resid
    } 