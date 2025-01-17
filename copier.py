import os
import glob
import pandas

if os.name == "nt":
    sep = "\\"
else:
    sep = "/"

path = os.getcwd()
input_path = path + "/DatavyuToSupercoder/Output"
output_path = path + "/combining/Input"
files = glob.glob(os.path.join(input_path, "*.xls"))

# gets rid of that weird OUTPUT.DS_S file
real_files = []
for file in files:
    file_name = file.split(sep)[-1]
    if file_name != "OUTPUT_.DS_S.xls":
        real_files.append(file_name)

# gets the relevant parts of the data
os.chdir(input_path)
dataframes = []
coders = []
for file in real_files:
    df = pandas.read_excel(file, skiprows = [0], na_filter = True)
    df = df[["Code", "Onset", "Offset"]]
    dataframes.append(df)
    coder = file.split(".")[0].split("_")[-1]
    coders.append(coder)

# creates the .xlsx files
name = "_".join(real_files[0].split("_")[1:-1])
os.chdir(output_path)
with pandas.ExcelWriter(name+'.xlsx') as writer:  
    dataframes[0].to_excel(writer, sheet_name='Coder 1 ' + coders[0], index = False, header = False)
    dataframes[1].to_excel(writer, sheet_name='Coder 2 ' + coders[1], index = False, header = False)
