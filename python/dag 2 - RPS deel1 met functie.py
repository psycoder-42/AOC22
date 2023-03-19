file = open('/Users/mavo/documents/Advent of Code/python/Dag 2/dag 2 - input.txt', 'r')
score=0

def bereken(zet1, zet2):
    ronde = 0
    if zet1=="A":
        if zet2== "Y": ronde=6+2
        if zet2== "X": ronde=3+1
        if zet2== "Z": ronde=0+3
        
    if zet1=="B":
        if zet2== "Z": ronde=6+3
        if zet2== "Y": ronde=3+2
        if zet2== "X": ronde=0+1
    
    if zet1=="C":
        if zet2== "X": ronde=6+1
        if zet2== "Z": ronde=3+3
        if zet2== "Y": ronde=0+2
     

    return ronde
     
       

for regel in file:
    tegenzet=regel[0]
    eigenzet=regel[2]        
    score=score + bereken(tegenzet,eigenzet)
    
print (score)    
    
    
        