import subprocess
import sys
import numpy as np 
import math
def run_cc(eta, del_eta):
    n_iter=int(100/del_eta)
    if n_iter>100000:
        n_iter=100000
    print('running for eta = '+str(eta)+'and number of iterations =' +str(n_iter))
    process=subprocess.Popen(["./link.sh", str(eta), str(n_iter)], stdout=subprocess.PIPE)
    process.wait()
    a=process.communicate()[0]
    print(a)
    return a
def checker(eta1, eta2, len1, len2, del_eta):
    a=(len1==len2)
    conv1=0.00000005
    print('checking convergence of eta1 = ' +str(eta1) +' and eta2 = ' +str(eta2)+' with convergence limit = '+str(conv1))
    #print(len1)
    #print(len2)
    print(a)
    while(conv1>0.000000000001):
        if (abs(eta1-eta2)<conv1 and not a):  #convergence reached, return 1  
            print('eta1 and eta2 converged')
            print('onset point between eta1 = '+str(eta1)+' and eta2 = '+str(2*eta2-eta1))
            exit()

            return 1
        elif(abs(eta1-eta2)>conv1 and not a): #root is here, go deeper, return 0
            print('rerun calculation in eta1 = '+ str(eta1)+' and eta2 = ' + str(eta2))
            return 0
        elif(abs(eta1-eta2)>conv1 and a):#root is not here, return 2
            print('root not in eta1 = '+ str(eta1) + ' and eta2 = '+str(eta2))
            return 2
        else: 
            #print('error')
            print('onset point between eta1 = '+str(eta1)+' and eta2 = '+str(2*eta2-eta1))
            exit()
    else:
        print('too small to compare, break')
        print(eta1, eta2)
        exit()
def bisection(eta1, eta2, len1, len2, del_eta):
    while(abs(eta1-eta2)>del_eta*0.00001):
        eta12=(eta1+eta2)*0.5
        print('run for eta12='+str(eta12))
        del_eta_new=del_eta*0.793
        len12=run_cc(eta12, del_eta)
        b=checker(eta1, eta12, len1, len12, del_eta)
        if(b==0):
            eta2=eta12
            len2=len12
            del_eta=del_eta_new
            bisection(eta1, eta2, len1, len2, del_eta)
        elif(b==2):
            eta1=eta12
            len1=len12
            del_eta=del_eta_new
            bisection(eta1, eta2, len1, len2, del_eta)
            #print('difference too small to compare', eta1, eta2, len1, len2, del_eta_new)
            return eta1, eta2, len1, len2, del_eta
eta=0.36642
feig_cons=4.7
del_eta=0.00002
num_iter=25
len1=run_cc(eta, del_eta)
#print(len1)
for i in range(num_iter):
    len2=run_cc(eta+del_eta, del_eta)
    x1=eta
    x2=eta+del_eta
    x3=len1
    x4=len2
    x5=del_eta
    a=checker(x1, x2, x3, x4, x5)
    if (a==1):
        del_eta=del_eta/feig_cons
        eta=eta+del_eta
    else: 
        if(a==0):
            bisection(x1, x2, x3, x4, x5)
        else: 
            eta=eta+del_eta
            len1=len2
