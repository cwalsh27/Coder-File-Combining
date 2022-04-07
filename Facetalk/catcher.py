import os
import glob
from openpyxl import *
from openpyxl.styles import Color, PatternFill, Font, Border
from openpyxl.styles import colors

path = os.getcwd() + "/Input/"

file = glob.glob(os.path.join(path, "*xlsx"))
file_name = file[0].split("\\")[-1]

os.chdir(path)

num_trials = 75

wb = load_workbook(file_name)

for sheet in wb:
    b = 0
    s = 0
    num_rows = 0
    b_fill = PatternFill(start_color = 'FFD3AA',
                              end_color = 'FFD3AA',
                              fill_type = 'solid')
    if sheet.title == 'AVERAGES ACROSS CODERS':
        continue
    # makes sure the number of trials is correct
    for row in sheet:
        if row[0].value == "B":
            b += 1
            row[0].fill = b_fill
            sheet["M" + str(num_rows + 1)] = b
            sheet["M" + str(num_rows + 1)].fill = b_fill
        if row[0].value == "S":
            s += 1
        num_rows += 1
    if b != num_trials or s != num_trials:
        print(sheet.title + " has incorrect number of trials.\n" + str(b) + " B\n" + str(s) + " S\n" + "Should have " + str(num_trials) + " of each.")
        exit(1)
    # makes sure every S has a B following it (except for the last one)
    for i in range(0, num_rows):
        row = list(sheet)[i]
        if list(row)[0].value == "S" and i != num_rows - 1:
            if list(sheet)[i+1][0].value != "B":
                print(sheet.title + " has an S that isn't followed by a B in row " + str(i+1))
                exit(1)
                
    wb.save(path + file_name)