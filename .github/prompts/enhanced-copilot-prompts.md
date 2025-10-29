# Enhanced Copilot Workshop Prompts for Finnish Happiness Factor Finder

## Copilot-Optimized Prompts with Keywords & Principles

These prompts are specifically designed to leverage GitHub Copilot's strengths by using concrete, actionable language with architectural keywords that encourage scalable, clean code solutions.

## General Setup & Architecture

### 🏗️ Project Structure Prompt
```
Generate a scalable project structure for a Python data analysis app that follows clean code principles and modern architectural best practices. The project should analyze Finnish happiness factors using CSV data, external APIs, and statistical analysis. Include separation of concerns for data loading, processing, analysis, and visualization with proper dependency management and configuration handling.
```

### 📁 Folder Layout Prompt  
```
Suggest an initial folder and file layout for a data science project analyzing happiness factors, separating concerns like data loading, API integration, statistical processing, visualization, and web interface. Follow state-of-the-art Python project structure with proper module organization and scalable architecture.
```

## Data Infrastructure & Processing

### 🔄 Modular Data Loading Prompt
```
Write boilerplate code to load CSV files (WHR2024.csv, EdibleFoods data) using pandas, ensuring the design is modular, reusable, and follows clean code principles. Include comprehensive error handling, data validation, type annotations, and well-documented functions that can be easily extended for new data sources.
```

### 🔌 API Integration Prompt
```
Create a scalable API client for Statistics Finland PxWeb API using requests in Python, ensuring the design is modular and reusable. Include rate limiting, caching, error handling with exponential backoff, and clean function definitions with type annotations. Structure the code for easy extension to other APIs.
```

### 🧹 Data Cleaning Pipeline Prompt
```
Create a comprehensive data cleaning pipeline using pandas that handles missing values, outliers, country name standardization, and type conversions for happiness and food consumption datasets. Make sure functions are well-structured, documented with docstrings, and follow separation of concerns principles for scalability.
```

## Statistical Analysis & Insights

### 📊 Correlation Analysis Prompt
```
Show how to compute correlations between happiness factors and various indicators using pandas, numpy, and scipy, with clean function definitions and type annotations. Include statistical significance testing, multiple comparison corrections, and structure the code so it can be easily extended for new statistical tests and analysis methods.
```

### 🔬 Hypothesis Testing Prompt
```
Generate code for statistical hypothesis testing using scipy to analyze Finnish happiness factors, and structure the code so it can be easily extended for new tests. Include proper documentation, error handling, and follow state-of-the-art statistical analysis patterns with clear separation of data preparation and analysis logic.
```

### 🎯 Insight Generation Prompt
```
Create a modular insight generation system that converts statistical findings into actionable hypotheses about Finnish happiness. Use clean code principles with well-documented functions, type annotations, and scalable architecture that can handle different types of statistical inputs and generate formatted business insights.
```

## Visualization & Dashboard

### 📈 Reusable Plotting Prompt
```
Write plotting code using plotly to visualize relationships between happiness variables and Finnish factors. Structure the code so plots can be reused and customized, with clear separation of data preparation and visualization logic. Include functions for correlation heatmaps, country comparisons, and time series plots with consistent styling and Finland highlighting.
```

### 🎨 Chart Library Prompt
```
Create reusable functions for generating different plot types (correlation heatmaps, bar charts, radar charts, time series) using plotly, ensuring separation of data preparation and visualization logic. Follow clean code principles with type annotations, docstrings, and modular design that supports easy customization and extension.
```

### 🌐 Interactive Dashboard Prompt
```
Generate a scalable Streamlit app to interactively explore Finnish happiness analysis results, using modular code and best practices for UI/UX. Include navigation, filtering, export functionality, and follow state-of-the-art dashboard architecture with clear separation between data processing, visualization, and user interface components.
```

