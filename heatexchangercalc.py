

U = float(input("enter overall heat transfer coefficient (U) in W/M^2.K: "))
A = float(input(" enter heat transfer area (A) in M^2: "))


Th_in = float(input("enter hot fluid inlet temperature: "))
Th_out = float(input("enter hot fluid outlet tempeature: "))
Tc_in = float(input("enter cold fluid inlet temperature: "))
Tc_out = float(input("enter cold fluid outlet temperature: "))

# temperature difference
dT1 = Th_in - Tc_out
dT2 = Th_out - Tc_in

print(" delta T1 =", dT1)
print(" delta T2 =", dT2) 

if dT1 <= 0 or dT2 <= 0 :
    print("Error: Temperature difference must be positive.")
    print(" Check your inlet and outlet temperature.")
    exit()

import math

if dT1 == dT2:
    LMTD = dT1
else:
    LMTD = (dT1 - dT2) / math.log(dT1/dT2)

print("LMTD =", LMTD)

Q = U*A*LMTD

print("Heat duty (Q):", Q,("watts"))

Q_kw = Q/1000
print("heat duty (Q) =", Q_kw ,"kw")

