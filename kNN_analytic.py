import numpy as np
from scipy.special import gamma, gammaln

def Erlang(k, lam, x):
    if k == 0:
        klamx = lam * x
        gammak = 1
    else:
        klamx = k * lam * x
        gammak = gamma(k)
#    return (klamx) ** k / gammak * np.exp(-klamx)
    return np.exp(k*np.log(klamx) -klamx -gammaln(k))

def PPoisson(k, nV): 
    ''' Calculates the probability of finding exactly k points in a volume V of a Poisson process
    with mean number density n. 
	See section 3.1 of Banerjee and Abel https://arxiv.org/abs/2007.13342 
	'''
    if k == 0:
        return np.exp(-nV)
    else:
        return Erlang(k, 1/k, nV)/k

# when we get alot of overflow warnings we could turn the output off while debugging the issue
#import warnings  
#suppress warnings
#warnings.filterwarnings('ignore')
# 
def PGaussian(k, nV, sig):
	''' Calculates the probabilities of finding exactly k points in a volume V for a 
	Gaussian random field which has a rms sigma_V given by the array sig and mean 
	number density n.
	See section 3.2 of Banerjee and Abel https://arxiv.org/abs/2007.13342 
	for more detail of the Gaussian random field aspect and equation 8 in that paper
	which define these P_{k|V}. 	
	'''
	return { 0: OneMinusPGg0 \
			,1: PG1 \
			,2: PG2 \
			,3: PG3 \
			,4: PG4 \
			,5: PG5 \
			,6: PG6 \
			,7: PG7 \
			,8: PG8 \
			,9: PG9 \
			,10: PG10 \
			,11: PG11 \
			,12: PG12 \
			,13: PG13 \
			,14: PG14 \
			,15: PG15 \
			,16: PG16 \
			,17: PG17 \
			,18: PG18 \
			,19: PG19 \
			,20: PG20 \
		}.get(k, OneMinusPGg0)(nV, sig)    # OneMinusPGg0 will be returned default if x is not found

def CDFGaussian(k, nV, sig):
	''' Calculates the CDF of finding >k points in a volume V for a 
	Gaussian random field which has a rms sigma_V given by the array sig and mean 
	number density n.
	See section 3.2 of Banerjee and Abel https://arxiv.org/abs/2007.13342 
	for more detail of the Gaussian random field aspect and equation 8 in that paper
	which define these P_{k|V}. 	
	'''
	return { 0: PGg0 \
			,1: PGg1 \
			,2: PGg2 \
			,3: PGg3 \
			,4: PGg4 \
			,5: PGg5 \
			,6: PGg6 \
			,7: PGg7 \
			,8: PGg8 \
			,9: PGg9 \
			,10: PGg10 \
			,11: PGg11 \
			,12: PGg12 \
			,13: PGg13 \
		}.get(k, PGg0)(nV, sig)    # PG_0 will be returned default if x is not found

''' This code is generated with Mathematica. 
Here it is the source, just in case you ever need to change anything.
PG[n_] := 
 SeriesCoefficient[(1 - Exp[nV (x - 1) + nV^2/2 \[Sigma]^2 (x - 1)^2])/(1 - x), {x, 0, n}] 
Print["def PGg0(nV,sig):\n\treturn ", FortranForm[PG[0] /. {\[Sigma] -> sig}] ]
Print["def OneMinusPGg0(nV,sig):\n\treturn ",  FortranForm[1 - PG[0] /. {\[Sigma] -> sig}] ]

For[i = 1, i < 21, i++, 
 If[i < 14,
  Print["\ndef PGg", i, "(nV, sig)", 
   ":\n\treturn PGg0(nV,sig)+OneMinusPGg0(nV,sig)*(", 
   FortranForm[
    FullSimplify[(PG[i] - (PG[0]))/(1 - PG[0])] /. {\[Sigma] -> 
       sig}] , ")"] ];
 Print["def PG", i, "(nV, sig)", 
  ":\n\treturn OneMinusPGg0(nV,sig)*(", 
  FortranForm[
   FullSimplify[(PG[i - 1] - PG[i])/(1 - PG[0])] /. {\[Sigma] -> 
      sig}] , ")"]]
'''
def PGg0(nV,sig):
	return 1 - np.exp(-nV + (nV**2*sig**2)/2.)

def OneMinusPGg0(nV,sig):
	return np.exp(-nV + (nV**2*sig**2)/2.)

PG0 = OneMinusPGg0


def PGg1(nV, sig):
	return PGg0(nV,sig)+OneMinusPGg0(nV,sig)*(nV*(-1 + nV*sig**2))

def PG1(nV, sig):
	return (-(np.exp((nV*(-2 + nV*sig**2))/2.)*nV*(-1 + nV*sig**2)))


def PGg2(nV, sig):
	return PGg0(nV,sig)+OneMinusPGg0(nV,sig)*(-0.5*(nV*(2 + nV - nV*(1 + 2*nV)*sig**2 + nV**3*sig**4)))

def PG2(nV, sig):
	return ((np.exp((nV*(-2 + nV*sig**2))/2.)*(nV**2*sig**2 + (nV - nV**2*sig**2)**2))/2.)


def PGg3(nV, sig):
	return PGg0(nV,sig)+OneMinusPGg0(nV,sig)*((nV*(-6 - nV*(3 + nV) + 3*nV*(1 + nV + nV**2)*sig**2 - 3*nV**4*sig**4 + nV**5*sig**6))/6.)

