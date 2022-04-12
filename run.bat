@echo off
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
pause