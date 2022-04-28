# FaceTalk_Combining
Note: pandas, xlrd, and openpyxl are required (install with pip)

Place the two coder .csv files in the INPUT folder\
Edit the config file's 2nd and 4th lines to match the study's information*\
Mac: Type bash run.sh in the console under the folder's directory\
Windows: Run run.bat\
Check the OUTPUT folder\
*Use run.bat/sh only the first time for every set of coder files*\
*Running it again will undo your edits*

If you want to make an edit to the output and then recombine:\
Mac: Type bash rerun.sh in the console under the folder's directory\
Windows: Run rerun.bat\
Check the OUTPUT folder

The program may attempt to fix errors in the coder files, which you can choose to approve\
The files will only be combined if all errors are fixed\
After being combined, the trials with disagreements will be displayed, and you can choose whether or not to add each one to the list of recodes\
Afterwards, a .txt file with the list of recodes will be in the OUTPUT folder

\*FaceTalk has 75 trials\
WLS has 24 trials\
AWL has 96 (V1) or 32 (V2) trials

Disclaimer: I did not make the DatavyuToSupercoder files or most of the code for combining.py

Detailed documentation can be found at https://docs.google.com/document/d/1Jf_brgiBGb9W7MyF3SSILPgEbyqWEapZw3UfH5-P3RQ/edit?usp=sharing
