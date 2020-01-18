### rep til eksamen.
## 1.4 Length conversion

## Lage et program som gjør om meter til...
meter = float(input("m = "))

## inches
# i meter.Slik at meter strykes når man deler meter på inch f.eks.

inch = 2.54/100
## feet
foot = 12*inch

## Yard
yard = 3*foot

## Engelsk mil
mile = 1760*yard

## Dermed blir
length_in_meters = meter
length_in_inches = meter/inch
length_in_feet = meter/foot
length_in_yards = meter/yard
length_in_miles = meter/mile

# print(length_in_inches, length_in_feet , length_in_yards, length_in_miles)

answer = '%g meters is %g inches, %g feet,\
%g yards and %g miles.' %(length_in_meters,length_in_inches, length_in_feet,
length_in_yards, length_in_miles)

print(answer)
