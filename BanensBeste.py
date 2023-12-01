import matplotlib.pyplot as plt
kamper = 'matches.csv'



def BanensBestePlot(*Aar):
    Aar = list(Aar)
    Aar = sorted(Aar)
    antall = Aar[-1] - Aar[0]
    for i in range(1,antall):
        ar = Aar[0] + i
        Aar.append(ar)
    Aar = sorted(Aar)
    liste = []
    liste2 = []
    for x in ordbok[str(Aar[0])]['Banens beste'].items():
        liste.append([x[0], x[1]])
        liste2.append(x[0]) 
    
    for i in range(len(Aar)-1):
        for y in ordbok[str(Aar[i+1])]['Banens beste'].items():
            if y[0] in liste2:
                liste[liste2.index(y[0])][1] += y[1]
            else:
                liste.append([y[0], y[1]])
                liste2.append(y[0])
    
    for a in liste2:
        if liste2.count(a) > 1:
            print('Flere enn en')
                  
    liste = sorted(liste, key=lambda x: -x[-1])
    a = liste[10][-1]
    b = sum(x[-1] == a for x in liste)
    c = sum(x[-1] == a for x in liste[:10])
       
    
    plt.subplots(1,1, figsize = (6, 8))
    plt.table(cellText=liste[:10], loc = 'center', bbox=[0, 0, 1, 1])
    plt.axis('off')
    plt.title('De 10 spillerne med flest banens beste kåringer fra ' + str(Aar[0]) + " til " + str(Aar[-1]))
    if b-c == 1:
        plt.text(0, -0.04, 'Det er en spiller til med ' + str(a) + ' kåringer.')
        plt.text(0, -0.08, 'Totalt blir ' + str(len(liste)) + ' spillere kåret til banens beste.')
    elif b-c > 1:
        plt.text(0, -0.04, 'Det er ' + str(b-c) + ' flere spillere med ' + str(a) + ' kåringer.')
        plt.text(0, -0.08, 'Totalt blir ' + str(len(liste)) + ' spillere kåret til banens beste.')
    else:
        plt.text(0, -0.08, 'Totalt blir ' + str(len(liste)) + ' spillere kåret til banens beste.')
    



with open(kamper) as fil:
    x = fil.readline()
    x = x.split(',')
    ordbok = {}
    BanensBeste = x.index('player_of_match')
    for x in fil:
        x = x.split(',')
        try:
            ordbok[x[1]]['AntallKamper'] += 1
        except:
            ordbok[x[1]] = {}
            ordbok[x[1]]['Aar'] = x[1]
            ordbok[x[1]]['AntallKamper'] = 1
           
            ordbok[x[1]]['Banens beste'] = {}
        try:
            if not x[BanensBeste] == '':
                ordbok[x[1]]['Banens beste'][x[BanensBeste]] += 1
        except:
            if not x[BanensBeste] == '':
                ordbok[x[1]]['Banens beste'][x[BanensBeste]] = 1
    
                
BanensBestePlot(2008, 2017)