def PG3(nV, sig):
	return (-0.16666666666666666*(np.exp((nV*(-2 + nV*sig**2))/2.)*nV**3*(-1 + nV*sig**2)*(1 + sig**2*(3 + nV*(-2 + nV*sig**2)))))


def PGg4(nV, sig):
	return PGg0(nV,sig)+OneMinusPGg0(nV,sig)*((nV*(-24 - nV*(12 + nV*(4 + nV)) + 2*nV*(6 + nV*(6 + nV*(3 + 2*nV)))*sig**2 - 3*nV**3*(1 + 2*nV**2)*sig**4 + 2*nV**5*(-1 + 2*nV)*sig**6 - nV**7*sig**8))/24.)

def PG4(nV, sig):
	return ((np.exp((nV*(-2 + nV*sig**2))/2.)*nV**4*(1 + sig**2*(3*(2 + sig**2) + nV*(-2 + nV*sig**2)*(2 + sig**2*(6 + nV*(-2 + nV*sig**2))))))/24.)


def PGg5(nV, sig):
	return PGg0(nV,sig)+OneMinusPGg0(nV,sig)*((nV*(-120 - nV*(60 + nV*(20 + nV*(5 + nV))) + 5*nV*(12 + nV*(2 + nV)*(6 + nV**2))*sig**2 - 5*nV**3*(3 + 3*nV + 2*nV**3)*sig**4 + 5*nV**5*(1 + 2*(-1 + nV)*nV)*sig**6 - 5*(-1 + nV)*nV**7*sig**8 + nV**9*sig**10))/120.)

def PG5(nV, sig):
	return (-0.008333333333333333*(np.exp((nV*(-2 + nV*sig**2))/2.)*nV**5*(-1 + nV*sig**2)*(1 + sig**2*(5*(2 + 3*sig**2) + nV*(-2 + nV*sig**2)*(2 - 2*(-5 + nV)*sig**2 + nV**2*sig**4)))))


def PGg6(nV, sig):
	return PGg0(nV,sig)+OneMinusPGg0(nV,sig)*((nV*(-720 - nV*(360 + nV*(120 + nV*(30 + nV*(6 + nV)))) + 3*nV*(120 + nV*(120 + nV*(60 + nV*(20 + nV*(5 + 2*nV)))))*sig**2 - 15*nV**3*(6 + nV*(6 + 3*nV + nV**3))*sig**4 + 5*nV**5*(3 + 2*nV*(3 + nV*(-3 + 2*nV)))*sig**6 - 15*(-1 + nV)**2*nV**7*sig**8 + 3*nV**9*(-3 + 2*nV)*sig**10 - nV**11*sig**12))/720.)

def PG6(nV, sig):
	return ((np.exp((nV*(-2 + nV*sig**2))/2.)*nV**6*(1 + sig**2*(15 - 6*nV + 15*(-3 + nV)*(-1 + nV)*sig**2 + 5*(3 - 2*(-3 + nV)*nV*(-3 + 2*nV))*sig**4 + 15*(-3 + nV)*(-1 + nV)*nV**2*sig**6 + 3*(5 - 2*nV)*nV**4*sig**8 + nV**6*sig**10)))/720.)


def PGg7(nV, sig):
	return PGg0(nV,sig)+OneMinusPGg0(nV,sig)*(-nV + (nV**2*(-1 + sig**2))/2. + (nV**3*(-840 - nV*(210 + nV*(42 + nV*(7 + nV))) + 7*(360 + nV*(180 + nV*(60 + nV*(15 + nV*(3 + nV)))))*sig**2 - 21*nV*(30 + nV*(30 + nV*(15 + 5*nV + nV**3)))*sig**4 + 35*nV**3*(3 + nV*(3 + nV*(3 + (-2 + nV)*nV)))*sig**6 - 35*nV**6*(3 + (-3 + nV)*nV)*sig**8 + 21*(-2 + nV)*(-1 + nV)*nV**7*sig**10 - 7*(-2 + nV)*nV**9*sig**12 + nV**11*sig**14))/5040.)

def PG7(nV, sig):
	return (-0.0001984126984126984*(np.exp((nV*(-2 + nV*sig**2))/2.)*nV**7*(-1 + nV*sig**2)*(1 + sig**2*(21 - 6*nV + 3*(35 + nV*(-28 + 5*nV))*sig**2 + (105 - 2*nV*(105 + nV*(-63 + 10*nV)))*sig**4 + 3*nV**2*(35 + nV*(-28 + 5*nV))*sig**6 + 3*(7 - 2*nV)*nV**4*sig**8 + nV**6*sig**10))))


def PGg8(nV, sig):
	return PGg0(nV,sig)+OneMinusPGg0(nV,sig)*(-nV + (nV**2*(-1 + sig**2))/2. + (nV**3*(-6720 - nV*(1680 + nV*(336 + nV*(56 + nV*(8 + nV)))) + 4*(5040 + nV*(2520 + nV*(840 + nV*(210 + nV*(42 + nV*(7 + 2*nV))))))*sig**2 - 14*nV*(360 + nV*(360 + nV*(180 + nV*(60 + 15*nV + 2*nV**3))))*sig**4 + 28*nV**3*(30 + nV*(30 + nV*(15 + nV*(10 + nV*(-5 + 2*nV)))))*sig**6 - 35*nV**5*(3 + 2*nV**2*(6 + (-4 + nV)*nV))*sig**8 + 28*nV**7*(-3 + nV*(12 + nV*(-9 + 2*nV)))*sig**10 - 14*nV**9*(7 + 2*(-4 + nV)*nV)*sig**12 + 4*nV**11*(-5 + 2*nV)*sig**14 - nV**13*sig**16))/40320.)

