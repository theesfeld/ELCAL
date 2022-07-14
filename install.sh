echo '[ELCAL] Creating virtual environment'
python -m venv .venv
echo '[ELCAL] Activating virtual environment'
source .venv/bin/activate
echo '[ELCAL] Upgrading pip'
pip install --upgrade pip
echo '[ELCAL] Installing requirements'
pip install -r requirements.txt
echo '[ELCAL] Complete.'