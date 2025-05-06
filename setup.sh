#!/bin/bash

# GlamMate Setup Script
echo "Setting up GlamMate development environment..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is not installed. Please install Python 3 and try again."
    exit 1
fi

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    # Windows
    source venv/Scripts/activate
else
    # Linux/Mac
    source venv/bin/activate
fi

# Install dependencies
echo "Installing required libraries..."
pip install -r requirements.txt

echo ""
echo "Setup complete! Virtual environment has been created and dependencies installed."
echo ""
echo "To activate the virtual environment:"
echo "  - On Windows: venv\\Scripts\\activate"
echo "  - On Linux/Mac: source venv/bin/activate"
echo ""
echo "To run the application:"
echo "  - python run.py"
echo ""
echo "Don't forget to create a .env file with your AWS credentials for email notifications."