# Sea Level Predictor Dashboard Documentation

## Overview
This Streamlit dashboard visualizes and analyzes sea level rise data from the EPA. It provides interactive visualizations, statistical analysis, and data exploration capabilities.

## Installation
1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application
```bash
streamlit run app.py
```

## Features
1. **Interactive Visualization**
   - Historical sea level data visualization
   - Multiple trend lines
   - Adjustable prediction range
   - Date range filtering

2. **Analysis Tools**
   - Basic and Advanced analysis modes
   - Multiple chart types
   - Trend analysis with statistics
   - Confidence intervals

3. **Data Export**
   - CSV format
   - Excel format
   - JSON format

4. **Data Explorer**
   - Raw data viewing
   - Column selection
   - Basic statistics

## File Structure
- `app.py`: Main application file
- `epa-sea-level.csv`: Source data
- `requirements.txt`: Project dependencies

## Usage Guide
1. **Dashboard Controls** (Sidebar)
   - Analysis Type: Choose between Basic and Advanced
   - Chart Type: Select visualization style
   - Prediction Range: Adjust future predictions
   - Export Options: Download data in various formats

2. **Main Visualization**
   - Interactive plot with historical data
   - Two prediction lines (full period and recent trend)
   - Adjustable date range filter

3. **Statistical Analysis**
   - Trend analysis for different periods
   - Summary statistics
   - Raw data explorer

## Troubleshooting
Common issues and solutions:
1. Date Range Error: Ensure dates are in correct format (YYYY-MM-DD)
2. Data Loading Error: Verify CSV file is in correct location
3. Installation Issues: Check Python and package versions 