# Quick Start Guide - Finnish Happiness Factor Finder

## 🎯 Hackathon Mission (Quick Recap)

Build an application that helps Finland's Ministry of Mirth and Merriment understand what drives Finnish happiness by analyzing data and presenting insights.

### Core Requirements (Must Have)
1. ✅ Load data from 2+ sources
2. ✅ Analyze correlations with happiness
3. ✅ Create visualizations showing relationships
4. ✅ Present findings in accessible format (dashboard/report)
5. ✅ Explain hypotheses in 5-10 minute presentation

---

## 🛠️ CHOSEN TECHNOLOGY STACK

```
Backend:       Python 3.9+
Data:          pandas, numpy, scipy, scikit-learn
Analysis:      scipy.stats for correlations
Visualization: Plotly (interactive charts)
Dashboard:     Streamlit (web interface)
Testing:       pytest
```

**Why Streamlit for Hackathon?**
- ⚡ Fastest development (minimal boilerplate)
- 🎨 Beautiful UI without any CSS/JavaScript
- 🔄 Hot reload for instant feedback
- 📊 Native support for pandas & plotting
- 🤖 Excellent Copilot code generation

---

## 📅 TIMELINE (Realistic 6-8 hour hackathon)

| Phase | Time | Tasks |
|-------|------|-------|
| Setup & Data Loading | 1 hour | Python environment, load CSVs, API setup |
| Analysis | 2 hours | Correlations, statistical testing, insights |
| Visualization | 1.5 hours | Create interactive charts, comparisons |
| Dashboard | 1.5 hours | Streamlit UI, integration, styling |
| Polish & Testing | 1 hour | Bug fixes, testing, presentation prep |
| **TOTAL** | **6-8 hours** | |

---

## 🚀 GETTING STARTED (Right Now)

### Step 1: Clone & Setup (10 minutes)
```bash
# Clone repository
git clone https://github.com/yasali/copilot-data-analysis-exercise.git
cd copilot-data-analysis-exercise

# Create virtual environment
python -m venv venv
source venv/bin/activate  # macOS/Linux
# OR
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements-hackathon.txt
```

### Step 2: Verify Data Files (5 minutes)
```bash
# Check data directory
ls -la data/

# Should see:
# - WHR2024.csv (145 countries, happiness data)
# - EdibleFoods-1961-2011.csv (food consumption data)
```

### Step 3: Start with Exploration (30 minutes)
```bash
# Option A: Use Jupyter for exploration
jupyter notebook notebooks/exploration.ipynb

# Option B: Direct Python script
python src/data/loader.py
```

---

## 📚 IMPLEMENTATION APPROACH

### Phase 1: Data Loading (Using Enhanced Copilot Prompts)

**In GitHub Copilot Chat, use this prompt:**
```
"Create a modular, reusable DataLoader class in Python using pandas 
that loads WHR2024.csv and EdibleFoods-1961-2011.csv with comprehensive 
validation, type annotations, error handling, and caching for repeated use. 
Follow clean code principles with well-documented methods that can be 
easily extended for new data sources."
```

**Expected Output:**
- DataLoader class with methods for both CSV files
- Data validation checking for completeness
- Caching to avoid reloading
- Error handling for missing files

---

### Phase 2: Data Analysis (Using Copilot)

**Prompt:**
```
"Build a modular statistical analysis class for happiness factors using 
pandas, numpy, and scipy that calculates Pearson and Spearman correlations 
with p-values, identifies the strongest correlations for Finland, and 
compares Finland against Nordic countries. Include type annotations, 
comprehensive docstrings, and proper error handling following clean code 
principles."
```

**Expected Output:**
- Statistical correlations with significance testing
- Country comparison capabilities
- Insights about what correlates with Finnish happiness

---

### Phase 3: Visualization (Using Copilot)

**Prompt:**
```
"Create reusable plotly visualization functions for happiness data analysis 
including correlation heatmaps, country comparison bar charts, and scatter 
plots with trend lines. Ensure consistent styling with Finland highlighted 
in all charts, interactive features like hover tooltips, and export 
capabilities. Follow clean code principles with type annotations and 
comprehensive docstrings."
```

**Expected Output:**
- Interactive correlation heatmap
- Country comparison charts
- Scatter plots for factor relationships
- All with professional styling

---

### Phase 4: Dashboard (Using Copilot)

**Prompt:**
```
"Create a complete Streamlit web application for Finnish happiness analysis 
with: (1) Executive summary page with key findings, (2) Correlation analysis 
with interactive charts, (3) Country comparison page, (4) Data explorer with 
raw data viewing, following modern UI/UX best practices with caching, 
responsive design, and professional styling. Use modular code with clear 
separation between data processing and visualization logic."
```

**Expected Output:**
- Fully functional Streamlit app
- Multi-page navigation
- Interactive visualizations
- Professional appearance

---

## 💻 RUNNING THE APPLICATION

### During Development
```bash
# Terminal 1: Run Streamlit app with hot reload
streamlit run app.py

# Opens automatically at http://localhost:8501
# Changes to code update in real-time (no refresh needed!)
```

### Testing
```bash
# Run all tests
pytest tests/

# Run with coverage
pytest tests/ --cov=src/

# Run specific test file
pytest tests/test_analysis.py -v
```

### Code Quality
```bash
# Format code
black src/

# Check linting
flake8 src/

# Type checking (optional)
mypy src/
```

---

## 📊 EXPECTED ANALYSIS RESULTS

### What You Should Find

1. **Top Happiness Correlations for Finland:**
   - Social support (likely strong)
   - Healthy life expectancy
   - Freedom to make life choices
   - GDP per capita

