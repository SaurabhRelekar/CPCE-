Q 1:-
1 # To Determine the bearing capacity of soil with water table
2 BulkDensity =float(input("Enter the value of Bulk Density of soil:"))
3 SatDensity = float(input("Enter the value of Saturated Density of soil:"))
4 WaterDensity = float(input("Enter the unit Weight of Water:"))
5 Df= float(input("Enter the value of depth of footing:")) 
6 Dw = float(input("Enter the value of water table above footing level:"))
7 Dw1 = float(input("Enter the value of Water table below the level of footing:"))
8 B float(input("Enter the value of width of footing:"))
9 Nq= float(input("Enter the value of Nq:"))
10 N float(input("Enter the value of N ganna (N):"))
11 SubDensity SatDensity WaterDensity
12 print ("Submerged Weight of soil is:", SubDensity)
13 # The bearing capacity of soil when water table is at ground
14 print ("CASE A")
15 qu= (SubDensity*Df*Nq) + (0.5*0.8*B*SubDensity*N)
16 print ("The value of ultimate bearing capacity of soil is:", qu)
17 Approximate calculation of Bearing capacity of soil is.
18 Rw= 0.5 + 0.5*(Dw/B)
19 print ("The value of Rw is:", Rw)
28 Rw1 = 0.5 + 0.5*(Dw1/8)
21 print ("The value of Rw1 is:", Rw1)
22 qu= (BulkDensity*Df*Nq*Rw) + (0.5*0.8*8*BulkDensity *N*Rw1)
23 print ("The value ultimate bearing capacity of soil is:", qu)
24 # Case B
25 print ("CASE B")
26 qu= (BulkDensity Df*Nq) + (0.5*0.8*8*SubDensity)
 27 print ("The value of ultimate bearing capacity is:", qu)
28 Dw = float(input("Enter the value of water table above footing level:"))
 29 Dw1 = float(input("Enter the value of Water table below the level of footing: "))
30 print ("The approximate value of ultimate bearing capacity is: ")
31 Rw 0.5 + 0.5*(Dw/B)
32 print ("The value of Rw is:", Rw)
33 Rw1= 0.5 + 0.5* (Dw1/8)
 34 print ("The value of Rw1 is:", Rw1)
35 qu= (BulkDensity Df Nq Rw) (0.5 0.8*8*Bulk Density NR1)
36 print ("The approximate value of ultimate hearing capacity is:", qu)
37 # Case C
38 print ("CASE C")
39 x = float(input("Enter the value of depth of water below footing:"))
40 qu (BulkDensity Of Nq) + (0.5*0.8* ((BulkDensity*x)+(SubDensity (B-x)))*N)
41 print ("The value of ultimate bearing capacity is:", qu)
42 Dw = float(input("Enter the value of water table above footing level:"))
43 Dw1 = float(input("Enter the value of Water table below the level of footing:")) 
44 print ("The approximate value of ultimate bearing capacity is:")
45 Rw= 8.5+ 8.5*(Dw/B)
46 print ("The value of Rw is: ", Rw)
47 Rw1 = 0.5 + 0.5*(Dw1/8)
48 print ("The value of Rwl is: ", Rw1)
49 qu= (Bulk Density Df Nq Rw) + (0.5*0.8*8*Bulk Density*N*Rw1)
50 print ("the value of ultimate bearing capacity is:", qu)


Q2:-
1 # To find the ultimate load carring capacity of pile
2 UCS = float(input("Enter the value of UCS of soil:"))
3 Cu = UCS/2
4 B = float(input("Enter the value of dimension of pile:"))
 5 1 = float(input("Enter the length of pile:"))
6 Alpha = float(input("Enter the value of adhesion factor:"))
7 Nc = float(input("The value of Nc: "))|
8 Ab = B*B
9 print ("the Base area of footing is:", Ab)
10 As = 4*B*1
11 print ("The value of chohesion of soil is:", Cu)
12 Qpu = Cu*Nc*Ab
13 print ("Qpu: ", Qpu)
14 Qf = Alpha*Cu*As
15 print ("Qf:", Qf)
16 Qu= Qpu + Qf
17 print ("the value of load carring capacity of pile is (Qu):", Qu)
