# Create and activate Python virtual environment
echo "STEP 1: Create and activate Python virtual environment"
python_version=$(python3 -V 2>&1 | cut -d" " -f2 | cut -d"." -f1-2)

if ! which python3 >/dev/null 2>&1; then
    echo "ERROR: ❌ The 'python3' command not found."
    echo "ERROR: Please check the Python environment configuration."
    exit 1
else
    echo "INFO: The 'python3' command found." 
    if [ "$python_version" == "3.10" ]; then
        echo "INFO: ✅ The current Python version is 3.10"
        python3 -m venv venv
        echo "INFO: ✅ Python virtual enviroment created."
        source venv/bin/activate
        echo "INFO: ✅ Python virtual enviroment activated."
    else
        echo "ERROR: ❌ The current Python version is $python_version but 3.10 is required."
        echo "ERROR: Please switch to Python 3.10 before running this script."
        exit 1
    fi
fi

# Install Python dependencies
echo "STEP 2: Install Python dependencies."
pip3 install -r requirements.txt
pip3 install pyinstaller

# Delete .DS_Store files 
echo "STEP 3: Delete .DS_Store files."
echo "INFO: Permission required to delete .DS_Store files."
sudo find ./ -name '.DS_Store'
sudo find ./ -name '.DS_Store' -delete
echo "INFO: ✅ .DS_Store files all deleted."

# Create packaged app
echo "STEP 4: Create packaged app."
echo "INFO: Use the pyinstaller spec file to bundle the app."
sudo pyinstaller launch.spec
