import os
import glob

path = os.getcwd()

dts_input_path = path + "/DatavyuToSuperCoder/Input/"
os.chdir(dts_input_path)
dts_input_files = glob.glob(os.path.join(dts_input_path, "*.csv"))
for file in dts_input_files:
    os.remove(file)
    
dts_output_path = path + "/DatavyuToSuperCoder/Output/"
os.chdir(dts_output_path)
dts_output_files = glob.glob(os.path.join(dts_output_path, "*.xls"))
for file in dts_output_files:
    os.remove(file)
    
ft_path = path + "/Facetalk/Input/"
os.chdir(ft_path)
ft_files = glob.glob(os.path.join(ft_path, "*.xlsx"))
for file in ft_files:
    os.remove(file)
    
output_path = path + "/OUTPUT/"
os.chdir(output_path)
output_files = glob.glob(os.path.join(output_path, "*.xlsx"))
for file in output_files:
    os.remove(file)