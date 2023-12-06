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

                  
    liste = sorted(liste, key=lambda x: -x[-1])
    a = liste[9][-1]
    b = sum(x[-1] == a for x in liste)
    c = sum(x[-1] == a for x in liste[:10])
       
    for i in range(10):
        q = SpillerLag(liste[i][0], [x for x in Aar])
        liste[i].append(liste[i][-1])
        p = ''
        for j in range(len(q)):
            if j == len(q)-1 and len(q) != 1:
                p += f' og {q[j]}'
            elif j != 0:
                p += f', {q[j]}'
            else:
                p += q[j]
        liste[i][1] = p
        if len(Aar) > 1:
            liste[i].append(round(liste[i][-1]/AarSpilt(liste[i][0], Aar), 3))
    

    if len(Aar) > 1:
        plt.subplots(1,1, figsize = (12, 8))
        kolonne = ['Spiller', 'Lag', 'Kåringer', 'Kåringer per aktive år']
        plt.table(cellText=liste[:10], 
                  loc = 'center', bbox=[0, 0, 1, 1], 
                  colWidths=[2, 4.5, 0.9, 1.5], 
                  colLabels=kolonne,
                  colColours=['gray', 'gray', 'gray', 'gray'],
                  cellLoc = 'left')
        plt.title('De 10 spillerne med flest banens beste kåringer fra ' + str(Aar[0]) + " til " + str(Aar[-1]), size=15)
    else:
        plt.subplots(1,1, figsize = (8, 8)) 
        kolonne = ['Spiller', 'Lag', 'Kåringer']
        plt.table(cellText=liste[:10],
                  loc = 'center', bbox=[0, 0, 1, 1],
                  colWidths=[2, 2, 0.9], 
                  colLabels=kolonne, colColours=['gray', 'gray', 'gray'], 
                  cellLoc = 'left')
        plt.title('De 10 spillerne med flest banens beste kåringer i ' + str(Aar[0]), size=15)
        
    plt.axis('off')
    if b-c == 1:
        plt.text(0, -0.04, 'Det er en spiller til med ' + str(a) + ' kåringer.')
        plt.text(0, -0.08, 'Totalt blir ' + str(len(liste)) + ' spillere kåret til banens beste.')
    elif b-c > 1:
        plt.text(0, -0.04, 'Det er ' + str(b-c) + ' flere spillere med ' + str(a) + ' kåringer.')
        plt.text(0, -0.08, 'Totalt blir ' + str(len(liste)) + ' spillere kåret til banens beste.')
    else:
        plt.text(0, -0.08, 'Totalt blir ' + str(len(liste)) + ' spillere kåret til banens beste.')
   
    
def SpillerLag(spiller, Aar):
    liste = []
    for x in Aar:
        for y in lag[str(x)].items():
            if spiller in y[1]:
                liste.append(y[0])
    
    liste2 = []
    for x in liste:
        if x == 'Rising Pune Supergiants' and 'Rising Pune Supergiant' in liste:
            continue
        if x not in liste2:
            liste2.append(x)
    return liste2


def AarSpilt(Spiller, Aar):
    antall = 0
    try:
        for x in Aar:
            x = str(x)
            for y in lag[x].values():
                if Spiller in y:
                    antall += 1
    except:
        Aar = str(Aar)
        for x in lag[Aar].values():
            if Spiller in x:
                antall += 1
                
    return antall


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
    
    
with open(kamper) as fil:
    x = fil.readline()
    x = x.rstrip().split(',')
    season = x.index('season')
    kamp = x.index('id')
    kamp_id = {}
    for x in fil:
        x = x.rstrip().split(',')
        try:
            kamp_id[x[season]].append(int(x[kamp]))
        except:
            kamp_id[x[season]] = []
            kamp_id[x[season]].append(int(x[kamp]))
            

with open('deliveries.csv') as fil:
    x = fil.readline().split(',')
    lag = {}
    
    lag1 = x.index('batting_team')
    lag2 = x.index('bowling_team')
    batsman = x.index('batsman')
    bowler = x.index('bowler')
    non_striker = x.index('non_striker')
    fielder = x.index('fielder\n')
    kamp = x.index('match_id')
    
    for y in kamp_id.keys():
        lag[y] = {}
    for x in fil:
        x = x.rstrip().split(',')
        for y in kamp_id.items():
            if int(x[kamp]) in y[1]:
                aar = y[0]
                break
        try:
            if not x[bowler] in lag[aar][x[lag2]]:
                lag[aar][x[lag2]].append(x[bowler])
            if not x[batsman] in lag[aar][x[lag1]]:
                lag[aar][x[lag1]].append(x[batsman])
            if not x[non_striker] in lag[aar][x[lag1]]:
                lag[aar][x[lag1]].append(x[non_striker])
                
            if x[fielder] and x[fielder] not in lag[aar][x[lag2]]:
                if x[fielder].find('(sub)'):    
                    if x[fielder][:x[fielder].find('(sub)')-1] in lag[aar][x[lag2]]:
                        continue
                    x[fielder] = x[fielder][:x[fielder].find('(sub)')-1]
                lag[aar][x[lag2]].append(x[fielder])
                
        except:
            lag[aar][x[lag1]] = []
            lag[aar][x[lag2]] = []
            lag[aar][x[lag2]].append(x[bowler])
            lag[aar][x[lag1]].append(x[batsman])
            lag[aar][x[lag1]].append(x[non_striker])
            if x[fielder]:
                if x[fielder].find('(sub)') >= 0:
                    x[fielder] = x[fielder][:x[fielder].find('(sub)')-1]
                lag[aar][x[lag2]].append(x[fielder])
            
            
BanensBestePlot(2008)
