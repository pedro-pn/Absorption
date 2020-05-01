import matplotlib.pyplot as plt

def plot_e(wavelength_list, epsilon_mean_list):
    plt.plot(wavelength_list, epsilon_mean_list)
    plt.xlabel('Wavelength ($\lambda$)/nm')
    plt.ylabel('$\epsilon$')
    plt.show()

def plot_abs(wavelength_list, absorption_list, concentration_list):
    for sample_index in range(len(absorption_list)):
        plt.plot(wavelength_list, absorption_list[sample_index], label=str(concentration_list[sample_index]))
    plt.legend()
    plt.xlabel('Wavelength ($\lambda$)/nm')
    plt.ylabel('Absorption')
    plt.show()