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
    * **What:** Official Finnish statistics. Rich but complex. Use the PxWeb interface.
    * **Get This (Examples - use keywords/codes in StatFin PxWeb):**
        * **GDP:** Navigate **National Accounts** -> **Annual National Accounts** -> **Gross domestic product (GDP) and gross national income (GNI)**. Look for annual GDP per capita tables (e.g., keyword `GDP`, `per capita`. Table `kans_v` is often relevant).
        * **Unemployment:** Navigate **Labour market** -> **Employment and unemployment** -> **Labour force survey**. Look for the unemployment rate table (e.g., keyword `unemployment rate`, table `tyonv` or `tyti` series). Select annual averages.
        * **Life Expectancy:** Navigate **Population** -> **Deaths** -> **Life expectancy**. Look for table by sex (e.g., keyword `life expectancy`, table `kuol_le`).
        * **Education:** Navigate **Education** -> **Educational structure of population**. Look for tables on population by level of education completed (e.g., keyword `level of education`, table `vaerak_koul`).
    * **How:** Go to the [StatFin Database access page](https://stat.fi/en/statistics-and-data/statfin-database) and use the PxWeb interface. Browse by topic or search using keywords/table codes. Filter data for desired years and download as CSV/Excel.
    * **Registration/API Key Needed?:** Generally **No**.
    * **Bootstrap:** Pick *one* specific indicator (like unemployment rate or GDP per capita) to start.

3.  **World Bank Open Data:**
    * **What:** Global indicators, good for basic comparisons.
    * **Get This (Example Indicators - search by name or code):**
        * `GDP per capita (current US$)`: Code `NY.GDP.PCAP.CD`
        * `Life expectancy at birth, total (years)`: Code `SP.DYN.LE00.IN`
        * `Unemployment, total (% of total labor force) (modeled ILO estimate)`: Code `SL.UEM.TOTL.ZS`
        * `Individuals using the Internet (% of population)`: Code `IT.NET.USER.ZS`
    * **How:** Go to [https://data.worldbank.org/](https://data.worldbank.org/). Search for these indicators. Select Finland (and maybe Sweden/Norway/Denmark for comparison). View/download the time series data as CSV/Excel.
    * **Registration/API Key Needed?:** Generally **No**.
    * **Bootstrap:** Grab the time series for *one or two* of these indicators for Finland.

4.  **OECD Data:**
    * **What:** Data for OECD countries, strong on well-being metrics.
    * **Get This (Example Datasets/Indicators):**
        * **Better Life Index:** Explore this dataset directly on the OECD site for comparative scores on dimensions like `Life Satisfaction`, `Work-Life Balance`, `Community`, `Health Status`. ([https://www.oecdbetterlifeindex.org/](https://www.oecdbetterlifeindex.org/) often has interactive views and underlying data).
        * **Average Wages:** Search for `Average wages` (e.g., indicator `AV_AN_WAGE`) on the main portal [https://data.oecd.org/](https://data.oecd.org/).
        * **Social Expenditure:** Search for `Social expenditure` datasets (often under `Social Protection and Well-being`). Look for % of GDP.
    * **How:** Use the OECD data portal search or browse themes like `Well-being`. Focus on indicators available for Finland. Download relevant tables/indicators (CSV/Excel).
    * **Registration/API Key Needed?:** Generally **No**.
    * **Bootstrap:** The Better Life Index scores are a great comparative starting point if available easily. Otherwise, pick one indicator like average wages.

5.  **Eurostat:**
    * **What:** EU statistics office. Good for EU comparisons, potentially complex navigation.
    * **Get This (Example Table Codes - use in database search/navigation):**
        * **Overall life satisfaction:** Code `ilc_pw01` (under Population and social conditions -> Living conditions -> Quality of life)
        * **GDP per capita (PPS):** Code `nama_10_pc` (under Economy and finance -> National accounts -> GDP and main components)
        * **Healthy life years at birth:** Code `hlth_hlye` (under Population and social conditions -> Health -> Mortality and life expectancy)
        * **Persons at risk of poverty or social exclusion:** Code `ilc_peps01` (under Population and social conditions -> Living conditions -> Poverty and social exclusion)
    * **How:** Go to the [Eurostat Database](https://ec.europa.eu/eurostat/web/main/data/database). Use the search or navigate 'Database by themes'. Use table codes to find data. Filter by country (FI), time, and download (CSV/Excel often best).
    * **Registration/API Key Needed?:** Generally **No**.
    * **Bootstrap:** Pick *one* table (like life satisfaction or healthy life years) to download for Finland and maybe neighbours.

**Creative / Humorous Data Ideas (Harder to Source Reliably):**

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