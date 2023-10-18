# To find the ultimate moment carring capacity of singly r/f beam

2 fck = float(input("Enter the value of charateristics compressive strength:"))
3 fy= float(input("Enter the grade of steel:")) 
4 Es = float(input("Enter the value of Modulus of Elasticity of steel:"))
5 b = float(input("Enter the value of Width: "))
6 d = float(input("Enter the value of effective depth:"))
7 d1 = float(input("Enter the value of bar diameter (d1):"))
8 d2 = float(input("Enter the value of bar diameter (d2):"))
9 n = int(input("Enter the number of bars"))
10 Ast1= (n*0.7854*d1*d1)
11 Ast2 = (n*0.7854*d2*d2)
12 print ("The value of area of steel (Ast1):", Ast1)
13  print ("The value of area of steel (Ast2):", Ast2)
14 # Total area of steel
15 Ast = Ast1 + Ast2
16 print ("The value of area of steel (Ast):", Ast)
17 # Neutral Axis Factor
18 ku = 0.0035/(0.0055 + (fy/(1.15*Es)))
19 print ("The value of Neutral axis factor (ku):", ku)
20# Momenent of Resistance factor
21 Ru= 0.36*fck*ku*(1-(0.42*ku))
22 print ("The value of Moment of Resistance factor (Ru):", Ru)
23 # Maximum Neutral Axis:
24 xumax = ku*d
25 print ("The value of maximum neutral axis (xumax):", xumax)
26 xu = (0.87*fy*Ast)/(0.36*fck*b)
27 print ("The value of Actual Neutral Axis (xu):", xu)
28 if xumax>xu:
29 print ("UNDER REINFORCED")

30 else:
31 print ("OVER REINFORCED")
32 # By Comparing
33 X = float(input("Enter the value of Neutral Axis:"))
34 # Moment of Resistance
35 Mu = 0.36*fck*x*b*(d-(0.42*x))10*-6
36 print ("The value of Moment of Resistance is:", Mu)


