# Genereer dictionary met letterwaardes alfabet

letterWaarde=dict()
waarde=1
for letter in range(ord("a"), ord("z")+1):
    letterWaarde[chr(letter)]=waarde
    waarde+=1

waarde = 27    
for letter in range(ord("A"), ord("Z")+1):
    letterWaarde[chr(letter)]=waarde
    waarde+=1
 
print(letterWaarde)