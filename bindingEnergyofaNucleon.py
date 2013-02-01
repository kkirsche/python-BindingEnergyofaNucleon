from numpy import *
from math import *


# Set the constants (in electron volts).
a_1 = 15.67
a_2 = 17.23
a_3 = 0.75
a_4 = 93.2

A= 0.0

def A_mass(Z):
    """This calculates the mass, A, Z through 3Z+1 for all values of Z"""
    B = 0.0
    B = arange(Z,3.0*Z+1.0)
    return B

def a_5_calc(A,Z):
    """ This calculates the value of a_5 based on the input of A and Z."""
    m = list()
    for n in A:
        if ((n%2) == 0):
            if ((Z%2) == 0):
               m.append(12.0)
            else:
                m.append(12.0)
        else:
            m.append(0.0)

    return m

#a_1=p, a_2=h, a_3=y, a_4=z, a_5, A, Z=s
def B_calc(p,h,y,z,a_5,A,s):
    """This calculates the bidning energy."""
    i = 0
    E = list()
    for n in A:
        valueOfEnergy = (p*A[i])-(h*(A[i]**(2.0/3.0)))-(y*(s**2/(A[i]**(1.0/3.0))))-(z*((A[i]-2*s)**2/A[i]))+(a_5[i]/A[i]**(1.$
        i += 1
    E.append(valueOfEnergy)
    return E

def BE_N_calc(B,A):
    """ This calculates the Binding Energy per Nucleon, B/A."""
    i = 0
    BE = list()
    for n in A:
        perNucleon = B[i]/A[i]
        i += 1
    BE.append(perNucleon)
    return BE

#First we setup the range for Z
theIntegerRange = range(1,101)
#We need it to be a list of floating point numbers though, so we can loop
# through it and calculate each new value of BE_N
range = list()
#So we convert each item in the range into a floating point number, and store it in Z[index].
for theInteger in theIntegerRange:
    range.append(float(theInteger))

#For each item of Z (with values 1 through 100)
for Z in range:
    #show what Z is
    print "Z: ", Z
    #Calculates the masses for each Z.
    A = A_mass(Z)
    #print "A: ", A
    #Calculates the values of a_5.
    a_5 = a_5_calc(A,Z)
    #print "a_5: ", a_5
    # Calculates the Binding Energy of each nucleon
    B = B_calc(a_1,a_2,a_3,a_4,a_5,A,Z)
    #print "B: ", B
    # Calculates the Binding Energy per Nucleon
    BE_N = BE_N_calc(B,A)
    #print "BE_N: ", BE_N
    # First, we find the max value in our array, then we find the index of that
    indexOfBE_N = BE_N.index(max(BE_N))
    # Because they are all relational lists we use the index of the max Binding
    #Energy per Nucleon to find it relational A value.
    print "The value of A for the most stable nucleon: ", A[indexOfBE_N]
