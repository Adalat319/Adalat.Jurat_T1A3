#!/bin/bash

# Check if Python is installed
command -v python >/dev/null 2>&1 || { echo "Python is required but not installed. Aborting."; exit 1; }

# Create and activate a virtual environment
python -m venv myenv
source myenv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the main.py script
python main.py
