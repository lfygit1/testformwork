#!bin/bash

echo "############################################################"
echo "Installing Requirements..."
echo "############################################################"
echo "pip install -r ./requirements.txt --break-system-packages"
pip install -r ./requirements.txt --break-system-packages

echo "############################################################"
echo "Test Starting..."
echo "############################################################"
echo ""
python3 ./RunMain/run.py -m smoke