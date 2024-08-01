# Importando as bibliotecas
import numpy as np
import matplotlib.pyplot as plt

n = 1000 # Número de pontos
tx = 200 # Tamanho do eixo X
w = 2.0 * np.pi/tx # frequência angular

# Base de tempo
t = np.linspace(0, tx, n)

# Senoides
s1 = 2.0 * np.cos(2.0 * w * t)
s2 = 1.0 * np.cos(30.0 * w * t)
s = s1 + s2

# Transformada Discreta de Fourier.
freq = np.fft.fftfreq(n)

#  Mascara para só valores positivos
mask = freq > 0

# TFD da soma dos senoides
fft_calculation = np.fft.fft(s)

# Retirando números negativos 
fft_absolute = 2.0 * np.abs(fft_calculation/n)

# Criando figura do sinal original
plt.figure(1)
plt.title("Sinal original")
plt.plot(t, s)

# Criando figura do sinal transformado
plt.figure(2)
plt.title("Sinal da fft")
plt.plot(freq[mask], fft_absolute[mask])

plt.show()