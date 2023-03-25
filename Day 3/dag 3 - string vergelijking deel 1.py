file = open('/Users/mavo/documents/Advent of Code/python/Dag 3/dag 3 - input.txt', 'r')



#==============================================================================
# Zoek letterwaardes op in voorgedefinieerde lijst
#==============================================================================


priorityList = [['a','1'],['b','2'],['c','3'],['d','4'],['e','5'],['f','6'] \
            ,['g','7'],['h','8'],['i','9'],['j','10'],['k','11'],['l','12'] \
            ,['m','13'],['n','14'],['o','15'],['p','16'],['q','17'],['r','18'] \
            ,['s','19'],['t','20'],['u','21'],['v','22'],['w','23'],['x','24'] \
            ,['y','25'],['z','26'],['A','27'],['B','28'],['C','29'],['D','30'] \
            ,['E','31'],['F','32'],['G','33'],['H','34'],['I','35'],['J','36'] \
            ,['K','37'],['L','38'],['M','39'],['N','40'],['O','41'],['P','42'] \
            ,['Q','43'],['R','44'],['S','45'],['T','46'],['U','47'],['V','48'] \
            ,['W','49'],['X','50'],['Y','51'],['Z','52']]


#==============================================================================
# Zoek letterwaardes op in voorgedefinieerde dictionary
#==============================================================================

priority = {'a':'1','b':'2','c':'3','d':'4','e':'5','f':'6' \
            ,'g':'7','h':'8','i':'9','j':'10','k':'11','l':'12' \
            ,'m':'13','n':'14','o':'15','p':'16','q':'17','r':'18' \
            ,'s':'19','t':'20','u':'21','v':'22','w':'23','x':'24' \
            ,'y':'25','z':'26','A':'27','B':'28','C':'29','D':'30' \
            ,'E':'31','F':'32','G':'33','H':'34','I':'35','J':'36' \
            ,'K':'37','L':'38','M':'39','N':'40','O':'41','P':'42' \
            ,'Q':'43','R':'44','S':'45','T':'46','U':'47','V':'48' \
            ,'W':'49','X':'50','Y':'51','Z':'52'}


    
#==============================================================================
# functie zoekDubbele
#------------------------------------------------------------------------------
# Zoek de gemeenschappelijke elementen in twee lijsten.
# Maak van elke lijst een set (verzemeling) en gebruik de 
# Python doorsnede oparator "&". 
# Het resultaat is een set met alle elementen die in beide sets voorkomen.
#==============================================================================

def zoekDubbele(lijst1, lijst2):

    waarde = set(lijst1) & set(lijst2)
    return(waarde)    



def zoekDoorsnede(lijst1, lijst2):

    resultaat=[]
    for elem in lijst1:
        if elem in lijst2:
            resultaat.append(elem)
            
    return(resultaat)    



#==============================================================================
# functie deelRugzak
#------------------------------------------------------------------------------
# Verdeel de inhoud van een inputregel (de inhoud van een rugzak als string)
# in twee gelijke stukken (alle regels hebben een even aantal tekens).
#
# De eindpositie van het eerste deel wordt gebruikt om de string in tweeën 
# te splitsen. Omdat het resultaat van een deling (door 2) het type "float"
# krijgt, moet de functie "int" worden gebruikt om hier een integer van te
# maken, wat verplicht is voor de splice van de string.
#
# De functie geeft TWEE waarden terug, dus bij aanroep beide gebruiken!
#==============================================================================


def deelRugzak(regel):

        eindPos = int(len(regel)/2) 
        linkerDeel = list(regel[0:eindPos])
        rechterDeel = list(regel[eindPos: len(regel)])
        
        return(linkerDeel, rechterDeel)

    

#==============================================================================
# functie bereken
#------------------------------------------------------------------------------
# Bereken de waarde (in de puzzel de "prioriteit") van een teken.
# De ASCII waarde van hoofdletters loopt vanaf 65, die van de kleine letters
# is 32 groter. In de puzzel moeten echter de kleine letters juist de waarden
# vanaf 1 krijgen en de hoofdletters een waarde die 26 groter is.
# Vandaar de correcties. 
# (Probeer het uit: "A" (65) moet 27 worden en "a" (97) moet 1 worden).
#==============================================================================
 

def bereken(item):
    
        tekenlijst=list(item)   
        teken=tekenlijst[0]
        prioriteit=ord(teken) - 64
        if prioriteit > 26:
            prioriteit -= 32
        else:
            prioriteit += 26
        return prioriteit     



#==============================================================================
# Hoofdprogramma
#==============================================================================


totaal=0

for line in file:
    
        regel=line.strip('\n')
        linkerDeel, rechterDeel = deelRugzak(regel)

        item = zoekDoorsnede(linkerDeel, rechterDeel)
 #       item = zoekDubbele(linkerDeel, rechterDeel)
 
 
#==============================================================================
# Bereken letterwaardes met functie op basis van ASCII code
#==============================================================================

        # prioriteit = bereken(item)
 
#==============================================================================
# Zoek letterwaardes op in voorgedefinieerde lijst
#==============================================================================
        
        # for paar in priorityList:
        #     if item[0] == paar[0]:
        #         totaal+=int(paar[1])


#==============================================================================
# Zoek letterwaardes op in voorgedefinieerde dictionary
#==============================================================================

        totaal += int(priority[item[0]])


print("Totaal: ", totaal)        
