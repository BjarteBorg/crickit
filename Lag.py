with open('matches.csv') as fil:
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
