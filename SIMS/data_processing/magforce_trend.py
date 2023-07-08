import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


simulation_folder=                  'mag_test'


# mag_field_orientation=              '/parallel'  
mag_field_orientation=              '/perpendicular'
# mag_field_orientation=              '/perpendicular_plane'

susc_folder=                        '/susc1'
# susc_folder=                        '/susc4'

post_folder_MDM=                    'MDM'
post_folder_SHA=                    'SHA'
post_folder_inc=                    'inclusion'


# post_folder_SHA_2=                  'SHA_2'
# post_folder_SHA20=                  'auto'
# post_folder_SHA20_2=                'auto_2'
# post_folder_SHA_MDM_20=             'SHA_MDM_20'
# post_folder_SHA_MDM_20_betachange=  'SHA_MDM_20_betachange'
# post_folder_beta_print=             'print_beta'
# post_folder_beta_print10=           'print_beta10'
# post_folder_nb=                     'nobeta'
# post_folder_nbm=                    'nobeta_nomag'
# post_folder_trial=                  'trial'

c=                  np.arange(20,41,1)
force_MDM=          np.zeros(c.size)
force_SHA=          np.zeros(c.size)
force_inc=          np.zeros(c.size)

# force_nb=           np.zeros(c.size)
# force_trial=        np.zeros(c.size)
# force_nbm=          np.zeros(c.size)
# force_SHA_2=np.zeros(c.size)
# force_SHA20=np.zeros(c.size)
# force_SHA20_2=np.zeros(c.size)
# force_SHA_MDM_20=np.zeros(c.size)
# force_SHA_MDM_20_betachange=np.zeros(c.size)
# force_beta_print=np.zeros(c.size)
# force_beta_print10=np.zeros(c.size)

