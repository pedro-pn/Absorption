from calc import *
from plots import *

def format(file_name):
    name_string = file_name.split('.')
    return name_string[-1]

def save(wavelength_list, absorption_list, saved_file):
    saved_file += '.csv'
    file = open(saved_file, 'w')
    file.write('Wavelength/(nm),Epsilon\n')
    for column in range(len(wavelength_list)):
        row = "\n"+str(wavelength_list[column])+","+str(absorption_list[column])
        file.write(row)
    file.close()

def open_file(input_file):
    """Check if the file format entered is supported"""
    try:
        teste = open(input_file, "r")
        teste.close()
        return True
    except FileNotFoundError:
        print('"%s"' % input_file, "not found. Type again: ")
        return False

def menu(wavelength_list, absorption_list, epsilon_mean_list, epsilon_list, concentration_list):
    """Menu function to run in a loop."""
    menu = True
    while True:
        if menu == False:
            option = input()
        elif menu == True:
            option = input('\nSelect an option:\n\n(1) Absorption graph;\n(2) Epsilon mean graph; \n(3) Find a maximum value;\n(4) Save epsilon values as ".csv" file;\n(5) Change cuvette width;\n(6) Exit.\n')
        if option == '1':
            plot_abs(wavelength_list, absorption_list, concentration_list)
            menu = True
        elif option == '2':
            plot_e(wavelength_list, epsilon_mean_list)
            menu = True
        elif option == '3':
            menu = True
            while True:
                if menu == True:
                    max_option = input('(1) Absorption maximum;\n(2) Epsilon maximum;\n(3) Return\n')
                elif menu == False:
                    max_option = input()
                if max_option == '1':
                    maximum(wavelength_list, absorption_list, 'absorption', concentration_list)
                elif max_option == '2':
                    maximum(wavelength_list, epsilon_mean_list, 'epsilon', concentration_list)
                elif max_option == '3':
                    break
                else:
                    print('Invalid option!')
        elif option == '4':
            file_name = input('File name: ')
            save(wavelength_list, epsilon_mean_list, file_name)
        elif option == '5':
            print('Type the cuvette width: ')
            while True:
                try:
                    cuvette_width = float(input(''))
                    epsilon_list.clear()
                    epsilon_mean_list.clear()
                    epsilon(absorption_list, epsilon_list, concentration_list, cuvette_width)
                    epsilon_mean(epsilon_list, epsilon_mean_list)
                    break
                except ValueError:
                    print('Type a valid number.')
        elif option == '6':
            break
        else:
            print('Invalid option!')
            menu = False

def menu_2(wavelength_list, absorption_list, epsilon_list, epsilon_mean_list, concentration_list):
    """Main functions are called by menu_2"""
    epsilon(absorption_list, epsilon_list, concentration_list)
    epsilon_mean(epsilon_list, epsilon_mean_list)
    menu(wavelength_list, absorption_list, epsilon_mean_list, epsilon_list, concentration_list)