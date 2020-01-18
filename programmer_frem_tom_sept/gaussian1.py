""" 1.10: Evaluate a Gaussian function """
from math import exp,pi, sqrt

m = 0  # average
s = 2  # standard deviation
x = 1  # sample

f = (1/(sqrt(2*pi)*s))*exp((-1/2)*((x-m)/s)**2)

print("For m=%g, s=%g og x=%g er den Gaussiske verdien lik %.3g." %(m,s,x,f))

#### UTSKRIFT ####
"""python gaussian1.py
>> For m=0, s=2 og x=1 er den Gaussiske verdien lik 0.176."""
