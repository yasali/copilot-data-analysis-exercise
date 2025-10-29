# Phase 1.2: External Data Integration

## Context
Building on Phase 1.1's data loading foundation, now integrate external data sources to enrich the happiness analysis with additional Finnish statistics.

## Objective
Implement Statistics Finland API integration and create a unified data model that combines happiness data, food consumption data, and external statistics.

## External Data Sources
- **Primary:** Statistics Finland PxWeb API (https://pxdata.stat.fi/PxWeb/api/v1/en/StatFin/)
- **Target Indicators:** GDP per capita, unemployment rate, education statistics
- **Backup:** OECD or World Bank APIs if StatFin unavailable

## Tasks
1. Build API integration module with rate limiting and caching
2. Implement specific data fetchers for key Finnish statistics
3. Create unified data model combining all sources
4. Develop data synchronization and updating mechanisms
5. Perform initial correlation analysis between happiness and new factors

## Specific Implementation Requirements
- Use requests library with proper error handling and retries
- Implement JSON-stat2 data parsing for Statistics Finland
- Create data caching system (JSON files or SQLite)
- Handle API rate limits and connection errors gracefully
- Normalize all data to common time periods and country codes
- Create data validation for API responses

## API Integration Example
```python
# Statistics Finland GDP per capita example
url = "https://pxdata.stat.fi:443/PxWeb/api/v1/en/StatFin/kan/statfin_kan_pxt_132h.px"
query = {
    "query": [
        {"code": "Tiedot", "selection": {"filter": "item", "values": ["B1GMH"]}},
        {"code": "Vuosi", "selection": {"filter": "item", "values": ["2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022"]}}
    ],
    "response": {"format": "json-stat2"}
}
```

## Expected Outputs
- APIClient class with methods for different data sources
- Cached datasets from external APIs in data/ folder
- Unified DataFrame combining happiness, food, and economic data
- Initial correlation matrix between happiness and all available factors
- Data freshness tracking and update mechanisms

## Success Criteria
- [ ] Successfully fetches at least 3 economic indicators for Finland
- [ ] Data caching works properly with refresh capabilities
- [ ] All datasets can be joined on country/year dimensions
- [ ] API errors are handled gracefully with fallback options
- [ ] Initial correlations reveal interesting patterns

## Risk Mitigation
- Implement comprehensive error handling for API failures
- Cache all API responses to avoid repeated requests
- Provide fallback data sources if primary APIs are unavailable
- Include data validation to ensure API response quality

Please implement this with focus on reliability and data quality validation.