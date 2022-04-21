import os
import glob
import shutil
import sys

if os.name == "nt":
    sep = "\\"
else:
    sep = "/"

# True or false, based on if it's the first time being run in the rerun
input = sys.argv[-1]

path = os.getcwd()
if (eval(input)):
    input_path = path + "/OUTPUT/"
    output_path = path + "/Facetalk/Input/"
else:
    output_path = path + "/OUTPUT/"
    input_path = path + "/Facetalk/Input/"

# clear folder
os.chdir(output_path)
output_files = glob.glob(os.path.join(output_path, "*"))
for file in output_files:
    os.remove(file)

# move file
os.chdir(input_path)
file = glob.glob(os.path.join(input_path, "*.xlsx"))[0].split(sep)[-1]
shutil.copyfile(file, output_path + "Output.xlsx")