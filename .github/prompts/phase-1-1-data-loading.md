# Phase 1.1: Project Setup & Data Loading

## Context
You are implementing the Finnish Happiness Factor Finder for the Ministry of Mirth and Merriment. This is Phase 1.1 focusing on project setup and data loading infrastructure.

## Objective
Create a robust data loading system for the existing CSV files in the data/ folder, with proper validation, error handling, and initial exploratory analysis.

## Data Files Available
- `data/WHR2024.csv`: World Happiness Report 2024 (145 countries, happiness scores and factors)
- `data/EdibleFoods-1961-2011.csv`: Food supply data 1961-2011 (8927 records, nutrition and food quantities)

## Tasks
1. Create a Python project structure with proper imports and dependencies
2. Build a DataLoader class that can handle both CSV files with validation
3. Implement data quality checks and summary statistics
4. Create initial exploratory data analysis focused on Finland
5. Set up error handling and logging

## Specific Implementation Requirements
- Use pandas for data manipulation
- Include data validation (missing values, data types, country name consistency)
- Generate summary statistics for both datasets
- Filter and analyze Finland-specific data
- Create country mapping between datasets (handle name variations)
- Implement caching for processed data

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

Please implement this step by step, testing each component as you build it.