#!/bin/bash

# Check if Python3 is installed
command -v python3 >/dev/null 2>&1 || { echo "Python is required but not installed. Aborting."; exit 1; }

# Create and activate a virtual environment
Python3 -m venv myenv

# Check the operating system
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    source myenv/bin/activate
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Linux
    source myenv/bin/activate
elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" || "$OSTYPE" == "cygwin" ]]; then
    # Windows
    source myenv/Scripts/activate
else
    echo "Unsupported operating system: $OSTYPE"
    exit 1
fi


# Install dependencies
pip install -r requirements.txt

# Run the main.py script
Python3 main.py