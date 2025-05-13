# Project: The Finnish Happiness Factor Finder

**Mission:** To boldly go where many analysts have gone before, but this time with AI pair programmers!

## 1. Introduction: The Conundrum of Contentment

Finland, despite its reputation for reserved people, challenging climate, and a language structure that baffles linguists, consistently ranks as the happiest country in the world according to the World Happiness Report.

The newly formed (and slightly bewildered) **Ministry of Mirth and Merriment (MMM)** finds this delightful but needs actionable data. Is it the saunas? The surprisingly high coffee consumption? The efficient social systems? The sheer number of heavy metal bands per capita? Or something else entirely?

Your team's objective is to develop an application that fetches, analyzes, and visualizes data to help the MMM understand the potential drivers behind Finland's top happiness ranking. We need data-driven hypotheses, presented clearly!

## 2. Business Requirements

The application developed by your team must meet the following core requirements:

1.  **Data Ingestion/Fetching:**
    * The application must be capable of fetching or ingesting data from **at least two** different relevant external sources (see suggested sources below).
    * The process should be repeatable (i.e., running the app again should fetch fresh data if available, or use cached data appropriately).

2.  **Data Analysis:**
    * The application must perform analysis on the collected data to identify potential correlations between various societal, economic, environmental, or cultural factors and happiness indicators for Finland (and potentially comparison countries).
    * The team should define which factors they are investigating based on the available data.

3.  **Data Visualization:**
    * The application must generate clear and meaningful visualizations (e.g., charts, graphs, dashboards) that present the findings of the analysis.
    * These visualizations should help the MMM quickly grasp the potential relationships your team has uncovered. What factors seem to correlate strongly with Finland's happiness scores?

4.  **User Interface / Output:**
    * The results (key findings, visualizations) should be presented in an accessible format. This could be:
        * A simple web interface/dashboard.
        * Generated report files (e.g., HTML, PDF) containing text and charts.
        * Well-formatted console output with saved image files for charts.
    * The choice of interface/output is up to the team.

5.  **Technology Agnostic:**
    * The implementation technology (programming language, frameworks, data stores, visualization libraries) is entirely **up to the team**. Use what you know, or use this as a chance to learn something new with Copilot's help!

## 3. Expected Outcome & Deliverables

At the end of the workshop exercise, each team is expected to:

1.  Have a functional application that meets the business requirements outlined above.
2.  Present a brief (5-10 minutes) demonstration including:
    * A walkthrough of the application's features (data fetching, analysis logic, visualizations).
    * The key visualizations produced by the application.
    * The team's primary hypotheses regarding the factors contributing to Finnish happiness, based on their analysis and visualization of the data. Remember, correlation does not equal causation, but it's a great starting point for hypotheses!

## 4. Potential Data Sources (Accelerated Start!)

To get you analyzing faster, here are recommended sources with *specific suggestions* for relevant data points or tables. Focus on grabbing data for Finland, and maybe 1-2 comparison countries if you like. **Start with 1-2 indicators from 2 different sources.**