### ⚡ Web Interface Prompt
```
Write a Flask app skeleton for serving Finnish happiness analysis results, following clean code principles with separate routes, services, and templates. Include proper error handling, configuration management, and scalable architecture that can be easily extended for additional analysis features and deployment scenarios.
```

## Code Quality & Collaboration

### 🔍 Code Review Prompt
```
Review this Finnish happiness analysis code snippet and suggest improvements to follow clean code principles and state-of-the-art patterns. Focus on modularity, reusability, error handling, documentation, and architectural improvements that enhance maintainability and scalability for a data analysis application.
```

### ♻️ Refactoring Prompt
```
Refactor this function/class for Finnish happiness data processing to improve readability, scalability, and adherence to clean code principles. Include proper type annotations, comprehensive docstrings, error handling, and suggest architectural improvements that follow separation of concerns.
```

### 📚 Documentation Prompt
```
Generate comprehensive documentation for this Finnish happiness analysis module, including docstrings with examples, type annotations, usage patterns, and architectural explanations. Follow state-of-the-art documentation practices that help other developers understand and extend the codebase.
```

## Testing & Quality Assurance

### 🧪 Testing Framework Prompt
```
Create a comprehensive pytest testing suite for Finnish happiness data analysis components, following clean code principles and state-of-the-art testing patterns. Include unit tests, integration tests, fixture management, and parametrized tests that ensure data quality, statistical accuracy, and system reliability.
```

### ⚡ Performance Optimization Prompt
```
Analyze and optimize this Finnish happiness data processing code for performance and scalability. Suggest improvements using pandas best practices, caching strategies, and architectural patterns that handle large datasets efficiently while maintaining clean, readable code structure.
```

## Advanced Analysis & Extensions

### 🔮 Predictive Analysis Prompt
```
Extend the Finnish happiness analysis with predictive modeling capabilities using scikit-learn, ensuring the design is modular, scalable, and follows machine learning best practices. Include proper model validation, feature engineering, and clean separation between data preparation, model training, and prediction logic.
```

### 🌍 Multi-Country Extension Prompt
```
Refactor the happiness analysis system to support multiple countries beyond Finland, using scalable architecture and clean code principles. Include configuration-driven country selection, comparative analysis capabilities, and modular design that can easily accommodate new countries and analysis dimensions.
```

## Copilot Optimization Keywords

### 🎯 Essential Keywords to Include
- **Architecture:** "modular", "scalable", "reusable", "extensible"
- **Code Quality:** "clean code principles", "best practices", "well-documented"
- **Technical:** "type annotations", "error handling", "separation of concerns"
- **Modern Patterns:** "state-of-the-art", "modern architectural", "follows standards"

### 💡 Prompting Best Practices
1. **Be Technology-Specific:** Always mention exact libraries (pandas, plotly, streamlit)
2. **Request Structure:** Ask for modular, reusable components
3. **Emphasize Quality:** Include "clean code", "best practices", "well-documented"
4. **Think Scalability:** Use "scalable", "extensible", "maintainable"
5. **Request Examples:** Ask for docstrings, type annotations, usage examples

## Sample Enhanced Prompt Usage

### Before (Generic):
```
"Create a function to load CSV data"
```

### After (Copilot-Optimized):
```
"Create a modular, reusable function to load Finnish happiness CSV data using pandas, following clean code principles with comprehensive error handling, type annotations, and well-documented docstrings. Structure the code for easy extension to additional data sources and include data validation that follows state-of-the-art practices."
```

## Integration with Existing Phases

Each phase prompt should be enhanced with these keywords:

- **Phase 1:** Add "modular data loading", "scalable architecture", "clean error handling"
- **Phase 2:** Include "statistical best practices", "extensible analysis framework"  
- **Phase 3:** Emphasize "reusable visualization components", "modern UI patterns"
- **Phase 4:** Focus on "comprehensive testing", "production-ready quality"

This enhanced approach will generate significantly better code from Copilot while maintaining the comprehensive structure of our existing implementation plan.