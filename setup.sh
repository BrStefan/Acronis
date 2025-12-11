#!/usr/bin/env bash

set -e  # stop the script on any error

echo "🔧 Setting up project environment..."

# 1. Create virtual environment if not existing
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# 2. Activate venv
echo "📦 Activating virtual environment..."
source venv/bin/activate

# 3. Upgrade pip (recommended)
pip install --upgrade pip

# 4. Install Python dependencies
echo "📦 Installing dependencies from requirements.txt..."
pip install -r requirements.txt

# 5. Install Playwright browsers
echo "🌐 Installing Playwright browsers..."
python -m playwright install

echo "✅ Setup complete!"
echo "------------------------------------------------------"
echo "You can now run tests with:"
echo "source venv/bin/activate"
echo "pytest --html=reports/report.html --self-contained-html"
echo "------------------------------------------------------"
