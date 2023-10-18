Q:-1
 # To find the downstream depth of open channel
2 # Given Data
3 Q= float(input("Enter the value of Discharge:"))
4 T= int(input("Enter the value of top width:"))
5 g = float(input("Enter the value of acceleration due to Gravity:"))
6 y1 = float(input("enter the value of upstream depth:"))
 7 Z = float(input("Enter the Value of hump: "))
8 # Dicharge per meter width
9 q = Q/T
10 print ("The value of discharge per meter width is:", q)
11 # Area Calculation
12 A1= T*y1
13 print ("The value of upstream area is:", A1)
14 # Calculation of Froude Number
15 Fr1 = ((Q*Q*T)/(g*A1* A1 *A1))**0.5
16 print ("The value of Froude number is:", Fr1)
17 if Fr1>1:
18 print("The flow is Super Critical Flow")
19 else:
20 print("The flow is Sub Critical Flow")
21 # Upstream Energy
22 E1 = y1 + ((Q*Q)/(2*g*A1 *A1))
23 print ("The value of Energy at initial Section is:", E1)
24 # Downstream Energy
25 E2 = E1 - Z
26 print ("The value of downstream Energy E2 is:", E2)
27 # Critical Depth
28 yc = (q*q/g)**0.3333
29 print ("The Value of critical depth is:", yc)
30 Ec = 1.5*yc
31 print ("The value of critical Energy is", Ec)
32 if Ec>E2:
33 print ("Chocking Condition")
34 else:
35 print ("SAFE")
36 # Calculation of Zmax
37 Zmax = E1- Ec
38 print ("The value of maximum hump is:", Zmax)

Q 2:-
1 # To find the downstream depth of open channel
2 # Given Data
3 Q= float(input("Enter the value of Discharge:"))
4 B1 = float(input("Enter the value of width at upstream: "))
5 B2 = float(input("Enter the value of width at downstream: "))
6 g= float(input("Enter the value of acceleration due to Gravity:"))
7 y1= float(input("enter the value of upstream depth:")) 
8 # Dicharge per meter width
9 q1=Q/B1 
10 q2= Q/B2 
11 print ("The value of discharge per meter width is:", q1)
12 print ("The value of discharge per meter width is:", q2)
13 # Area Calculation
14 A1 = B1*y1
15 print ("The value of upstream area is: ", A1)
16 # Calculation of Froude Number
17 Fr1 = ((Q*Q*B1)/(g*A1*A1*A1))**0.5
18 print ("The value of Froude number is:", Fr1)
19 if Fr1>1:
20 print("The flow is Super Critical Flow")
21 else:
22 print("The flow is Sub Critical Flow")
23 # Upstream Energy
24 E1 = y1 + ((Q*Q)/(2*g*A1*A1))
25 print ("The value of Energy at initial Section is:", E1)
26 (type alias) B2min: Any dition
27 B2min = ((27*Q*Q)/(8*g*E1*E1*E1))**0.5
28 print ("The value of minimum width to be kept to avoid Chocking is: ", B2min)
29 if B2min > B2:
30 print ("Chocking Condition")
31 else:
32 print ("SAFE")
33 # Critical Depth
34 yc = ((Q*Q)/(B2*82*g))**0.3333
35 print ("The Value of critical depth is: ", yc)
36 Ec = 1.5*yc
37 print ("The value of critical Energy is", Ec)


Q 3:-
1 #Design of Efficient Channel Section
2 Q= float(input("Enter the value of Discharge:"))
3 n=float(input("Enter the value of Rugosity coefficient:"))
4 So= float(input("Enter the value of bed slope:"))
5 g = float(input("Enter the value of acceleration due to Gravity:"))
6 #Manning's Formula
7 #Q = (AR^2/3 S^1/2)/n 
8 yn ((Q*n*50*1.591)/(1.732))**(3/8)
9 print ("The Value of yn is", yn)
10 #To encounter the effect of free board
11 yn1= 1.1*yn
12 print ("The Value of ynl is", yn1) 
13 # Cross Sectional Area
14 A = 1.732 yn* yn1
15 print ("The cross sectional Area is:", A)
16 # Top Width
17 T = 4* yn/1.732
18 print ("The value of top Width is:", T)
19 # Bottom Width
20 B= 2 yn/1.732
21 print ("The value of Bottom Width is", 8)
22 Fr= ((Q*Q*T)/(g*A*A*A))*0.5
23 print ("The value of Froude number is: ", Fr)
24 if Fr>1:
25 print("The flow is Super Critical Flow")
26 else:
27 print("The flow is Sub Critical Flow")
 

