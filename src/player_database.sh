#!/bin/bash

if command -v python3 &> /dev/null
then 
    echo "Python3 is currently installed on your computer."
else
    echo "Python3 is not installed, you will need to download and install on your computer."

    fi

check_pop() {
    if comand -v pip &> /dev/null; 
    then
        echo "Pip is currently installed on your computer."
    else:
        echo "Pip is not installed, you will need to download and install on your computer."
        fi 
}

if [ -d "venv" ];
then
    echo "Your Virual Environment exists."
else
    echo "Error, Virtual Environment does not exit, please create a virtual enviroment to run this program. Enter into the prompt "python3 -m venv venv" and press enter."
    exit 1
fi


source venv/bin/activate

pip install -r requirements.txt

echo "Your Environment set up is complete, and activated."

pytho3 main.py

deactivate

