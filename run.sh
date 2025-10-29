#!/bin/bash

# Finnish Happiness Factor Finder - Run Script
# Starts the Streamlit dashboard application

echo "🇫🇮 Starting Finnish Happiness Factor Finder..."
echo "=========================================="

# Check if virtual environment exists
if [ ! -d ".venv" ]; then
    echo "❌ Virtual environment not found. Please run setup first:"
    echo "   python -m venv .venv"
    echo "   source .venv/bin/activate"
    echo "   pip install -r requirements.txt"
    exit 1
fi

# Activate virtual environment
source .venv/bin/activate

# Check if required packages are installed
if ! python -c "import streamlit" 2>/dev/null; then
    echo "❌ Dependencies not installed. Installing now..."
    pip install -r requirements.txt
fi

# Start the application
echo "✅ Starting Streamlit dashboard..."
echo "🌐 Application will open at: http://localhost:8501"
echo ""
echo "Press Ctrl+C to stop the application"
echo ""

streamlit run app.py --server.headless true