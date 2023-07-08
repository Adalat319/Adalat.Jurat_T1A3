#!/bin/bash

# Check if Python3 is installed
command -v python3 >/dev/null 2>&1 || { echo "Python is required but not installed. Aborting."; exit 1; }

# Create and activate a virtual environment
python3 -m venv myenv

# Activate the virtual environment
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" || "$OSTYPE" == "cygwin" ]]; then
    # Windows
    source myenv/Scripts/activate
else
    # macOS or Linux
    source myenv/bin/activate
fi

# Install dependencies
pip3 install -r requirements.txt

# Run the main.py script
python3 main.py
