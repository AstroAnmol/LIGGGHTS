import matplotlib.pyplot as plt
import numpy as np
# import pandas as pd


simulation_folder=      'mag_test'
post_folder_MDM=            '/post_par3_MDM'
post_folder_SHA=            '/post_par3_SHA'
post_folder_SHA_2=            '/post_par3_SHA_2'
post_folder_SHA20=            '/post_par3'
post_folder_SHA20_2=            '/post_par3_2'
post_folder_SHA_MDM_20=            '/post_par3_SHA_MDM_20'
post_folder_SHA_MDM_20_betachange=            '/post_par3_SHA_MDM_20_betachange'
post_folder_print_beta=         '/post_par3_print_beta'
post_folder_print_beta10=         '/post_par3_print_beta10'
post_folder_inclusion=         '/post_par3_inclusion'
post_folder_nobeta=         '/post_par3_nobeta'
post_folder_nobeta_nomag=         '/post_par3_nobeta_nomag'

c=np.arange(20,41,1)
force_MDM=np.zeros(c.size)
force_SHA=np.zeros(c.size)
force_SHA_2=np.zeros(c.size)
force_SHA20=np.zeros(c.size)
force_SHA20_2=np.zeros(c.size)
force_SHA_MDM_20=np.zeros(c.size)
force_SHA_MDM_20_betachange=np.zeros(c.size)
force_print_beta=np.zeros(c.size)
force_print_beta10=np.zeros(c.size)
force_inclusion=np.zeros(c.size)
force_nobeta=np.zeros(c.size)
force_nobeta_nomag=np.zeros(c.size)

for i in range(c.size):
    sep_file=c[i]
    MDM_file_location= (simulation_folder + post_folder_MDM + f"/dump_{sep_file}_3.liggghts")
    force_MDM[i]=np.loadtxt(MDM_file_location, skiprows=9, usecols=4)

    SHA_file_location= (simulation_folder + post_folder_SHA + f"/dump_{sep_file}_2.liggghts")
    force_SHA[i]=np.loadtxt(SHA_file_location, skiprows=9, usecols=4)

    SHA_file_location_2= (simulation_folder + post_folder_SHA_2 + f"/dump_{sep_file}_2.liggghts")
    force_SHA_2[i]=np.loadtxt(SHA_file_location_2, skiprows=9, usecols=4)

    file_location_SHA20= (simulation_folder + post_folder_SHA20 + f"/dump_{sep_file}_2.liggghts")
    force_SHA20[i]=np.loadtxt(file_location_SHA20, skiprows=9, usecols=4)

    file_location_SHA20_2= (simulation_folder + post_folder_SHA20_2 + f"/dump_{sep_file}_2.liggghts")
    force_SHA20_2[i]=np.loadtxt(file_location_SHA20_2, skiprows=9, usecols=4)

    file_location_SHA_MDM_20= (simulation_folder + post_folder_SHA_MDM_20 + f"/dump_{sep_file}_2.liggghts")
    force_SHA_MDM_20[i]=np.loadtxt(file_location_SHA_MDM_20, skiprows=9, usecols=4)

    file_location_SHA_MDM_20_betachange= (simulation_folder + post_folder_SHA_MDM_20_betachange + f"/dump_{sep_file}_2.liggghts")
    force_SHA_MDM_20_betachange[i]=np.loadtxt(file_location_SHA_MDM_20_betachange, skiprows=9, usecols=4)

    file_location_print_beta= (simulation_folder + post_folder_print_beta + f"/dump_{sep_file}_2.liggghts")
    force_print_beta[i]=np.loadtxt(file_location_print_beta, skiprows=9, usecols=4)
    
    file_location_print_beta10= (simulation_folder + post_folder_print_beta10 + f"/dump_{sep_file}_2.liggghts")
    force_print_beta10[i]=np.loadtxt(file_location_print_beta10, skiprows=9, usecols=4)

    file_location_inclusion= (simulation_folder + post_folder_inclusion + f"/dump_{sep_file}_3.liggghts")
    force_inclusion[i]=np.loadtxt(file_location_inclusion, skiprows=9, usecols=4)

    file_location_nobeta= (simulation_folder + post_folder_nobeta + f"/dump_{sep_file}_3.liggghts")
    force_nobeta[i]=np.loadtxt(file_location_nobeta, skiprows=9, usecols=4)

    file_location_nobeta_nomag= (simulation_folder + post_folder_nobeta_nomag + f"/dump_{sep_file}_3.liggghts")
    force_nobeta_nomag[i]=np.loadtxt(file_location_nobeta_nomag, skiprows=9, usecols=4)


print('MDM', force_MDM)
print('SHA', force_SHA)
# print('SHA2', force_SHA_2)
# print('SHA 20', force_SHA20)
# print('SHA 20_2', force_SHA20_2)
# print('SHA MDM_20', force_SHA_MDM_20)
# print('SHA MDM_20_betachange', force_SHA_MDM_20_betachange)
# print('Print beta', force_print_beta)
print('Inclusion', force_inclusion)
print('nobeta', force_nobeta)
print('nobeta_nomag', force_nobeta_nomag)

# print('--------------------')
# MDM_SHA=(force_MDM-force_SHA)
# MDM_SHA2=(force_MDM-force_SHA_2)
# SHA_SHA2=(force_SHA-force_SHA_2)
# print('MDM - SHA', MDM_SHA)
# print('MDM - SHA2', MDM_SHA2)
# print('SHA - SHA2', SHA_SHA2)

plt.plot(c/10, -force_MDM, 'b-', label= 'MDM')
# plt.plot(c/10, -force_print_beta, '--',label= 'Print beta')
# plt.plot(c/10, -force_print_beta10, label= 'Print beta10')
plt.plot(c/10, -force_SHA, 'g--', label= 'SHA')
plt.plot(c/10, -force_inclusion, label= 'inclusion')
plt.plot(c/10, -force_nobeta, label= 'nobeta')
plt.plot(c/10, -force_nobeta_nomag, label= 'nobeta_nomag')
# plt.plot(c/10, -force_SHA_2,  label= 'Inclusion Model 2.0')
# plt.plot(c/10, -force_SHA20,  label= 'Inclusion Model 20')
# plt.plot(c/10, -force_SHA20_2,  label= 'Inclusion Model 20 2')
# plt.plot(c/10, -force_SHA_MDM_20,  label= 'Inclusion Model MDM 20')
# plt.plot(c/10, -force_SHA_MDM_20_betachange,  label= 'Inclusion Model MDM 20_betachange')
plt.legend()
plt.show()