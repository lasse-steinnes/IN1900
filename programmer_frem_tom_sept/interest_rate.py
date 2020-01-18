""" 1.6 money in bank """

A = 1000   ## euro
p = 5   ## rente
n = 3      ## år

money_ = A*(1+(p/100))**n

print ("""Etter n=%g år i banken, med rente p=%g,
 har 1000 euro vokst til %g euro.""" %(n,p,money_))

### Utskrift ####
"""python interest_rate.py
>> Etter n=3 år i banken, med rente p=5,
 har 1000 euro vokst til 1157.63 euro."""
