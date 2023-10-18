Q-1:-
# Calculation of total Infiltration by Horton's Equation
 fo = float(input("Enter the value of initial Infiltration Rate:"))
fc= float(input("Enter the value of Final infiltration Rate:"))
t = int(input("Enter the value of Time:"))
kh= float(input("Enter the value of Decay Coefficient:"))
 # The total Infiltration is given by: 
Fp= fc't+ (fo - fc)/kh
 print ("The value of Total Infiltration is:", Fp)

Q 2 :- 
1 Calculation of Mean precipitation by theissen's polygon Method
 2 The value of precipitation at Each station is
3 p1=int(input("Enter the value of rainfall at Station 1:"))
4 p2= int(input("Enter the value of rainfall at Station 2:"))
5 p3 =int(input("Enter the value of rainfall at Station 3:"))
6 p4 =int(input("Enter the value of rainfall at Station 4:"))
7 p5 =int(input("Enter the value of rainfall at Station 5:"))
 8 #Area for each station
9 A1= int(input("Enter the value of Catchment Area for raingauge station 1:"))
10 A2= int(input("Enter the value of Catchment Area for raingauge station 2:"))
11 A3 =int(input("Enter the value of Catchment Area for raingauge station 3:"))
12 A4=int(input("Enter the value of Catchment Area for raingauge station 4:"))
13 A5= int(input("Enter the value of Catchment Area for raingauge station 5:"))
 14 The total catchment area is
15 A=A1 + A2 + A3 + A4 + A5
16 print ("The value of Total Catchment area is:", A)
17 # Runoff Volume
 18 The volume shall be multiplied by the coefficient 2500 to cater scale effects
17 #Runoff Volume
19 V= (p1* A1+ p2* A2+ p3* A3+ p4 *A4+p5* A5)*2500
 20 print ("The runoff volume from the given catchment is:", V)
21 # Mean Precipitation 
22 p (p1 A1+ p2 A2 p3 A3+ p4A4+ p5 A5)/A
23 print ("The value of Mean Precipitalon is:", p)


1 #Calculation of Mean precipitation by Isohytel Method
2 #The value of precipitation at Each station is
 3 p1=int(input("Enter the value of rainfall at Station 1:”))
4 p2= int(input("Enter the value of rainfall at Station 2:"))
5 p3= Int(Input("Enter the value of rainfall at Station 3:”))
 6 p4=int(input("Enter the value of rainfall at Station 4:"))
7 p5= int(input("Enter the value of rainfall at Station 5"))
8 p6=int(input("Enter the value of rainfall at Station 6:”))
9 p7= Int(input("Enter the value of rainfall at Station 7:"))
10 p8=int(input("Enter the value of rainfall at Station 8:"))
 11 # Area for each station 
12 A1= int(input("Enter the value of Catchment Area for raingage station 1:”))
13 A2= int(input("Enter the value of Catchment Area for raingauge station 2:”))
14 A3= int(input("Enter the value of Catchment Area for raingauge station 3:")) 
15 A4=int(input("Enter the value of Catchment Area for reingauge station 4:"))
 16 A5= int(input("Enter the value of Catchment Ares for raingauge station 5:"))
17 A6= Int(input("Enter the value of Catchment Area for raingeuge station 6:”))
18 A7= int(input("Enter the value of Catchment Area for reingauge station 7:"))
19# The total catchment area is
 20 A= A1+ A2+ A3+ A4+ A5+ A6+ A7
21 print ("The value of Total Catchment area is :”4)
22# Mean Precipitation
23 p=((p1+p2)*A1/2 + (p2+p3)*A2/2+ (p3+p4)*A3/2+ (p4+p5)* A4/2 + (p5+p6)*A5/2 + (p6+p7)*A6/2        + (p7+p8)*A7/2)/A
24 print (“the value of Mean Precipitalon is:”)
