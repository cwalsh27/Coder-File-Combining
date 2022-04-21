import os
import shutil
import glob

if os.name == "nt":
    sep = "\\"
else:
    sep = "/"

path = os.getcwd()
input_path = path + "/Facetalk/Input/"
output_path = path + "/OUTPUT/"
name_path = path + "/INPUT/"

files = glob.glob(os.path.join(name_path, "*.csv"))
file_name = files[0].split(sep)[-1]
participant = file_name.split("_")[0] + "_" + file_name.split("_")[1]

file = glob.glob(os.path.join(input_path, "*.xlsx"))[0].split(sep)[-1]
os.chdir(input_path)
shutil.copyfile(file, output_path + participant + "_Combined.xlsx")