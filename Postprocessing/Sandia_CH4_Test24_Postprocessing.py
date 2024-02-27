import matplotlib.pyplot as plt
import numpy as np

# Vertical RMS velocity
wp3_rms_dx6 = np.genfromtxt('Sandia_CH4_1m_Test24_dx6cm_line.csv', delimiter=',', usecols=(7), skip_header=2)
wp5_rms_dx6 = np.genfromtxt('Sandia_CH4_1m_Test24_dx6cm_line.csv', delimiter=',', usecols=(8), skip_header=2)
wp9_rms_dx6 = np.genfromtxt('Sandia_CH4_1m_Test24_dx6cm_line.csv', delimiter=',', usecols=(9), skip_header=2)

wp3_rms_dx3 = np.genfromtxt('Sandia_CH4_1m_Test24_dx3cm_line.csv', delimiter=',', usecols=(7), skip_header=2)
wp5_rms_dx3 = np.genfromtxt('Sandia_CH4_1m_Test24_dx3cm_line.csv', delimiter=',', usecols=(8), skip_header=2)
wp9_rms_dx3 = np.genfromtxt('Sandia_CH4_1m_Test24_dx3cm_line.csv', delimiter=',', usecols=(9), skip_header=2)

# Radial RMS velocity
up3_rms_dx6 = np.genfromtxt('Sandia_CH4_1m_Test24_dx6cm_line.csv', delimiter=',', usecols=(10), skip_header=2)
up5_rms_dx6 = np.genfromtxt('Sandia_CH4_1m_Test24_dx6cm_line.csv', delimiter=',', usecols=(11), skip_header=2)
up9_rms_dx6 = np.genfromtxt('Sandia_CH4_1m_Test24_dx6cm_line.csv', delimiter=',', usecols=(12), skip_header=2)

up3_rms_dx3 = np.genfromtxt('Sandia_CH4_1m_Test24_dx3cm_line.csv', delimiter=',', usecols=(10), skip_header=2)
up5_rms_dx3 = np.genfromtxt('Sandia_CH4_1m_Test24_dx3cm_line.csv', delimiter=',', usecols=(11), skip_header=2)
up9_rms_dx3 = np.genfromtxt('Sandia_CH4_1m_Test24_dx3cm_line.csv', delimiter=',', usecols=(12), skip_header=2)

# Radial position
x_dx6 = np.genfromtxt('Sandia_CH4_1m_Test24_dx6cm_line.csv', delimiter=',', usecols=(0), skip_header=2)
x_dx3 = np.genfromtxt('Sandia_CH4_1m_Test24_dx3cm_line.csv', delimiter=',', usecols=(0), skip_header=2)

TKE_3_dx6 = 0.5*(np.square(wp3_rms_dx6) + np.square(up3_rms_dx6))
TKE_5_dx6 = 0.5*(np.square(wp5_rms_dx6) + np.square(up5_rms_dx6))
TKE_9_dx6 = 0.5*(np.square(wp9_rms_dx6) + np.square(up9_rms_dx6))

TKE_3_dx3 = 0.5*(np.square(wp3_rms_dx3) + np.square(up3_rms_dx3))
TKE_5_dx3 = 0.5*(np.square(wp5_rms_dx3) + np.square(up5_rms_dx3)) 
TKE_9_dx3 = 0.5*(np.square(wp9_rms_dx3) + np.square(up9_rms_dx3))

# Read experimental data set
x_0p3m_exp = np.genfromtxt('Test24_0p3m_exp.csv', delimiter=',', usecols=(0), skip_header=1)
TKE_0p3m_exp = np.genfromtxt('Test24_0p3m_exp.csv', delimiter=',', usecols=(1), skip_header=1)

x_0p5m_exp = np.genfromtxt('Test24_0p5m_exp.csv', delimiter=',', usecols=(0), skip_header=1)
TKE_0p5m_exp = np.genfromtxt('Test24_0p5m_exp.csv', delimiter=',', usecols=(1), skip_header=1)

x_0p9m_exp = np.genfromtxt('Test24_0p9m_exp.csv', delimiter=',', usecols=(0), skip_header=1)
TKE_0p9m_exp = np.genfromtxt('Test24_0p9m_exp.csv', delimiter=',', usecols=(1), skip_header=1)

# Plot figures
fig, (axs, axs1, axs2) = plt.subplots(1,3, figsize=(15,4.5))
axs.plot(x_0p3m_exp, TKE_0p3m_exp, 'o', label='Experimental')
axs.plot(x_dx6, TKE_3_dx6, '-.', label='FDS 6cm')
axs.plot(x_dx3, TKE_3_dx3, '--', label='FDS 3cm')
axs.text(-0.45, 4.25, 'Sandia Methane Pool Fire \nTest 24, z = 0.3 m', fontsize = 12)
axs.set_ylabel("TKE (m$^2$/s$^2$)")
axs.set_xlabel("Radial Position (m)")
axs.set_ylim(0, 5)
axs.set_xlim(-0.5, 0.5)
axs.legend()
axs.set_yticks(np.arange(0, 5.1, 1))
axs.set_yticks(np.arange(0, 5.1, 0.2), minor=True)
axs.set_xticks(np.arange(-0.5,0.51,0.1))
axs.set_xticks(np.arange(-0.5,0.51,0.02), minor=True)

axs1.plot(x_0p5m_exp, TKE_0p5m_exp, 'o', label='Experimental')
axs1.plot(x_dx6, TKE_5_dx6, '-.', label='FDS 6cm')
axs1.plot(x_dx3, TKE_5_dx3, '--', label='FDS 3cm')
axs1.text(-0.45, 4.25, 'Sandia Methane Pool Fire \nTest 24, z = 0.5 m', fontsize = 12)
axs1.set_ylabel("TKE (m$^2$/s$^2$)")
axs1.set_xlabel("Radial Position (m)")
axs1.set_ylim(0, 5)
axs1.set_xlim(-0.5, 0.5)
axs1.legend()
axs1.set_yticks(np.arange(0, 5.1, 1))
axs1.set_yticks(np.arange(0, 5.1, 0.2), minor=True)
axs1.set_xticks(np.arange(-0.5,0.51,0.1))
axs1.set_xticks(np.arange(-0.5,0.51,0.02), minor=True)

axs2.plot(x_0p9m_exp, TKE_0p9m_exp, 'o', label='Experimental')
axs2.plot(x_dx6, TKE_9_dx6, '-.', label='FDS 6cm')
axs2.plot(x_dx3, TKE_9_dx3, '--', label='FDS 3cm')
axs2.text(-0.45, 4.25, 'Sandia Methane Pool Fire \nTest 24, z = 0.9 m', fontsize = 12)
axs2.set_ylabel("TKE (m$^2$/s$^2$)")
axs2.set_xlabel("Radial Position (m)")
axs2.set_ylim(0, 5)
axs2.set_xlim(-0.5, 0.5)
axs2.legend()
axs2.set_yticks(np.arange(0, 5.1, 1))
axs2.set_yticks(np.arange(0, 5.1, 0.2), minor=True)
axs2.set_xticks(np.arange(-0.5,0.51,0.1))
axs2.set_xticks(np.arange(-0.5,0.51,0.02), minor=True)

fig.tight_layout()
fig.subplots_adjust(wspace=0.25)
plt.savefig("TKE.jpg")