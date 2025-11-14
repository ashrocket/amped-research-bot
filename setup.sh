#!/bin/bash
# Setup script for AMPED Research Bot

echo "🎵 AMPED Research Bot Setup"
echo "=============================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8+ first."
    exit 1
fi

echo "✅ Python 3 found: $(python3 --version)"
echo ""

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt
echo ""

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo "📝 Creating .env file..."
    cp .env.example .env
    echo "✅ .env file created"
    echo ""
    echo "⚠️  IMPORTANT: Edit .env and add your API keys:"
    echo "   - ANTHROPIC_API_KEY (get from https://console.anthropic.com/)"
    echo "   - SERPAPI_KEY (get from https://serpapi.com/)"
    echo ""
else
    echo "✅ .env file already exists"
    echo ""
fi

echo "=============================="
echo "✨ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Edit .env and add your API keys"
echo "2. Run: python amped_bot.py \"Artist Name\""
echo ""
echo "Example:"
echo "  python amped_bot.py \"Jane Remover\""
echo ""
