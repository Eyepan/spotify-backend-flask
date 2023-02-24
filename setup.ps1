# Check if venv directory exists, and create it if it doesn't
if (-not (Test-Path -Path "./venv" -PathType Container)) {
    echo "Creating virtual environment..."
    python -m venv venv
}

# Activate the virtual environment
& ./venv/Scripts/Activate.ps1

# Install the requirements
echo "Installing requirements..."
pip install -r requirements.txt

echo "Setup complete!"