"""Data loading module for happiness analysis."""

import os
import logging
from pathlib import Path
from typing import Dict, Tuple, Optional
import pandas as pd
import numpy as np

logger = logging.getLogger(__name__)


class DataLoader:
    """Robust data loader for happiness and food consumption datasets."""
    
    def __init__(self, data_dir: str = "data"):
        """Initialize DataLoader with data directory path.
        
        Args:
            data_dir: Path to data directory containing CSV files
        """
        self.data_dir = Path(data_dir)
        self.whr_path = self.data_dir / "WHR2024.csv"
        self.food_path = self.data_dir / "EdibleFoods-1961-2011.csv"
        
        self.whr_data: Optional[pd.DataFrame] = None
        self.food_data: Optional[pd.DataFrame] = None
        self.finland_whr: Optional[pd.DataFrame] = None
        self.finland_food: Optional[pd.DataFrame] = None
    
    def validate_files(self) -> Tuple[bool, Dict[str, str]]:
        """Validate that required CSV files exist.
        
        Returns:
            Tuple of (is_valid, error_dict)
        """
        errors = {}
        
        if not self.whr_path.exists():
            errors["WHR2024"] = f"File not found: {self.whr_path}"
        
        if not self.food_path.exists():
            errors["EdibleFoods"] = f"File not found: {self.food_path}"
        
        return len(errors) == 0, errors
    
    def load_whr_data(self) -> pd.DataFrame:
        """Load and validate World Happiness Report 2024 data.
        
        Returns:
            Loaded WHR DataFrame
            
        Raises:
            FileNotFoundError: If WHR2024.csv not found
            ValueError: If data validation fails
        """
        if not self.whr_path.exists():
            raise FileNotFoundError(f"WHR2024.csv not found at {self.whr_path}")
        
        logger.info(f"Loading WHR2024.csv from {self.whr_path}")
        self.whr_data = pd.read_csv(self.whr_path)
        
        logger.info(f"Loaded {len(self.whr_data)} countries from WHR2024.csv")
        logger.info(f"Columns: {self.whr_data.columns.tolist()}")
        
        # Validate data
        if self.whr_data.empty:
            raise ValueError("WHR2024.csv is empty")
        
        # Standardize column names
        self.whr_data.columns = self.whr_data.columns.str.strip()
        
        return self.whr_data
    
    def load_food_data(self) -> pd.DataFrame:
        """Load and validate Food Supply data.
        
        Returns:
            Loaded Food data DataFrame
            
        Raises:
            FileNotFoundError: If EdibleFoods CSV not found
            ValueError: If data validation fails
        """
        if not self.food_path.exists():
            raise FileNotFoundError(f"EdibleFoods-1961-2011.csv not found at {self.food_path}")
        
        logger.info(f"Loading EdibleFoods-1961-2011.csv from {self.food_path}")
        self.food_data = pd.read_csv(self.food_path)
        
        logger.info(f"Loaded {len(self.food_data)} records from EdibleFoods")
        logger.info(f"Columns: {self.food_data.columns.tolist()}")
        
        # Validate data
        if self.food_data.empty:
            raise ValueError("EdibleFoods-1961-2011.csv is empty")
        
        # Standardize column names
        self.food_data.columns = self.food_data.columns.str.strip()
        
        return self.food_data
    
    def load_all_data(self) -> Tuple[pd.DataFrame, pd.DataFrame]:
        """Load all required datasets.
        
        Returns:
            Tuple of (WHR DataFrame, Food DataFrame)
        """
        self.load_whr_data()
        self.load_food_data()
        return self.whr_data, self.food_data
    
    def get_finland_data(self) -> Tuple[pd.DataFrame, pd.DataFrame]:
        """Extract Finland-specific data from both datasets.
        
        Returns:
            Tuple of (Finland WHR data, Finland Food data)
            
        Raises:
            ValueError: If Finland not found in datasets
        """
        if self.whr_data is None:
            self.load_whr_data()
        if self.food_data is None:
            self.load_food_data()
        
        # Get Finland data - handle multiple possible country column names
        country_col = self._find_country_column(self.whr_data)
        self.finland_whr = self.whr_data[
            self.whr_data[country_col].str.contains("Finland", case=False, na=False)
        ]
        
        if self.finland_whr.empty:
            raise ValueError("Finland not found in WHR2024.csv")
        
        logger.info(f"Found Finland in WHR data with shape {self.finland_whr.shape}")
        
        # Get Finland food data
        country_col = self._find_country_column(self.food_data)
        self.finland_food = self.food_data[
            self.food_data[country_col].str.contains("Finland", case=False, na=False)
        ]
        
        if self.finland_food.empty:
            logger.warning("Finland not found in food data")
        else:
            logger.info(f"Found Finland in food data with shape {self.finland_food.shape}")
        
        return self.finland_whr, self.finland_food
    
    def get_summary_statistics(self) -> Dict[str, Dict]:
        """Generate summary statistics for all datasets.
        
        Returns:
            Dictionary containing summary statistics
        """
        if self.whr_data is None:
            self.load_whr_data()
        if self.food_data is None:
            self.load_food_data()
        
        summary = {
            "WHR": {
                "rows": len(self.whr_data),
                "columns": len(self.whr_data.columns),
                "countries": self.whr_data.shape[0],
                "missing_values": self.whr_data.isnull().sum().to_dict(),
                "numeric_summary": self.whr_data.describe().to_dict()
            },
            "Food": {
                "rows": len(self.food_data),
                "columns": len(self.food_data.columns),
                "unique_areas": self.food_data[self._find_country_column(self.food_data)].nunique(),
                "year_range": f"{self.food_data[self._find_year_column(self.food_data)].min()}-{self.food_data[self._find_year_column(self.food_data)].max()}",
                "missing_values": self.food_data.isnull().sum().to_dict()
            }
        }
        
        return summary
    
    def get_data_quality_report(self) -> Dict[str, any]:
        """Generate detailed data quality report.
        
        Returns:
            Data quality report dictionary
        """
        if self.whr_data is None:
            self.load_whr_data()
        if self.food_data is None:
            self.load_food_data()
        
        report = {
            "WHR": self._quality_report(self.whr_data),
            "Food": self._quality_report(self.food_data)
        }
        
        return report
    
    @staticmethod
    def _find_country_column(df: pd.DataFrame) -> str:
        """Find the country column name in dataframe.
        
        Args:
            df: DataFrame to search
            
        Returns:
            Column name containing country information
        """
        possible_names = ["Country", "Area", "Country name", "CountryName", "Country_abr"]
        for col in df.columns:
            if col in possible_names or any(name.lower() in col.lower() for name in possible_names):
                return col
        return df.columns[0]  # Fallback to first column
    
    @staticmethod
    def _find_year_column(df: pd.DataFrame) -> str:
        """Find the year column name in dataframe.
        
        Args:
            df: DataFrame to search
            
        Returns:
            Column name containing year information
        """
        possible_names = ["Year", "Year Fao"]
        for col in df.columns:
            if any(name.lower() in col.lower() for name in possible_names):
                return col
        return "Year"  # Default
    
    @staticmethod
    def _quality_report(df: pd.DataFrame) -> Dict:
        """Generate quality report for a dataframe.
        
        Args:
            df: DataFrame to analyze
            
        Returns:
            Quality report dictionary
        """
        missing_pct = (df.isnull().sum() / len(df) * 100).to_dict()
        
        return {
            "total_rows": len(df),
            "total_columns": len(df.columns),
            "memory_usage_mb": df.memory_usage(deep=True).sum() / 1024 ** 2,
            "duplicate_rows": len(df[df.duplicated()]),
            "missing_values_percent": missing_pct,
            "completeness": f"{(1 - df.isnull().sum().sum() / (len(df) * len(df.columns))) * 100:.2f}%"
        }
