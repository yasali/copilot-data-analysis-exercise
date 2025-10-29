"""Test suite for data loading module."""

import pytest
import pandas as pd
import numpy as np
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.data.loader import DataLoader
from src.data.cleaner import DataCleaner


class TestDataLoader:
    """Test DataLoader class."""
    
    @pytest.fixture
    def loader(self):
        """Create DataLoader instance."""
        return DataLoader("data")
    
    def test_file_validation(self, loader):
        """Test file validation."""
        is_valid, errors = loader.validate_files()
        assert isinstance(is_valid, bool)
        assert isinstance(errors, dict)
    
    def test_load_whr_data(self, loader):
        """Test loading WHR data."""
        whr_data = loader.load_whr_data()
        assert isinstance(whr_data, pd.DataFrame)
        assert len(whr_data) > 0
        assert not whr_data.empty
    
    def test_load_food_data(self, loader):
        """Test loading food data."""
        food_data = loader.load_food_data()
        assert isinstance(food_data, pd.DataFrame)
        assert len(food_data) > 0
        assert not food_data.empty
    
    def test_load_all_data(self, loader):
        """Test loading all data."""
        whr, food = loader.load_all_data()
        assert isinstance(whr, pd.DataFrame)
        assert isinstance(food, pd.DataFrame)
        assert len(whr) > 0
        assert len(food) > 0
    
    def test_get_finland_data(self, loader):
        """Test getting Finland-specific data."""
        finland_whr, finland_food = loader.get_finland_data()
        assert len(finland_whr) > 0
        assert len(finland_food) >= 0  # May be empty
    
    def test_summary_statistics(self, loader):
        """Test summary statistics generation."""
        loader.load_all_data()
        summary = loader.get_summary_statistics()
        assert "WHR" in summary
        assert "Food" in summary
        assert summary["WHR"]["rows"] > 0


class TestDataCleaner:
    """Test DataCleaner class."""
    
    @pytest.fixture
    def sample_whr_data(self):
        """Create sample WHR data."""
        return pd.DataFrame({
            "Country name": ["Finland", "Denmark", "Sweden"],
            "Ladder score": [7.8, 7.6, 7.5],
            "GDP per capita": [1.2, 1.3, 1.1]
        })
    
    def test_clean_whr_data(self, sample_whr_data):
        """Test WHR data cleaning."""
        cleaned = DataCleaner.clean_whr_data(sample_whr_data)
        assert isinstance(cleaned, pd.DataFrame)
        assert not cleaned.empty
        assert "Country name" in cleaned.columns
    
    def test_handle_missing_values(self, sample_whr_data):
        """Test missing value handling."""
        # Add missing values
        sample_whr_data.loc[0, "GDP per capita"] = np.nan
        
        cleaned = DataCleaner.handle_missing_values(sample_whr_data, strategy="mean")
        assert not cleaned.isnull().any().any()
    
    def test_normalize_data(self, sample_whr_data):
        """Test data normalization."""
        normalized, params = DataCleaner.normalize_data(sample_whr_data)
        
        assert isinstance(normalized, pd.DataFrame)
        assert isinstance(params, dict)
        assert len(params) > 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
