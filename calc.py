from decimal import Decimal

def epsilon(absorption_list, epsilon_list, concentration_list, cuvette_width = 1):
    """Calculates the absorption coefficient in all wavelengths measured and returns the values to a list"""
    for sample_index in range(len(absorption_list)):
        epsilon_sample_list=[]
        for sample_value_index in range(len(absorption_list[sample_index])):
            epsilon_sample_list.append((absorption_list[sample_index][sample_value_index])/(concentration_list[sample_index]*cuvette_width))
        epsilon_list.append(epsilon_sample_list)

def epsilon_mean(epsilon_list, epsilon_mean_list):
    """Calculates the epsilon mean of all concentrations and return the values as a list."""
    for epsilon_index in range(len(epsilon_list[0])):
        sum = 0
        for epsilon_sample_index in range(len(epsilon_list)):
            sum+= (epsilon_list[epsilon_sample_index][epsilon_index])
        epsilon_mean_list.append(sum/len(epsilon_list))

def maximum(wavelength_list, absorption_list, data_type, concentration_list):
    while True:
        menu = True
        max_values_list = []
        while True:
            try:
                input_1 = float(input('Enter the band limit wished values: '))
                input_2 = float(input(''))
                break
            except ValueError:
                print('Invalid value!')
        if data_type == 'absorption':
            for sample_index in range(len(absorption_list)):
                input_range_values = []
                for wavelength_value in wavelength_list:
                    if (input_1 <= wavelength_value <= input_2) and input_2 > input_1:
                        input_range_values.append(absorption_list[sample_index][wavelength_list.index(wavelength_value)])
                        menu = False
                    elif (input_2 <= wavelength_value <= input_1) and input_1 > input_2:
                        input_range_values.append(absorption_list[sample_index][wavelength_list.index(wavelength_value)])
                        menu = False
                if len(input_range_values) == 0:
                    print('Values not found!')
                    break
                max_values_list.append(max(input_range_values))
        elif data_type == 'epsilon':
            for wavelength_value in wavelength_list:
                if (input_1 <= wavelength_value <= input_2) and input_2 > input_1:
                    max_values_list.append(absorption_list[wavelength_list.index(wavelength_value)])
                    menu = False
                elif (input_2 <= wavelength_value <= input_1) and input_1 > input_2:
                    max_values_list.append(absorption_list[wavelength_list.index(wavelength_value)])
                    menu = False
            if len(max_values_list) == 0:
                print('Values not found!')
        if menu == False:
            break
    if data_type == 'absorption' and len(max_values_list) != 0:
        print('The max %s values in %fnm are: \n' %(data_type, wavelength_list[absorption_list[0].index(max_values_list[0])]))
        print("Concentration:\tAbs")
        for i in range(len(max_values_list)):
            print("%.5E\t\t%f" %(Decimal(concentration_list[i]), max_values_list[i]))
    elif data_type == 'epsilon' and len(max_values_list) != 0:
        print('The %s max value is %f in %fnm\n' %(data_type, max(max_values_list), wavelength_list[absorption_list.index(max(max_values_list))]))