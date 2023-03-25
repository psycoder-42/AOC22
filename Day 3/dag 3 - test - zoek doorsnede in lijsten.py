file = open('/Users/mavo/documents/Advent of Code/python/dag 3 - input.txt', 'r')



#==============================================================================
# functie zoekDoorsnede
#------------------------------------------------------------------------------
# Zoek de gemeenschappelijke elementen in twee lijsten.
# Maak van elke lijst een set (verzemeling) en gebruik de 
# Python doorsnede oparator "&". 
# Het resultaat is een set met alle elementen die in beide sets voorkomen.
#==============================================================================

def zoekDoorsnede(lijst1, lijst2):

    waarde = set(lijst1) & set(lijst2)
    return(waarde)    



#==============================================================================
# functie zoekDubbele
#------------------------------------------------------------------------------
# Zoek de gemeenschappelijke elementen in twee lijsten.
# Doorloop in een loop de eerste lijst en bij elk element de tweede lijst.
# Het resultaat is een lijst met alle elementen die in beide voorkomen.
#==============================================================================


def zoekDubbele(lijst1, lijst2):

    resultaat=[]
    for elem in lijst1:
        if elem in lijst2:
            resultaat.append(elem)
            
    return(resultaat)    



#==============================================================================
# Hoofdprogramma
# Vergelijk de performance van beide methodes om gemeenschappelijke 
# elementen in twee lijsten te zoeken.
# De ingebouwde functie "&" voor sets is vele malen sneller, omdat de 
# onderliggende efficiënte machinecode direct wordt gebruikt.
#==============================================================================


lijst1=list(20000 * "a") + ["c"]
lijst2=list(20000 * "b") + ["c"]

teken=zoekDubbele(lijst1, lijst2)
print(teken)

teken=zoekDoorsnede(lijst1, lijst2)
print(teken)

    