for n in range(3):
    particle_number=n+2
    if particle_number==2:
        post_folder_par=            '/post_par2_'
        skip_rows=10
    
    elif particle_number==3:
        post_folder_par=            '/post_par3_'
        skip_rows=9

    elif particle_number==4:
        post_folder_par=            '/post_par3_triangle_'
        skip_rows=9

    for i in range(c.size):
        sep_file=c[i]
        dump_folder=            simulation_folder + mag_field_orientation + susc_folder + post_folder_par 

        MDM_file_location=      (dump_folder + post_folder_MDM + f"/dump_{sep_file}_2.liggghts")
        force_MDM[i]=           np.loadtxt(MDM_file_location, skiprows=skip_rows, usecols=4)

        SHA_file_location=      (dump_folder + post_folder_SHA + f"/dump_{sep_file}_2.liggghts")
        force_SHA[i]=           np.loadtxt(SHA_file_location, skiprows=skip_rows, usecols=4)

        inc_file_location=      (dump_folder + post_folder_inc+ f"/dump_{sep_file}_2.liggghts")
        force_inc[i]=           np.loadtxt(inc_file_location, skiprows=skip_rows, usecols=4)

        # nb_file_location=       (dump_folder + post_folder_nb+ f"/dump_{sep_file}_2.liggghts")
        # force_nb[i]=            np.loadtxt(nb_file_location, skiprows=skip_rows, usecols=4)   
        
        # trial_file_location=    (dump_folder + post_folder_trial+ f"/dump_{sep_file}_2.liggghts")
        # force_trial[i]=            np.loadtxt(trial_file_location, skiprows=skip_rows, usecols=4)   
        
        # nbm_file_location=      (dump_folder + post_folder_nbm+ f"/dump_{sep_file}_2.liggghts")
        # force_nbm[i]=           np.loadtxt(nbm_file_location, skiprows=skip_rows, usecols=4)

        # SHA_file_location_2= (simulation_folder + mag_field_orientation + post_folder_par + post_folder_SHA_2 + f"/dump_{sep_file}_2.liggghts")
        # force_SHA_2[i]=np.loadtxt(SHA_file_location_2, skiprows=skip_rows, usecols=4)

        # file_location_SHA20= (simulation_folder + post_folder_SHA20 + f"/dump_{sep_file}_2.liggghts")
        # force_SHA20[i]=np.loadtxt(file_location_SHA20, skiprows=skip_rows, usecols=4)

        # file_location_SHA20_2= (simulation_folder + post_folder_SHA20_2 + f"/dump_{sep_file}_2.liggghts")
        # force_SHA20_2[i]=np.loadtxt(file_location_SHA20_2, skiprows=skip_rows, usecols=4)

        # file_location_SHA_MDM_20= (simulation_folder + post_folder_SHA_MDM_20 + f"/dump_{sep_file}_2.liggghts")
        # force_SHA_MDM_20[i]=np.loadtxt(file_location_SHA_MDM_20, skiprows=skip_rows, usecols=4)

        # file_location_SHA_MDM_20_betachange= (simulation_folder + post_folder_SHA_MDM_20_betachange + f"/dump_{sep_file}_2.liggghts")
        # force_SHA_MDM_20_betachange[i]=np.loadtxt(file_location_SHA_MDM_20_betachange, skiprows=skip_rows, usecols=4)

        # file_location_beta_print= (simulation_folder + post_folder_beta_print + f"/dump_{sep_file}_2.liggghts")
        # force_beta_print[i]=np.loadtxt(file_location_beta_print, skiprows=skip_rows, usecols=4)

        # file_location_beta_print10= (simulation_folder + post_folder_beta_print10 + f"/dump_{sep_file}_2.liggghts")
        # force_beta_print10[i]=np.loadtxt(file_location_beta_print10, skiprows=skip_rows, usecols=4)

    plt.figure(i+1)
    plt.plot(c/10, force_MDM, 'b-', label= 'MDM')
    # plt.plot(c/10, force_beta_print, '', label= 'inclusion')
    # plt.plot(c/10, force_beta_print10, '', label= 'inclusion10')
    plt.plot(c/10, force_SHA, 'g--', label= 'SHA')
    plt.plot(c/10, force_inc, label= 'inclusion')
    # plt.plot(c/10, force_nb, label= 'nobeta')
    # plt.plot(c/10, force_trial, label= 'trial')
    # plt.plot(c/10, force_nbm, label= 'nobeta_nomag')
    # plt.plot(c/10, force_SHA_2,  label= 'Inclusion Model 2.0')
    # plt.plot(c/10, force_SHA20,  label= 'Inclusion Model 20')
    # plt.plot(c/10, force_SHA20_2,  label= 'Inclusion Model 20 2')
    # plt.plot(c/10, force_SHA_MDM_20,  label= 'Inclusion Model MDM 20')
    # plt.plot(c/10, force_SHA_MDM_20_betachange,  label= 'Inclusion Model MDM 20 Betachange')
    plt.title("Parallel Susceptibilty=1")
    plt.grid()
    plt.legend()
    plt.show()






# print('MDM', force_MDM)
# # print('SHA', force_SHA)
# # print('SHA2', force_SHA_2)
# # print('SHA 20', force_SHA20)
# # print('SHA 20_2', force_SHA20_2)
# # print('SHA MDM 20', force_SHA_MDM_20)
# # print('SHA MDM 20 beta change', force_SHA_MDM_20_betachange)
# print('beta_print',force_beta_print)
# print('beta_print10',force_beta_print10)
# print('inclusion',force_inclusion)
# print('nobeta',force_nobeta)


# # MDM_SHA=(force_MDM-force_SHA)
# # MDM_SHA2=(force_MDM-force_SHA_2)
# # SHA_SHA2=(force_SHA-force_SHA_2)
# # print('MDM - SHA', MDM_SHA)
# # print('MDM - SHA2', MDM_SHA2)
# # print('SHA - SHA2', SHA_SHA2)
