import random
import logging

#definicja funkcji rekurencyjnej do zgadywanki
def zgaduj(proba,liczba):
    traf = int(input("Podaj proszę losową liczbę z przedziału od 1 do 99: "))
    proba+=1
    if traf == liczba:
        print("Gratulacje! odgadłeś magiczną liczbę !")
        return traf
    elif traf > liczba:
        print("ZA DUŻO")
    elif traf < liczba:
        print("ZA MAŁO")
    if proba == 5: 
        print("Niestety przegrywasz ! Limit 5 prob wyczerpany !")
        traf = liczba 
        return traf 
    return zgaduj(proba,liczba)


def dzielReszta(reszta):
    reszta = reszta/2
    return round(reszta)

def dodaj(traf, reszta):
    traf = traf + reszta
    return traf

def odejmij(traf, reszta):
    traf = traf - reszta
    return traf

def losuj(start,stop):
    if start == 1: 
        stop-=1
    elif stop == 99:
        start+=1
    else:
        start+=1
        stop-=1
    liczba = random.randint(start,stop)
    return liczba


#patent nieustannego dzielenia przedzialu na pol
def zgadujKomp(proba,liczba,pocz,koniec,trafy,reszty,l_zgad):
    if proba is 0: 
        trafy.append(round(koniec/2))
        reszty.append(trafy[-1])
    #tutaj musi byc if else
    
    #reszta = dzielReszta(reszty[-1])
    reszta = round(reszty[-1]/2)
    reszty.pop()
    reszty.append(reszta)    
    
    if trafy[-1] < liczba:
        pocz = trafy[-1]
        l_zgad = dodaj(trafy[-1],reszty[-1])
        trafy.append(l_zgad) 
    elif trafy[-1] > liczba:
        koniec = trafy[-1]
        l_zgad = odejmij(trafy[-1],reszty[-1])
        trafy.append(l_zgad)

    logging.warning(trafy)
    logging.warning(reszty)
    if proba is 4:
        traf = losuj(pocz,koniec)
        return traf
    
    if liczba is trafy[-1]:
        return trafy[-1]    
    proba+=1
    return zgadujKomp(proba,liczba,pocz,koniec,trafy,reszty,l_zgad)


##wlasciwy kod zgadwanki
w = int(input("Wybierz: 1. Aby pokonac komputer\n2. Aby sprawdzic komputer\n"))
s1 = []
s2 = []
if w is 1:
    #losowanie liczby przez komputer
    losowa_liczba = random.randint(1,99)
    wynik = zgaduj(0,losowa_liczba)
    print("Wylosowana liczba to {}".format(str(wynik)))
elif w is 2:
    l = int(input("Proszę podaj liczbę z przedziału od 1 do 99: "))
    wynik = zgadujKomp(0,l,1,99,s1,s2,0)
    print("Wylosowana liczba to {}, podana liczba to {}".format(str(wynik),str(l)))