"""Data cleaning and preprocessing module."""

import logging
from typing import Dict, List, Optional, Tuple
import pandas as pd
import numpy as np

logger = logging.getLogger(__name__)


class DataCleaner:
    """Clean and preprocess happiness and food data."""
    
    # Standard country name mappings for consistency
    COUNTRY_MAPPING = {
        "Czechoslovakia": "Czech Republic",
        "USSR": "Russia",
        "Republic of Ireland": "Ireland"
    }
    
    @staticmethod
    def clean_whr_data(df: pd.DataFrame) -> pd.DataFrame:
        """Clean World Happiness Report data.
        
        Args:
            df: Raw WHR DataFrame
            
        Returns:
            Cleaned WHR DataFrame
        """
        df = df.copy()
        
        # Standardize country names
        if "Country name" in df.columns:
            df["Country name"] = df["Country name"].str.strip()
            df["Country name"] = df["Country name"].replace(DataCleaner.COUNTRY_MAPPING)
        
        # Remove duplicates keeping first occurrence
        df = df.drop_duplicates(subset=["Country name"], keep="first")
        
        # Convert numeric columns
        numeric_cols = df.select_dtypes(include=["object"]).columns
        for col in numeric_cols:
            try:
                df[col] = pd.to_numeric(df[col], errors="coerce")
            except Exception:
                pass
        
        logger.info(f"Cleaned WHR data: {len(df)} rows")
        return df
    
    @staticmethod
    def clean_food_data(df: pd.DataFrame) -> pd.DataFrame:
        """Clean food supply data.
        
        Args:
            df: Raw food data DataFrame
            
        Returns:
            Cleaned food DataFrame
        """
        df = df.copy()
        
        # Find and standardize country/area column
        area_col = None
        for col in df.columns:
            if "Area" in col or "Country" in col.lower():
                area_col = col
                break
        
        if area_col:
            df[area_col] = df[area_col].str.strip()
        
        # Remove rows with missing critical values
        critical_cols = [col for col in df.columns if "Value" in col or "value" in col]
        if critical_cols:
            df = df.dropna(subset=critical_cols, how="all")
        
        # Convert Value column to numeric
        if "Value" in df.columns:
            df["Value"] = pd.to_numeric(df["Value"], errors="coerce")
        
        logger.info(f"Cleaned food data: {len(df)} rows")
        return df
    
    @staticmethod
    def handle_missing_values(df: pd.DataFrame, strategy: str = "mean") -> pd.DataFrame:
        """Handle missing values in dataset.
        
        Args:
            df: DataFrame with missing values
            strategy: Strategy for handling - "mean", "median", "drop", "forward_fill"
            
        Returns:
            DataFrame with handled missing values
        """
        df = df.copy()
        
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        
        if strategy == "mean":
            df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
        elif strategy == "median":
            df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())
        elif strategy == "drop":
            df = df.dropna()
        elif strategy == "forward_fill":
            df = df.fillna(method="ffill").fillna(method="bfill")
        
        logger.info(f"Handled missing values with {strategy} strategy")
        return df
    
    @staticmethod
    def normalize_data(df: pd.DataFrame, columns: Optional[List[str]] = None) -> Tuple[pd.DataFrame, Dict]:
        """Normalize numeric columns to 0-1 range.
        
        Args:
            df: DataFrame to normalize
            columns: List of columns to normalize (None = all numeric)
            
        Returns:
            Tuple of (normalized DataFrame, scaling parameters)
        """
        df = df.copy()
        params = {}
        
        numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        if columns:
            numeric_cols = [c for c in columns if c in numeric_cols]
        
        for col in numeric_cols:
            min_val = df[col].min()
            max_val = df[col].max()
            params[col] = {"min": min_val, "max": max_val}
            
            if max_val > min_val:
                df[col] = (df[col] - min_val) / (max_val - min_val)
            else:
                df[col] = 0
        
        logger.info(f"Normalized {len(numeric_cols)} numeric columns")
        return df, params
    
    @staticmethod
    def filter_by_country(df: pd.DataFrame, countries: List[str], 
                         country_col: str = "Country name") -> pd.DataFrame:
        """Filter dataframe to specific countries.
        
        Args:
            df: Input DataFrame
            countries: List of country names to keep
            country_col: Name of country column
            
        Returns:
            Filtered DataFrame
        """
        if country_col not in df.columns:
            logger.warning(f"Country column {country_col} not found")
            return df
        
        df = df[df[country_col].isin(countries)].copy()
        logger.info(f"Filtered to {len(df)} rows for {len(countries)} countries")
        return df
    
    @staticmethod
    def get_correlation_ready_data(whr_df: pd.DataFrame, 
                                   food_df: Optional[pd.DataFrame] = None,
                                   year: Optional[int] = None) -> Tuple[pd.DataFrame, List[str]]:
        """Prepare data for correlation analysis.
        
        Args:
            whr_df: Cleaned WHR data
            food_df: Optional cleaned food data
            year: Optional year to filter food data
            
        Returns:
            Tuple of (correlation-ready DataFrame, list of factor columns)
        """
        df = whr_df.copy()
        
        # Identify happiness factors
        happiness_factors = [col for col in df.columns if col not in 
                            ["Country name", "Year", "Regional indicator"]]
        
        # Add food data if available
        if food_df is not None and len(food_df) > 0:
            if year:
                year_col = None
                for col in food_df.columns:
                    if "Year" in col:
                        year_col = col
                        break
                if year_col:
                    food_df = food_df[food_df[year_col] == year]
            
            # Aggregate food data
            area_col = None
            for col in food_df.columns:
                if "Area" in col or "Country" in col.lower():
                    area_col = col
                    break
            
            if area_col:
                value_col = None
                for col in food_df.columns:
                    if "Value" in col:
                        value_col = col
                        break
                
                if value_col and area_col:
                    food_agg = food_df.groupby(area_col)[value_col].mean().reset_index()
                    food_agg.columns = [area_col, "AvgFoodSupply"]
        
        return df, happiness_factors