def PG8(nV, sig):
	return ((np.exp((nV*(-2 + nV*sig**2))/2.)*nV**8*(1 + sig**2*(28 - 8*nV + 14*(15 + 2*(-6 + nV)*nV)*sig**2 + 28*(15 + nV*(-30 + (15 - 2*nV)*nV))*sig**4 + 35*(3 + 2*(-2 + nV)*nV*(6 + (-6 + nV)*nV))*sig**6 + 28*nV**2*(15 + nV*(-30 + (15 - 2*nV)*nV))*sig**8 + 14*nV**4*(15 + 2*(-6 + nV)*nV)*sig**10 + 4*(7 - 2*nV)*nV**6*sig**12 + nV**8*sig**14)))/40320.)


def PGg9(nV, sig):
	return PGg0(nV,sig)+OneMinusPGg0(nV,sig)*(-nV + (nV**2*(-1 + sig**2))/2. + (nV**3*(-60480 - nV*(15120 + nV*(3024 + nV*(504 + nV*(72 + nV*(9 + nV))))) + 9*(20160 + nV*(10080 + nV*(3360 + nV*(840 + nV*(168 + nV*(28 + nV*(4 + nV)))))))*sig**2 - 18*nV*(2520 + nV*(2520 + nV*(1260 + nV*(420 + nV*(105 + 21*nV + 2*nV**3)))))*sig**4 + 42*nV**3*(180 + nV*(180 + nV*(90 + nV*(30 + nV*(15 + 2*(-3 + nV)*nV)))))*sig**6 - 63*nV**5*(15 + 15*nV + 2*nV**3*(10 + (-5 + nV)*nV))*sig**8 + 63*nV**7*(3 + 2*nV*(-6 + nV*(12 + (-6 + nV)*nV)))*sig**10 - 42*(-3 + nV)*nV**9*(3 + 2*(-3 + nV)*nV)*sig**12 + 18*nV**11*(11 + 2*(-5 + nV)*nV)*sig**14 - 9*(-3 + nV)*nV**13*sig**16 + nV**15*sig**18))/362880.)

def PG9(nV, sig):
	return (-2.7557319223985893e-6*(np.exp((nV*(-2 + nV*sig**2))/2.)*nV**9*(-1 + nV*sig**2)*(1 + sig**2*(36 - 8*nV + (378 + 4*nV*(-54 + 7*nV))*sig**2 + 4*(315 + nV*(-378 + (135 - 14*nV)*nV))*sig**4 + (945 + 2*nV*(-1260 + nV*(1134 + 5*nV*(-72 + 7*nV))))*sig**6 + 4*nV**2*(315 + nV*(-378 + (135 - 14*nV)*nV))*sig**8 + 2*nV**4*(189 + 2*nV*(-54 + 7*nV))*sig**10 + 4*(9 - 2*nV)*nV**6*sig**12 + nV**8*sig**14))))


def PGg10(nV, sig):
	return PGg0(nV,sig)+OneMinusPGg0(nV,sig)*(-nV + (nV**2*(-1 + sig**2))/2. + (nV**3*(-1 + 3*sig**2))/6. + (nV**4*(-151200 - nV*(30240 + nV*(5040 + nV*(720 + nV*(90 + nV*(10 + nV))))) + 5*(181440 + nV*(60480 + nV*(15120 + nV*(3024 + nV*(504 + nV*(72 + nV*(9 + 2*nV)))))))*sig**2 - 45*(10080 + nV*(10080 + nV*(5040 + nV*(1680 + nV*(420 + nV*(84 + 14*nV + nV**3))))))*sig**4 + 30*nV**2*(2520 + nV*(2520 + nV*(1260 + nV*(420 + nV*(105 + 2*nV*(21 + nV*(-7 + 2*nV)))))))*sig**6 - 105*nV**4*(90 + nV*(90 + 45*nV + 2*nV**3*(15 + (-6 + nV)*nV)))*sig**8 + 63*nV**6*(15 + 2*nV*(15 + nV*(-30 + nV*(40 + nV*(-15 + 2*nV)))))*sig**10 - 105*nV**8*(9 + 2*(-3 + nV)**2*(-2 + nV)*nV)*sig**12 + 30*nV**10*(-39 + 2*nV*(33 + nV*(-15 + 2*nV)))*sig**14 - 45*(-4 + nV)*(-2 + nV)*nV**12*sig**16 + 5*nV**14*(-7 + 2*nV)*sig**18 - nV**16*sig**20))/3.6288e6)

def PG10(nV, sig):
	return ((np.exp((nV*(-2 + nV*sig**2))/2.)*nV**10*(1 + 5*(9 - 2*nV)*sig**2 + 45*(14 + (-8 + nV)*nV)*sig**4 - 30*(-105 + 2*nV*(63 + nV*(-21 + 2*nV)))*sig**6 + 105*(45 + 2*nV*(-60 + nV*(45 + (-12 + nV)*nV)))*sig**8 - 63*(-15 + 2*nV*(5 + (-5 + nV)*nV)*(15 + nV*(-15 + 2*nV)))*sig**10 + 105*nV**2*(45 + 2*nV*(-60 + nV*(45 + (-12 + nV)*nV)))*sig**12 - 30*nV**4*(-105 + 2*nV*(63 + nV*(-21 + 2*nV)))*sig**14 + 45*nV**6*(14 + (-8 + nV)*nV)*sig**16 + 5*(9 - 2*nV)*nV**8*sig**18 + nV**10*sig**20))/3.6288e6)


