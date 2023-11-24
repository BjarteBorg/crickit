kamper = matches.csv

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
