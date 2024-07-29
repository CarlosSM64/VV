#🇨🇴 Colombian pesos
#🇵🇪 Peruvian soles
#🇧🇷 Brazilian reais

CO = float(input("What do you have left in pesos?: "))
PE = float(input("What do you have left in soles?: "))
BR = float(input("What do you have left in reais?: "))

cCO = CO/4027.19

cPE = PE/3.74

cBR = BR/5.62

USD = cCO + cPE + cBR

print(USD)