def PGg11(nV, sig):
	return PGg0(nV,sig)+OneMinusPGg0(nV,sig)*(-nV + (nV**2*(-1 + sig**2))/2. + (nV**3*(-1 + 3*sig**2))/6. + (nV**4*(-1663200 - nV*(332640 + nV*(55440 + nV*(7920 + nV*(990 + nV*(110 + nV*(11 + nV)))))) + 11*(907200 + nV*(302400 + nV*(75600 + nV*(15120 + nV*(2520 + nV*(360 + nV*(45 + nV*(5 + nV))))))))*sig**2 - 55*(90720 + nV*(90720 + nV*(45360 + nV*(15120 + nV*(3780 + nV*(756 + nV*(126 + 18*nV + nV**3)))))))*sig**4 + 165*nV**2*(5040 + nV*(5040 + nV*(2520 + nV*(840 + nV*(210 + nV*(42 + nV*(14 + (-4 + nV)*nV)))))))*sig**6 - 165*nV**4*(630 + nV*(630 + nV*(315 + 105*nV + 2*nV**3*(21 + (-7 + nV)*nV))))*sig**8 + 231*nV**6*(45 + nV*(45 + nV*(45 + 2*nV*(-30 + nV*(30 + (-9 + nV)*nV)))))*sig**10 - 231*nV**9*(45 + 2*nV*(-45 + nV*(35 + (-10 + nV)*nV)))*sig**12 + 165*nV**10*(27 + 2*nV*(-39 + nV*(33 + (-10 + nV)*nV)))*sig**14 - 165*(-3 + nV)*nV**12*(6 + (-6 + nV)*nV)*sig**16 + 55*nV**14*(11 + (-7 + nV)*nV)*sig**18 - 11*(-4 + nV)*nV**16*sig**20 + nV**18*sig**22))/3.99168e7)

def PG11(nV, sig):
	return (-2.505210838544172e-8*(np.exp((nV*(-2 + nV*sig**2))/2.)*nV**11*(-1 + nV*sig**2)*(1 + sig**2*(55 - 10*nV + 5*(198 + nV*(-88 + 9*nV))*sig**2 + 10*(693 - 2*nV*(297 + nV*(-77 + 6*nV)))*sig**4 + 5*(3465 + 2*nV*(-2772 + nV*(1485 + 7*nV*(-44 + 3*nV))))*sig**6 + (10395 - 2*nV*(17325 + nV*(-20790 + nV*(9900 + 7*nV*(-275 + 18*nV)))))*sig**8 + 5*nV**2*(3465 + 2*nV*(-2772 + nV*(1485 + 7*nV*(-44 + 3*nV))))*sig**10 + 10*nV**4*(693 - 2*nV*(297 + nV*(-77 + 6*nV)))*sig**12 + 5*nV**6*(198 + nV*(-88 + 9*nV))*sig**14 + 5*(11 - 2*nV)*nV**8*sig**16 + nV**10*sig**18))))


def PGg12(nV, sig):
	return PGg0(nV,sig)+OneMinusPGg0(nV,sig)*(-nV + (nV**2*(-1 + sig**2))/2. + (nV**3*(-1 + 3*sig**2))/6. + (nV**4*(-(nV*(3991680 + nV*(665280 + nV*(95040 + nV*(11880 + nV*(1320 + nV*(132 + nV*(12 + nV)))))))) + 6*nV*(6652800 + nV*(1663200 + nV*(332640 + nV*(55440 + nV*(7920 + nV*(990 + nV*(110 + nV*(11 + 2*nV))))))))*sig**2 - 33*(1814400 + nV*(1814400 + nV*(907200 + nV*(302400 + nV*(75600 + nV*(15120 + nV*(2520 + nV*(360 + 45*nV + 2*nV**3))))))))*sig**4 + 110*nV**2*(90720 + nV*(90720 + nV*(45360 + nV*(15120 + nV*(3780 + nV*(756 + nV*(126 + nV*(36 + nV*(-9 + 2*nV)))))))))*sig**6 - 495*nV**4*(2520 + nV*(2520 + nV*(1260 + nV*(420 + 105*nV + nV**3*(28 + (-8 + nV)*nV)))))*sig**8 + 198*nV**6*(630 + nV*(630 + nV*(315 + 2*nV*(105 + nV*(-105 + nV*(84 + nV*(-21 + 2*nV)))))))*sig**10 - 231*nV**8*(45 + 2*nV**2*(135 + nV*(-180 + nV*(105 + 2*(-12 + nV)*nV))))*sig**12 + 198*nV**10*(-45 + 2*nV*(135 + nV*(-195 + nV*(110 + nV*(-25 + 2*nV)))))*sig**14 - 495*nV**12*(33 + (-6 + nV)*nV*(12 + (-6 + nV)*nV))*sig**16 + 110*nV**14*(-60 + nV*(66 + nV*(-21 + 2*nV)))*sig**18 - 33*nV**16*(29 + 2*(-8 + nV)*nV)*sig**20 + 6*nV**18*(-9 + 2*nV)*sig**22 - nV**20*sig**24 + 19958400*(-1 + 6*sig**2)))/4.790016e8)

