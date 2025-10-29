# Phase 1.1: Project Setup & Data Loading

## Context
You are implementing the Finnish Happiness Factor Finder for the Ministry of Mirth and Merriment. This is Phase 1.1 focusing on project setup and data loading infrastructure.

## Objective
Create a robust data loading system for the existing CSV files in the data/ folder, with proper validation, error handling, and initial exploratory analysis.

## Data Files Available
- `data/WHR2024.csv`: World Happiness Report 2024 (145 countries, happiness scores and factors)
- `data/EdibleFoods-1961-2011.csv`: Food supply data 1961-2011 (8927 records, nutrition and food quantities)

## Enhanced Copilot Tasks
1. **Generate a scalable Python project structure** with proper imports, dependencies, and modern architectural best practices following clean code principles
2. **Build a modular, reusable DataLoader class** that handles both CSV files with comprehensive validation, type annotations, and well-documented methods
3. **Implement robust data quality checks** and summary statistics using pandas best practices with error handling and extensible design
4. **Create comprehensive exploratory data analysis** focused on Finland using state-of-the-art data science patterns with clear separation of concerns
5. **Set up production-ready error handling** and logging with scalable architecture that can be easily extended

## Enhanced Implementation Requirements
- **Use pandas with modern best practices** for data manipulation, including type annotations and comprehensive docstrings
- **Include scalable data validation** (missing values, data types, country name consistency) with modular, reusable validation functions
- **Generate comprehensive summary statistics** for both datasets using clean code principles and extensible statistical analysis
- **Filter and analyze Finland-specific data** with well-structured functions that follow separation of concerns
- **Create robust country mapping** between datasets with error handling and configurable name variations management
- **Implement intelligent caching** for processed data using state-of-the-art caching patterns and performance optimization

## Expected Outputs
- Working DataLoader class with methods for both files
- Data quality report showing completeness and issues
- Summary statistics for Finland across both datasets
- Initial insights about Finland's happiness ranking and food patterns
- Clean, well-documented code following Python best practices

## Success Criteria
- [ ] Both CSV files load successfully with proper data types
- [ ] Finland data is correctly identified and extracted
- [ ] Data quality issues are identified and reported
- [ ] Code includes comprehensive error handling
- [ ] Initial analysis provides meaningful insights about Finnish data

## Copilot Optimization Keywords
When implementing, use these specific phrases to get the best results from GitHub Copilot:
- "Generate modular, reusable functions with type annotations"
- "Create scalable data processing pipeline following clean code principles"
- "Implement comprehensive error handling with state-of-the-art patterns"
- "Build extensible validation system with well-documented methods"
- "Design maintainable architecture with separation of concerns"

Please implement this step by step, testing each component as you build it, following modern Python best practices and clean code principles.