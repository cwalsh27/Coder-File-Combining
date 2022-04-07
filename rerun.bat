echo off
py rerunner.py True
cd Facetalk
py catcher.py
py facetalk.py
cd ..
py rerunner.py False
pause