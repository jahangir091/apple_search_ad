#!/usr/bin/env bash

apt update
apt upgrade
apt install gcc python-software-properties python-support python-dev

cd
cd /home

git clone https://github.com/jahangir091/apple_search_ad.git

cd apple_search_ad

python3 -m venv .venv

source .venv/bin/activaate

pip install -r requrements.txt