1.  **World Happiness Report Data:**
    * **What:** The primary source for happiness rankings and correlated factors.
    * **Get This:** Download the main data file (usually Excel or CSV) for the **latest available year** from the official [World Happiness Report](https://worldhappiness.report/) site (look for data appendices/downloads) or a reputable source like Kaggle (Example: [https://www.kaggle.com/datasets/ajaypalsinghlo/world-happiness-report-2024](https://www.kaggle.com/datasets/ajaypalsinghlo/world-happiness-report-2024) - check relevance).
    * **Key Columns to Use:**
        * `Country name`
        * `Year`
        * `Ladder score` (or similar main Happiness Score)
        * `Logged GDP per capita`
        * `Social support`
        * `Healthy life expectancy`
        * `Freedom to make life choices`
        * `Generosity`
        * `Perceptions of corruption`
    * **Format:** CSV or Excel.
    * **Registration/API Key Needed?:** Generally **No** for direct downloads. Kaggle API needs setup if used.
    * **Bootstrap:** This gives you the core happiness score and its commonly associated factors directly.

2.  **Statistics Finland (Tilastokeskus):**
    * **What:** Official Finnish statistics. Rich but complex. Use the PxWeb interface or the API.
    * **Get This:**
        * When you visit the [StatFin Database access page](https://pxdata.stat.fi/PxWeb/pxweb/en/StatFin/), you can browse and select from a wide range of statistics (e.g., GDP, unemployment, life expectancy, education, etc.).
        * **Important:** You cannot simply download the data as CSV/Excel directly for all tables. Instead, you need to fetch the data programmatically using the PxWeb API.
        * Each table provides an "API query" example (see the "Show API query" or similar button). You must use this to fetch your selected data.
    * **How:**
        1. Go to the [StatFin Database access page](https://pxdata.stat.fi/PxWeb/pxweb/en/StatFin/).
        2. Browse by topic or search using keywords/table codes (e.g., GDP, unemployment rate, life expectancy, education).
        3. Select your desired table and filter for the years, variables, and breakdowns you want.
        4. Click the "Show API query" button to get the API endpoint and example JSON query for your selection.
        5. Fetch the data using a script or your app. For example, you can use Python:

           ```python
           import requests
           import json
           import os

           url = "https://pxdata.stat.fi:443/PxWeb/api/v1/en/StatFin/eot/statfin_eot_pxt_11ty.px"
           query = {
               "query": [
                   {
                       "code": "Ikä",
                       "selection": {
                           "filter": "item",
                           "values": ["SSS", "16-24", "25-34", "35-49", "50-64", "65-74", "75-84", "85-"]
                       }
                   }
               ],
               "response": {"format": "json-stat2"}
           }

           response = requests.post(url, json=query)
           data = response.json()
           # Save fetched data into the 'data' folder for consistency
           os.makedirs('data', exist_ok=True)
           with open('data/output.json', 'w') as f:
               json.dump(data, f)
           ```

        6. You can then convert the JSON-stat data to CSV using Python (see the main README for an example with `pyjstat` and `pandas`).
        7. **Recommendation:** Always save fetched data into a dedicated `data` folder in your project. This keeps raw and processed datasets organized and makes your workflow reproducible.
    * **Registration/API Key Needed?:** Generally **No**.
    * **Bootstrap:** Pick *one* specific indicator (like unemployment rate or GDP per capita) to start. You must fetch the data yourself using the API as described above.

3.  **Statistics Finland: Education by Gender, Age, and Field (PxWeb API)**
    * **What:** Official Finnish statistics on education, broken down by gender, age, and field of education.
    * **Source (UI):** [https://pxdata.stat.fi/PxWeb/pxweb/fi/StatFin/StatFin__vkour/statfin_vkour_pxt_12br.px/](https://pxdata.stat.fi/PxWeb/pxweb/fi/StatFin/StatFin__vkour/statfin_vkour_pxt_12br.px/)
    * **How to Fetch (Python Example):**

      ```python
      import requests
      import json
      import os

      url = "https://pxdata.stat.fi:443/PxWeb/api/v1/fi/StatFin/vkour/statfin_vkour_pxt_12br.px"
      query = {
          "query": [
              {"code": "Alue", "selection": {"filter": "item", "values": ["SSS"]}},
              {"code": "Ikä", "selection": {"filter": "item", "values": [
                  "SSS", "15-19", "20-24", "25-29", "30-34", "35-39", "40-44", "45-49", "50-54", "55-59", "60-64", "65-69", "70-74", "75-79", "80-"
              ]}},
              {"code": "Sukupuoli", "selection": {"filter": "item", "values": ["SSS", "1", "2"]}},
              {"code": "Koulutusala", "selection": {"filter": "item", "values": [
                  "SSS", "00T10", "00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "SSSX00T10", "X"
              ]}}
          ],
          "response": {"format": "json-stat2"}
      }

      response = requests.post(url, json=query)
      data = response.json()
      os.makedirs('data', exist_ok=True)
      with open('data/statfin_vkour_pxt_12br.json', 'w') as f:
          json.dump(data, f)
      print("Saved to data/statfin_vkour_pxt_12br.json")
      ```

    * **Registration/API Key Needed?:** No
    * **Bootstrap:** This fetches the full education by gender, age, and field dataset for Finland. You can further process or convert the JSON-stat2 data to CSV for analysis.
    * **Troubleshooting:** If the code does not work, visit the [source UI](https://pxdata.stat.fi/PxWeb/pxweb/fi/StatFin/StatFin__vkour/statfin_vkour_pxt_12br.px/) to check the correct API endpoint and JSON schema for your query.

4.  **Food Supply Data (via Kaggle - FAOSTAT source):**
    * **What:** Data on food supply quantity (kg/capita/year) and nutritional values (kcal/capita/day, protein, fat) for various food items across many countries. Originally from the UN Food and Agriculture Organization (FAOSTAT).
    * **Get This:** Download the CSV from Kaggle: [https://www.kaggle.com/datasets/aliesmaeilpoor/ediblefoods-1961-to-2011](https://www.kaggle.com/datasets/aliesmaeilpoor/ediblefoods-1961-to-2011)
    * **Key Columns/Data to Use:** Filter by `Area` (e.g., 'Finland'). Select relevant `Item`s (e.g., 'Fish, Seafood', 'Fruits - Excluding Wine', 'Vegetables', 'Animal fats', 'Milk - Excluding Butter') and `Element`s (e.g., `Food supply quantity (kg/capita/yr)` or `Food supply (kcal/capita/day)`).
    * **Format:** CSV.
    * **Registration/API Key Needed?:** **Yes**, Kaggle account required to download via website UI. Kaggle API setup needed for programmatic download.
    * **Bootstrap:** Be aware the data **ends in 2011**. Filter for 'Finland' and start by analyzing the trend for *one or two specific food items* (like Fish or Fruits) or a broad `Element` like total `Food supply (kcal/capita/day)`. Compare its trend over the available years (1961-2011) with happiness data for overlapping years if possible.

**Creative / Humorous Data Ideas (Optional Bonus):**

* These require significant data hunting/cleaning (e.g., scraping Metal Archives for bands, finding coffee import stats, estimating sauna numbers). **Avoid these initially** if the goal is a fast start on analysis. Tackle only if you finish early and want a challenge. *Registration/API keys might be needed for specific niche sources or scraping might be involved (check terms!)*.

By providing these more direct pointers, participants should be able to acquire initial datasets much faster and move on to the core task of analyzing and visualizing with Copilot's help.

* **Sauna Density:** Might require combining data from Statistics Finland (building types) with regional data, or creative estimation. *Registration Needs:* Depends on source; official stats likely open, niche sources might vary.
* **Coffee Consumption:** Look for data from trade organizations (like the International Coffee Organization) or market research reports. *Registration Needs:* Trade orgs *might* be open; market research sites (e.g., Statista) often require registration or subscription for full data access.
* **Heavy Metal Bands per Capita:** Could involve scraping data from sources like Wikipedia lists or dedicated music encyclopedias (e.g., Metal Archives) and combining with population data. *Registration Needs:* Scraping usually doesn't require keys (but **always check Terms of Service and `robots.txt`**). If an official API exists for a music database, it *might* require registration/keys.

Choose sources that seem accessible and relevant to the factors your team wants to investigate! Good luck!

## 5. How to Use This Repo (Workshop Instructions)

1.  Clone this repository.
2.  Create your project files (code, notebooks, etc.) within your cloned repository.
3.  Collaborate with your team using standard Git practices.
4.  **Leverage GitHub Copilot!** Ask it to help you:
    * Write boilerplate code for fetching data (e.g., using `requests`, `pandas`).
    * Clean and process data.
    * Perform statistical analysis (e.g., correlations using `pandas`, `numpy`, `scipy`).
    * Generate plotting code (e.g., using `matplotlib`, `seaborn`, `plotly`).
    * Build a simple web interface (e.g., using Flask, Streamlit, Dash).
    * Explain code snippets or suggest alternative approaches.
5.  Commit your code and prepare for your presentation.