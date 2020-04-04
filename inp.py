
                   ##----------------------------------------------------------------------------------------------------------------##
                                   
                                              # Input file to run CCSD-LRT/iCCSDn-LRT to get Excitation Energy #
                                                     # as well as ground state CCSD, iCCSDn and iCCSDn-PT #
                                    
                                                # Author: Anish Chakraborty, Pradipta Samanta & Rahul Maitra #
                                                                  # Date - 10th Dec, 2019 # 

                   ##----------------------------------------------------------------------------------------------------------------##


##---------------------------------------------------------##
               #Import important modules
##---------------------------------------------------------##

import pyscf.gto
from pyscf import gto

##---------------------------------------------------------##
             #Specify geometry and basis set#       
##---------------------------------------------------------##

mol = pyscf.gto.M(
verbose = 5,
output = None,
#unit='Bohr',
atom ='''
O        0.00000        0.00000        0.07229
H        1.05798        0.00000       -0.86746
H       -1.05798        0.00000       -0.86746
''', 
basis = 'ccpvdz',
symmetry = 'C2v',
)
##---------------------------------------------------------##
                #Specify CC-Type#
       #Specific for the ground state calculation#
       #Options are 'LCCD', 'CCSD', 'ICCSD', 
##---------------------------------------------------------##

calc = 'ICCSD'

##---------------------------------------------------------##
               #Specify LRT-Type#
          #LR_type = 'ICCSD' for iCCSDn-LRT#
        #LR_type = 'CCSD' or 'None' for CCSD-LRT#
##---------------------------------------------------------##

LR_type = 'ICCSD'

##---------------------------------------------------------##
            #Specify convergence criteria ground state#
##---------------------------------------------------------##

conv = 6

##---------------------------------------------------------##
     #Specify convergence criteria for excited state#
##---------------------------------------------------------##

LR_conv = 4

##---------------------------------------------------------##
      #Specify max number of iteration for ground state#
##---------------------------------------------------------##

n_iter=100000

##---------------------------------------------------------##
          #Specify max number of iteration for LRT#
##---------------------------------------------------------##

lrt_iter = 400

##---------------------------------------------------------##
                      #Specify DIIS#
     #If diis='TRUE'; max_diis needs to be specified#
       #Specific for the ground state calculation#
##---------------------------------------------------------##

diis = False
max_diis = 7

##---------------------------------------------------------##
         #Specify number of active orbitals#
    #Currently same for both ground and excited states#
##---------------------------------------------------------##

o_act = 2
v_act = 2

##---------------------------------------------------------##
         #Specify number of frozen orbitals#
##---------------------------------------------------------##

nfo = 0
nfv = 0

##---------------------------------------------------------------------------##
     #Specify no of steps after which linear combination has to be taken#
                       #Specific for LRT#
                #This might need further testing#
##---------------------------------------------------------------------------##

n_davidson = 500

##-----------------------------------------------------------------------##
             #Number of roots required for each symmetry#
      #The ordering of the states for C2v group is A1,B1,B2,A2#
      #The ordering for D2h group is Ag,B3u,B2u,B1g,B1u,B2g,B3g,Au#
                       #Specific for LRT#
##-----------------------------------------------------------------------##

nroot = [1,1,1,1]

##----------------------------------------------------------------------##
         #External parameter to control the iteration procedure#
##----------------------------------------------------------------------##

eta=0.24





'''
O        0.00000        0.00000        0.07229
H        1.05798        0.00000       -0.86746
H       -1.05798        0.00000       -0.86746

! Experimental geometry(Bohr)
! Taken from Li and Paldus Mol. Phys. Volume 104, 2006 
O   0.000000   0.00000    0.1366052
H   0.768958   0.00000   -0.5464208
H  -0.768958   0.00000   -0.5464208

#stretched geometry of water in Bohr
O   0.00000         0.00000    0.1366083016
H   1.153432135     0.00000   -0.8879256144
H  -1.153432135     0.00000   -0.8879256144

#stretched geometry of water in angs (3*eqm_len)
O        0.00000        0.00000        0.07229
H        1.22074        0.00000       -1.01204
H       -1.22074        0.00000       -1.01204

#stretched geometry of water in angs (2*eqm_len)
O        0.00000        0.00000        0.07229
H        0.81383        0.00000       -0.65060
H       -0.81383        0.00000       -0.65060

#stretched geometry of water in angs (2.5*eqm_len)
O        0.00000        0.00000        0.07229
H        1.01729        0.00000       -0.83132
H       -1.01729        0.00000       -0.83132

#stretched geometry of water in angs (2.6*eqm_len)
O        0.00000        0.00000        0.07229
H        1.05798        0.00000       -0.86746
H       -1.05798        0.00000       -0.86746

H 0.000000 0.923274 1.238289
H 0.000000 -0.923274 1.238289
H 0.000000 0.923274 -1.238289
H 0.000000 -0.923274 -1.238289
C 0.000000 0.000000 0.668188
C 0.000000 0.000000 -0.668188
'''
