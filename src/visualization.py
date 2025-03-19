def create_advanced_plots(df: pd.DataFrame, stats: Dict[str, Any]) -> Dict[str, go.Figure]:
    """
    Create additional visualization plots
    """
    plots = {}
    
    # Create rate of change plot
    roc_fig = go.Figure()
    roc_fig.add_trace(go.Scatter(
        x=df['Year'],
        y=df['Annual_Change'],
        mode='lines+markers',
        name='Annual Change',
        line=dict(color='orange')
    ))
    roc_fig.update_layout(
        title="Annual Rate of Sea Level Change",
        xaxis_title="Year",
        yaxis_title="Change (inches/year)"
    )
    plots['rate_of_change'] = roc_fig
    
    # Create decadal trends plot
    decade_fig = go.Figure()
    decade_fig.add_trace(go.Bar(
        x=stats['decadal_trends'].index,
        y=stats['decadal_trends'].values,
        name='Decadal Average'
    ))
    decade_fig.update_layout(
        title="Decadal Sea Level Averages",
        xaxis_title="Decade",
        yaxis_title="Average Sea Level (inches)"
    )
    plots['decadal_trends'] = decade_fig
    
    return plots

def add_annotations(fig: go.Figure, stats: Dict[str, Any]) -> None:
    """
    Add statistical annotations to plot
    """
    fig.add_annotation(
        text=f"Acceleration: {stats['acceleration']:.4f} inches/year²",
        xref="paper", yref="paper",
        x=0.02, y=0.98,
        showarrow=False,
        bgcolor="rgba(255, 255, 255, 0.8)"
    ) 