def PG12(nV, sig):
	return ((np.exp((nV*(-2 + nV*sig**2))/2.)*nV**12*(1 + sig**2*(66 - 12*nV + 33*(45 + 2*(-10 + nV)*nV)*sig**2 - 110*(-126 + nV*(108 + nV*(-27 + 2*nV)))*sig**4 + 495*(105 + nV*(-168 + nV*(84 + (-16 + nV)*nV)))*sig**6 - 198*(-315 + 2*nV*(525 + nV*(-525 + nV*(210 + nV*(-35 + 2*nV)))))*sig**8 + 231*(45 + 2*(-3 + nV)*nV*(90 + nV*(-195 + nV*(135 + 2*(-15 + nV)*nV))))*sig**10 - 198*nV**2*(-315 + 2*nV*(525 + nV*(-525 + nV*(210 + nV*(-35 + 2*nV)))))*sig**12 + 495*nV**4*(105 + nV*(-168 + nV*(84 + (-16 + nV)*nV)))*sig**14 - 110*nV**6*(-126 + nV*(108 + nV*(-27 + 2*nV)))*sig**16 + 33*nV**8*(45 + 2*(-10 + nV)*nV)*sig**18 + 6*(11 - 2*nV)*nV**10*sig**20 + nV**12*sig**22)))/4.790016e8)


def PGg13(nV, sig):
	return PGg0(nV,sig)+OneMinusPGg0(nV,sig)*(-nV + (nV**2*(-1 + sig**2))/2. + (nV**3*(-1 + 3*sig**2))/6. + (nV**4*(-(nV*(51891840 + nV*(8648640 + nV*(1235520 + nV*(154440 + nV*(17160 + nV*(1716 + nV*(156 + nV*(13 + nV))))))))) + 13*nV*(39916800 + nV*(9979200 + nV*(1995840 + nV*(332640 + nV*(47520 + nV*(5940 + nV*(660 + nV*(66 + nV*(6 + nV)))))))))*sig**2 - 39*(19958400 + nV*(19958400 + nV*(9979200 + nV*(3326400 + nV*(831600 + nV*(166320 + nV*(27720 + nV*(3960 + nV*(495 + 55*nV + 2*nV**3)))))))))*sig**4 + 143*nV**2*(907200 + nV*(907200 + nV*(453600 + nV*(151200 + nV*(37800 + nV*(7560 + nV*(1260 + nV*(180 + nV*(45 + 2*(-5 + nV)*nV)))))))))*sig**6 - 715*nV**4*(22680 + nV*(22680 + nV*(11340 + nV*(3780 + nV*(945 + 189*nV + nV**3*(36 + (-9 + nV)*nV))))))*sig**8 + 1287*nV**6*(1260 + nV*(1260 + nV*(630 + nV*(210 + nV*(105 + nV*(-84 + nV*(56 + (-12 + nV)*nV)))))))*sig**10 - 429*nV**8*(315 + 315*nV + 2*nV**3*(315 + nV*(-315 + nV*(147 + 2*(-14 + nV)*nV))))*sig**12 + 429*nV**10*(45 + 2*nV*(-135 + nV*(405 + nV*(-390 + nV*(165 + 2*(-15 + nV)*nV)))))*sig**14 - 1287*nV**12*(-45 + nV*(165 + nV*(-180 + nV*(80 + (-15 + nV)*nV))))*sig**16 + 715*nV**14*(69 + nV*(-120 + nV*(66 + (-14 + nV)*nV)))*sig**18 - 143*nV**16*(-93 + nV*(87 + 2*(-12 + nV)*nV))*sig**20 + 39*nV**18*(37 + 2*(-9 + nV)*nV)*sig**22 - 13*(-5 + nV)*nV**20*sig**24 + nV**22*sig**26 + 259459200*(-1 + 6*sig**2)))/6.2270208e9)

def PG13(nV, sig):
	return (-1.6059043836821613e-10*(np.exp((nV*(-2 + nV*sig**2))/2.)*nV**13*(-1 + nV*sig**2)*(1 + sig**2*(-12*nV**11*sig**20 + nV**12*sig**22 + 6*nV**10*sig**18*(11 + 13*sig**2) - 20*nV**9*sig**16*(11 + 39*sig**2) + 39*(2 + 55*sig**2) + 15*nV**8*sig**14*(33 + 234*sig**2 + 143*sig**4) - 24*nV**7*sig**12*(33 + 390*sig**2 + 715*sig**4) - 24*nV**5*sig**8*(33 + 819*sig**2 + 715*sig**4*(7 + 9*sig**2)) + 6435*sig**4*(4 + 21*(sig + sig**3)**2) + 12*nV**6*sig**10*(77 + 65*sig**2*(21 + 77*sig**2 + 33*sig**4)) - 20*nV**3*sig**4*(11 + 39*sig**2*(12 + 154*sig**2 + 660*sig**4 + 693*sig**6)) + 15*nV**4*sig**6*(33 + 13*sig**2*(84 + 770*sig**2 + 1980*sig**4 + 693*sig**6)) - 12*nV*(1 + 65*(sig**2 + 22*sig**4 + 198*sig**6 + 693*sig**8 + 693*sig**10)) + 6*nV**2*sig**2*(11 + 65*sig**2*(9 + 11*sig**2*(14 + 90*sig**2 + 63*sig**4*(3 + sig**2))))))))

