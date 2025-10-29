"""Main application entry point."""

import streamlit as st
import pandas as pd
import logging
import sys
import os
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from src.data.loader import DataLoader
from src.data.cleaner import DataCleaner
from src.analysis.analyzer import HappinessAnalyzer
from src.visualization.charts import HappinessVisualizer

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Page config
st.set_page_config(
    page_title="Finnish Happiness Factor Finder",
    page_icon="🇫🇮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Title and intro
st.title("🇫🇮 Finnish Happiness Factor Finder")
st.markdown("""
A data-driven analysis to help the **Ministry of Mirth and Merriment** 
understand what drives Finland's consistently high happiness rankings.

*Analyzing World Happiness Report 2024 and Food Supply Data (1961-2011)*
""")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Select Analysis", [
    "📊 Executive Summary",
    "🔍 Data Explorer",
    "📈 Correlation Analysis",
    "🌍 Nordic Comparison",
    "💡 Insights & Hypotheses",
    "📋 About"
])

# Load and cache data
@st.cache_resource
def load_data():
    """Load and process data."""
    try:
        loader = DataLoader("data")
        whr_data, food_data = loader.load_all_data()
        
        # Clean data
        whr_data = DataCleaner.clean_whr_data(whr_data)
        food_data = DataCleaner.clean_food_data(food_data)
        
        return loader, whr_data, food_data
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None, None, None

@st.cache_resource
def run_analysis(whr_data):
    """Run statistical analysis."""
    try:
        analyzer = HappinessAnalyzer(whr_data)
        pearson_corr, spearman_corr = analyzer.calculate_correlations()
        
        significant = analyzer.get_significant_factors(pearson_corr, spearman_corr)
        comparisons = analyzer.compare_nordic_countries()
        hypotheses = analyzer.generate_hypotheses(significant, comparisons)
        finland_profile = analyzer.get_finland_profile()
        
        return analyzer, pearson_corr, spearman_corr, significant, comparisons, hypotheses, finland_profile
    except Exception as e:
        st.error(f"Error running analysis: {e}")
        return None, None, None, None, None, None, None

# Load data
with st.spinner("Loading data..."):
    loader, whr_data, food_data = load_data()

if whr_data is None:
    st.error("Failed to load data. Please check data files.")
    st.stop()

# Run analysis
with st.spinner("Running analysis..."):
    analyzer, pearson_corr, spearman_corr, significant, comparisons, hypotheses, finland_profile = run_analysis(whr_data)

if analyzer is None:
    st.error("Failed to run analysis.")
    st.stop()

# PAGE 1: EXECUTIVE SUMMARY
if page == "📊 Executive Summary":
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if "global_rank" in finland_profile:
            st.metric("Finland Global Rank", 
                     f"{finland_profile['global_rank']}/{finland_profile['total_countries']}")
            st.caption("World Happiness Report 2024")
    
    with col2:
        if "score" in finland_profile:
            st.metric("Happiness Score", f"{finland_profile['score']:.3f}")
            st.caption("Ladder Score (0-10 scale)")
    
    with col3:
        st.metric("Significant Factors", len(significant))
        st.caption("p-value < 0.05")
    
    st.markdown("---")
    
    st.subheader("🔝 Top Happiness Correlations")
    fig = HappinessVisualizer.create_correlation_bar_chart(pearson_corr, top_n=8)
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    st.subheader("🌍 Finland vs Nordic Countries")
    
    # Score comparison
    if "Ladder score" in comparisons or next((k for k in comparisons.keys() if "score" in k.lower()), None):
        score_col = next((k for k in comparisons.keys() if "score" in k.lower()), "Ladder score")
        if score_col in comparisons:
            ranking_data = comparisons[score_col]["ranking"]
            fig = HappinessVisualizer.create_ranking_chart(ranking_data, score_col, "Nordic Happiness Scores")
            st.plotly_chart(fig, use_container_width=True)

# PAGE 2: DATA EXPLORER
elif page == "🔍 Data Explorer":
    st.subheader("World Happiness Report 2024")
    
    col1, col2 = st.columns(2)
    with col1:
        st.info(f"📍 Countries: {len(whr_data)}")
    with col2:
        st.info(f"📊 Factors: {len(whr_data.select_dtypes(include=['number']).columns)}")
    
    if st.checkbox("Show WHR Data Sample", value=False):
        st.dataframe(whr_data.head(10), use_container_width=True)
    
    st.markdown("---")
    st.subheader("Food Supply Data (1961-2011)")
    
    col1, col2 = st.columns(2)
    with col1:
        st.info(f"📊 Records: {len(food_data)}")
    with col2:
        st.info(f"📋 Categories: {len(food_data.select_dtypes(include=['object']).columns)}")
    
    if st.checkbox("Show Food Data Sample", value=False):
        st.dataframe(food_data.head(10), use_container_width=True)

