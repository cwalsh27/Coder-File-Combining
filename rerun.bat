echo off
py rerunner.py True
cd Facetalk
py facetalk.py
cd ..
py rerunner.py False
pause