def PG14(nV, sig):
	return ((np.exp((nV*(-2 + nV*sig**2))/2.)*nV**14*(1 + sig**2*(91 - 14*nV + 91*(33 + (-12 + nV)*nV)*sig**2 - 91*(-495 + 2*nV*(165 + nV*(-33 + 2*nV)))*sig**4 + 1001*(315 + nV*(-360 + nV*(135 + (-20 + nV)*nV)))*sig**6 - 1001*(-945 + nV*(1890 + nV*(-1260 + nV*(360 + nV*(-45 + 2*nV)))))*sig**8 + 3003*(315 + nV*(-1260 + nV*(1575 + nV*(-840 + nV*(210 + (-24 + nV)*nV)))))*sig**10 - 429*(-315 + 2*nV*(2205 + nV*(-6615 + nV*(7350 + nV*(-3675 + 2*nV*(441 + nV*(-49 + 2*nV)))))))*sig**12 + 3003*nV**2*(315 + nV*(-1260 + nV*(1575 + nV*(-840 + nV*(210 + (-24 + nV)*nV)))))*sig**14 - 1001*nV**4*(-945 + nV*(1890 + nV*(-1260 + nV*(360 + nV*(-45 + 2*nV)))))*sig**16 + 1001*nV**6*(315 + nV*(-360 + nV*(135 + (-20 + nV)*nV)))*sig**18 - 91*nV**8*(-495 + 2*nV*(165 + nV*(-33 + 2*nV)))*sig**20 + 91*nV**10*(33 + (-12 + nV)*nV)*sig**22 + 7*(13 - 2*nV)*nV**12*sig**24 + nV**14*sig**26)))/8.71782912e10)

def PG15(nV, sig):
	return ((np.exp((nV*(-2 + nV*sig**2))/2.)*nV**15*(1 - 15*(-7 + nV)*sig**2 + 105*(39 + (-13 + nV)*nV)*sig**4 - 455*(-165 + nV*(99 + (-18 + nV)*nV))*sig**6 + 1365*(495 + nV*(-495 + nV*(165 + (-22 + nV)*nV)))*sig**8 - 3003*(-945 + nV*(1575 + nV*(-900 + nV*(225 + (-25 + nV)*nV))))*sig**10 + 5005*(945 + nV*(-2835 + nV*(2835 + nV*(-1260 + nV*(270 + (-27 + nV)*nV)))))*sig**12 - 6435*(-315 + nV*(2205 + nV*(-4410 + nV*(3675 + nV*(-1470 + nV*(294 + (-28 + nV)*nV))))))*sig**14 + 6435*nV*(-315 + nV*(2205 + nV*(-4410 + nV*(3675 + nV*(-1470 + nV*(294 + (-28 + nV)*nV))))))*sig**16 - 5005*nV**3*(945 + nV*(-2835 + nV*(2835 + nV*(-1260 + nV*(270 + (-27 + nV)*nV)))))*sig**18 + 3003*nV**5*(-945 + nV*(1575 + nV*(-900 + nV*(225 + (-25 + nV)*nV))))*sig**20 - 1365*nV**7*(495 + nV*(-495 + nV*(165 + (-22 + nV)*nV)))*sig**22 + 455*nV**9*(-165 + nV*(99 + (-18 + nV)*nV))*sig**24 - 105*nV**11*(39 + (-13 + nV)*nV)*sig**26 + 15*(-7 + nV)*nV**13*sig**28 - nV**15*sig**30))/1.307674368e12)

def PG16(nV, sig):
	return ((np.exp((nV*(-2 + nV*sig**2))/2.)*nV**16*(1 + 8*(15 - 2*nV)*sig**2 + 60*(91 + 2*(-14 + nV)*nV)*sig**4 - 280*(-429 + nV*(234 + nV*(-39 + 2*nV)))*sig**6 + 910*(1485 + 2*nV*(-660 + nV*(198 + (-24 + nV)*nV)))*sig**8 - 2184*(-3465 + nV*(4950 + nV*(-2475 + nV*(550 + nV*(-55 + 2*nV)))))*sig**10 + 4004*(4725 + nV*(-11340 + nV*(9450 + nV*(-3600 + nV*(675 + 2*(-30 + nV)*nV)))))*sig**12 - 5720*(-2835 + nV*(13230 + nV*(-19845 + nV*(13230 + nV*(-4410 + nV*(756 + nV*(-63 + 2*nV)))))))*sig**14 + 6435*(315 + 2*nV*(-2520 + nV*(8820 + nV*(-11760 + nV*(7350 + nV*(-2352 + nV*(392 + (-32 + nV)*nV)))))))*sig**16 - 5720*nV**2*(-2835 + nV*(13230 + nV*(-19845 + nV*(13230 + nV*(-4410 + nV*(756 + nV*(-63 + 2*nV)))))))*sig**18 + 4004*nV**4*(4725 + nV*(-11340 + nV*(9450 + nV*(-3600 + nV*(675 + 2*(-30 + nV)*nV)))))*sig**20 - 2184*nV**6*(-3465 + nV*(4950 + nV*(-2475 + nV*(550 + nV*(-55 + 2*nV)))))*sig**22 + 910*nV**8*(1485 + 2*nV*(-660 + nV*(198 + (-24 + nV)*nV)))*sig**24 - 280*nV**10*(-429 + nV*(234 + nV*(-39 + 2*nV)))*sig**26 + 60*nV**12*(91 + 2*(-14 + nV)*nV)*sig**28 + 8*(15 - 2*nV)*nV**14*sig**30 + nV**16*sig**32))/2.0922789888e13)

