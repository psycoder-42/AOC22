file = open('/Users/mavo/documents/Advent of Code/python/Dag 3/Ton/RucksackReorganization.txt', 'r')

# ----------
# Constanten
# ----------

GROEPSGROOTTE = 3



#==============================================================================
# functie gemeenTeken
#------------------------------------------------------------------------------
#
# Zoek het teken dat 3 sublijsten van de parameter "lijst" 
# gemeenschappelijk hebben. Gegeven is, dat dit slechts één teken
# zal zijn, waardoor de intersection van 3 sets bruikbaar is.
# 
# Deze intersection levert een set op met één element. Maak hier een
# lijst van (die dus ook één element bevat) en haal dit element op.
#==============================================================================


def gemeenTeken(lijst):
    
    doorsnede = set(lijst[0]) & set(lijst[1]) & set(lijst[2])
    
    gemeenLijst = list(doorsnede)
    teken = gemeenLijst[0]
    
    return(teken)    



#==============================================================================
# functie waarde
#------------------------------------------------------------------------------
#
# Bereken de waarde (in de puzzel de "prioriteit") van een teken.
# De ASCII waarde van hoofdletters loopt vanaf 65, die van de kleine letters
# vanaf 97. In de puzzel moeten echter de kleine letters juist de waarden
# vanaf 1 krijgen en de hoofdletters vanaf 27.
#==============================================================================


def waarde(teken):

    ascWaarde = ord(teken)
    if ascWaarde > 96:
       prioriteit = ascWaarde - 96
    else:
       prioriteit = ascWaarde - 64 + 26

 
    return prioriteit

    

#==============================================================================
# Hoofdprogramma
# -----------------------------------------------------------------------------
# 
# Lees de input regels en maak van elke regel een lijst.
# Verzamel steeds drie van deze lijsten in een groep.
# 
# Zodra een groep vol is (dus drie sublijsten bevat), bepaal dan het
# gemeenschappelijke teken in de groep.
# Bepaal de waarde van dit teken en tel deze bij het lopende totaal.
#==============================================================================


totaal=0
groep=[]
i = 1

for line in file:
    
    rugzak = list(line.strip('\n'))
    groep.append(rugzak)
    
    if i == GROEPSGROOTTE:
        i = 0
        teken = gemeenTeken(groep)
        prioriteit = waarde(teken)
        totaal += prioriteit
        print(teken, prioriteit)   # Ter controle
        groep = []

    i += 1

 
print(totaal)