import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


simulation_folder=      'mag_test'
post_folder_MDM=            '/post_two_par_MDM'
post_folder_SHA=            '/post_two_par_SHA'
post_folder_SHA_2=            '/post_two_par_SHA_2'


c=np.arange(20,41,1)
force_MDM=np.zeros(c.size)
force_SHA=np.zeros(c.size)
force_SHA_2=np.zeros(c.size)

for i in range(c.size):
    sep_file=c[i]
    MDM_file_location= (simulation_folder + post_folder_MDM + f"/dump_{sep_file}_2.liggghts")
    force_MDM[i]=np.loadtxt(MDM_file_location, skiprows=10, usecols=4)

    SHA_file_location= (simulation_folder + post_folder_SHA + f"/dump_{sep_file}_2.liggghts")
    force_SHA[i]=np.loadtxt(SHA_file_location, skiprows=10, usecols=4)

    SHA_file_location_2= (simulation_folder + post_folder_SHA_2 + f"/dump_{sep_file}_2.liggghts")
    force_SHA_2[i]=np.loadtxt(SHA_file_location_2, skiprows=10, usecols=4)


print('MDM', force_MDM)
print('SHA', force_SHA)
print('SHA2', force_SHA_2)


# MDM_SHA=(force_MDM-force_SHA)
# MDM_SHA2=(force_MDM-force_SHA_2)
# SHA_SHA2=(force_SHA-force_SHA_2)
# print('MDM - SHA', MDM_SHA)
# print('MDM - SHA2', MDM_SHA2)
# print('SHA - SHA2', SHA_SHA2)