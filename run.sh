#!bin/bash

nginx_host=$1

echo "############################################################"
echo "Installing Requirements..."
echo "############################################################"
echo "pip install -r ./requirements.txt --break-system-packages"
pip install -r ./requirements.txt --break-system-packages


echo "############################################################"
echo "Build Argument"
echo "############################################################"
echo ""
echo "nginx_host: $nginx_host"
python3 ./ExtTools/buildargument.py --nginx_host $nginx_host



echo "############################################################"
echo "Test Starting..."
echo "############################################################"
echo ""

# python3 ./RunMain/run.py -m smoke 