2. **Finland vs Nordic Countries:**
   - How does Finland rank against Denmark, Sweden, Norway, Iceland?
   - Which factors give Finland an advantage?

3. **Food & Happiness Relationship:**
   - Any trends in food consumption (1961-2011) that correlate with happiness?
   - How has Finnish diet evolved?

4. **Key Hypotheses to Present:**
   - "Finland's strong social support system contributes to happiness"
   - "Nordic countries share similar happiness factors"
   - "Economic stability correlates with life satisfaction"
   - etc.

---

## 📝 PROJECT STRUCTURE (After Setup)

```
finnish-happiness-finder/
├── app.py                          # Streamlit main app
├── requirements-hackathon.txt      # Dependencies
│
├── src/
│   ├── data/
│   │   ├── loader.py              # CSV/API loading
│   │   └── cleaner.py             # Data cleaning
│   ├── analysis/
│   │   ├── correlations.py        # Statistical analysis
│   │   └── comparisons.py         # Country comparisons
│   └── visualization/
│       └── charts.py              # Plotly functions
│
├── data/
│   ├── WHR2024.csv                # Happiness data
│   └── EdibleFoods-1961-2011.csv   # Food data
│
├── notebooks/
│   └── exploration.ipynb          # EDA notebook
│
└── .github/prompts/               # All planning docs
    ├── technical-stack.md
    ├── requirements-verification.md
    ├── workshop-guide.md
    └── ... (other guides)
```

---

## 🎓 USING THE COPILOT PROMPTS

### Pre-Made Prompts Available
See `.github/prompts/` for:
- `enhanced-copilot-prompts.md` - Optimized prompts with keywords
- `phase-1-1-data-loading.md` - Data loading specifics
- `phase-2-1-statistical-analysis.md` - Analysis specifics
- `phase-3-1-visualizations.md` - Visualization specifics
- `phase-3-2-dashboard.md` - Dashboard specifics

### Quick Prompt Strategy
1. Start with data loading prompt
2. Test locally (quick 2-5 min verification)
3. Move to analysis prompt
4. Test results with sample data
5. Move to visualization
6. Integrate into dashboard
7. Iterate and refine

---

## ✅ VALIDATION CHECKLIST

Before final presentation, verify:

### Functionality
- [ ] Application loads WHR2024.csv without errors
- [ ] Application loads EdibleFoods data without errors
- [ ] Statistical correlations computed for Finland
- [ ] Visualizations display correctly
- [ ] Dashboard navigation works smoothly

### Analysis Quality
- [ ] Identified 5+ factors correlating with happiness
- [ ] Statistical significance reported (p-values < 0.05)
- [ ] Finland compared against Nordic countries
- [ ] Insights are specific to Finland (not generic)

### Presentation Readiness
- [ ] 5-10 minute presentation prepared
- [ ] Key visualizations identified and highlighted
- [ ] 3-5 hypotheses documented with evidence
- [ ] Team can explain the technical approach

### Code Quality
- [ ] Tests run without errors (pytest tests/)
- [ ] Code is formatted (black src/)
- [ ] No lint errors (flake8 src/)
- [ ] Functions have docstrings

---

## 🚨 COMMON ISSUES & SOLUTIONS

### Issue: "ModuleNotFoundError: No module named 'streamlit'"
**Solution:** Install requirements
```bash
pip install -r requirements-hackathon.txt
```

### Issue: "FileNotFoundError: data/WHR2024.csv not found"
**Solution:** Verify file paths (case-sensitive on Linux/Mac)
```bash
ls -la data/  # Check files exist
```

### Issue: "Port 8501 already in use"
**Solution:** Use different port
```bash
streamlit run app.py --server.port 8502
```

### Issue: "Analysis is running too slow"
**Solution:** Add caching to data loading
```python
@st.cache_data
def load_data():
    return pd.read_csv('data/WHR2024.csv')
```

### Issue: "Correlation analysis not working"
**Solution:** Check for missing values
```python
df = df.dropna()  # Remove rows with NaN
# OR
df = df.fillna(df.mean())  # Impute missing values
```

---

## 📞 GETTING HELP

1. **Check `.github/prompts/` directory** for detailed guides
2. **Use enhanced Copilot prompts** with specific keywords
3. **Reference `requirements-verification.md`** for scope clarity
4. **Check `technical-stack.md`** for architecture questions
5. **Use Copilot for code** - it's your pair programmer!

---

## 🎯 SUCCESS = COMPLETE MVP IN TIME FOR DEMO

### Minimal Working Example (Hours 1-3)
```python
# Load data
df = pd.read_csv('data/WHR2024.csv')
finland = df[df['Country name'] == 'Finland']

# Basic stats
print(f"Finland happiness: {finland['Ladder score'].values[0]}")
print(f"Finland rank: {len(df[df['Ladder score'] > finland['Ladder score'].values[0]]) + 1}")

# Simple correlation
correlation = df.corr()
print(correlation['Ladder score'].sort_values(ascending=False))
```

### Full Implementation (Hours 3-6)
- Add multiple data sources
- Statistical significance testing
- Interactive Streamlit dashboard
- Professional visualizations

### Polish & Presentation (Hour 6-8)
- Bug fixes and optimization
- Documentation
- Presentation slides
- Practice 5-minute demo

---

## 🎉 YOU'RE READY!

Everything you need is prepared:
- ✅ Project requirements clearly understood
- ✅ Technical stack optimized for hackathon
- ✅ Copilot prompts ready to use
- ✅ Data files pre-loaded
- ✅ Timeline realistic (6-8 hours)
- ✅ Success criteria defined

**Now: Clone the repo, start with Phase 1, and use Copilot to build!**

Questions? Check `.github/prompts/README.md` for the complete prompt library.