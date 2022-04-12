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

def error_region(i, sheet, row_num):
    error_region = "\n"
    if i == 0:
        area = [i, i+1]
    elif i == row_num - 1:
        area = [i-1, i]
    else:
        area = [i-1, i, i+1]
    # gets the relevant row and surrounding rows
    for j in area:
        row = list(list(sheet)[j])
        error_region += str(j+1) + " "
        for cell in row[0:3]:
            if not cell.value:
                error_region += "  "
            else:
                error_region += str(cell.value) + " "
        error_region += "\n"
    return error_region

# catches errors, highlights B cells, and indexes trials
for sheet in wb:
    b = 0
    s = 0
    row_num = 0
    b_fill = PatternFill(start_color = 'FFD3AA', end_color = 'FFD3AA', fill_type = 'solid')
    if sheet.title == 'AVERAGES ACROSS CODERS':
        continue
    for row in sheet:
        if row[0].value == "B":
            b += 1
            # highlights cells and indexes trials
            row[0].fill = b_fill
            sheet["M" + str(row_num + 1)] = b
            sheet["M" + str(row_num + 1)].fill = b_fill
        if row[0].value == "S":
            s += 1
        row_num += 1
    # makes sure every S has a B following it (except for the last one)
    # also makes sure that every row has something in the first column
    for i in range(0, row_num):
        row = list(sheet)[i]
        if not list(row)[0].value:
            print(sheet.title + " missing look in row " + str(i+1))
            print(error_region(i, sheet, row_num))
            exit(1)
        if list(row)[0].value == "S" and i != row_num - 1:
            if list(sheet)[i+1][0].value != "B":
                print(sheet.title + " has an S that isn't followed by a B in row " + str(i+1))
                print(error_region(i+1, sheet, row_num))
                exit(1)
        # makes sure the number of trials is correct
    if b != num_trials or s != num_trials:
        print(sheet.title + " has incorrect number of trials.\n" + str(b) + " B\n" + str(s) + " S\n" + "Should have " + str(num_trials) + " of each.")       
        exit(1)
    wb.save(path + file_name)