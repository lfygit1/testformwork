#!bin/bash

echo "############################################################"
echo "Installing Requirements..."
echo "############################################################"
echo ""
pip install -r requirements.txt 

echo "############################################################"
echo "Test Starting..."
echo "############################################################"
echo ""
python3 ./RunMain/run.py -m smoke