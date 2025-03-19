# Sea Level Predictor Dashboard - Transfer Guide

## System Requirements
- Python 3.8 or higher
- pip or conda package manager
- Git (optional)

## Installation Steps

1. **Set up Python Environment**
   ```bash
   # Using conda
   conda create -n sealevel python=3.9
   conda activate sealevel
   
   # OR using venv
   python -m venv sealevel
   source sealevel/bin/activate  # Linux/Mac
   .\sealevel\Scripts\activate   # Windows
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify Installation**
   ```bash
   python -c "import streamlit; import pandas; import plotly"
   ```

4. **Data Setup**
   - Ensure `epa-sea-level.csv` is in the root directory
   - Verify data format matches expected schema

5. **Running the Dashboard**
   ```bash
   streamlit run app.py
   ```

## Common Issues and Solutions

1. **Streamlit Not Found Error**
   ```bash
   # Solution 1: Install directly
   pip install streamlit
   
   # Solution 2: Use python -m
   python -m streamlit run app.py
   ```

2. **Date Range Error**
   - Ensure data is properly formatted
   - Check Year column contains valid integers
   - Verify datetime conversions

3. **Package Conflicts**
   ```bash
   # Solution: Create fresh environment
   conda create -n sealevel_new python=3.9 --no-deps
   conda activate sealevel_new
   pip install -r requirements.txt
   ```

## Data Format Requirements
- CSV file must contain:
  - "Year" column (integer)
  - "CSIRO Adjusted Sea Level" column (float)
- No missing values in required columns

## Deployment Notes
1. Local Development:
   - Use `streamlit run app.py`
   - Access at http://localhost:8501

2. Server Deployment:
   - Set PYTHONPATH to project directory
   - Configure streamlit config.toml if needed
   - Use process manager (e.g., supervisor) 