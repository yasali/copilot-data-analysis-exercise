"""Test suite for analysis module."""

import pytest
import pandas as pd
import numpy as np
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.data.loader import DataLoader
from src.analysis.analyzer import HappinessAnalyzer


class TestHappinessAnalyzer:
    """Test HappinessAnalyzer class."""
    
    @pytest.fixture
    def analyzer(self):
        """Create analyzer instance with real data."""
        loader = DataLoader("data")
        whr_data = loader.load_whr_data()
        return HappinessAnalyzer(whr_data)
    
    def test_initialization(self, analyzer):
        """Test analyzer initialization."""
        assert analyzer.whr_data is not None
        assert analyzer.country_col is not None
        assert analyzer.score_col is not None
    
    def test_calculate_correlations(self, analyzer):
        """Test correlation calculation."""
        pearson, spearman = analyzer.calculate_correlations()
        assert isinstance(pearson, pd.DataFrame)
        assert isinstance(spearman, pd.DataFrame)
        assert len(pearson) > 0
        assert len(spearman) > 0
    
    def test_get_significant_factors(self, analyzer):
        """Test significant factors extraction."""
        pearson, spearman = analyzer.calculate_correlations()
        significant = analyzer.get_significant_factors(pearson, spearman)
        assert isinstance(significant, dict)
        # Should find at least some significant factors
        assert len(significant) > 0
    
    def test_compare_nordic_countries(self, analyzer):
        """Test Nordic country comparison."""
        comparison = analyzer.compare_nordic_countries()
        assert isinstance(comparison, dict)
        assert len(comparison) > 0
    
    def test_generate_hypotheses(self, analyzer):
        """Test hypothesis generation."""
        pearson, spearman = analyzer.calculate_correlations()
        significant = analyzer.get_significant_factors(pearson, spearman)
        comparisons = analyzer.compare_nordic_countries()
        
        hypotheses = analyzer.generate_hypotheses(significant, comparisons)
        assert isinstance(hypotheses, list)
        assert len(hypotheses) > 0
        
        for hypothesis in hypotheses:
            assert "title" in hypothesis
            assert "description" in hypothesis
            assert "confidence" in hypothesis
    
    def test_get_finland_profile(self, analyzer):
        """Test Finland profile extraction."""
        profile = analyzer.get_finland_profile()
        assert isinstance(profile, dict)
        assert len(profile) > 0
        assert "country" in profile
        assert "all_data" in profile


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
