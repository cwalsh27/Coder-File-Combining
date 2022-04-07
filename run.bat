echo off
py clearer.py
py input_mover.py
cd DatavyuToSupercoder
java -jar DatavyuToSupercoder.jar
cd ..
py copier.py
cd Facetalk
py catcher.py
py facetalk.py
cd ..
py output_mover.py
pause