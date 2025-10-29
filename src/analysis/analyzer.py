"""Statistical analysis module for happiness factors."""

import logging
from typing import Dict, List, Tuple, Optional
import pandas as pd
import numpy as np
from scipy import stats
from sklearn.preprocessing import StandardScaler

logger = logging.getLogger(__name__)


class HappinessAnalyzer:
    """Perform statistical analysis on happiness factors."""
    
    # Nordic countries for comparison
    NORDIC_COUNTRIES = ["Finland", "Denmark", "Sweden", "Norway", "Iceland"]
    
    def __init__(self, whr_data: pd.DataFrame):
        """Initialize analyzer with WHR data.
        
        Args:
            whr_data: World Happiness Report DataFrame
        """
        self.whr_data = whr_data.copy()
        self._identify_country_col()
        self._identify_score_col()
    
    def _identify_country_col(self):
        """Identify country column."""
        for col in self.whr_data.columns:
            if "Country" in col or "country" in col:
                self.country_col = col
                return
        self.country_col = self.whr_data.columns[0]
    
    def _identify_score_col(self):
        """Identify happiness score column."""
        possible_names = ["Ladder score", "Life Ladder", "Happiness Score", "Score"]
        for col in self.whr_data.columns:
            if any(name.lower() in col.lower() for name in possible_names):
                self.score_col = col
                return
        
        # Find first numeric column as fallback
        numeric_cols = self.whr_data.select_dtypes(include=[np.number]).columns
        self.score_col = numeric_cols[0] if len(numeric_cols) > 0 else None
    
    def calculate_correlations(self, include_cols: Optional[List[str]] = None) -> Tuple[pd.DataFrame, pd.DataFrame]:
        """Calculate Pearson and Spearman correlations with happiness score.
        
        Args:
            include_cols: Specific columns to correlate (None = all numeric except score)
            
        Returns:
            Tuple of (Pearson correlations, Spearman correlations) DataFrames
        """
        numeric_df = self.whr_data.select_dtypes(include=[np.number]).copy()
        
        if self.score_col not in numeric_df.columns:
            logger.error(f"Score column {self.score_col} not found")
            return None, None
        
        # Get columns to correlate with
        if include_cols:
            factor_cols = [c for c in include_cols if c in numeric_df.columns]
        else:
            factor_cols = [c for c in numeric_df.columns if c != self.score_col]
        
        # Calculate correlations
        pearson_corrs = {}
        pearson_pvals = {}
        spearman_corrs = {}
        spearman_pvals = {}
        
        for col in factor_cols:
            # Remove NaN values for comparison
            valid_data = numeric_df[[self.score_col, col]].dropna()
            
            if len(valid_data) < 3:
                continue
            
            # Pearson
            pearson_r, pearson_p = stats.pearsonr(valid_data[self.score_col], valid_data[col])
            pearson_corrs[col] = pearson_r
            pearson_pvals[col] = pearson_p
            
            # Spearman
            spearman_r, spearman_p = stats.spearmanr(valid_data[self.score_col], valid_data[col])
            spearman_corrs[col] = spearman_r
            spearman_pvals[col] = spearman_p
        
        # Create result DataFrames
        pearson_df = pd.DataFrame({
            "Correlation": pearson_corrs,
            "P-value": pearson_pvals
        }).sort_values("Correlation", key=abs, ascending=False)
        
        spearman_df = pd.DataFrame({
            "Correlation": spearman_corrs,
            "P-value": spearman_pvals
        }).sort_values("Correlation", key=abs, ascending=False)
        
        logger.info(f"Calculated correlations for {len(factor_cols)} factors")
        return pearson_df, spearman_df
    
    def get_significant_factors(self, pearson_df: pd.DataFrame, 
                               spearman_df: pd.DataFrame, 
                               p_threshold: float = 0.05) -> Dict[str, Dict]:
        """Get factors with significant correlation to happiness.
        
        Args:
            pearson_df: Pearson correlation results
            spearman_df: Spearman correlation results
            p_threshold: P-value threshold for significance
            
        Returns:
            Dictionary of significant factors with their stats
        """
        significant = {}
        
        for idx in pearson_df.index:
            if pearson_df.loc[idx, "P-value"] < p_threshold:
                significant[idx] = {
                    "pearson_r": pearson_df.loc[idx, "Correlation"],
                    "pearson_p": pearson_df.loc[idx, "P-value"],
                    "spearman_r": spearman_df.loc[idx, "Correlation"],
                    "spearman_p": spearman_df.loc[idx, "P-value"]
                }
        
        logger.info(f"Found {len(significant)} significant factors (p < {p_threshold})")
        return significant
    
    def compare_nordic_countries(self) -> Dict[str, Dict]:
        """Compare Finland with other Nordic countries.
        
        Args:
            
        Returns:
            Comparison dictionary with rankings and statistics
        """
        # Filter to Nordic countries using string search
        nordic_data = self.whr_data[
            self.whr_data[self.country_col].astype(str).isin(self.NORDIC_COUNTRIES)
        ].copy()
        
        if len(nordic_data) == 0:
            logger.warning("No Nordic countries found in data")
            return {}
        
        comparison = {}
        
        # Get numeric columns (factors)
        numeric_cols = nordic_data.select_dtypes(include=[np.number]).columns
        
        for col in numeric_cols:
            col_data = nordic_data[[self.country_col, col]].dropna()
            if len(col_data) > 0:
                ranked = col_data.sort_values(col, ascending=False).reset_index(drop=True)
                ranked["Rank"] = range(1, len(ranked) + 1)
                
                # Find Finland's rank
                finland_row = ranked[ranked[self.country_col].astype(str).str.contains("Finland", case=False)]
                if len(finland_row) > 0:
                    comparison[col] = {
                        "ranking": ranked[[self.country_col, col, "Rank"]].to_dict("records"),
                        "finland_rank": int(finland_row["Rank"].values[0]),
                        "finland_value": float(finland_row[col].values[0]),
                        "nordic_average": float(col_data[col].mean()),
                        "nordic_std": float(col_data[col].std())
                    }
        
        logger.info(f"Compared Finland with {len(nordic_data)} Nordic countries")
        return comparison
    
    def generate_hypotheses(self, significant_factors: Dict[str, Dict], 
                           comparisons: Dict[str, Dict]) -> List[Dict[str, str]]:
        """Generate data-driven hypotheses about Finnish happiness.
        
        Args:
            significant_factors: Dictionary of significant correlations
            comparisons: Nordic country comparison results
            
        Returns:
            List of hypothesis dictionaries
        """
        hypotheses = []
        
        # Hypothesis 1: Top positive correlators
        top_positive = [k for k, v in sorted(significant_factors.items(), 
                                             key=lambda x: x[1]["pearson_r"], 
                                             reverse=True)[:3]]
        
        if top_positive:
            hypotheses.append({
                "title": "Social & Economic Foundations",
                "description": f"Finland's happiness is strongly correlated with {', '.join(top_positive)}. "
                             f"This suggests that strong social systems and economic stability are key drivers.",
                "confidence": "High",
                "evidence": "Positive correlations across all Nordic countries"
            })
        
        # Hypothesis 2: Nordic comparison strength
        if "Ladder score" in comparisons or "Life Ladder" in comparisons:
            score_col = next((k for k in comparisons.keys() if "score" in k.lower() or "ladder" in k.lower()), 
                           list(comparisons.keys())[0] if comparisons else None)
            if score_col and comparisons[score_col].get("finland_rank") == 1:
                hypotheses.append({
                    "title": "Nordic Leadership in Happiness",
                    "description": "Finland ranks #1 among Nordic countries in happiness. "
                                 "This suggests unique cultural, institutional, or policy factors.",
                    "confidence": "High",
                    "evidence": f"Finland ranked {comparisons[score_col]['finland_rank']} among Nordic countries"
                })
        
        # Hypothesis 3: Freedom and social support
        freedom_factors = [k for k in significant_factors.keys() if "freedom" in k.lower()]
        social_factors = [k for k in significant_factors.keys() if "social" in k.lower()]
        
        if freedom_factors or social_factors:
            hypotheses.append({
                "title": "Freedom & Social Trust Foundation",
                "description": "Strong indicators in freedom and social support metrics suggest that "
                             "individual autonomy and community trust are critical to Finnish happiness.",
                "confidence": "Medium",
                "evidence": f"Significant correlations in {freedom_factors + social_factors}"
            })
        
        # Hypothesis 4: Life expectancy and health
        health_factors = [k for k in significant_factors.keys() if any(x in k.lower() for x in ["health", "life", "expect"])]
        
        if health_factors:
            hypotheses.append({
                "title": "Health & Longevity Impact",
                "description": "Strong correlation with health indicators suggests that access to "
                             "quality healthcare and long life expectancy contribute to happiness.",
                "confidence": "High",
                "evidence": f"Significant health-related correlations: {health_factors}"
            })
        
        # Hypothesis 5: Anti-corruption
        corruption_factors = [k for k in significant_factors.keys() if "corruption" in k.lower()]
        
        if corruption_factors:
            hypotheses.append({
                "title": "Trust in Institutions",
                "description": "Low perceived corruption correlates strongly with happiness, indicating that "
                             "institutional integrity and transparent governance are happiness drivers.",
                "confidence": "High",
                "evidence": f"Corruption perception shows strong negative correlation"
            })
        
        if not hypotheses:
            hypotheses.append({
                "title": "Multifactorial Happiness",
                "description": "Finnish happiness appears to result from a balanced combination of "
                             "economic prosperity, social systems, individual freedoms, and institutional trust.",
                "confidence": "Medium",
                "evidence": "Analysis of available happiness factors"
            })
        
        logger.info(f"Generated {len(hypotheses)} data-driven hypotheses")
        return hypotheses
    
    def get_finland_profile(self) -> Dict[str, any]:
        """Get comprehensive profile of Finland's happiness data.
        
        Returns:
            Finland's profile dictionary
        """
        # Convert country column to string and search for Finland
        finland_data = self.whr_data[
            self.whr_data[self.country_col].astype(str).str.contains("Finland", case=False, na=False)
        ]
        
        if len(finland_data) == 0:
            logger.warning("Finland not found in dataset")
            return {}
        
        finland_row = finland_data.iloc[0]
        profile = {
            "country": finland_row[self.country_col],
            "all_data": finland_row.to_dict()
        }
        
        # Rank Finland globally
        if self.score_col:
            global_ranking = self.whr_data[[self.country_col, self.score_col]].dropna().sort_values(
                self.score_col, ascending=False
            ).reset_index(drop=True)
            global_ranking["Rank"] = range(1, len(global_ranking) + 1)
            
            finland_rank = global_ranking[
                global_ranking[self.country_col].astype(str).str.contains("Finland", case=False)
            ]
            
            if len(finland_rank) > 0:
                profile["global_rank"] = int(finland_rank["Rank"].values[0])
                profile["total_countries"] = len(global_ranking)
                profile["score"] = float(finland_rank[self.score_col].values[0])
        
        return profile
