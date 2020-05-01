import csv

file = open('testecsv2.csv', 'r')
reader = csv.reader(file)
header_row = next(reader)
number_of_columns = len(header_row)
absorption = []
for column in range(number_of_columns):
    column_values_list = []
    for row in reader:
        if len(row) == number_of_columns:
            try:
                column_values_list.append(float(row[column]))
            except:
                pass
    absorption.append(column_values_list)
for row in reader:
    print(row)
print(absorption)



"""for column_index in range(number_of_columns):
    column_values_list = []
    for row_index in range(len(file_lines)):
        row_data_list = file_lines[row_index].strip("\n")
        row_data = row_data_list.split(',')  # list of a row
        try:
            row_data.remove("")
            row_data.remove('\t')
            row_data.remove('\n')
        except:
            pass
        try:
            if column_index == 0 and len(row_data) == number_of_columns:
                wavelength_list.append(float(row_data[column_index]))
            elif column_index != 0 and len(row_data) == number_of_columns:
                column_values_list.append(float(row_data[column_index].strip("\n\t")))
        except:
            pass
    if column_index != 0:
        absorption_list.append(column_values_list)
for i in range(len(absorption_list)):
    while True:
        try:
            concentration_list.append(float(input("Enter the concentration of sample %i : " % (i + 1))))
            break
        except:
            print('Invalid Value.')
file.close()
"""