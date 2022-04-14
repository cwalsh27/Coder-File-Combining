@echo off
echo Note: this file should only be run once per set of coder files
echo If you want to edit the output and run again, use rerun.bat
echo --------------------------------------------------------------
py clearer.py
if %errorlevel% neq 0 (
	pause
	exit)
py input_mover.py
if %errorlevel% neq 0 (
	pause
	exit)
cd DatavyuToSupercoder
java -jar DatavyuToSupercoder.jar
cd ..
py copier.py
if %errorlevel% neq 0 (
	pause
	exit)
cd Facetalk
py catcher.py
if %errorlevel% neq 0 (
	pause
	exit)
py facetalk.py
if %errorlevel% neq 0 (
	pause
	exit)
cd ..
py output_mover.py
if %errorlevel% neq 0 (
	pause
	exit)
py recode_finder.py
if %errorlevel% neq 0 (
	pause
	exit)
pause