def PG17(nV, sig):
	return ((np.exp((nV*(-2 + nV*sig**2))/2.)*nV**17*(1 - 17*(-8 + nV)*sig**2 + 68*(105 + 2*(-15 + nV)*nV)*sig**4 - 340*(-546 + nV*(273 + 2*(-21 + nV)*nV))*sig**6 + 1190*(2145 + 2*nV*(-858 + nV*(234 + (-26 + nV)*nV)))*sig**8 - 3094*(-5940 + nV*(7425 + 2*nV*(-1650 + nV*(330 + (-30 + nV)*nV))))*sig**10 + 6188*(10395 + nV*(-20790 + nV*(14850 + nV*(-4950 + nV*(825 + 2*(-33 + nV)*nV)))))*sig**12 - 9724*(-9450 + nV*(33075 + nV*(-39690 + nV*(22050 + nV*(-6300 + nV*(945 + 2*(-35 + nV)*nV))))))*sig**14 + 12155*(2835 + 2*nV*(-11340 + nV*(26460 + nV*(-26460 + nV*(13230 + nV*(-3528 + nV*(504 + (-36 + nV)*nV)))))))*sig**16 - 12155*nV*(2835 + 2*nV*(-11340 + nV*(26460 + nV*(-26460 + nV*(13230 + nV*(-3528 + nV*(504 + (-36 + nV)*nV)))))))*sig**18 + 9724*nV**3*(-9450 + nV*(33075 + nV*(-39690 + nV*(22050 + nV*(-6300 + nV*(945 + 2*(-35 + nV)*nV))))))*sig**20 - 6188*nV**5*(10395 + nV*(-20790 + nV*(14850 + nV*(-4950 + nV*(825 + 2*(-33 + nV)*nV)))))*sig**22 + 3094*nV**7*(-5940 + nV*(7425 + 2*nV*(-1650 + nV*(330 + (-30 + nV)*nV))))*sig**24 - 1190*nV**9*(2145 + 2*nV*(-858 + nV*(234 + (-26 + nV)*nV)))*sig**26 + 340*nV**11*(-546 + nV*(273 + 2*(-21 + nV)*nV))*sig**28 - 68*nV**13*(105 + 2*(-15 + nV)*nV)*sig**30 + 17*(-8 + nV)*nV**15*sig**32 - nV**17*sig**34))/3.55687428096e14)

def PG18(nV, sig):
	return ((np.exp((nV*(-2 + nV*sig**2))/2.)*nV**18*(1 + 9*(17 - 2*nV)*sig**2 + 153*(-10 + nV)*(-6 + nV)*sig**4 - 204*(-1365 + 2*nV*(315 + nV*(-45 + 2*nV)))*sig**6 + 1530*(3003 + 2*nV*(-1092 + nV*(273 + (-28 + nV)*nV)))*sig**8 - 2142*(-19305 + 2*nV*(10725 + nV*(-4290 + nV*(780 + nV*(-65 + 2*nV)))))*sig**10 + 9282*(20790 + nV*(-35640 + nV*(22275 + 2*nV*(-3300 + nV*(495 + (-36 + nV)*nV)))))*sig**12 - 7956*(-51975 + nV*(145530 + nV*(-145530 + nV*(69300 + nV*(-17325 + 2*nV*(1155 + nV*(-77 + 2*nV)))))))*sig**14 + 21879*(14175 + 2*nV*(-37800 + nV*(66150 + nV*(-52920 + nV*(22050 + nV*(-5040 + nV*(630 + (-40 + nV)*nV)))))))*sig**16 - 12155*(-2835 + 2*(-3 + nV)*nV*(-8505 + nV*(31185 + nV*(-42525 + nV*(25515 + nV*(-7371 + nV*(1071 + nV*(-75 + 2*nV))))))))*sig**18 + 21879*nV**2*(14175 + 2*nV*(-37800 + nV*(66150 + nV*(-52920 + nV*(22050 + nV*(-5040 + nV*(630 + (-40 + nV)*nV)))))))*sig**20 - 7956*nV**4*(-51975 + nV*(145530 + nV*(-145530 + nV*(69300 + nV*(-17325 + 2*nV*(1155 + nV*(-77 + 2*nV)))))))*sig**22 + 9282*nV**6*(20790 + nV*(-35640 + nV*(22275 + 2*nV*(-3300 + nV*(495 + (-36 + nV)*nV)))))*sig**24 - 2142*nV**8*(-19305 + 2*nV*(10725 + nV*(-4290 + nV*(780 + nV*(-65 + 2*nV)))))*sig**26 + 1530*nV**10*(3003 + 2*nV*(-1092 + nV*(273 + (-28 + nV)*nV)))*sig**28 - 204*nV**12*(-1365 + 2*nV*(315 + nV*(-45 + 2*nV)))*sig**30 + 153*(-10 + nV)*(-6 + nV)*nV**14*sig**32 + 9*(17 - 2*nV)*nV**16*sig**34 + nV**18*sig**36))/6.402373705728e15)

