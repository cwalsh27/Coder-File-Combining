#!/bin/bash
echo Note: this file should only be run once per set of coder files
echo If you want to edit the output and run again, use rerun.bat
echo --------------------------------------------------------------
python3 clearer.py 
if [ $? -ne 0 ]; then exit 0; fi 
python3 input_mover.py 
if [ $? -ne 0 ]; then exit 0; fi 
cd DatavyuToSupercoder 
java -jar $(pwd)/DatavyuToSupercoder.jar 
cd .. 
python3 copier.py 
if [ $? -ne 0 ]; then exit 0; fi 
cd combining 
python3 catcher.py 
if [ $? -ne 0 ] 
then
	echo 
	cd .. 
	python3 output_mover.py 
	exit 0 
fi 
python3 combining.py 
if [ $? -ne 0 ]; then exit 0; fi 
cd .. 
python3 output_mover.py 
if [ $? -ne 0 ]; then exit 0; fi 
python3 recode_finder.py 
if [ $? -ne 0 ]; then exit 0; fi 