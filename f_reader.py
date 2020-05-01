def data_txt(wavelength_list, absorption_lists, concentration_list, file_name): #dados > data_txt
    """This function receive as input the empty list of wavelengths,
    absorptions, concentrations and the text file with wavelength
    and absorption data. The data in the text document must be separated by "*" and organized by columns,
    where the first column is the wavelength of measurement followed by the respective abs values.
    The columns must be separated by empty spaces. The empty lists will be filled with their respective
    data. The "absorption_lists" list will be a list of lists because using this
    approach the program can process a undefined number of samples."""
    file = open(file_name, "r")
    numeric_data = file.read().split("*")
    data_rows = numeric_data[1].split("\n")
    counter = 0
    while counter < len(data_rows): # A looping to remove possible empty data.
        if data_rows[counter] == '\n' or data_rows[counter] == '':
            data_rows.pop(counter)
            counter = 0
        else:
            counter+=1
    column_lenght = len(data_rows[0].split())
    for column_index in range(column_lenght):
        absorption_list=[]
        for row_index in range(len(data_rows)):
            row_items = data_rows[row_index].split()
            if column_index == 0: #Select only the wavelength values
                wavelength_list.append(float(row_items[column_index]))
            if column_index != 0: #Select only absorption data
                absorption_list.append(float(row_items[column_index]))
        if column_index != 0:
            absorption_lists.append(absorption_list)
    for sample_measured in range(len(absorption_lists)):
        """This loop uses the number of list of absorption_lists to ask
        the user the concentration values."""
        while True:
            try:
                concentration_list.append(float(input(
                    'Enter the concentration of sample %i: '
                    %(sample_measured+1)))
                )
                break
            except:
                print('Invalid Value!')
    file.close()

def csv_br(wavelength_list, absorption_lists, concentrations_list, file_name):
    """This function was created to deal with csv outputs of pt-br configured
    programs. In brazilian notation, decimals are represented by a comma
    instead of a point; csv files are separated by semi-colon instead of comma."""
    file = open(file_name, 'r')
    file_lines = file.readlines()
    converted_csv_data_list = []
    for line in file_lines:
        """This loop changes the commas into dots and the semi-colons into commas"""
        converted_row = []
        line_data_list = line.split(";")
        for line_data in line_data_list:
            try:
                if (
                    (line_data != "") and (line_data != "\n")
                    and (line_data.replace(",", ".") not in (converted_row))
                ):
                    """Sometimes the csv file comes with the wavelength repeated,
                    so this loop makes sure to not add it twice, and avoid blank
                    data as well."""
                    converted_row.append(line_data.replace(",", ".")).strip("\n")
            except:
                pass
        converted_csv_data_list.append(converted_row)
    for row in converted_csv_data_list: #determine number of columns
        for row_data in row:
            try:
                float(row_data) #check if the column starts with a number.
                number_of_columns = len(row)
                break
            except:
                pass
    for column_number in range(number_of_columns):
        absorption_list=[]
        for row_number in range(len(converted_csv_data_list)):
            try:
                data = converted_csv_data_list[row_number][column_number].strip("\n")
                if (
                    (column_number == 0) and
                    (len(converted_csv_data_list[row_number]) == number_of_columns)
                ): #a simple way to not add anything but measurement data.
                    wavelength_list.append(float(data))
                elif (
                    (column_number != 0) and
                    (len(converted_csv_data_list[row_number]) == number_of_columns)
                ):
                    absorption_list.append(float(data))
            except:
                pass
        if column_number != 0:
            absorption_lists.append(absorption_list)
    for sample_measured in range(len(absorption_lists)):
        while True:
            try:
                concentrations_list.append(float(input(
                'Enter the concentration of sample %s: '
                %(sample_measured+1)))
                )
                break
            except:
                print('Invalid value!')
    file.close()

def csv_en(wavelength_list, absorption_list, concentration_list, file_name):
    """Reads CSV files and makes a list of wavelength and absorption values."""
    file = open(file_name, 'r')
    file_lines = file.readlines()
    for line in file_lines: # identify the number of measures of the CSV file.
        row_list = line.split(',')
        for row_data in row_list:
            try:
                row_list.remove("\n")
            except:
                pass
            try:
                float(row_data)
                number_of_columns = len(row_list)
                break
            except:
                break
    for column_index in range(number_of_columns):
        column_values_list=[]
        for row_index in range(len(file_lines)):
            row_data_list = file_lines[row_index].strip("\n")
            row_data = row_data_list.split(',') #list of a row
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
                concentration_list.append(float(input("Enter the concentration of sample %i : " %(i+1))))
                break
            except:
                print('Invalid Value.')
    file.close()
