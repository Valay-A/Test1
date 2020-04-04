import numpy as np          
import math

def run(eta, del_eta):   #add couple cluster code here
    x=0.6 
    n_iter=int(1000/del_eta)  # to change the number of steps according to the accuracy required
    if(n_iter>30000000):
        print('max iterations reached')
        n_iter=30000000  #checks the number of steps, not more than a million
    resfile=np.zeros([n_iter])
    for i in range(n_iter):
        y=eta*x*(1-x)               #results here
        resfile[i]=("%.7f" %y)     #truncate results   for 9 decimals
        x=y #actual couple cluster stuff
    result=np.array(resfile[-200:])
    uniq=np.unique(result)
    print('completed simulation with eta = '+str(eta) + ' and del_eta = '+ str(del_eta) + 'and iteration steps = '+str(n_iter)+' energies = ' + str(len(uniq)))
    return len(np.unique(np.array(resfile[-200:])))

def period():
    return math.log(len(uniq),2)

def checker(eta1, eta2, len1, len2, del_eta):
    b=(len1==len2)
    conv1=del_eta*0.001
    print('checking convergence of eta1 = ' +str(eta1) +' and eta2 = ' +str(eta2)+' with convergence limit = '+str(conv1))
    while(conv1>0.0000000001):
        if (abs(eta1-eta2)<conv1 and not b): #convergence reached, return 1
            print('eta1 and eta2 converged')
            return 1
        elif(abs(eta1-eta2)>conv1 and not b): #root is here, go deeper, return 0
            print('rerun calculation in eta1 = '+ str(eta1)+ ' and eta2 = ' + str(eta2) + ' with del_eta = '+ str(del_eta))
            return 0
        elif(abs(eta1-eta2)>conv1 and b):#root is not here, return 2
            print('root not in eta1 = '+ str(eta1) + ' and eta2 = '+str(eta2))
            return 2
        else: #there is some error
            print('error in program, relook at dynamic limit checker')
    else: 
        print('too small to compare, break')
        #break

def bisection(eta1, eta2, len1, len2, del_eta):
    while(abs(eta1-eta2)>del_eta*0.00001):
        eta12=(eta1+eta2)*0.5
        print(eta12) 
        del_eta_new = del_eta*0.5
        len12=run(eta12, del_eta)  
        b=checker(eta1, eta12, len1, len12, del_eta) 
        if (b==1):
            print('found root', eta1, eta2, len1, len2, del_eta)
            return eta1, eta12, len1, len12, del_eta  
        if (b==0):
            eta2=eta12
            len2=len12
            del_eta=del_eta_new
        else:
            eta1=eta12
            len1=len12
            del_eta=del_eta_new
    print('difference too small to compare', eta1, eta2, len1, len2, del_eta_new)
    return eta1, eta2, len1, len2, del_eta                      
#main
eta=3.569
feig_cons=4.7
del_eta=0.0001
num_iter=25 
len1=run(eta, del_eta)
for i in range(num_iter):
    len2=run(eta+del_eta, del_eta)
    x1=eta
    x2=eta+del_eta
    x3=len1
    x4=len2
    x5=del_eta
    a=checker(x1, x2, x3, x4, x5)
    if (a==1): 
        print(eta, eta+del_eta, len1, len2, del_eta,'root found')
        del_eta=del_eta/feig_cons
        eta=eta+del_eta
    else:
        if(a==0):
            bisection(x1, x2, x3, x4, x5)
        else: 
            print('next step = '+str(eta+del_eta) + 'with del_eta = ' +str(del_eta) )
            eta=eta+del_eta
            len1=len2