Q 2:-
1 # Design of Slab
2 # Given Data
3 # Effective span is already given in question
4 span= span float(input("Enter the value of effective span in meters:"))
5 b= float(input("Enter the value of width of slab in mm:"))
6 bs= float(input("Entert the value of Support Width in meters:"))
7 fck float(input("Enter the value of Characteristics Compressive Strength:"))
8 fy = float(input("Enter the value of grade of steel:"))
9 Es float (input("Enter the value of Modulus of Elasticity is:"))
10 LL = float(input("Enter the value of Live Load:"))
11 FF = float(input("Enter the value of Floor Finish:"))
12 Density float(input("Enter the value of Density of RCC:"))
13 # Design Constants
14 # Neutral Axis Factor
15 ku 0.0035/((0.0055)+ (fy/(1.15 Es)))
16 print ("The value of Neutral Axis Factor (ku) is:", ku)
17 # Moment of Resistance Facor
18 Ru= 0.36*fck*ku (1-(0.42*ku))
19 print ("The value of Moment Resisteance factor (Ru) is:", Ru)
20 # Assuming pt 0.5 from fig.4 from IS 456:2007 page no.38
21 fs float(input("Enter the value of Steel Stress of Service:"))
22 # From Graph find out the Modification Factor
23 MF float(input("Enter the value of Modification Factor:"))
24 #From Clause 23.2.1 Select span/d Ratio
25 S= float(input("Enter the value of span/d ratio:"))
26 # Correction Factors
27 k1 float(input("Enter the value of Correction factor if sapn> 10m (k1):"))
28 k2= float(input("Enter the value of Tension r/f correction factor (k2):"))
29 k3= float(input("Enter the value of Compression r/f correction factor (k3):"))
30 k4= float (input("Enter the value of correction factor in case of flanged section (k4):"))
31 # Effective depth
32 d1= (span*1000)/(S*MF*k1*k2k3*k4)
33 print ("The value of effective depth as per deflection criteria is:", di)
34 # Define Effective depth and overall depth Assuming value of cover
35 d = float(input("Enter the value of Effective depth in mm (d):"))
36 D= float(input("Enter the value of Overall depth in mm (D):"))
37 # Load Calculations
38 # Self Weight of slab
39 DL = D*Density/1000
40 print ("The Dead load is:", DL)
41 # Total Load is
42 Factor float(input("Enter the value of partial Safety Factor is: "))
43 TL = DL + LL + FF
44 print ("The value of total load is:", TL)
45 Wu Factor*TL
46 print ("Wu=", Wu)
47 # Bendingf Moment Calculations (Mu)
48 Mu= Wu*span*span/8
49 print ("The Value of Bending Moment (Mu) is:", Mu)
50 # Check for effective depth
51 d2 ((Mu 1000000)/(Ru*b))**0.5
52 print ("The value of Effective depth as per Moment criteria:", d2)
53 if d2>d:
54 print ("Revise the Depth:")
55 else:
56 print ("SAFE")
57 d = float(input("Enter the value of Effective depth in mm (d):"))
58 print ("Minimum Steel Calculations")
59 Astmin = 0.12*b*D/100
60 print ("The value of Minimum steel is:", Astmin)
61 print ("Main Steel calculations") 
62 Ast ((0.5 fck*b*d)/(fy))(1-((1-((4.6*Mu*1000000)/(fck*b*d*d)))*0.5))
63 print ("Ast:", Ast)
64 print ("Check for Ast")
65 if Ast<Astmin:
66 print ("Take Ast=Astmin")
67 else:
68 print ("Ast>Astmin, Hence SAFE")
69 dia1 = float(input("Enter the value of bar diameter for main steel:"))
70 dia2 = float(input("Enter the value of bar diameter for Distribution steel:"))
71# Area of bar
72 ao1 = 0.7854*dia1*dial
73 print ("The Value of Area of main steel bar (ao1):", ao1)
74 a02= 0.7854*dia2*dia2
75 print ("The Value of Area of main steel bar (ao2):", a02)
76 # Sapcing Calculations
77 Spacing1 = ao1*b/Ast
78 print ("The sapcing for main steel bars is;", Spacing1)
79 Spacing2 = ao2*b/Astmin
80 print ("The sapcing for distribution steel bars is;", Spacing2)
81 print ("Check 1 for main steel")
82 if Spacing1>300:
83 print ("UNSAFE")
84 else:
85 print ("SAFE")
86 print ("Check 2 for main steel")
87 if Spacing1>3*d:
88 print ("UNSAFE")
89 else:
90 print ("SAFE")
91 print ("Check 1 for Distribution steel")
92 if Spacing1>300:
93 print ("UNSAFE")
94 else:
95 print ("SAFE")
96 print ("Check 2 for Distribution steel")
97 if Spacing1>5*d:
98 print ("UNSAFE")
99 else:
100 print ("SAFE")
101 print ("Approximated values of Sapcing:")
102 S1 float(input("Enter the value of spacing of main bars:"))
103 S2 float(input("Enter the value of spacing of distribution bars:"))
104 Astprovided ao1*b/S1 
105 print ("The provided steel area for main bars at section in mm^2 is:", Astprovided)
106 Astprodist ao2 b/52
107 print ("The provided steel area for distribution bars at section in mm^2 is: ", Astprodist)
108 # Check for Shear
109 Vu = (Wu*span/2)-(Wu*((bs/2)-(d/1000)))
110 print ("The value of SF at a Section is:", Vu)
111 SStress = (Vu*1000)/(b*d)
112 print ("The value of shear stress is:", SStress)
113 # From table 20 IS 456:2007 page 73
114 SStressmax = float(input("Enter the value of maximum Shear stress:"))
115 if SStress>SStressmax:
116 print ("Crushing will happen")
117 else:
118 print ("SAFE")
119 # Percentage Steel
120 pt =(100 Ast)/(b*d) 120 
121 print ("Enter the value of percentage steel is:", pt)
122 # From table 19 IS 456:2007 page 73
123 SS= float(input("Enter the value of Shear Stress is:"))
124 k = float(input("Enter the value of depth factor:"))
125 Shear k*SS
126 print ("The value of shear at section is, Shear)
127 if SStress>Shear:
128 print ("Shear Reinforcement Required")
129 else:
130 print ("Shear Reinforcement not Required, SAFE")
131 # Check for Deflection
132 ActDEF = span*1000/d
133 print ("The value od span/d is:", ActDEF)
134 # Actual Deflection
135 MaxDEF = S*MF*k1*k2*k3*k4
136 print ("The permissible deflection is:", MaxDEF)
137 if MaxDEF>S/d:
138 print ("SAFE")
139 else:
140 print ("UNSAFE")
141 # Check for Anchorage Length
142 M1 = 0.87*fy*Ast* (d ((fy*Ast)/(fck*b))) -
143 print ("The value of Moment (M1)", M1)
144 lo = 8*dial
145 La = 1.3*(M1/Vu)+10
146 print ("The value of Anchorage length is:", La)
147 # Development Length
148 bonds = float(input("Enter the value of Bond Stress:"))
149 Ld = 0.87*fy*dia1/4*bondS*1.6
150 print ("The value of Development length is:", Ld)
151 if La>Ld:
152 print ("SAFE")
153 else:
154 print ("increase anchorage")


