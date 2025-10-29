# Finnish Happiness Factor Finder 🇫🇮

A comprehensive data analysis application built for Finland's Ministry of Mirth and Merriment to understand the drivers behind Finland's consistently high happiness rankings in the World Happiness Report.

## 🎯 Project Overview

This project analyzes happiness factors using data science and AI pair programming to generate data-driven insights about what makes Finland one of the happiest countries in the world.

### Key Features ✅

- **Multi-source Data Integration**: Combines World Happiness Report 2024 and Food Supply data (1961-2011)
- **Statistical Analysis**: Pearson and Spearman correlations with significance testing
- **Interactive Visualizations**: Built with Plotly for dynamic charts and graphs
- **Web Dashboard**: Streamlit-based interface with multiple analysis views
- **Nordic Comparisons**: Benchmarks Finland against other Nordic countries
- **Hypothesis Generation**: AI-powered insights based on statistical correlations
- **Export Capabilities**: Download charts and reports
- **Responsive Design**: Works on desktop and tablet devices

## 📊 Analysis Results

### Finland's Global Performance
- **Global Happiness Rank**: #1 out of 143 countries (2024)
- **Happiness Score**: 7.741 out of 10
- **Significant Factors**: 8 statistically significant correlations found

### Top Happiness Correlations
1. **Social Support** (r = 0.814, p < 0.001)
2. **Log GDP per capita** (r = 0.789, p < 0.001)
3. **Healthy Life Expectancy** (r = 0.757, p < 0.001)
4. **Freedom to Make Life Choices** (r = 0.549, p < 0.001)
5. **Perceptions of Corruption** (negative correlation)

### Data-Driven Hypotheses

1. **Social & Economic Foundations**: Strong social systems and economic stability are key drivers
2. **Nordic Leadership**: Finland ranks #1 among Nordic countries in happiness
3. **Freedom & Social Trust**: Individual autonomy and community trust are critical
4. **Health & Longevity Impact**: Quality healthcare and life expectancy contribute significantly
5. **Trust in Institutions**: Low perceived corruption correlates with happiness

## 🛠️ Technology Stack

### Core Technologies
- **Python 3.13**: Programming language
- **pandas 2.3**: Data manipulation and analysis
- **NumPy 1.26**: Numerical computing
- **SciPy 1.16**: Statistical analysis
- **scikit-learn 1.7**: Machine learning utilities

### Visualization & Interface
- **Plotly 5.17**: Interactive visualizations
- **Streamlit 1.28**: Web dashboard framework
- **HTML/CSS**: Custom styling

### Data Processing
- **requests 2.31**: HTTP client for API calls
- **python-dotenv**: Environment configuration

### Testing & Quality
- **pytest 7.4**: Testing framework
- **pytest-cov**: Coverage reporting

## 📁 Project Structure

```
copilot-data-analysis-exercise/
├── data/                          # Data files
│   ├── WHR2024.csv               # World Happiness Report 2024
│   ├── EdibleFoods-1961-2011.csv # Food supply data
│   └── cache/                    # API response cache
├── src/                          # Source code
│   ├── data/                     # Data loading and cleaning
│   │   ├── loader.py            # DataLoader class
│   │   └── cleaner.py           # DataCleaner class
│   ├── analysis/                 # Statistical analysis
│   │   └── analyzer.py          # HappinessAnalyzer class
│   ├── visualization/            # Charts and graphs
│   │   └── charts.py            # HappinessVisualizer class
│   └── dashboard/                # Web interface
│       └── app.py               # Streamlit application
├── tests/                        # Test suite
│   ├── test_data.py             # Data module tests
│   └── test_analysis.py         # Analysis module tests
├── requirements.txt              # Python dependencies
└── README.md                    # Project documentation
```

## 🚀 Getting Started

### Prerequisites
- Python 3.9 or higher
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yasali/copilot-data-analysis-exercise.git
   cd copilot-data-analysis-exercise
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # macOS/Linux
   # OR
   .venv\Scripts\activate     # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the dashboard**
   ```bash
   # Option 1: Use the run script (recommended)
   ./run.sh
   
   # Option 2: Run directly
   streamlit run app.py
   ```

5. **Access the application**
   - Open your browser to `http://localhost:8501` or `http://localhost:8502`
   - Navigate through different analysis sections using the sidebar

### Quick Analysis

For a quick analysis without the web interface:

```python
from src.data.loader import DataLoader
from src.analysis.analyzer import HappinessAnalyzer

# Load data
loader = DataLoader('data')
whr_data, _ = loader.load_all_data()

# Run analysis
analyzer = HappinessAnalyzer(whr_data)
pearson, spearman = analyzer.calculate_correlations()
print("Top happiness correlations:")
print(pearson.head())
```

## 📈 Usage Guide

### Dashboard Navigation

1. **📊 Executive Summary**: Key metrics and top correlations
2. **🔍 Data Explorer**: Browse raw datasets
3. **📈 Correlation Analysis**: Statistical relationships
4. **🌍 Nordic Comparison**: Finland vs other Nordic countries
5. **💡 Insights & Hypotheses**: Data-driven conclusions
6. **📋 About**: Project information and technical details

### Data Sources

- **World Happiness Report 2024**: 143 countries, 11 happiness factors
- **Food Supply Data (1961-2011)**: 8,925 records of food consumption patterns

## 🧪 Testing

Run the test suite:

```bash
pytest tests/ -v
```

Run with coverage:

```bash
pytest tests/ --cov=src --cov-report=html
```

## 📋 Requirements Verification

### ✅ Core Business Requirements Met

1. **Data Ingestion from 2+ Sources**: WHR2024.csv + EdibleFoods-1961-2011.csv
2. **Data Analysis**: Statistical correlations with significance testing
3. **Data Visualization**: Interactive Plotly charts and graphs
4. **User Interface**: Complete Streamlit web dashboard
5. **Technology Agnostic**: Python-based, modular architecture

### ✅ Technical Acceptance Criteria

- [x] Successfully loads 143 countries from WHR2024.csv
- [x] Processes 8,925 food consumption records
- [x] Calculates correlations for 10+ happiness factors
- [x] Identifies 8 statistically significant factors (p < 0.05)
- [x] Generates 4+ data-driven hypotheses
- [x] Interactive dashboard with 6 analysis sections
- [x] Responsive design for desktop and tablet
- [x] Export functionality for visualizations
- [x] Clean, documented, testable code

## 🎤 Presentation Ready

### Key Talking Points (5-10 minute demo)

1. **Problem**: Understanding Finland's happiness leadership
2. **Solution**: Data-driven analysis of multiple factors
3. **Key Findings**: Social support, GDP, health are top correlators
4. **Nordic Leadership**: Finland ranks #1 among Nordic countries
5. **Actionable Insights**: Policy implications for maintaining happiness

### Demo Flow
1. Show Executive Summary (Finland's #1 ranking)
2. Navigate to Correlation Analysis (top factors)
3. Display Nordic Comparison (Finland's leadership)
4. Present Hypotheses (data-driven conclusions)
5. Highlight technical implementation (dashboard features)

## 🤝 Contributing

This project was built as a hackathon submission using GitHub Copilot for AI pair programming.

### Development Workflow
1. Data loading and validation
2. Statistical analysis implementation
3. Visualization component creation
4. Dashboard development
5. Testing and validation

## 📜 License

This project is for educational and demonstration purposes.

---

**Built with GitHub Copilot 🤖** | **Finnish Happiness Factor Finder** | **Data Analysis Workshop**