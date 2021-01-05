#!/bin/bash

sudo apt update && sudo apt upgrade
sudo apt-get install wget build-essential checkinstall
sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev \
    libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev

cd /usr/src

sudo wget https://www.python.org/ftp/python/3.7.1/Python-3.7.1.tgz
sudo tar xzf Python-3.7.1.tgz

cd Python-3.7.1
sudo ./configure --enable-optimizations
sudo make install

sudo python3 -m pip install --upgrade pip

pip --version
pip install virtualenv
