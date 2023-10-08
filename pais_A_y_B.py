A : float = 25
B : float = 18.9
C : float = 2022
while A > B:
    crecA = 1 + 0.02
    crecB = 1 + 0.03
    A *= crecA
    B *= crecB
    C += 1
print("En el año " +str(C)+ " la población del país B será mayor que la población del país A")