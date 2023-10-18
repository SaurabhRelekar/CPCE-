Q 1.
# To find BOD at 7th day 25C
# To find Decay Coefficient at 25C
K= float(input(“Decay Coefficient:”))
T= float(input(“Temperature of 3rd day BOD:”)) 
T1=float(input(“Temperature of 7th day BOD:”))
 K2 = (K*((1.047)**(T1-T)))
print(”The value of K2 is:", K2) # To find Ultimate BOD
e= 2.718
print(”The value ofe is:", e)
B1 = float(input("BOD at 3rd day 20c:”)) t=float(input(“time in days for finding B1:”)) E= 1-(e**(-0.23*t))
print(”The value of E is:", E) lo	(B1/E)
print(”The value of lo is:", lo) # To find BOD at 7th day 25C
t1 =float(input("time in days for finding B2:")) El = 1-(e**(-0.289*t1))
print(”The value of El is:", El) B2 = (lo*E1)
print(”The value of B2 is:", B2)


Q 2.
#Determination if density of sludge removed from aeration tank 
M= float(input(“Enter the value of initial mass :”))
S=float(input(“Enter the value ofsolid containing sludge in percentage:"))
 Gs= float(input("Enterthe value of Specific gravity ofsludge solid:”))
 Rho_W= float(input(“Enter the value of density of water:”))
Ws = ((S/M)*100)
m = M - Ws
print(”the value of mass of water“, m)
print(”The value of Solid Content in sludge”, Ws)
Vw = m /Rho_W
print(”The Value of Volume", Vw)
Rho_S = Gs * Rho_W
print(”The value ofDensity of solid content in sludge”, Rho_S) Vs=(Ws/(Gs*Rho_S ))
print(”The value of volume of solid content in sludge”, Vs)
Vt= Vw + Vs
print(”The value of total volume of solid content in sludge”, Vt)
Rho_SL= M/ Vt
print(”The value of Density of sludge removed from aeration”, Rho_SL)
