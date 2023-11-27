with open('deliveries.csv') as fil:
    x = fil.readline().rstrip().split(',')
    
    kamp = x.index('match_id')
    runs = {'total_runs': x.index('total_runs'),
            'wide_runs': x.index('wide_runs'),
            'bye_runs': x.index('bye_runs'),
            'legbye_runs': x.index('legbye_runs'),
            'noball_runs': x.index('noball_runs'),
            'penalty_runs': x.index('penalty_runs'),
            'batsman_runs': x.index('batsman_runs'),
            'extra_runs': x.index('extra_runs')}
    dismissal = x.index('dismissal_kind')
    dismissed_player = x.index('player_dismissed')
    fielder = x.index('fielder')
    lag1 = x.index('batting_team')
    lag2 = x.index('bowling_team')
    
    kamper = {}
    a = []
    
    for x in fil:
        x = x.rstrip().split(',')
        if x[0] != '1':
            continue
        if not x[kamp] in a:
            kamper[x[kamp]] = {x[lag1]:{'wickets': 0, 'total_runs':0}, 
                               x[lag2]:{'wickets': 0, 'total_runs':0}}
            a.append(x[kamp])
        if x[dismissal]:
            print(x[dismissal])
            if x[fielder] and x[fielder].find('(sub)'):
                x[fielder] = x[fielder][:x[fielder].find(' (sub)')]
            try:
                kamper[x[kamp]][x[lag2]][x[dismissal]][x[fielder]] += 1
                kamper[x[kamp]][x[lag2]]['wickets'] += 1
            except:
                try:
                    kamper[x[kamp]][x[lag2]][x[dismissal]][x[fielder]] = 1
                except:
                    kamper[x[kamp]][x[lag2]][x[dismissal]] = {}
                    kamper[x[kamp]][x[lag2]][x[dismissal]][x[fielder]] = 1
                kamper[x[kamp]][x[lag2]]['wickets'] += 1
                
