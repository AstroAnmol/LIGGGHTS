import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


simulation_folder=      'mag_test'
post_folder_MDM=            '/post_two_par_MDM'
post_folder_SHA=            '/post_two_par_SHA'
post_folder_SHA_2=            '/post_two_par_SHA_2'
post_folder_SHA20=            '/post_two_par_auto'
post_folder_SHA20_2=            '/post_two_par_auto_2'
post_folder_SHA_MDM_20=            '/post_two_par_SHA_MDM_20'
post_folder_SHA_MDM_20_betachange=            '/post_two_par_SHA_MDM_20_betachange'

c=np.arange(20,41,1)
force_MDM=np.zeros(c.size)
force_SHA=np.zeros(c.size)
force_SHA_2=np.zeros(c.size)
force_SHA20=np.zeros(c.size)
force_SHA20_2=np.zeros(c.size)
force_SHA_MDM_20=np.zeros(c.size)
force_SHA_MDM_20_betachange=np.zeros(c.size)

for i in range(c.size):
    sep_file=c[i]
    MDM_file_location= (simulation_folder + post_folder_MDM + f"/dump_{sep_file}_2.liggghts")
    force_MDM[i]=np.loadtxt(MDM_file_location, skiprows=10, usecols=4)

    SHA_file_location= (simulation_folder + post_folder_SHA + f"/dump_{sep_file}_2.liggghts")
    force_SHA[i]=np.loadtxt(SHA_file_location, skiprows=10, usecols=4)

    SHA_file_location_2= (simulation_folder + post_folder_SHA_2 + f"/dump_{sep_file}_2.liggghts")
    force_SHA_2[i]=np.loadtxt(SHA_file_location_2, skiprows=10, usecols=4)

    file_location_SHA20= (simulation_folder + post_folder_SHA20 + f"/dump_{sep_file}_2.liggghts")
    force_SHA20[i]=np.loadtxt(file_location_SHA20, skiprows=10, usecols=4)

    file_location_SHA20_2= (simulation_folder + post_folder_SHA20_2 + f"/dump_{sep_file}_2.liggghts")
    force_SHA20_2[i]=np.loadtxt(file_location_SHA20_2, skiprows=10, usecols=4)

    file_location_SHA_MDM_20= (simulation_folder + post_folder_SHA_MDM_20 + f"/dump_{sep_file}_2.liggghts")
    force_SHA_MDM_20[i]=np.loadtxt(file_location_SHA_MDM_20, skiprows=10, usecols=4)

    file_location_SHA_MDM_20_betachange= (simulation_folder + post_folder_SHA_MDM_20_betachange + f"/dump_{sep_file}_2.liggghts")
    force_SHA_MDM_20_betachange[i]=np.loadtxt(file_location_SHA_MDM_20_betachange, skiprows=10, usecols=4)


print('MDM', force_MDM)
print('SHA', force_SHA)
print('SHA2', force_SHA_2)
print('SHA', force_SHA20)
print('SHA', force_SHA20_2)
print('SHA', force_SHA_MDM_20)
print('SHA', force_SHA_MDM_20_betachange)

# MDM_SHA=(force_MDM-force_SHA)
# MDM_SHA2=(force_MDM-force_SHA_2)
# SHA_SHA2=(force_SHA-force_SHA_2)
# print('MDM - SHA', MDM_SHA)
# print('MDM - SHA2', MDM_SHA2)
# print('SHA - SHA2', SHA_SHA2)

# plt.plot(c/10, force_MDM, 'b-', label= 'MDM')
# plt.plot(c/10, force_SHA, label= 'Inclusion Model')
# plt.plot(c/10, force_SHA20,  label= 'Inclusion Model 20')
# plt.plot(c/10, force_SHA20_2,  label= 'Inclusion Model 20 2')
# plt.plot(c/10, force_SHA_2,  label= 'Inclusion Model 2.0')
plt.plot(c/10, force_SHA_MDM_20,  label= 'Inclusion Model MDM 20')
plt.plot(c/10, force_SHA_MDM_20_betachange,  label= 'Inclusion Model MDM 20 Betachange')
plt.legend()
plt.show()