def PG19(nV, sig):
	return ((np.exp((nV*(-2 + nV*sig**2))/2.)*nV**19*(1 - 19*(-9 + nV)*sig**2 + 171*(68 + (-17 + nV)*nV)*sig**4 - 969*(-420 + nV*(180 + (-24 + nV)*nV))*sig**6 + 1938*(4095 + 2*nV*(-1365 + nV*(315 + (-30 + nV)*nV)))*sig**8 - 5814*(-15015 + nV*(15015 + 2*nV*(-2730 + nV*(455 + (-35 + nV)*nV))))*sig**10 + 13566*(38610 + nV*(-57915 + nV*(32175 + 2*nV*(-4290 + nV*(585 + (-39 + nV)*nV)))))*sig**12 - 25194*(-62370 + nV*(145530 + nV*(-124740 + nV*(51975 + 2*nV*(-5775 + nV*(693 + (-42 + nV)*nV))))))*sig**14 + 37791*(51975 + 2*nV*(-103950 + nV*(145530 + nV*(-97020 + nV*(34650 + nV*(-6930 + nV*(770 + (-44 + nV)*nV)))))))*sig**16 - 46189*(-14175 + nV*(127575 + 2*nV*(-170100 + nV*(198450 + nV*(-119070 + nV*(39690 + nV*(-7560 + nV*(810 + (-45 + nV)*nV))))))))*sig**18 + 46189*nV*(-14175 + nV*(127575 + 2*nV*(-170100 + nV*(198450 + nV*(-119070 + nV*(39690 + nV*(-7560 + nV*(810 + (-45 + nV)*nV))))))))*sig**20 - 37791*nV**3*(51975 + 2*nV*(-103950 + nV*(145530 + nV*(-97020 + nV*(34650 + nV*(-6930 + nV*(770 + (-44 + nV)*nV)))))))*sig**22 + 25194*nV**5*(-62370 + nV*(145530 + nV*(-124740 + nV*(51975 + 2*nV*(-5775 + nV*(693 + (-42 + nV)*nV))))))*sig**24 - 13566*nV**7*(38610 + nV*(-57915 + nV*(32175 + 2*nV*(-4290 + nV*(585 + (-39 + nV)*nV)))))*sig**26 + 5814*nV**9*(-15015 + nV*(15015 + 2*nV*(-2730 + nV*(455 + (-35 + nV)*nV))))*sig**28 - 1938*nV**11*(4095 + 2*nV*(-1365 + nV*(315 + (-30 + nV)*nV)))*sig**30 + 969*nV**13*(-420 + nV*(180 + (-24 + nV)*nV))*sig**32 - 171*nV**15*(68 + (-17 + nV)*nV)*sig**34 + 19*(-9 + nV)*nV**17*sig**36 - nV**19*sig**38))/1.21645100408832e17)

def PG20(nV, sig):
	return ((np.exp((nV*(-2 + nV*sig**2))/2.)*nV**20*(1 + sig**2*(190 - 20*nV + 95*(153 + 2*(-18 + nV)*nV)*sig**2 - 570*(-1020 + nV*(408 + nV*(-51 + 2*nV)))*sig**4 + 4845*(2730 + nV*(-1680 + nV*(360 + (-32 + nV)*nV)))*sig**6 - 3876*(-45045 + 2*nV*(20475 + nV*(-6825 + nV*(1050 + nV*(-75 + 2*nV)))))*sig**8 + 9690*(135135 + 2*nV*(-90090 + nV*(45045 + nV*(-10920 + nV*(1365 + 2*(-42 + nV)*nV)))))*sig**10 - 19380*(-270270 + nV*(540540 + nV*(-405405 + 2*nV*(75075 + nV*(-15015 + nV*(1638 + nV*(-91 + 2*nV)))))))*sig**12 + 62985*(155925 + 2*nV*(-249480 + nV*(291060 + nV*(-166320 + nV*(51975 + nV*(-9240 + nV*(924 + (-48 + nV)*nV)))))))*sig**14 - 41990*(-155925 + 2*nV*(467775 + nV*(-935550 + nV*(873180 + nV*(-436590 + nV*(124740 + nV*(-20790 + nV*(1980 + nV*(-99 + 2*nV)))))))))*sig**16 + 46189*(14175 + 2*nV*(-141750 + nV*(637875 + nV*(-1134000 + nV*(992250 + nV*(-476280 + nV*(132300 + nV*(-21600 + nV*(2025 + 2*(-50 + nV)*nV)))))))))*sig**18 - 41990*nV**2*(-155925 + 2*nV*(467775 + nV*(-935550 + nV*(873180 + nV*(-436590 + nV*(124740 + nV*(-20790 + nV*(1980 + nV*(-99 + 2*nV)))))))))*sig**20 + 62985*nV**4*(155925 + 2*nV*(-249480 + nV*(291060 + nV*(-166320 + nV*(51975 + nV*(-9240 + nV*(924 + (-48 + nV)*nV)))))))*sig**22 - 19380*nV**6*(-270270 + nV*(540540 + nV*(-405405 + 2*nV*(75075 + nV*(-15015 + nV*(1638 + nV*(-91 + 2*nV)))))))*sig**24 + 9690*nV**8*(135135 + 2*nV*(-90090 + nV*(45045 + nV*(-10920 + nV*(1365 + 2*(-42 + nV)*nV)))))*sig**26 - 3876*nV**10*(-45045 + 2*nV*(20475 + nV*(-6825 + nV*(1050 + nV*(-75 + 2*nV)))))*sig**28 + 4845*nV**12*(2730 + nV*(-1680 + nV*(360 + (-32 + nV)*nV)))*sig**30 - 570*nV**14*(-1020 + nV*(408 + nV*(-51 + 2*nV)))*sig**32 + 95*nV**16*(153 + 2*(-18 + nV)*nV)*sig**34 + 10*(19 - 2*nV)*nV**18*sig**36 + nV**20*sig**38)))/2.43290200817664e18)