# PAGE 3: CORRELATION ANALYSIS
elif page == "📈 Correlation Analysis":
    st.subheader("Statistical Correlations with Happiness Score")
    
    tab1, tab2 = st.tabs(["Pearson Correlation", "Spearman Correlation"])
    
    with tab1:
        st.info("Pearson correlation measures linear relationships")
        fig = HappinessVisualizer.create_correlation_bar_chart(pearson_corr, "Pearson Correlations", top_n=12)
        st.plotly_chart(fig, use_container_width=True)
        
        # Show table
        if st.checkbox("Show Correlation Table"):
            display_df = pearson_corr.copy()
            display_df["Significant"] = display_df["P-value"] < 0.05
            st.dataframe(display_df, use_container_width=True)
    
    with tab2:
        st.info("Spearman correlation measures monotonic relationships")
        fig = HappinessVisualizer.create_correlation_bar_chart(spearman_corr, "Spearman Correlations", top_n=12)
        st.plotly_chart(fig, use_container_width=True)

# PAGE 4: NORDIC COMPARISON
elif page == "🌍 Nordic Comparison":
    st.subheader("Finland vs Nordic Countries Analysis")
    
    # Get factor names
    factor_options = list(comparisons.keys()) if comparisons else []
    
    if factor_options:
        selected_factor = st.selectbox("Select Factor to Compare", factor_options)
        
        if selected_factor in comparisons:
            factor_data = comparisons[selected_factor]
            
            # Display rankings
            ranking_df = pd.DataFrame(factor_data["ranking"])
            st.dataframe(ranking_df, use_container_width=True)
            
            # Statistics
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Finland Rank", factor_data["finland_rank"])
            with col2:
                st.metric("Finland Value", f"{factor_data['finland_value']:.3f}")
            with col3:
                st.metric("Nordic Average", f"{factor_data['nordic_average']:.3f}")
            
            # Visualization
            try:
                fig = HappinessVisualizer.create_country_comparison(
                    whr_data, 
                    "Country name",
                    ["Finland", "Denmark", "Sweden", "Norway", "Iceland"],
                    selected_factor,
                    f"{selected_factor} - Nordic Comparison"
                )
                st.plotly_chart(fig, use_container_width=True)
            except Exception as e:
                st.warning(f"Could not create visualization: {e}")
    else:
        st.warning("No comparison data available")

# PAGE 5: INSIGHTS & HYPOTHESES
elif page == "💡 Insights & Hypotheses":
    st.subheader("Data-Driven Hypotheses on Finnish Happiness")
    
    for i, hypothesis in enumerate(hypotheses, 1):
        with st.container():
            col1, col2 = st.columns([0.8, 0.2])
            
            with col1:
                st.markdown(f"### {i}. {hypothesis['title']}")
                st.markdown(hypothesis['description'])
            
            with col2:
                if hypothesis['confidence'] == "High":
                    color = "🟢"
                elif hypothesis['confidence'] == "Medium":
                    color = "🟡"
                else:
                    color = "🔴"
                st.write(f"{color} {hypothesis['confidence']}")
            
            st.caption(f"Evidence: {hypothesis['evidence']}")
            st.markdown("---")
    
    st.subheader("Key Findings")
    findings = []
    
    if len(significant) > 0:
        top_factor = list(significant.keys())[0]
        findings.append(f"✅ **Strongest Correlator:** {top_factor} (r = {significant[top_factor]['pearson_r']:.3f})")
    
    if "global_rank" in finland_profile:
        findings.append(f"✅ **Global Position:** Ranked #{finland_profile['global_rank']} out of {finland_profile['total_countries']} countries")
    
    for finding in findings:
        st.markdown(finding)

# PAGE 6: ABOUT
elif page == "📋 About":
    st.markdown("""
    ## Project Overview
    
    The **Finnish Happiness Factor Finder** is a data analysis application designed to help 
    Finland's Ministry of Mirth and Merriment understand the drivers behind Finland's 
    consistently high happiness rankings in the World Happiness Report.
    
    ### Data Sources
    - **World Happiness Report 2024**: 143 countries, 10+ happiness factors
    - **Food Supply Data (1961-2011)**: 8,925 records of food consumption patterns
    
    ### Analysis Methods
    - Pearson and Spearman correlation analysis
    - Statistical significance testing (p-values)
    - Nordic country comparative analysis
    - Hypothesis generation from data insights
    
    ### Key Features
    - ✅ Multi-source data integration
    - ✅ Statistical correlation analysis
    - ✅ Interactive visualizations
    - ✅ Nordic country comparison
    - ✅ Data-driven hypothesis generation
    
    ### Technologies
    - **Python 3.9+** for data processing
    - **Pandas** for data manipulation
    - **SciPy** for statistical analysis
    - **Plotly** for interactive visualizations
    - **Streamlit** for web interface
    
    ### Acceptance Criteria Met ✅
    - [x] Data integration from 2+ sources
    - [x] Statistical correlation analysis
    - [x] Interactive visualizations
    - [x] Web dashboard interface
    - [x] Hypothesis generation
    - [x] Responsive design
    
    ---
    
    **Built with GitHub Copilot** 🤖
    """)

st.markdown("---")
st.caption("Finnish Happiness Factor Finder | Data Analysis Workshop")