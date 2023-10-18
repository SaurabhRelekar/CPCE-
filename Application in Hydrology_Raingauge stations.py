# Calculation of Mean precipitation by Isohytel Method 
# The value of precipitation at Each station is
p1 = int(input("Enter the value of rainfall at Station 1:"))
 p2 = int(input("Enter the value of rainfall at Station 2:")) 
 p3 = int(input("Enter the value of rainfall at Station 3:"))
 p4 = int(input("Enter the value of rainfall at Station 4:")) 
 p5 = int(input("Enter the value of rainfall at Station 5:")) 
 p6 = int(input("Enter the value of rainfall at Station 6:"))
 p7 = int(input("Enter the value of rainfall at Station 7:"))
 p8 = int(input("Enter the value of rainfall at Station 8:"))
 # Area for each station
A1 = int(input("Enter the value of Catchment Area for raingauge station 1:"))
 A2 = int(input("Enter the value of Catchment Area for raingauge station 2:")) 
 A3 = int(input("Enter the value of Catchment Area for raingauge station 3:")) 
 A4 = int(input("Enter the value of Catchment Area for raingauge station 4:")) 
 A5 = int(input("Enter the value of Catchment Area for raingauge station 5:")) 
 A6 = int(input("Enter the value of Catchment Area for raingauge station 6:")) 
 A7 = int(input("Enter the value of Catchment Area for raingauge station 7:")) 
 # The total catchment area is
A = A1 + A2 + A3 + A4 + A5 + A6 + A7
print ("The value of Total Catchment area is:", A) # Mean Precipitation
p = ((p1+p2)*A1/2 + (p2+p3)*A2/2 + (p3+p4)*A3/2 + (p4+p5)/2*A4 + (p5+p6)*A5/2
+ (p6+p7)*A6/2 + (p7+p8)*A7/2)/A
print ("The value of Mean Precipitaion is:", p)
