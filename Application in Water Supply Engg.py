# To determine alkalinity of given sample
H2S04_reg = float(input(“Enter the volume ofH2S04 required in ml:“)) 
Sample = float(input(“Enter the value of sample inlitres:”))
AlkalinityRemoved = H2S04_reg print(”AlkalinityRemoved: “,AlkalinityRemoved, ”'mg“) 
Alkmgperlit = AlkalinityRemoved/ Sample print(”TotalAlkalinity:“,Alkmgperlit,"mg/lit”)
OH= float (input("Enter the value of OH-Alkalinity present : ”)) 
#Alkalinity removed till pH of 8.3
H2S04_req = float (input(”Enter the volume of H2S04 required in ml :"))
AlkalinityRemoved = H2S04_req print(”AlkalinityRemoved: ",AlkalinityRemoved, ”mg“)
C03_Combined = AlkalinityRemoved / Sample
print ("Carbonate Alkalinity upto pH8.3:“,C03_Combined, "mgperlit“ )
CO3 = CO3_Combined - OH
print(”Carbonate Alkalinity:”, CO3,“'mg/lit”)
HCO3 =Alkmgperlit - 2*CO3-OH
print(”Bicarbonate Alkalinity:”, HC03, "mg/it“)
