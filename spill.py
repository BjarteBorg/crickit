kamper = 'matches.csv'
import random as r

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
                

def start():
    Aar = [2008 + i for i in range(10)]
    print(Aar)
    while True:
        try:
            a = input('Sett inn året/årene du vil spille:').split()
            for i in range(len(a)):
                a[i] = int(a[i])
                if a[i] not in Aar:
                    int('a')
            break
        except:
            a = 0
    
    poeng = 0
    liste = spillere(a)
    tall = int(r.random()*len(liste))
    runde(liste[tall][0], liste[tall][1], poeng, liste)
    

def runde(spiller, spillertall, poeng, liste):
    print('\n' + '*************************************')
    print('Poeng: ' + str(poeng))
    print('Hvem har vunnet banens beste flest ganger?')
    print('1. ' + spiller + '   Kåringer: ' + str(spillertall))
    tekst = '2. '
    while True:
        tall = int(r.random()*len(liste))
        if liste[tall][1] == spillertall:
            continue
        else:
            tekst += str(liste[tall][0])
            if liste[tall][1] > spillertall:
                a = True
            else:
                a = False
            break
        
    print(tekst, end='\n\n')
    
    while True:
        try:
            b = input('Hvilken spiller har flest kåringer?')
            b = int(b)
            break
        except:
            b = 0
    
    if b == 2 and a:
        poeng += 1
        runde(liste[tall][0], liste[tall][1], poeng, liste)
    elif b == 1 and not a:
        poeng += 1
        runde(liste[tall][0], liste[tall][1], poeng, liste)
    else:
        ferdig(liste[tall][0], liste[tall][1], poeng)
        

def ferdig(spiller, spillertall, poeng):
    print('\n' + '*************************************')
    print('Det var feil.')
    print(spiller, 'fikk', spillertall, 'kåringer.')
    print('Du fikk ' + str(poeng) + ' poeng')
     
    
    

def spillere(a):
    spillere = {}
    for x in a:
        for y in ordbok[str(x)]['Banens beste'].items():
            try:
                spillere[y[0]] += y[1]
            except:
                spillere[y[0]] = y[1]
    
    liste = []
    for x in spillere.items():
        liste.append([x[0], x[1]])
        
    return liste
            
start()
