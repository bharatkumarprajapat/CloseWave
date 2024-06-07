#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Define the virtual environment directory
VENV_DIR="venv"

# Check if the virtual environment directory exists
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment..."
    python -m venv $VENV_DIR
fi

# Activate the virtual environment
echo "Activating virtual environment..."
source $VENV_DIR/Scripts/activate

# Upgrade pip
#echo "Upgrading pip..."
#pip install --upgrade pip

# Install dependencies
if [ -f "requirements.txt" ]; then
    echo "Installing dependencies from requirements.txt..."
    pip install -r requirements.txt
else
    echo "requirements.txt not found. Installing Django directly..."
    pip install django
fi

# Verify Django installation
echo "Verifying Django installation..."
python -m django --version

# Additional build commands can go here
# For example, collecting static files for Django
# python manage.py collectstatic --noinput

echo "Build completed."
