file = open('/Users/mavo/documents/Advent of Code/python/Dag 2/dag 2 - input.txt', 'r')

#==============================================================================
# Berekening van de rondepunten in een class i.p.v. een functie.
#------------------------------------------------------------------------------
#
# Er wordt een class gemaakt voor een spelronde, bestaande uit een zet van
# de tegenstander en een eigen zet. Deze zetten zijn de parameters van de 
# class.
#
# De class heeft een functie "punten" waarin op basis van de beide zetten de
# punten worden berekend die de ronde oplevert.
# Deze functie is dan een method van de class, die in het programma kan 
# worden aangeroepen met de "dot operator" bij een object van de class.
#==============================================================================


class ronde:
    
    def __init__(self, tegenZet, eigenZet):
        self.tegen=tegenZet
        self.eigen=eigenZet
        
        
    def punten(self):
        
        if self.tegen =="A":
            if self.eigen == "Y": p=6+2
            if self.eigen == "X": p=3+1
            if self.eigen == "Z": p=0+3
            
        if self.tegen =="B":
            if self.eigen == "Z": p=6+3
            if self.eigen == "Y": p=3+2
            if self.eigen == "X": p=0+1
        
        if self.tegen =="C":
            if self.eigen == "X": p=6+1
            if self.eigen == "Z": p=3+3
            if self.eigen == "Y": p=0+2
         
        return p

        

#==============================================================================
# Hoofdprogramma
#------------------------------------------------------------------------------
#
# Maak voor elke regel in de input een object "beurt" aan van de class
# "ronde", met de beide zetten uit de inputregel als argumenten.
#
# Het aantal punten dat de combinatie van de zetten oplevert, kan nu direct
# worden opgevraagd met de method "punten" van het "beurt" object.
# Dit gebeurt in de typische object oriented syntax van de "dot operator", 
# bestaande uit de naam van het object, gevolgd door een punt en de naam van
# de gewenste method bij het object.
#==============================================================================

       
score = 0
for regel in file:
    tegenZet=regel[0]
    eigenZet=regel[2]        
    beurt = ronde(tegenZet, eigenZet)
    score += beurt.punten()
    
print (score)    
    
    
        