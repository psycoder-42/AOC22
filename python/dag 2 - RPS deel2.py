file = open('/Users/mavo/documents/Advent of Code/python/dag 2 - input RPS.txt', 'r')

# ----------
# Constanten
# ----------

# Codering voor verlies, gelijkspel en winst met punten

VERLIES=["X",0]
GELIJK=["Y",3]
WIN =["Z",6]


# Puntenwaardering voor eigen zetten

ZETWAARDEN = [["A",1],["B",2],["C",3]]


# Mogelijke zetcombinaties per spelresultaat
              
VERLIES_COMBINATIES = [["A","C"],["B","A"],["C","B"]]
GELIJK_COMBINATIES = [["A","A"],["B","B"],["C","C"]]
WIN_COMBINATIES = [["A","B"],["B","C"],["C","A"]]



# --------
# Functies
# --------

def bepaalEigenZet(tegenZet, uitslag):
    
    if uitslag == VERLIES[0]:
        for paar in VERLIES_COMBINATIES:
            if tegenZet == paar[0]:
               eigenZet = paar[1] 
 
    if uitslag == GELIJK[0]:
        for paar in GELIJK_COMBINATIES:
            if tegenZet == paar[0]:
               eigenZet = paar[1] 

    if uitslag == WIN[0]:
        for paar in WIN_COMBINATIES:
            if tegenZet == paar[0]:
               eigenZet = paar[1] 
               
    return eigenZet



def bereken(zet1, uitslag):

    for paar in ZETWAARDEN:
        if zet1 == paar[0]:
           punten = paar[1] 

    if uitslag == GELIJK[0]:
        punten += GELIJK[1]           
        
    if uitslag == WIN[0]:
        punten += WIN[1]           
        
    return punten
 
    
# --------------
# Hoofdprogramma
# --------------
       
score=0

for regel in file:
    zet=regel[0]         # "zet" is de zet van de tegenstander
    uitslag =regel[2]    # 'uitslag is de gewenste uitslag
    
    eigenZet = bepaalEigenZet(zet, uitslag)
       
    score=score + bereken(eigenZet,uitslag)
    
print (score)    
    
