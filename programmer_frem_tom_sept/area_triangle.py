### Oppgave 3.16 Beregn arealet til en trekant

# Algoritme;
# Definere funksjon
# Først lage en nøstet liste med hjørnene (dvs koordinater)
# Dermed skrive uttrykket, må behandle med indeks

def triangle_area(vertices):
    area = (1/2)*abs(vertices[1][0]*vertices[2][1]\
    - vertices[2][0]*vertices[1][1] + vertices[0][0]*vertices[2][1]\
    + vertices[2][0]*vertices[0][1] - vertices[0][0]*vertices[1][1]\
    - vertices[1][0]*vertices[0][1])
    return area

v1 = [0,0]; v2 = [1,0]; v3 = [0,2]
vertices_1 = [v1, v2, v3]
print(triangle_area(vertices_1))

# Består koden testen?
from math import e

def test_triangle_area():
     """
     Verify the are of a triangle with vertex coordinates
     (0,0), (1,0) and (0,2).
     """
     v1 = [0,0]; v2 = [1,0]; v3 = [0,2]
     vertices_1 = [v1, v2, v3]
     expected = 1
     computed = triangle_area(vertices_1)
     tol = 1e-14
     success = abs(expected - computed) < tol
     msg = "computed area=%g !=%g (expected)" % \
            (computed, expected)
     assert success, msg

test_triangle_area()
