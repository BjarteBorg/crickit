import matplotlib.pyplot as plt
kamper = 'matches.csv'


def BanensBestePlot(Aar):
    global liste
    liste = []
    for x in ordbok[str(Aar)]['Banens beste'].keys():    
        liste.append([x, ordbok[str(Aar)]['Banens beste'][x]])
        
    liste = sorted(liste, key=lambda x: x[-1])
    liste.reverse()
    a = liste[10][-1]
    b = sum(x[-1] == a for x in liste)
    c = sum(x[-1] == a for x in liste[:10])
    
    plt.subplots(1,1, figsize = (6, 8))
    plt.table(cellText=liste[:10], loc = 'center', bbox=[0, 0, 1, 1])
    plt.axis('off')
    plt.title('De 10 spillerne med flest banens beste kåringer i ' + str(Aar))
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
    a = x.index('player_of_match')
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
            ordbok[x[1]]['Banens beste'][x[a]] += 1
        except:
            ordbok[x[1]]['Banens beste'][x[a]] = 1
