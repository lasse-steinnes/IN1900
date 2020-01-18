### Lag klasser for et rektangel og et triangel ###
## representere geometriske figurer

## Triangel
class Triangel(object):
    def __init__(self,pkt):
        """
        pkt må være en nøstet liste med punktene i triangelet
        """
        self.pkt = pkt

    def Areal(self):
        pkt = self.pkt
        A = (1/2)*abs(pkt[1][0]*pkt[2][1]\
        - pkt[2][0]*pkt[1][1] + pkt[0][0]*pkt[2][1]\
        + pkt[2][0]*pkt[0][1] - pkt[0][0]*pkt[1][1]\
        - pkt[1][0]*pkt[0][1])
        return A

    def Omkrets(self):    # perimeter
        pkt = self.pkt
        from math import sqrt
        sum_ = 0
        for i in range(1,3):
            side = sqrt((pkt[i][0]-pkt[i-1][0])**2+(pkt[i][1]-pkt[i-1][1])**2)
            sum_ += side
        side_3 = sqrt((pkt[2][0]-pkt[0][0])**2+(pkt[2][1]-pkt[0][1])**2)
        sum_ += side_3
        return sum_

# Rektangel
class Rektangel(object):
    def __init__(self,W,H,pkt):
         self.W = W # bredde
         self.H = H # høyde
         self.pkt = pkt # en liste med [x0,y0],

    def Areal(self):
        return self.W*self.H

    def Omkrets(self):
        return 2*self.W + 2*self.H

# Består koden testen?

def test_triangle_area():
     """
     Verify the area of a triangle with vertex coordinates
     (0,0), (1,0) and (0,2).
     """
     v1 = [0,0]; v2 = [1,0]; v3 = [0,2]
     pkt1 = [v1, v2, v3]
     t1 = Triangel(pkt1) # lager et tilfelle (insidens)

     ### Areal ###
     expected = 1
     computed = t1.Areal()

     ### Omkrets
     from math import sqrt
     expected_2 = 2 + 1 + sqrt(5) # Bruker ren pytagoras og legger sammen sidene
     computed_2 = t1.Omkrets()

     tol = 1e-14
     success = abs(expected - computed) < tol
     success_2 = abs(expected_2 - computed_2) < tol
     msg = "computed area=%g !=%g (expected)" % \
            (computed, expected)
     msg_2 = "computed perimeter=%g !=%g (expected)" % \
            (computed_2, expected_2)
     assert success, msg
     assert success_2, msg_2

test_triangle_area()

## Består funksjonen testen?
def test_rektangel():
    """
    Tester om klassen for funksjonen fungerer
    """
    W = 4
    H = 2
    x0_y0 = [1,1]

    r1 = Rektangel(W,H,x0_y0)

    ## areal
    computed = r1.Areal()
    expected = W*H
    ## omkrets
    computed_2 = r1.Omkrets()
    expected_2 = 2*W + 2*H
    tol = 1e-14
    success = abs(expected - computed) < tol
    success_2 = abs(expected_2 - computed_2) < tol
    msg = "computed area=%g !=%g (expected)" % \
           (computed, expected)
    msg_2 = "computed perimeter=%g !=%g (expected)" % \
           (computed_2, expected_2)
    assert success, msg
    assert success_2, msg_2


test_rektangel()

print('\nEt kjøreeksempel for klassen Triangel:\n')
v1 = [0,0]; v2 = [1,0]; v3 = [0,2]
pkt1 = [v1, v2, v3]
t1 = Triangel(pkt1)
print('ID til insidens t1 er: {:}'.format(id(t1)))
a1 = t1.Areal()
o1 = t1.Omkrets()
print('Areal: {:}    Omkrets:{:.4e} \n(når hjørnene i trekanten er gitt ved {:})'.format(a1,o1,pkt1))
print('\nEt kjøreeksempel for klassen Rektangel:\n')
W = 4
H = 2
x0_y0 = [1,1]
r1 = Rektangel(W,H,x0_y0)
print('ID til insidens r1 er: {}, og typen er {}'.format(id(r1),type(r1)))
a2 = r1.Areal()
o2 = r1.Omkrets()
print('Et rektangel med W={} og H={}, har:\nAreal: {}   Omkret: {}'.format(W,H,a2,o2))
print('\n')

## Kjøreeksempel:
"""
>> python geometric_shapes.py

python geometric_shapes.py

Et kjøreeksempel for klassen Triangel:

ID til insidens t1 er: 4570182096
Areal: 1.0    Omkrets:5.2361e+00
(når hjørnene i trekanten er gitt ved [[0, 0], [1, 0], [0, 2]])

Et kjøreeksempel for klassen Rektangel:

ID til insidens r1 er: 4570182152, og typen er <class '__main__.Rektangel'>
Et rektangel med W=4 og H=2, har:
Areal: 8   Omkret: 12

"""
