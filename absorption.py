import sys
from f_reader import *
from calc import *
from plots import *
from menu import *

print('\t\t=========================\n\t\t*\t\t\t\t\t\t*\n\t\t*\t\tABSORPTION\t\t*\n\t\t*\t\t\t\t\t\t*\n\t\t=========================\n\t\t\t\t\tby: Pedro P.\n')

menu1 = True
enter = True
try:
    input_file = sys.argv[1]
    test = open(input_file, 'r')
    test.close()
    menu1 = False
except FileNotFoundError:
    print('"%s" not found!' %input_file)
    enter = False
except IndexError:
    enter = False

while True: # Main loop
    if menu1 == True :
        print('Enter the file name with absorption data or type "exit": ')
        enter = False
    wavelength_list = []
    concentration_list = []
    epsilon_list = []
    epsilon_mean_list = []
    absorption_list = []
    if enter == False:
        input_file = input()
    if input_file == 'exit':
        break
    if open_file(input_file):
        file_format = format(input_file)


        if file_format == 'txt' or file_format == 'csv':
            if file_format == 'txt':
                data_txt(wavelength_list, absorption_list, concentration_list, input_file)
                menu_2(wavelength_list, absorption_list, epsilon_list, epsilon_mean_list, concentration_list)
                menu1 = True
            elif file_format == 'csv':
                print('(1) Semicolon CSV file;\n(2) Comma CSV file.\n')
                while True:
                    CSV_type = input()
                    if CSV_type == '1':
                        csv_br(wavelength_list, absorption_list, concentration_list, input_file)
                        menu_2(wavelength_list, absorption_list, epsilon_list, epsilon_mean_list, concentration_list)
                        menu1 = True
                        break
                    elif CSV_type == '2':
                        csv_en(wavelength_list, absorption_list, concentration_list, input_file)
                        menu_2(wavelength_list, absorption_list, epsilon_list, epsilon_mean_list, concentration_list)
                        menu1 = True
                        break
                    else:
                        print('Enter a valid option!')
        else:
            print('File format not supported!')
            enter = False
            menu1 = False


    else:
        menu1 = False