#!/bin/bash
# Jobbie-Clothes Resume Enhancer Startup Script

echo "🚀 Starting Jobbie-Clothes Resume Enhancer..."
echo "💅 👔 👠 👞 🦺 Welcome to your Job Boutique! 🦺 👞 👠 👔 💅"
echo ""

# Check if virtual environment exists
if [ ! -d "jobbie-env" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv jobbie-env
    echo "✅ Virtual environment created!"
fi

# Activate virtual environment and install dependencies
echo "📥 Installing dependencies..."
source jobbie-env/bin/activate

# Check if packages are installed
if ! python -c "import streamlit, nltk, sklearn" 2>/dev/null; then
    echo "Installing required packages..."
    pip install streamlit nltk scikit-learn python-docx PyPDF2 numpy
fi

echo "✅ All dependencies ready!"
echo ""
echo "🌐 Starting local web application..."
echo "📝 The app will open in your browser automatically"
echo "🔒 Running locally only - no external access"
echo ""

# Start Streamlit with local-only access
streamlit run main.py --server.port 8501 --server.address localhost --browser.serverAddress localhost