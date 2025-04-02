#!/bin/bash

echo "📦 Creating virtual environment..."
python3 -m venv venv

echo "✅ Virtual environment created at ./venv"

echo "🐍 Activating virtual environment..."
source venv/bin/activate

echo "📃 Installing requirements..."
pip install -r requirements.txt

echo "🧹 Setting up .gitignore..."
echo "venv/" >> .gitignore
echo "__pycache__/" >> .gitignore
echo "*.pyc" >> .gitignore

echo "🎉 All done! You're ready to go."
echo "Run: source venv/bin/activate to activate your environment anytime."