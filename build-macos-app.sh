# Install Python 3.10.6 via pyenv
if command -v pyenv >/dev/null 2>&1; then
  pyenv install '3.10.6'
else
  echo "pyenv is not installed"
fi

# Activate Python 3.10.6 in global environment
pyenv global '3.10.6'

# Create and activate Python 3.10.6 virtual environment
python -m venv 'venv'
source 'venv/bin/activate'

# Install dependencies
pip3 install -r requirements.txt
pip3 install pyinstaller

# Delete all .DS_Store
sudo find ./ -name '.DS_Store' -delete

# Build macOS app via pyinstaller
sudo pyinstaller launch.spec
