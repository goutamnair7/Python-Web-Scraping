#!/bin/bash

if [ -d ./"`date +%d-%m-%Y`" ];
then
rm -r ./`date +%d-%m-%Y`;
mkdir ./`date +%d-%m-%Y`;
else
mkdir ./`date +%d-%m-%Y`;
fi;

python get100stockinfo.py
