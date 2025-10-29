"""Visualization module for interactive charts."""

import logging
from typing import Dict, List, Optional, Tuple
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

logger = logging.getLogger(__name__)


class HappinessVisualizer:
    """Create interactive visualizations for happiness analysis."""
    
    # Color palette
    COLORS = {
        "finland": "#003580",  # Finnish blue
        "nordic": "#E0E0E0",
        "other": "#F0F0F0",
        "primary": "#003580",
        "secondary": "#FF5733"
    }
    
    @staticmethod
    def create_correlation_heatmap(correlations: pd.DataFrame, title: str = "Correlation Heatmap") -> go.Figure:
        """Create correlation heatmap visualization.
        
        Args:
            correlations: DataFrame with correlation values
            title: Chart title
            
        Returns:
            Plotly figure object
        """
        # Create heatmap
        fig = go.Figure(data=go.Heatmap(
            z=correlations.values if hasattr(correlations, 'values') else correlations,
            x=correlations.index if hasattr(correlations, 'index') else range(len(correlations)),
            colorscale="RdBu",
            zmid=0,
            zmin=-1,
            zmax=1,
            colorbar=dict(title="Correlation")
        ))
        
        fig.update_layout(
            title=title,
            xaxis_title="Factors",
            yaxis_title="Factors",
            height=600,
            width=900,
            font=dict(size=10)
        )
        
        return fig
    
    @staticmethod
    def create_correlation_bar_chart(correlations: pd.DataFrame, 
                                     title: str = "Top Happiness Correlations",
                                     top_n: int = 10) -> go.Figure:
        """Create bar chart of top correlations.
        
        Args:
            correlations: DataFrame with correlation values and p-values
            title: Chart title
            top_n: Number of top factors to show
            
        Returns:
            Plotly figure object
        """
        if len(correlations) > top_n:
            top_corrs = correlations.head(top_n)
        else:
            top_corrs = correlations
        
        # Add significance indicator
        colors = ["green" if p < 0.05 else "lightgray" for p in top_corrs["P-value"]]
        
        fig = go.Figure(data=[
            go.Bar(
                x=top_corrs.index,
                y=top_corrs["Correlation"],
                marker_color=colors,
                text=top_corrs["Correlation"].round(3),
                textposition="auto"
            )
        ])
        
        fig.update_layout(
            title=title,
            xaxis_title="Factors",
            yaxis_title="Correlation with Happiness",
            height=500,
            width=900,
            hovermode="x unified",
            showlegend=False
        )
        
        fig.add_hline(y=0, line_dash="dash", line_color="gray")
        
        return fig
    
    @staticmethod
    def create_country_comparison(data: pd.DataFrame, 
                                 country_col: str, 
                                 nordic_countries: List[str],
                                 metric_col: str,
                                 title: str = "Nordic Country Comparison") -> go.Figure:
        """Create bar chart comparing Nordic countries.
        
        Args:
            data: DataFrame with country data
            country_col: Name of country column
            nordic_countries: List of Nordic country names
            metric_col: Column to compare
            title: Chart title
            
        Returns:
            Plotly figure object
        """
        # Filter to Nordic countries
        nordic_data = data[data[country_col].isin(nordic_countries)].copy()
        nordic_data = nordic_data.sort_values(metric_col, ascending=False)
        
        # Highlight Finland
        colors = [HappinessVisualizer.COLORS["finland"] if "Finland" in country 
                 else HappinessVisualizer.COLORS["nordic"] 
                 for country in nordic_data[country_col]]
        
        fig = go.Figure(data=[
            go.Bar(
                x=nordic_data[country_col],
                y=nordic_data[metric_col],
                marker_color=colors,
                text=nordic_data[metric_col].round(3),
                textposition="auto"
            )
        ])
        
        fig.update_layout(
            title=title,
            xaxis_title="Country",
            yaxis_title=metric_col,
            height=500,
            width=700,
            hovermode="x unified",
            showlegend=False
        )
        
        return fig
    
    @staticmethod
    def create_scatter_plot(data: pd.DataFrame, 
                           x_col: str, 
                           y_col: str,
                           country_col: str = "Country name",
                           highlight_countries: Optional[List[str]] = None,
                           title: str = "") -> go.Figure:
        """Create scatter plot showing relationship between two factors.
        
        Args:
            data: DataFrame with data
            x_col: X-axis column
            y_col: Y-axis column
            country_col: Country column name
            highlight_countries: Countries to highlight
            title: Chart title
            
        Returns:
            Plotly figure object
        """
        if not title:
            title = f"{x_col} vs {y_col}"
        
        # Prepare data
        plot_data = data[[country_col, x_col, y_col]].dropna()
        
        # Determine colors
        if highlight_countries:
            colors = [HappinessVisualizer.COLORS["finland"] if any(h in country for h in highlight_countries)
                     else HappinessVisualizer.COLORS["other"]
                     for country in plot_data[country_col]]
        else:
            colors = HappinessVisualizer.COLORS["primary"]
        
        fig = go.Figure(data=[
            go.Scatter(
                x=plot_data[x_col],
                y=plot_data[y_col],
                mode="markers+text",
                marker=dict(
                    size=8,
                    color=colors if isinstance(colors, str) else [colors] if isinstance(colors, str) else colors,
                    opacity=0.7
                ),
                text=plot_data[country_col],
                textposition="top center",
                hovertemplate="<b>%{text}</b><br>" + x_col + ": %{x:.2f}<br>" + y_col + ": %{y:.2f}<extra></extra>"
            )
        ])
        
        fig.update_layout(
            title=title,
            xaxis_title=x_col,
            yaxis_title=y_col,
            height=600,
            width=900,
            hovermode="closest"
        )
        
        return fig
    
    @staticmethod
    def create_ranking_chart(ranking_data: List[Dict], 
                            metric_col: str,
                            title: str = "Country Rankings") -> go.Figure:
        """Create horizontal bar chart for country rankings.
        
        Args:
            ranking_data: List of dicts with country and ranking info
            metric_col: Column name for values
            title: Chart title
            
        Returns:
            Plotly figure object
        """
        df = pd.DataFrame(ranking_data)
        
        # Highlight Finland
        colors = [HappinessVisualizer.COLORS["finland"] if "Finland" in str(country)
                 else HappinessVisualizer.COLORS["nordic"]
                 for country in df.get("Country name", df.columns[0])]
        
        fig = go.Figure(data=[
            go.Bar(
                x=df.get(metric_col, df.iloc[:, -1]),
                y=df.get("Country name", df.iloc[:, 0]),
                orientation="h",
                marker_color=colors,
                text=df.get(metric_col, df.iloc[:, -1]).round(2),
                textposition="auto"
            )
        ])
        
        fig.update_layout(
            title=title,
            xaxis_title=metric_col,
            yaxis_title="Country",
            height=600,
            width=900,
            hovermode="y unified"
        )
        
        return fig
    
    @staticmethod
    def create_multi_factor_radar(country_data: Dict[str, float], 
                                 country_name: str = "Finland",
                                 title: str = "Happiness Factors Profile") -> go.Figure:
        """Create radar chart for multiple factors.
        
        Args:
            country_data: Dictionary of factor: value pairs
            country_name: Name of country
            title: Chart title
            
        Returns:
            Plotly figure object
        """
        fig = go.Figure(data=[
            go.Scatterpolar(
                r=list(country_data.values()),
                theta=list(country_data.keys()),
                fill="toself",
                name=country_name,
                line_color=HappinessVisualizer.COLORS["finland"]
            )
        ])
        
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 1]
                )
            ),
            title=title,
            height=600,
            width=800
        )
        
        return fig
    
    @staticmethod
    def create_time_series(time_data: pd.DataFrame,
                          time_col: str,
                          value_col: str,
                          country_col: str = None,
                          title: str = "Trend Over Time") -> go.Figure:
        """Create time series plot.
        
        Args:
            time_data: DataFrame with time series data
            time_col: Time column name
            value_col: Value column name
            country_col: Optional country column for multi-line
            title: Chart title
            
        Returns:
            Plotly figure object
        """
        fig = go.Figure()
        
        if country_col and country_col in time_data.columns:
            for country in time_data[country_col].unique():
                country_data = time_data[time_data[country_col] == country].sort_values(time_col)
                fig.add_trace(go.Scatter(
                    x=country_data[time_col],
                    y=country_data[value_col],
                    mode="lines+markers",
                    name=str(country),
                    line_color=HappinessVisualizer.COLORS["finland"] if "Finland" in str(country) else None
                ))
        else:
            sorted_data = time_data.sort_values(time_col)
            fig.add_trace(go.Scatter(
                x=sorted_data[time_col],
                y=sorted_data[value_col],
                mode="lines+markers",
                name=value_col,
                line_color=HappinessVisualizer.COLORS["primary"]
            ))
        
        fig.update_layout(
            title=title,
            xaxis_title=time_col,
            yaxis_title=value_col,
            height=500,
            width=900,
            hovermode="x unified"
        )
        
        return fig
